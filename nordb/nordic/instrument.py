"""
Contains information relevant to Instrument object

Classes and Functions
---------------------
"""
import operator
import unidecode 

from nordb.core.validationTools import validateFloat
from nordb.core.validationTools import validateInteger
from nordb.core.validationTools import validateString
from nordb.core.validationTools import validateDate
from nordb.core.utils import addString2String
from nordb.core.utils import addInteger2String
from nordb.core.utils import addFloat2String
from nordb.core.utils import stringToDate

class Instrument:
    """
    Class for instrument information. Comes from css instrument format.

    :param array data: all the relevant data for Sensor in an array. These values are accessed by its numerations.
    :ivar int header_type: 12
    :ivar Response response: response file to which this response is attached to
    :ivar string band: Frequency band. Maximum of 1 character
    :ivar string instrument_name: Name of the instrument. Maximum of 50 characters
    :ivar string instrument_type: Type of the instrument. Maximum of 6 characters
    :ivar string digital: data type: d - digital a - analog. Maximum of 1 characters
    :ivar float samprate: sampling rate in samples/sec
    :ivar float ncalib: nominal calibration (nn/count)
    :ivar flaot ncalper: nominal calibration period (sec)
    :ivar string resp_dir: Directory for instrument response file. Maximum of 64 characters
    :ivar string dfile: Maximum of 32 characters
    :ivar string rsptype: response type. Maximum of 6 characters
    :ivar int i_id: id of this instrument
    :ivar int css_id: css id of this instrument
    :ivar int response_id: id of the response of this instrument
    :ivar date lddate: load date
    :ivar int response_id: id of the response of the instrument
    :ivar int INSTRUMENT_NAME: Enumeration of the data list. Value of 0
    :ivar int INSTRUMENT_TYPE: Enumeration of the data list. Value of 1
    :ivar int BAND: Enumeration of the data list. Value of 2
    :ivar int DIGITAL: Enumeration of the data list. Value of 3
    :ivar int SAMPRATE: Enumeration of the data list. Value of 4
    :ivar int NCALIB: Enumeration of the data list. Value of 5
    :ivar int NCALPER: Enumeration of the data list. Value of 6
    :ivar int RESP_DIR: Enumeration of the data list. Value of 7
    :ivar int DFILE: Enumeration of the data list. Value of 8
    :ivar int RSPTYPE: Enumeration of the data list. Value of 9
    :ivar int LDDATE: Enumeration of the data list. Value of 10
    :ivar int I_ID: Enumeration of the data list. Value of 11
    :ivar int CSS_ID: Enumeration of the data list. Value of 12
    :ivar int RESPONSE ID: Enumeration of the data list. Value of 13
    """
    header_type = 12
    INSTRUMENT_NAME = 0
    INSTRUMENT_TYPE = 1
    BAND = 2
    DIGITAL = 3
    SAMPRATE = 4
    NCALIB = 5
    NCALPER = 6
    RESP_DIR = 7
    DFILE = 8
    RSPTYPE = 9
    LDDATE = 10
    I_ID = 11
    CSS_ID = 12
    RESPONSE_ID = 13

    def __init__(self, data = None):
        if data is None:
            self.response = None
            self.instrument_name = None
            self.instrument_type = None
            self.band = None
            self.digital = None
            self.samprate = None
            self.ncalib = None
            self.ncalper = None
            self.resp_dir = None
            self.dfile = None
            self.rsptype = None
            self.lddate = None
            self.i_id = -1
            self.css_id = -1
            self.response_id = -1
        else:
            self.response = None
            self.instrument_name = data[self.INSTRUMENT_NAME]
            self.instrument_type = data[self.INSTRUMENT_TYPE]
            self.band = data[self.BAND]
            self.digital = data[self.DIGITAL]
            self.samprate = data[self.SAMPRATE]
            self.ncalib = data[self.NCALIB]
            self.ncalper = data[self.NCALPER]
            self.resp_dir = data[self.RESP_DIR]
            self.dfile = data[self.DFILE]
            self.rsptype = data[self.RSPTYPE]
            self.lddate = data[self.LDDATE]
            self.i_id = data[self.I_ID]
            self.css_id = data[self.CSS_ID]
            self.response_id = data[self.RESPONSE_ID]

    instrument_name = property(operator.attrgetter('_instrument_name'), doc="")

    @instrument_name.setter
    def instrument_name(self, val):
        val_instrument_name = validateString(val, "instrument_name", 0, 50, None, self.header_type)
        self._instrument_name = val_instrument_name

    instrument_type = property(operator.attrgetter('_instrument_type'), doc="")

    @instrument_type.setter
    def instrument_type(self, val):
        val_instrument_type = validateString(val, "instrument_type", 0, 6, None, self.header_type)
        self._instrument_type = val_instrument_type

    band = property(operator.attrgetter('_band'), doc="")

    @band.setter
    def band(self, val):
        val_band = validateString(val, "band", 0, 1, None, self.header_type)
        self._band = val_band

    digital = property(operator.attrgetter('_digital'), doc="")

    @digital.setter
    def digital(self, val):
        val_digital = validateString(val, "digital", 0, 1, None, self.header_type)
        self._digital = val_digital

    samprate = property(operator.attrgetter('_samprate'), doc="")

    @samprate.setter
    def samprate(self, val):
        val_samprate = validateFloat(val, "samprate", 0.0, 1000.0, self.header_type)
        self._samprate = val_samprate

    ncalib = property(operator.attrgetter('_ncalib'), doc="")

    @ncalib.setter
    def ncalib(self, val):
        val_ncalib = validateFloat(val, "ncalib", -1.0, 10000.0, self.header_type)
        self._ncalib = val_ncalib

    ncalper = property(operator.attrgetter('_ncalper'), doc="")

    @ncalper.setter
    def ncalper(self, val):
        val_ncalper = validateFloat(val, "ncalper", -1.0, 10000.0, self.header_type)
        self._ncalper = val_ncalper

    resp_dir = property(operator.attrgetter('_resp_dir'), doc="")

    @resp_dir.setter
    def resp_dir(self, val):
        val_resp_dir = validateString(val, "resp_dir", 0, 64, None, self.header_type)
        self._resp_dir = val_resp_dir

    dfile = property(operator.attrgetter('_dfile'), doc="")

    @dfile.setter
    def dfile(self, val):
        val_dfile = validateString(val, "dfile", 0, 32, None, self.header_type)
        self._dfile = val_dfile

    rsptype = property(operator.attrgetter('_rsptype'), doc="")

    @rsptype.setter
    def rsptype(self, val):
        val_rsptype = validateString(val, "rsptype", 0, 6, None, self.header_type)
        self._rsptype = val_rsptype

    lddate = property(operator.attrgetter('_lddate'), doc="")

    @lddate.setter
    def lddate(self, val):
        val_lddate = validateDate(val, "lddate", self.header_type)
        self._lddate = val_lddate

    css_id = property(operator.attrgetter('_css_id'), doc="")

    @css_id.setter
    def css_id(self, val):
        val_css_id = validateInteger(val, "css_id", None, None, self.header_type)
        self._css_id = val_css_id

    response_id = property(operator.attrgetter('_response_id'), doc="")

    @response_id.setter
    def response_id(self, val):
        val_response_id = validateInteger(val, "response_id", None, None, self.header_type)
        self._response_id = val_response_id


    def __str__(self):
        instrumentString = ""

        instrumentString += addInteger2String(self.css_id, 8, '>')

        instrumentString += " "

        instrumentString += addString2String(self.instrument_name, 50, '<')

        instrumentString += " "

        instrumentString += addString2String(self.instrument_type, 6, '<')

        instrumentString += " "

        instrumentString += addString2String(self.band, 2, '<')
        instrumentString += addString2String(self.digital, 2, '<')
        instrumentString += addFloat2String (self.samprate, 11, 6, '>')

        instrumentString += "    "

        instrumentString += addFloat2String (self.ncalib, 13, 6, '>')

        instrumentString += "    "

        instrumentString += addFloat2String(self.ncalper, 13, 6, '>')

        instrumentString += " "

        instrumentString += addString2String(self.resp_dir, 64, '<')

        instrumentString += " "

        instrumentString += addString2String(self.dfile, 32, '<')

        instrumentString += " "

        instrumentString += addString2String(self.rsptype, 6, '<')

        instrumentString += "       "

        instrumentString += addString2String(self.lddate.strftime("%Y-%b-%d"), 11, '<')

        return instrumentString

    def getAsList(self):
        instrument_list = [ self.css_id,
                            self.instrument_name,
                            self.instrument_type,
                            self.band,
                            self.digital,
                            self.samprate,
                            self.ncalib,
                            self.ncalper,
                            self.resp_dir,
                            self.dfile,
                            self.rsptype,
                            self.lddate,
                            self.response_id]

        return instrument_list

