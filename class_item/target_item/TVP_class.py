import numpy as np
import math
import matplotlib.pyplot as plt
import csv

from scipy import integrate
from bezier_class import bezier
from ..color_class import pycolor
'''
print pycolor.RED + "RED TEXT" + pycolor.END
'''
class trapezoidal_velocity_profile(object):
    """docstring fs trapezoidal_velocity_profile."""
    p_max = 0
    time_end = 0
    num_tvp = 0
    curve_length = 0
    time_count=0
    alfa = []
    V = []
    def get_p_max(self):
        return self.p_max
    def get_time_end(self):
        return self.time_end
    def get_V(self):
        return self.V
    def get_time_count(self):
        return self.time_count
    def __init__(self):
        pass
    def making_curve_length(self, x_ref, y_ref):
        list_length = np.arange(start=0.0, stop=len(x_ref)-1, step=1, dtype= int)
        print('+--+-start making_curve_length-+--+')
        #print('list_length = {}'.format(list_length))
        print('len(x_ref) = {}'.format(len(x_ref)))
        for index in list_length:
            if (index - 1) <= 0:
                dx = x_ref[index]
                dy = y_ref[index]
            else:
                dx = x_ref[index] - x_ref[index - 1]
                dy = y_ref[index] - y_ref[index - 1]
            ds = np.sqrt(dx**2 + dy**2)
            self.curve_length += ds
        print('+--+-end making_curve_length-+--+\n')
    def deside(self):
        print('+--+-start deside-+--+')
        num = int(self.time_end/0.008)
        print('num = {}'.format(num))
        print('+--+-end deside-+--+\n')
        return num
    def making_angle(self, NEW_LOBS, len_new_index_for_bezier):
        x_ref = NEW_LOBS.T[0]
        y_ref = NEW_LOBS.T[1]
        IND = np.arange(start=0, stop=len_new_index_for_bezier-1, step=1, dtype= int)
        for index in IND:
            if (index - 1) <= 0:
                dx = x_ref[index]
                dy = y_ref[index]
            else:
                dx = x_ref[index] - x_ref[index-1]
                dy = y_ref[index] - y_ref[index-1]
            self.alfa.append(np.arctan(dy/dx))
        return self.alfa
    def making_TVP(self, x_ref, y_ref, vell_want, vell_start, vell_end, P_start, time_start):
        print('+--+-start making_TVP-+--+')
        theta = 0
        list_of_theta = []
        #list_length = np.linspace(0, len(x_ref)-1, len(x_ref), dtype = int)
        #inint##############
        self.p_max = self.curve_length #*0.001#m  :=mitinori
        print("self.p_max = {}".format(self.p_max))
        A = 1.0#m/ss
        ####################
        #vell_want, vell_start, vell_end, P_start
        T1 = (vell_want - vell_start)/A
        T3 = (vell_want - vell_end)/A

        L = self.p_max
        L1 = (vell_start - vell_want)*T1 / 2
        L3 = (vell_want - vell_end)*T1 / 2

        T2 = (L - L1 -L3)/vell_want
        T = T1+T2+T3
        print("Game time = {}".format(T+time_start))
        self.time_end = T
        ####################
        self.time_count = np.arange(start=0.0, stop=T, step=0.008, dtype=np.float)
        print('len(self.time_count) = {}'.format(len(self.time_count)))
        #print('time_count = {}'.format(time_count))
        Ac = []
        v1 = 0.0
        v2 = 0.0
        v3 = 0.0
        P = []
        p1 = 0.0
        p2 = 0.0
        p3 = 0.0
        if T2<0:
            print pycolor.RED + "T2 error" +pycolor.END
            print("T2 = {}".format(T2))
            print("self.p_max = {}".format(self.p_max))

        for t in self.time_count:
            if t<=T1:
                Ac.append(A)
                v1 = A*t +vell_start
                self.V.append(v1)
                #P.append(A*t**2/2.0)
                p1 = A*t**2/2.0 +P_start
                P.append(p1)
            elif t<=T2+T1:
                Ac.append(0.0)
                v2 = v1
                self.V.append(v2)
                p2 = A*T1*(t-T1) + p1
                P.append(p2)
            elif t<= T:
                Ac.append(-A)
                v3 = -A*(t-(T1+T2)) +v2
                self.V.append(v3)
                p3 = -A*(t-(T1+T2))**2/2.0 +A*T1*(t-(T1+T2)) +p2
                P.append(p3)
            else:
                print pycolor.RED + "a-t error" +pycolor.END
        Vx = []
        Vy = []
        linspace_time = np.linspace(0, len(self.time_count)-1, len(self.time_count), dtype = int)
        arange_time = np.arange(start=0.0, stop=len(self.time_count)-1, step=1, dtype= int)
        #print('linspace_time = {}'.format(linspace_time))
        '''
        for index in arange_time:#linspace_time:
            if (index - 1) <= 0:
                Vx.append(V[index] * np.sin(list_of_theta[index]))
                Vy.append(V[index] * np.cos(list_of_theta[index]))
                print("index = {}".format(index))
            else:
                Vx.append(V[index] * np.sin(list_of_theta[index-1]))
                Vy.append(V[index] * np.cos(list_of_theta[index-1]))
                print("index = {}".format(index))
        #'''
        time = np.arange(start=0.0+time_start, stop=self.time_end+time_start, step=0.008, dtype= np.float)
        plt.plot(time,Ac,color ="red", marker="o")#marker=".", ls=""
        plt.plot(time,self.V,color ="#FE9A2E", marker="o")#linewidth=3
        plt.plot(time,P,color ="Green", marker="o")
        print('+--+-end making_TVP-+--+\n')
        return P
        '''
        header = [['time'], ['a'], ['v'], ['p'],['theta'],['Vx'],['Vy']]
        with open('sample.csv', 'w') as f:
            writer = csv.writer(f)  # writer
            writer.writerows(header)
            writer.writerow(time)
            writer.writerow(Ac)
            writer.writerow(V)
            writer.writerow(P)
            writer.writerow(list_of_theta)
            writer.writerow(Vx)
            writer.writerow(Vy)
            #writer.writerow(sai)
        #'''
