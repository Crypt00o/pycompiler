from builtins import open,exec
from importlib.util import spec_from_file_location,module_from_spec
from marshal import load
from sys import argv 

def run_compiled_code(bytecode_file):
    with open(bytecode_file,'rb') as file:
        bytecode=load(file)
        exec(bytecode)


def run_full_compiled_code(bytecode_file):
    try:
        spec = spec_from_file_location(bytecode_file, bytecode_file)
        module_compiled = module_from_spec(spec)
        spec.loader.exec_module(module_compiled)
        return module_compiled.main()
    except Exception as exception: 
        print(exception)

if __name__ == "__main__" :
    try:
        run_compiled_code(argv[1])
    except:
        run_full_compiled_code(argv[1])
