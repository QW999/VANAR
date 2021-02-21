
# def wrap_brackets(text):
#   return "(" + text + ")"
# def wrap_brackets2(text):
#   return "[[[" + text + "]]]"
# def wrap_brackets3(text):
#   return "<<<" + text + ">>>"
#
# print( wrap_brackets("12345") )
# print( wrap_brackets2("12345") )
# print( wrap_brackets3("12345") )



def wrap_brackets3(text3):
    def wrap_brackets2(text2):
        def wrap_brackets(text):
            return "(" + text + ")"
        return "[[[" + wrap_brackets(text2) + "]]]"
    return "<<<" + wrap_brackets2(text3) + ">>>"

# print( wrap_brackets("12345") )
# print( wrap_brackets2("12345") )
print( wrap_brackets3("12345") )
