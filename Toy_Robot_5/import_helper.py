import sys
from importlib import import_module
  
# dynamic import  
def dynamic_import(): 


    module_name = sys.argv[-1]

    try:
        script_module = import_module(module_name)
    except ImportError:
        print(f"Error: could not import module '{module_name}' ")
        sys.exit(1)

    if hasattr(script_module, 'dynamic_import'):
        script_module.dynamic_import()
    else:
        print(f"Eror: Module '{module_name}' does not have a 'main' function")
 