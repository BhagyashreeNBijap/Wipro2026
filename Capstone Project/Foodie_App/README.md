# 🍽️ Foodie App – REST API with Automation Testing

A complete RESTful backend application built with **Python Flask**, featuring comprehensive automation testing using **Pytest** and **Robot Framework**.

This project demonstrates REST API best practices, input validation, layered architecture, and enterprise-grade automated testing.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Pytest](https://img.shields.io/badge/Pytest-7.0+-orange.svg)](https://pytest.org)
[![Robot Framework](https://img.shields.io/badge/Robot%20Framework-6.0+-red.svg)](https://robotframework.org)

---

## 📋 Table of Contents

- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Features](#-features-implemented)
- [API Endpoints](#-api-endpoints)
- [REST Principles](#-rest-principles-followed)
- [Installation](#-installation)
- [Running the Application](#-running-the-application)
- [Testing](#-testing)
- [Architecture](#-architecture-design)
- [Learning Outcomes](#-learning-outcomes)
- [Project Status](#-project-status)

---

## 🚀 Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend Framework** | Python Flask |
| **Manual Testing** | Postman |
| **Automation Testing** | Pytest, Robot Framework |
| **Libraries** | requests, jsonschema, RequestsLibrary |
| **Data Format** | JSON |
| **Architecture** | Layered (Routes → Services → Models) |

---

## 📁 Project Structure

```
Foodie_App/
│
├── app.py                 # Main Flask application entry point
├── config.py              # Application configuration
├── requirements.txt       # Python dependencies
│
├── models/                # Data models and storage
│   └── ...
│
├── services/              # Business logic layer
│   └── ...
│
├── routes/                # API route handlers
│   └── ...
│
├── utils/                 # Utility functions and helpers
│   └── ...
│
├── tests/                 # Test suites
│   ├── pytest/            # Pytest automation tests
│   │   └── ...
│   └── robot/             # Robot Framework tests
│       └── ...
│
└── README.md              # Project documentation
```

---

## 📌 Features Implemented

### 1️⃣ Restaurant Module
- ✅ Register Restaurant
- ✅ Update Restaurant Details
- ✅ Disable Restaurant
- ✅ View Restaurant Information

### 2️⃣ Dish Module
- ✅ Add New Dish
- ✅ Update Dish Details
- ✅ Enable/Disable Dish Availability
- ✅ Delete Dish

### 3️⃣ Admin Module
- ✅ Approve Restaurant Registrations
- ✅ Disable Restaurant Operations
- ✅ View Customer Feedback
- ✅ View All Orders

### 4️⃣ User Module
- ✅ User Registration
- ✅ Search Restaurants
- ✅ Place Orders
- ✅ Submit Ratings & Reviews

### 5️⃣ Order Module
- ✅ View Orders by Restaurant
- ✅ View Orders by User

**Total APIs Implemented: 18**

---

## 🔌 API Endpoints

### Restaurant APIs
```
POST   /api/restaurants              # Register new restaurant
PUT    /api/restaurants/{id}         # Update restaurant details
DELETE /api/restaurants/{id}         # Disable restaurant
GET    /api/restaurants/{id}         # Get restaurant details
```

### Dish APIs
```
POST   /api/dishes                   # Add new dish
PUT    /api/dishes/{id}              # Update dish
PATCH  /api/dishes/{id}/toggle       # Enable/Disable dish
DELETE /api/dishes/{id}              # Delete dish
```

### User APIs
```
POST   /api/users/register           # Register user
GET    /api/restaurants/search       # Search restaurants
POST   /api/orders                   # Place order
POST   /api/ratings                  # Submit rating
```

### Admin APIs
```
PUT    /api/admin/restaurants/{id}/approve   # Approve restaurant
DELETE /api/admin/restaurants/{id}           # Disable restaurant
GET    /api/admin/feedback                   # View feedback
GET    /api/admin/orders                     # View all orders
```

### Order APIs
```
GET    /api/orders/restaurant/{id}   # Orders by restaurant
GET    /api/orders/user/{id}         # Orders by user
```

---

## 🧠 REST Principles Followed

✅ **Resource-Based URIs** – Clean, meaningful endpoint paths  
✅ **HTTP Methods** – Proper use of GET, POST, PUT, PATCH, DELETE  
✅ **Stateless Communication** – Each request is independent  
✅ **JSON Format** – Standardized request/response structure  
✅ **HTTP Status Codes** – Appropriate codes (200, 201, 400, 404, 409, 500)  
✅ **Error Handling** – Consistent error response format  

---

## 🛠️ Input Validation

- ✅ Required fields validation
- ✅ Data type validation
- ✅ Conflict handling (duplicate entries)
- ✅ Invalid ID handling
- ✅ Bad request handling with descriptive messages

---

## 💻 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd Foodie_App
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Application

### Start the Flask Server

```bash
python app.py
```

The API will be available at: `http://localhost:5000`

### Verify Installation

```bash
curl http://localhost:5000/api/health
```

---

## 🧪 Testing

### Manual Testing with Postman

1. Import the Postman collection (if available)
2. Test individual endpoints
3. Verify request/response formats
4. Check status codes
5. Test positive and negative scenarios

### Automated Testing

#### Pytest Automation

**Features:**
- ✅ Uses `requests` library for HTTP calls
- ✅ Fixtures for test setup and teardown
- ✅ Parameterized tests for multiple scenarios
- ✅ Status code validation
- ✅ Response body validation
- ✅ JSON schema validation
- ✅ Integration flow testing

**Run Pytest:**

```bash
# Ensure Flask server is running in another terminal
python app.py

# Run all tests
pytest -v

# Run specific test file
pytest tests/pytest/test_restaurants.py -v

# Run with coverage report
pytest --cov=. --cov-report=html
```

**Sample Pytest Test:**
```python
def test_register_restaurant(client):
    response = client.post('/api/restaurants', json={
        'name': 'Test Restaurant',
        'cuisine': 'Italian',
        'location': 'Downtown'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Restaurant registered successfully'
```

---

#### Robot Framework Automation

**Features:**
- ✅ Uses RequestsLibrary
- ✅ Keyword-driven test framework
- ✅ Data-driven test cases
- ✅ Separate setup and teardown
- ✅ Integration flow testing
- ✅ HTML test reports with screenshots

**Run Robot Tests:**

```bash
# Ensure Flask server is running
python app.py

# Run all robot tests
robot tests/robot/

# Run specific test suite
robot tests/robot/restaurant_tests.robot

# Run with custom output directory
robot --outputdir results tests/robot/
```

**Generated Reports:**
- `report.html` – High-level test summary
- `log.html` – Detailed test execution log
- `output.xml` – Machine-readable results

**Sample Robot Test:**
```robot
*** Test Cases ***
Register New Restaurant
    [Documentation]    Test restaurant registration endpoint
    ${response}=    POST    ${BASE_URL}/api/restaurants
    ...    json={"name": "Test Restaurant", "cuisine": "Italian"}
    Should Be Equal As Integers    ${response.status_code}    201
    Should Contain    ${response.json()}[message]    successfully
```

---

## 🏗️ Architecture Design

The project follows a **layered architecture** pattern:

```
┌─────────────────────────────────────┐
│         Routes Layer                │  ← HTTP Request Handling
│  (API Endpoints & Request/Response) │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│        Service Layer                │  ← Business Logic
│   (Validation, Processing, Rules)   │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│         Models Layer                │  ← Data Management
│      (Data Storage & Retrieval)     │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│         Tests Layer                 │  ← Quality Assurance
│   (Pytest & Robot Framework Tests)  │
└─────────────────────────────────────┘
```

**Benefits:**
- Clear separation of concerns
- Easy to maintain and extend
- Testable components
- Reusable business logic

---

## 🎯 Learning Outcomes

Through this project, you will learn:

- ✅ REST API development with Flask
- ✅ RESTful design principles and best practices
- ✅ Input validation and error handling
- ✅ Layered architecture implementation
- ✅ Manual API testing with Postman
- ✅ Automated testing with Pytest
- ✅ Keyword-driven testing with Robot Framework
- ✅ Integration and end-to-end testing
- ✅ Test report generation and analysis
- ✅ Professional project structure and documentation

---

## 🏆 Project Status

| Component | Status |
|-----------|--------|
| Backend API | ✅ Complete |
| Manual Testing | ✅ Complete |
| Pytest Automation | ✅ Complete |
| Robot Framework Automation | ✅ Complete |
| Documentation | ✅ Complete |
| Code Review | 🟡 Ready for Review |

---

## 📝 API Response Format

### Success Response
```json
{
    "status": "success",
    "message": "Operation completed successfully",
    "data": { }
}
```

### Error Response
```json
{
    "status": "error",
    "message": "Error description",
    "error_code": "ERROR_CODE"
}
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is developed for educational purposes as part of REST API and Automation Testing practice.

---

## 👨‍💻 Author

Developed as part of REST API and Automation Testing practice project.

---

## 📞 Support

For questions or issues, please open an issue in the repository.

---

## 🙏 Acknowledgments

- Flask documentation
- Pytest documentation
- Robot Framework community
- REST API design best practices

---

**Happy Coding! 🚀*
