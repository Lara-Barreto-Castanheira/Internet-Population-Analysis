# Internet Population Analysis 

- Reads internet population data from a CSV file

- Structures the data into a dictionary format

- Generates population trend plots for each continent

## Overview

This project analyzes the growth of internet users across different continents over time using data from a CSV file. The script reads the population data, structures it into a dictionary, and generates plots for visualization.


## Requirements

This project requires Python and the following libraries:

- csv (built-in Python module)

- matplotlib (To install matplotlib, run: pip install matplotlib)

## Usage

Ensure you have a CSV file named data.csv in the project directory, formatted with columns: continent, year, and population.

## Run the script:

The script will generate and display plots showing the internet population growth for each continent.

## Functions

### 1. generate_population_dictionary_from_datacsv(filename)

- Reads data from a CSV file and creates a dictionary structured as:

{
    "Africa": {"population": [100, 200, 300], "years": [1990, 2000, 2010]},
    "Asia": {"population": [150, 250, 350], "years": [1990, 2000, 2010]},
    "Europe": {"population": [50, 100, 200], "years": [1990, 2000, 2010]}
}

- Returns the dictionary

### 2. generate_population_plots_from_population_dictionary(population_dictionary)

- Uses the dictionary to generate line plots for each continent.

- Displays the trends in internet population over time.


## License

This project was created as part of She Codes. Feel free to use and modify it for learning purposes. If you use this code in a project, please give credit.

