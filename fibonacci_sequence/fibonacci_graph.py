from matplotlib import pyplot


class FibonacciGraph:
    def __init__(self, x_values, y_values):
        self.x_values = x_values
        self.y_values = y_values
        self.x_axis_max = x_values[-1]
        self.y_axis_max = y_values[-1]
        self.title = 'Fibonacci Graph'
        self.xlabel = 'Fibonacci Sequence Number'
        self.ylabel = 'Fibonacci Sequence Value'

    def plot_fibonacci_sequence(self):
        pyplot.plot(self.x_values, self.y_values, 'bo-')
        pyplot.title(self.title, fontsize=24)
        pyplot.xlabel(self.xlabel, fontsize=12)
        pyplot.ylabel(self.ylabel, fontsize=12)
        pyplot.tick_params(axis='both', which='major', labelsize=14)
        pyplot.xticks(self.x_values)
        pyplot.yticks(self.y_values)
        pyplot.axis([0, self.x_axis_max, 0, self.y_axis_max])
        pyplot.show()
