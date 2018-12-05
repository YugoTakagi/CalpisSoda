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
    IND = np.arange(start = 0,stop = 100, step = 1, dtype = int)
    for index in IND:
        print('index = {}'.format(index))
        cy.using_model(0,0.6,0,0)
        stateX, stateY = sov.using_algo(cy.get_v1()*dt, cy.get_v2()*dt, cy.get_v3()*dt)

        cy.set_state(stateX, stateY, 0)
        plt.plot(stateX, stateY, marker="o")
        plt.pause(0.01)
        plt.show

if __name__ == '__main__':
    print("++  + start +  ++")
    main()
    print("++  +  end  +  ++")
