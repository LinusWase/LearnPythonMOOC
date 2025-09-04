limit = int(input("Limit: "))
numbers = 1
summary = 1
summary_text = "1"

while summary < limit:
    numbers += 1
    summary += numbers
    summary_text += " + " + str(numbers)

print(f"The consecutive sum: {summary_text} = {summary}")
