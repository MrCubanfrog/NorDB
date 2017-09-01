from lxml import etree
import math
import sys
import time

sys.path.insert(0, '../nordic')
import nordicHandler
import psycopg2

QUAKEML_ROOT_STRING = '''<?xml version="1.0" encoding="US-ASCII" standalone="yes"?><q:quakeml xmlns:q="http://quakeml.org/xmlns/quakeml/1.2" xmlns="http://quakeml.org/xmlns/bed/1.2" xmlns:ingv="http://webservices.ingv.it/fdsnws/event/1"></q:quakeml>'''

AUTHORITY_ID = "wh.atis.ids"
NETWORK_CODE = "netcode"

EVENT_TYPE_CONVERSION = {' ': "not reported",  '*': "earthquake", 'Q': "earthquake", 'E':"explosion", 'P':"explosion" ,'I':"induced or triggered event" ,'V': "volcanic eruption", 'X':"landslide" }
PICK_POLARITY_CONVERSION = {'C': "positive", 'D': "negative", "+": "undecidable", "-": "undecidable"}
MAGNITUDE_TYPE_CONVERSION = {'L': 'ML', 'C': 'Mc', 'B': 'mb', 'S': 'Ms', 'W': 'MW'}
INSTRUMENT_TYPE_CONVERSION = {'S': 'SH','B': 'BH', 'L': 'LH'}

def addEventParameters(quakeml, nordic, long_quakeML):
	eventParameters = etree.SubElement(quakeml, "eventParameters")
	eventParameters.attrib["publicID"] = "smi:" + AUTHORITY_ID + "/path/to/event/parameter"
	
	addEvent(eventParameters, nordic, long_quakeML)

def addEvent(eventParameters, nordic, long_quakeML):
	#Add event
	event = etree.SubElement(eventParameters, "event")
	event.attrib["publicID"] = "smi:" + AUTHORITY_ID + "/path/to/event/"

	#Adding event type	
	event_type_txt = " "
	for header in nordic.get_main_headers():
		if header.event_desc_id is not None:
			event_type_txt = header.event_desc_id

	event_type = etree.SubElement(event, "type")
	event_type.text = EVENT_TYPE_CONVERSION[event_type_txt]

	#Adding event comments
	for header_comment in nordic.get_comment_headers():
		if header_comment.h_comment is not None:
			event_comment = etree.SubElement(event, "comment")
			event_comment_txt = etree.SubElement(event_comment, "text")
			event_comment_txt.text = header_comment.h_comment

	#Creating the all elements and their subelement
	for i in xrange(0,len(nordic.headers[1])):
		addOrigin(event, nordic, i)
		if long_quakeML:
			addMagnitude(event, nordic, i)
	
	for i in xrange(0, len(nordic.headers[5])):
		addFocalMech(event, nordic.headers[5][i])

	if long_quakeML:
		for phase_data in nordic.phase_data:
			addPick(event, nordic, phase_data)
			addAmplitude(event, nordic, phase_data)
			for origin in event.iter("origin"):
				addArrival(origin, phase_data, nordic)

def addPick(event, nordic, phase_data):
	pick = etree.SubElement(event, "pick")
	pick.attrib["publicID"] = "smi:" + AUTHORITY_ID + "/path/to/pick/" + str(phase_data.phase_id)

	time_value = ""
	#time value for the pick	
	if (phase_data.time_info == '+'):
		time_value = str(nordic.headers[1][0].date + datetime.timedelta(days=1)) + "T"
	elif (phase_data.time_info == '-'):
		time_value = str(nordic.headers[1][0].date - datetime.timedelta(days=1)) + "T"
	else:
		time_value = str(nordic.headers[1][0].date) + "T"

	if phase_data.hour < 10:
		time_value = time_value + "0" + str(phase_data.hour) + ":"
	else:
		time_value = time_value + str(phase_data.hour) + ":"

	if phase_data.minute < 10:
		time_value = time_value + "0" + str(phase_data.minute) + ":"
	else:
		time_value = time_value + str(phase_data.minute) + ":"

	if phase_data.second < 10:
		time_value = time_value + "0" + str(int(phase_data.second)) + "Z"
	else:
		time_value = time_value + str(int(phase_data.second)) + "Z" 

	addTime(pick, time_value, 0)

	#Pick waveform ID
	waveform_id = etree.SubElement(pick, "waveformID")
	waveform_id.attrib["networkCode"] = "" + NETWORK_CODE
	waveform_id.attrib["stationCode"] = phase_data.station_code.strip()
	if phase_data.sp_instrument_type is not None and phase_data.sp_component is not None:
		waveform_id.attrib["channelCode"] = INSTRUMENT_TYPE_CONVERSION[phase_data.sp_instrument_type] + phase_data.sp_component.strip()

	#Pick first motion
	if phase_data.first_motion is not None and phase_data.first_motion in PICK_POLARITY_CONVERSION:
		pick_polarity = etree.SubElement(pick, "polarity")	
		pick_polarity.text = PICK_POLARITY_CONVERSION[phase_data.first_motion]

	#Pick backazimuth
	if phase_data.back_azimuth is not None:
		pick_back_azimuth = etree.SubElement(pick, "backazimuth")
		pick_back_azimuth_value = etree.SubElement(pick_back_azimuth, "value")
		pick_back_azimuth_value.text = str(phase_data.back_azimuth)

