import random
'''
def machinePrecision(f=float):
    machine=f(1)
    while f(1)+f(machine)!=f(1):
        new_machine=machine
        machine=f(machine)/f(2)
    return new_machine

print("before:",abs(3.0*(4.0/3.0-1)-1))
print("after:",abs(3.0*(4.0/3.0-1)-1)-machinePrecision())
'''




def unit_matrix(n):
    result = []
    temp = []
    for i in range(n):
        for j in range(n):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        result.append(temp)
        temp = []
    return result

def createMatrix():
    x=[]
    y=[]
    rows=int(input("enter the size rows matrix:"))
    cols=int(input("enter the size cols matrix:"))
    for i in range(rows):
        for j in range(cols):
            num=int(input("enter number:"))
            y.append(num)
        x.append(y)
        y=[]
    return x

def createVector():
    x = []
    y = []
    rows = int(input("enter the size rows matrix:"))
    cols = 1
    for i in range(rows):
        for j in range(cols):
            num = int(input("enter number:"))
            y.append(num)
        x.append(y)
        y = []
    return x


def multiplymatrix(x,y):
    result = []
    temp = []
    for i in range(len(x)):
        for i in range(len(y[0])):
            temp.append(0)
        result.append(temp)
        temp = []

    # iterate through rows of X
    for i in range(len(x)):
   # iterate through columns of Y
        for j in range(len(y[0])):
       # iterate through rows of Y
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    return result
def maxMatrix(M,V):
    for i in range(len(M)):
        temp=[]
        for j in range(len(M)):
            if i<=j:
                temp.append(abs(M[j][i]))
        x=max(temp)

        p=temp.index(x)+i
        k=unit_matrix(len(M))
        k[p],k[i]=k[i],k[p]
        M=multiplymatrix(k,M)
        V=multiplymatrix(k,V)
    return M,V



def ChangeMatrix(x, vectorB):
    x,vectorB=maxMatrix(x,vectorB)
    #print("after max x=",x,"after max b=",  vectorB)
    z = 1
    while z == 1:
        z = 0
        for i in range(len(x)):
            for j in range(len(x)):
                if i == j and x[i][j] == 0:
                    for y in range(len(x)):
                        if x[y][j] != 0:
                            k = unit_matrix(len(x))  # change i with y
                            k[i], k[y] = k[y], k[i]
                            old=x
                            x = multiplymatrix(k, x)
                            vectorB=multiplymatrix(k, vectorB)
                            printAsMatrix(x, vectorB, k,old)
                            z = 1
                            break
#no zero
    for i in range(len(x)):
        for j in range(len(x)):
            if i==j:
                y=unit_matrix(len(x))
                y[i][j]=(1/x[i][j])
                oldMatrix = x
                vectorB=multiplymatrix(y, vectorB)
                x=multiplymatrix(y,x)#after the change pivot is 1
                #printAsMatrix(x, vectorB, y,oldMatrix)
            else:
                y=unit_matrix(len(x))
                y[j][i]=(x[j][i]/x[i][i])*(-1)
                oldMatrix=x
                vectorB = multiplymatrix(y, vectorB)
                x=multiplymatrix(y,x)
                #printAsMatrix(x, vectorB, y, oldMatrix)
    return vectorB



def printAsMatrix(x,b,k,old):
    with open("file5.txt", 'a') as f:
        for i in range(len(x)):
            print("E-->",k[i],"old-->",old[i],"= A-->",x[i],"b->",b[i])
            f.write("E-->"+ str(k[i])+ "\t\told A-->"+ str(old[i])+ "\t\t= A after the change-->"+ str(x[i])+ "\t\tthe vector b ->"+ str(b[i]))
            f.write("\n")
        f.write("----------------------------------------------------------------------------------------------------------------\n")
        print("-----------------------")

def Rand():
    lin = 209487370
    tal = 316261353
    yuval = 207059544
    x =[tal,lin,yuval]
    y=random.choice(x)
    return int(y%12)+19









x=[[2, 0, 0,0], [0.6666666, 2, 0.333333333,0], [0, 0.25, 2,0.75],[0,0,0,2]]
b=[[0],[-1.2489254],[-2.398637],[0]]
#f=open("file5.txt",'w')
#f.close()
#printAsMatrix(x,b,unit_matrix(3),x)
print(ChangeMatrix(x,b),"the v")

#print(Rand())

