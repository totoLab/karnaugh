def formula(args):
    x1, x2, x3 = args # add args variables as needed
    
    # assign formula using the above arguments to the ret variable
    ret = x1 or (x2 and x3)

    return ret

def generate_input(n): # dinamically generates typically ordered truth values
    col = []
    rows = 2**n
    for i in range(n):
        truth_values = []
        step = rows / (2**(i+1))
        to_append = True
        for j in range(rows):
            if j % step == 0:
                to_append = not to_append
            truth_values.append(to_append)

        col.append(truth_values)
    
    return col

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

def print_results(n, values):
    print_header(n)

    results = []
    for j in range(len(values[0])): # lock on a coloumn
        col = []
        for i in range(len(values)): # extract same position element in matrix
            x = values[i][j]
            col.append(x)

        result = formula(tuple(col)) # convert to tuple for unpacking
        results.append(result) # save results
        print_row(col, result) # print current row of output

vars = 3
values = generate_input(vars)
print_results(vars, values)