def addAmplitude(event, nordic, phase_data):
	if phase_data.max_amplitude is not None:
		amplitude = etree.SubElement(event, "amplitude")
		amplitude.attrib["publicID"] = "smi:" + AUTHORITY_ID + "/path/to/amplitude/" + str(phase_data.phase_id)

		#adding generic amplitude
		generic_amplitude = etree.SubElement(amplitude, "genericAmplitude")
		generic_amplitude_value = etree.SubElement(generic_amplitude, "value")
		generic_amplitude_value.text = str(math.pow(phase_data.max_amplitude, -9)) #Convert to meters from nanometers

		#Adding amplitude period
		if phase_data.max_amplitude_period is not None:
			amplitude_period = etree.SubElement(amplitude, "period")
			amplitude_period_value = etree.SubElement(amplitude_period, "value")
			amplitude_period_value.text = str(phase_data.max_amplitude_period)

		#Adding amplitude unit
		amplitude_unit = etree.SubElement(amplitude, "unit")
		amplitude_unit.text = "m"

		#Adding time window
		if phase_data.signal_duration is not None:
			time_window = etree.SubElement(amplitude, "timeWindow")
			time_window_value = etree.SubElement(time_window, "value")
			time_window_value.text = str(phase_data.signal_duration)

		if phase_data.signal_to_noise is not None:
			snr = etree.SubElement(amplitude, "snr")
			snr.text = str(phase_data.signal_to_noise)

