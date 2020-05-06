NO_TRANSPORTATION_ERROR_MESSAGE = 'Boarding Card has no mean of transportation.'


class InvalidDataError(Exception):
    pass


class BoardingCardBase:

    """ This is a base class for boarding cardes of different transportations"""

    def __init__(self, transportation, **kwargs):
        self.transportation = transportation
        self.origin = kwargs.get('origin')
        self.destination = kwargs.get('destination')


class AirplaneBoardingCard(BoardingCardBase):

    def __init__(self, transportation, **kwargs):
        super().__init__(transportation, **kwargs)
        self.flight = kwargs.get('flight')
        self.seat = kwargs.get('seat')
        self.gate = kwargs.get('gate')
        self.ticket_counter = kwargs.get('ticket_counter')
        self.automatic_baggage_transfer = kwargs.get('automatic_baggage_transfer')


class TrainBoardingCard(BoardingCardBase):

    def __init__(self, transportation, **kwargs):
        super().__init__(transportation, **kwargs)
        self.seat = kwargs.get('seat')


class AirportBusBoardingCard(BoardingCardBase):

    def __init__(self, transportation, **kwargs):
        super().__init__(transportation, **kwargs)
        self.seat = kwargs.get('seat')
        
        
BOARDING_CARD_CLASS_MAP = {
    'train': TrainBoardingCard,
    'airport bus': AirportBusBoardingCard,
    'airplane': AirplaneBoardingCard
}


def boarding_card_factory(raw_data):
    try:
        transportation = raw_data.pop('transportation')
    except KeyError:
        raise InvalidDataError(NO_TRANSPORTATION_ERROR_MESSAGE)

    class_ = BOARDING_CARD_CLASS_MAP.get(transportation, BoardingCardBase)
    return class_(transportation, **raw_data)
