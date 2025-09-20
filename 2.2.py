def ex2(a, b):
    
    funny_tickets = []

    for ticket_number in range(a, b + 1):
        digits = [int(d) for d in str(ticket_number)]
        even_count = sum(1 for d in digits if d % 2 == 0)
        od_count = len(digits) - even_count

        if even_count == od_count:
            funny_tickets.append(ticket_number)

    return funny_tickets

print(ex2(1,1000))