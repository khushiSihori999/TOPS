
class BusReservation:
    def __init__(self):
        # Predefined routes with prices
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 700,
            "Ahmedabad to Surat": 400
        }
        self.tickets = {}   # Store tickets {ticket_id: details}
        self.next_ticket_id = 1
        self.available_seats = {route: 40 for route in self.routes}

    #  Show Available Routes (numbered)
    def show_routes(self):
        print("\n--- Available Routes ---")
        for i, (route, price) in enumerate(self.routes.items(), start=1):
            seats = self.available_seats[route]
            print(f"{i}. {route} - ₹{price} | Seats Left: {seats}")

    #  Book Ticket (route can be route string or route index)
    def book_ticket(self, name, age, mobile, route_choice):
        # Resolve route_choice (accept number or exact route string)
        routes_list = list(self.routes.keys())
        route = None
        if isinstance(route_choice, int):
            idx = route_choice - 1
            if 0 <= idx < len(routes_list):
                route = routes_list[idx]
        else:
            # accept exact match (case-sensitive) or case-insensitive match
            if route_choice in self.routes:
                route = route_choice
            else:
                for r in routes_list:
                    if r.lower() == route_choice.strip().lower():
                        route = r
                        break

        if route is None:
            print("Invalid route selection!")
            return None

        if self.available_seats[route] <= 0:
            print("No seats available for this route!")
            return None

        if not (mobile.isdigit() and len(mobile) == 10):
            print("Invalid mobile number. Must be 10 digits.")
            return None

        ticket_id = self.next_ticket_id
        seat_no = 41 - self.available_seats[route]  # Seat assignment starts at 1
        self.tickets[ticket_id] = {
            "Name": name,
            "Age": age,
            "Mobile": mobile,
            "Route": route,
            "Price": self.routes[route],
            "Seat No": seat_no
        }
        self.available_seats[route] -= 1
        self.next_ticket_id += 1

        print(f"Ticket booked successfully! Ticket ID = {ticket_id}, Seat No = {seat_no}")
        return ticket_id

    #  View Ticket
    def view_ticket(self, ticket_id):
        ticket = self.tickets.get(ticket_id)
        if ticket:
            print(f"\n--- Ticket Details (ID: {ticket_id}) ---")
            for key, value in ticket.items():
                print(f"{key}: {value}")
        else:
            print("Ticket not found!")

    #  Cancel Ticket
    def cancel_ticket(self, ticket_id):
        ticket = self.tickets.get(ticket_id)
        if ticket:
            route = ticket["Route"]
            self.available_seats[route] += 1
            del self.tickets[ticket_id]
            print(f"Ticket {ticket_id} cancelled successfully.")
        else:
            print("Ticket not found!")

    #  Exit
    def exit_system(self):
        print("Exiting Bus Reservation System. Goodbye!")
        # If you want to exit the program, uncomment next line:
        # exit()


if __name__ == "__main__":
    brs = BusReservation()

    while True:
        print("\n--- Bus Reservation System ---")
        print("1. Show Available Routes")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        raw = input("Enter your choice (1-5): ").strip()
        try:
            choice = int(raw)
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            brs.show_routes()

        elif choice == 2:
            name = input("Enter Passenger Name: ").strip()
            try:
                age = int(input("Enter Age: ").strip())
            except ValueError:
                print("Invalid age. Must be a number.")
                continue

            mobile = input("Enter Mobile Number: ").strip()
            brs.show_routes()
            route_input = input("Enter route number OR exact route name: ").strip()
            # try to use a numeric route selection first
            try:
                route_choice = int(route_input)
            except ValueError:
                route_choice = route_input  # pass string, book_ticket will resolve
            brs.book_ticket(name, age, mobile, route_choice)

        elif choice == 3:
            try:
                ticket_id = int(input("Enter Ticket ID: ").strip())
            except ValueError:
                print("Ticket ID must be a number.")
                continue
            brs.view_ticket(ticket_id)

        elif choice == 4:
            try:
                ticket_id = int(input("Enter Ticket ID to cancel: ").strip())
            except ValueError:
                print("Ticket ID must be a number.")
                continue
            brs.cancel_ticket(ticket_id)

        elif choice == 5:
            brs.exit_system()
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
