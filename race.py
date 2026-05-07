import numpy as np

class Race:
    def __init__(self, space, lanes):
        self.space = space
        self.lane = lanes

# Create the space
space = np.zeros((400, 400))

# Create the lanes
lanes = {
    'green': { 'start_x': 0, 'finish_x': 400,'y': 100},
    'red': {'start_x': 0, 'finish_x': 400,'y': 200},
    'blue': {'start_x': 0, 'finish_x': 400,'y': 300},
    'yellow': {'start_x': 0, 'finish_x': 400,'y': 400}
}