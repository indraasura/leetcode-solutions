hashmap = []
def check_uniqueness(string):
    for i in string:
        if i in hashmap: 
            return False
        hashmap.append(i)
    return True

string = input('Enter string: ')
if check_uniqueness(string):
    print('Unique')
else: 
    print('Not unique')