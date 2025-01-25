import Rover


def test_init():
    rover = Rover.Rover()
    assert rover.direction == 'EAST'
    assert rover.coords == [0, 0]

def test_init_with_direction_north():
    rover = Rover.Rover(direction='NORTH')
    assert rover.direction == 'NORTH'
    assert rover.coords == [0, 0]

def test_init_with_coords():
    rover = Rover.Rover(coords=[1, 1])
    assert rover.direction == 'EAST'
    assert rover.coords == [1, 1]

def test_turn_right_from_north():
    rover = Rover.Rover(direction='NORTH')
    rover.command('RIGHT')
    assert rover.direction == 'EAST'

def test_turn_left_from_north():
    rover = Rover.Rover(direction='NORTH')
    rover.command('LEFT')
    assert rover.direction == 'WEST'

def test_turn_right_from_east():
    rover = Rover.Rover(direction='EAST')
    rover.command('RIGHT')
    assert rover.direction == 'SOUTH'

def test_turn_left_from_east():
    rover = Rover.Rover(direction='EAST')
    rover.command('LEFT')
    assert rover.direction == 'NORTH'

def test_turn_left_from_west():
    rover = Rover.Rover(direction='WEST')
    rover.command('LEFT')
    assert rover.direction == 'SOUTH'

def test_move_forward_from_00_east():
    rover = Rover.Rover(direction='EAST', coords=[0, 0])
    rover.command('FORWARD')
    assert rover.direction == 'EAST'
    assert rover.coords == [1, 0]
