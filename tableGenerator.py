import logical_parser
    x1, x2, x3 = args # add args variables as needed

tokenization = {
    'True': True,
    'False': False,
    'and': lambda left, right: left and right,
    'or': lambda left, right: left or right,
    '(': '(',
    ')': ')'
}

def formula(n, vars, expr):
    custom_tokens = {}

    for i in range(n):
        value = True if vars[i] == 1 else False
        custom_tokens[f"x{i}"] = value
    
    custom_tokens.update(tokenization)

    return logical_parser.nested_bool_eval(expr, custom_tokens)

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

def generate(n, expr):
    values = generate_input(n)

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

        result = formula(n, col, expr)
        results.append(result) # save results
        print_row(col, result) # print current row of output

vars = 3
values = generate_input(vars)
print_results(vars, values)