"""
This module contains all classes surrounding the representation of events in the program. The classes are usually actually just a containers for lists that have all the information of the event and the information concerning what index in the list contains what info. This has been chosen as the representation because of how psycopg2 handles data. It takes lists as arguments during execution of commands which means that these database operations are easier to make due to the nature of these classes. Though this makes handling these classes more cubersome as you have to use the enumerations that the classes themselves contain to get the correct info out of the lists.

Examples::

    hour = nordicData.data[nordicData.HOUR]
    cur.execute(insert_query, nordicData.data)

Functions and Classes
---------------------
"""

from datetime import date

class NordicEvent:
    """
    Container object of nordic event information
    """
    def __init__(self, headers, data, event_id):
        self.headers = headers
        self.data = data
        self.event_id = event_id
    
class NordicData:
    """
    A class that functions as a collection of enums. Contains the information of the phase data line of a nordic file. 

    :ivar data(list): The data of a nordic phase in a list where each index of a value corresponds to NordicData's pseudo-enum. The data easily accessed with the enums provided by the class
    :ivar int header_type: This value tells that this is a NordicData object Value of 7
    :ivar int STATION_CODE: The location of the unique station code. Value of 0
    :ivar int SP_INSTRUMENT_TYPE: The location of the type of the instrument that observed the event. Value of 1
    :ivar int SP_COMPONENT: The location of the component of the observation. Value of 2
    :ivar int QUALITY_INDICATOR: The location of the quality of the observation. Value of 3 
    :ivar int PHASE_TYPE: The location of the type of the phase observed. Value of 4
    :ivar int WEIGHT: The location of the weight value. Value of 5
    :ivar int FIRST_MOTION: The location of the direction of the first motion. Value of 6
    :ivar int TIME_INFO: The location of the information on which day the event was observed relative the the day it actually happened. Value of 7
    :ivar int HOUR: The location of the hour time of the observation. Value of 8
    :ivar int MINUTE: The location of the minute time of the observation.  Value of 9 
    :ivar int SECOND: The location of the second time of the observation.Value of 10
    :ivar int SIGNAL_DURATION: The location of the signal duration of the observation. Value of 11
    :ivar int MAX_AMPLITUDE: The location of the maximum amplitude of the observation. Value of 12 
    :ivar int MAX_AMPLITUDE_PERIOD: The location of the maximum amplitude period of the observation. Value of 13
    :ivar int BACK_AZIMUTH: The location of the back azimuth of the observation. Value of 14
    :ivar int APPARENT_VELOCITY: The location of the apparent velocity of the observation. Value of 15
    :ivar int SIGNAL_TO_NOISE: The location of the signal to noise ratio of the observation. Value of 16
    :ivar int AZIMUTH_RESIDUAL: The location of the azimuth residual of the observation. Value of 17
    :ivar int TRAVEL_TIME_RESIDUAL: The location of the travel time residual of the observation. Value of 18
    :ivar int LOCATION_WEIGHT: The location of the actual weight of the observation. Value of 19
    :ivar int EPICENTER_DISTANCE: The location of the epicenter distance of the observation. Value of 20
    :ivar int EPICENTER_TO_STATION_AZIMUTH: The location of the epicenter to station azimuth of the observation. Value of 21
    :ivar int EVENT_ID: The location of the event id of the observation. Value of 22
    :ivar int ID: The location of the id of the observation. Value of 23
    """
    header_type = 7
    STATION_CODE = 0
    SP_INSTRUMENT_TYPE = 1
    SP_COMPONENT = 2
    QUALITY_INDICATOR = 3 
    PHASE_TYPE = 4
    WEIGHT = 5
    FIRST_MOTION = 6
    TIME_INFO = 7
    HOUR = 8
    MINUTE = 9 
    SECOND = 10
    SIGNAL_DURATION = 11
    MAX_AMPLITUDE = 12 
    MAX_AMPLITUDE_PERIOD = 13
    BACK_AZIMUTH = 14
    APPARENT_VELOCITY = 15
    SIGNAL_TO_NOISE = 16
    AZIMUTH_RESIDUAL = 17
    TRAVEL_TIME_RESIDUAL = 18
    LOCATION_WEIGHT = 19
    EPICENTER_DISTANCE = 20
    EPICENTER_TO_STATION_AZIMUTH = 21
    EVENT_ID = 22
    ID = 23

    def __init__(self, data):
        self.data = data
 
