from datetime import datetime


def get_datetime() -> dict:
    """Retrieve the current time and date.

    Use this tool when the user makes a reference to the current date or time,
    or when the user asks for care recommendations that depend on the time of
    year.

    Returns:
        dict: The current date and time.
            On success: {"status": "success", "datetime": "<current datetime in ISO format>"}
            On error: {"status": "error", "message": "<error message>"}
    """
    return {"status": "success", "datetime": datetime.now().isoformat()}
