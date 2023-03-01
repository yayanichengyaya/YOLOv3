from lib2to3.pgen2.token import CIRCUMFLEX
import numpy as np
from predict import pre
import matplotlib.pyplot as plt

#情况分类，有车的情况，输入1；没有车，输入0
print('输入情况类别：')
circum=input()

print('输入测试集大小：')
len=int(input())
Re=np.zeros(19,float)
Pr=np.zeros(19,float)
co=0

for i in range(1,20,1): 
   FP=TP=TN=FN=0
   con=i/20
   y=pre(con,len)
   y_pred=np.array(y)
   print(y_pred)
   if circum == 'a':
     y_true=np.ones(len,int)
   elif circum == 'b':
     y_true=np.zeros(len,int)

   for j in range(0,len-1):
       if y_pred[j]>0:
          if y_true[j]==1:
              TP=TP+1
              FP=FP+y_pred[j]-y_true[j]
          elif y_true[j]==0:
              FP=FP+y_pred[j]
       elif y_pred[j]==0:
           if y_true[j]==0:
              TN=TN+1
           else:
              FN=FN+1

   err = (FP+FN)/(FP+FN+TP+TN)
   print("错误率：",err)
   #召回率，正例被正确判断的比例
   Recall = TP / (TP+FN)
   print("召回率：",Recall)
   #精确率，判断的正例中正确的比例
   Re[co]=Recall
   Precision = TP / (TP+FP)
   print(Re)
   Pr[co]=Precision
   print(Pr)
   co=co+1
   print("精确率：",Precision)
   #F1—score
   F1 = 2*Recall*Precision / (Recall + Precision)
   print("F1—score",F1)

print(Re)
print(Pr)
plt.plot(Re,Pr)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.show()

