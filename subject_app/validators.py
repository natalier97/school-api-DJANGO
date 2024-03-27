from django.core.exceptions import ValidationError
import re




def validate_professor_name(professor_name):
    #Professor name must be in the format "Professor Adam".'
    regex= r"^Professor+ [A-Z][a-z]+$"
    error_message = 'Professor name must be in the format "Professor Adam".'
    good_name= re.match(regex, professor_name)
    if good_name:
        return professor_name
    else:
        raise ValidationError(error_message, params={'professor_name': professor_name})

def validate_subject_name(value):
    if value.title() != value:
        raise ValidationError("Subject must be in title case format.")

# def validate_subject_name(subject_name):
   
#     regex = r"^[A-Z][a-z]+$"
#     # (?: [A-Z][a-z]+)?
#  #title format
#     error_message = "Subject must be in title case format."
#     good_name = re.match(regex, subject_name)
#     if good_name:
#         return subject_name
#     else:
#         raise ValidationError(error_message, params={'subject_name': subject_name})
