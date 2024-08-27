from PIL import Image
import model
from ursina import *

from forest import Forest
from train import Train

class TrainsField:
    def __init__(self):
        self.model = model.Model()
        self.forest = Forest()
        self.plane = Entity(
            model='plane',
            scale=(20, 1, 20),
            texture='assets/background.png',
            rotation_x=0  # Remove rotation to keep plane flat
        )
        self.train = Train()

    def update(self, state):
        x, z, angle = state
        # print(f"TrainsField: x={x:.2f}, z={z:.2f}, angle={angle:.2f}")
        self.train.update(state)

    def set_model(self, model):
        model.attach(self)  # Attach to the model