class NordicMain:
    """
    A class that functions as a collection of enums. Contains the information of the main header line of a nordic file. 

    :ivar list header: The header of a nordic main in a list where each index of a value corresponds to NordicMain's pseudo-enum. This data is easily accessed by it's enums.
    :ivar int header_type: This value tells that this is a NordicData object Value of 1
    :ivar int DATE: Location of the date of the event. Value of 0
    :ivar int HOUR: Location of the hour of the event. Value of 1
    :ivar int MINUTE: Location of the minute of the event. Value of 2
    :ivar int SECOND: Location of the second of the event. Value of 3
    :ivar int LOCATION_MODEL: Location of the location model sign of the event. Value of 4
    :ivar int DISTANCE_INDICATOR: Location of the distance indicator sign of the event. Value of 5
    :ivar int EVENT_DESC_ID: Location of the event description id of the event. Value of 6
    :ivar int EPICENTER_LATITUDE: Location of the epicenter latitude of the event. Value of 7
    :ivar int EPICENTER_LONGITUDE: Location of the epicenter longitude of the event. Value of 8
    :ivar int DEPTH: Location of the depth of the event. Value of 9 
    :ivar int DEPTH_CONTROL: Location of the depth control sign of the event. Value of 10
    :ivar int LOCATING_INDICATOR: Location of the locating indicator sign of the event. Value of 11
    :ivar int EPICENTER_REPORTING_AGENCY: Location of the epicenter reporting agency of the event. Value of 12
    :ivar int STATIONS_USED: Location of the number of stations used of the event. Value of 13
    :ivar int RMS_TIME_RESIDUALS: Location of the rms time residuals of the event. Value of 14
    :ivar int MAGNITUDE_1: Location of the magnitude 1 of the event. Value of 15
    :ivar int TYPE_OF_MAGNITUDE_1: Location of the type of magnitude 1 of the event. Value of 16
    :ivar int MAGNITUDE_REPORTING_AGENCY_1: Location of the magnitude reporting agency 1 of the event. Value of 17
    :ivar int MAGNITUDE_2: Location of the magnitude 2 of the event. Value of 18
    :ivar int TYPE_OF_MAGNITUDE_2: Location of the type of magnitude 2 of the event. Value of 19
    :ivar int MAGNITUDE_REPORTING_AGENCY_2: Location of the magnitude reporting agency 2 of the event. Value of 20
    :ivar int MAGNITUDE_3: Location of the magnitude 3 of the event. Value of 21
    :ivar int TYPE_OF_MAGNITUDE_3: Location of the type of magnitude 3 of the event. Value of 22
    :ivar int MAGNITUDE_REPORTING_AGENCY_3: Location of the magnitude reporting agency 3 of the event. Value of 23
    :ivar int EVENT_ID: Location of the event id of the event. Value of 24
    :ivar int ID: Location of the id of the event. Value of 25
    :ivar int O_STRING: Location of the old string from which the event was created. Value of 26
    """

    header_type = 1
    DATE = 0
    HOUR = 1
    MINUTE = 2
    SECOND = 3
    LOCATION_MODEL = 4
    DISTANCE_INDICATOR = 5
    EVENT_DESC_ID = 6
    EPICENTER_LATITUDE = 7
    EPICENTER_LONGITUDE = 8
    DEPTH = 9 
    DEPTH_CONTROL = 10
    LOCATING_INDICATOR = 11
    EPICENTER_REPORTING_AGENCY = 12
    STATIONS_USED = 13
    RMS_TIME_RESIDUALS = 14
    MAGNITUDE_1 = 15
    TYPE_OF_MAGNITUDE_1 = 16
    MAGNITUDE_REPORTING_AGENCY_1 = 17
    MAGNITUDE_2 = 18
    TYPE_OF_MAGNITUDE_2 = 19
    MAGNITUDE_REPORTING_AGENCY_2 = 20
    MAGNITUDE_3 = 21
    TYPE_OF_MAGNITUDE_3 = 22
    MAGNITUDE_REPORTING_AGENCY_3 = 23
    EVENT_ID = 24
    ID = 25
    O_STRING = 26

    def __init__(self, header):
        self.header = header
 
