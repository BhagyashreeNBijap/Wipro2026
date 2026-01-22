'''#Question 1 – Web Interaction & REST API Consumption
Topics Covered: Working with Web & APIs, Automation/Web interaction, requests library, Basics of REST API
Write a Python program that:
1. Uses the requests library to send a GET request to a public REST API (e.g., users or posts API)
2. Sends custom headers with the request
3. Parses the JSON response and extracts specific fields
4. Serializes the extracted data and saves it into a JSON file
5. Handles HTTP errors using proper exception handling give correct one'''


import requests
import json

def fetch_users_data():
    url = "https://jsonplaceholder.typicode.com/users"

    # Custom headers
    headers = {
        "User-Agent": "Python-Requests",
        "Accept": "application/json"
    }

    try:
        # Sending GET request
        response = requests.get(url, headers=headers, timeout=10)

        # Raise error for bad status codes (4xx, 5xx)
        response.raise_for_status()

        # Parse JSON response
        users = response.json()

        # Extract specific fields
        extracted_data = []
        for user in users:
            extracted_data.append({
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"]
            })

        # Save extracted data to JSON file
        with open("users_data.json", "w") as file:
            json.dump(extracted_data, file, indent=4)

        print("Data fetched successfully and saved to users_data.json")

    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred:", http_err)

    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")

    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")

    except requests.exceptions.RequestException as err:
        print("An error occurred:", err)


if __name__ == "__main__":
    fetch_users_data()
