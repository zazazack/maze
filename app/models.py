"""Data Models."""
import shutil


class Grid(object):
    """Grid object."""

    def __init__(self):
        """Initialize the object."""
        super(object, self).__init__()
        self.width, self.height = shutil.get_terminal_size()
        self.shape = self.width, self.height

    def __init_subclass(cls, **kwargs):
        super().__init_subclass(**kwargs)

    def shape(self):
        return (self.row, self.col)

    def grid(self):
        cel = '[ ]'
        row = cel * self.width
        [print(row) for row in row * self.height]

grid = Grid()

grid.grid()
