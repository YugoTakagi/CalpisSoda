import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
class bezier(object):
    """docstring for bezier."""
    number_of_points = 0
    def __init__(self,number_of_points):
        self.number_of_points = number_of_points
    def comb(self, n, k):
        m = 1
        if n < 2 * k:
            k = n - k
        for i in xrange(1, k + 1):
            m = m * (n - i + 1) / i
        return m
    def bernstein(self, n, i, t):
        return self.comb(n, i) * t**i * (1 - t)**(n-i)
    def bezier(self, n, t, q):
        p = np.zeros(2)
        for i in range(n + 1):
            p += self.bernstein(n, i, t) * q[i]
        return p
    def bezier_making(self, bezier_set1):
        list_of_bezier = []
        for t in np.linspace(0, 1, self.number_of_points):
            list_of_bezier.append(self.bezier(3,t,bezier_set1))
        LOBS1 = np.array(list_of_bezier)
        plt.plot(LOBS1.T[0], LOBS1.T[1])
        plt.axis("equal")
        plt.grid(True)
        plt.show()
        return LOBS1, list_of_bezier
    def new_bezier_plt(self, list_of_bezier, new_index_for_bezier, len_new_index_for_bezier):
        '''ten ha sikkari haitte iru.
        plt.plot(list_of_bezier.T[0],list_of_bezier.T[1], marker="*", color="#4278C5")
        plt.axis("equal")
        plt.grid(True)
        plt.show()
        '''
        IND = np.arange(start=0, stop=len_new_index_for_bezier-1, step=1, dtype= int)
        new_lobs = []
        for ind in IND:
            new_lobs.append(list_of_bezier[new_index_for_bezier[ind]])
        NEW_LOBS = np.array(new_lobs)
        plt.plot(NEW_LOBS.T[0], NEW_LOBS.T[1], marker="o")
        plt.axis("equal")
        plt.grid(True)
        plt.show()
        return NEW_LOBS, new_lobs
