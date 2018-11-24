"""Utility functions of the package music
"""

from datetime import date
from enum import Enum
from pathlib import Path

from classes2018 import settings


def format_duration(seconds):
    """Converts a duration from seconds to string of the form '<mm>:<ss>'.
    """

    return '%d:%02d' % (divmod(seconds, 60)) if seconds > 0 else 'unknown'


def format_date(a_date):
    """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'.
    """

    return a_date.strftime('%b %d, %Y') if isinstance(a_date, date) else 'unknown'


def date_py_to_json(a_date):
    """Converts datetime.date objects to JSON.
    """

    return a_date.isoformat() if isinstance(a_date, date) else 'null'


def date_json_to_py(iso_date):
    """Converts string formatted as 'YYYY-mm-dd' to datetime.date object.
    """

    return date.fromisoformat(iso_date)


def get_project_dir():
    """Returns the Path object corresponding to the project root directory.
    """

    return Path(settings.PROJECT_DIR)


def get_data_dir():
    """Returns the Path object corresponding to the data directory
    (by convention located right under the project root directory).
    """

    data_dir = Path(get_project_dir() / 'data')
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


if __name__ == '__main__':

    # print(date_py_to_json(date(1978, 3, 2)))
    # print(date_json_to_py(date_py_to_json(date(1978, 3, 2))))
    # print(str(date(1978, 3, 2)))

    pass
