import re

#. Validate a strong password
def validate_password(password):
    # Lookahead assertions:
    # (?=.*[A-Z]) → at least one uppercase
    # (?=.*[a-z]) → at least one lowercase
    # (?=.*\d)    → at least one digit
    # (?=.*[@$!%*?&]) → at least one special character
    # .{8,} → minimum 8 characters
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

    if re.match(pattern, password):
        print("Password is STRONG")
    else:
        print("Password is WEAK")
        print("Rules:")
        print("- Minimum 8 characters")
        print("- At least one uppercase letter")
        print("- At least one lowercase letter")
        print("- At least one digit")
        print("- At least one special character (@$!%*?&)")

# Test password
pwd = input("Enter your password: ")
validate_password(pwd)


# 3. Demonstrate regex modifiers
def demonstrate_modifiers():
    print("\n--- Regex Modifiers Demonstration ---")

    # re.IGNORECASE example
    text1 = "Learning Python is fun"
    pattern1 = "python"
    match1 = re.search(pattern1, text1, re.IGNORECASE)
    if match1:
        print("\nIGNORECASE Example:")
        print("Matched:", match1.group())

    # re.MULTILINE example
    text2 = "JavaScript\nPython\nC#\nGoLang"
    pattern2 = "^Python"
    match2 = re.search(pattern2, text2, re.MULTILINE)
    if match2:
        print("\nMULTILINE Example:")
        print("Matched:", match2.group())

    # re.DOTALL → dot (.) matches newline characters as well
    text3 = "First line of text\nSecond line of text"
    pattern3 = "First.*Second"
    match3 = re.search(pattern3, text3, re.DOTALL)
    if match3:
        print("\nDOTALL Example:")
        print("Matched:", match3.group())

demonstrate_modifiers()
