import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class arrange_the_point(object):
    """docstring for arrange_the_point."""
    delta_s = 0.0
    ARRANGE_INDEXS = []
    maxmum_interval = 0
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
    def arrange(self, before_x, before_y, TVP_of_S):
        print('+--+-start arrange-+--+')
        index_for_TVP = 1
        count = 0
        self.maximumInterval(TVP_of_S)
        INDEX_OF_BEFORE = np.arange(start=0.0, stop=len(before_x)-1, step=1, dtype= int)
        print('INDEX_OF_BEFORE = {}'.format(len(INDEX_OF_BEFORE)))
        #print('len(TVP_of_S) = {}'.format(len(TVP_of_S)))
        for index in INDEX_OF_BEFORE:
            dx = before_x[index+1] - before_x[index]
            dy = before_y[index+1] - before_y[index]
            ds = np.sqrt(dx**2 + dy**2)
            self.delta_s += ds
            if index_for_TVP <= len(TVP_of_S)-1:
                error = TVP_of_S[index_for_TVP] - self.delta_s
                #if error > self.maxmum_interval:
                if error <= 0:
                    self.ARRANGE_INDEXS.append(index)
                    index_for_TVP = index_for_TVP + 1
        print('index_for_TVP = {}'.format(index_for_TVP))
        print('len(self.ARRANGE_INDEXS) = {}'.format(len(self.ARRANGE_INDEXS)))
        print('+--+-end arrange-+--+')
        return self.ARRANGE_INDEXS, len(self.ARRANGE_INDEXS)
