# The import statement is used to include modules in Python. A module is a file containing Python code that can define functions, classes, and variables. It allows for code reusability and better organization.
import sys # sys is included in the python library so it doens't need to be installed separately
from math import sqrt, pi # Importing specific functions and constants from the math module


sys.path.insert(1, r'C:\Users\majog\Desktop\Coursera Osiris\Coursera-Backend\Workplace') # Adding a directory to the system path to import custom modules from that location
import trial #el IDE no lo reconoce pero funciona bien
print(trial.names)

# for modules that are not part of the standard library, you can install them using package managers like pip.
# Example of importing a module and using its functions
# reload() no es muy utilizado en producción, pero es útil en desarrollo para recargar un módulo sin reiniciar el intérprete.

# Packages mas conocidos
# NumPy: Used for numerical computations and handling arrays.
# Pandas: Used for data manipulation and analysis.
# Matplotlib: Used for creating static, animated, and interactive visualizations in Python.
# Scikit-learn: Used for machine learning and data mining.
