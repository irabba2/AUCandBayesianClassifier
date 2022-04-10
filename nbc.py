# Implementing a Naïve-Bayesian Classifier - CS 411 Programming Assignment #2 
# Megan Mehta and Ifra Rabbani

import sys 
import pandas as pd 
import csv 
from math import sqrt

#get the standard deviation and mean for every column
def dataset_summary(all):
    summary = []
    #i is the list
    for i in all: 
        mean = sum(i)/len(i)
        vari = sum([(x-mean)**2 for x in i]) / float(len(i)-1)
        stdev = sqrt(vari)
        vals = (mean, stdev) #create a tuple with the mean and stdev vals 
        summary.append(vals)

    del(summary[-1]) #don't need to calculate vals for column C 
    return summary 
    
'''Your program should print all the probabilities in the following format, where the
#ordering of the conditional probabilities are not important. 
P(C=1) = 0.4
P(C=0) = 0.6
P(A1= a | C=1) = 0.3
P(A1= z | C=1) = 0.4
P(A1= a | C=0) = 0.2
P(A1= z | C=0) = 0.3'''

#def compute_probabilities():
    
    
    
    
#main function
if __name__ == '__main__':
    '''Input data: The input data will be given in a file in the following format, where the first row
    gives the attribute names and the rest are the data instances. 
    A1, A2, A3, C
    a, b, t, 1
    x, y, f, 0'''
    
    #NEED TO FIND A WAY TO DO THIS WITHOUT PANDAS 
    #read the input as a list of lists
    #accept file input + read file into matrix 
    input_file = input("Enter .txt file here: ")
    df = pd.read_csv(input_file, sep=':', engine='python')
    a1 = df['A1'].tolist()
    a2 = df['A2'].tolist()
    a3 = df['A3'].tolist()
    c = df['C'].tolist()
 
    all = [a1, a2, a3, c]