import numpy as np
import matplotlib.pyplot as plt


def loadData():
    datMat=np.array(
        [[1., 2.1],
         [1.5, 1.6],
         [1.3, 1.],
         [1., 1.],
         [2., 1.]]
    )
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLabels

def loadDataSet(fileName):
    numFeat=len(open(fileName).readline().strip().split('\t'))
    dataMat = [];
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat - 1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


def showData(dataMat,labelMat):
    fig,axs=plt.subplots(1,1)
    data_plus=[]
    data_mins=[]
    for i in range(len(labelMat)):
        if labelMat[i]==1:
            data_plus.append(dataMat[i])
        else:
            data_mins.append(dataMat[i])

    axs.scatter(np.array(data_plus).T[0],np.array(data_plus).T[1],color='red')
    axs.scatter(np.array(data_mins).T[0],np.array(data_mins).T[1],color='green')
    plt.show()


"""
Parameters:
    dataMatrix - 数据矩阵
    dimen - 第dimen列，也就是第几个特征
    threshVal - 阈值
    threshIneq - 标志
Returns:
    retArray - 分类结果
"""
# 单层决策树分类函数
def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray = np.ones((np.shape(dataMatrix)[0],1))         #初始化retArray为1
    if threshIneq == 'lt':
        retArray[dataMatrix[:,dimen] <= threshVal] = -1.0   #如果小于阈值,则赋值为-1
    else:
        retArray[dataMatrix[:,dimen] > threshVal] = -1.0    #如果大于阈值,则赋值为-1
    return retArray

"""
Parameters:
    dataArr - 数据矩阵
    classLabels - 数据标签
    D - 样本权重
Returns:
    bestStump - 最佳单层决策树信息
    minError - 最小误差
    bestClasEst - 最佳的分类结果
"""
# 找到数据集上最佳的单层决策树
def buildStump(dataArr,classLabels,D):
    dataMatrix = np.mat(dataArr); labelMat = np.mat(classLabels).T
    m,n = np.shape(dataMatrix)
    numSteps = 10.0; bestStump = {}; bestClasEst = np.mat(np.zeros((m,1)))
    minError = float('inf')                                                     #最小误差初始化为正无穷大
    for i in range(n):                                                          #遍历所有特征
        rangeMin = dataMatrix[:,i].min(); rangeMax = dataMatrix[:,i].max()      #找到特征中最小的值和最大值
        stepSize = (rangeMax - rangeMin) / numSteps                             #计算步长
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']: # 确定好阈值后，还要确定一下大于、小于阈值的是哪一类                                       #大于和小于的情况，均遍历。lt:less than，gt:greater than
                threshVal = (rangeMin + float(j) * stepSize)                    #计算阈值
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)#计算分类结果
                errArr = np.mat(np.ones((m,1)))                                 #初始化误差矩阵
                errArr[predictedVals == labelMat] = 0                           #分类正确的,赋值为0
                weightedError = D.T * errArr                                    #计算误差
                # print("split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (i, threshVal, inequal, weightedError))
                if weightedError < minError:                                    #找到误差最小的分类方式
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump,minError,bestClasEst


# aggClassEst是adaboost的总 权重错误率之和，当所有的权重加和大于0，被分为1，否则为-1
def adaBoostTrain(dataArr,classLabels,numIt=40):
    weakClassArr=[]
    m=np.shape(dataArr)[0]
    D=np.ones((m,1))/m
    # print(D)
    aggClassEst=np.zeros((m,1))
    for i in range(numIt):
        bestStump,error,classEst=buildStump(dataArr,classLabels,D)

        alpha=float(0.5*np.log((1-error)/ max(error, 1e-16)))
        bestStump['alpha']=alpha
        weakClassArr.append(bestStump)
        # print(classEst)
        # print(np.multiply(-1*alpha,classEst))
        # print(classLabels)
        # print(np.array(classLabels))
        expon=np.multiply(np.multiply(-1*alpha,classEst),np.mat(classLabels).T)
        # print(expon)
        D=np.multiply(D,np.exp(expon))
        D=D/D.sum()

        # print(alpha*classEst)
        # print(np.multiply(alpha,classEst))
        aggClassEst+=np.multiply(alpha,classEst)
        # print(aggClassEst)
        aggErrors=np.multiply(np.sign(aggClassEst)!=np.mat(classLabels).T,np.ones((m,1)))
        # print(aggErrors)
        errorRate=aggErrors.sum()/m
        # print("errorRate:%f"%(errorRate))
        if errorRate==0.0:
            break
    return weakClassArr,aggClassEst

def adaClassify(dataToClass,classifierArr):
    dataMatrix=np.mat(dataToClass)
    m=np.shape(dataMatrix)[0]
    aggClassEst=np.zeros((m,1))
    for classify in classifierArr:
        classEst=stumpClassify(dataMatrix,classify['dim'],classify['thresh'],classify['ineq'])
        aggClassEst+=classify['alpha']*classEst
        # print(aggClassEst)
    return np.sign(aggClassEst)


def myTest0():
    dataMat, label = loadData()
    # showData(dataMat,label)
    D = np.ones((5, 1)) / 5
    bestStump, minError, bestClasEst = buildStump(dataMat, label, D)
    print('bestStump:\n', bestStump)
    print('minError:\n', minError)
    print('bestClasEst:\n', bestClasEst)
def myTest1():
    dataArr, classLabels = loadData()
    weakClassArr, aggClassEst = adaBoostTrain(dataArr, classLabels)
    print(weakClassArr)
    print(aggClassEst)

def myTest2():
    dataArr, classLabels = loadData()
    weakClassArr, aggClassEst = adaBoostTrain(dataArr, classLabels)
    print(adaClassify([[0, 0], [5, 5]], weakClassArr))
def myTest3():
    dataArr,labelArr=loadDataSet('../data/horseColicTraining2.txt')
    weakClassArr,aggClassEst=adaBoostTrain(dataArr,labelArr,40)
    print(weakClassArr)
    testMat,testLabel=loadDataSet('../data/horseColicTest2.txt')
    trainPredictLabel=adaClassify(dataArr,weakClassArr)
    testPredictLabel=adaClassify(testMat,weakClassArr)

    trainErrMat=np.ones((len(dataArr),1))
    testErrMat=np.ones((len(testMat),1))
    # print(np.shape(np.mat(labelArr)))
    # print(np.mat(labelArr))
    # print(np.shape(trainPredictLabel))
    # print(trainPredictLabel)
    print('训练集的错误率：%f'%(float(trainErrMat[np.mat(labelArr).T!=trainPredictLabel].sum()/len(labelArr))))
    # print(testPredictLabel!=1)
    print('测试集的错误率：%f'%(float(testErrMat[np.mat(testLabel).T!=testPredictLabel].sum())/len(testLabel)))


if __name__=='__main__':
    myTest3()