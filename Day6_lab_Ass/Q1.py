import re

# 1. Uses re.match() to check whether a string starts with a valid employee ID (EMP + 3 digits)
emp_id = "EMP123"
if re.match(r"[A-Z]{3}\d{3}", emp_id):
    print("Valid employee ID and the ID is:", emp_id)
else:
    print("Invalid employee ID and the ID is:", emp_id)


# 2. Uses re.search() to find the first occurrence of a valid email address
text = "For any queries, reach out to bhagya@gmail.com"
search_result = re.search(r"\w+@\w+\.\w+", text)
if search_result:
    print("Email Found:", search_result.group())
else:
    print("No email found")


# 3. Demonstrates meta-characters (., *, +, ?) and special sequences (\d, \w, \s)
sample_text = "Python programming is powerful"

# . → any single character
dot_match = re.search(r"P.t", sample_text)
if dot_match:
    print("Dot (.) match:", dot_match.group())

# * → zero or more occurrences
star_match = re.search(r"Py.*g", sample_text)
if star_match:
    print("Star (*) match:", star_match.group())

# + → one or more occurrences
plus_match = re.search(r"o+", sample_text)
if plus_match:
    print("Plus (+) match:", plus_match.group())

# ? → zero or one occurrence
question_match = re.search(r"program+ing", sample_text)  # + → one or more 'm'
if question_match:
    print("Question (?) match:", question_match.group())


# 4. Prints matched groups using capturing parentheses
data = "Bhagya125 accessed the system at 9:30 AM"

match = re.search(r"(\w+)(\d+)", data)
if match:
    print("Group 1 (Name):", match.group(1))
    print("Group 2 (Number):", match.group(2))



