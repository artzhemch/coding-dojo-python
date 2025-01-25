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

    def __init__(self, direction='EAST', coords=None):
        self.direction = direction
        if coords:
            self.coords = coords
        else:
            self.coords = [0, 0] # x, y

    def command(self, command):
        self.direction = self.rotations[(self.direction, command)]
