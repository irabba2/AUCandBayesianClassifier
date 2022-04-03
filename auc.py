import sys

def auc():
    #read in two files for data 
    inputFile = input("Enter first file: ")
    inputFile2 = input("Enter second file: ")
    dataList = []
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
                    instance.append(groundtruth[j])
            dataList.append(instance)
    #sort the list in descending order 
    dataList.sort(key = lambda x:x[1], reverse=True)
    print(dataList)

#main function 
if __name__ == '__main__':
    auc()

