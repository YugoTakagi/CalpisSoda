

class pid(object):
    """docstring for pid."""
    KP = 0
    KI = 0
    KD = 0
    diff0 = 0
    diff1 = 0
    adjustment = 0
    integral = 0
    time = 0.1
    x=0

    def __init__(self):
        pass
    def set_present(self, pidx):
        self.x = pidx
    def set_gain(self, kp, ki, kd):
        self.KP = kp
        self.KI = ki
        self.KD = kd
    def run_pid(self, xref):
        self.diff0 = self.diff1;
        self.diff1 = xref - self.x;
        self.integral += ((self.diff1 + self.diff0) / 2)*self.time
        self.adjustment = self.KP*self.diff1 + self.KI*self.integral + self.KD*(self.diff1 - self.diff0) / self.time
        return self.adjustment
