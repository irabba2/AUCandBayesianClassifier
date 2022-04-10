Computing AUC and Implementing a Naïve-Bayesian Classifier

auc()
This function asks for two input files, the first containing the ID for the test instance and the probability for the positive class, the second file contains the ID for the test instance and the ground truth value. These files are then parsed and sorted into a list where each item is in the format [ID, positiveClassProbability, groundTruth] for each test instance. This list is then iterated through to identify the truth positive rate and false positive rate after each occurence. These values are stored in the tpr[] and fpr[] lists so they can then be used for the final AUC calculation. The final under the curve area is printed to the screen and written into a text file, called auc.txt

