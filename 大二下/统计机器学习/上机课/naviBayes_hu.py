# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:24:29 2023

@author: win10
"""

import numpy as np

#构造NB分类器
def Train(X_train, Y_train, feature):
    global class_num,label
    class_num = 2           #分类数目
    label = [1, -1]         #分类标签
    feature_len = 3         #特征长度
    #构造3×2的列表
    feature = [[1, 'S'],    
               [2, 'M'],
               [3, 'L']]

    prior_probability = np.zeros(class_num)                         # 初始化先验概率
    conditional_probability = np.zeros((class_num,feature_len,2))   # 初始化条件概率
    
    positive_count = 0     #统计正类
    negative_count = 0     #统计负类
    for i in range(len(Y_train)):
        if Y_train[i] == 1:
            positive_count += 1
        else:
            negative_count += 1
    prior_probability[0] = positive_count / len(Y_train)    #求得正类的先验概率
    prior_probability[1] = negative_count / len(Y_train)    #求得负类的先验概率
    
    '''
    conditional_probability是一个2*3*2的三维列表，第一维是类别分类，第二维和第三维是一个3*2的特征分类
    '''
    #分为两个类别
    for i in range(class_num):
        #对特征按行遍历
        for j in range(feature_len):
            #遍历数据集，并依次做判断
            for k in range(len(Y_train)): 
                if Y_train[k] == label[i]: #相同类别
                    if X_train[k][0] == feature[j][0]:
                        conditional_probability[i][j][0] += 1
                    if X_train[k][1] == feature[j][1]:
                        conditional_probability[i][j][1] += 1

    class_label_num = [positive_count, negative_count]  #存放各类型的数目
    for i in range(class_num):
        for j in range(feature_len):
            conditional_probability[i][j][0] = conditional_probability[i][j][0] / class_label_num[i]  #求得i类j行第一个特征的条件概率 
            conditional_probability[i][j][1] = conditional_probability[i][j][1] / class_label_num[i]  #求得i类j行第二个特征的条件概率

    return prior_probability,conditional_probability

#给定数据进行分类
def Predict(testset, prior_probability, conditional_probability, feature):
    result = np.zeros(len(label))
    for i in range(class_num):
        for j in range(len(feature)):
            if feature[j][0] == testset[0]:
                conditionalA = conditional_probability[i][j][0]
            if feature[j][1] == testset[1]:
                conditionalB = conditional_probability[i][j][1]
        result[i] = conditionalA * conditionalB * prior_probability[i]

    result = np.vstack([result,label])

    return result


def main():
    X_train = [[1, 'S'], [1, 'M'], [1, 'M'], [1, 'S'],  [1, 'S'],
               [2, 'S'], [2, 'M'], [2, 'M'], [2, 'L'],  [2, 'L'],
               [3, 'L'], [3, 'M'], [3, 'M'], [3, 'L'],  [3, 'L']]
    Y_train = [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]   

    #构造3×2的列表
    feature = [[1, 'S'],    
               [2, 'M'],
               [3, 'L']]

    testset = [2, 'S']
    
    prior_probability, conditional_probability= Train(X_train, Y_train, feature)
    
    result = Predict(testset, prior_probability, conditional_probability, feature)
    print(result)

if __name__ == '__main__':
    main()