class NordicMacroseismic:
    """
    A class that functions as a collection of enums. Contains the information of the macroseismic header line of a nordic file. 

    :param list header: The header of a nordic macroseismic in a list where each index of a value corresponds to NordicMacroseismic's pseudo-enum.
    :ivar int header_type: This value tells that this is a NordicData object Value of 2
    :ivar int DESCRIPTION: Location of the description of the event. Value of 0
    :ivar int DIASTROPHISM_CODE: Location of the diastrophism code of the event. Value of 1
    :ivar int TSUNAMI_CODE: Location of the tsunami code of the event. Value of 2
    :ivar int SEICHE_CODE: Location of the seiche_code of the event. Value of 3 
    :ivar int CULTURAL_EFFECTS: Location of the cultural effects of the event. Value of 4
    :ivar int UNUSUAL_EFFECTS: Location of the unusual effects of the event. Value of 5
    :ivar int MAXIMUM_OBSERVED_INTENSITY: Location of the maximum observed intensity of the event. Value of 6
    :ivar int MAXIMUM_INTENSITY_QUALIFIER: Location of the maximum intensity qualifier of the event. Value of 7
    :ivar int INTENSITY_SCALE: Location of the intensity scale of the event. Value of 8
    :ivar int MACROSEISMIC_LATITUDE: Location of the macroseismic latitude of the event. Value of 9
    :ivar int MACROSEISMIC_LONGITUDE: Location of the macroseismic longitude of the event. Value of 10
    :ivar int MACROSEISMIC_MAGNITUDE: Location of the macroseismic magnitude of the event. Value of 11
    :ivar int TYPE_OF_MAGNITUDE: Location of the type of magnitude of the event. Value of 12
    :ivar int LOGARITHM_OF_RADIUS: Location of the logarithm of radius of the event. Value of 13
    :ivar int LOGARITHM_OF_AREA_1: Location of the logarithm of area 1 of the event. Value of 14
    :ivar int BORDERING_INTENSITY_1: Location of the bordering intensity 1 of the event. Value of 15
    :ivar int LOGARITHM_OF_AREA_2: Location of the logarithm of area 2 of the event. Value of 16
    :ivar int BORDERING_INTENSITY_2: Location of the bordering intensity 2 of the event. Value of 17
    :ivar int QUALITY_RANK: Location of the quality rank of the event. Value of 18
    :ivar int REPORTING_AGENCY: Location of the reporting agency of the event. Value of 19
    :ivar int EVENT_ID: Location of the event id of the event. Value of 20
    :ivar int ID: Location of the id of the event. Value of 21
    """
    header_type = 2
    DESCRIPTION = 0
    DIASTROPHISM_CODE = 1
    TSUNAMI_CODE = 2
    SEICHE_CODE = 3 
    CULTURAL_EFFECTS = 4
    UNUSUAL_EFFECTS = 5
    MAXIMUM_OBSERVED_INTENSITY = 6
    MAXIMUM_INTENSITY_QUALIFIER = 7
    INTENSITY_SCALE = 8
    MACROSEISMIC_LATITUDE = 9
    MACROSEISMIC_LONGITUDE = 10
    MACROSEISMIC_MAGNITUDE = 11
    TYPE_OF_MAGNITUDE = 12
    LOGARITHM_OF_RADIUS = 13
    LOGARITHM_OF_AREA_1 = 14
    BORDERING_INTENSITY_1 = 15
    LOGARITHM_OF_AREA_2 = 16
    BORDERING_INTENSITY_2 = 17
    QUALITY_RANK = 18
    REPORTING_AGENCY = 19
    EVENT_ID = 20
    ID = 21

    def __init__(self, header):
        self.header = header
 
class NordicComment:
    """
    A class that functions as a collection of enums. Contains the information of the comment header line of a nordic file. 

    :param list header: The header of a nordic comment in a list where each index of a value corresponds to NordicComment's pseudo-enum.
    :ivar int header_type: This value tells that this is a NordicData object Value of 3
    :ivar int H_COMMENT: Location of the comment int the event. Value of 0
    :ivar int EVENT_ID: Location of the event id of the event. Value of 1
    :ivar int ID: Location of the id of the event. Value of 2
    """
    header_type = 3
    H_COMMENT = 0
    EVENT_ID = 1
    ID = 2

    def __init__(self, header):
        self.header = header

class NordicError:
    """
    A class that functions as a collection of enums. Contains the information of the error header line of a nordic file. 

    :param list header: The header of a nordic error in a list where each index of a value corresponds to NordicError's pseudo-enum.
    :ivar int header_type: This value tells that this is a NordicData object Value of 5
    :ivar int GAP: Location of the gap of the event. Value of 0
    :ivar int SECOND_ERROR: Location of the second error of the event. Value of 1
    :ivar int EPICENTER_LATITUDE_ERROR: Location of the epicenter latitude error of the event. Value of 2
    :ivar int EPICENTER_LONGITUDE_ERROR: Location of the epicenter longitude error of the event. Value of 3
    :ivar int DEPTH_ERROR: Location of the depth error of the event. Value of 4
    :ivar int MAGNITUDE_ERROR: Location of the magnitude error of the event. Value of 5
    :ivar int HEADER_ID: Location of the header id of the event. Value of 6
    :ivar int ID: Location of the id of the event. Value of 7
    """
    header_type = 5
    GAP = 0
    SECOND_ERROR = 1
    EPICENTER_LATITUDE_ERROR = 2
    EPICENTER_LONGITUDE_ERROR = 3
    DEPTH_ERROR = 4
    MAGNITUDE_ERROR = 5
    HEADER_ID = 6
    ID = 7

    def __init__(self, header, header_pos):
        self.header = header
        self.header_pos = header_pos

    
