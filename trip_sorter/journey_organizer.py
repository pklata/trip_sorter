from trip_sorter.errors import InvalidDataError


class JourneyOrganizer:
    """Collection of Boarding Cards"""

    def __init__(self):
        # there will be a little memory overhead but
        # we won't have to iterate over dict
        self._items_by_origin = dict()
        self._items_by_destination = dict()

    def add(self, item):
        if item.destination in self._items_by_destination:
            raise InvalidDataError('Duplicated destination')
        if item.origin in self._items_by_origin:
            raise InvalidDataError('Duplicated origin')
        self._items_by_origin[item.origin] = item
        self._items_by_destination[item.destination] = item

    def sorted(self):
        starting_points = list(self._items_by_origin.keys()
                               - self._items_by_destination.keys())

        if len(starting_points) != 1:
            raise InvalidDataError('Origin can not be found')
        origin = starting_points[0]

        final_destinations = list(self._items_by_destination.keys()
                                  - self._items_by_origin.keys())

        if len(final_destinations) != 1:
            raise InvalidDataError('Destination can not be found')
        destination = final_destinations[0]

        ordered_items = list()
        while True:
            ordered_items.append(self._items_by_origin[origin])
            origin = self._items_by_origin[origin].destination
            if origin == destination:
                break

        return ordered_items

    def get_journey_plan(self):
        ordered_items = self.sorted()
        journey_plan = f''
        stage = 1
        for item in ordered_items:
            journey_plan = f'{journey_plan}{stage}. {item.description}\n'
            stage += 1
        journey_plan = f'{journey_plan}{stage}. ' \
                       f'You have arrived at your final destination.'
        return journey_plan
