import sys

def auc():
    #read in two files for data 
    inputFile = input("Enter first file: ")
    inputFile2 = input("Enter second file: ")
    dataList = []
    # pos and neg will store the total positive and negative values from files
    pos = 0
    neg = 0
    # sort the data from the two files into lists 
    with open (inputFile, 'r') as f, open(inputFile2, 'r') as fs:
        instance = []
        readData = f.read()
        readData2 = fs.read()
        lines = readData.split("\n")
        truth = readData2.split("\n")
        for i in range (0, len(lines)):
            instance = []
            data = lines[i].split(", ")
            groundtruth = truth[i].split(", ")
            for j in range(0, len(data)):
                if data[j].isdigit():
                    instance.append(int(data[j]))
                else:
                    instance.append(float(data[j]))
                if (groundtruth[j]).isalpha():
                    if groundtruth[j] == 'P':
                        pos = pos + 1
                    else:
                        neg = neg + 1
                    instance.append(groundtruth[j])
            dataList.append(instance)
    #sort the list in descending order 
    dataList.sort(key = lambda x:x[1], reverse=True)
    print(dataList)
    #true negative and false negative values 
    tn = neg
    fn = pos
    #true positive and false positive values
    tp = 0
    fp = 0
    tpr = [] #stores the tpr and fpr for each item in dataList
    fpr = []
    for event in dataList:
        if event[2] == 'N':
            tn = tn - 1
            fp = fp + 1
        else:
            fn = fn - 1
            tp = tp + 1
        tpr.append(tp/(tp+fn))
        fpr.append(fp/(tn+fp))
    #auc calculation: integration method
    area = 0
    for i in range (0, len(tpr)-1):
        area = area + ((fpr[i+1] - fpr[i]) * (tpr[i]+tpr[i+1])) / 2
    print ("Area: ") 
    print(area)
    
#main function 
if __name__ == '__main__':
    auc()

