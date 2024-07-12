def safe_divide(numerator, denominator):
        try:
            num = float(numerator)
            denom = float(denominator)

            if denom == 0:
                return "Error: Cannot divide by zero."
            
            return num / denom
        except ValueError:
            return "Error: Non-numeric input. Please enter valid numbers"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."