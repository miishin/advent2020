FIELDS = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
OPTIONAL_FIELDS = ['cid']

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
    for field in FIELDS:
        if field not in p_as_dict:
            return False
    return True
    
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
