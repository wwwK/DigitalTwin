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

def lwlr(testPoint,xArr,yArr,k=1.0):
    xMat=np.mat(xArr)
    yMat=np.mat(yArr).T
    m=np.shape(xMat)[0]
    w=np.mat(np.eye(m))
    for i in range(m):
        diff=testPoint-xMat[i,:]
        w[i,i]=np.exp(diff*diff.T/(-2.0*k**2))
    xTwx=xMat.T*w*xMat
    if np.linalg.det(xTwx)==0:
        print('矩阵不可逆')
        return
    ws=xTwx.I*xMat.T*w*yMat
    return testPoint*ws

def lwlrTest(testArr,xArr,yArr,k=1.0):
    m=np.shape(testArr)[0]
    yHat=np.zeros(m)
    for i in range(m):
        yHat[i]=lwlr(testArr[i],xArr,yArr,k)
    return yHat

def rssError(yArr,yHat):
    return ((yArr-yHat)**2).sum()


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

def test3():
    abX, abY = loadData('../data/abalone.txt')
    print('训练集与测试集相同:局部加权线性回归,核k的大小对预测的影响:')
    yHat01 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 0.1)
    yHat1 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 1)
    yHat10 = lwlrTest(abX[0:99], abX[0:99], abY[0:99], 10)
    print('k=0.1时,误差大小为:',rssError(abY[0:99], yHat01.T))
    print('k=1  时,误差大小为:',rssError(abY[0:99], yHat1.T))
    print('k=10 时,误差大小为:',rssError(abY[0:99], yHat10.T))
    print('')
    print('训练集与测试集不同:局部加权线性回归,核k的大小是越小越好吗？更换数据集,测试结果如下:')
    yHat01 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 0.1)
    yHat1 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 1)
    yHat10 = lwlrTest(abX[100:199], abX[0:99], abY[0:99], 10)
    print('k=0.1时,误差大小为:',rssError(abY[100:199], yHat01.T))
    print('k=1  时,误差大小为:',rssError(abY[100:199], yHat1.T))
    print('k=10 时,误差大小为:',rssError(abY[100:199], yHat10.T))
    print('')
    print('训练集与测试集不同:简单的线性归回与k=1时的局部加权线性回归对比:')
    print('k=1时,误差大小为:', rssError(abY[100:199], yHat1.T))
    ws = standRegression(abX[0:99], abY[0:99])
    yHat = np.mat(abX[100:199]) * ws
    print('简单的线性回归误差大小:', rssError(abY[100:199], yHat.T.A))

if __name__ == '__main__':
    # print(np.eye(5))
    # # test3()
    test3()