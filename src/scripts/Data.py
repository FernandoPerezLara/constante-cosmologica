from scripts import m, s, kg, C

# Constants
constants = [
    [
        # Universal constants
        [299792458, m/s],
        [6.6743*10**-11, (m**3)/(kg*(s**2))],
        [6.6260664*10**-34, (kg*(m**2))/s],
        [8.9875517923*10**9, (kg*(m**3))/((C**2)*(s**2))],
        [1.25663706212*10**-6, (kg*m)/(C**2)],
        [8.8541878176*10**-12, ((C**2)*(s**2))/(kg*(m**3))],
        [1.602176*10**-19, C],
        [7.297352568*10**-3, 1]
    ], [
        # Cosmological constant
        1.1*10**-52, m**-2
    ]
]

# Powers
powers = [-7, -6, -5, -4, -3, -2, -1, -0.5, 0, 0.5, 1, 2, 3, 4, 5, 6, 7]

# Length
lengthConstants = len(constants[0])
lengthPowers = len(powers)