class NordicWaveform:
    """
    A class that functions as a collection of enums. Contains the information of the waveform header line of a nordic file. 

    :param list header: The header of a nordic waveform in a list where each index of a value corresponds to NordicWaveform's pseudo-enum.
    :ivar int header_type: This value tells that this is a NordicData object Value of 6
    :ivar int WAVEFORM INFO: Location of the waveform info of the event. value of 0
    :ivar int EVENT ID: Location of the event id of the event. value of 1
    :ivar int ID: Location of the id of the event. value of 2
    """
    header_type = 6
    WAVEFORM_INFO = 0
    EVENT_ID = 1
    ID = 2
    def __init__(self, header):
        self.header = header


def createStringMainHeader(header):
    """
    Function that creates NordicMain object with a list with values being strings
    
    :param str header: string from where the data is parsed from
    :return: NordicMain object with list of values parsed from header
    """

    nordic_main = [None]*27

    nordic_main[NordicMain.DATE] = header[1:5] + "-" + header[6:8] + "-" + header[8:10]
    nordic_main[NordicMain.HOUR ] = header[11:13].strip()
    nordic_main[NordicMain.MINUTE ] = header[13:15].strip()
    nordic_main[NordicMain.SECOND ] = header[16:20].strip()
    nordic_main[NordicMain.LOCATION_MODEL ] = header[20].strip()
    nordic_main[NordicMain.DISTANCE_INDICATOR ] = header[21].strip()
    nordic_main[NordicMain.EVENT_DESC_ID ] = header[22].strip()
    nordic_main[NordicMain.EPICENTER_LATITUDE ] = header[23:30].strip()
    nordic_main[NordicMain.EPICENTER_LONGITUDE ] = header[30:38].strip()
    nordic_main[NordicMain.DEPTH ] = header[38:43].strip()
    nordic_main[NordicMain.DEPTH_CONTROL ] = header[43].strip()
    nordic_main[NordicMain.LOCATING_INDICATOR ] = header[44].strip()
    nordic_main[NordicMain.EPICENTER_REPORTING_AGENCY ] = header[45:48].strip()
    nordic_main[NordicMain.STATIONS_USED ] = header[48:51].strip()
    nordic_main[NordicMain.RMS_TIME_RESIDUALS ] = header[51:55].strip()
    nordic_main[NordicMain.MAGNITUDE_1 ] = header[56:59].strip()
    nordic_main[NordicMain.TYPE_OF_MAGNITUDE_1 ] = header[59].strip()
    nordic_main[NordicMain.MAGNITUDE_REPORTING_AGENCY_1 ] = header[60:63].strip()
    nordic_main[NordicMain.MAGNITUDE_2 ] = header[64:67].strip()
    nordic_main[NordicMain.TYPE_OF_MAGNITUDE_2 ] = header[67].strip()
    nordic_main[NordicMain.MAGNITUDE_REPORTING_AGENCY_2 ] = header[68:71].strip()
    nordic_main[NordicMain.MAGNITUDE_3 ] = header[71:75].strip()
    nordic_main[NordicMain.TYPE_OF_MAGNITUDE_3 ] = header[75].strip()
    nordic_main[NordicMain.MAGNITUDE_REPORTING_AGENCY_3 ] = header[76:79].strip()
    nordic_main[NordicMain.O_STRING] = header

    return NordicMain(nordic_main)

def createStringMacroseismicHeader(header): 
    """
    Function that creates NordicMacroseismic list with values being strings
    
    :param str header: string from where the data is parsed from
    :return: NordicMacroseismic object with list of values parsed from header
    """
    nordic_macroseismic = [None]*20

    nordic_macroseismic[NordicMacroseismic.DESCRIPTION] = header[5:20].strip()
    nordic_macroseismic[NordicMacroseismic.DIASTROPHISM_CODE] = header[22].strip()
    nordic_macroseismic[NordicMacroseismic.TSUNAMI_CODE] = header[23].strip()
    nordic_macroseismic[NordicMacroseismic.SEICHE_CODE] = header[24].strip()
    nordic_macroseismic[NordicMacroseismic.CULTURAL_EFFECTS] = header[25].strip()
    nordic_macroseismic[NordicMacroseismic.UNUSUAL_EFFECTS] = header[26].strip()
    nordic_macroseismic[NordicMacroseismic.MAXIMUM_OBSERVED_INTENSITY] = header[27:29].strip()
    nordic_macroseismic[NordicMacroseismic.MAXIMUM_INTENSITY_QUALIFIER] = header[29].strip()
    nordic_macroseismic[NordicMacroseismic.INTENSITY_SCALE] = header[30:32].strip()
    nordic_macroseismic[NordicMacroseismic.MACROSEISMIC_LATITUDE] = header[33:39].strip()
    nordic_macroseismic[NordicMacroseismic.MACROSEISMIC_LONGITUDE] = header[40:47].strip()
    nordic_macroseismic[NordicMacroseismic.MACROSEISMIC_MAGNITUDE] = header[48:51].strip()
    nordic_macroseismic[NordicMacroseismic.TYPE_OF_MAGNITUDE] = header[51].strip()
    nordic_macroseismic[NordicMacroseismic.LOGARITHM_OF_RADIUS] = header[52:56].strip()
    nordic_macroseismic[NordicMacroseismic.LOGARITHM_OF_AREA_1] = header[56:61].strip()
    nordic_macroseismic[NordicMacroseismic.BORDERING_INTENSITY_1] = header[61:63].strip()
    nordic_macroseismic[NordicMacroseismic.LOGARITHM_OF_AREA_2] = header[63:68].strip()
    nordic_macroseismic[NordicMacroseismic.BORDERING_INTENSITY_2] = header[68:70].strip()
    nordic_macroseismic[NordicMacroseismic.QUALITY_RANK] = header[72].strip()
    nordic_macroseismic[NordicMacroseismic.REPORTING_AGENCY] = header[72:75].strip()

    return NordicMacroseismic(nordic_macroseismic)

