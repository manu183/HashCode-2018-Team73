class Ride:
    def __init__(self, start_position, target_position, earliest_start, latest_finish):
        self.s_position = start_position
        self.t_position = target_position
        self.distance = (target_position[1] - start_position[1]) + (target_position[0] - target_position[0])
        self.earliest_start = earliest_start
        self.latest_finish = latest_finish
