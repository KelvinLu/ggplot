from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy


class scale_shape_manual(scale):
    """
    Specify a list of shapes to use manually.

    Parameters
    ----------
    values : list of shapes/strings
        List of shapes with length greater than or equal to the number
        of unique discrete items to which you want to apply shape.

    Examples
    --------
    >>> from ggplot import *
    >>> shape_list = ['o', '^', 's', 'p', '*']
    >>> gg = ggplot(diamonds, aes('carat', 'price', shape='cut')) + \\
    ...     geom_point()
    >>> print(gg + scale_shape_manual(values=shape_list) + \\
    ...     ggtitle('With manual shapes'))
    >>> print(gg + ggtitle('Without manual shapes'))
    """
    VALID_SCALES = ['values']
    def __radd__(self, gg):
        gg = deepcopy(gg)
        if not (self.values is None):
            n_shapes_needed = gg.data[gg.aesthetics['shape']].nunique()
            n_shapes_provided = len(self.values)
            if n_shapes_provided < n_shapes_needed:
                msg = 'Error: Insufficient values in manual scale. {0} needed but only {1} provided.'
                raise Exception(msg.format(n_shapes_needed, n_shapes_provided))
            gg.manual_shape_list = self.values[:n_shapes_needed]
        return gg

