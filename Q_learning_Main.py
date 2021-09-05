from typing import List
from Q_learning import map
import itertools
import numpy as np
map=map()



timesoftranning = 300
gamma = 0.8


l = [False, True]
gold=list(itertools.product(l, repeat=len(map.Goldlist)))


for j in range (0, len(map.Qtable)):
    #epsilon = 9999999999999
    #decay = 0.9
    for i in range(timesoftranning):
        #fetch Q-table according to gold state
        k=tuple(map.whichq(j))
        
        Goldlist,accumulate,Done,location,state=map.reset(j)
        while Done==False:
            #if tuple((map.x_c,map.y_c))==(1,7):
                #print("hi")
            #if np.random.uniform() >= epsilon and map.x_c!=0 and map.y_c!=0 and map.x_c!=9 and map.y_c!=9:
                #direction = k[state].index(max(k[state]))
            #else:
            direction=map.randomdirection()#add logic between random and choose max later.

            #the movement
            Done,R_P,nextstate,accumulate,state=map.move(direction,accumulate)
            
            #check the gold avilibility
            Goldstate=tuple(map.Goldlist.values())
            
            #Ballmen's
            k[int(state)][direction] = R_P + gamma * max(k[nextstate])
            


            state=nextstate
        #epsilon -= decay*epsilon


    

    


