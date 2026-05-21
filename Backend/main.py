from code_parser import CodeParser
from carbon_estimator import CarbonEstimator


code = """
for i in range(n):
    for j in range(m):
        if j > 2:
            pass
"""

# STEP 1: Parse Code
parser = CodeParser(
    language="Python",
    memory_mb=120,
    variables={"n": 10, "m": 5}
)

features = parser.parse(code)

print("Extracted Features:")
print(features)


# STEP 2: Estimate Carbon
estimator = CarbonEstimator(
    complexity=features["Complexity_Score"],
    nesting=features["Nesting_Depth"],
    memory=features["Memory_MB"],
    language=features["Language"]
)

result = estimator.run()

print("\nFinal Output:")
print(result)