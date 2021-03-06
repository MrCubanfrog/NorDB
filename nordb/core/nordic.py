"""
This module contains all classes surrounding the representation of events in the program. NordicEvent is the root object to which all other objects in this module refer to.

Examples::

    hour = nordicData.hour
    cur.execute(insert_query, nordicData.__dir__())

Functions and Classes
---------------------
"""

from datetime import date
from datetime import datetime
from datetime import time
from nordb.core import nordicRead
from nordb.core import nordicFix
from nordb.core.nordicRead import readNordicFile
from nordb.core.utils import addString2String
from nordb.core.utils import addInteger2String
from nordb.core.utils import addFloat2String
from nordb.nordic.nordicEvent import NordicEvent
from nordb.nordic.nordicMain import NordicMain
from nordb.nordic.nordicMacroseismic import NordicMacroseismic
from nordb.nordic.nordicComment import NordicComment
from nordb.nordic.nordicError import NordicError
from nordb.nordic.nordicWaveform import NordicWaveform
from nordb.nordic.nordicData import NordicData
from nordb.database.sql2nordic import getEventRootId

def createStringMainHeader(header, fix_nordic):
    """
    Function that creates NordicMain object with a list with values being strings

    :param str header: string from where the data is parsed from
    :param bool fix_nordic: Flag for fixing some common mistakes with nordic files. See nordicFix module.
    :return: NordicMain object with list of values parsed from header
    """
    nordic_main = [None]*24
    nordic_main[NordicMain.ORIGIN_DATE] = header[1:10]
    nordic_main[NordicMain.ORIGIN_TIME] = header[11:20]
    nordic_main[NordicMain.LOCATION_MODEL] = header[20].strip()
    nordic_main[NordicMain.DISTANCE_INDICATOR] = header[21].strip()
    nordic_main[NordicMain.EVENT_DESC_ID] = header[22].strip()
    nordic_main[NordicMain.EPICENTER_LATITUDE] = header[23:30].strip()
    nordic_main[NordicMain.EPICENTER_LONGITUDE] = header[30:38].strip()
    nordic_main[NordicMain.DEPTH] = header[38:43].strip()
    nordic_main[NordicMain.DEPTH_CONTROL] = header[43].strip()
    nordic_main[NordicMain.LOCATING_INDICATOR] = header[44].strip()
    nordic_main[NordicMain.EPICENTER_REPORTING_AGENCY] = header[45:48].strip()
    nordic_main[NordicMain.STATIONS_USED] = header[48:51].strip()
    nordic_main[NordicMain.RMS_TIME_RESIDUALS] = header[51:55].strip()
    nordic_main[NordicMain.MAGNITUDE_1] = header[56:59].strip()
    nordic_main[NordicMain.TYPE_OF_MAGNITUDE_1] = header[59].strip()
    nordic_main[NordicMain.MAGNITUDE_REPORTING_AGENCY_1] = header[60:63].strip()
    nordic_main[NordicMain.MAGNITUDE_2] = header[64:67].strip()
    nordic_main[NordicMain.TYPE_OF_MAGNITUDE_2] = header[67].strip()
    nordic_main[NordicMain.MAGNITUDE_REPORTING_AGENCY_2] = header[68:71].strip()
    nordic_main[NordicMain.MAGNITUDE_3] = header[72:75].strip()
    nordic_main[NordicMain.TYPE_OF_MAGNITUDE_3] = header[75].strip()
    nordic_main[NordicMain.MAGNITUDE_REPORTING_AGENCY_3] = header[76:79].strip()
    nordic_main[NordicMain.EVENT_ID] = -1
    nordic_main[NordicMain.H_ID] = -1

    if fix_nordic:
        nordicFix.fixMainData(nordic_main)

    return NordicMain(nordic_main)

