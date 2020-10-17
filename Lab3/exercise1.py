import os
print(os.getcwd())
print(os.listdir())
new1 = "My name is Kenneth-29 \n I am studying Computer Systems Engineeering in BAC\n"
os.chdir('C:\\Users\\kenne\\PycharmProjects\\IS\\testing_images')
with open('1.txt', 'a') as f:
    data = f.write('\n')
    data = f.write(new1)
print(data)

with open('1.txt', 'r') as f:
    data = f.read()
print(data)

filenames = ['file1.txt', 'file2.txt']
with open('blank.txt', 'w') as output:
    for filename in filenames:
        with open(filename) as infile:
            contents = infile.read()
            output.write(contents)
