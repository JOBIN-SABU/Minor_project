import math


class NestingTracker:
    def __init__(self):
        self.stack = []
        self.max_depth = 0
        self.total_loop_cost = 0

    def enter_loop(self, iterations):
        self.stack.append(iterations)
        self.max_depth = max(self.max_depth, len(self.stack))

        current_cost = math.prod(self.stack)
        self.total_loop_cost += current_cost

    def exit_loop(self):
        if self.stack:
            self.stack.pop()

    def get_results(self):
        return {
            "max_depth": self.max_depth,
            "loop_cost": self.total_loop_cost
        }