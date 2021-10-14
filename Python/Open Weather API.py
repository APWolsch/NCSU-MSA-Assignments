#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:23:53 2021

@author: wolschlag
"""
# Call necessary python packages
import pprint
import requests
import sys
from datetime import datetime
from datetime import timedelta
import csv
import pandas as pd
import numpy as np

#List of Lists that was given 
loc = [\
       [ 'Anchorage', 'Alaska' ],\
       [ 'Chennai', 'India' ],\
       [ 'Jiangbei', 'China' ],\
       [ 'Kathmandu', 'Nepal' ],\
       [ 'Kothagudem', 'India' ],\
       [ 'Lima', 'Peru' ],\
       [ 'Manhasset', 'New York' ],\
       [ 'Mexico City', 'Mexico' ],\
       [ 'Nanaimo', 'Canada' ],\
       [ 'Peterhead', 'Scotland' ],\
       [ 'Polevskoy', 'Russia' ],\
       [ 'Round Rock', 'Texas' ],\
       [ 'Seoul', 'South Korea' ],\
       [ 'Solihull', 'England' ],\
       [ 'Tel Aviv', 'Israel' ],\
      ]

# Created  an object that is a list of strings
city_l = [ 'Anchorage,Alaska','Chennai,India','Jiangbei,China','Kathmandu,Nepal',
          'Kothagudem,India','Lima,Peru','Manhasset,New York','Mexico City,Mexico',
          'Nanaimo,Canada','Peterhead,Scotland','Polevskoy,Russia','Round Rock,Texas',
          'Seoul,South Korea','Solihull,England','Tel Aviv,Israel' ] 

# Loop cities
final_city_list = []
for j in range (0, len(city_l)):

# Calling the API using a private key
    api_key = '7fd3b2465d0db40c14998ddab3ca7f9c'
    URL = 'https://api.openweathermap.org/data/2.5/forecast?'
    URL = URL + 'q=' + city_l[j] + '&units=metric&appid=' + api_key


    response = requests.get( URL )
    if response.status_code != 200:      # Failure?
          print( 'Error:', response.status_code )
          sys.exit( 0 )
    
    data = response.json()
    
    #  Get OUR current date
    from datetime import date
    cur_dt = date.today()
    
    #  Now, search for the first block that starts tomorrow
    for i in range( 0, len( data[ 'list' ] ) ):
    
    #  Get date and time in UTC, then convert it to a Python
    #  datetime object
        dt_str = data[ 'list' ][ i ][ 'dt_txt' ]
        dt_tm = datetime.strptime( dt_str, '%Y-%m-%d %H:%M:%S' )
    
    #  Offset the UTC time by the city's timezone offset to
    #  get the city's local time
        tz_offset = data[ 'city' ][ 'timezone' ]
        dt_tm = dt_tm + timedelta( seconds=tz_offset )
        
        #  If our day is the same as the block's day, the block is for
        #  today and NOT tomorrow, so keep searching, otherwise break
        #  out of the loop
        if cur_dt.day == dt_tm.day:
            print( 'Block', str( i ), 'is still part of today' )
        else:
            start_point = i
            break  
    print( 'Block', str( i ), 'is the block at the start of tomorrow' )
    print( 'Date in Raleigh:', cur_dt )
    print( 'Date/time in ' + city_l[j] +':', dt_tm )

# First block for tomorrow 
    day_start = []
    day_start.append(start_point)
    while (start_point + 8) < 40:
        start_point = start_point + 8
        day_start.append(start_point)
    # Define days    
    day_1_block = [data['list'][day_start[0]:day_start[1]]]
    day_2_block = [data['list'][day_start[1]:day_start[2]]]
    day_3_block = [data['list'][day_start[2]:day_start[3]]]
    day_4_block = [data['list'][day_start[3]:day_start[4]]]
    day_5_block = [data['list'][day_start[4]:]]
            
    day_1_temps = []
    day_2_temps = []
    day_3_temps = []
    day_4_temps = []
    day_5_temps = []
    for x in range(0,8):
        day_1_temps.append([day_1_block[0][x][ 'main']['temp']])
        day_2_temps.append([day_2_block[0][x][ 'main']['temp']])
        day_3_temps.append([day_3_block[0][x][ 'main']['temp']])
        day_4_temps.append([day_4_block[0][x][ 'main']['temp']])
    for x in range(0,len(day_5_block[0])):    
        day_5_temps.append([day_5_block[0][x][ 'main']['temp']])
    
    day_1_mm = [min(day_1_temps),max(day_1_temps)]
    day_2_mm = [min(day_2_temps),max(day_2_temps)]
    day_3_mm = [min(day_3_temps),max(day_3_temps)]
    day_4_mm = [min(day_4_temps),max(day_4_temps)]
    day_5_mm = [min(day_5_temps),max(day_5_temps)]
    
    all_min = [day_1_mm[0],day_2_mm[0],day_3_mm[0],day_4_mm[0],day_5_mm[0]]
    all_max = [day_1_mm[1],day_2_mm[1],day_3_mm[1],day_4_mm[1],day_5_mm[1]]
    
    #Flatten list of list to perform math
    flat_all_min = [y for x in all_min for y in x]
    flat_all_max = [y for x in all_max for y in x]
    
    #flatten day min_maxes
    flat_d1_final = [y for x in day_1_mm for y in x]
    flat_d2_final = [y for x in day_2_mm for y in x]
    flat_d3_final = [y for x in day_3_mm for y in x]
    flat_d4_final = [y for x in day_4_mm for y in x]
    flat_d5_final = [y for x in day_5_mm for y in x]
    
    
    avg_min = round((sum(flat_all_min) / len(flat_all_min)),2)
    avg_max = round((sum(flat_all_max) / len(flat_all_max)),2)
    
    #Build out city list
    avg_total = [avg_min + avg_max]
    all_days_list = flat_d1_final + flat_d2_final + flat_d3_final + flat_d4_final + flat_d5_final + [avg_min] + [avg_max]
    One_City_List = [city_l[j]] + all_days_list
    final_city_list.append(One_City_List)
    
    print(One_City_List)
#Data Frame

df = pd.DataFrame(final_city_list, columns = ['City','Min 1','Max 1','Min 2','Max 2','Min 3','Max 3','Min 4','Max 4','Min 5','Max 5','Min Avg','Max Avg'])
df.to_csv('temp.csv',index = False)
           
#sum(l)/len()

# Specifying the calls on the json
#printer = pprint.PrettyPrinter( width=80, compact=False )
#printer.pprint( data[ 'list' ][ 0 ]['dt_txt'] )
#printer.pprint( city_l[0])
#val = [city_l[0]] 
#for i in range (0,39):
     #printer.pprint( data[ 'list' ][ i ][ 'main' ]['temp'] )
    # val = val + [data[ 'list' ][ i ][ 'main' ]['temp']]
     
# Write to file
#inp = open( 'temp_output.csv', 'w', encoding='latin' )
#writer = csv.writer(inp)
#writer.writerow(val)
#inp.close()


#  Print UTC and local times
#print( 'UTC time for ' + city_l[0] + ':', dt_str )
#local_str = dt_tm.strftime( '%Y-%m-%d %H:%M:%S' )
#print( 'Local time for ' + city_l[0] + ':', local_str )

#Calling Today's Date    
 
# Unused json calls
#printer.pprint( data[ 'city' ]['name'] )
#printer.pprint( data[ 'city' ]['country'] )

#printer = pprint.PrettyPrinter( width=80, compact=False )
#printer.pprint( data[ 'list' ][ 0 ]['dt_txt'] )
#printer.pprint( city_l[1])
#val = [city_l[0]] 
#for i in range (0,39):
     #printer.pprint( data[ 'list' ][ i ][ 'main' ]['temp'] )
    # val = val + [data[ 'list' ][ i ][ 'main' ]['temp']]
     
# Write to file
#inp = open( 'temp_output.csv', 'w', encoding='latin' )
#writer = csv.writer(inp)
#writer.writerow(val)
#inp.close()
       


 
 

 
 

       
           