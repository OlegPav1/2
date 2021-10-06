class Quadcopter(object):
    def wifi_line(self,  x, y):
        raise NotImplementedError()

class Phantom_4_PRO(Quadcopter):
    def wifi_line(self,  x, y):
        print('Quadcopter activ. Coordinate point - ({}, {})'.format(x, y))

class RemoteControlBase(object):
    def __init__(self):
        self._signal = self.get_signal()
    def get_signal(self):
        raise NotImplementedError()
    def wifi_line(self, x, y):
        self._signal.wifi_line(x, y)

class RemoteComtrol(RemoteControlBase):
    def __init__(self):
        super(RemoteComtrol, self).__init__()
        self._line = 0
    def get_signal(self):
        return Phantom_4_PRO()
    def wifi_line(self, x, y):
        super(RemoteComtrol, self).wifi_line(x, y)
        self._x = x
        self._y = y
    def go_left(self):
        self._x += 1
        self.wifi_line(self._x)
    def go_right(self):
        self._x -= 1
        self.wifi_line(self._x)
    def go_forward(self):
        self._y += 1
        self.wifi_line(self._y)
    def go_back(self):
        self._y -= 1
        self.wifi_line(self._y)

remote_control = RemoteComtrol()
remote_control.wifi_line(2, 3)