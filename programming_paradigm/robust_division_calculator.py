def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        result = numerator / denominator
        return f'The result of the division is {result}' 

    except ZeroDivisionError:
        return 'Cannot divide by zero.'
        
    except ValueError:
        return 'Please enter numeric values only.'


    
