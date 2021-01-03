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
        1.1*10**-52, C**0.5*(kg*m/C**2)**(-0.5)
    ]
]

# Powers
powers = [-1.5, -0.5, 0, 0.5, 1.5]

# Length
lengthConstants = len(constants[0])
lengthPowers = len(powers)