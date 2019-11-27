import matplotlib.pyplot as plt

# Graph between number of candidate classes and accuracies
x=[10,15,20,50]  #number of candidate classes
y=[24.5,26,31,32.75] #accuracies achieved
plt.plot(x,y,label='')
plt.xlabel('number of candidate classes')
plt.ylabel('accuracy')
plt.title('number of candidate classes vs accuracies')
plt.show()

#Graph between various algorithms and their accuracies
p=['SVM','ADAboost','LogisticRegression','LinearRegression']  #Algorithms
q=[37.5,23.64,38.29,39.51] #accuracies achieved
plt.plot(p,q,label='')
plt.xlabel('Algorithms')
plt.ylabel('Accuracy')
plt.title('Algorithms vs Accuracies')
plt.show()

#Graph between various algorithms and their f-measures
r=['SVM','ADAboost','LogisticRegression','LinearRegression']  #Algorithms
s=[0.26,0.057,0.26,0.24] #f-measures achieved
plt.plot(r,s,label='')
plt.xlabel('Algorithm')
plt.ylabel('F-measure')
plt.title('Algorithm vs F-measure')
plt.show()
