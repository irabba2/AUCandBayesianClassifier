# Implementing a Naïve-Bayesian Classifier - CS 411 Programming Assignment #2 
# Megan Mehta and Ifra Rabbani

from enum import unique
import sys 
import csv 
from math import sqrt
from math import pi 
from math import exp

#get the standard deviation and mean for every column (A1, A2, A3, etc.)
def data_by_cols(all):
    data = []
    #i is the row in the data
    #zip(*column_data) will take the existing data list and convert each column into a tuple 
    for i in zip(*all): 
        data.append(list(i))
        
    return data #returns a list of tuples where mean is first val, stdev is second val

#put C vals into dictionary, and values of dictionary keys are the rows that equal t 
def separate_by_class(all):
    by_class = dict()
    for i in range(len(all)): #iterate thorugh all the data lists 
        a = all[i]
        c_val = a[-1] #take out the C value 
        if (c_val not in by_class):
            by_class[c_val] = list()
        by_class[c_val].append(a)
    return by_class    
    
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

def get_unique_vals(colData):
    uniqueVals = []
    for i in colData:
        u = []
        u = list(set(i))
        uniqueVals.append(u)

    return uniqueVals

#put all unique class values in a list 
def get_class_vals(uniqueVals):
    classVals = []
    classVals = uniqueVals[-1] #last list in uniqueVals are the class values 
    return classVals

def compute_class_prob(classVals):
    #figure out total number of uniques in C 
    class_counts = dict()
    b = []
    for u in classVals:
        c_count = colData[-1].count(u)
        class_counts[u] = c_count #update dictionary with count of C val
    
    return class_counts

#for every row, print the probability 
def compute_probability(colData, train, uniqueVals, classVals, class_counts):
    del(uniqueVals[-1]) #delete the class values 
    probs = []
        
    #create a list of tuples, with all possible combinations for data instance, and class 
    count = 0
    for i in uniqueVals:
        for x in i:
            for y in classVals:
                probs.append([x, y, count])
    
    #calculate the number of times each a combo appears 
    #ex: when 'g' and 't' appear twice, count increases to 2 in the probs list 
    for i in probs: #iterate through possible options 
        for x in train: #iterate through all rows 
            if i[0] in x and i[1] in x:
                i[2] += 1
    c = 0 
    #actually do the probability calculation (divide by total number of C val)
    for x in classVals:
        for i in probs:
            if x in i:
                c = i[2] 
                i[2] = c/class_counts[x]   
        
    return probs

#list containing info for .txt output file 
def print_probs(probs, class_counts):
    text_probs = []
    
    ct = 0
    for i in class_counts:
       x = class_counts[i]/len(train)
       b = "P(" + str(i) + ") = " + str(x)
       text_probs.append(b)
       ct +=1
    
    for i in probs:
        b = "P(" + str(i[0]) + "|" + str(i[1]) + ") = " + str(i[2])
        text_probs.append(b)
        
    with open('NB_probabilities_no_smoothing.txt', 'w') as f:
        for i in text_probs:
            f.write(i + '\n')
    
    with open('NB_ probabilities_smoothing.txt', 'w') as f:
        for i in text_probs:
            f.write(i + '\n')
    

def predict_class(probs, train, test, class_counts):
    #iterate through all possible class values 
    temp = []  #store tuples of initial test vals 
    temp2 = dict()  #every tuple will be a key, and every value will be a list of possible classes 
    uniClasses = len(class_counts)
    temp = test
    z = ""
    probs2 = []
    for i in probs:
        z = str(i[1]) + str(i[0])
        probs2.append(z)
        x = i[2]
        probs2.append(x)

    it = iter(probs2)
    prob_dic = dict(zip(it, it)) #combinational probability pairs in dictionary 
    
    #need total class probabilities
    class_prob = dict()
    for i in class_counts:
       x = class_counts[i]/len(train)
       class_prob[i] = x
       
    #fill in the dictionary with test values 
    for x in class_counts:
        temp2[x] = temp
    
    
    a = ""
    all = []
    for key, values in temp2.items():
        for v in values:
            cal = 0
            for i in v:
                a = str(key) + str(i)
                print(a)
                cal = cal * prob_dic[a]
            cal = cal * class_prob[key]
            all.append(cal)
    
    with open('NB_test_smoothing.txt,', 'w') as f:
        for i in all:
            f.write(str(i) + '\n')
    
    
#main function
if __name__ == '__main__':
    '''Input data: The input data will be given in a file in the following format, where the first row
    gives the attribute names and the rest are the data instances. 
    A1, A2, A3, C
    a, b, t, 1
    x, y, f, 0'''
    
    #read the input as a list of lists (every row will be a list, and delete the initial column names)
    #accept file input + read file into matrix 
    training_set = input("Enter training .txt file here: ")
    train = []
    
    test_set = input("Enter test .txt file here: ")
    test = []
    
    with open (training_set, 'r') as f:
        read_data = f.read()
        content_list = read_data.split("\n")
        del(content_list[0])
    
        for i in content_list:
            a = list(i.split(', '))
            train.append(a)
    
    with open (test_set, 'r') as f:
        read_data = f.read()
        content_list = read_data.split("\n")
        del(content_list[0])
    
        for i in content_list:
            a = list(i.split(', '))
            test.append(a)
 
    colData = data_by_cols(train)
    uniqueVals = get_unique_vals(colData)
    classVals = get_class_vals(uniqueVals)
    class_counts = compute_class_prob(classVals)
    probability = compute_probability(colData, train, uniqueVals, classVals, class_counts) #just lists 
    text = print_probs(probability, class_counts)
    prediction = predict_class(probability, train, test, class_counts)
  