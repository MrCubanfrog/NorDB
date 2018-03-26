"""
This module contains all functions for adding, modifying and removing solution_type ids in the database.

Functions and Classes
---------------------
"""
from nordb.core import usernameUtilities
from nordb.database import nordicModify
from nordb.database import nordicSearch

def addSolutionType(type_id, type_desc, allow_multiple):
    """
    This function adds a new solution type to the database with id of type_id.
    
    :param str type_id: The id of the solution_type. Maximum of 6 characters
    :param str type_desc: The description of the solution type id. Maximum of 32 characters
    :param boolean allow_multiple: flag for allowing multiple events with same solution_type into the event_root
    """
    if len(type_id) > 6:
        raise Exception("Solution type {0} is too long! Maximum of 6 characters!".format(type_id))

    if len(type_desc) > 32:
        raise Exception("Solution type description ({0}) is too long! Maximum on 32 characters")

    conn = usernameUtilities.log2nordb()
    cur = conn.cursor()

    cur.execute("SELECT allow_multiple FROM solution_type WHERE type_id = %s", (type_id,))
    ans = cur.fetchone()
    
    if ans is not None:
        raise Exception("{0} is already in the database! Either remove the old solution type from the database or consider a new id for the new one".format(type_id))

    cur.execute("INSERT INTO solution_type (type_id, type_desc, allow_multiple) VALUES (%s, %s, %s)", (type_id, type_desc, allow_multiple))

    conn.commit()
    conn.close() 

def getSolutionTypes():
    """
    Function for getting all solution types from the database as an array.

    :returns: Solution type id, description and allow_multiple values in a array
    """
    conn = usernameUtilities.log2nordb()
    cur = conn.cursor()

    cur.execute("SELECT type_id, type_desc, allow_multiple FROM solution_type")
    ans = cur.fetchall()

    conn.close()
    return ans

def removeSolutionType(solution_type, new_solution_type = None):
    """
    This function changes all old events with solution_type id solution_type to new_solution_type and removes the solution_type from the database.

    :param str solution_type: solution_type to be removed
    :param str new_solution_type: new solution_type
    """
    search = nordicSearch.NordicSearch()
    search.addSearchExactly("solution_type", solution_type)
    e_ids = search.searchEventIds()

    for e_id in e_ids:
        nordicModify.changeSolutionType(e_id, new_solution_type)

    conn = usernameUtilities.log2nordb()
    cur = conn.cursor()

    cur.execute("DELETE FROM solution_type WHERE type_id = %s", (solution_type,))

    conn.commit()
    conn.close()
