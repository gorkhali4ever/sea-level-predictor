import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df.Year, 
        df['CSIRO Adjusted Sea Level']
        )

    years = range(df.Year.min(), 2051)
    prediction_first = intercept + slope * years
    plt.plot(years, prediction_first, 'r', label='fitted line since 1880 data')

    # Create second line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(
        df.loc[df.Year >=2000, 'Year'], 
        df.loc[df.Year >= 2000, 'CSIRO Adjusted Sea Level']
        )

    years = range(2000, 2051)
    prediction_second = intercept + slope * years
    plt.plot(years, prediction_second, 'g', label = 'fitted line since 2000 data')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()