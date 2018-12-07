from bezier_class import bezier
from TVP_class import trapezoidal_velocity_profile
from color_class import pycolor as pc

import numpy as np
import math
import matplotlib.pyplot as plt
import csv

def main():
    bez = bezier(1000)
    TVP1 = trapezoidal_velocity_profile()

    list_of_bezier_set1 = np.array([[7*74,7*74],[4000,(25*74+46*74)/2],[-800,(25*74+46*74)/2],[17*74,(66*74+46*74)/2]], dtype=np.float)
    list_of_bezier1 = bez.bezier_making(list_of_bezier_set1)
    #list_of_bezier_set1 = np.array([[0,0],[1225,0],[1225+500,2000-1225],[1225+500,2000]], dtype=np.float)
    #list_of_bezier1 = bez.bezier_making(list_of_bezier_set1)
    plt.show()
    #making_TVP(self, x_ref, y_ref, vell_want, vell_start, vell_end, P_start, time_start):
    TVP1.making_TVP(list_of_bezier1.T[0], list_of_bezier1.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
    plt.show()

if __name__ == '__main__':
    print("++  + start +  ++")
    main()
    print("++  +  end  +  ++")
