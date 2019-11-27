# ML-Phase-3
Final Report




The source code[1] needs to be run as follows:

"python MLImplementation.py (training file name) (testing file name) (no. of example samples) (sampling rate) (no. of candidate classes)"

where,

no. of example samples are the no. of samples to be chosen per class
sampling rate is the rate of choosing the classes to sample
no. of candidate classes are the classes for prediction


We have analysed the results (acccuracies achieved) obtained by plotting a graph between accuracy and number of candidate classes considered. Code for the same has been attached (Graphs.py). We have also considered additional evaluation parameters like F1 Score, Logarithmic loss,mean absolute error. Code for the same has also been added to the MLProject.py file.

We tried Principal Component Analysis as a feature selection method, Ensemble Boosting technique (AdaBoost) and Regression techniques (Linear and Logistic Regression) in order to improve the accuracy of the existing model. The code for the same can be found under "Learn" function in MLProject.py.
Various results have been analysed using graphs and code for the same has been attached. (Graphs.py)


DATASETS:
link to the WIKIPEDIA dataset which we used: https://drive.google.com/open?id=1iAVpPOp9GbAkAM88FGEHTkEe4vYbVY-4

REFERENCES:
[1] Joshi B., Amini M.-R., Partalas I., Iutzeler F., Maximov Y. Aggressive Sampling for Multi-class to Binary Reduction with Applications to Text Classification Advances in Neural Information Processing Systems 30 (NIPS 2017), p. 4162-4171
