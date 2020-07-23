def words_to_numbers(string, lang="en"):
    func_dict = {
        "en": en_words_to_numbers,
        "zh-tw": zhtw_words_to_numbers
    }
    try:
        func_dict[lang](string)
    except KeyError:
        langs = ", ".join([i for i in func_dict])
        print(f"Language code '{lang}' does not exist. Valid language codes: [{langs}]")

def en_words_to_numbers(string):    
    # Initialize variables
    output_number = 0
    output_string = ""
    prev_type = None
    value = 0
    
    # Process the strings
    string = clean_string(string)
    nums = [i for i in string.split(" ") if not i.isspace() and i != ""]
    print(nums)

    # If literal is True: We take the words literally, used for verbal expressions
    # Idea: literal = True if no "units" exist
    # Examples: 
    # Nineteen Ninety-Eight = 1998 (year)
    # One Twenty = 120
    literal = not has_units(nums)
    
    # Do
    for i in range(len(nums)):
        num = nums[i]
        print(num)
        try:
            this_type = get_type(num)
            if this_type == "ones":
                if literal:
                    if prev_type == "tens":
                        value += int(conv[num])
                        output_string += str(value)
                        value = 0
                    else:
                        output_string += conv[num]
                else:
                    value += int(conv[num])
            elif this_type == "special_tens":
                if literal:
                    output_string += conv[num]
                else:
                    value += int(conv[num])
            elif this_type == "tens":
                if literal:
                    try:
                        next_type = get_type(nums[i+1])
                        if next_type == "ones":
                            value += int(conv[num])
                        else:
                            output_string += conv[num]
                    except IndexError:
                        output_string += conv[num]
                else:
                    value += int(conv[num])
            elif this_type == "units":
                # If the first sub-string is a unit, then we append "one" - i.e. intialize the value instead of multiplying
                if i == 0:
                    value = int(conv[num])

                # Otherwise we multiply the value by the unit (i.e. hundred, thousand, etc..)
                else:
                    value *= int(conv[num])

                if "thousand" in num or "million" in num or "billion" in num:
                    output_number += value
                    value = 0
            
            if i == len(nums) - 1:
                output_number += value
                value = 0
            prev_type = this_type
            print(output_number, output_string)

        except KeyError as e:
            print(repr(e))
    
    return output_number

def zhtw_words_to_numbers(string):
    pass

def get_type(num_string):
    if num_string in ones:
        return "ones"
    if num_string in tens:
        return "tens"
    if num_string in special_tens:
        return "special_tens"
    if num_string in units:
        return "units"

def has_units(num_list):
    for unit in units:
        if unit in num_list:
            return True
    else:
        return False

def string_add(curr, string):
    return string + curr

def sum_add(curr, string):
    return str(eval(curr + string))

def clean_string(string):
    string = re.sub(r'(\b)(and)(\b)', " ", string)
    string = re.sub(r'[^\w]', " ", string)
    return string
