import observer
import math
import time
import threading

class Model(observer.Subject):
    def __init__(self):
        super().__init__()
        self._state = (1, 0)  # Starting point (1, 0)
        self._angle = 0
        self._radius = 1.06
        self._update_thread = threading.Thread(target=self._update_loop)
        self._update_thread.daemon = True

    def set_state(self, state):
        self._state = state
        self.notify()

    def get_state(self):
        return self._state

    def _update_loop(self):
        while True:
            self._update()
            time.sleep(0.05)

    def _update(self):
        # Increase the angle (in radians)
        self._angle += (math.pi/180)*0.6  # You can adjust this value to change the speed of rotation

        # Calculate new x and z coordinates
        x = self._radius * math.cos(self._angle)
        z = self._radius * math.sin(self._angle)

        # Update the state
        new_state = (x, z, self._angle)
        self.set_state(new_state)

    def start(self):
        self._update_thread.start()

    def wait_for_stop(self):
        self._update_thread.join()