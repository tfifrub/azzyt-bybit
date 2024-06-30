from datetime import datetime

import pytz


def ts_dt(time : int, is_ms = True):
    """
    Конвертация Timestamp в Python DateTime
    :param time:
    :param is_ms:
    :return:
    """
    if isinstance(time, str): time = int(time)
    if is_ms: time = int(time / 1000)

    return datetime.fromtimestamp(time, tz=pytz.UTC)

timestamp_ms = 1719777600000
dt_object_ms = ts_dt(timestamp_ms)
print("Milliseconds timestamp: ", dt_object_ms)

timestamp_s = 1719777600
dt_object_s = ts_dt(timestamp_s, is_ms=False)
print("Seconds timestamp: ", dt_object_s)
