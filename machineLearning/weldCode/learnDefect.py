import torch
from torch import nn
import torch.nn.functional as F
import numpy as np
from torch.utils.data import DataLoader,Dataset,TensorDataset
from matplotlib import pyplot as plt

def lodaData():
    # 正负样本数量
    n_positive, n_negative = 2000, 2000

    # 生成正样本, 小圆环分布
    r_p = 5.0 + torch.normal(0.0, 1.0, size=[n_positive, 1])
    theta_p = 2 * np.pi * torch.rand([n_positive, 1])
    Xp = torch.cat([r_p * torch.cos(theta_p), r_p * torch.sin(theta_p)], axis=1)
    Yp = torch.ones_like(r_p)

    # 生成负样本, 大圆环分布
    r_n = 8.0 + torch.normal(0.0, 1.0, size=[n_negative, 1])
    theta_n = 2 * np.pi * torch.rand([n_negative, 1])
    Xn = torch.cat([r_n * torch.cos(theta_n), r_n * torch.sin(theta_n)], axis=1)
    Yn = torch.zeros_like(r_n)

    # 汇总样本
    X = torch.cat([Xp, Xn], axis=0)
    Y = torch.cat([Yp, Yn], axis=0)
    return X,Y,Xn,Xp

class DNNModel(nn.Module):

    def __init__(self):
        super(DNNModel,self).__init__()
        self.fc1=nn.Linear(2,4)
        self.fc2=nn.Linear(4,8)
        self.fc3=nn.Linear(8,1)


    def forward(self,x):
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        y=nn.Sigmoid()(self.fc3(x))
        return y
    def loss_func(self,y_pred,y_true):
        return nn.BCELoss()(y_pred,y_true)
    # 评估函数(准确率)
    def metric_func(self,y_pred,y_true):
        y_pred = torch.where(y_pred>0.5,torch.ones_like(y_pred,dtype = torch.float32),
                          torch.zeros_like(y_pred,dtype = torch.float32))
        acc = torch.mean(1-torch.abs(y_true-y_pred))
        return acc
    @property
    def optimizer(self):
        return torch.optim.Adam(self.parameters(),lr=0.001)
def train_step(model,features,labels):
    # 正向传播
    pre=model(features)
    loss=model.loss_func(pre,labels)
    metric=model.metric_func(pre,labels)
    # 反向传播
    loss.backward()

    model.optimizer.step()
    model.optimizer.zero_grad()


    return loss.item(),metric.item()

def train_model(dl,model,epochs):
    for epoch in range(1,epochs+1):
        loss_list,metric_list=[],[]
        for features,labels in dl:
            li,mi=train_step(model,features,labels)
            loss_list.append(li)
            metric_list.append(mi)
        if epoch % 5 == 0:
            print('epoch=', epoch, '\tloss=', np.mean(loss_list), '\tmertic=', np.mean(metric_list))


if __name__ == '__main__':
    X,Y,Xn,Xp=lodaData()
    # print(X)
    # print(Y)
    dataset=TensorDataset(X,Y)
    dataloader=DataLoader(dataset,batch_size=10,shuffle=True,num_workers=2)
    # print(dataset)
    # print(dataloader)
    model=DNNModel()
    features,labels=next(iter(dataloader))
    # loss,mertric=train_step(model,features,labels)
    # print(loss)
    # print(mertric)
    train_model(dataloader,model,30)

    # 结果可视化
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
    ax1.scatter(Xp[:, 0], Xp[:, 1], c="r")
    ax1.scatter(Xn[:, 0], Xn[:, 1], c="g")
    ax1.legend(["positive", "negative"])
    ax1.set_title("y_true")

    Xp_pred = X[torch.squeeze(model.forward(X) >= 0.5)]
    Xn_pred = X[torch.squeeze(model.forward(X) < 0.5)]

    ax2.scatter(Xp_pred[:, 0], Xp_pred[:, 1], c="r")
    ax2.scatter(Xn_pred[:, 0], Xn_pred[:, 1], c="g")
    ax2.legend(["positive", "negative"])
    ax2.set_title("y_pred")
    plt.show()

