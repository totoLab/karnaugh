printing_notation = { # horizontal space used by each col
    "bool": 6,
    "zeros": 3,
}

def print_header(n, notation="bool"):
    string = ""
    max_len = 1 + len(str(n))
    for i in range(n):
        string += "x" + str(i) + " " * (printing_notation[notation] - max_len)
    string += "| formula"
    print(string)

def print_row(col, result, notation="bool"):
    for k in range(len(col)):
        if col[k]:
            if notation == "bool":
                value = "True "
            else:
                value = "1 "
            print(value, end=" ")
        else:
            if notation == "bool":
                value = "False"
            else:
                value = "0 "
            print(value, end=" ")
   
    if result:
        if notation == "bool":
            value = "True "
        else:
            value = "1 "
    else:
        if notation == "bool":
            value = "False"
        else:
            value = "0 " 

    print("| {}".format(value))