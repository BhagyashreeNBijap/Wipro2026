import requests
import pytest

BASE_URL = "http://localhost:5000/api/patients"


def test_add_patient():
    payload = {
        "name": "Ravi",
        "age": 30,
        "gender": "Male",
        "disease": "Fever",
        "doctor": "Dr. Sharma"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201


def test_get_all_patients():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize("patient", [
    {"name": "Asha", "age": 25, "gender": "Female"},
    {"name": "Rahul", "age": 40, "gender": "Male"}
])
def test_add_multiple_patients(patient):
    response = requests.post(BASE_URL, json=patient)
    assert response.status_code == 201


def test_invalid_patient():
    response = requests.post(BASE_URL, json={"name": ""})
    assert response.status_code == 400


@pytest.mark.skip(reason="Under development")
def test_skip_example():
    pass


@pytest.mark.xfail
def test_expected_failure():
    assert 1 == 2
