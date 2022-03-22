
try:
    file = open('a_file.txt')
except FileNotFoundError:
    # print("There was an error")
    file = open('a_file.txt', 'w')
    file.write("Something")

try:
    file = open('a_file.txt')
    a_dctionary = {'key':'value'}
    print(a_dctionary['adasd'])
except FileNotFoundError:
    # print("There was an error")
    file = open('a_file.txt', 'w')
    file.write("Something")

try:
    a_dctionary = {'key':'value'}
    print(a_dctionary['adasd'])
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    raise KeyError