def createStringMacroseismicHeader(header):
    """
    Function that creates NordicMacroseismic list with values being strings

    :param str header: string from where the data is parsed from
    :return: NordicMacroseismic object with list of values parsed from header
    """
    nordic_macroseismic = [None]*22

    nordic_macroseismic[NordicMacroseismic.DESCRIPTION] = header[5:20].strip()
    nordic_macroseismic[NordicMacroseismic.DIASTROPHISM_CODE] = header[21].strip()
    nordic_macroseismic[NordicMacroseismic.TSUNAMI_CODE] = header[22].strip()
    nordic_macroseismic[NordicMacroseismic.SEICHE_CODE] = header[23].strip()
    nordic_macroseismic[NordicMacroseismic.CULTURAL_EFFECTS] = header[24].strip()
    nordic_macroseismic[NordicMacroseismic.UNUSUAL_EFFECTS] = header[25].strip()
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
    nordic_macroseismic[NordicMacroseismic.QUALITY_RANK] = header[71].strip()
    nordic_macroseismic[NordicMacroseismic.REPORTING_AGENCY] = header[72:75].strip()
    nordic_macroseismic[NordicMacroseismic.EVENT_ID] = -1
    nordic_macroseismic[NordicMacroseismic.H_ID] = -1

    return NordicMacroseismic(nordic_macroseismic)

def createStringCommentHeader(header):
    """
    Function that creates Nordic comment list with values being strings

    :param str header: string from where the data is parsed from
    :return: NordicComment object with a list of values parsed from header
    """

    nordic_comment = [None]*3

    nordic_comment[NordicComment.H_COMMENT] = header[1:79].strip()
    nordic_comment[NordicComment.EVENT_ID] = -1
    nordic_comment[NordicComment.H_ID] = -1

    return NordicComment(nordic_comment)

def createStringErrorHeader(header, fix_nordic, fixed_depth = None):
    """
    Function that creates Nordic error list with values being strings

    :param str header: string from where the data is parsed from
    :param bool fix_nordic: Flag for fixing some common mistakes with nordic files. See nordicFix module.
    :param str fixed_depth: Flag for if the depth value was fixed for clearing the depth_error value
    :return: NordicError object with a list of values parsed from header
    """
    nordic_error = [None]*8

    nordic_error[NordicError.GAP] = header[5:8].strip()
    nordic_error[NordicError.SECOND_ERROR] = header[16:20].strip()
    nordic_error[NordicError.EPICENTER_LATITUDE_ERROR] = header[24:30].strip()
    nordic_error[NordicError.EPICENTER_LONGITUDE_ERROR] = header[31:38].strip()
    nordic_error[NordicError.DEPTH_ERROR] = header[40:43].strip()
    nordic_error[NordicError.MAGNITUDE_ERROR] = header[56:59].strip()
    nordic_error[NordicError.HEADER_ID] = -1
    nordic_error[NordicError.H_ID] = -1

    if fix_nordic:
        nordicFix.fixErrorData(nordic_error, fixed_depth)

    return NordicError(nordic_error)

def createStringWaveformHeader(header):
    """
    Function that creates Nordic waveform list with values being strings

    :param str header: string from where the data is parsed from
    :return: NordicWaveform object with a list of values parsed from header
    """

    nordic_waveform = [None]*3

    nordic_waveform[NordicWaveform.WAVEFORM_INFO] = header[1:79].strip()
    nordic_waveform[NordicWaveform.EVENT_ID] = -1
    nordic_waveform[NordicWaveform.H_ID] = -1

    return NordicWaveform(nordic_waveform)

def createStringPhaseData(data, fix_nordic, obs_datetime):
    """
    Function that creates Nordic phase data list with values being strings

    :param str data: string from where the data is parsed from
    :param bool fix_nordic: Flag for fixing some common mistakes with nordic files. See nordicFix module.
    :param obs_time obs_time: obs_time of the first main header for creating the observation_time
    :return: NordicData object with alist of values parsed from data
    """
    phase_data = [None]*21

    phase_data[NordicData.STATION_CODE] = data[1:6].strip()
    phase_data[NordicData.SP_INSTRUMENT_TYPE] = data[6].strip()
    phase_data[NordicData.SP_COMPONENT] = data[7].strip()
    phase_data[NordicData.QUALITY_INDICATOR] = data[9].strip()
    phase_data[NordicData.PHASE_TYPE] = data[10:14].strip()
    phase_data[NordicData.WEIGHT] = data[14].strip()
    phase_data[NordicData.OBSERVATION_TIME] = obs_datetime.strftime("%Y %m%d ") + data[18:28]
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
    phase_data[NordicData.EVENT_ID] = -1
    phase_data[NordicData.D_ID] = -1

    if fix_nordic:
        nordicFix.fixPhaseData(phase_data, obs_datetime)

    return NordicData(phase_data)

