katz_deli = []


def line(deli):
    if len(deli) == 0:
        return print("The line is currently empty.")
    else:
        list_order = ["The line is currently:"]
        for customer in deli:
            list_order.append(f" {deli.index(customer) + 1}. {customer}")
        
        return print("".join(list_order))


def take_a_number(deli, customer):
    deli.append(customer)
    return print(f"Welcome, {customer}." + f" You are number {len(deli)} in line." )


def now_serving(deli):
    if len(deli) == 0:
        return print("There is nobody waiting to be served!")
    return print(f"Currently serving {deli.pop(0)}.")
    

line(katz_deli)
take_a_number(katz_deli, "Brenda")
take_a_number(katz_deli, "Alvin")
take_a_number(katz_deli, "Chip")

line(katz_deli)

now_serving(katz_deli)
