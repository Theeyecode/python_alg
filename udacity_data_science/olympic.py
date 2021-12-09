#    Using the numpy.dot function, create a new dataframe called
#     'olympic_points_df' that includes:
#         a) a column called 'country_name' with the country name
#         b) a column called 'points' with the total number of points the country
#            earned at the Sochi olympics.

import numpy as np
import pandas as pd
from pandas import DataFrame, Series


countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
             'Netherlands', 'Germany', 'Switzerland', 'Belarus',
             'Austria', 'France', 'Poland', 'China', 'Korea',
             'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
             'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
             'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3,
        3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4,
          3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2,
          2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_countries = {'country_name': Series(countries), 'gold': Series(
    gold), 'silver': Series(silver), 'bronze': Series(bronze)}
olympic_countries_df = DataFrame(olympic_countries)
olympic_medals = olympic_countries_df[['gold', 'silver', 'bronze']]
olympic_medals_dot = np.dot(olympic_medals, [4, 2, 1])
olympic_points = {'country_name': Series(
    countries), 'points': Series(olympic_medals_dot)}
olympic_points_df = DataFrame(olympic_points)
print(olympic_points_df)
