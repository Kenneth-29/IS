import os
print(os.getcwd())
print(os.listdir())
os.chdir('C:\\Users\\kenne\\PycharmProjects\\IS\\testing_images')
with open('1.txt', 'r') as f:
    data = f.read()
print(data)
with open('1.txt', 'w') as f:
    data = 'This is fantastic, Python \n Programing is really fun'
    f.write(data)
with open('1.txt', 'r') as f:
    data = f.read()
print(data)