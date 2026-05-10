import numpy as np

class Race:
    def __init__(self, space, lanes):
        self.space = space
        self.lane = lanes

# Create the space
space = np.zeros((400, 400))

# Create the lanes
lanes = {
    'verde': { 'start_x': 0, 'finish_x': 400,'y': 100},
    'rojo': {'start_x': 0, 'finish_x': 400,'y': 200},
    'azul': {'start_x': 0, 'finish_x': 400,'y': 300},
    'amarillo': {'start_x': 0, 'finish_x': 400,'y': 400}
}