# Computing AUC and Implementing a Naïve-Bayesian Classifier

## Overview of functions 

### AUC

`auc()`
This function asks for two input files, the first containing the ID for the test instance and the probability for the positive class, the second file contains the ID for the test instance and the ground truth value. These files are then parsed and sorted into a list where each item is in the format [ID, positiveClassProbability, groundTruth] for each test instance. This list is then iterated through to identify the truth positive rate and false positive rate after each occurence. These values are stored in the tpr[] and fpr[] lists so they can then be used for the final AUC calculation. The final under the curve area is printed to the screen and written into a text file, called auc.txt

### NBC 

`data_by_cols(all)`

This function will take the input and create a list of tuples, where every tuple contains values for one column. 

`separate_by_class(all)`

This function will put all of the C values into a dictionary, and the keys for the dictionary are the rows that equal that C value. 

`get_unique_vals(colData)`

This function will get all of the unique values in all columns except C. 

`get_class_vals(uniqueVals)`

This function will get all of the unique class values. 

`compute_class(classVals)`

This function will create a dictionary with all of the class values as keys, and the value will be the number of times each class value appears in the table. 

`compute_probability(colData, train, uniqueVals, classVals, class_counts)`

This function will compute the probability for all possible combinations of column and class values. First, a list is created with all possible combination s of class and column values, and a count value. Then, it iterates through all of the rows and increases the count whenever the possible combination exists. Finally, once all of the counts are complete, each list combination count will be divided by the total row count. 

`print_probs(probs, class_counts)`

This function will write out all the text required for the final .txt output file relating to probabilities. 

`predict_class(probs, train, test, class_counts)`

This function will predict the class based on the test file given. First, a dictionary will be created with the possible class values and the value will be the test file instances. Then, it iterates through the dictionary and using another reference dictionary with the probabilities, a calculation is done to compute the conditional probability that a class will be selected based on the test values. The output of this function is a list of possible class values. 
