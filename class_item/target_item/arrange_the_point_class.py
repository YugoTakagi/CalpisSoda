import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from decimal import *

class arrange_the_point(object):
    """docstring for arrange_the_point."""
    sum_s = 0.0
    ARRANGE_INDEXS = []
    #ARRANGE_INDEX_TVP = []
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
        self.ds_befor = 0
        self.index_of_tvp = 0
        for index in range(len(before_x)):
            dx = before_x[index] - before_x[index-1]
            dy = before_y[index] - before_y[index-1]
            ds = np.sqrt(dx**2 + dy**2)
            self.sum_s = self.sum_s + ds
            self.ds_befor = ds
            if self.sum_s >= TVP_of_S[self.index_of_tvp]:
                self.ARRANGE_INDEXS.append(index)
                self.index_of_tvp += 1
                if len(self.ARRANGE_INDEXS) == len(TVP_of_S):
                    break

        #print(self.ARRANGE_INDEXS)
        print('len(TVP_of_S) = {}'.format(len(TVP_of_S)))
        print('len(before_x) = {}'.format(len(before_x)))
        print('len(self.ARRANGE_INDEXS) = {}'.format(len(self.ARRANGE_INDEXS)))
        print('+--+-end arrange-+--+')
        return self.ARRANGE_INDEXS, len(self.ARRANGE_INDEXS)
    def arrange1(self, before_x, before_y, TVP_of_S):
        print('+--+-start arrange-+--+')
        INDEX_OF_BEFORE = np.arange(start=0, stop=len(before_x)-1, step=1, dtype= int)
        INDEX_OF_TVPS = np.arange(start=1, stop=len(TVP_of_S)-1, step=1, dtype= int)
        BEFORE_S = []
        self.maximumInterval(TVP_of_S)
        for index in INDEX_OF_BEFORE:
            dx = before_x[index+1] - before_x[index]
            dy = before_y[index+1] - before_y[index]
            ds = np.sqrt(dx*dx + dy*dy)
            self.sum_s = ds + self.sum_s
            if self.sum_s <= 0:
                print("self.sum_s <= 0 ?")
            BEFORE_S.append(self.sum_s)
        flag = 0
        index_of_ancer = 0
        for index_of_tvp in INDEX_OF_TVPS:
            for index in INDEX_OF_BEFORE:
                if index <= 1:
                    b_error = TVP_of_S[index_of_tvp] - BEFORE_S[index]
                else:
                    a_error = TVP_of_S[index_of_tvp] - BEFORE_S[index]
                    if b_error > a_error:
                        b_error = a_error
                    else:
                        self.ARRANGE_INDEXS.append(index)
                        break

        self.maximumInterval(TVP_of_S)
        self.minmumInterval(TVP_of_S)
        print('INDEX_OF_TVPS = {}'.format(INDEX_OF_TVPS))
        print('len(INDEX_OF_BEFORE) = {}'.format(len(INDEX_OF_BEFORE)))
        print('len(self.ARRANGE_INDEXS) = {}'.format(len(self.ARRANGE_INDEXS)))
        print('+--+-end arrange-+--+')
        return self.ARRANGE_INDEXS, len(self.ARRANGE_INDEXS)
    def arrange2(self, before_x, before_y, TVP_of_S):
        print('+--+-start arrange-+--+')
        count = 0
        min_index = 0

        INDEX_OF_BEFORE = np.arange(start=0, stop=len(before_x)-1, step=1, dtype= int)
        INDEX_OF_TVPS = np.arange(start=1, stop=len(TVP_of_S)-1, step=1, dtype= int)
        BEFORE_S = []
        self.maximumInterval(TVP_of_S)
        for index in INDEX_OF_BEFORE:
            dx = before_x[index+1] - before_x[index]
            dy = before_y[index+1] - before_y[index]
            ds = np.sqrt(dx*dx + dy*dy)
            self.sum_s = ds + self.sum_s
            if ds < 0:
                print("self.sum_s <= 0 ?")
                print("dx = {}, dy = {}".format(dx,dy))
            BEFORE_S.append(self.sum_s)
        flag = 0
        index_of_ancer = 0
        for index_of_tvp in INDEX_OF_TVPS:
            INDEX_OF_FLAG = np.arange(start=flag, stop=len(before_x)-1, step=1, dtype= int)#okasiikamo
            for ind in INDEX_OF_FLAG:
                interval = BEFORE_S[ind] - BEFORE_S[flag]
                if interval >= self.maxmum_interval:
                    index_of_ancer = ind
                    if int(flag - (flag+index_of_ancer)/2) >= 0:
                        index_of_start = int(flag - (flag+index_of_ancer)/2)
                    else:
                        index_of_start = 0
                    INDEX_OF_SARCH = np.arange(start=index_of_start, stop=index_of_ancer, step=1, dtype= int)
                    b_error = 100
                    for ind_of_sarch in INDEX_OF_SARCH:
                        a_error = TVP_of_S[index_of_tvp] - BEFORE_S[ind_of_sarch]
                        if b_error >= a_error:
                            b_error = a_error
                            min_index = ind_of_sarch
                            count += 1
                            #print("count = {}".format(count))
                        else:
                            print("erorr")
                    #self.ARRANGE_INDEXS.append(min_index)
                    #self.ARRANGE_INDEX_TVP.append(index_of_tvp)

                    flag = index_of_ancer - 1
                #break
            self.ARRANGE_INDEXS.append(min_index)
            self.ARRANGE_INDEX_TVP.append(index_of_tvp)
        self.maximumInterval(TVP_of_S)
        self.minmumInterval(TVP_of_S)
        print('INDEX_OF_TVPS = {}'.format(INDEX_OF_TVPS))
        print('len(INDEX_OF_BEFORE) = {}'.format(len(INDEX_OF_BEFORE)))
        print('len(self.ARRANGE_INDEXS) = {}'.format(len(self.ARRANGE_INDEXS)))
        #print(self.ARRANGE_INDEX_TVP)
        print('+--+-end arrange-+--+')
        return self.ARRANGE_INDEXS, len(self.ARRANGE_INDEXS)
    def arrange_old3(self, before_x, before_y, TVP_of_S):
        print('+--+-start arrange-+--+')
        index_for_TVP = 1
        self.maximumInterval(TVP_of_S)
        self.minmumInterval(TVP_of_S)
        INDEX_OF_BEFORE = np.arange(start=0, stop=len(before_x)-1, step=1, dtype= int)
        INDEX_OF_TVPS = np.arange(start=1, stop=len(TVP_of_S)-1, step=1, dtype= int)
        print('INDEX_OF_BEFORE = {}'.format(len(INDEX_OF_BEFORE)))
        print('len(TVP_of_S) = {}'.format(len(TVP_of_S)))
        error = 0
        ERROR = []
        ARR = []
        for index_for_TVP in INDEX_OF_TVPS:
            ERROR = []
            for index in INDEX_OF_BEFORE:
                dx = before_x[index+1] - before_x[index]
                dy = before_y[index+1] - before_y[index]
                ds = np.sqrt(dx*dx + dy*dy)
                self.sum_s = ds + self.sum_s
                ERROR.append(TVP_of_S[index_for_TVP] - self.sum_s)
                if (-0.00003 <= ERROR[index]) and (ERROR[index] <= 0.00003):
                    self.ARRANGE_INDEXS.append(index)
                    #ARR.append(ERROR[index])
                    break
                else:
                    #ARR.append(0)
                    pass
        #plt.plot(INDEX_OF_BEFORE, ERROR, marker=".", c="#58ACFA")
        #plt.plot(INDEX_OF_BEFORE, ARR, marker=".", c="#FF8000")
        plt.title("arrange")
        plt.grid(True)
        plt.show()
        print('index_for_TVP = {}'.format(index_for_TVP))
        print('len(self.ARRANGE_INDEXS) = {}'.format(len(self.ARRANGE_INDEXS)))
        print('+--+-end arrange-+--+')
        return self.ARRANGE_INDEXS, len(self.ARRANGE_INDEXS)
    def arrange_old1(self, before_x, before_y, TVP_of_S):
        print('+--+-start arrange-+--+')
        index_for_TVP = 1
        count = 0
        self.maximumInterval(TVP_of_S)
        self.minmumInterval(TVP_of_S)
        INDEX_OF_BEFORE = np.arange(start=0.0, stop=len(before_x)-1, step=1, dtype= int)
        print('INDEX_OF_BEFORE = {}'.format(len(INDEX_OF_BEFORE)))
        print('len(TVP_of_S) = {}'.format(len(TVP_of_S)))

        #getcontext().prec = 20
        error = 0
        ERROR = []
        LIST = []
        for index in INDEX_OF_BEFORE:
            dx = before_x[index+1] - before_x[index]
            dy = before_y[index+1] - before_y[index]
            ds = np.sqrt(dx*dx + dy*dy)
            self.sum_s = ds + self.sum_s
            if index_for_TVP <= len(TVP_of_S)-1:
                error = TVP_of_S[index_for_TVP] - self.sum_s
                ERROR.append(error)
                #plt.plot(index,ERROR[index],marker=".",c="#58ACFA")
                #print(error)
                #if error > self.maxmum_interval:
                if ERROR[index] < 0:
                    index_for_TVP = index_for_TVP + 1
                if ERROR[index] < 0.001:

                    #print('-: index[{}] = {}'.format(index_for_TVP,index))
                    self.ARRANGE_INDEXS.append(index)
                    LIST.append(ERROR[index])
                    #plt.plot(index,ERROR[index],marker=".",c="#FF8000")
                else:
                    pass
            else:
                pass
        plt.plot(INDEX_OF_BEFORE,ERROR,marker=".",c="#58ACFA")
        plt.title("arrange")
        plt.grid(True)
        plt.show()
        print('len:LIST = {}'.format(len(LIST)))
        print('index_for_TVP = {}'.format(index_for_TVP))
        print('len(self.ARRANGE_INDEXS) = {}'.format(len(self.ARRANGE_INDEXS)))
        print('+--+-end arrange-+--+')
        return self.ARRANGE_INDEXS, len(self.ARRANGE_INDEXS)
    def arrange_yoi(self, before_x, before_y, TVP_of_S):
        print('+--+-start arrange-+--+')
        index_for_TVP = 1
        self.maximumInterval(TVP_of_S)
        self.minmumInterval(TVP_of_S)
        INDEX_OF_BEFORE = np.arange(start=0.0, stop=len(before_x)-1, step=1, dtype= int)
        print('INDEX_OF_BEFORE = {}'.format(len(INDEX_OF_BEFORE)))
        print('len(TVP_of_S) = {}'.format(len(TVP_of_S)))
        error = 0
        ERROR = []
        ARR = []
        for index in INDEX_OF_BEFORE:
            dx = before_x[index+1] - before_x[index]
            dy = before_y[index+1] - before_y[index]
            ds = np.sqrt(dx*dx + dy*dy)
            self.sum_s = ds + self.sum_s
            ERROR.append(TVP_of_S[index_for_TVP] - self.sum_s)
            if index_for_TVP <= len(TVP_of_S)-1:
                #if self.sum_s >= TVP_of_S[index_for_TVP]:
                if ERROR[index] < 0:
                    self.ARRANGE_INDEXS.append(index)
                    ARR.append(ERROR[index])
                    index_for_TVP += 1
                else:
                    ARR.append(0)
        plt.plot(INDEX_OF_BEFORE, ERROR, marker=".", c="#58ACFA")
        plt.plot(INDEX_OF_BEFORE, ARR, marker=".", c="#FF8000")
        plt.title("arrange")
        plt.grid(True)
        plt.show()
        print('index_for_TVP = {}'.format(index_for_TVP))
        print('len(self.ARRANGE_INDEXS) = {}'.format(len(self.ARRANGE_INDEXS)))
        print('+--+-end arrange-+--+')
        return self.ARRANGE_INDEXS, len(self.ARRANGE_INDEXS)
