import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class arrange_the_point(object):
    """docstring for arrange_the_point."""
    delta_s = 0
    index = []
    maxmum_interval = 0
    def __init__(self):
        pass
    def maximumInterval(self, TVP_of_S):
        INDEX_OF_TVPS = np.arange(start=0.0, stop=len(TVP_of_S)-1, step=1, dtype= int)
        for index in INDEX_OF_TVPS
            if (index-1) <= 0:
                self.maxmum_interval = TVP_of_S[index]
            else:
                interval = TVP_of_S[index] - TVP_of_S[index-1]
                if self.maxmum_interval<interval:
                    self.maxmum_interval = interval
                else:
                    pass
    def arrange(self, before_x, before_y, TVP_of_S):
        print('+--+-start arrange-+--+')
        index_for_TVP = 0
        count = 0
        self.maxmumInterval(TVP_of_S)
        Ib = np.arange(start=0.0, stop=len(before_x)-1, step=1, dtype= int)
        #print('Ib = {}'.format(Ib))
        for index in Ib:
            if (index-1) <= 0:
                dx = before_x[index]
                dy = before_y[index]
            else:
                dx = before_x[index] - before_x[index-1]
                dy = before_y[index] - before_y[index-1]
            ds = np.sqrt(dx**2 + dy**2)
            self.delta_s = self.delta_s + ds
            error = TVP_of_S[index_for_TVP] - self.delta_s
            if error < self.maxmum_interval:
                self.index.append(index)
                error = 0.0
                index_for_TVP = index_for_TVP + 1
                #print('index_for_TVP = {}'.format(index_for_TVP))
                count = count + 1
                #print('count = {}'.format(count))
            else:
                pass
        #print('self.index = {}'.format(self.index))
        print('len(self.index) = {}'.format(len(self.index)))
        print('+--+-end arrange-+--+')
        return self.index, len(self.index)
