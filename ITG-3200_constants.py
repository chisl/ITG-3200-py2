#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""ITG-3200: Single-chip, digital-output, 3-axis MEMS gyro"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["InvenSense Inc."]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

class REG:
	WhoAmI = 0
	SampleRateDivider = 21
	DLPF = 22
	InterruptConfiguration = 23
	InterruptStatus = 26
	TEMP_OUT = 27
	GYRO_XOUT = 29
	GYRO_YOUT = 31
	GYRO_ZOUT = 33
	PowerManagement = 62
