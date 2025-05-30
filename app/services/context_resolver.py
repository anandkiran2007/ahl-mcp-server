from app.models.context_bundle import MCPBundle, Condition, Medication, NLPResult

def build_context_bundle(patient_id: str) -> MCPBundle:
    # Mock data for testing
    return MCPBundle(
        patient_id=patient_id,
        conditions=[Condition(code="I10", description="Hypertension")],
        medications=[Medication(name="Lisinopril", dose="10mg")],
        nlp=NLPResult(
            problems=["Hypertension"],
            medications=["Lisinopril"],
            tests=["Blood Pressure"]
        ),
        model_metadata={"model_id": "summarizer-v1", "invoked_at": "2025-05-30T18:00Z"}
    )
