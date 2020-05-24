# --------------
#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 


#Code for categorical variable
def categorical(df):
    categorical_var=df.select_dtypes(include='object')
    return categorical_var

#Code for numerical variable
def numerical(df):
    numerical_var=df.select_dtypes(include='number')
    return numerical_var


#code to check distribution of variable
def clear(df,col,val):
    return df[col].value_counts()[val]
   

#Code to check instances based on the condition
def instances_based_condition(df,col1,val1,col2,val2):
   return df[(df[col1] > val1) & (df[col2]== val2)]


# Code to calculate different aggreagted values according to month

def agg_values_ina_month(df,date_col,agg_col, agg):
    df[date_col] = pd.to_datetime(df[date_col])
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min,'sum':np.sum,'len':len}
    aggregated_value = df.pivot_table(values=[agg_col], index=df[date_col].dt.month,aggfunc={agg_col:aggregate      [agg]})
    return aggregated_value


# Code to group values based on the feature
def group_values(df,col1,agg1):
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min,'sum':np.sum,'len':len}
    return df.groupby(col1).agg(aggregate[agg1])


# function for conversion 
def convert(df,celsius):
    fahr_temp=32+ 9*df[celsius]/5
    return fahr_temp


# Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable `path` for you.
weather=pd.read_csv(path)

categorical(weather)
numerical(weather)

#You might be interested in checking the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column. Feel free to check on other values.
#You can check it by calling the function clear with respective parameters.
#By using index of the value or name of the value you can check the number of count
clear(weather,'Weather','Cloudy')


# Now suppose you want to check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25. You can dicretly check it by calling the function instances_based_condition with respective parameters.
wind_speed_35_vis_25 = instances_based_condition(weather,'Wind Spd (km/h)',35,'Visibility (km)',25)


#You have temperature data and want to calculate the mean temperature recorded by month.You can generate a pivot table which contains the aggregated values(like mean, max ,min, sum, len) recoreded by month. 
#You can call the function agg_values_ina_month with respective parameters. 

agg_values_ina_month(weather,'Date/Time','Dew Point Temp (C)','mean')


# To groupby based on a column like you want to groupby on Weather column and then aggregate the mean values of each column for different types of weather using mean. You can call the function group_values.
# Feel free to try on diffrent aggregated functions like max, min, sum, len

mean_weather = group_values(weather,"Weather",'mean')


# You have a temperature data and wanted to convert celsius temperature into fahrehheit temperatures you can call the function convert.

convert(weather,"Temp (C)")



