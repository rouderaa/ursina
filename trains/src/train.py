from ursina import *
from roundrobinbuffer import *

class Train:
    def __init__(self):
        self.positions = RoundRobinBuffer(100)
        self.carriages = []
        self.carriages.append(
            Entity(model='assets/train-carriage-container-blue.glb', scale=0.5, position=(5, -10, 10))
        )
        self.carriages.append(
            Entity(model='assets/train-carriage-dirt.glb', scale=0.5, position=(5, -10, 10))
        )
        self.carriages.append(
            Entity(model='assets/train-carriage-lumber.glb', scale=0.5, position=(5, -10, 10))
        )
        self.carriages.append(
            Entity(model='assets/train-carriage-coal.glb', scale=0.5, position=(5, -10, 10))
        )
        self.carriages.append(
            Entity(model='assets/train-locomotive-b.glb', scale=0.5, position=(5, -10, 10))
        )

    def update(self, state):
        x, z, angle = state
        self.positions.push((x, z, angle))
        self.draw(x, z, angle)

    def draw(self, x, z, angle):
        position = 0
        for carriage in self.carriages:
            pos = self.positions.peek(position)
            if pos is not None:
                x, z, angle = pos
                carriage.position = (x * 6, 0, z * 6)
                carriage.rotation = (0, ((-angle / math.pi) * 180) + 180, 0)  # in DEGREES
            position += 21
