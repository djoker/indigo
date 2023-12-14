from .stats import Stats


class Capture(object):
    def __init__(self) -> None:
        self.data = []

    def add(self, item: int) -> None:
        if type(item) == int:
            self.data.append(item)
        else:
            raise ValueError("Invalid Value: must to be a integer")

    def build_stats(self) -> Stats:
        return Stats(self.data)
