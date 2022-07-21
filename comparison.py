import matplotlib.pyplot as plt
from pylab import *
figure()


t = [1,2,3,4]
tr1 = [82.17, 81.08, 64.9, 97.9]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('SVM','NB','KNN','HP'))
xlabel('')
ylabel('Accuracy (%)')
title('')
plt.xticks(rotation=45)
grid(True)
show()




t = [1,2,3,4]
tr1 = [81.17, 82.08, 63.9, 98.9]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('SVM','NB','KNN','HP'))
xlabel('')
ylabel('Precision (%)')
title('')
plt.xticks(rotation=45)
grid(True)
show()
figure()


t = [1,2,3,4]
tr1 = [82.17, 83.08, 66.9, 98.7]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('SVM','NB','KNN','HP'))
xlabel('')
ylabel('Recall(%)')
title('')
plt.xticks(rotation=45)
grid(True)
show()
t = [1,2,3,4]
tr1 = [80.17, 81.08, 76.9, 98.7]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('SVM','NB','KNN','HP'))
xlabel('')
ylabel('F1-Score(%)')
title('')
plt.xticks(rotation=45)
grid(True)
show()
figure()

t = [1,2,3,4]
tr1 = [81.17, 81.88, 75.9, 98.79]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('SVM','NB','KNN','HP'))
xlabel('')
ylabel('Sensitivity(%)')
title('')
plt.xticks(rotation=45)
grid(True)
show()
figure()
t = [1,2,3,4]
tr1 = [82.17, 82.08, 76.9, 98.75]

plot(t, tr1,marker='o', markerfacecolor='blue', markersize=6,label='',linewidth=2.0)



xticks(t , ('SVM','NB','KNN','HP'))
xlabel('')
ylabel('Specificity(%)')
title('')
plt.xticks(rotation=45)
grid(True)
show()
figure()

