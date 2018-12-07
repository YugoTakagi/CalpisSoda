from omu3_ikm import omu3
from pid import pid
from synthesis_of_vector import synthesis_of_vector

from class_item.bezier_class import bezier
from class_item.TVP_class import trapezoidal_velocity_profile
from class_item.color_class import pycolor as pc
from class_item.state_class import State

import numpy as np
import math
import matplotlib.pyplot as plt
import csv

def main():
    cy = omu3()
    sov = synthesis_of_vector()
    dt = 0.08
    theta = np.pi/4

    number_of_index = 100
    list_of_bezier1 = np.array([])
    state = State(x=0.0, y=-0.0, yaw=0.0)
    ############################################################################
    ############################################################################
    bez = bezier(number_of_index)
    TVP1 = trapezoidal_velocity_profile()

    #list_of_bezier_set1 = np.array([[7*74,7*74],[4000,(25*74+46*74)/2],[-800,(25*74+46*74)/2],[17*74,(66*74+46*74)/2]], dtype=np.float)
    list_of_bezier_set1 = np.array([[0,0],[1225,0],[1225+500,2000-1225],[1225+500,2000]], dtype=np.float)
    list_of_bezier_set2 = np.array([[1225+500,2000],[1225+500,2000+500],[1225-500,2000+1500-500],[1225-500,2000+1500]], dtype=np.float)
    list_of_bezier_set3 = np.array([[1225-500,2000+1500],[1225-500,2000+1500+500],[1225+500,2000+1500+1500-500],[1225+500,2000+1500+1500]], dtype=np.float)
    list_of_bezier_set4 = np.array([[1225+500,2000+1500+1500],[1225+500,2000+1500+1500+500],[1225,2000+1500+1500+1500-500],[1225,2000+1500+1500+1500]], dtype=np.float)

    nplist_of_bezier1, list_of_bezier1 = bez.bezier_making(list_of_bezier_set1)
    nplist_of_bezier2, list_of_bezier2 = bez.bezier_making(list_of_bezier_set2)
    nplist_of_bezier3, list_of_bezier3 = bez.bezier_making(list_of_bezier_set3)
    nplist_of_bezier4, list_of_bezier4 = bez.bezier_making(list_of_bezier_set4)

    LOB = []
    LOB.extend(list_of_bezier1)
    LOB.extend(list_of_bezier2)
    LOB.extend(list_of_bezier3)
    LOB.extend(list_of_bezier4)
    npLOB = np.array(LOB)


    plt.show()
    TVP1.making_TVP(npLOB.T[0], npLOB.T[1], 2.0, 0.0, 0.0, 0.0, 0.0)
    plt.show()
    ############################################################################
    ############################################################################
    r_of_stateAlfa = 5
    print("len(LOB) = {}".format(len(LOB)))
    IND = np.arange(start = 0,stop = len(LOB), step = 1, dtype = int)
    plt.plot(0, 0, marker="$start$", markersize="20")
    for index in IND:
        state.update(cy.get_v1(), cy.get_v2(), cy.get_v3())
        cy.using_model(state, npLOB.T[0][index], npLOB.T[1][index], theta, index)
        #cy.using_model(state, 0, 10, 0, index)
        if index==0:
            plt.plot(state.x, state.y, marker="*")
            plt.plot(state.x+r_of_stateAlfa*np.sin(state.yaw), state.y+r_of_stateAlfa*np.cos(state.yaw), marker=".", color="#0AB721")
        elif index < len(LOB)/2:
            plt.plot(state.x, state.y, marker="p", color="#4278C5")
            plt.plot(state.x+r_of_stateAlfa*np.sin(state.yaw), state.y+r_of_stateAlfa*np.cos(state.yaw), marker=".", color="#0AB721")
            r_of_stateAlfa += 0.2
        else:
            plt.plot(state.x, state.y, marker="o", color="#F56260")
            plt.plot(state.x+r_of_stateAlfa*np.sin(state.yaw), state.y+r_of_stateAlfa*np.cos(state.yaw), marker=".", color="#0AB721")
            r_of_stateAlfa += 0.2
        plt.pause(0.01)
        plt.axis("equal")
        plt.grid(True)
        plt.show

if __name__ == '__main__':
    print("++  + start +  ++")
    main()
    print("++  +  end  +  ++")
