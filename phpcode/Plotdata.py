import matplotlib.pyplot as plt
import math
import json
import numpy as np
import random 

data = []
filename = 'agk_results.json'
# with open(filename) as f:
#     for line in f:
#         data.append(json.loads(line))

with open(filename) as json_file:
	s = json.load(json_file)

#r = pd.DataFrame(s['response'])
#t = pd.DataFrame(s['targetvalue'])

c = s["targetblurvalues"]
h = s["targetheightsvalues"]
d = s["targetvalue"]
n = len(s["targetvalue"])
responses = s['response']
target = s['targetvalue']
responses_new = []
h_new = []

for j in range(0,n-1):
	responses_new.append(int(responses[j])+2*random.uniform(-1,1))

for k in range(0,n-1):
	h_new.append(float(h[k]))
colors = []
sizes_ax1 = []
sizes_ax2 = []

cmap=plt.get_cmap('Reds')


# color is for blur level
for x in range(0, n-1):
    if c[x] == '0.4':
    	colors.append((0,  0, 0))
    elif c[x] == '1.0':
    	colors.append((0.35,  0.35, 0.4))
    elif c[x] == '2.0':
    	colors.append((0.3,  0.75, 1.0))
    else:
    	colors.append((0.75,  0.9, 0.9))

# size is for height values
for x in range(0, n-1):
    if h[x] == '0.01':
    	sizes_ax1.append(100)
    elif h[x] == '0.02':
    	sizes_ax1.append(200)
    elif h[x] == '0.03':
    	sizes_ax1.append(300)
    elif h[x] == '0.04':
    	sizes_ax1.append(500)
    elif h[x] == '0.05':
    	sizes_ax1.append(700)

# size is for densities values
for x in range(0, n-1):
    if d[x] == '114':
    	sizes_ax2.append(0)
    elif d[x] == '140':
    	sizes_ax2.append(0)
    elif d[x] == '178':
    	sizes_ax2.append(0)
    else:
    	sizes_ax2.append(400)

#f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
#target density versus match densities
plt.figure(1)
plt.scatter(target,responses,c=colors,s=sizes_ax1, edgecolor='none',alpha = 0.8)

plt.xlim(60, 310)
plt.ylim(60, 310)
plt.plot([60, 310], [60, 310], 'k-')
plt.xlabel('target density')
plt.ylabel('match density')
plt.grid()

plt.savefig('agk_targetvsmatch.png')

plt.figure(2)
# target height versus match densities. 
plt.scatter(h_new,responses_new,c=colors,s=sizes_ax2, edgecolor='none',alpha = 0.8)
plt.gray()
plt.xlim(0, 0.06)
plt.ylim(60, 310)
plt.xlabel('target height')
plt.ylabel('match density')
plt.title('Density=218')
plt.grid()
plt.savefig('agk_density218_height.png')
plt.show()


