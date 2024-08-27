import os
from random import random
import math
from ursina import Entity

class Forest:
    def __init__(self):
        # list all assets that start with tree
        assets_directory = os.listdir("assets")
        self.tree_assets = [asset for asset in assets_directory if asset.startswith("tree_pine")]
        self.plant_trees()

    def plant_trees(self):
        self.trees = []
        for i in range(80):
            # random position not on the railway track
            angle = random() * 2 * math.pi
            radius = random() * 2.8 + 7
            tree_asset_index = random() * len(self.tree_assets)
            tree = Entity(
                model=f"assets/{self.tree_assets[int(tree_asset_index)]}",
                scale = 1.2,
                position=(radius * math.cos(angle), 0, radius * math.sin(angle))
            )
            print(tree.texture)
            self.trees.append(tree)

    def add_tree(self, tree):
        self.trees.append(tree)

    def grow(self):
        for tree in self.trees:
            tree.grow()