def createStringCommentHeader(header):
    """
    Function that creates Nordic comment list with values being strings

    :param str header: string from where the data is parsed from
    :return: NordicComment object with a list of values parsed from header
    """

    nordic_comment = [None]

    nordic_comment[NordicComment.H_COMMENT] = header[1:79].strip()

    return NordicComment(nordic_comment)


def createStringErrorHeader(header, h_id):
    """
    Function that creates Nordic error list with values being strings

    :param str header: string from where the data is parsed from
    :return: NordicError object with a list of values parsed from header
    """
    nordic_error = [None]*6

    nordic_error[NordicError.GAP] = header[5:8].strip()
    nordic_error[NordicError.SECOND_ERROR] = header[16:20].strip()
    nordic_error[NordicError.EPICENTER_LATITUDE_ERROR] = header[24:30].strip()
    nordic_error[NordicError.EPICENTER_LONGITUDE_ERROR] = header[31:38].strip()
    nordic_error[NordicError.DEPTH_ERROR] = header[40:43].strip()
    nordic_error[NordicError.MAGNITUDE_ERROR] = header[56:59].strip()
   
    return NordicError(nordic_error, h_id)

def createStringWaveformHeader(header):
    """
    Function that creates Nordic waveform list with values being strings

    :param str header: string from where the data is parsed from
    :return: NordicWaveform object with a list of values parsed from header
    """

    nordic_waveform = [None]

    nordic_waveform[NordicWaveform.WAVEFORM_INFO] = header[1:79].strip()

    return NordicWaveform(nordic_waveform)

def createStringPhaseData(data):
    """
    Function that creates Nordic phase data list with values being strings

    :param str data: string from where the data is parsed from
    :return: NordicData object with alist of values parsed from data
    """
    phase_data = [None]*22

    phase_data[NordicData.STATION_CODE] = data[1:5].strip()
    phase_data[NordicData.SP_INSTRUMENT_TYPE] = data[6].strip()
    phase_data[NordicData.SP_COMPONENT] = data[7].strip()
    phase_data[NordicData.QUALITY_INDICATOR] = data[9].strip()
    phase_data[NordicData.PHASE_TYPE] = data[10:14].strip()
    phase_data[NordicData.WEIGHT] = data[14].strip()
    phase_data[NordicData.FIRST_MOTION] = data[16].strip()
    phase_data[NordicData.TIME_INFO] = data[17].strip()
    phase_data[NordicData.HOUR] = data[18:20].strip()
    phase_data[NordicData.MINUTE] = data[20:22].strip()
    phase_data[NordicData.SECOND] = data[23:28].strip()
    phase_data[NordicData.SIGNAL_DURATION] = data[29:33].strip()
    phase_data[NordicData.MAX_AMPLITUDE] = data[34:40].strip()
    phase_data[NordicData.MAX_AMPLITUDE_PERIOD] = data[41:45].strip()
    phase_data[NordicData.BACK_AZIMUTH] = data[46:52].strip()
    phase_data[NordicData.APPARENT_VELOCITY] = data[52:56].strip()
    phase_data[NordicData.SIGNAL_TO_NOISE] = data[56:60].strip()
    phase_data[NordicData.AZIMUTH_RESIDUAL] = data[60:63].strip()
    phase_data[NordicData.TRAVEL_TIME_RESIDUAL] = data[63:68].strip()
    phase_data[NordicData.LOCATION_WEIGHT] = data[68:70].strip()
    phase_data[NordicData.EPICENTER_DISTANCE] = data[70:75].strip()
    phase_data[NordicData.EPICENTER_TO_STATION_AZIMUTH] = data[76:79].strip()

    return NordicData(phase_data)

