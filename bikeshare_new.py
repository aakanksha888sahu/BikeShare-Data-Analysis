import pandas as pd
import numpy as np
import time
def load_data(city,month='none',day='none'):
    city_data={'chicago':'chicago.csv','washington':'washington.csv','new_york':'new_york_city.csv'}
    df=pd.read_csv(city_data[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    return df
def none_filter(df):   
    print('Computing the statistics!')
    start=time.time()
    pop_hour=df['hour'].mode()[0]
    print('The popularity in whole six months are\n')
    print('The most popular hour is: ',pop_hour)
    print('Time for computation ',time.time()-start,'\n')
    pop_month=df['month'].mode()[0]
    print('The most popular month is: ',pop_month)
    print('Time for computation ',time.time()-start,'\n')
    pop_day=df['day_of_week'].mode()[0]
    print('The most popular day of the week is: ',pop_day)
    print('Time for computation ',time.time()-start,'\n')
    pop_station_start=df['Start Station'].mode()[0]
    pop_station_end=df['End Station'].mode()[0]
    print('The most common start station is: ',pop_station_start)
    print('Time for computation ',time.time()-start,'\n')
    print('The most common end station is: ',pop_station_end)
    print('Time for computation ',time.time()-start,'\n')
    customers=df['User Type'].value_counts()
    print('The customers types are \n',customers)
    print('Time for computation ',time.time()-start,'\n')
    if(city=='chicago' or city=='new_york'):
        genders=df['Gender'].value_counts()
        print('The Gender types are \n',genders)
        print('Time for computation ',time.time()-start,'\n')
        earliest_year=df['Birth Year'].min()
        print('The earliest year of DOB is: ',earliest_year)
        print('Time for computation ',time.time()-start,'\n')
        latest_year=df['Birth Year'].max()
        print('The youngest year of DOB is: ',latest_year)
        print('Time for computation ',time.time()-start,'\n')
        most_common_year=df['Birth Year'].mode()
        print('The most common year of birth is: ',most_common_year)
        print('Time for computation ',time.time()-start,'\n')
    total=df['Trip Duration'].sum()
    print('The total time of trip is: ',total)
    print('Time for computation ',time.time()-start,'\n')
    avg=df['Trip Duration'].mean()
    print('The average time of trip is: ',avg)
    print('Time for computation ',time.time()-start,'\n')
    df['combine'] = df['Start Station']+df['End Station']
    comm_route=df['combine'].mode()[0]
    print('The Common route is: ',comm_route)
    print('Time for computation ',time.time()-start,'\n')
    #print(df.head())
    print('\nThe total time for computation is ',time.time()-start,'\n')
def month_filter(df,month):
    start=time.time()
    is_month=df['month']==month
    is_value=df[is_month]
    df2=pd.DataFrame(is_value)
    pop_month_hour=df2['hour'].mode()[0]
    print('The most popular hour is ',pop_month_hour)
    print('Time for computation ',time.time()-start,'\n')
    pop_month_day=df2['day_of_week'].mode()[0]
    print('The most popular day of the week is ',pop_month_day)
    print('Time for computation ',time.time()-start,'\n')
    pop_station_start=df2['Start Station'].mode()[0]
    pop_station_end=df2['End Station'].mode()[0]
    print('The most common start station is: ',pop_station_start)
    print('Time for computation ',time.time()-start,'\n')
    print('The most common end station is: ',pop_station_end)
    print('Time for computation ',time.time()-start,'\n')
    customers=df2['User Type'].value_counts()
    print('The customers types are \n',customers)
    print('Time for computation ',time.time()-start,'\n')
    if(city=='chicago' or city=='new_york'):
        genders=df2['Gender'].value_counts()
        print('The Gender types are \n',genders)
        print('Time for computation ',time.time()-start,'\n')
        earliest_year=df2['Birth Year'].min()
        print('The earliest year of DOB is: ',earliest_year)
        print('Time for computation ',time.time()-start,'\n')
        print('\n')
        latest_year=df2['Birth Year'].max()
        print('The youngest year of DOB is: ',latest_year)
        print('Time for computation ',time.time()-start,'\n')
        most_common_year=df2['Birth Year'].mode()
        print('The most common year of birth is: ',most_common_year)
        print('Time for computation ',time.time()-start,'\n')
    total=df2['Trip Duration'].sum()
    print('The total time of trip is: ',total)
    print('Time for computation ',time.time()-start,'\n')
    avg=df2['Trip Duration'].mean()
    print('The average time of trip is: ',avg)
    print('Time for computation ',time.time()-start,'\n')
    df2['combine'] = df2['Start Station']+df['End Station']
    comm_route=df2['combine'].mode()[0]
    print('The Common route is: ',comm_route)
    print('Time for computation ',time.time()-start,'\n')
    print('\nThe total time for computation is ',time.time()-start,'\n')
def week_day_filter(df,week_day):
    start=time.time()
    is_week_day=df['day_of_week']==week_day
    is_value=df[is_week_day]
    df2=pd.DataFrame(is_value)
    pop_day_hour=df2['hour'].mode()[0]
    print('The most popular hour is ',pop_day_hour)
    print('Time for computation ',time.time()-start,'\n')
    pop_station_start=df2['Start Station'].mode()[0]
    pop_station_end=df2['End Station'].mode()[0]
    print('The most common start station is: ',pop_station_start)
    print('Time for computation ',time.time()-start,'\n')
    print('The most common end station is: ',pop_station_end)
    print('Time for computation ',time.time()-start,'\n')
    customers=df2['User Type'].value_counts()
    print('The customers types are \n',customers)
    print('Time for computation ',time.time()-start,'\n')
    if(city=='chicago' or city=='new_york'):
        genders=df2['Gender'].value_counts()
        print('The Gender types are \n',genders)
        print('Time for computation ',time.time()-start,'\n')
        earliest_year=df2['Birth Year'].min()
        print('The earliest year of DOB is: ',earliest_year)
        print('Time for computation ',time.time()-start,'\n')
        latest_year=df2['Birth Year'].max()
        print('The youngest year of DOB is: ',latest_year)
        print('Time for computation ',time.time()-start,'\n')
        most_common_year=df2['Birth Year'].mode()
        print('The most common year of birth is: ',most_common_year)
        print('Time for computation ',time.time()-start,'\n')
    total=df2['Trip Duration'].sum()
    print('The total time of trip is: ',total)
    print('Time for computation ',time.time()-start,'\n')
    avg=df2['Trip Duration'].mean()
    print('The average time of trip is: ',avg)
    print('Time for computation ',time.time()-start,'\n')
    df2['combine'] = df2['Start Station']+df['End Station']
    comm_route=df2['combine'].mode()[0]
    print('The Common route is: ',comm_route)
    print('Time for computation ',time.time()-start,'\n')
    print('\nThe total time for computation is ',time.time()-start,'\n')
    

print("Hello Welcome to Bikeshare!")
city=input('Which city data you would like to view:- \n chicago \n washington \n new_york\n')
choice_of_filter=input('Would you like to filter by month, day or nothing?\n')
if(choice_of_filter=='month'):
    month=int(input('Which month data you would like to view ?\n Enter between 1-6\n'))
if(choice_of_filter=='day'):
    week_day=input('Which day of the week you would like to see? \n Eg- Monday\n')
df=load_data(city)
if(choice_of_filter=='nothing'):
    none_filter(df)
if(choice_of_filter=='month'):
    month_filter(df,month)
if(choice_of_filter=='day'):
    week_day_filter(df,week_day)