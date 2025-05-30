
from fastapi import APIRouter, HTTPException
from typing import Dict, List
from uuid import uuid4

router = APIRouter(prefix="/ahl", tags=["HealthLake Mock APIs"])

# Mock datastore
mock_patients: Dict[str, Dict] = {}
mock_conditions: Dict[str, List[Dict]] = {}
mock_medications: Dict[str, List[Dict]] = {}
mock_observations: Dict[str, List[Dict]] = {}

@router.post("/Patient")
def create_patient(patient: Dict):
    patient_id = str(uuid4())
    mock_patients[patient_id] = patient
    return {"id": patient_id, **patient}

@router.get("/Patient/{patient_id}")
def get_patient(patient_id: str):
    if patient_id not in mock_patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"id": patient_id, **mock_patients[patient_id]}

@router.put("/Patient/{patient_id}")
def update_patient(patient_id: str, patient: Dict):
    mock_patients[patient_id] = patient
    return {"id": patient_id, **patient}

@router.delete("/Patient/{patient_id}")
def delete_patient(patient_id: str):
    if patient_id in mock_patients:
        del mock_patients[patient_id]
    return {"message": "Patient deleted"}

@router.get("/Condition")
def get_conditions(patient: str):
    return mock_conditions.get(patient, [])

@router.get("/MedicationRequest")
def get_medications(patient: str):
    return mock_medications.get(patient, [])

@router.get("/Observation")
def get_observations(patient: str):
    return mock_observations.get(patient, [])

@router.post("/mock/add_condition/{patient_id}")
def add_condition(patient_id: str, condition: Dict):
    mock_conditions.setdefault(patient_id, []).append(condition)
    return {"message": "Condition added"}

@router.post("/mock/add_medication/{patient_id}")
def add_medication(patient_id: str, medication: Dict):
    mock_medications.setdefault(patient_id, []).append(medication)
    return {"message": "Medication added"}

@router.post("/mock/add_observation/{patient_id}")
def add_observation(patient_id: str, observation: Dict):
    mock_observations.setdefault(patient_id, []).append(observation)
    return {"message": "Observation added"}