def readHeaders(event, nordic_string, fix_nordic):
    """
    Function for reading all the header files from the nordic file and returning them a header objects.

    :param NordicEvent event: nordic event to which the headers will be read to
    :param Array nordic_string: nordic file in string array form
    :param bool fix_nordic: Flag for fixing some common mistakes with nordic files. See nordicFix module.
    :return: amount of headers read
    """
    i = 1

    #find where the data starts 
    while (i < len(nordic_string)):
        if (nordic_string[i][79] == ' '):
            i+=1
            break
        i+=1

    if (len(nordic_string) != i):
        i-=1

    mheader_pos = -1
    fixed_depth = None

    for x in range(0, i):
        if (nordic_string[x][79] == '1'):
            event.main_h.append(createStringMainHeader(nordic_string[x], fix_nordic))
            fixed_depth = event.main_h[-1].depth_control
            mheader_pos +=1
        elif (nordic_string[x][79] == '2'):
            event.macro_h.append(createStringMacroseismicHeader(nordic_string[x]))
        elif (nordic_string[x][79] == '3'):
            event.comment_h.append(createStringCommentHeader(nordic_string[x]))
        elif (nordic_string[x][79] == '5'):
            event.main_h[mheader_pos].error_h = createStringErrorHeader(nordic_string[x], fix_nordic, fixed_depth)
        elif (nordic_string[x][79] == '6'):
            event.waveform_h.append(createStringWaveformHeader(nordic_string[x]))
        elif (nordic_string[x][79] == 'I'):
            event.root_id = getEventRootId(int(nordic_string[x][4:78]))

    return i

def readNordic(nordic_string, fix_nordic=True, root_id = -1, creation_id = -1, event_type = "O"):
    """
    Function for creating a single NordicEvent object from a string.

    :param Array nordic_string: String array representation of a nordic
    :param bool fix_nordic: Flag for fixing some common mistakes with nordic files. See nordicFix module.
    :param int root_id: id of the root event
    :param int creation_id: id of the creation id in the database
    :param str event_type: Type of the event.
    :return: Nordic Event object
    """
    event = NordicEvent(-1, root_id, creation_id, event_type)

    headers_size = readHeaders(event, nordic_string, fix_nordic)

    if headers_size == 0:
        raise Exception("No headers!")

    for x in range(headers_size, len(nordic_string)):
        if event.main_h[0].origin_time is None:
            obs_date = datetime.combine(event.main_h[0].origin_date,
                                       time(hour=0, minute=0, second= 0))
        else:
            obs_date = datetime.combine(event.main_h[0].origin_date,
                                        event.main_h[0].origin_time)

        event.data.append(createStringPhaseData(nordic_string[x],
                                                fix_nordic,
                                                obs_date))

    return event

def createNordicEvents(nordic_file, solution_type="O"):
    """
    Function for creating a finalised Array of NordicEvent objects from a python file object

    :param file nordic_file: file to be read
    :param string solution_type: solution type of the event
    :returns: Array of NordicEvent Objects and Array of failed Events as string
    """
    nordic_strings = nordicRead.readNordicFile(nordic_file)
    nordic_events = []
    nordic_failed = []

    for n_string in nordic_strings:
        try:
            nordic_events.append(readNordic(    n_string,
                                                True,
                                                -1,
                                                -1,
                                                solution_type))
        except Exception as e:
            nordic_failed.append("Errors:\n{0}\n--------------\n".format(e))
            raise e

    return nordic_events, nordic_failed
