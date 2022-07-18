def print_header(n):
    string = ""
    for x in range(n):
        string += "x" + str(x + 1) + "    "
    string += "| formula"
    print(string)

def print_row(col, result):
    for k in range(len(col)):
        if col[k]:
            print("true ", end=" ")
        else:
            print("false", end=" ")
            
    print("| {}".format(result))