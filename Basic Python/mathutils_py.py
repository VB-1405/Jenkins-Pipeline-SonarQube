class MathUtils:
    def add(self, a, b):
        """Returns the sum of a and b."""
        return a + b
    
    def subtract(self, a, b):
        """Returns the difference of a and b."""
        return a - b
    
    def multiply(self, a, b):
        """Returns the product of a and b."""
        return a * b
    
    def divide(self, a, b):
        """Returns the quotient of a and b. Returns -1.0 if b is zero."""
        if b == 0:
            return -1.0
        return a / b