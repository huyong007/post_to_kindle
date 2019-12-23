filename = 'AliceinWonderland.txt'

try:
    with open('book/'+filename) as book:
        contents = book.read()
except FileNotFoundError as identifier:
    msg = 'Sorry,the filename not exist'
    print(msg)
else:
    words = contents.split()
    print('then file'+filename+'has about ' +str(len(words))+'words.')
