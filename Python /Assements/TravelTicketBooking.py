
class BusReservation:
  
  def __init__(self):

    self.routes={
       "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 700,
            "Ahmedabad to Surat": 400

    }

    self.tickets={}
    self.next_ticket_id=1
    self.available_seats={route:40 for route in self.routes}

def show_routes(self):
    print("\n--available rotes--")
    for route,price in self.routes.items():
        seats=self.available_seats[route]
        print(f"{route}- ₹{price} |Seats Left:{seats} ")

if __name__ == "__main__":
 brs=BusReservation()

 while True:
    print("--Bus reservation system\n")
    print("1. Show Available routes")
    print("2. Book Tickets")
    print("3. View Tickets")
    print("4. Cancel Tickets")
    print("5. Exit")

    choice=input("Enter your choice")

    if choice== "1":
      brs.show_routes()

    elif choice== "2":
      name=input("Enter name")
      age=int(input("Enter ur age"))
      mobile=input("entr mobile number:")
      brs.show_routes()
      route=input("Enter route exactly as above")

      brs.book_tickets(name,age,mobile,route)

    elif choice=="3":
      ticket_id= int(input("Enter your ticket id"))
      brs.view_ticket(ticket_id)

    elif choice=="4":
      ticket_id= int(input("Enter your ticket id"))
      brs.cancel_ticket(ticket_id)

    elif choice=="5":
      brs.exit_system()

    else:
      print("Invalid choice enter valid choice")
      