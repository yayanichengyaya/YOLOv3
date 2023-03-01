from winreg import REG_LINK
import numpy as np
from sklearn import datasets

#求解协方差
def coVariance(X):  # 数据的每一行是一个样本，每一列是一个特征
    ro, cl = X.shape
    row_mean = np.mean(X,axis=0)
    X_Mean = np.zeros_like(X)
    X_Mean[:] = row_mean       #把向量赋值给每一行
    X_Minus = X - X_Mean
    covarMatrix = np.zeros((cl,cl))
    for i in range(cl):
        for j in range(cl):
            covarMatrix[i,j] = (X_Minus[:,i].dot(X_Minus[:,j].T)) / (ro-1)
    return covarMatrix

def len(V,H,R):
    for i in range(1,)
    E_ijk = V[j] - H*R[i]


