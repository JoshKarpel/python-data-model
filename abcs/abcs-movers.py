import abc


class Mover(abc.ABC):
    def __init__(self, starting_location):
        self.current_location = starting_location

    @abc.abstractmethod
    def move_to(self, new_location):
        raise NotImplementedError

    def trip(self, route):
        for location in route:
            self.move_to(location)

