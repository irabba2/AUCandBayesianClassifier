# Implementing a Naïve-Bayesian Classifier - CS 411 Programming Assignment #2 
# Megan Mehta and Ifra Rabbani

import sys 
import csv 
from math import sqrt
from math import pi 
from math import exp 

#get the standard deviation and mean for every column (A1, A2, A3, etc.)
def dataset_summary(all):
    summary = []
    #i is the list of column vals (ex: all of A1 vals will be 1 list)
    #zip(*column_data) will take the existing data list and convert each column into a tuple 
    for i in zip(*all): 
        print(i)
        mean = sum(i)/len(i)
        vari = sum([(x-mean)**2 for x in i]) / float(len(i)-1)
        stdev = sqrt(vari)
        vals = (mean, stdev) #create a tuple with the mean and stdev vals 
        summary.append(vals)

    del(summary[-1]) #don't need to calculate vals for column C 
    return summary #returns a list of tuples where mean is first val, stdev is second val

def separate_by_class(all):
    by_class = dict()
    for i in range(len(all)): #iterate thorugh all the data lists 
        a = all[i]
        c_val = a[-1] #take out teh C value 
        if (c_val not in by_class):
            by_class[c_val] = list()
        by_class[c_val].append(a)
    return by_class    

    
#we need to get summary statistics based on the C vals 
def summary_by_class(by_class):
    #separate the data by class 
    class_summary = dict()
    for c_val, rows in by_class.items():
        class_summary[c_val] = dataset_summary(rows)

    return class_summary
    
'''Your program should print all the probabilities in the following format, where the
#ordering of the conditional probabilities are not important. 
P(C=1) = 0.4
P(C=0) = 0.6
P(A1= a | C=1) = 0.3
P(A1= z | C=1) = 0.4
P(A1= a | C=0) = 0.2
P(A1= z | C=0) = 0.3'''

#formula for the gaussian probability distribution function 
def gaussian_probability(mean, stdev, x):
    g_pdf = (1 / sqrt(2 * pi) * stdev) * exp(-((x-mean)^2 / (2 * stdev**2)))

#for every row, print the probability 
#def compute_probability(data):
    

#probability of C=1 and C=0
#def compute_class_probability(class_summary):
   
    
#main function
if __name__ == '__main__':
    '''Input data: The input data will be given in a file in the following format, where the first row
    gives the attribute names and the rest are the data instances. 
    A1, A2, A3, C
    a, b, t, 1
    x, y, f, 0'''
    
    #read the input as a list of lists (every row will be a list, and delete the initial column names)
    #accept file input + read file into matrix 
    training_set = input("Enter .txt file here: ")
    train = []
    
    with open (training_set, 'r') as f:
        read_data = f.read()
        content_list = read_data.split("\n")
        del(content_list[0])
    
        for i in content_list:
            a = list(i.split(','))
            train.append(a)
    
    datasetSummary = dataset_summary(train)
    databyClass = separate_by_class(train)
    classSummary = summary_by_class(databyClass)
    #probs = compute_probabilities(classSummary, train)
    print(datasetSummary)