import time
from fptree1 import *
from csv import reader

start = time.time()

fptree = FP1tree()

def readfromcsvfile(filename):
        dataset = []
        frequency = []
        type(filename)
        csv_reader= reader(filename)    
        for text in csv_reader:
            text = list(filter(None, text))
            dataset.append(text)
            frequency.append(1)
        return dataset, frequency

def getproductSupport(productset, productsetList):
        productSupport = 0
        for product in productsetList:
            if(set(productset).issubset(product)):
                productSupport += 1
        return productSupport

def BuildAssociationRule(freqItemSet, dataset,min_sup):
        asrules = []
        for productset in freqItemSet:
            productsubsets = chain.from_iterable(combinations(productset, r) for r in range(1, len(productset)))
            itemSetSup = getproductSupport(productset, dataset)
            for prod in productsubsets:
                if(itemSetSup > min_sup):
                    asrules.append([set(prod), set(productset.difference(prod)), itemSetSup])                   
        return asrules 

def fpGrowth(filename, minSup):
    dataset, fqy = readfromcsvfile(filename)
    min_sup = len(dataset)* minSup
    fpTree, prodfreqTable = fptree.ConstructTree(dataset, fqy, min_sup)
    if(fpTree != None):
        freqItems = []
        fptree.MineTreeRecursively(prodfreqTable, min_sup, set(), freqItems)
        rules = BuildAssociationRule(freqItems, dataset,min_sup)   
    else:
        print('No frequent item set')
    return freqItems, rules

if __name__ == "__main__":
    filename = open('/Users/vinithkumarpasula/Downloads/adult.csv', 'r') 
    minSup=float(input("Enter min support value: "))
    freqItemSet, rules = fpGrowth(filename, minSup)
    #print(freqItemSet,end='\n')
    print("Length of frequent itemsets:", len(freqItemSet),'\n')
    #print(rules,'\n')

end = time.time()
print('Execution time: ', (end-start) * 10**3, 'millisecs', '\n')