def readInstrumentStringToInstrument(ins_line):
    """
    Function for reading instrument info to a Instrument object

    :param str ins_line: css intrument line
    :returns: Instrument object
    """
    instrument = [None]*14

    instrument[Instrument.INSTRUMENT_NAME]  = unidecode.unidecode(ins_line[8:58].strip())
    instrument[Instrument.INSTRUMENT_TYPE]  = unidecode.unidecode(ins_line[60:67].strip())
    instrument[Instrument.BAND]             = unidecode.unidecode(ins_line[67].strip())
    instrument[Instrument.DIGITAL]          = unidecode.unidecode(ins_line[69].strip())
    instrument[Instrument.SAMPRATE]         = unidecode.unidecode(ins_line[70:82].strip())
    instrument[Instrument.NCALIB]           = unidecode.unidecode(ins_line[82:100].strip())
    instrument[Instrument.NCALPER]          = unidecode.unidecode(ins_line[101:116].strip())
    instrument[Instrument.RESP_DIR]         = unidecode.unidecode(ins_line[117:182].strip())
    instrument[Instrument.DFILE]            = unidecode.unidecode(ins_line[182:215].strip())
    instrument[Instrument.RSPTYPE]          = unidecode.unidecode(ins_line[215:228].strip())
    instrument[Instrument.LDDATE]           = unidecode.unidecode(stringToDate(ins_line[228:].strip()))
    instrument[Instrument.I_ID]             = -1
    instrument[Instrument.CSS_ID]           = unidecode.unidecode(ins_line[:8].strip())
    instrument[Instrument.RESPONSE_ID]      = -1

    return Instrument(instrument)


