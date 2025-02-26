#Importing libraries
import csv
import matplotlib.pyplot as plt

#Creating two necessary functions
def generate_population_dictionary_from_datacsv(filename):
  """
  Generates a dictionary from csv data
  Returns a dictionary following this format:
  {
    "Africa":{population:[100,200,300]}, years:[1990,2000,2010]}
    "Asia":{population:[100,200,300]}, years:[1990,2000,2010]}
    "Europe":{population:[100,200,300]}, years:[1990,2000,2010]} 
  }
  """
  #Creating an empty dictionary
  dictionary = {}

  #Opening the data.csv file
  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    #Looping through the lines of the file
    for line in reader:
      continent = line['continent']
      year = int(line['year'])
      population = int(line['population'])
      
      #Creating the continent if it doesn't exist in the population_dicitonary
      if continent not in dictionary:
        dictionary[continent] = {'population': [], 'years': []}

      #Adding the popilation and years to the continents
      dictionary[continent]['population'].append(population)
      dictionary[continent]['years'].append(year)

  #Returning the population_dicitonary
  return dictionary

def generate_population_plots_from_population_dictionary(population_dictionary):
  """
  Generates the population plots from a dcitionary 
  One plot per continet
  """
  #Looping through the continents in the population_dictionary
  for continent in population_dictionary:
    years = population_dictionary[continent]['years']
    population = population_dictionary[continent]['population']
    plt.plot(years, population, label=continent, marker="o", alpha=0.5)

  plt.title("Internet Population per continent")
  plt.xlabel("Year")
  plt.ylabel("Internet users (in billion users)")
  plt.grid(True)
  plt.tight_layout()
  plt.legend()
  plt.show()

#Name of the cas file
filename = 'data.csv'

#Displaing a plot with the Internet population per continent
population_per_continent = generate_population_dictionary_from_datacsv(filename)
generate_population_plots_from_population_dictionary(population_per_continent)