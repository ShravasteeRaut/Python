medical_cause = input("Did you have a medical cause? (Y/N):").strip().upper()

if medical_cause == "Y":
    print("You are allowed")
else: 
    atten = int(input("Enter the attendance of the student: "))

    if atten >= 75:
        print("Allowed")
    else:
        print("Not allowed")
        