def addOrigin(event, nordic, i):
	origin = etree.SubElement(event, "origin")
	origin.attrib["publicID"] = "smi:" + AUTHORITY_ID + "/path/to/origin"

	#time value for the origin
	time_value = ""
	time_value = str(nordic.headers[1][i].date) + "T"

	if nordic.headers[1][i].hour is not None:
		if nordic.headers[1][i].hour < 10:
			time_value = time_value + "0" + str(nordic.headers[1][i].hour) + ":"
		else:
			time_value = time_value + str(nordic.headers[1][i].hour) + ":"
	else:
		time_value = time_value + "00:"

	if nordic.headers[1][i].minute is not None:
		if nordic.headers[1][i].minute < 10:
			time_value = time_value + "0" + str(nordic.headers[1][i].minute) + ":"
		else:
			time_value = time_value + str(nordic.headers[1][i].minute) + ":"
	else:
		time_value = time_value + "00:"
	
	if nordic.headers[1][i].second is not None:
		if nordic.headers[1][i].second < 10:
			time_value = time_value + "0" + str(int(nordic.headers[1][i].second)) + "Z"
		else:
			time_value = time_value + str(int(nordic.headers[1][i].second)) + "Z" 
	else:
		time_value = time_value + "00Z"

	#time uncertainty	
	time_uncertainty = 0
	for h_error in nordic.headers[5]:
		if h_error.header_main_id == nordic.headers[1][i]:
			time_uncertainty = h_error.second_error
			break

	addTime(origin, time_value, time_uncertainty)

	#Adding value for epicenter latitude
	if nordic.headers[1][i].epicenter_latitude is not None:
		origin_latitude = etree.SubElement(origin, "latitude")
		origin_latitude_value = etree.SubElement(origin_latitude, "value")
		origin_latitude_value.text = str(nordic.headers[1][i].epicenter_latitude)
		for h_error in nordic.headers[5]:
			if h_error.header_main_id == nordic.headers[1][i]:
				if h_error.epicenter_latitude_error is not None:
					origin_latitude_uncertainty = etree.SubElement(origin_latitude, "uncertainty")
					origin_latitude_uncertainty.text = str(h_error.epicenter_latitude_error)
				break

	#Adding value for epicenter longitude
	if nordic.headers[1][i].epicenter_longitude is not None:
		origin_longitude = etree.SubElement(origin, "longitude")
		origin_longitude_value = etree.SubElement(origin_longitude, "value")
		origin_longitude_value.text = str(nordic.headers[1][i].epicenter_longitude)
		for h_error in nordic.headers[5]:
			if h_error.header_main_id == nordic.headers[1][i]:
				if h_error.epicenter_longitude_error is not None:
					origin_longitude_uncertainty = etree.SubElement(origin_longitude, "uncertainty")
					origin_longitude_uncertainty.text = str(h_error.epicenter_longitude_error)
				break

	#Adding value for depth
	if nordic.headers[1][i].depth is not None:
		origin_depth = etree.SubElement(origin, "depth")
		origin_depth_value = etree.SubElement(origin_depth, "value")
		origin_depth_value.text = str(nordic.headers[1][i].depth * 1000)
		for h_error in nordic.headers[5]:
			if h_error.header_main_id == nordic.headers[1][i]:
				if h_error.depth_error is not None:
					origin_depth_uncertainty = etree.SubElement(origin_depth, "uncertainty")
					origin_depth_uncertainty.text = str(h_error.depth_error * 1000)
				break

	#Adding value for rms time residuals
	if nordic.headers[1][i].rms_time_residuals is not None:
		origin_quality = etree.SubElement(origin, "quality")
		origin_quality_standard_error = etree.SubElement(origin_quality, "standardError")
		origin_quality_standard_error.text = str(nordic.headers[1][i].rms_time_residuals)

def addMagnitude(event, nordic, i):
	if nordic.headers[1][i].magnitude_1 is not None:
		magnitude = etree.SubElement(event, "magnitude")
		magnitude.attrib["publicID"] = "smi:" + AUTHORITY_ID + "/path/to/magnitude"
		
		#Adding a value for magnitude
		magnitude_mag = etree.SubElement(magnitude, "mag")
		magnitude_mag_value = etree.SubElement(magnitude_mag, "value")
		magnitude_mag_value.text = str(nordic.headers[1][i].magnitude_1)
		if len(nordic.headers[5]) > 0:
			for h_error in nordic.headers[5]:
				if h_error.header_id == nordic.headers[1][i].header_id:
					if h_error.magnitude_error is not None:
						magnitude_mag_uncertainty = etree.SubElement(magnitude_mag, "uncertainty")
						magnitude_mag_uncertainty.text = str(h_error.magnitude_error)
					break

		#Adding magnitude type 
		if nordic.headers[1][i].type_of_magnitude_1 is not None and nordic.headers[1][i].type_of_magnitude_1 in MAGNITUDE_TYPE_CONVERSION:
			magnitude_type = etree.SubElement(magnitude, "type")
			magnitude_type.text = MAGNITUDE_TYPE_CONVERSION[nordic.headers[1][i].type_of_magnitude_1]
		
		#Adding number of stations 
		if nordic.headers[1][i].stations_used is not None:
			magnitude_station_count = etree.SubElement(magnitude, "stationCount")
			magnitude_station_count.text = str(nordic.headers[1][i].stations_used)

		if nordic.headers[1][i].magnitude_reporting_agency_1 is not None:
			magnitude_creation_info = etree.SubElement(magnitude, "creationInfo")
			magnitude_creation_info_agency = etree.SubElement(magnitude_creation_info, "agencyID")
			magnitude_creation_info_agency.text = nordic.headers[1][i].magnitude_reporting_agency_1
			magnitude_creation_info_agency_uri = etree.SubElement(magnitude_creation_info, "agencyURI")
			magnitude_creation_info_agency_uri.text = "smi:" + AUTHORITY_ID + "/path/to/agency"

		magnitude_origin_id = etree.SubElement(magnitude, "originID")
		magnitude_origin_id.text =  "smi:" + AUTHORITY_ID + "/path/to/origin"