def returnInt(integer):
    """
    Function that casts integer to a int or None if it's empty.

    :param str integer: integer or empty string
    :return: Integer or None
    """
    try:
        return int(integer)
    except:
        return None

def returnDate(date_s):
    """
    Function that casts date_s to a date or None if it's empty.

    :param str date_s: date or empty string
    :return: datetime or None
    """
    try:
        return date(year=int(date_s[:4]), month=int(date_s[5:7]), day=int(date_s[8:]))
    except ValueError:
        return None

def returnFloat(float_s):
    """
    Function that casts float_s to a integer or None if it's empty.

    :param str float_s: float or empty string
    :return: Float or None
    """
    try:
        return float(float_s)
    except:
        return None

def returnString(string):
    """
    Function that returns string or None if the string is empty.

    :param str string: the string value
    :return: string or None
    """
    if string == "":
        return None
    else:
        return string

def mainString2Main(main_string, event_id):
    """
    Function that converts all values in main string list into main list with correct value types.
        
    :param list main_string: list of all string valus of the main header
    :param int event_id: event id of the main header
    :return: List of all main info in correct order
    """
    main = [None]*25

    main[NordicMain.DATE]                           = returnDate    (main_string.header[NordicMain.DATE])
    main[NordicMain.HOUR]                           = returnInt     (main_string.header[NordicMain.HOUR])
    main[NordicMain.MINUTE]                         = returnInt     (main_string.header[NordicMain.MINUTE])
    main[NordicMain.SECOND]                         = returnFloat   (main_string.header[NordicMain.SECOND])
    main[NordicMain.LOCATION_MODEL]                 = returnString  (main_string.header[NordicMain.LOCATION_MODEL])
    main[NordicMain.DISTANCE_INDICATOR]             = returnString  (main_string.header[NordicMain.DISTANCE_INDICATOR])
    main[NordicMain.EVENT_DESC_ID]                  = returnString  (main_string.header[NordicMain.EVENT_DESC_ID])
    main[NordicMain.EPICENTER_LATITUDE]             = returnFloat   (main_string.header[NordicMain.EPICENTER_LATITUDE])
    main[NordicMain.EPICENTER_LONGITUDE]            = returnFloat   (main_string.header[NordicMain.EPICENTER_LONGITUDE])
    main[NordicMain.DEPTH]                          = returnFloat   (main_string.header[NordicMain.DEPTH])
    main[NordicMain.DEPTH_CONTROL]                  = returnString  (main_string.header[NordicMain.DEPTH_CONTROL])
    main[NordicMain.LOCATING_INDICATOR]             = returnString  (main_string.header[NordicMain.LOCATING_INDICATOR])
    main[NordicMain.EPICENTER_REPORTING_AGENCY]     = returnString  (main_string.header[NordicMain.EPICENTER_REPORTING_AGENCY])
    main[NordicMain.STATIONS_USED]                  = returnInt     (main_string.header[NordicMain.STATIONS_USED])
    main[NordicMain.RMS_TIME_RESIDUALS]             = returnFloat   (main_string.header[NordicMain.RMS_TIME_RESIDUALS])
    main[NordicMain.MAGNITUDE_1]                    = returnFloat   (main_string.header[NordicMain.MAGNITUDE_1])
    main[NordicMain.TYPE_OF_MAGNITUDE_1]            = returnString  (main_string.header[NordicMain.TYPE_OF_MAGNITUDE_1])
    main[NordicMain.MAGNITUDE_REPORTING_AGENCY_1]   = returnString  (main_string.header[NordicMain.MAGNITUDE_REPORTING_AGENCY_1])
    main[NordicMain.MAGNITUDE_2]                    = returnFloat   (main_string.header[NordicMain.MAGNITUDE_2]) 
    main[NordicMain.TYPE_OF_MAGNITUDE_2]            = returnString  (main_string.header[NordicMain.TYPE_OF_MAGNITUDE_2])
    main[NordicMain.MAGNITUDE_REPORTING_AGENCY_2]   = returnString  (main_string.header[NordicMain.MAGNITUDE_REPORTING_AGENCY_2])
    main[NordicMain.MAGNITUDE_3]                    = returnInt     (main_string.header[NordicMain.MAGNITUDE_3])
    main[NordicMain.TYPE_OF_MAGNITUDE_3]            = returnString  (main_string.header[NordicMain.TYPE_OF_MAGNITUDE_3])
    main[NordicMain.MAGNITUDE_REPORTING_AGENCY_3]   = returnString  (main_string.header[NordicMain.MAGNITUDE_REPORTING_AGENCY_3])
    main[NordicMain.EVENT_ID]                       = event_id

    return NordicMain(main) 

