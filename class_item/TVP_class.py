import numpy as np
import math
import matplotlib.pyplot as plt
import csv

from scipy import integrate
from bezier_class import bezier
from color_class import pycolor

def main():
    '''inint*******************************
    ***************************************'''
    bez = bezeir()
    list_of_bezeir_set1 = np.array([[7*74,7*74],[4000,(25*74+46*74)/2],[-800,(25*74+46*74)/2],[17*74,(66*74+46*74)/2]], dtype=np.float)
    list_of_bezeir1 = bez.bezeir_making(list_of_bezeir_set1)
    '''/inint******************************
    ***************************************'''
    #ii = np.linspace(0,2*np.pi,1000)
    #s = np.sqrt(1**2 + np.cos(ii)**2)
class trapezoidal_velocity_profile(object):
    """docstring fs trapezoidal_velocity_profile."""
    p_max = 0
    time_end = 0
    vx = []
    vy = []
    def get_p_max(self):
        return self.p_max
    def get_time_end(self):
        return self.time_end
    def __init__(self):
        pass
    def get_vx(self):
        return
        pass
    def get_vy(self):
        pass
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
        #self.vell_end = vell_end
        theta = 0
        list_of_theta = []
        list_length = np.linspace(0, len(x_ref)-1, len(x_ref), dtype = int)
        #print("len(x_ref) = ", len(x_ref))
        curve_length = 0
        for index in list_length:
            if (index - 1) <= 0:
                dx = x_ref[index]
                dy = y_ref[index]
            else:
                dx = x_ref[index] - x_ref[index - 1]
                dy = y_ref[index] - y_ref[index - 1]

                #dtheta.append(np.arctan(dx/dy))
                dtheta = np.arctan(dx/dy)
                #theta.append(theta[index-2] + dtheta[index-1])
                theta += dtheta
            ds = np.sqrt(dx**2 + dy**2)
            curve_length += ds
            list_of_theta.append(theta)
        #inint##############
        self.p_max = curve_length * 0.001#m  :=mitinori
        print("self.p_max = {}".format(self.p_max))
        print("list_length = {}".format(list_length))
        #Vmax = 5.0#m/s
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
        time_count = np.linspace(0,T,T*len(x_ref))
        Ac = []
        V = []
        v1 = 0.0
        v2 = 0.0
        v3 = 0.0
        P = []
        p1 = 0.0
        p2 = 0.0
        p3 = 0.0
        if T2<0:
            print pycolor.RED + "T2 error" +pycolor.END
            print("T2 error",T2)
            print("self.p_max = {}".format(self.p_max))

        for t in time_count:
            if t<=T1:
                Ac.append(A)
                v1 = A*t +vell_start
                V.append(v1)
                #P.append(A*t**2/2.0)
                #p1 = A*t**2.0/2.0
                p1 = A*t**2/2.0 +P_start
                P.append(p1)
            elif t<=T2+T1:
                Ac.append(0.0)
                v2 = v1
                V.append(v2)
                p2 = A*T1*(t-T1) + p1
                P.append(p2)
            elif t<= T:
                Ac.append(-A)
                v3 = -A*(t-(T1+T2))/2.0 +v2
                V.append(v3)
                #p3 = -A*(t-(T1+T2))**2/2 +p2
                #p3 = -A*(t-self.time_end)**2 + self.p_max
                p3 = -A*(t-(T1+T2))**2/2.0 +A*T1*(t-(T1+T2)) +p2
                P.append(p3)
            else:
                print("a-t error")
        Vx = []
        Vy = []
        for index in list_length:
            if (index - 1) <= 0:
                Vx.append(V[index] * np.sin(list_of_theta[index]))
                Vy.append(V[index] * np.cos(list_of_theta[index]))
            else:
                Vx.append(V[index-1] * np.sin(list_of_theta[index-1]))
                Vy.append(V[index-1] * np.cos(list_of_theta[index-1]))
        #print("T = ",T)
        time = np.linspace(0+time_start,T+time_start,T*len(x_ref))
        print("\n")
        plt.plot(time,Ac,color ="red",ls="-.")#,marker="."
        plt.plot(time,V,color ="#FE9A2E",ls="-.")#, linewidth=3
        plt.plot(time,P,color ="Green",ls="-.")
        #plt.show()
        self.vx.extend(Vx)
        self.vy.extend(Vy)
        #print(self.vx)
        with open('vx_ref.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.vx)
        with open('vy_ref.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.vy)
            #writer.writerow(sai)
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

        return P
