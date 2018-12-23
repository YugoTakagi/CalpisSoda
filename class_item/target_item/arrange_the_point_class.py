import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from decimal import *

class arrange_the_point(object):
    """docstring for arrange_the_point."""
    delta_s = 0.0
    ARRANGE_INDEXS = []
    maxmum_interval = 0
    minmumInterval = 0
    def __init__(self):
        pass
    def maximumInterval(self, TVP_of_S):
        INDEX_OF_TVPS = np.arange(start=0.0, stop=len(TVP_of_S)-1, step=1, dtype= int)
        for index in INDEX_OF_TVPS:
            if (index-1) <= 0:
                self.maxmum_interval = TVP_of_S[index]
            else:
                interval = TVP_of_S[index] - TVP_of_S[index-1]
                if self.maxmum_interval<interval:
                    self.maxmum_interval = interval
                else:
                    pass
        print('self.maxmum_interval = {}'.format(self.maxmum_interval))
    def minmumInterval(self, TVP_of_S):
        INDEX_OF_TVPS = np.arange(start=0.0, stop=len(TVP_of_S)-1, step=1, dtype= int)
        for index in INDEX_OF_TVPS:
            if (index-1) <= 0:
                self.minmum_interval = TVP_of_S[index]
            else:
                interval = TVP_of_S[index] - TVP_of_S[index-1]
                if self.minmum_interval>interval:
                    self.minmum_interval = interval
                else:
                    pass
        print('self.minmum_interval = {}'.format(self.minmum_interval))
    def arrange(self, before_x, before_y, TVP_of_S):
        print('+--+-start arrange-+--+')
        index_for_TVP = 1
        count = 0
        self.maximumInterval(TVP_of_S)
        self.minmumInterval(TVP_of_S)
        INDEX_OF_BEFORE = np.arange(start=0.0, stop=len(before_x)-1, step=1, dtype= int)
        print('INDEX_OF_BEFORE = {}'.format(len(INDEX_OF_BEFORE)))
        print('len(TVP_of_S) = {}'.format(len(TVP_of_S)))

        #getcontext().prec = 20
        error = []
        for index in INDEX_OF_BEFORE:
            dx = before_x[index+1] - before_x[index]
            dy = before_y[index+1] - before_y[index]
            ds = np.sqrt(dx*dx + dy*dy)
            self.delta_s = ds + self.delta_s
            if index_for_TVP <= len(TVP_of_S)-1:
                error.append(TVP_of_S[index_for_TVP] - self.delta_s)
                #print(error)
                #if error > self.maxmum_interval:
                '''
                if error < 0.0001:
                    print('+: index[{}] = {}'.format(index_for_TVP,index))
                    self.ARRANGE_INDEXS.append(index)
                    index_for_TVP = index_for_TVP + 1
                #'''
                if error[index] < 0:
                    #print('-: index[{}] = {}'.format(index_for_TVP,index))
                    self.ARRANGE_INDEXS.append(index)
                    index_for_TVP = index_for_TVP + 1
        plt.plot(error)
        plt.title("arrange")
        plt.grid(True)
        plt.show()
        print('index_for_TVP = {}'.format(index_for_TVP))
        print('len(self.ARRANGE_INDEXS) = {}'.format(len(self.ARRANGE_INDEXS)))
        print('+--+-end arrange-+--+')
        return self.ARRANGE_INDEXS, len(self.ARRANGE_INDEXS)