def macroseismicString2Macroseismic(macro_string, event_id):
    """
    Function that converts all values in macroseismic string list into macroseismic list with correct value types.
    :param list macro_string.header: list of all string valus of the macroseismic header
    :param int event_id: event id of the macroseismic header
    :return: List of all macroseismic info in correct order
    """
    macro = [None]*21

    macro[NordicMacroseismic.DESCRIPTION]                   = returnString  (macro_string.header[NordicMacroseismic.DESCRIPTION])
    macro[NordicMacroseismic.DIASTROPHISM_CODE]             = returnString  (macro_string.header[NordicMacroseismic.DIASTROPHISM_CODE])
    macro[NordicMacroseismic.TSUNAMI_CODE]                  = returnString  (macro_string.header[NordicMacroseismic.TSUNAMI_CODE])
    macro[NordicMacroseismic.SEICHE_CODE]                   = returnString  (macro_string.header[NordicMacroseismic.SEICHE_CODE])
    macro[NordicMacroseismic.CULTURAL_EFFECTS]              = returnString  (macro_string.header[NordicMacroseismic.CULTURAL_EFFECTS])
    macro[NordicMacroseismic.UNUSUAL_EFFECTS]               = returnString  (macro_string.header[NordicMacroseismic.UNUSUAL_EFFECTS])
    macro[NordicMacroseismic.MAXIMUM_OBSERVED_INTENSITY]    = returnFloat   (macro_string.header[NordicMacroseismic.MAXIMUM_OBSERVED_INTENSITY])
    macro[NordicMacroseismic.MAXIMUM_INTENSITY_QUALIFIER]   = returnString  (macro_string.header[NordicMacroseismic.MAXIMUM_INTENSITY_QUALIFIER])
    macro[NordicMacroseismic.INTENSITY_SCALE]               = returnString  (macro_string.header[NordicMacroseismic.INTENSITY_SCALE])
    macro[NordicMacroseismic.MACROSEISMIC_LATITUDE]         = returnFloat   (macro_string.header[NordicMacroseismic.MACROSEISMIC_LATITUDE])
    macro[NordicMacroseismic.MACROSEISMIC_LONGITUDE]        = returnFloat   (macro_string.header[NordicMacroseismic.MACROSEISMIC_LONGITUDE])
    macro[NordicMacroseismic.MACROSEISMIC_MAGNITUDE]        = returnFloat   (macro_string.header[NordicMacroseismic.MACROSEISMIC_MAGNITUDE])
    macro[NordicMacroseismic.TYPE_OF_MAGNITUDE]             = returnString  (macro_string.header[NordicMacroseismic.TYPE_OF_MAGNITUDE])
    macro[NordicMacroseismic.LOGARITHM_OF_RADIUS]           = returnFloat   (macro_string.header[NordicMacroseismic.LOGARITHM_OF_RADIUS])
    macro[NordicMacroseismic.LOGARITHM_OF_AREA_1]           = returnFloat   (macro_string.header[NordicMacroseismic.LOGARITHM_OF_AREA_1])
    macro[NordicMacroseismic.BORDERING_INTENSITY_1]         = returnFloat   (macro_string.header[NordicMacroseismic.BORDERING_INTENSITY_1])
    macro[NordicMacroseismic.LOGARITHM_OF_AREA_2]           = returnFloat   (macro_string.header[NordicMacroseismic.LOGARITHM_OF_AREA_2])
    macro[NordicMacroseismic.BORDERING_INTENSITY_2]         = returnFloat   (macro_string.header[NordicMacroseismic.BORDERING_INTENSITY_2])
    macro[NordicMacroseismic.QUALITY_RANK]                  = returnString  (macro_string.header[NordicMacroseismic.QUALITY_RANK])
    macro[NordicMacroseismic.REPORTING_AGENCY]              = returnString  (macro_string.header[NordicMacroseismic.REPORTING_AGENCY])
    macro[NordicMacroseismic.EVENT_ID]                      = event_id

    return NordicMacroseismic(macro)

def commentString2Comment(comment_string, event_id):
    """
    Function that converts all values in comment string list into comment list with correct value types.
        
    :param list comment_string.header: list of all string valus of the comment header
    :param int event_id: event id of the comment header
    :return: List of all comment info in correct order
    """
    comment = [None]*2

    comment[NordicComment.H_COMMENT] = returnString (comment_string.header[NordicComment.H_COMMENT])
    comment[NordicComment.EVENT_ID]  = event_id

    return NordicComment(comment)

