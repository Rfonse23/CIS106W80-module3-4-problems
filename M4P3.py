last_name = input("Enter last name: ")
midterm = float(input("Enter midterm score: "))
final = float(input("Enter final exam score: "))

total = (midterm * 0.40) + (final * 0.60)

print(f"{last_name} total exam points: {total:.2f}")