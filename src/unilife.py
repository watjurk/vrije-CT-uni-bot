import csv
import datetime
import pathlib
from typing import List, Tuple


def read_unilife() -> Tuple[List[str], List[str], List[str]]:
    unilife_default_path = pathlib.Path(__file__).parent.joinpath("unilife.csv").resolve()

    unilife_sports = []
    unilife_associations = []
    unilife_events = []

    with open(unilife_default_path) as f:
        unilife_reader = csv.reader(f)
        next(unilife_reader)
        for sport, association, event in unilife_reader:
            unilife_sports.append(sport.strip())
            unilife_associations.append(association.strip())
            unilife_events.append(event.strip())

    return (unilife_sports, unilife_associations, unilife_events)


unilife_sports, unilife_associations, unilife_events = read_unilife()


def time_to_event(unilife_event: str) -> float:
    event_date_open_index = unilife_event.find("(")
    event_date = unilife_event[event_date_open_index:].replace("(", "").replace(")", "")

    def parse_datetime(date_str: str, format: str) -> datetime.datetime:
        return datetime.datetime.strptime(date_str, format)

    try:
        datetime_format = "%d %b"
        event_datetime = parse_datetime(event_date, datetime_format)
    except:
        datetime_format = "%d %B"
        event_datetime = parse_datetime(event_date, datetime_format)

    now = datetime.datetime.now()
    today_year = datetime.date.today().year

    event_datetime = event_datetime.replace(year=today_year)
    if event_datetime < now:
        event_datetime = event_datetime.replace(year=today_year + 1)

    return (event_datetime - now).total_seconds()
