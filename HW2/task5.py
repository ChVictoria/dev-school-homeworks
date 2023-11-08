
def get_root_property(dict_, value):
    for key in dict_.keys():
        if type(dict_[key]) == list:
            if value in dict_[key]:
                return key
        else:
            if get_root_property(dict_[key], value):
                return key
    return

object = {
"one": {
"nest1": {
"val1": [9, 34, 92, 100]
}
},
"2f7": {
"n1": [10, 92, 53, 71],
"n2": [82, 34, 6, 19]
}
}
print(get_root_property(object,9))
