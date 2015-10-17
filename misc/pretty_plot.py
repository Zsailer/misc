import numpy as np
import matplotlib.pyplot as plt

def pretty_plot(ax, xlabel="x data", ylabel="y data", title="title",
                scale=0.1, xlims=None, ylims=None, n_xticks=5, n_yticks=5, axis=None):
    """ Make matplotlib pretty.

        Arguments:

        scale: float

        xlims: limits for xticks

        ylims: limits for yticks

        n_xticks: number of x ticks

        n_yticks: number of y ticks
    """
    xdata = [l.get_xdata()[0] for l in ax.lines]
    ydata = [l.get_ydata()[0] for l in ax.lines]

    # Format plots
    xmax = max(xdata)
    xmin = min(xdata)
    ymax = max(ydata)
    ymin = min(ydata)

    dx = abs(xmax - xmin)
    dy = abs(ymax - ymin)

    xupper = xmax + scale*(dx)
    xlower = xmin - scale*(dx)
    yupper = ymax + scale*(dy)
    ylower = ymin - scale*(dy)

    # Set axis bounds
    if axis is None:
        axis = [xlower, xupper, ylower, yupper]
    ax.axis(axis)

    if xlims is not None:
        xmin = xlims[0]
        xmax = xlims[1]

    if ylims is not None:
        ymin = ylims[0]
        ymax = ylims[1]

    # Set vertical axis
    ax.set_yticks(np.linspace(ymax, ymin, n_yticks))
    ax.spines['left'].set_bounds(ymax, ymin)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_ticks_position("left")

    #Set horizontal axis
    ax.set_xticks(np.linspace(xmax, xmin, n_xticks))
    ax.spines['bottom'].set_bounds(xmax, xmin)
    ax.spines["top"].set_visible(False)
    ax.xaxis.set_ticks_position("bottom")

    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.set_title(title, fontsize=16)

    return ax
