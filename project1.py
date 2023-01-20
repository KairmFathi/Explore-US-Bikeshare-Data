import time
import pandas as pd

cities_dict = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#----------------------------------------------------------------------------------------------------------------------
def user_data():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\nHello!, let\'s explore US-bikshare data together')
    
    #Ask user to enter certain city
    while True:
        city=input('\nFirstly, choose your target city (for Chicago enter (a), New York City enter (b), Washington enter (c):\n')
        if city not in ('a','b','c'):
            print('\nPlease check your choice again!')
            continue
        else:
            break
    if city=='a':
        city='chicago'
    elif city=='b':
        city='new york city'
    else:
        city='washington'
   
    #Ask user to choose between all months or specific one
    while True:
        month=input('\nNow, if you want to display the whole 6 months enter (all), otherwise enter (1) for January.....(6) for June):\n')
        if month not in ('1','2','3','4','5','6','all'):
            print('\nPlease check your choice again!')
            continue
        else:
            break   
    
    #Ask user to choose between the whole week or specific day
    while True:
        day=input('\nFinally, for the whole week enter (all), otherwise choose specfifc day:\n').lower()
        if day not in ('saturday','sunday','monday','tuesday','wednesday','thursday','friday','all'):
            print('\nPlease check your choice again!')
            continue
        else:
            break
    
    print('-'*40)
    return city,month,day
#----------------------------------------------------------------------------------------------------------------------
def filtered_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    #load data file based on the entered city
    df=pd.read_csv(cities_dict.get(city))
    
    #insert 'month' and 'week_day' columns after the modification of the 'Start Time' column
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name()
    
    #user based Month filtration
    if month != 'all':
        df=df[df['month']==int(month)]
    
    #user based Week_day filtration
    if day != 'all':
        df=df[df['week_day']==day.title()]
    return df
#-----------------------------------------------------------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #Calculating the most popular month,day and hour 
    print('Most Common Month:',df['month'].mode()[0])
    print('Most Common day:',df['week_day'].mode()[0])
    df['hour']=df['Start Time'].dt.hour
    print('Most Common hour:',df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-----------------------------------------------------------------------------------------------------------------------        
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
     
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    #Calculating the most common start_station, end_station and trip
    print('Most common \'Start Station\': ',df['Start Station'].mode()[0])
    print('Most common \'End Station\': ',df['End Station'].mode()[0])
    
    df['trip']=df['Start Station']+ ' - ' +df['End Station']
    print('Most common \'Trip\': ',df['trip'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-----------------------------------------------------------------------------------------------------------------------
def trip_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #Calculating Total and Average travel time
    print('Total travel time: ',df['Trip Duration'].sum()/60/60/24,'Days')
    print('Average travel time: ',df['Trip Duration'].mean()/60,'Mins')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-----------------------------------------------------------------------------------------------------------------------   
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
   
    #Calculating User_Type allocation
    print(df.groupby(['User Type']) ['User Type'].count(),'\n')
    
    #Calculating Gender allocation
    try:
        print('Allocation of',df.groupby(['Gender']) ['Gender'].count())
    except:
        print('Allocation of Genders\n','No gender information available for this city')
    
    #Calculating earliest birth year    
    try:
        print('\nThe earliest birth year: ',int(df['Birth Year'].min()))
    except:
        print('\nThe earliest birth year: \n','No availabe data')
    
    #Calculating recent birth year     
    try:
        print('\nThe most recent birth year: ',int(df['Birth Year'].max()))
    except:
        print('\nThe most recent birth year: \n','No availabe data')
   
    #Calculating most common birth year    
    try:
        print('\nThe most common birth year: ',int(df['Birth Year'].mode()[0]))
    except:
        print('\nThe most common birth year: \n','No availabe data')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#-----------------------------------------------------------------------------------------------------------------------    
def raw_data(df):
    """Displays 5 by 5 rows as per user request"""    
    i=0
    more='y'
    while more=='y':
        print(df.iloc[i:i+5])
        i+=5
        more=input('Do you want to dsiplay more 5 rows of data? (y or n)')
    print('-'*40)
#-----------------------------------------------------------------------------------------------------------------------    
def main():
    restart='y'
    while restart=='y':
        city,month,day = user_data()
        df=filtered_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_stats(df)
        user_stats(df)        
        raw_data(df)
        restart=input('Do you want to start over again? (y or n)')
#-----------------------------------------------------------------------------------------------------------------------      

if __name__=='__main__':
    main()
