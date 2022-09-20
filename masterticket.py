TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ") 
    number_of_tickets = input("How many tickets would you like, {}?  ".format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please try again.".format(err))
        
    else:
        order_total = calculate_price(number_of_tickets)
        print("Your total price will be {}.".format(order_total))
        proceed_purchase = input("Would you like to proceed with purchase [Y/N]?  ")
        if proceed_purchase.upper() == 'Y': 
            #TODO: Gather credit card information and process it
            print("SOLD!")
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you anyways, {}".format(name))
print("Sorry, we are all out of tickets!  ")
