from preprocess.utils.utils import compute_volume_stats

import numpy as np 
import logging

class Test_Utils:
    def test_zeros_compute_volume_stats(self):
        """Test compute_volume_stats with a volume of zeros."""
        zero_vol = np.zeros((10, 10))
        median, mean, std, minimum, maximum, percentile_99_5, percentile_00_5 = compute_volume_stats(zero_vol)
        logging.info("median: {}, mean: {}, std: {}, min: {}, max: {}, 99.5%: {}, 00.5%: {}".format(median, mean, std,
                                                                                                minimum, maximum,
                                                                                                percentile_99_5, 
                                                                                                percentile_00_5))
        assert median == 0
        assert mean == 0
        assert std == 0
        assert minimum == 0
        assert maximum == 0
        assert percentile_99_5 == 0
        assert percentile_00_5 == 0
   