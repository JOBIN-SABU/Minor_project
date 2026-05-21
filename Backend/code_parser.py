import re

from loop_parser import LoopParser
from nesting_tracker import NestingTracker


class CodeParser:
    def __init__(self, language, memory_mb, variables=None):
        self.language = language
        self.memory_mb = memory_mb
        self.variables = variables or {}

        self.loop_parser = LoopParser(self.variables)
        self.tracker = NestingTracker()

        self.conditionals = 0
        self.functions = 0
        self.classes = 0

    def parse(self, code: str):
        try:
            # -------------------------
            # 🔴 RESET STATE (CRITICAL FIX)
            # -------------------------
            self.tracker = NestingTracker()
            self.loop_parser = LoopParser(self.variables)

            self.conditionals = 0
            self.functions = 0
            self.classes = 0

            # -------------------------
            # HANDLE EMPTY CODE
            # -------------------------
            if not code.strip():
                return {
                    "Complexity_Score": 0,
                    "Nesting_Depth": 0,
                    "Memory_MB": self.memory_mb,
                    "Language": self.language
                }

            lines = code.splitlines()
            indent_stack = []

            for line in lines:
                stripped = line.strip()

                if not stripped:
                    continue

                # -------------------------
                # PYTHON PARSING
                # -------------------------
                if self.language.lower() == "python":
                    indent = len(line) - len(line.lstrip())

                    while indent_stack and indent < indent_stack[-1]:
                        indent_stack.pop()
                        self.tracker.exit_loop()

                    if stripped.startswith("for ") and "range(" in stripped:
                        iterations = self.loop_parser.parse_python_loop(stripped)
                        self.tracker.enter_loop(iterations)
                        indent_stack.append(indent)

                    elif stripped.startswith("if "):
                        self.conditionals += 1

                    elif stripped.startswith("def "):
                        self.functions += 1

                    elif stripped.startswith("class "):
                        self.classes += 1

                # -------------------------
                # C / C++ / JAVA PARSING
                # -------------------------
                else:
                    if "for" in stripped and "(" in stripped:
                        iterations = self.loop_parser.parse_brace_loop(stripped)
                        self.tracker.enter_loop(iterations)

                    if "}" in stripped:
                        self.tracker.exit_loop()

                    if re.match(r'if\s*\(', stripped):
                        self.conditionals += 1

                    if re.match(r'class\s+', stripped):
                        self.classes += 1

                    if re.match(r'.*\(.*\)\s*\{', stripped) and "for" not in stripped and "if" not in stripped:
                        self.functions += 1

            loop_results = self.tracker.get_results()

            complexity_score = (
                loop_results["loop_cost"]
                + self.conditionals * 2
                + self.functions * 5
                + self.classes * 10
                + loop_results["max_depth"] ** 2
            )

            return {
                "Complexity_Score": complexity_score,
                "Nesting_Depth": loop_results["max_depth"],
                "Memory_MB": self.memory_mb,
                "Language": self.language
            }

        except Exception:
            # -------------------------
            # SAFE FALLBACK (NO CRASH)
            # -------------------------
            return {
                "Complexity_Score": 0,
                "Nesting_Depth": 0,
                "Memory_MB": self.memory_mb,
                "Language": self.language
            }