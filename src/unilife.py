import csv         # Importing the csv module for CSV file operations
import datetime    # Importing the datetime module for date and time manipulation
import pathlib     # Importing pathlib for file path operations
from typing import List, Tuple  

def read_unilife() -> Tuple[List[str], List[str], List[str]]: # Function to read data from a 'unilife.csv' file and return lists of sports, associations, and events
    unilife_default_path = pathlib.Path(__file__).parent.joinpath("unilife.csv").resolve()  # defining a path to the 'unilife.csv' file 

    unilife_sports = []           # Initializing lists to store sports data
    unilife_associations = []     # Initializing lists to store association data
    unilife_events = []           # Initializing lists to store events data

    with open(unilife_default_path) as f:   # Opening the CSV file and reading its contents
        unilife_reader = csv.reader(f)
        next(unilife_reader)                # Skipping the header row of the CSV file
        # Iterating over each row in the CSV file
        for sport, association, event in unilife_reader:
            # Stripping whitespace and adding the data to respective 3 pre-defined lists
            unilife_sports.append(sport.strip())
            unilife_associations.append(association.strip())
            unilife_events.append(event.strip())

    return (unilife_sports, unilife_associations, unilife_events)  # Returning  with filled lists of sports, associations, and events

unilife_sports, unilife_associations, unilife_events = read_unilife() # Running the function and storing the data in respective variables

def time_to_event(unilife_event: str) -> float:    # Function to calculate the time until a given event in seconds
    event_date_open_index = unilife_event.find("(") # Finding the index of the opening to find the event date
    event_date = unilife_event[event_date_open_index:].replace("(", "").replace(")", "") # Collecting the date string from the event and removing parentheses

    def parse_datetime(date_str: str, format: str) -> datetime.datetime: #Defining a function which converts date string(from unilife.csv)into python object
        return datetime.datetime.strptime(date_str, format)              #returning the converted datetime object
    
    try:
        datetime_format = "%d %b"  # First datetime format
        event_datetime = parse_datetime(event_date, datetime_format)
    except:
        datetime_format = "%d %B"  # Second datetime format in exception cases
        event_datetime = parse_datetime(event_date, datetime_format)

    now = datetime.datetime.now()            #importing the current date and time
    today_year = datetime.date.today().year  # importing the current year

    event_datetime = event_datetime.replace(year=today_year)           # Updating the year in the event's datetime object
    if event_datetime < now:                                           # If the event date is in the past
        event_datetime = event_datetime.replace(year=today_year + 1)   #replace it to the next year
    return (event_datetime - now).total_seconds()                      # Returning the time difference between now and the event time in seconds
