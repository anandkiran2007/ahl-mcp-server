from pydantic import BaseModel
from typing import List, Dict

class Condition(BaseModel):
    code: str
    description: str

class Medication(BaseModel):
    name: str
    dose: str

class NLPResult(BaseModel):
    problems: List[str]
    medications: List[str]
    tests: List[str]

class MCPBundle(BaseModel):
    patient_id: str
    conditions: List[Condition]
    medications: List[Medication]
    nlp: NLPResult
    model_metadata: Dict[str, str]
