import json
from pathlib import Path

file_path = Path(__file__).with_name("tickets.json")

# Load saved tickets.
if file_path.exists():
    with open(file_path, "r") as file:
        tickets = json.load(file)
else:
    tickets = []

while True:
    print("\n--- PC Repair Tracker ---")
    print("1. Add a ticket")
    print("2. View all tickets")
    print("3. Update ticket status")
    print("4. Search tickets")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        device = input("What device needs repair? ").strip()
        problem = input("What is wrong with it? ").strip()

        if not device or not problem:
            print("Device and problem cannot be empty.")
            continue

        ticket = {
            "device": device,
            "problem": problem,
            "status": "Pending"
        }

        tickets.append(ticket)

        with open(file_path, "w") as file:
            json.dump(tickets, file, indent=4)

        print("Ticket saved!")

    elif choice == "2":
        if not tickets:
            print("No tickets yet.")
        else:
            for number, ticket in enumerate(tickets, start=1):
                print(f"\nTicket #{number}")
                print("Device:", ticket["device"])
                print("Problem:", ticket["problem"])
                print("Status:", ticket["status"])

    elif choice == "3":
        if not tickets:
            print("No tickets to update.")
            continue

        for number, ticket in enumerate(tickets, start=1):
            print(f"{number}. {ticket['device']} - {ticket['status']}")

        ticket_number = input("Enter the ticket number: ").strip()

        if not ticket_number.isdecimal():
            print("Please enter a number.")
            continue

        index = int(ticket_number) - 1

        if index < 0 or index >= len(tickets):
            print("That ticket does not exist.")
            continue

        print("\nChoose the new status:")
        print("1. Pending")
        print("2. In Progress")
        print("3. Completed")

        status_choice = input("Choose a status: ").strip()

        statuses = {
            "1": "Pending",
            "2": "In Progress",
            "3": "Completed"
        }

        if status_choice not in statuses:
            print("Please choose 1, 2, or 3.")
            continue

        tickets[index]["status"] = statuses[status_choice]

        with open(file_path, "w") as file:
            json.dump(tickets, file, indent=4)

        print("Status updated and saved!")

    elif choice == "4":
        search = input("Search by device or problem: ").strip().lower()

        if not search:
            print("Please enter something to search for.")
            continue

        found = False

        for number, ticket in enumerate(tickets, start=1):
            if (
                search in ticket["device"].lower()
                or search in ticket["problem"].lower()
            ):
                print(f"\nTicket #{number}")
                print("Device:", ticket["device"])
                print("Problem:", ticket["problem"])
                print("Status:", ticket["status"])
                found = True

        if not found:
            print("No matching tickets found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Please enter 1, 2, 3, 4, or 5.")