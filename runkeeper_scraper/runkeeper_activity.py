import config
from bs4 import BeautifulSoup as BfS
from datetime import datetime


class RunkeeperActivity:
    def __init__(self, my_user, activity_info):
        self.activity_id = activity_info.get('activity_id')
        self.distance = activity_info.get('distance')
        self.distance_units = activity_info.get('distanceUnits')
        self.day_of_month = activity_info.get('dayOfMonth')
        self.month = activity_info.get('month')
        self.year = activity_info.get('year')
        self.user = my_user
        self.session = my_user.session

    def download_activity_as_gpx(self):
        download_activity_url = '{}/download/activity'.format(config.SITE_URL)
        payload = {'activityId': self.activity_id, 'downloadType': 'gpx'}
        gpx_activity = self.session.get(download_activity_url, params=payload)
        return gpx_activity.text

    def get_activity_url(self):
        activity_url = '{}/user/{}/activity/{}'.format(config.SITE_URL,
                                                       self.user.profile_name,
                                                       self.activity_id)
        return activity_url

    def get_activity_datetime(self):
        activity_url = self.get_activity_url()
        activity_session = self.session.get(activity_url)
        soup = BfS(activity_session.text, 'html.parser')
        datetime_form = soup.find('div', {'class': 'micro-text activitySubTitle'})
        for date_info in datetime_form:
            activity_datetime_split = date_info.split('-')[0].rstrip()
            activity_datetime_string = ''.join(activity_datetime_split)
            activity_datetime = datetime.strptime(activity_datetime_string, '%a %b %d %H:%M:%S %Z %Y')
        return activity_datetime

    def get_converted_datetime(self):
        converted_datetime = datetime.strftime(self.get_activity_datetime(), '%Y-%m-%d_%H%M%S')
        return converted_datetime
