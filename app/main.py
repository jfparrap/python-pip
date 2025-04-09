import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
   '''
  df=pd.read_csv('data.csv')
  countries=df['Country']
  percentages=df['World Population Percentage']
  charts.generate_pie_chart(countries, percentages)
  df=df[df['Continent']== 'South America']
  country = input('Type Country => ')
  result = utils.population_by_country(df, country)
  if len(result) > 0:
    #labels, values = utils.get_population(result[0])
    labels, values = utils.get_population(result)
    charts.generate_bar_chart(country,labels, values)
  
if __name__ == '__main__':
  run()