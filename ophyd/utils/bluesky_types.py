from typing import (
    Generic,
    ParamSpec,
    TypeVar,
    TypedDict,
)


# TODO: these are not placed in Events by RE yet
class ReadingOptional(TypedDict, total=False):
    """A dictionary containing the optional per-reading metadata of a piece of scan data"""

    #: * -ve: alarm unknown, e.g. device disconnected
    #: * 0: ok, no alarm
    #: * +ve: there is an alarm
    #:
    #: The exact numbers are transport specific
    alarm_severity: int
    #: A descriptive message if there is an alarm
    message: str


T = TypeVar("T")
P = ParamSpec("P")


class Reading(Generic[T], ReadingOptional):
    """A dictionary containing the value and timestamp of a piece of scan data"""

    #: The current value, as a JSON encodable type or numpy array
    value: T
    #: Timestamp in seconds since the UNIX epoch
    timestamp: float
