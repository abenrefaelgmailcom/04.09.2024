# Get user's first name
fname: str = input("what's your first name?");

# Get user's last name
lname: str = input("what's your last name?");

# Get user's year of height
height: float = float(input("what's your height?"));

# Get user's year of birth
year_of_birth: int = int(input("what's your year of birth?"));


# Print user information
print(f"Your name is ", fname, lname, "your year of birth is:", year_of_birth, "your height is:", height);

# Print user information using formatted string
print(f"Your name is {fname} {lname} your year of birth is: {year_of_birth}, ""your height is:", {height});



# קלוט פרטי 3 משתמשים והצג אותם זה מתחת לזה, שהכול יופיע מיושר כמו בטבלה,
# רמז: השתמש ב ("..."f(print עם הסימן "<" וכו' )כפי שעשינו בשיעור(
name1: str = "adam";
age1: int = 34;
name2: str = "ronen";
age2: int = 35;
name3: str = "vlad";
age3: int = 32;

# Print names and ages with different alignments
print(f"Name: {name1} {age1} {age3}")
print(f"Name: {name2} {age2} {age3}")
print(f"Name: {name1:<11} {age1:>4}")
print(f"Name: {name1:<11} {age1:^5}")
print(f"Name: {name2:<11} {age2}")

# Define and print a percentage
prc: float = 0.5;
print(f"percentage: {prc:%}");
