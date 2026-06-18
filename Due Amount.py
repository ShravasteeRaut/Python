def due_amount(bill, paid):
    due = bill - paid

    if due > 0:
        print("Customer still needs to pay:", due)
    else:
        print("Bill paid successfully!")

bill = int(input("Enter bill amount: "))
paid = int(input("Enter amount paid: "))

due_amount(bill, paid)

   













