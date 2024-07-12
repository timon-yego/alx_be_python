def safe_divide(numerator, denominator):
        try:
            num = float(numerator)
            denom = float(denominator)

            if denom == 0:
                return "Error: Division by zero is not allowed."
            
            return num / denom
        except ValueError:
            return "Error: Non-numeric input. Please enter valid numbers"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."