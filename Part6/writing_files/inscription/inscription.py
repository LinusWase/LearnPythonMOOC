user_input = input("Whom should i sign this to: ")
file_name = input("Where shall i save it: ")

with open(file_name, "w") as file:
    file.write(f"Hi {user_input}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")