def errorString2Error(error_string, header_id):
    """
    Function that converts all values in comment string list into comment list with correct value types.

    :param list comment_string.header: list of all string valus of the comment header
    :param int header_id: header id of the comment header
    :return: List of all error info in correct order
    """
    error = [None]*7

    error[NordicError.GAP]                          = returnInt     (error_string.header[NordicError.GAP]) 
    error[NordicError.SECOND_ERROR]                 = returnFloat   (error_string.header[NordicError.SECOND_ERROR]) 
    error[NordicError.EPICENTER_LATITUDE_ERROR]     = returnFloat   (error_string.header[NordicError.EPICENTER_LATITUDE_ERROR]) 
    error[NordicError.EPICENTER_LONGITUDE_ERROR]    = returnFloat   (error_string.header[NordicError.EPICENTER_LONGITUDE_ERROR]) 
    error[NordicError.DEPTH_ERROR]                  = returnFloat   (error_string.header[NordicError.DEPTH_ERROR]) 
    error[NordicError.MAGNITUDE_ERROR]              = returnFloat   (error_string.header[NordicError.MAGNITUDE_ERROR]) 
    error[NordicError.HEADER_ID]                    = header_id

    return NordicError(error, error_string.header_pos)

def waveformString2Waveform(waveform_string, event_id):
    """
    Function that converts all values in waveform string list into waveform list with correct value types.

    :param list waveform_string.header: list of all string valus of the waveform header
    :param int header_id: header id of the waveform header
    :return: List of all waveform info in correct order
    """
    waveform = [None]*2

    waveform[NordicWaveform.WAVEFORM_INFO]  = returnString  (waveform_string.header[NordicWaveform.WAVEFORM_INFO])
    waveform[NordicWaveform.EVENT_ID]       = event_id

    return NordicWaveform(waveform)

def dataString2Data(data_string, event_id):
    """
    Function that converts all values in data string list into data list with correct value types.

    :param list data_string.header: list of all string valus of the data header
    :param int header_id: header id of the data header
    :return: List of all data info in correct order
    """
    data = [None]*23

    data[NordicData.STATION_CODE]                   = returnString  (data_string.data[NordicData.STATION_CODE])
    data[NordicData.SP_INSTRUMENT_TYPE]             = returnString  (data_string.data[NordicData.SP_INSTRUMENT_TYPE])
    data[NordicData.SP_COMPONENT]                   = returnString  (data_string.data[NordicData.SP_COMPONENT])
    data[NordicData.QUALITY_INDICATOR]              = returnString  (data_string.data[NordicData.QUALITY_INDICATOR])
    data[NordicData.PHASE_TYPE]                     = returnString  (data_string.data[NordicData.PHASE_TYPE])
    data[NordicData.WEIGHT]                         = returnInt     (data_string.data[NordicData.WEIGHT])
    data[NordicData.FIRST_MOTION]                   = returnString  (data_string.data[NordicData.FIRST_MOTION])
    data[NordicData.TIME_INFO]                      = returnString  (data_string.data[NordicData.TIME_INFO])
    data[NordicData.HOUR]                           = returnInt     (data_string.data[NordicData.HOUR])
    data[NordicData.MINUTE]                         = returnInt     (data_string.data[NordicData.MINUTE])
    data[NordicData.SECOND]                         = returnFloat   (data_string.data[NordicData.SECOND])
    data[NordicData.SIGNAL_DURATION]                = returnInt     (data_string.data[NordicData.SIGNAL_DURATION])
    data[NordicData.MAX_AMPLITUDE]                  = returnFloat   (data_string.data[NordicData.MAX_AMPLITUDE])
    data[NordicData.MAX_AMPLITUDE_PERIOD]           = returnFloat   (data_string.data[NordicData.MAX_AMPLITUDE_PERIOD])
    data[NordicData.BACK_AZIMUTH]                   = returnFloat   (data_string.data[NordicData.BACK_AZIMUTH])
    data[NordicData.APPARENT_VELOCITY]              = returnFloat   (data_string.data[NordicData.APPARENT_VELOCITY])
    data[NordicData.SIGNAL_TO_NOISE]                = returnFloat   (data_string.data[NordicData.SIGNAL_TO_NOISE])
    data[NordicData.AZIMUTH_RESIDUAL]               = returnInt     (data_string.data[NordicData.AZIMUTH_RESIDUAL])
    data[NordicData.TRAVEL_TIME_RESIDUAL]           = returnFloat   (data_string.data[NordicData.TRAVEL_TIME_RESIDUAL])
    data[NordicData.LOCATION_WEIGHT]                = returnInt     (data_string.data[NordicData.LOCATION_WEIGHT])
    data[NordicData.EPICENTER_DISTANCE]             = returnInt     (data_string.data[NordicData.EPICENTER_DISTANCE])
    data[NordicData.EPICENTER_TO_STATION_AZIMUTH]   = returnInt     (data_string.data[NordicData.EPICENTER_TO_STATION_AZIMUTH])
    data[NordicData.EVENT_ID]                       = event_id

    return NordicData(data)

