#!/usr/bin/python
#
# Runs verious statistics against data bundle
#
#######################################################

import numpy as np
from sklearn import calibration



ccv_bad = calibration.CalibratedClassifierCV()
ccv_good = calibration.CalibratedClassifierCV()
