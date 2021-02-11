import copy
from scripts import m, s, kg, C

# Constants
constants = [
    [
        # Universal constants
        [299792458, m/s],
        [6.6743*10**-11, (m**3)/(kg*(s**2))],
        [6.626*10**-34, (kg*(m**2))/s],
        [1.2566*10**-6, (kg*m)/(C**2)],
        [1.6*10**-19, C],
        [9.11*10**-31, kg]
    ], [
        # Cosmological constant
        1.1*10**-52, m**-2
    ]
]

# Powers
powers = [-10, -9, -8, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 8, 9, 10]

# Length
lengthConstants = len(constants[0])
lengthPowers = len(powers)

# Processed data
temp_constants = copy.deepcopy(constants)
temp_powers = copy.deepcopy(powers)