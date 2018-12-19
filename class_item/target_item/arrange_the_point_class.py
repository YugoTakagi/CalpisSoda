import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class arrange_the_point(object):
    """docstring for arrange_the_point."""
    delta_s = 0.0
    index = []
    def __init__(self):
        pass
    def arrange(self, bezier_set_x, bezier_set_y, TVP_of_S):
        print('+--+-start arrange-+--+')
        index_for_TVP = 0
        count = 0
        Ib = np.arange(start=0.0, stop=len(bezier_set_x)-1, step=1, dtype= int)
        #print('Ib = {}'.format(Ib))
        for index_for_bezier in Ib:
            if (index_for_bezier-1) < 0:
                dx = bezier_set_x[index_for_bezier]
                dy = bezier_set_y[index_for_bezier]
            else:
                dx = bezier_set_x[index_for_bezier] - bezier_set_x[index_for_bezier-1]
                dy = bezier_set_y[index_for_bezier] - bezier_set_y[index_for_bezier-1]
            ds = np.sqrt(dx**2 + dy**2)
            self.delta_s = self.delta_s + ds
            error = TVP_of_S[index_for_TVP] - self.delta_s
            if error < 0:
                error = -1.0 * error
            else:
                pass
            if error < 4:
                self.index.append(index_for_bezier)
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
