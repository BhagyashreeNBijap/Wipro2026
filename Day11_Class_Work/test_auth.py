def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Invalid Credentials"

def test_valid_login():
    assert login("admin", "admin123") == "Login Successful"

def test_invalid_login():
    assert login("user", "wrong") == "Invalid Credentials"
