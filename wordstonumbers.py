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
    value = 0
    
    # Process the strings
    string = clean_string(string)
    nums = [i for i in string.split(" ") if not i.isspace() and i != ""]
    print(nums)
    
    # Do
    for i in range(len(nums)):
        num = nums[i]
        print(num)
        try:
            this_type = get_type(num)
            if this_type == "ones" or this_type == "tens":
                value += int(conv[num])
            elif this_type == "units":
                value *= int(conv[num])
                if "thousand" in num or "million" in num or "billion" in num:
                    output_number += value
                    value = 0
            
            if i == len(nums) - 1:
                output_number += value
                value = 0
            print(output_number, value)
        except KeyError as e:
            print(repr(e))
    
    return output_number

def zhtw_words_to_numbers(string):
    pass

def get_type(num_string):
    if num_string in ones:
        return "ones"
    if num_string in tens or num_string in special_tens:
        return "tens"
    if num_string in units:
        return "units"

def get_add_type(this, other):
    if this == "ones":
        if other == "ones":
            return string_add
        return sum_add
    elif this == "tens":
        if other == "units":
            return sum_add
        return string_add
    return string_add

def string_add(curr, string):
    return string + curr

def sum_add(curr, string):
    return str(eval(curr + string))

def clean_string(string):
    string = re.sub(r'(\b)(and)(\b)', " ", string)
    string = re.sub(r'[^\w]', " ", string)
    return string
