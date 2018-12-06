from omu3_ikm import omu3
from pid import pid
from synthesis_of_vector import synthesis_of_vector

from class_item.bezier_class import bezier
from class_item.TVP_class import trapezoidal_velocity_profile
from class_item.color_class import pycolor as pc

import numpy as np
import math
import matplotlib.pyplot as plt
import csv

def main():
    cy = omu3()
    sov = synthesis_of_vector()
    dt = 0.08
    theta = 0.0#np.pi/4
    alfa = 0

    number_of_index = 1000
    ############################################################################
    ############################################################################
    bez = bezier(number_of_index)
    TVP1 = trapezoidal_velocity_profile()

    list_of_bezier_set1 = np.array([[7*74,7*74],[4000,(25*74+46*74)/2],[-800,(25*74+46*74)/2],[17*74,(66*74+46*74)/2]], dtype=np.float)
    nplist_of_bezier1 = bez.bezier_making(list_of_bezier_set1)
    plt.show()
    TVP1.making_TVP(nplist_of_bezier1.T[0], nplist_of_bezier1.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
    plt.show()
    ############################################################################
    ############################################################################
    IND = np.arange(start = 0,stop = number_of_index, step = 1, dtype = int)
    plt.plot(0, 0, marker="*")
    for index in IND:
        #print('index = {}'.format(index))
        cy.using_model(nplist_of_bezier1.T[0][index],nplist_of_bezier1.T[1][index],theta,alfa)
        sov.get_alfa(alfa)
        stateX, stateY = sov.using_algo(cy.get_v1(), cy.get_v2(), cy.get_v3())
        cy.set_state(stateX, stateY, 0)
        if index==0:
            plt.plot(stateX, stateY, marker="*")
        elif index < number_of_index/2:
            plt.plot(stateX, stateY, marker="p", color="#4278C5")
        else:
            plt.plot(stateX, stateY, marker="o", color="#F56260")
        plt.pause(0.001)
        plt.axis("equal")
        plt.grid(True)
        plt.show

if __name__ == '__main__':
    print("++  + start +  ++")
    main()
    print("++  +  end  +  ++")
