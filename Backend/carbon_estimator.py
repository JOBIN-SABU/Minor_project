import pickle
import pandas as pd
import os


class CarbonEstimator:

    def __init__(self, complexity, nesting, memory, language):
        self.complexity = complexity
        self.nesting = nesting
        self.memory = memory
        self.language = language

        # Load trained model
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(BASE_DIR, "energy_model.pkl")

        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    # -------------------------
    # Complexity Score
    # -------------------------
    def compute_complexity_score(self):
        return (
            0.5 * self.complexity
            + 2.0 * self.nesting
            + 0.1 * self.memory
        )

    # -------------------------
    # Prepare ML Features
    # -------------------------
    def prepare_features(self):

        language_map = {
            "C": 0,
            "C++": 1,
            "Java": 2,
            "Python": 3
        }

        data = {
            "Language_Encoded": language_map[self.language],
            "Complexity_Score": self.complexity,
            "Nesting_Depth": self.nesting,
            "Memory_MB": self.memory
        }

        return pd.DataFrame([data])

    # -------------------------
    # Predict Energy
    # -------------------------
    def predict_energy(self):
        features = self.prepare_features()
        energy = self.model.predict(features)[0]
        return energy

    # -------------------------
    # Convert Energy → Carbon
    # -------------------------
    def energy_to_carbon(self, energy):
        return (energy / 3.6e6) * 0.4

    # -------------------------
    # Full Pipeline
    # -------------------------
    def run(self):
        energy = self.predict_energy()
        carbon = self.energy_to_carbon(energy)

        return {
            "energy_joules": float(energy),
            "carbon_kg": float(carbon)
        }