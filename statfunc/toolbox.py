'''
Created on Sep 12, 2017

@author: idolchevic
'''
import re
def convert_string_to_float(value):
    try:
        return float(str(value).replace(',','.').strip())
    except ValueError:
        return None

def convert_string_to_int(value):
    return int(''.join(re.findall('[0-9]',value)))   