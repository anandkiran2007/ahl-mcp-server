
import requests
from app.core.config import FHIR_ENDPOINT

def get_patient_by_id(patient_id: str):
    url = f"{FHIR_ENDPOINT}/Patient/{patient_id}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def search_conditions(patient_id: str):
    url = f"{FHIR_ENDPOINT}/Condition?patient=Patient/{patient_id}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json().get("entry", [])

def search_medications(patient_id: str):
    url = f"{FHIR_ENDPOINT}/MedicationRequest?patient=Patient/{patient_id}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json().get("entry", [])

def search_observations(patient_id: str):
    url = f"{FHIR_ENDPOINT}/Observation?patient=Patient/{patient_id}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json().get("entry", [])
