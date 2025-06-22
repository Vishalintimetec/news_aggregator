from datetime import datetime

def format_datetime(dt: datetime, mode: str = "full"):
    if mode == "date":
        return dt.strftime("%d-%b-%Y")
    elif mode == "time":
        return dt.strftime("%I:%M%p")
    return dt.strftime("%d-%b-%Y %I:%M%p")
