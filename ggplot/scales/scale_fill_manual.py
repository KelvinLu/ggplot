from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from .scale import scale
from copy import deepcopy


class scale_fill_manual(scale):
    """
    Specify a list of fill colors, for geom_bar, to use manually.

    Parameters
    ----------
    values : list of colors/strings
        List of colors with length greater than or equal to the number
        of unique discrete items to which you want to apply color.
    """
    VALID_SCALES = ['values']
    def __radd__(self, gg):
        gg = deepcopy(gg)
        if not (self.values is None):
            n_colors_needed = gg.data[gg.aesthetics['fill']].nunique()
            n_colors_provided = len(self.values)
            if n_colors_provided < n_colors_needed:
                msg = 'Error: Insufficient values in manual scale. {0} needed but only {1} provided.'
                raise Exception(msg.format(n_colors_needed, n_colors_provided))
            gg.manual_fill_list = self.values[:n_colors_needed]
        return gg

