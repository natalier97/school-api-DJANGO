from django.core.exceptions import ValidationError
import re




def validate_combination_format(locker_combination):
# validate_combination_format: Only accepts string in the following format "12-12-12" (Ensures there are numbers only)
    regex =  r"^[-0-9]+$"
# Validation Error: 'Combination must be in the format "12-12-12"'
    error_message = 'Combination must be in the format "12-12-12"'

    good_combo = re.match(regex, locker_combination)
    
    if good_combo:
        return locker_combination
    else:
        raise ValidationError(error_message, params={'locker_combination': locker_combination})


def validate_name_format(name):
    # validate_name_format: Only accepts string in the following format "First M. Last"
    regex = r"^([A-Z][a-z]*)\s+[A-Z]\. [A-Z][a-z]*$" 

    # Validation Error: 'Name must be in the format "First Middle Initial. Last"'
    error_message = 'Name must be in the format "First Middle Initial. Last"'

    good_name = re.match(regex, name) #returns T/F
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={'name' : name})
    

def validate_school_email(school_email):
    # validate_school_email: Only accepts string ending with "@school.com"
    regex =  r'^.*@school\.com$'

    # Validation Error: 'Invalid school email format. Please use an email ending with "@school.com".'
    error_message =  'Invalid school email format. Please use an email ending with "@school.com".'

    good_email =  re.match(regex, school_email)
    if good_email:
        return school_email
    else:
        raise ValidationError(error_message, params={'school_email': school_email})