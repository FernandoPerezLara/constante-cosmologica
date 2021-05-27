<br />
<p align="center">
  <a href="https://github.com/FernandoPerezLara/cosmological-constant/">
    <img src="https://i.imgur.com/Y7hhM9l.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Cosmological Constant</h3>

  <p align="center">
    Heuristic determination of the cosmological constant
    <br />
    <a href="https://www.worldscientific.com/doi/abs/10.1142/S0217732321501145"><strong>Read more about the study »</strong></a>
    <br />
    <br />
    <a href="https://github.com/FernandoPerezLara/cosmological-constant/">View Code</a>
    ·
    <a href="https://github.com/FernandoPerezLara/cosmological-constant/issues">Report Bug</a>
    ·
    <a href="https://github.com/FernandoPerezLara/cosmological-constant/discussions">Start a discussion</a>
  </p>
</p>
<br />

<p align="center">
    <a href="https://github.com/FernandoPerezLara/cosmological-constant" alt="Github downloads">
        <img src="https://img.shields.io/github/downloads/FernandoPerezLara/cosmological-constant/total?logo=github&style=flat-square" />
    </a>
    <a href="https://github.com/FernandoPerezLara/cosmological-constant/issues" alt="Github open issues">
        <img src="https://img.shields.io/github/issues-raw/FernandoPerezLara/cosmological-constant?logo=github&style=flat-square" />
    </a>
    <a href="https://github.com/FernandoPerezLara/cosmological-constant/issues" alt="Github clossed issues">
        <img src="https://img.shields.io/github/issues-closed-raw/FernandoPerezLara/cosmological-constant?logo=github&style=flat-square" />
    </a>
    <a href="https://github.com/FernandoPerezLara/cosmological-constant/releases" alt="Github releases">
        <img src="https://img.shields.io/github/v/release/FernandoPerezLara/cosmological-constant?logo=github&style=flat-square" />
    </a>
    <a href="https://github.com/FernandoPerezLara/cosmological-constant/commits" alt="Github commit activity">
        <img src="https://img.shields.io/github/commit-activity/y/FernandoPerezLara/cosmological-constant?logo=github&style=flat-square" />
    </a>
</p>

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

## How does it work?
As previously said, this program will create all the possible combinations to find those units that are the same as those from the cosmological constant.

These combinations are made up of powers that act as powers, roots and divisions.

The number of combinations will be equal to the number of powers that we want to raise raised to the number of constants with which we want to work.
<p align="center">
    <img src="https://render.githubusercontent.com/render/math?math=N_{Combinations}={L_{Powers}}^{L_{Constants}}">
</p>

To optimize processing time, these combinations are performed simultaneously based on the number of constants we use. We use multiprocessing to perform these operations, if we have 8 combinations, the program will be executed in 8 cores.

To see if a combination is among the possible ones, the resulting units are compared and stored.

## Contributors
This work has been possible thanks to:
- [Manuel Ureña Palomo](https://www.linkedin.com/in/manuel-urue%C3%B1a-palomo/) for having the idea and for having trusted it.
- [Fernando Pérez Lara](https://www.linkedin.com/in/fernandoperezlara/) ([**@FernandoPerezLara**](https://github.com/FernandoPerezLara)) for having developed the necessary software to make this idea come true.

## Acknowledgments
I would like to thank [Manuel Ureña Palomo](https://www.linkedin.com/in/manuel-urue%C3%B1a-palomo/) for giving me the pleasure of working with him on this magnificent project. It has been a pleasure to have worked side by side with this person, I have learned a lot and I have had a great time.

I hope you continue to grow as a person in this wonderful world in which we live. ♥

## License
Copyright (c) 2021 Fernando Pérez Lara.

Licensed and distributed under the [MIT](LICENSE.txt) license.
