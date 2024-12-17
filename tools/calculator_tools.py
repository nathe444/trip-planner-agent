from langchain.tools import tool

class CalculatorTools():
    @tool
    def calculate(operation):
        try:
            return eval(operation)
        except:
            return "Invalid syntax in mathematical expression"