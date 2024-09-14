# Ex 07 - TicketPrices.py


def get_ticket_price_metod(age):
    if age < 4:
        return 0
    elif 4 <= age <= 18:
        return 25
    elif 19 <= age <= 65:
        return 40
    else:
        return 20


ages = [2, 5, 17, 20, 70]
for age in ages:
    price = get_ticket_price_metod(age)
    print(f"Age: {age}, Ticket Price: ${price}")
