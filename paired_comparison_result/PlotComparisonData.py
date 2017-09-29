""" python plotting json data"""
""" September 29, 2017, bx wrote it """

import matplotlib.pyplot as plt
import math
import json
import numpy as np
import random 
import os
# s it the data array, accumulating data from all blocks. 
#subjects = ['ar','bx','cz','hn','sk','ju','ww']
#for nSubject in range(len(subjects)):
    #subject = subjects[nSubject]
subject = 'pj'

script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'outputplot/') 
s = {}

# read the data from json file. 
for i in range(2):    
    filename = subject+"_block_"+str(i+1)+'_results.json'
    with open(filename) as json_file:
        s[i] = json.load(json_file)

# concatenate the data across the blocks
responses = s[0]['choices']+s[1]['choices']
leftdensity = s[0]['targetvalue']+s[1]['targetvalue']
rightdensity = s[0]['matchvalue']+s[1]['matchvalue']
blur = s[0]['targetblurvalues']+s[1]['targetblurvalues']
height = s[0]['targetheightsvalues']+s[1]['targetheightsvalues']
lighting = s[0]['targetilluminations']+s[1]['targetilluminations']

totalconditions = len(leftdensity)
correct = 0
lighting_response = {}
lighting_response['backlit'] = 0
lighting_response['sidelit'] = 0

height_response = {}
height_response['0.01'] = 0
height_response['0.02'] = 0
height_response['0.03'] = 0
height_response['0.04'] = 0
height_response['0.05'] = 0

blur_response = {}
response_list = []

# compute overall percent correctness.
for i in range(totalconditions):
    if (leftdensity[i] < rightdensity[i]) and (responses[i] =='left')\
    or (leftdensity[i]>rightdensity[i]) and (responses[i] == 'right'):
        correct = correct+1
        response_list.append(1)

        if lighting[i] == 'backlit':
            lighting_response['backlit'] = lighting_response['backlit']+1    
        else:
           lighting_response['sidelit'] = lighting_response['sidelit']+1 
        # height 
        if height[i] == '0.01':
            height_response['0.01']+=1    
        elif height[i] == '0.02':
            height_response['0.02']+=1  
        elif height[i] == '0.03':
            height_response['0.03']+=1  
        elif height[i] == '0.04':
            height_response['0.04']+=1  
        else: 
            height_response['0.05']+=1 

    else:
        response_list.append(0)

                
percent_correct = correct/float(totalconditions)
print percent_correct

blur_list = zip(response_list,blur)

# initialize the dictionary
for key,value in blur_list:
    blur_response[str(value)] = 0

# make histograms
for key,value in blur_list:
    if key == 1:
        blur_response[str(value)]+=1

plt.figure()
x = np.arange(len(height_response))
plt.bar(x,height_response.values(), align='center', width=0.5)
plt.xticks(x, height_response.keys())
ymax = max(height_response.values()) + 1
plt.title('Histogram of correct responses over heights')
plt.ylim(0, ymax)
plt.show()



