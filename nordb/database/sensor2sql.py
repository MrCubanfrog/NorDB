"""
This module contains all functions and classes for reading a sensor file in `CSS3.0 format`_ and pushing it into the database

.. _CSS3.0 format: ftp://ftp.pmel.noaa.gov/newport/lau/tphase/data/css_wfdisc.pdf

Functions and Classes
---------------------
"""
from datetime import datetime

from nordb.nordic.sitechan import SiteChan
from nordb.database import sitechan2sql
from nordb.core import usernameUtilities

FAKE_CHANNEL_LINE = {
                        "n":[None, None, None, None, "n", 0.0,  0.0, 90.0, "% AUTOMATICALLY GENERATED CHANNEL! PROBABLY NOT OK", None, -1, -1, -1],
                        "e":[None, None, None, None, "n", 0.0, 90.0, 90.0, "% AUTOMATICALLY GENERATED CHANNEL! PROBABLY NOT OK", None, -1, -1, -1],
                        "z":[None, None, None, None, "n", 0.0, -1.0,  0.0, "% AUTOMATICALLY GENERATED CHANNEL! PROBABLY NOT OK", None, -1, -1, -1],
                    }

SENSOR_INSERT = (
                "INSERT INTO sensor "
                "   (time, endtime, jdate, calratio, "
                "   calper, tshift, instant, lddate, "
                "   sitechan_id, instrument_id) "
                "VALUES "
                "(  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
                )

def genFakeChannel(sensor):
    """
    Function for generating a false SiteChan object related to the Sensor object given by user.
    This is used to quarantee that all sensors are attached to a SiteChan in the database.

    :param Sensor sensor: Sensor object for which the SiteChan is generated for
    :returns: SiteChan object
    """
    fakeChan = SiteChan(FAKE_CHANNEL_LINE[sensor.channel_code[-1].lower()])
    fakeChan.station_code = sensor.station_code
    fakeChan.channel_code = sensor.channel_code[0].upper() + "H" + sensor.channel_code[-1].upper()
    fakeChan.css_id = sensor.channel_css_id
    fakeChan.on_date = datetime.fromtimestamp(sensor.time).date()

    if sensor.endtime != 9999999999.999:
        fakeChan.off_date = datetime.fromtimestamp(sensor.endtime).date()

    if fakeChan.css_id == -1:
        conn = usernameUtilities.log2nordb()
        cur = conn.cursor()

        cur.execute("SELECT MAX(css_id) FROM sitechan;")
        ans = cur.fetchone()
        if ans is None:
            css_id = 0
        else:
            css_id = ans[0]+1

        fakeChan.css_id = css_id

    return fakeChan

def insertSensor2Database(sensor):
    """
    Function for inserting the sensor array to the database

    :param Sensor sensor: sensor that will be inserted to the database
    """
    conn = usernameUtilities.log2nordb()
    cur = conn.cursor()

    try:
        cur.execute("SELECT id FROM instrument WHERE css_id = %s", (sensor.instrument_css_id,))
        ans = cur.fetchone()

        if ans is None:
            raise Exception("No instrument for sensor")

        sensor.instrument_id = ans[0]

        cur.execute("SELECT id FROM sitechan WHERE css_id = %s", (sensor.channel_css_id,))
        ans = cur.fetchone()

        if ans is None:
            fakeChan = genFakeChannel(sensor)
            sitechan2sql.insertSiteChan2Database(fakeChan)
            sensor.channel_css_id = fakeChan.css_id
            cur.execute("SELECT id FROM sitechan WHERE css_id = %s", (fakeChan.css_id,))
            ans = cur.fetchone()

            if ans is None:
                raise Exception("Cannot find the fake channel for the sensor")

        sensor.channel_id = ans[0]

        cur.execute(SENSOR_INSERT, sensor.getAsList())
    except Exception as e:
        conn.close()
        raise e
    conn.commit()
    conn.close()

