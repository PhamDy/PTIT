list_demo = []
print(type(list_demo))
print(len(list_demo))
list_demo.append('Red')
list_demo.append('Blue')
list_demo.append('Yellow')
print(list_demo)
print(len(list_demo))

list_demo[1] = 'Orange'
print(list_demo)

list_demo.insert(0, 'White')
print(list_demo)

del list_demo[1]
print(list_demo)