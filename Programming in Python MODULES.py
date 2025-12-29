# The import statement is used to include modules in Python. A module is a file containing Python code that can define functions, classes, and variables. It allows for code reusability and better organization.
import sys # sys is included in the python library so it doens't need to be installed separately
from math import sqrt, pi # Importing specific functions and constants from the math module


sys.path.insert(1, r'C:\Users\majog\Desktop\Coursera Osiris\Coursera-Backend\Workplace') # Adding a directory to the system path to import custom modules from that location
import trial #el IDE no lo reconoce pero funciona bien
print(trial.names)

# for modules that are not part of the standard library, you can install them using package managers like pip.
# Example of importing a module and using its functions