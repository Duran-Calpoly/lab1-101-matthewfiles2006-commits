def check_multiple(number):
    if(number%3==0 and number%5==0):
        return True
    else:
        return False  
def check_password(input_string):
    if(input_string=="ysfrgbsrgjhbrsjygi3rgwi7g4w8g4wgfeiu9g"):
        return "access granted"     
    else:
        return "access denied"     

def calculate_federal_tax(salary):
    if(salary <= 11000):
        return salary*.10
    elif( 11000 <= salary <= 44725):
        return salary*.12
    elif( 44725 <= salary <= 95375):
        return salary*.22
    else:
        return salary*.24 