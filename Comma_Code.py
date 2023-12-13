import sys

spam = ['apples', 'bananas', 'tofu', 'cats']
one_item_list = ["city"]
empty_list = []

def comma_code(input_list):
    #print(input_list)
    if len(input_list) == 0:
        print("input_list is empty")
        sys.exit()
    elif len(input_list) == 1:
        return input_list[0]
    else:
        var = ""
        for i in input_list[:-1]:
            var = var + i + ", " 
        var = var + "and " + input_list[-1]
        print(var)

comma_code(spam)

# def format_list(input_list):
#     if not input_list:
#         return "The list is empty."
#     elif len(input_list) == 1:
#         return str(input_list[0])
#     else:
#         # Join all items with commas and spaces, with 'and' before the last item
#         return ', '.join(input_list[:-1]) + ', and ' + input_list[-1]

# # Example usage:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# formatted_string = format_list(spam)
# print(formatted_string)
