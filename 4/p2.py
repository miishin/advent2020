from string import hexdigits
FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
OPTIONAL_FIELDS = ['cid']
BYR_LOW = 1920
BYR_HIGH = 2002
IYR_LOW = 2010
IYR_HIGH = 2020
EYR_LOW = 2020
EYR_HIGH = 2030
HGT_CM_LOW = 150
HGT_CM_HIGH = 193
HGT_IN_LOW = 59
HGT_IN_HIGH = 76
EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def main():
    f = open('input.txt', 'r')
    passports = split_into_passports(f)
    count = 0
    for passport in passports:
        if validate_passport(passport):
            count += 1
    print(count)

def split_into_passports(file):
    """
    Takes in a file object and returns a list of
    strings, each representing a single passport
    file -> [string]
    """
    passports = file.read().split('\n\n')
    return passports

def validate_passport(p):
    """
    Takes in a string representation of a passport
    String -> Boolean
    """
    p = p.replace('\n', ' ')
    p_as_dict = passport_to_dict(p)
    for key in FIELDS:
        if key in p_as_dict:
            if not validate_field(key, p_as_dict[key]):
                return False
        else:
            return False
    return True

def validate_field(field, value):
    if field == FIELDS[0]:
        return validate_byr(value)
    elif field == FIELDS[1]:
        return validate_iyr(value)
    elif field == FIELDS[2]:
        return validate_eyr(value)
    elif field == FIELDS[3]:
        return validate_hgt(value)
    elif field == FIELDS[4]:
        return validate_hcl(value)
    elif field == FIELDS[5]:
        return validate_ecl(value)
    elif field == FIELDS[6]:
        return validate_pid(value)
    else:
        return True

def validate_byr(value):
    try:
        return BYR_LOW <= int(value) <= BYR_HIGH
    except ValueError:
        raise ValueError('Birth Year must be Integer')

def validate_iyr(value):
    try:
        return IYR_LOW <= int(value) <= IYR_HIGH
    except ValueError:
        raise ValueError('Issue Year must be Integer')

def validate_eyr(value):
    try:
        return EYR_LOW <= int(value) <= EYR_HIGH
    except ValueError:
        raise ValueError('Expiration Year must be Integer')

def validate_hgt(value):
    if value.find('cm') == -1:
        if value.find('in') == -1:
            return False
        else:
            return HGT_IN_LOW <= int(value[:-2]) <= HGT_IN_HIGH
    else:
        return HGT_CM_LOW <= int(value[:-2]) <= HGT_CM_HIGH
    
def validate_hcl(value):
    if len(value) == 7 and value[0] == '#':
        for char in value[1:]:
            if char not in hexdigits[:16]:
                return False
        return True
    return False

def validate_ecl(value):
    return value in EYE_COLORS

def validate_pid(value):
    return len(value) == 9 and value.isnumeric()
    
def passport_to_dict(passport):
    """
    Takes in a passport string and returns it as a dictionary
    String -> Dictionary
    """
    p_dict = {}
    fields = passport.split(' ')
    for field in fields:
        if field == '':
            break
        subfields = field.split(':')
        key = subfields[0]
        value = subfields[1]
        p_dict[key] = value
    return p_dict
        
    
if __name__ == '__main__':
    main()
