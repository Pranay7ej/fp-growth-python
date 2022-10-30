from collections import defaultdict
from itertools import chain, combinations

class FP1tree:

    def itemfreqTable( self,dataset,frequency): 
        itemfreqTable = defaultdict(int)
        for i, transactions in enumerate(dataset):
            for product in transactions:
                itemfreqTable[product] = itemfreqTable[product] + frequency[i]
        return itemfreqTable

    def ConstructTree(self,dataset, frequency, minSup):
        itemfreqTable = self.itemfreqTable(dataset,frequency)
        itemfreqTable = dict((product, support) for product, support in itemfreqTable.items() if support >= minSup)
        if(len(itemfreqTable) == 0):
            return None, None
        for product in itemfreqTable:
            itemfreqTable[product] = [itemfreqTable[product], None]  
        sortedtransactions= self.SortTransactions(dataset,itemfreqTable)
        tree, itemfreqTable = self.BuildTree(sortedtransactions,itemfreqTable,frequency)
        return tree,itemfreqTable

    def BuildTree(self, transactions, itemfreqTable, frequency): 
        fpTree = FPNode(None, None, None)
        for indx, productset in enumerate(transactions):
            productset = [item for item in productset if item in itemfreqTable]
            productset.sort(key=lambda item: itemfreqTable[item][0], reverse=True)
            presentNode = fpTree
            for item in productset:
                presentNode = self.insertFPTree(item, presentNode, itemfreqTable, frequency[indx])
        return fpTree, itemfreqTable
    
    def insertFPTree(self,item, treeNode, itemfreqTable, frequency):
        if item[0] not in treeNode.children:
            newItemNode = FPNode(item, frequency, treeNode)
            treeNode.children[item] = newItemNode
            self.updatefreqtable(item, newItemNode, itemfreqTable)    
        else:       
            treeNode.children[item[0]].increment(frequency)
        return treeNode.children[item]

    def updatefreqtable(self,item, targetNode, itemfreqTable):
        if(itemfreqTable[item][1] != None):
            currentNode = itemfreqTable[item][1]
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = targetNode     
        else:
            itemfreqTable[item][1] = targetNode

    def SortTransactions(self,dataset,itemfreqTable):
        sortedheaderTable = [item[0] for item in sorted(list(itemfreqTable.items()),key=lambda p:p[1][0],reverse=True)]
        newlist = []
        for i in range(len(dataset)):
            newTrans = [x for a in sortedheaderTable for x in dataset[i] if x== a]
            newlist.append(newTrans) if len(newTrans) > 0 else None
        return newlist    

 
    def MineTreeRecursively(self,itemfreqTable, minSup,previousset, freqItemList):
        sortedItemList = [item[0] for item in sorted(list(itemfreqTable.items()), key=lambda p:p[1][0])] 
        for item in sortedItemList:  
            newFreqSet = previousset.copy()
            newFreqSet.add(item)
            freqItemList.append(newFreqSet)    
            conditionalPattBase, frequency = self.ConditionalPatternBase(item, itemfreqTable) 
            conditionalTree, newHeaderTable = self.ConstructTree(conditionalPattBase, frequency, minSup) 
            if newHeaderTable != None:
                self.MineTreeRecursively(newHeaderTable, minSup,newFreqSet, freqItemList)

    def revisitfptree(self, node, previouspath):
        if node.parent != None:
            previouspath.append(node.product)
            self.revisitfptree(node.parent, previouspath)

    def ConditionalPatternBase(self,Basepattern, itemfreqTable):
        treeNode = itemfreqTable[Basepattern][1] 
        condPatterns = []
        frequency = []
        while treeNode != None:
            previouspath = []
            self.revisitfptree(treeNode, previouspath)  
            if len(previouspath) > 1:               
                condPatterns.append(previouspath[1:])
                frequency.append(treeNode.freq)
            treeNode = treeNode.next  
        return condPatterns, frequency

class FPNode:
    def __init__(self, product, frequency, parentNode):
        self.product = product
        self.freq = frequency
        self.parent = parentNode
        self.children = {}
        self.next = None

    def increment(self, frequency):
        self.freq = self.freq+ frequency
