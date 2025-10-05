def safe_divide(numerator, denominator):
    numerator = float(numerator)
    denominator = float(denominator)
    try:
        result = numerator / denominator
        return f'The result is {result}' 

    except ZeroDivisionError:
        return 'Denominator cannot be zero.'
        
    except ValueError:
        return 'Enter a numeric value.'


    
