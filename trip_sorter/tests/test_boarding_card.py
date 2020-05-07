from unittest import TestCase
from trip_sorter.boarding_card import boarding_card_factory, BoardingCardBase, \
    AirplaneBoardingCard, TrainBoardingCard, AirportBusBoardingCard


class BoardingCardTest(TestCase):

    def test_boarding_card_factory_returns_boarding_card(self):
        transportation = 'airplane'
        origin = 'Stockholm'
        destination = 'New York JFK'

        raw_boarding_card_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination
        }
        boarding_card = boarding_card_factory(raw_boarding_card_data)

        self.assertIsInstance(boarding_card, BoardingCardBase)
        self.assertEqual(boarding_card.transportation, transportation)
        self.assertEqual(boarding_card.origin, origin)
        self.assertEqual(boarding_card.destination, destination)


class AirplaneBoardingCardTest(TestCase):

    def test_boarding_card_factory_returns_airplane_boarding_card(self):
        transportation = 'airplane'
        origin = 'Girona Airport'
        destination = 'Stockholm'
        flight = 'SK455'
        seat = '3A'
        gate = '45B'
        ticket_counter = '344'
        automatic_baggage_transfer = True

        raw_boarding_card_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination,
            'flight': flight,
            'seat': seat,
            'gate': gate,
            'ticket_counter': ticket_counter,
            'automatic_baggage_transfer': automatic_baggage_transfer
        }
        boarding_card = boarding_card_factory(raw_boarding_card_data)

        self.assertIsInstance(boarding_card, AirplaneBoardingCard)
        self.assertEqual(boarding_card.transportation, transportation)
        self.assertEqual(boarding_card.origin, origin)
        self.assertEqual(boarding_card.destination, destination)
        self.assertEqual(boarding_card.flight, flight)
        self.assertEqual(boarding_card.seat, seat)
        self.assertEqual(boarding_card.gate, gate)
        self.assertEqual(boarding_card.ticket_counter, ticket_counter)
        self.assertEqual(boarding_card.automatic_baggage_transfer, automatic_baggage_transfer)

    def test_airport_bus_boarding_card_description(self):
        data1 = {
            'transportation': 'airplane',
            'origin': 'Girona Airport',
            'destination': 'Stockholm',
            'flight': 'SK455',
            'seat': '3A',
            'gate': '45B',
            'ticket_counter': '344'
        }
        boarding_card1 = boarding_card_factory(data1)
        expected_text1 = 'From Girona Airport, take flight SK455 to Stockholm. ' \
                         'Gate 45B, seat 3A. Baggage drop at ticket counter 344.'

        self.assertEqual(boarding_card1.description, expected_text1)

        data2 = {
            'transportation': 'airplane',
            'origin': 'Stockholm',
            'destination': 'New York JFK',
            'flight': 'SK22',
            'seat': '7B',
            'gate': '22',
            'automatic_baggage_transfer': True
        }
        boarding_card2 = boarding_card_factory(data2)
        expected_text2 = 'From Stockholm, take flight SK22 to New York JFK. Gate 22, seat 7B. ' \
                         'Baggage will we automatically transferred from your last leg.'

        self.assertEqual(boarding_card2.description, expected_text2)


class AirportBusBoardingCardTest(TestCase):

    def test_boarding_card_factory_returns_airport_bus_boarding_card(self):
        transportation = 'airport bus'
        origin = 'Barcelona'
        destination = 'Girona Airport'

        raw_boarding_card_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination,
        }
        boarding_card = boarding_card_factory(raw_boarding_card_data)

        self.assertIsInstance(boarding_card, AirportBusBoardingCard)
        self.assertEqual(boarding_card.transportation, transportation)
        self.assertEqual(boarding_card.origin, origin)
        self.assertEqual(boarding_card.destination, destination)

    def test_airport_bus_boarding_card_description(self):
        data = {
            'transportation': 'airport bus',
            'origin': 'Barcelona',
            'destination': 'Girona Airport',
            'seat': None
        }
        boarding_card = boarding_card_factory(data)
        expected_text = 'Take the airport bus from Barcelona to Girona Airport. No seat assignment.'
        self.assertEqual(boarding_card.description, expected_text)


class TrainBoardingCardTest(TestCase):

    def test_boarding_card_factory_returns_train_boarding_card(self):
        transportation = 'train'
        origin = 'Madrid'
        destination = 'Barcelona'
        seat = '45B'
        number = '78A'

        raw_boarding_card_data = {
            'transportation': transportation,
            'origin': origin,
            'destination': destination,
            'seat': seat,
            'number': number
        }
        boarding_card = boarding_card_factory(raw_boarding_card_data)

        self.assertIsInstance(boarding_card, TrainBoardingCard)
        self.assertEqual(boarding_card.transportation, transportation)
        self.assertEqual(boarding_card.origin, origin)
        self.assertEqual(boarding_card.destination, destination)
        self.assertEqual(boarding_card.seat, seat)
        self.assertEqual(boarding_card.number, number)

    def test_train_boarding_card_description(self):
        data = {
            'transportation': 'train',
            'origin': 'Madrid',
            'destination': 'Barcelona',
            'seat': '45B',
            'number': '78A'
        }
        boarding_card = boarding_card_factory(data)
        expected_text = 'Take train 78A from Madrid to Barcelona. Sit in seat 45B.'
        self.assertEqual(boarding_card.description, expected_text)
