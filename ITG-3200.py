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

from ITG_3200_constants import *

# name:        ITG-3200
# description: Single-chip, digital-output, 3-axis MEMS gyro
# manuf:       InvenSense Inc.
# version:     0.1
# url:         https://www.invensense.com/products/motion-tracking/3-axis/itg-3200/
# date:        2016-08-01


# Derive from this class and implement read and write
class ITG_3200_Base:
	"""Single-chip, digital-output, 3-axis MEMS gyro"""
	# Register WhoAmI
	# verify the identity of the device. 
	
	def setWhoAmI(self, val):
		"""Set register WhoAmI"""
		self.write(REG.WhoAmI, val, 8)
	
	def getWhoAmI(self):
		"""Get register WhoAmI"""
		return self.read(REG.WhoAmI, 8)
	
	# Bits unused_0
	# Bits ID
	# Contains the I2C address of the device, which can also be changed by writing to this register. 
	# Bits unused_1
	# Register SampleRateDivider
	# This register determines the sample rate of the ITG-3200 gyros. The gyros outputs are sampled internally at
	#       either 1kHz or 8kHz, determined by the DLPF_CFG setting (see register 22). This sampling is then filtered
	#       digitally and delivered into the sensor registers after the number of cycles determined by this register.
	#       The sample rate is given by the following formula:
	#       Fsample = Finternal / (divider+1),
	#       where Finternal is either 1kHz or 8kHz 
	
	
	def setSampleRateDivider(self, val):
		"""Set register SampleRateDivider"""
		self.write(REG.SampleRateDivider, val, 8)
	
	def getSampleRateDivider(self):
		"""Get register SampleRateDivider"""
		return self.read(REG.SampleRateDivider, 8)
	
	# Bits SampleRateDivider
	# Register DLPF
	
	
	def setDLPF(self, val):
		"""Set register DLPF"""
		self.write(REG.DLPF, val, 8)
	
	def getDLPF(self):
		"""Get register DLPF"""
		return self.read(REG.DLPF, 8)
	
	# Bits unused_0
	# Bits FS_SEL
	# Set the full-scale range of the gyro sensors. The power-on-reset value of FS_SEL is 00h.
	#           Set to 03h for proper operation. 
	
	# Bits DLPF_CFG
	# Register InterruptConfiguration
	# This register configures the interrupt operation of the device. The interrupt output pin (INT) configuration can be set, the interrupt latching/clearing method can be set, and the triggers for the interrupt can be set.<br>
	#       Note that if the application requires reading every sample of data from the ITG-3200 part, it is best to enable the raw data ready interrupt (RAW_RDY_EN). This allows the application to know when new sample data is available. 
	
	
	def setInterruptConfiguration(self, val):
		"""Set register InterruptConfiguration"""
		self.write(REG.InterruptConfiguration, val, 8)
	
	def getInterruptConfiguration(self):
		"""Get register InterruptConfiguration"""
		return self.read(REG.InterruptConfiguration, 8)
	
	# Bits ACTL
	# Logic level for INT output pin 
	# Bits OPEN
	# Drive type for INT output pin 
	# Bits LATCH_INT_EN
	# Latch mode 
	# Bits INT_ANYRD_2CLEAR
	# Latch clear method 
	# Bits reserved_0
	# Bits ITG_RDY_EN
	# Enable interrupt when device is ready (PLL ready after changing clock source) 
	# Bits reserved_1
	# Bits RAW_RDY_EN
	# Enable interrupt when data is available 
	# Register InterruptStatus
	# Whenever one of the interrupt sources is triggered, the corresponding bit will be set. The polarity of the interrupt pin (active high/low) and the latch type (pulse or latch) has no affect on these status bits. 
	
	def setInterruptStatus(self, val):
		"""Set register InterruptStatus"""
		self.write(REG.InterruptStatus, val, 8)
	
	def getInterruptStatus(self):
		"""Get register InterruptStatus"""
		return self.read(REG.InterruptStatus, 8)
	
	# Bits RAW_DATA_RDY
	# Raw data is ready
	# Bits unused_0
	# Bits ITG_RDY
	# PLL ready
	# Bits unused_1
	# Register TEMP_OUT
	# 16-bit temperature data (2's complement format)
	#       At any time, these values can be read from the device; however it is best to use the interrupt function to determine when new data is available 
	
	
	def setTEMP_OUT(self, val):
		"""Set register TEMP_OUT"""
		self.write(REG.TEMP_OUT, val, 16)
	
	def getTEMP_OUT(self):
		"""Get register TEMP_OUT"""
		return self.read(REG.TEMP_OUT, 16)
	
	# Bits TEMP_OUT
	# Register GYRO_XOUT
	# 16-bit X gyro output data (2's complement format)
	#       At any time, these values can be read from the device; however it is best to use the interrupt function to determine when new data is available 
	
	
	def setGYRO_XOUT(self, val):
		"""Set register GYRO_XOUT"""
		self.write(REG.GYRO_XOUT, val, 16)
	
	def getGYRO_XOUT(self):
		"""Get register GYRO_XOUT"""
		return self.read(REG.GYRO_XOUT, 16)
	
	# Bits GYRO_XOUT
	# Register GYRO_YOUT
	# 16-bit Y gyro output data (2's complement format)
	#       At any time, these values can be read from the device; however it is best to use the interrupt function to determine when new data is available 
	
	
	def setGYRO_YOUT(self, val):
		"""Set register GYRO_YOUT"""
		self.write(REG.GYRO_YOUT, val, 16)
	
	def getGYRO_YOUT(self):
		"""Get register GYRO_YOUT"""
		return self.read(REG.GYRO_YOUT, 16)
	
	# Bits GYRO_YOUT
	# Register GYRO_ZOUT
	# 16-bit Y gyro output data (2's complement format)
	#       At any time, these values can be read from the device; however it is best to use the interrupt function to determine when new data is available 
	
	
	def setGYRO_ZOUT(self, val):
		"""Set register GYRO_ZOUT"""
		self.write(REG.GYRO_ZOUT, val, 16)
	
	def getGYRO_ZOUT(self):
		"""Get register GYRO_ZOUT"""
		return self.read(REG.GYRO_ZOUT, 16)
	
	# Bits GYRO_ZOUT
	# Register PowerManagement
	# Setting the SLEEP bit in the register puts the device into very low power sleep mode. In this mode, only the serial interface and internal registers remain active, allowing for a very low standby current. Clearing this bit puts the device back into normal mode. To save power, the individual standby selections for each of the gyros should be used if any gyro axis is not used by the application. 
	
	def setPowerManagement(self, val):
		"""Set register PowerManagement"""
		self.write(REG.PowerManagement, val, 8)
	
	def getPowerManagement(self):
		"""Get register PowerManagement"""
		return self.read(REG.PowerManagement, 8)
	
	# Bits CLK_SEL
	# Bits STBY_ZG
	# Bits STBY_YG
	# Bits STBY_XG
	# Bits SLEEP
	# Puts the device into very low power sleep mode. In this mode, only the serial interface
	#           and internal registers remain active, allowing for a very low standby current.
	#           Clearing this bit puts the device back into normal mode. To save power, the individual
	#           standby selections for each of the gyros should be used if any gyro axis is not used
	#           by the application. 
	
	# Bits H_RESET
