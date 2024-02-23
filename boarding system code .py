from enum import Enum
class Method(Enum):
    CREDIT_CARD = 'Credit Card'
    DEBIT_CARD = 'Debit Card'
    PAYPAL = 'PayPal'
    CASH = 'Cash'
class Status(Enum):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    CANCELLED = 'Cancelled'
class ClassType(Enum):
    ECONOMY = 'Economy'
    BUSINESS = 'Business'
    FIRST_CLASS = 'First Class'
class Availability(Enum):
    AVAILABLE = 'Available'
    BOOKED = 'Booked'
class Airline(Enum):
    NATIONAL_AIRLINES = 'National Airlines'
    DELTA_AIRLINES = 'Delta Airlines'
    UNITED_AIRLINES = 'United Airlines'
    AMERICAN_AIRLINES = 'American Airlines'
class Passenger:
    def __init__(self, passenger_id, name, contact_info, passport_number):
        self.passenger_id = passenger_id
        self.name = name
        self.contact_info = contact_info
        self.passport_number = passport_number
    # Setter and getter methods for passenger_id
    def set_passenger_id(self, passenger_id):
        self.passenger_id = passenger_id
    def get_passenger_id(self):
        return self.passenger_id
    # Setter and getter methods for name
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    # Setter and getter methods for contact_info
    def set_contact_info(self, contact_info):
        self.contact_info = contact_info
    def get_contact_info(self):
        return self.contact_info
    # Setter and getter methods for passport_number
    def set_passport_number(self, passport_number):
        self.passport_number = passport_number
    def get_passport_number(self):
        return self.passport_number
    # Other required functions (to be implemented)
class Flight:
    def __init__(self, flight_number, departure_time, arrival_time, origin, destination, airline):
        self.flight_number = flight_number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.origin = origin
        self.destination = destination
        self.airline = airline
    # Setter and getter methods for flight_number
    def set_flight_number(self, flight_number):
        self.flight_number = flight_number
    def get_flight_number(self):
        return self.flight_number
    # Setter and getter methods for departure_time
    def set_departure_time(self, departure_time):
        self.departure_time = departure_time
    def get_departure_time(self):
        return self.departure_time
    # Setter and getter methods for arrival_time
    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time
    def get_arrival_time(self):
        return self.arrival_time
    # Setter and getter methods for origin
    def set_origin(self, origin):
        self.origin = origin
    def get_origin(self):
        return self.origin
    # Setter and getter methods for destination
    def set_destination(self, destination):
        self.destination = destination
    def get_destination(self):
        return self.destination
    # Setter and getter methods for airline
    def set_airline(self, airline):
        self.airline = airline
    def get_airline(self):
        return self.airline
    # Other required functions (to be implemented)
class Booking(Passenger, Flight):
    def __init__(self, booking_id, flight, passenger):
        Passenger.__init__(self, passenger.passenger_id, passenger.name, passenger.contact_info,
                           passenger.passport_number)
        Flight.__init__(self, flight.flight_number, flight.departure_time, flight.arrival_time, flight.origin,
                        flight.destination, flight.airline)
        self.booking_id = booking_id
    # Setter and getter methods for booking_id
    def set_booking_id(self, booking_id):
        self.booking_id = booking_id
    def get_booking_id(self):
        return self.booking_id
    # Other required functions (to be implemented)
class BoardingPass(Flight, Passenger):
    def __init__(self, boarding_pass_id, gate, boarding_time, flight, passenger):
        Flight.__init__(self, flight.flight_number, flight.departure_time, flight.arrival_time, flight.origin,
                        flight.destination, flight.airline)
        Passenger.__init__(self, passenger.passenger_id, passenger.name, passenger.contact_info,
                           passenger.passport_number)
        self.boarding_pass_id = boarding_pass_id
        self.gate = gate
        self.boarding_time = boarding_time
    # Setter and getter methods for boarding_pass_id
    def set_boarding_pass_id(self, boarding_pass_id):
        self.boarding_pass_id = boarding_pass_id
    def get_boarding_pass_id(self):
        return self.boarding_pass_id
    # Setter and getter methods for gate
    def set_gate(self, gate):
        self.gate = gate
    def get_gate(self):
        return self.gate
    # Setter and getter methods for boarding_time
    def set_boarding_time(self, boarding_time):
        self.boarding_time = boarding_time
    def get_boarding_time(self):
        return self.boarding_time
    # Other required functions (to be implemented)
