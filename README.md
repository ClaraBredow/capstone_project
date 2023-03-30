# CropIT - capstone project

------

### The Project

Sugar and weather make everything better: a climate-based crop recommendation.

A regional recommendation tool for sugar beet cultivar planting.

Enter regional weather data and find out which genetic combination of your sugar beet will result in the highest sugar yield.

------

### The Data

Our anonymous stakeholder kindly provided us with genetic background and sugar yield information for 1205 sugar beet cultivars.

Additionally, we were provided with detailed weather information from company-owned field-stations as well as from Openweather stations closest to the fields.

1. 'df_sugarbeet'
2. 'df_weatherstations'
3. 'df_openweather'
4. 'df_locations'

'df_sugarbeet': 1205 sugar beet cultivars on 15 fields, their sugar content and genetic background.

'df_weatherstations': hourly information of weather parameters on 15 fields for 2021.

'df_openweather': hourly information of weather parameters on the closest OpenWeather stations.

'df_locations': field locations and sowing/harvesting dates for 2021.

------

### The Team

- Dr. Clara Bredow [LinkedIn](https://www.linkedin.com/in/clara-bredow/) [GitHub](https://github.com/ClaraBredow)
- Isabelle Flaig, Dipl. Biol. [LinkedIn](https://www.linkedin.com/in/isabellecarinaflaig/) [GitHub](https://github.com/IsabelleCarinaFlaig)
- Nidia Loureiro, Msc. Global Change [LinkedIn](https://www.linkedin.com/in/nidia-loureiro-2b6524116/) [GitHub](https://github.com/NidiaL)
- Dr. Gina Capistrano Goßmann [LinkedIn](https://www.linkedin.com/in/ginacapistrano/) [GitHub](https://github.com/fraugina)

------

### The Files

Enjoy the [Notebooks]() and the [Presentation Slides]().

------

### The Requirements and Environment

**Requirements**: 

pyenv with Python: 3.9.8

**Environment**: 

use the following commands to set up the virtual environment:

    pyenv local 3.9.8
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
