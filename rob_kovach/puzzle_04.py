"""
Advent of Code Day 4
"""

location = __file__
passports = open(location.replace('.py', '_input.txt')).read().split('\n\n')
passport_count = len(passports)

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
fields = required_fields + ['cid']

valid_birth_years = (1920, 2002)
valid_issue_years = (2010, 2020)
valid_expiration_years = (2020, 2030)
valid_height_cm = (150, 193)
valid_heigh_in = (59,76)
valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
passport_id_length = 9

def part1():
    valid_passports = 0
    for passport in passports:
        invalid = False
        for field in required_fields:
            if (field+":") not in passport:
                invalid = True
        if not invalid:
            valid_passports += 1
    return valid_passports

def validate_fields(passport):
    valid = True
    for field in required_fields:
        if (field+":") not in passport:
            valid = False
            break
    return valid

def validate_range(value, range_):
    return int(value) >= range_[0] and int(value) <= range_[1]

def validate_height(value):
    if not value.endswith('in') and not value.endswith('cm'):
        return False
    if value.endswith('in'):
        return validate_range(int(value.replace('in', '')), valid_heigh_in)
    if value.endswith('cm'):
        return validate_range(int(value.replace('cm', '')), valid_height_cm) 

def validate_color(value):
    if not len(value) == 7:
        return False
    if value[0] != '#':
        return False
    if not value[1::].isalnum():
        return False
    return True

def validate_eye_color(value):
    return value in valid_eye_color

def validate_passport_id(value):
    if len(value) == 9 and value.isdigit():
        return True
    return False

def part2():
    valid_passports = 0
    for passport in passports:
        valid = True
        if not validate_fields(passport):
            continue
        
        fields = passport.split()
        for field in fields:
            key, value = field.split(':')
            if key == 'byr':
                if not validate_range(value, valid_birth_years):
                    valid = False
            elif key == 'iyr':
                if not validate_range(value, valid_issue_years):
                    valid = False
            elif key == 'eyr':
                if not validate_range(value, valid_expiration_years):
                    valid = False
            elif key == 'hgt':
                if not validate_height(value):
                    valid = False
            elif key == 'hcl':
                if not validate_color(value):
                    valid = False
            elif key == 'ecl':
                if not validate_eye_color(value):
                    valid = False
            elif key == 'pid':
                if not validate_passport_id(value):
                    valid = False
        if valid:
            valid_passports += 1
    return valid_passports

if __name__ == '__main__':
    print(part1())
    print(part2())