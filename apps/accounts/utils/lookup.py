"""lookup.py

Look up users by various complex logic
"""

from django.contrib.auth import get_user_model

from htk.utils import utcnow
from htk.utils.datetime_utils import get_timezones_within_current_local_time_bounds

def get_users_currently_at_local_time(start_hour, end_hour):
    """Returns a list of Users whose current local time is within a time range

    Strategy 1 (inefficient):
    enumerate through every User, and keep the ones whose current local time is within the range

    Strategy 2:
    - find all the timezones that are in the local time
    - query users in that timezone

    `start_hour` and `end_hour` are naive datetimes
    """
    timezones = get_timezones_within_current_local_time_bounds(start_hour, end_hour)
    UserModel = get_user_model()
    users = UserModel.objects.filter(
        profile__timezone__in=timezones
    )
    return users
