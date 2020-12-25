# 🌌 Cosmological constant

The main purpose of this project is to find where the cosmological constant comes from.

This program aims to show you that the cosmological constant comes from other universal constants by mixing all kinds of combinations between them.

The condition is that the combination of these constants must form the same units of the cosmological constant.

The constants we are working with now are:
- Speed of light in vacuum: <img align="center" src="https://render.githubusercontent.com/render/math?math=299792458\enspace\frac{m}{s}">
- Newtonian constant of gravitation: <img align="center" src="https://render.githubusercontent.com/render/math?math=6.6743*10^{-11}\enspace\frac{m^3}{kg*s^2}">
- Planck constant: <img align="center" src="https://render.githubusercontent.com/render/math?math=6.626*10^{-34}\enspace\frac{kg*m^2}{s}">
- Vacuum magnetic permeability: <img align="center" src="https://render.githubusercontent.com/render/math?math=1.2566*10^{-6}\enspace\frac{kg*m}{C^2}">
- Elementary charge: <img align="center" src="https://render.githubusercontent.com/render/math?math=1.6*10^{-19}\enspace{C}">
- Electron mass: <img align="center" src="https://render.githubusercontent.com/render/math?math=9.11*10^{-31}\enspace{kg}">

Combining these constants we must obtain results like the following:
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=A^{0}%20*%20B^{-1}%20*%20C^{-2}%20*%20D^{2}%20*%20E^{-1}%20*%20F^{0}%20*%20G^{2}%20*%20H^{2}%20=%20Z\enspace{m^{-2}}">
</p>

## Installation
To run this project it is necessary to download this repository. It can be done under the command:
```
git clone https://github.com/FernandoPerezLara/cosmological-constant.git
```

Once the repository is cloned on your local machine, we must execute the program with the following commands:
```
cd cosmological-constant
python -m pip install -r requirements.txt
```

## Run program
To run the program you must launch the command `python src/main.py`. This programa accepts different arguments, to see these you have to launch `--help`.

Available arguments:
* `-h, --help` Show a help message and exit.
* `--dont-save` Results are not saved, they are only displayed.
* `--hide` Results are not displayed on the screen.
* `--parameters` Hide entered parameters.

Execution command example:
```
python src/main.py --hide --parameters
```