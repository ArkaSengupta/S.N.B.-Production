import os
from django.core.exceptions import ValidationError

# def validate_file_extension(value):
#     ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
#     valid_extensions = ['.pdf', '.jpg', '.png']
#     if not ext.lower() in valid_extensions:
#         raise ValidationError('Unsupported file extension.')

def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Error message')
