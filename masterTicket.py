SERVICE_CHARGE = 2

TICKET_PRICE = 10

ticket_remaining = 100

def ticket_calculate(ticket_proceed):
    return (ticket_proceed * TICKET_PRICE) + SERVICE_CHARGE

while ticket_remaining >= 1:

    print("We are {} tickets remaining.".format(ticket_remaining))
    user_name = input("What is your name?  ")

    ticket_proceed = input("Hello, {}. How many tickets would you like?  ".format(user_name))

    try:
        ticket_proceed = int(ticket_proceed)
        if ticket_proceed > ticket_remaining:
            raise ValueError("Sorry, We are only {} tickets remaining.".format(ticket_remaining))
        if ticket_proceed < 1:
            raise ValueError("the smallest amount of ticket for purchasing is 1 ticket at least.")

    except ValueError as err:
        print("Oh no! that's an invalid value. Please try again.")
        print("({})".format(err))

    else:
        total_due = ticket_calculate(ticket_proceed)
        print("Total due of the {} ticket(s) is ${}. (service charge is included)".format(ticket_proceed,total_due))

        agreement = input("Would you like to purchase? (Y/N)  ")
        
        if agreement.lower() == "y":
            print("SOLD! Thank you for your purchasing.")
            ticket_remaining -= ticket_proceed
        else:
            print("Thank you anyways, {}!".format(user_name))

print("Sorry. All tickets are sold out!")