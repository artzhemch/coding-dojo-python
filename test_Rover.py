import Rover


def test_init():
    rover = Rover.Rover()
    assert rover.direction == 'EAST'
    assert rover.coords == [0, 0]


def test_turn_right():
    rover = Rover.Rover()
    assert rover.direction == 'NORTH'
    rover.command('RIGHT')
    assert rover.direction == 'EAST'
