
# 🏥 MCP Server for AWS HealthLake (Mocked)

This project is an **open-source Model Context Protocol (MCP) server** that connects to (mocked) AWS HealthLake data sources and provides structured, standardized context bundles for clinical models.

## ✅ Features

- Mocked AWS HealthLake APIs (FHIR-based)
- Context bundling per MCP spec (FHIR + NLP)
- Model registration and tailored context delivery
- Mocked model invocation endpoint
- Audit logging
- Optional `USE_AWS` flag for future AWS integration

---

## 🚀 Quick Start

### 1. Clone or Download

```bash
unzip mcp-server.zip
cd mcp-server
```

### 2. Install Python Dependencies

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Locally (Mock Mode)

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔁 Endpoints

### 📦 MCP Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/context/{patient_id}` | GET | Get context bundle |
| `/models/register` | POST | Register model info |
| `/models/{model_id}/context/{patient_id}` | GET | Tailored context |
| `/model/invoke/{model_id}?patient_id=...` | POST | Mock model prediction |

### 🧪 Mock HealthLake Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/ahl/Patient` | POST | Create patient |
| `/ahl/Patient/{id}` | GET | Get patient |
| `/ahl/Condition?patient=...` | GET | Get conditions |
| `/ahl/MedicationRequest?patient=...` | GET | Get meds |
| `/ahl/Observation?patient=...` | GET | Get labs |
| `/ahl/mock/add_*` | POST | Add mock data (condition/med/obs) |

---

## ⚙️ Switching Between Mock and AWS Mode

By default, the app runs in **mock mode**.

To prepare for future AWS integration:

```bash
export USE_AWS=true
```

Note: AWS mode is not implemented yet but ready for integration.

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 📂 Folder Structure

```
app/
├── api/                # API endpoints
├── core/               # Config and logging
├── fhir/               # Placeholder for FHIR connector
├── models/             # Pydantic models
├── nlp/                # NLP mock enhancer
├── services/           # Context resolver, policy logic
├── main.py             # FastAPI entry
infra/
tests/                  # Test cases
schemas/                # MCP JSON schema
.env
requirements.txt
```

---

## 📜 License

MIT License

---

## 🧠 Coming Soon

- AWS HealthLake integration (`boto3`)
- Amazon Comprehend Medical / Bedrock models
- Dockerfile + ECS deployment
- Real-time cohort search
- SMART-on-FHIR authentication

