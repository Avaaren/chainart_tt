import sys
from datetime import datetime

def time_decorator(func):
    # Simple decorator for time benchmark
    def wrapper(filename):
        start = datetime.now()
        func(filename)
        stop = datetime.now() - start
        print(f'Выполнено за {stop}')
    return wrapper

@time_decorator
def decrypt(filename):
    # Try open file with entered name
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    # If file not found -> stoping script
    except(FileNotFoundError):
        print('File not found')
        sys.exit()
    # If file has more then 100k chars -> exit
    if len(text) > 100000:
        print('File too long')
        sys.exit()
    # String is immutable -> convert it to list
    text = [text[i] for i in range(len(text))]
    i = 0
    # Run cycle to check string with i-counter
    while i < (len(text)-1):
        # If 2 neigboring chars are equal -> pop them
        if (text[i] == text[i+1]):
            text.pop(i)
            text.pop(i)
            continue
        # Otherwise mark char as checked and go to next
        else:
            i+=1
    # In the end convert result list to string
    text = ''.join(text)
    print (f'decrypted message: {text}')

if __name__ == '__main__':
    # Check command line args
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print('Аргументы запуска введены некорректно')
        sys.exit()
    # Call decrypt function
    decrypt(sys.argv[1])



