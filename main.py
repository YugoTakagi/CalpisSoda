from omu3_ikm import omu3
from pid import pid
from synthesis_of_vector import synthesis_of_vector

import numpy as np
import math
import matplotlib.pyplot as plt
import csv

def main():
    cy = omu3()
    sov = synthesis_of_vector()
    dt = 0.08
    alfa = 0.0
    IND = np.arange(start = 0,stop = 100, step = 1, dtype = int)
    for index in IND:
        #print('index = {}'.format(index))
        cy.using_model(0,1,alfa,0)
        sov.get_alfa(alfa)
        stateX, stateY = sov.using_algo(cy.get_v1(), cy.get_v2(), cy.get_v3())
        cy.set_state(stateX, stateY, 0)
        if index==0:
            plt.plot(stateX, stateY, marker="*")
        elif index < 50:
            plt.plot(stateX, stateY, marker="p")
        else:
            plt.plot(stateX, stateY, marker="o")
        plt.pause(0.1)
        plt.axis("equal")
        plt.grid(True)
        plt.show

if __name__ == '__main__':
    print("++  + start +  ++")
    main()
    print("++  +  end  +  ++")
