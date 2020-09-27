def hello():
    print("Hello world!")
def do_operations(num1, num2):
    s = num1+num2
    sub = num1-num2
    d = num1/num2
    r = num1%num2
    m = num1*num2
    ex = num1**num2
    return s,sub,d,r,m,ex # returns a tuple

def multiplicationLineColumn(line,column):
    try:
        sizeLine= len(line)
        sizeColumn = len(column)
        if(sizeLine!=sizeColumn):
            raise ValueError("Exception")
        res = sum([line[i] * column[i] for i in range(sizeLine)])
        return res
    except ValueError:
        print("Should have the sam len line & column")

def getColumn(matrix, numColumn):
    size = len(matrix)
    column = [matrix[i][numColumn] for i in range(size)]
    return column

def getLine(matrix, numLine):
    line = matrix[numLine]
    return line
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]
matrix = []
for i in range(len(A)):
    matrix.append([])
    for j in range(len(B)):
        matrix[i].append(multiplicationLineColumn(getLine(A,i), getColumn(B,j)))
    print(matrix)
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

d = do_operations(num1, num2)
print('The following is the results of applying ops on %d and %d'%(num1, num2))
print('The result are of addition, subtraction, division, remainder, multiplication and exponent')
for i in d:
    print(i)
#print()
print(hello())
print(matrix)