def addArrival(origin, phase_data, nordic):
	if phase_data.phase_type is not None:
		arrival = etree.SubElement(origin, "arrival")
		arrival.attrib["publicID"] = "smi:" + AUTHORITY_ID + "/path/to/arrival/" + str(phase_data.phase_id)

		#Adding pick reference
		arrival_pick_id = etree.SubElement(arrival, "pickID")
		arrival_pick_id.text = "smi:" + AUTHORITY_ID + "/path/to/pick/" + str(phase_data.phase_id)

		#Adding phase
		arrival_phase = etree.SubElement(arrival, "phase")
		arrival_phase.text = phase_data.phase_type
	
		#Adding azimuth
		if phase_data.epicenter_to_station_azimuth is not None:
			arrival_azimuth = etree.SubElement(arrival, "azimuth")
			arrival_azimuth.text = str(phase_data.epicenter_to_station_azimuth)
	
		#Adding time residual
		if phase_data.travel_time_residual is not None:
			arrival_time_residual = etree.SubElement(arrival, "timeResidual")
			arrival_time_residual.text = str(phase_data.travel_time_residual)

		#Adding arrival distance
		if phase_data.epicenter_distance is not None:
			arrival_distance = etree.SubElement(arrival, "distance")
			arrival_distance.text = str(phase_data.epicenter_distance)

#TODO: See if station magnitude information can be found from somewhere. Without it stationMagnitude and staionMagnitudeContribution elements are useless.

#TODO: addStationMag
#def addStationMag(event, phase_data, nordic):
#	if phase_data.max_amplitude is not None:
#		station_magnitude = etree.SubElement(event, "stationMagnitude")
#		station_magnitude.attrib["publicID"] = "smi:" + AUTHORITY_ID + "/path/to/stationmag/"
#TODO: addStationMagContribution

#TODO: addFocalMech
def addFocalMech(event, h_error):
	if (h_error.gap is not None):
		focal_mechanism = etree.SubElement(event, "focalMechanism")
		focal_mechanism.attrib["publicID"] = "smi:" + AUTHORITY_ID + "/path/to/focalMech"
		
		#Adding Gap
		focal_mechanism_gap = etree.SubElement(focal_mechanism, "azimuthalGap")
		focal_mechanism_gap.text = str(h_error.gap)

def addTime(container, time_value, time_uncertainty):
	time = etree.SubElement(container, "time")
	value = etree.SubElement(time, "value")
	value.text = time_value

	if time_uncertainty != 0:
		uncertainty = etree.SubElement(time, "uncertainty")
		uncertainty.text = str(time_uncertainty)

def validateQuakeMlFile(test, parser, xmlschema):
	xmlschema.validate(etree.XML(test))
	try:
		etree.fromstring(test, parser)
		return True
	except:
		fErr = open("errorlogs/xml_error_" + str(time.time()) + ".log", 'w')
		log = xmlschema.error_log
		fErr.write(str(log))
		print "Error with XML validation. Check error log file " + fErr.name + " for more info!"	
		fErr.close()
		sys.exit(-1)

def nordicEventToQuakeMl(nordicEvent, long_quakeML):
	f = open("QuakeML-1.2.xsd")
	xmlschema_doc = etree.parse(f)
	f.close()

	quakeml = etree.XML(QUAKEML_ROOT_STRING)

	addEventParameters(quakeml, nordicEvent, long_quakeML)

	xmlschema = etree.XMLSchema(xmlschema_doc)
	parser = etree.XMLParser(schema=xmlschema)

	#Parse the tree to a string and back to the object because of a weird bug on validating the tree...
	test = etree.tostring(quakeml)
	quakeml = etree.XML(test)

	validateQuakeMlFile(test, parser, xmlschema)

	return quakeml

if __name__ == '__main__':
	nordic = nordicHandler.getNordicEvent(183)
	qkjuttu = nordicEventToQuakeMl(nordic, False)

	print(etree.tostring(qkjuttu, pretty_print=True))