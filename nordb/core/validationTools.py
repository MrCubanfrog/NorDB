"""
Module containing all the tools for validation.

Functions and Classes
---------------------
"""
import math
import logging
from datetime import time
from datetime import date
from datetime import datetime

n_types = {  0: "Nordic Event",
            1: "Nordic Main Header",
            2: "Nordic Macroseismic Header",
            3: "Nordic Comment Header",
            5: "Nordic Error Header",
            6: "Nordic Waveform Header",
            8: "Nordic Phase Data",
            9: "Scandic Header",
            10: "Station Data",
            11: "Sitechan Data",
            12: "Instrument Data",
            13: "Sensor Data",
            14: "Response Data",
            -999: "Validation Test",}

class values():
    maxInt = 9223372036854775807

def validateInteger(val, value_name, low, high, n_type):
    """
    Function that determines and returns a string as integer or None if the given value is valid integer and falls between given parameters or is empty. 

    :param str val: value to be validated
    :param str value_name: name of the parameter for messaging purposes
    :param int low: lower limit of the val
    :param int high: upper limit of the val
    :param int ntype: header name id. Used for messaging purposes
    :returns: correct value as a integer or None if it's empty
    """

    if val == "" or val is None:
        return None
    value = -9

    if type(val) is str:
        try:
            value = int(val)
        except:
            msg = "Validation Error - {0}: {1} is not an integer! ({2})"
            raise Exception(msg.format(n_types[n_type], value_name, val))
    elif type(val) is not int:
        msg = "Validation Error - {0}: {1} is of wrong type! ({2})"
        raise Exception(msg.format(n_types[n_type], value_name, type(val)))
    else:
        value = val

    if low is not None and value < low:
        msg = "Validation Error - {0}: {1} is smaller than {2}! ({3})"
        raise Exception(msg.format(n_types[n_type], value_name, low, val))

    if high is not None and value > high:
        msg = "Validation Error - {0}: {1} is larger than {2}! ({3})"
        raise Exception(msg.format(n_types[n_type], value_name, high, val))

    return value

def validateFloat(val, value_name, low, high, n_type):
    """
    Function that determines and returns string as float if the given value is valid float, falls between given parameters and is not nAn or inf.

    :param str val: value to be validated
    :param str value_name: name of the parameter for messaging purposes
    :param float low: lower limit of the val
    :param float high: upper limit of the val
    :param int ntype: header name id. Used for messaging purposes
    :returns: correct value as a float or None if it's empty
    """
    if val == "" or val is None:
        return None

    value = -9.9

    if type(val) is str:
        try:
            value = float(val)
        except:
            msg = "Validation Error - {0}: {1} is not an float! ({2})"
            raise Exception(msg.format(n_types[n_type], value_name, val))
    elif type(val) is not float:
        msg = "Validation Error - {0}: {1} is of wrong type! ({2})"
        raise Exception(msg.format(n_types[n_type], value_name, type(val)))
    else:
        value = val

    if math.isnan(value):
        msg = "Validation Error - {0}: {1} is {2} which is not allowed!"
        raise Exception(msg.format(n_types[n_type], value_name, val))

    if math.isinf(value):
        msg = "Validation Error - {0}: {1} is {2} which is not allowed!"
        raise Exception(msg.format(n_types[n_type], value_name, val))

    if low is not None and value < low:
        msg = "Validation Error - {0}: {1} is smaller than {2}! ({3})"
        raise Exception(msg.format(n_types[n_type], value_name, low, val))

    if high is not None and value > high:
        msg = "Validation Error - {0}: {1} is larger than {2}! ({3})"
        raise Exception(msg.format(n_types[n_type], value_name, high, val))

    return value

