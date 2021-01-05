import matplotlib.pyplot as plt
import numpy as np
import matplotlib


# 加载数据
def loadDataSet(fileName,xNum):
    """
    Parameters:
        fileName - 文件名
    Returns:
        xArr - x数据集
        yArr - y数据集
    """
    xArr = []
    yArr = []
    featureName=open(fileName,encoding='utf-8').readline().split('\t')
    numFeat = len(featureName)
    fr = open(fileName)
    fr.readline()
    for line in fr.readlines():
        xLine = []
        yLine=[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            if i<xNum:
                xLine.append(float(curLine[i]))
            else:
                yLine.append(float(curLine[i]))
        xArr.append(xLine)
        yArr.append(yLine)
    print(featureName)
    return xArr, yArr


# # 绘制多条局部加权回归曲线
# def plotlwlrRegression():
#     matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
#     xArr, yArr = loadDataSet('../data/ex0.txt')  # 加载数据集
#     yHat_1 = lwlrTest(xArr, xArr, yArr, 1.0)  # 根据局部加权线性回归计算yHat
#     yHat_2 = lwlrTest(xArr, xArr, yArr, 0.01)  # 根据局部加权线性回归计算yHat
#     yHat_3 = lwlrTest(xArr, xArr, yArr, 0.003)  # 根据局部加权线性回归计算yHat
#     xMat = np.mat(xArr)  # 创建xMat矩阵
#     yMat = np.mat(yArr)  # 创建yMat矩阵
#     srtInd = xMat[:, 1].argsort(0)  # 排序，返回索引值
#     xSort = xMat[srtInd][:, 0, :]
#     fig, axs = plt.subplots(nrows=3, ncols=1, sharex=False, sharey=False, figsize=(10, 8))
#     axs[0].plot(xSort[:, 1], yHat_1[srtInd], c='red')  # 绘制回归曲线
#     axs[1].plot(xSort[:, 1], yHat_2[srtInd], c='red')  # 绘制回归曲线
#     axs[2].plot(xSort[:, 1], yHat_3[srtInd], c='red')  # 绘制回归曲线
#     axs[0].scatter(xMat[:, 1].flatten().A[0], yMat.flatten().A[0], s=20, c='blue', alpha=.5)  # 绘制样本点
#     axs[1].scatter(xMat[:, 1].flatten().A[0], yMat.flatten().A[0], s=20, c='blue', alpha=.5)  # 绘制样本点
#     axs[2].scatter(xMat[:, 1].flatten().A[0], yMat.flatten().A[0], s=20, c='blue', alpha=.5)  # 绘制样本点
#     # 设置标题,x轴label,y轴label
#     axs0_title_text = axs[0].set_title(u'局部加权回归曲线,k=1.0')
#     axs1_title_text = axs[1].set_title(u'局部加权回归曲线,k=0.01')
#     axs2_title_text = axs[2].set_title(u'局部加权回归曲线,k=0.003')
#     plt.setp(axs0_title_text, size=8, weight='bold', color='red')
#     plt.setp(axs1_title_text, size=8, weight='bold', color='red')
#     plt.setp(axs2_title_text, size=8, weight='bold', color='red')
#     plt.xlabel('X')
#     plt.show()


# 使用局部加权线性回归计算回归系数w
def lwlr(testPoint, xArr, yArr, k=1.0):
    """
    Parameters:
        testPoint - 测试样本点
        xArr - x数据集
        yArr - y数据集
        k - 高斯核的k,自定义参数
    Returns:
        ws - 回归系数
    """
    print()
    print(xArr)
    print(yArr)
    xMat = np.mat(xArr)
    yMat = yArr.T
    m = np.shape(xMat)[0]
    weights = np.mat(np.eye((m)))  # 创建权重对角矩阵
    for j in range(m):  # 遍历数据集计算每个样本的权重
        diffMat = testPoint - xMat[j, :]
        weights[j, j] = np.exp(diffMat * diffMat.T / (-2.0 * k ** 2))
    xTx = xMat.T * (weights * xMat)
    if np.linalg.det(xTx) == 0.0:
        print("矩阵为奇异矩阵,不能求逆")
        return
    # tem0=weights * yMat
    # tem1=xMat.T*tem0
    # ws=xTx.I *tem1
    ws = xTx.I * (xMat.T * (weights * yMat))  # 计算回归系数
    return testPoint * ws


# # 局部加权线性回归测试
# def lwlrTest(testArr, xArr, yArr, k=1.0):
#     """
#     Parameters:
#         testArr - 测试数据集
#         xArr - x数据集
#         yArr - y数据集
#         k - 高斯核的k,自定义参数
#     Returns:
#         ws - 回归系数
#     """
#     m = np.shape(testArr)[0]  # 计算测试数据集大小
#     yHat = np.zeros(m)
#     for i in range(m):  # 对每个样本点进行预测
#         yHat[i] = lwlr(testArr[i], xArr, yArr, k)
#     return yHat


if __name__ == '__main__':
    xArr,yArr=loadDataSet("../welding.txt",2)
    print(xArr)
    print(yArr)
    yMat=np.array(yArr)  # lwlr输入的yArr的形状是一行n列的形式，每列对应着xArr的结果值
    print(lwlr([8.0,5.0],xArr,yMat[:,1].reshape(1,-1),k=0.5))


