import numpy as np
import pandas as pd

np.random.seed(42)

# -----------------------------
# Languages
# -----------------------------
languages = ['C', 'C++', 'Java', 'Python']
samples_per_lang = 1000

# Relative energy coefficients
energy_multiplier = {
    'C': 1.0,
    'C++': 1.2,
    'Java': 10.0,
    'Python': 75.0
}

data = []

for lang in languages:
    for _ in range(samples_per_lang):

        complexity = np.random.randint(1, 101)
        nesting = np.random.randint(1, 6)
        memory = np.random.uniform(10, 500)

        # CPU workload model
        base_energy = (
            0.55 * complexity +
            7.5 * nesting +
            0.18 * memory
        )

        joules = base_energy * energy_multiplier[lang]

        # Ryzen-like Gaussian noise
        noise = np.random.normal(
            0,
            joules * 0.07
        )

        final_energy = max(0, joules + noise)

        data.append([
            lang,
            complexity,
            nesting,
            memory,
            final_energy
        ])

df = pd.DataFrame(data, columns=[
    'Language',
    'Complexity_Score',
    'Nesting_Depth',
    'Memory_MB',
    'Joules'
])

df.to_csv("carbon_dataset.csv", index=False)

print(df.head())
print("Dataset Shape:", df.shape)