import re
from expression_evaluator import SafeEvaluator


class LoopParser:
    def __init__(self, variables=None):
        self.evaluator = SafeEvaluator(variables)

    def parse_python_loop(self, line: str):
        """
        Example:
        for i in range(n*m+2):
        """
        match = re.search(r'range\((.*?)\)', line)

        if not match:
            return None

        expr = match.group(1)
        return self.evaluator.evaluate(expr)

    def parse_brace_loop(self, line: str):
        """
        Example:
        for(int i=0; i<n+m; i++)
        """
        match = re.search(r'for\s*\((.*?);(.*?);(.*?)\)', line)

        if not match:
            return None

        condition = match.group(2).strip()

        # Extract right side of condition like i < n+m
        cond_match = re.search(r'[<>]=?\s*(.*)', condition)

        if not cond_match:
            return None

        expr = cond_match.group(1)
        return self.evaluator.evaluate(expr)