def validateString(string, string_name, minlen, maxlen, list_of_allowed, n_type):
    """
    Function that determines if val is empty, falls between given parameters or can be found from a given list.

    :param str string: value to be validated
    :param str string_name: name of the parameter for messaging purposes
    :param int minlen: lower limit of the string length
    :param int maxlen: upper limit of the string length
    :param array list_of_allowed: list of valid string from where the string needs to be found
    :param int ntype: header name id. Used for messaging purposes
    :returns: the same string or None if it's empty
    """

    if string is "" or string is None:
        return None
    if type(string) is not str:
        msg = "Validation Error - {0}: {1} is of wrong type! ({2})"
        raise Exception(msg.format(n_types[n_type], string_name, type(string)))
    string = string.strip()

    if list_of_allowed is not None and string not in list_of_allowed:
        msg = "Validation Error - {0}: {1} not in the list of allowed strings! ({2})\nAllowed:\n"
        for allowed in list_of_allowed:
            msg += "  -" + allowed + "\n"
        raise Exception(msg.format(n_types[n_type], string_name, string))

    if minlen >= -1  and len(string) < minlen:
        msg = "Validation Error - {0}: {1} is shorter than the minimum allowed length {2}! ({3})"
        raise Exception(msg.format(n_types[n_type], string_name, minlen, string))
    if minlen >= -1  and len(string) > maxlen:
        msg = "Validation Error - {0}: {1} is longer than the maximum allowed length {2}! ({3})"
        raise Exception(msg.format(n_types[n_type], string_name, maxlen, string))

    return string

def validateDatetime(datetime_val, datetime_name = None, n_type = None):
    """
    Function that determines if datetime_val is a valid datetime or empty

    :param str datetime_val: value to be validated
    :param str datetime_name: name of the parameter for messaging purposes
    :param int n_type: header name id. Used for messaging.
    :returns: Correct value as a datetime or None if it's empty
    """
    if datetime_val is None:
        return None
    if type(datetime_val) is datetime:
        return datetime_val
    if type(datetime_val) is not type("string"):
        if datetime_name is None:
            raise TypeError
        msg = "Validation Error - {0}: {1} is wrong type {2}"
        raise Exception(msg.format(n_types[n_type], datetime_name, type(datetime_val)))
    if datetime_val.strip() == "":
        return None
    try:
        return datetime (
                        year = int(datetime_val[:4]),
                        month = int(datetime_val[5:7]),
                        day = int(datetime_val[7:9]),
                        hour = int(datetime_val[10:12]),
                        minute = int(datetime_val[12:14]),
                        second = int(datetime_val[15:17]),
                        microsecond = int("{0:<06s}".format(datetime_val[18:].strip()))
                        )
    except:
        raise Exception("Validation Error - {0}: {1} is not in valid format ({2})".format(n_types[n_type],
                                                                                          datetime_name,
                                                                                          datetime_val))


def validateDate(date_string, date_name, n_type):
    """
    Function that determines if date_string is a valid date or not

    :param str date_string: value to be validated
    :param str date_name: name of the parameter for messaging purposes
    :param int ntype: header name id. Used for messaging purposes
    :returns: correct value as a date or None if it's empty
    """
    if date_string == None:
        return None
    if type(date_string) is date:
        return date_string
    if type(date_string) is datetime:
        return date_string.date()
    if type(date_string) is str and date_string.strip() == "":
        return None

    try:
        new_date = date(year=int(date_string[:4].strip()),
                        month=int(date_string[5:7].strip()),
                        day=int(date_string[7:].strip()))
    except:
        try:
            new_date = date(year=int(date_string[:4].strip()),
                            month=int(date_string[5:7].strip()),
                            day=int(date_string[8:].strip()))
        except:
            msg = "Validation Error - {0}: {1} is not parsable into date!({2})"
            raise Exception(msg.format(n_types[n_type], date_name, date_string))

    return new_date

def validateTime(time_string, time_name, n_type):
    """
    Function that determines if a time_string is a valid time or not

    :param str time_string: value to be validated
    :param str time_name: name of the parameter for messaging purposes
    :param int ntype: header name id. Used for messaging purposes
    :returns: correct value as a time or None if it's empty
    """
    if time_string == None:
        return None
    if type(time_string) is time:
        return time_string
    if type(time_string) is str and time_string.strip() == "":
        return None
    try:
        new_time = time(hour=int(time_string[:2]),
                        minute=int(time_string[2:4]),
                        second=int(time_string[5:7]),
                        microsecond=100000*int(time_string[8:]))
    except:
        msg = "Validation Error - {0}: {1} is not parsable into time!({2})"
        raise Exception(msg.format(n_types[n_type], time_name, time_string))

    return new_time
