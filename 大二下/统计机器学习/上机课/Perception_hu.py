# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 21:32:34 2023
感知机：原始算法与对偶算法
@author: win10
"""

import numpy as np
import matplotlib.pyplot as plt

class Perception():
    '''
    感知机算法，包括原始形式和对偶形式
    '''
    def __init__(self):
        self.learing_rate = 1

    def train(self, data, labels):
        '''
        原始形式的感知机算法，输入数据必须线性可分
        :param data: (n*m),n为样本个数，m为特征个数
        :param labels: 样本标签A
        '''
        data_size = data.shape[0]
        #初始化w,b
        self.w = [0] * (data.shape[1])
        self.b = 0
        y_pred = np.sign((np.dot(data, self.w) + self.b))
        #是否有误分类标记，当有误分类样本时执行以下循环
        flag = (y_pred == labels).all()
        while not flag:
            for i in range(data_size):
                y_pred = np.sign((np.dot(data, self.w) + self.b))
                if y_pred[i]*labels[i] <= 0:
                    self.w += self.learing_rate * data[i] * labels[i]
                    self.b += self.learing_rate * labels[i]
                    print(self.w,self.b)
            flag = (y_pred == labels).all()

    def get_gram_matrix(self, data):
        #计算格拉姆矩阵
        data_size = data.shape[0]
        gram_matrix = np.zeros((data_size, data_size))
        for i in range(data_size):
            for j in range(data_size):
                gram_matrix[i, j] = np.dot(data[i], data[j])
        self.gram_matrix = gram_matrix

    def dual_output(self, x_index, data_size, labels):
        '''
        计算第x_index个样本的对偶形式的输出，这里不进行符号函数运算
        :param x_index: 样本索引
        :param data_size: 样本个数
        :param labels: 样本标签
        '''
        output = self.b
        for i in range(data_size):
            output += (self.alpha[i] * labels[i] * self.gram_matrix[i, x_index])
        return output

    def train_dual(self, data, labels):
        #d对偶形式的感知机算法
        self.b = 0
        self.get_gram_matrix(data)
        data_size = data.shape[0]
        self.alpha = [0] * data_size
        flag = False
        while not flag:
            y_pred = [0] * data_size
            for i in range(data_size):
                y_pred[i] = np.sign(self.dual_output(i, data_size, labels))
                if labels[i] * y_pred[i] <= 0:
                    self.alpha[i] += self.learing_rate
                    self.b += self.learing_rate * labels[i]
                    print(self.alpha,self.b)
            flag = (y_pred == labels).all()


#书中例题数据检验算法
data = [[3,3],[4,3],[1,1]]
labels = [1,1,-1]
data = np.array(data)
labels = np.array(labels)
model = Perception()
model.train_dual(data,labels)
model.train(data,labels)


# #随机生成数据,在y=x附近生成数据
# x = np.linspace(0,50,50)
# y1 = x + np.random.randint(1,5,50)
# y2 = x + np.random.randint(-5,-1,50)
# data_positive = np.c_[x,y1]
# data_negative = np.c_[x,y2]
# labels_positive = np.ones(50)
# labels_negative = -np.ones(50)
# data = np.r_[data_positive,data_negative]
# labels = np.r_[labels_positive,labels_negative]
# model = Perception()
# model.train(data,labels)
# #计算感知机模型所算的斜率和截距
# k = - (model.w[0] / model.w[1])
# b = -model.b / model.w[1]

# xx = np.linspace(0,50,50)
# y = k*xx + b
# plt.scatter(x,y1)
# plt.scatter(x,y2)
# plt.plot(xx,y)
# plt.show()
