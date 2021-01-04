import matplotlib.pyplot as plt
import numpy as np


def loadData(dataPath):
    x=[]
    y=[]
    numFeat=len(open(dataPath,'r').readline().strip().split('\t'))-1
    with open(dataPath,'r') as fr:
        for line in fr.readlines():
            dataLine=line.strip().split('\t')
            lineArr=[]
            for i in range(numFeat):
                lineArr.append(float(dataLine[i]))
            x.append(lineArr)
            y.append(float(dataLine[-1]))

    return x,y

def standRegression(x,y):
    xMat=np.mat(x)
    yMat=np.mat(y).T
    xTx=xMat.T*xMat
    if np.linalg.det(xTx)==0:
        print('矩阵不可逆')
        return
    return xTx.I*xMat.T*yMat

def test1():
    dataPath = '../data/ex0.txt'
    x, y = loadData(dataPath)
    print(x)
    print(y)

def test2():
    dataPath = '../data/ex0.txt'
    x, y = loadData(dataPath)
    w=standRegression(x,y)
    print(w)
    yHat=np.mat(x)*w
    # print(yHat)
    # print(np.mat(y).T)
    print(np.corrcoef(yHat.T,np.mat(y)))

if __name__ == '__main__':
    test2()