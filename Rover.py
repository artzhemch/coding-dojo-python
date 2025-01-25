class Rover:
    rotations = {
        ('NORTH', 'LEFT'): 'WEST',
        ('NORTH', 'RIGHT'): 'EAST',
        ('EAST', 'LEFT'): 'NORTH',
        ('EAST', 'RIGHT'): 'SOUTH',  
        ('SOUTH', 'LEFT'): 'EAST', 
        ('SOUTH', 'RIGHT'): 'WEST', 
        ('WEST', 'LEFT'): 'SOUTH', 
        ('WEST', 'RIGHT'): 'NORTH',
    }
    moves = {
        ('NORTH', 'BACKWARD'): [0, -1],
        ('NORTH', 'FORWARD'): [0, 1],
        ('EAST', 'BACKWARD'): [-1, 0],
        ('EAST', 'FORWARD'): [1, 0],
        ('SOUTH', 'BACKWARD'): [0, 1],
        ('SOUTH', 'FORWARD'): [0, -1],
        ('WEST', 'BACKWARD'): [1, 0],
        ('WEST', 'FORWARD'): [-1, 0]
    }

    def __init__(self, direction='EAST', coords=None):
        self.direction = direction
        if coords:
            self.coords = coords
        else:
            self.coords = [0, 0] # x, y

    def command(self, command):
        if command in ['RIGHT', 'LEFT']:
            self.direction = self.rotations[(self.direction, command)]
        elif command in ['FORWARD', 'BACKWARD']:
            self.coords = [
                self.coords[0] + self.moves[(self.direction, command)][0],
                self.coords[1] + self.moves[(self.direction, command)][1],
            ]
            # if self.direction == 'EAST' and command == 'FORWARD':
            #     self.coords = [self.coords[0] + 1, self.coords[1]]
            # elif self.direction == 'EAST' and command == 'BACKWARD':
            #     self.coords = [self.coords[0] - 1, self.coords[1]]
            # elif self.direction == 'SOUTH' and command == 'BACKWARD':
            #     self.coords = [self.coords[0], self.coords[1] + 1]
