# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:31:18 2021

@author: ilmrd77
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#Creating boxes which return some values between its +-2.0 original value 

class box():
    
    def __init__(self,q):
        
        self.q = q
        
    def value(self):
        
        self.Q = np.random.uniform(-2,2) + self.q
        return self.Q
        

columnNames = ["Box1","Box2","Box3","Box4"]    # You can add number of columns
boxesDF = pd.DataFrame(index=np.arange(200) ,columns=columnNames) # Creating pandas DF

boxTrueValues = [8,3,9,6] #Boxes true values
boxes = [box(i) for i in boxTrueValues]

for line in range(0,200): # Fill the rows with random values
    for i in range(0,4):
        boxesDF.values[line,i] = boxes[i].value()

boxesDF.to_csv("FilePath/boxValues.csv")
    

    
boxesDF = pd.read_csv("FilePath/boxValues.csv")
boxesDF = boxesDF.iloc[:,1:] # Ignoring the index

time_step = 0
clicked = [0]*4
total_reward = 0
rewardList= []
chosenList = []
operation = 200
boxesNum = 4
confidence_lvl = 2


for line in range(0,operation):
    
    max_ucb = 0
    
    for box in range(0,boxesNum):
        
        if (clicked[box] > 0):
            
            exploration = math.sqrt(((math.log(time_step))/clicked[box]))*confidence_lvl
            exploitation = boxesDF.values[line,box]
            ucb = (exploitation+exploration)
        
        else : 
           
            ucb = 999999
            
        if (ucb>max_ucb):
            
            max_ucb = ucb
            chosenBox = box
    
    time_step+=1
    reward = boxesDF.values[line,chosenBox]
    total_reward+=reward
    clicked[chosenBox]+=1
    rewardList.append(reward)
    chosenList.append(chosenBox)
     

plt.hist(chosenList) # Histogram
plt.show()

           
