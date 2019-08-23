from rest_framework import status
from rest_framework.decorators import api_view

from . import constants
from rest_framework.response import Response

def return_type_standard(type_key):
    result = {}
    if  constants.area_mapping.get(type_key,None) is not None:
        type_value = constants.area_mapping.get(type_key)
        result['type_standard'] = 'normal'
        result['type_value'] = type_value
        return result
    elif type_key in constants.xfaPdf_area_mapping:
        result['type_standard'] = 'xfaPDF'
        result['type_value'] = type_key
        return result
    else:
        raise ValueError({'error': 'type 不在mapping列表里'})