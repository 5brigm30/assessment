"""
NO FUNCTIONS SHOULD BE ADDED OR REMOVED FROM THIS MODULE. SIMPLY COMPLETE EACH FUNCTION AS DESCRIBED.
YOU SHOULD ALSO NOT REMOVE ANY OF THE COMMENTS OR CHANGE THE STRUCTURE IN ANY WAY OTHER THAN AS INSTRUCTED.

This module is responsible for reading from and writing to the data file.
"""

# import required modules
import csv
import tui


# path to data file
relative_file_path = 'data/sales.csv'


def file_path():
    """
    Task 1: Return the path to the sales data file.
    
    The function should return the value of the relative file path variable.

    :return: A string which is the path to the sales data file.
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    global relative_file_path
    return relative_file_path


def load_data():
    """
    Task 2: Load data from the sales data file.

    The function should read the headings and each record from the sales data file.
    The function should return a tuple containing both a list of headings and a list of records.

    For higher marks (advance task):
        - Values in a record stored in the list of records should be of the correct type.
        - For example, record ids should be stored as integers, postal codes should be stored as integers and profit
        should be stored as float. Dates can be stored as strings.
        - Modify the function so that it stores values in each record with the correct type.

    For even higher marks (advance task):
        - the function should indicate the progress made by invoking the tui module's status function.
        - the progress message should be of the form 'Loaded records... (X)%'
        where 'X' is a whole number that indicates the percentage of records that have been loaded.
        - the progress message should only be displayed each time another 10% of the records have been loaded
        (i.e when 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80% and 90% of records have been loaded)
        - the progress message should not be displayed when no records (0%) have been loaded or
        all the records (100%) have been loaded

    :return: A tuple where the first item is a list containing the headings
    and the second item is a list containing the records
    """
    # TODO: Your code here (replace this TODO and remove the keyword pass)
    data_file = file_path()
    data = []
    try:
        with open(data_file) as file:
            readfile = csv.reader(file)
            headings = next(readfile)
            for record in readfile:
                data.append(record)
            tuple_list = (headings, data)
            return tuple_list
    except IOError:
        return 'cannot readfile'

