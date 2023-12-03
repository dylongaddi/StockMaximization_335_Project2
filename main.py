# Execute the content of ExhaustiveSearchStockMaximization.py
with open('ExhaustiveSearchStockMaximization.py') as file:
    code_object = compile(file.read(), 'ExhaustiveSearchStockMaximization.py', 'exec')
    exec(code_object)

# Execute the content of DPStockMaximization.py
with open('DPStockMaximization.py') as file:
    code_object = compile(file.read(), 'DPStockMaximization.py', 'exec')
    exec(code_object)
