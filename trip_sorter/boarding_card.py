from trip_sorter.errors import InvalidDataError

NO_TRANSPORTATION_ERROR_MESSAGE = 'Boarding Card has no mean of transportation.'


class BoardingCardBase:

    """ This is a base class for boarding cardes of different transportations
    Means of transportation can be added by implementing this interface"""

    def __init__(self, transportation, **kwargs):
        self.transportation = transportation
        self.origin = kwargs.get('origin')
        self.destination = kwargs.get('destination')

    @property
    def description(self):
        raise InvalidDataError("This is a base class, does nothing.")


class AirplaneBoardingCard(BoardingCardBase):

    def __init__(self, transportation, **kwargs):
        super().__init__(transportation, **kwargs)
        self.flight = kwargs.get('flight')
        self.seat = kwargs.get('seat')
        self.gate = kwargs.get('gate')
        self.ticket_counter = kwargs.get('ticket_counter')
        self.automatic_baggage_transfer = kwargs.get('automatic_baggage_transfer')

    @property
    def description(self):
        description = f'From {self.origin}, take flight {self.flight} to {self.destination}.'
        description = f'{description} Gate {self.gate}, seat {self.seat}.'
        if self.automatic_baggage_transfer:
            return f'{description} Baggage will we automatically transferred from your last leg.'
        return f'{description} Baggage drop at ticket counter {self.ticket_counter}.'


class TrainBoardingCard(BoardingCardBase):

    def __init__(self, transportation, **kwargs):
        super().__init__(transportation, **kwargs)
        self.number = kwargs.get('number')
        self.seat = kwargs.get('seat')

    @property
    def description(self):
        return f'Take train {self.number} from {self.origin} to {self.destination}. Sit in seat {self.seat}.'


class AirportBusBoardingCard(BoardingCardBase):

    def __init__(self, transportation, **kwargs):
        super().__init__(transportation, **kwargs)

    @property
    def description(self):
        return f'Take the airport bus from {self.origin} to {self.destination}. No seat assignment.'


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
