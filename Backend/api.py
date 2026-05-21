from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Dict

from code_parser import CodeParser
from carbon_estimator import CarbonEstimator

app = FastAPI(title="Green Code A.I API")


# ----------------------------
# ✅ CORS CONFIG (CRITICAL)
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ----------------------------
# ✅ REQUEST SCHEMA
# ----------------------------
class PredictionRequest(BaseModel):
    code: str = Field(..., min_length=1)
    language: str
    memory_mb: float = Field(..., gt=0)
    variables: Dict[str, float] = {}


# ----------------------------
# ✅ ROOT ENDPOINT
# ----------------------------
@app.get("/")
def root():
    return {"status": "Green Code API running"}


# ----------------------------
# ✅ PREDICTION ENDPOINT
# ----------------------------
@app.post("/predict")
def predict_carbon(request: PredictionRequest):
    try:
        # ----------------------------
        # 1. VALIDATION
        # ----------------------------
        if request.language not in ["Python", "C", "C++", "Java"]:
            raise HTTPException(status_code=400, detail="Unsupported language")

        # ----------------------------
        # 2. DEFAULT VARIABLES
        # ----------------------------
        variables = request.variables or {"n": 5}

        # ----------------------------
        # 3. FEATURE EXTRACTION
        # ----------------------------
        parser = CodeParser(
            language=request.language,
            memory_mb=request.memory_mb,
            variables=variables
        )

        features = parser.parse(request.code)

        # ----------------------------
        # 4. ESTIMATION
        # ----------------------------
        estimator = CarbonEstimator(
            complexity=features["Complexity_Score"],
            nesting=features["Nesting_Depth"],
            memory=features["Memory_MB"],
            language=features["Language"]
        )

        result = estimator.run()

        # ----------------------------
        # 5. RESPONSE
        # ----------------------------
        return {
            "energy_joules": float(result["energy_joules"]),
            "carbon_kg": float(result["carbon_kg"]),
            "complexity_score": int(features["Complexity_Score"]),
            "nesting_depth": int(features["Nesting_Depth"]),
            "approximation": True
        }

    except HTTPException:
        raise  # rethrow proper API errors

    except Exception as e:
        # Unexpected errors
        raise HTTPException(status_code=500, detail=str(e))