

import math
import numpy as np
from matplotlib import pyplot as plt

# dosages = np.array([0, 0.1, 0.3, 0.5, 0.7, 0.9])
dosages = [0, 0.1, 0.3, 0.5, 0.7, 0.9]
dose_list = []

# established NN parameters
top_w1 = -34.4
top_b1 = 2.14
top_w2 = -1.30
bot_w1 = -2.52
bot_b1 = 1.29
bot_w2 = 2.28
b2 = -0.58

top_g1_y = []
top_g2_y = []
bot_g1_y = []
bot_g2_y = []
g3_y = []
eff_y = []

for d in dosages:
    g3 = 0
    # top
    w1 = d * top_w1
    b1 = w1 + top_b1
    top_g1 = math.log(1 +math.e**b1) # softplus activation
    # math.log defaults to natural logarithm
    if d == 0:
        print(f'dose 0 top_g1:{top_g1}') # confirm same value as in video, but not a valid dose.
        continue
    top_g1_y.append(round(top_g1,5))    # round and save for plot input
    top_g2 = top_g1 * top_w2
    top_g2_y.append(round(top_g2,5))    # round and save for plot input
    g3 = g3 + top_g2

    # bottom
    w1 = d * bot_w1
    b1 = w1 + bot_b1
    bot_g1 = math.log(1 +math.e**b1) # softplus activation
    bot_g1_y.append(round(bot_g1,5))    # round and save for plot input

    bot_g2 = bot_g1 * bot_w2
    bot_g2_y.append(round(bot_g2,5))    # round and save for plot input
    g3 = g3 + bot_g2
    g3_y.append(round(g3,5))    # round and save for plot input

    eff = g3 + b2
    eff_y.append(round(eff,5))    # round and save for plot input

    dose_list.append(d) # dose 0 not appended

# print values for comparison to any given by video
print ('top_g1_y:')
for d, y in zip(dose_list, top_g1_y):
    print (f' dose:{d}  g1 value:{y}')
print ('top_g2_y:')
for d, y in zip(dose_list, top_g2_y):
    print (f' dose:{d}  g1 value:{y}')
print ('g3_y:')
for d, y in zip(dose_list, g3_y):
    print (f' dose:{d}  g1 value:{y}')
print ('eff_y:')
for d, y in zip(dose_list, eff_y):
    print (f' dose:{d}  g1 value:{y}')


plt.title('StatQuest Dosage Neural Network Tester')
plt.xlabel('dosage levels')
plt.ylabel('y results')
plt.grid(True)
# comment out any plot as needed to clarify.
plt.plot(dose_list, top_g1_y, color = 'blue', marker = 'x', label = 'top g1', linestyle = '--')
plt.plot(dose_list, top_g2_y, color = 'blue', marker = 'o', label = 'top g2')
plt.plot(dose_list, bot_g1_y, color = 'orange', marker = 'x', label = 'bot g1', linestyle = '--')
plt.plot(dose_list, bot_g2_y, color = 'orange', marker = 'o', label = 'bot g2')
plt.plot(dose_list, g3_y, color = 'green', marker = 'o', label = 'sum')
plt.plot(dose_list, eff_y, color = 'red', marker = 'o', label = 'efficacy')
plt.legend()
plt.show()


