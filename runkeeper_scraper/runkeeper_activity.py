

class RunkeeperActivity:
    def __init__(self, activity_info):
        self.activity_id = activity_info.get('activity_id')
        self.distance = activity_info.get('distance')
        self.distance_units = activity_info.get('distanceUnits')
        self.day_of_month = activity_info.get('dayOfMonth')
        self.month = activity_info.get('month')
        self.year = activity_info.get('year')
