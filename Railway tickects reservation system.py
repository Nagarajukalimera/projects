class RailwayTicketReservationSystem:
    def __init__(self):
        # Initialize available trains and bookings
        self.trains = [
            {"train_no": 101, "source": "Delhi", "destination": "Mumbai", "available_seats": 100},
            {"train_no": 102, "source": "Chennai", "destination": "Bangalore", "available_seats": 50},
            {"train_no": 103, "source": "Kolkata", "destination": "Hyderabad", "available_seats": 75},
            {"train_no": 104, "source": "Ahmedabad", "destination": "Pune", "available_seats": 60},
        ]
        self.bookings = []

    def show_trains(self):
        # Display available trains
        print("\nAvailable Trains:")
        for train in self.trains:
            print(f"Train No: {train['train_no']} | {train['source']} to {train['destination']} | Available Seats: {train['available_seats']}")

    def book_ticket(self):
        # Book a ticket
        self.show_trains()
        try:
            train_no = int(input("\nEnter the Train No. to book a ticket: "))
            passenger_name = input("Enter passenger's name: ")
            num_seats = int(input(f"Enter number of seats to book (Available seats: {self.get_available_seats(train_no)}): "))
            
            if num_seats <= 0:
                print("Invalid number of seats!")
                return

            available_seats = self.get_available_seats(train_no)
            if num_seats > available_seats:
                print(f"Sorry, not enough seats available. Only {available_seats} seats available.")
                return

            for train in self.trains:
                if train['train_no'] == train_no:
                    # Update available seats in train and booking list
                    train['available_seats'] -= num_seats
                    self.bookings.append({
                        "train_no": train_no,
                        "passenger_name": passenger_name,
                        "num_seats": num_seats
                    })
                    print(f"Ticket booked successfully for {passenger_name}. Train No: {train_no}, Seats: {num_seats}")
                    break
        except ValueError:
            print("Invalid input. Please enter the correct details.")

    def get_available_seats(self, train_no):
        # Get available seats for a given train
        for train in self.trains:
            if train['train_no'] == train_no:
                return train['available_seats']
        return 0

    def cancel_ticket(self):
        # Cancel a booked ticket
        passenger_name = input("\nEnter the passenger's name to cancel the ticket: ")
        train_no = int(input("Enter the Train No. of the ticket to cancel: "))

        for booking in self.bookings:
            if booking['train_no'] == train_no and booking['passenger_name'].lower() == passenger_name.lower():
                # Update available seats in the corresponding train
                for train in self.trains:
                    if train['train_no'] == train_no:
                        train['available_seats'] += booking['num_seats']
                        print(f"Ticket canceled successfully for {passenger_name}. Seats refunded: {booking['num_seats']}")
                        self.bookings.remove(booking)  # Remove the booking
                        return
                break
        else:
            print("Booking not found! Please check the details and try again.")

    def view_bookings(self):
        # View all current bookings
        if not self.bookings:
            print("\nNo bookings found.")
        else:
            print("\nCurrent Bookings:")
            for booking in self.bookings:
                print(f"Passenger: {booking['passenger_name']} | Train No: {booking['train_no']} | Seats: {booking['num_seats']}")

def main():
    system = RailwayTicketReservationSystem()
    
    while True:
        print("\n===== Railway Ticket Reservation System =====")
        print("1. View Available Trains")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View All Bookings")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            system.show_trains()
        elif choice == "2":
            system.book_ticket()
        elif choice == "3":
            system.cancel_ticket()
        elif choice == "4":
            system.view_bookings()
        elif choice == "5":
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