class Payment:
    def __init__(self, amount, method, status):
        self.amount = amount
        self.method = method
        self.status = status
    # Setter and getter methods for amount
    def set_amount(self, amount):
        self.amount = amount
    def get_amount(self):
        return self.amount
    # Setter and getter methods for method
    def set_method(self, method):
        self.method = method
    def get_method(self):
        return self.method
    # Setter and getter methods for status
    def set_status(self, status):
        self.status = status
    def get_status(self):
        return self.status
    # Other required functions (to be implemented)
class AirportStaff:
    def __init__(self, staff_id, name, role):
        self.staff_id = staff_id
        self.name = name
        self.role = role
    # Setter and getter methods for staff_id
    def set_staff_id(self, staff_id):
        self.staff_id = staff_id
    def get_staff_id(self):
        return self.staff_id
    # Setter and getter methods for name
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    # Setter and getter methods for role
    def set_role(self, role):
        self.role = role
    def get_role(self):
        return self.role
    # Other required functions (to be implemented)
class SystemAdministrator:
    def __init__(self, admin_id, name):
        self.admin_id = admin_id
        self.name = name
    # Setter and getter methods for admin_id
    def set_admin_id(self, admin_id):
        self.admin_id = admin_id
    def get_admin_id(self):
        return self.admin_id
# Define Seat class
class Seat:
    def __init__(self, seat_number, class_type, availability):
        self.seat_number = seat_number
        self.class_type = class_type
        self.availability = availability
    def __str__(self):
        return f"Seat Number: {self.seat_number}, Class Type: {self.class_type}, Availability: {self.availability.value}"
# Create Passenger
passenger1 = Passenger(passenger_id=1, name="John Doe", contact_info="john@example.com", passport_number="AB123456")
# Create Flight
flight1 = Flight(flight_number="NA123", departure_time="2024-02-22 08:00", arrival_time="2024-02-22 10:00",
                 origin="Chicago ORD", destination="New York JFK", airline=Airline.NATIONAL_AIRLINES)
# Create Booking
booking1 = Booking(booking_id=123, flight=flight1, passenger=passenger1)
# Create BoardingPass
boarding_pass1 = BoardingPass(boarding_pass_id=456, gate="Gate 1", boarding_time="2024-02-22 07:30", flight=flight1,
                              passenger=passenger1)
seat1 = Seat(seat_number="9A", class_type=ClassType.FIRST_CLASS, availability=Availability.AVAILABLE)
# Display Booking and BoardingPass details
print("Booking Details:")
print("Booking ID:", booking1.get_booking_id())
print("Passenger Name:", booking1.get_name())
print("Flight Number:", booking1.get_flight_number())
print("Departure Time:", booking1.get_departure_time())
print("Arrival Time:", booking1.get_arrival_time())
print("Origin:", booking1.get_origin())
print("Destination:", booking1.get_destination())
print("Airline:", booking1.get_airline())
print("\nBoarding Pass Details:")
print("Boarding Pass ID:", boarding_pass1.get_boarding_pass_id())
print("Gate:", boarding_pass1.get_gate())
print("Boarding Time:", boarding_pass1.get_boarding_time())
print("Passenger Name:", boarding_pass1.get_name())
print("Flight Number:", boarding_pass1.get_flight_number())
print("Departure Time:", boarding_pass1.get_departure_time())
print("Arrival Time:", boarding_pass1.get_arrival_time())
print("Origin:", boarding_pass1.get_origin())
print("Destination:", boarding_pass1.get_destination())
print("Airline:", boarding_pass1.get_airline())
print("Seat Details:")
print(seat1)

