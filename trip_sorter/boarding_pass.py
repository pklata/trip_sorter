NO_TRANSPORTATION_ERROR_MESSAGE = 'Boarding Pass has no mean of transportation.'


class InvalidDataError(Exception):
    pass


class BoardingPassBase:

    """ This is a base class for boarding passes of different transportations"""

    def __init__(self, transportation, **kwargs):
        self.transportation = transportation
        self.origin = kwargs.get('origin')
        self.destination = kwargs.get('destination')


def boarding_pass_factory(raw_data):
    try:
        transportation = raw_data.pop('transportation')
    except KeyError:
        raise InvalidDataError(NO_TRANSPORTATION_ERROR_MESSAGE)

    return BoardingPassBase(transportation, **raw_data)
