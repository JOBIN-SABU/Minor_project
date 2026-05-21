import ast
import operator


class SafeEvaluator:
    OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
    }

    def __init__(self, variables=None, default_value=5):
        self.variables = variables or {}
        self.default_value = default_value

    def evaluate(self, expression: str):
        tree = ast.parse(expression, mode='eval')
        return self._eval_node(tree.body)

    def _eval_node(self, node):
        if isinstance(node, ast.Constant):  # numbers
            return node.value

        elif isinstance(node, ast.Name):  # variables
            return self.variables.get(node.id, self.default_value)

        elif isinstance(node, ast.BinOp):  # binary operations
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op_type = type(node.op)

            if op_type in self.OPS:
                return self.OPS[op_type](left, right)

            raise ValueError(f"Unsupported operator: {op_type}")

        else:
            raise ValueError(f"Unsupported expression: {type(node)}")