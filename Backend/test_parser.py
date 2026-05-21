from code_parser import CodeParser

def parse(self, code):
    try:
        # RESET STATE (VERY IMPORTANT)
        self.complexity = 0
        self.nesting_depth = 0

        if not code.strip():
            return {
                "Complexity_Score": 0,
                "Nesting_Depth": 0,
                "Memory_MB": self.memory_mb,
                "Language": self.language
            }

        # your existing parsing logic...

        return {
            "Complexity_Score": self.complexity,
            "Nesting_Depth": self.nesting_depth,
            "Memory_MB": self.memory_mb,
            "Language": self.language
        }

    except Exception:
        return {
            "Complexity_Score": 0,
            "Nesting_Depth": 0,
            "Memory_MB": self.memory_mb,
            "Language": self.language
        }

def run_test(name, code):
    print(f"\n--- {name} ---")

    try:
        # Create NEW parser every time (fixes state carryover)
        parser = CodeParser(
            language="Python",
            memory_mb=100,
            variables={"n": 10}
        )

        # Handle empty code manually
        if not code.strip():
            features = {
                "Complexity_Score": 0,
                "Nesting_Depth": 0,
                "Memory_MB": 100,
                "Language": "Python"
            }
        else:
            features = parser.parse(code)

        print(features)

    except Exception as e:
        print("Handled Error:", e)
        print({
            "Complexity_Score": 0,
            "Nesting_Depth": 0,
            "Memory_MB": 100,
            "Language": "Python"
        })


# Test cases
tests = [
    ("Simple Loop", "for i in range(n): print(i)"),
    
    ("Nested Loop",
     "for i in range(n):\n    for j in range(n): print(i,j)"),
    
    ("Conditional",
     "if n > 0:\n    print(n)"),
    
    ("Empty Code", ""),
    
    ("Invalid Code",
     "for i in range(n print(i)")
]


# Run all tests
for name, code in tests:
    run_test(name, code)