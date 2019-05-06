# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:43:12 2019

@author: Sruthi Pasumarthy

DTMCs
"""
import numpy as np

inputFile = "D://DTMC_Input.txt"
with open(inputFile, "r", encoding="utf-8") as fin:
    inputs = list(fin.readlines())
    numOfNodes = int(inputs[0])
    numOfEdges = int(inputs[1])
    i = 2
    adjMatrix = np.empty([numOfNodes , numOfNodes])
    initialProbabilityVector = np.array([1,0]) #pi0
    qualityProbabilityVector = np.array([[0.9],[0.95]])
    minutes = 0
        
    while i< len(inputs):
        splits = inputs[i].split(' ')
        row = int(splits[0])
        col = int(splits[1])
        val = float(splits[2])
        adjMatrix[row][col] = val
        i = i + 1
    
    print(adjMatrix)
    print("******************************")
    
    for j in range(numOfNodes):
        kSum = 0
        for k in range(numOfNodes):
            if j == k:
                continue
            else:
                kSum = kSum + adjMatrix[j][k]
        adjMatrix[j][j] = 1 - kSum
    
    print(adjMatrix)

    def qualityOKProbability(activeProbabilityVector):
        
        probabilityValue = activeProbabilityVector.dot(qualityProbabilityVector)
        return probabilityValue;
    
    #steady state
    def steadyState(probabilityVector, minutes):
        
        currentVector = probabilityVector.dot(adjMatrix)
        minutes = minutes + 1
        
        if np.array_equal(probabilityVector, currentVector):
            print("Minutes",str(minutes))
            return currentVector;
        else:
            #At time : 8, probability that source 0 is active
            #At next minute(after 8minutes => 9th minute), probability of producing an OK item
            if minutes == 8:
                source0ActiveProb = currentVector[0]
                print("The probability that source 0 is active after 8 minutes",source0ActiveProb)
                probabilityValue = qualityOKProbability(currentVector)
                print("The probability of producing an OK item in the next minute(9th minute)",probabilityValue[0])            
            
            steadyState(currentVector, minutes)
    
    
    steadyStateVector = np.ndarray((1,numOfNodes),steadyState(initialProbabilityVector, 0))
    
    print("The probability that source 0 is active at steady state",steadyStateVector[0,0])
    
    steadyStateOKQuality = qualityOKProbability(steadyStateVector)
    print("The average probability of producing an OK item in steady state",steadyStateOKQuality[0,0])  
    
    
    
    
                
