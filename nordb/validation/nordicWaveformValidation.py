import os
import sys

if __name__=="__main__":
	os.chdir("../..")

from nordb.validation import validationTools 
from nordb.validation.validationTools import values

def validateWaveformHeader(header):
	validation = True
	mheader = 6

	if not validationTools.validateInteger(header.event_id,
											"event id",
											0,
											values.maxInt,
											False,
											mheader):
		validation = False

	if not validationTools.validateString(header.waveform_info,
									"waveform string",
									0,
									78,
									"",
									False,
									mheader):
		validation = False
	
	return validation	