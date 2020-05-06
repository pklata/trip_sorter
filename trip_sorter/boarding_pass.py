NO_TRANSPORTATION_ERROR_MESSAGE = 'Boarding Pass has no mean of transportation.'


class InvalidDataError(Exception):
    pass


class BoardingPassBase:

    """ This is a base class for boarding passes of different transportations"""

    def __init__(self, transportation, **kwargs):
        self.transportation = transportation
        self.origin = kwargs.get('origin')
        self.destination = kwargs.get('destination')


class AirplaneBoardingPass(BoardingPassBase):

    def __init__(self, transportation, **kwargs):
        super().__init__(transportation, **kwargs)
        self.flight = kwargs.get('flight')
        self.seat = kwargs.get('seat')
        self.gate = kwargs.get('gate')
        self.ticket_counter = kwargs.get('ticket_counter')
        self.automatic_baggage_transfer = kwargs.get('automatic_baggage_transfer')


class TrainBoardingPass(BoardingPassBase):

    def __init__(self, transportation, **kwargs):
        super().__init__(transportation, **kwargs)
        self.seat = kwargs.get('seat')


class AirportBusBoardingPass(BoardingPassBase):

    def __init__(self, transportation, **kwargs):
        super().__init__(transportation, **kwargs)
        self.seat = kwargs.get('seat')
        
        
BOARDING_CARD_CLASS_MAP = {
    'train': TrainBoardingPass,
    'airport bus': AirportBusBoardingPass,
    'airplane': AirplaneBoardingPass
}


def boarding_pass_factory(raw_data):
    try:
        transportation = raw_data.pop('transportation')
    except KeyError:
        raise InvalidDataError(NO_TRANSPORTATION_ERROR_MESSAGE)

    class_ = BOARDING_CARD_CLASS_MAP.get(transportation, BoardingPassBase)
    return class_(transportation, **raw_data)
