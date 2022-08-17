
def f1():
    import pandas as pd
    import matplotlib.pyplot as plt
    import time
    import numpy as np
    import mysql.connector
    from sqlalchemy import create_engine
    
    #df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
    
    df = pd.read_csv('csv1.csv', parse_dates=['Date'])
    df['Active_Cases'] = df['Confirmed']-df['Recovered']-df['Deaths']
    df.rename(columns={'Confirmed':'Total_Confirmed'},inplace=True)
    df.loc[df['Country']=='Korea, South','Country']='South Korea'
    dfw = pd.read_csv('worldwide-aggregate.csv', parse_dates=['Date'])
    
    #dfw = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/worldwide-aggregate.csv')
    
    dfw2=dfw.drop(columns=['Increase rate'])

    intro='''       ** * ** * ** * ** ** /// _ A Year of COVID - 19 Global Pandemic_ \\\ ** ** * ** ** * ** **

                     
       '''
    '''
    A novel strain of coronavirus — SARS-CoV-2 — was first detected in December
    2019 in Wuhan, a city in China’s Hubei province with a population of 11 million,
    after an outbreak of pneumonia without an obvious cause.
    The virus has now spread to over 200 countries and territories across the globe
    and was characterized as a pandemic by the World Health Organization.
    India coronavirus cases crossed the one million or the 10 lakh-mark.
    The aim of this project is todo the analysis of fights of World against Coronavirus.

    '''

    end='''

         DATA SOURCE :  https://github.com/datasets/covid-19
         REFRENCES:  https://stackoverflow.com/
                     https://www.geeksforgeeks.org/
                     https://www.w3schools.com/
                     https://matplotlib.org/            
                    
         Thank You'''
    datefrom=str((df['Date'].unique()).min()).partition('T')[0]
    updated_date=str((df['Date'].unique()).max()).partition('T')[0]


    main_menu= '''     + ======== MAIN MENU  ======== +
             1.COVID 19 Data Import To DataFrame or Export TO CSV File
             2.Data Manipulation
             3.COVID 19 Data Anyalysis
             4.COVID 19 Data Visualization
             5.Importing To sql 
             6.Exit
                        '''
    import_export_menu='''    + ========  IMPORT/EXPORT MENU  ======== +
             1.  Import CSV to DataFrame according to date
             2.  Export DataFrame Data to CSV File
             3.  Return to Main Menu
                           '''
    manipulation_menu='''\n
                    1. Insert Rows
                    2. Add another dataframe file
                    3. RETURN TO MENU '''

    analysis_menu='''\n            + ========  SEARCH/ADDITION/DELETION ======== +
                   1.   Dispaly All Records Datewise [else type 'n' or 'N
                   
                   2.   Display Data of Selected Column
                   3.   Search Records based on Country
                   
                   4.   Top 5 Countries with most cases overall.             
                   5.   Top 5 Countries with least cases overall.
                   
                   6.   Top 5 Countries with most Active cases at the present
                   
                   7.   Top 5 Countries with least Active cases at the present
                   8.   World - Total Overall,Recovered,Deaths and Active Cases 
                   9.   Display dataframe information
                   10.   Display description of DataFrame(aggregate functions)
                  11.   Return to Main Menu'''
    sqlmenu= ''' + ========  SQL MENU ======== +
                1.Export to Sql
                2.Import from Sql
                3.Return to main menu 
            '''
    
    plot_menu='''\n\n            + =========  PLOT MENU  ========= +
    1.  Line Plot of  COUNTRIES- India,US,Brazil,France,Russia,Italy on the basis of total cases
    2.  Line Plot of user defined countries on the basis of  -
               A) Active Cases
               B) Recovered
               C) Death
               D) Cases overall
    3.  Pie chart of Total Confirmed , Recovered and Deaths all over the world
    4.  Pie chart on the basis of top 5 countries in TOTAL CONFIRMED CASES
    5.  Bar chart on the basis of top 5 countries in TOTAL DEATHS CASES
    6.  Bar chart on the basis of top 5 countries in TOTAL RECOVERED CASES
    7.  Subplot of World's Confirmed Recovered and Deaths
    8.  Histogram showing frequency of India's Active Cases till date 
    9.  Return to Main Menu'''


    for i in intro:
        print(i,end='')
        time.sleep(0.001)

    while True:
        print(main_menu)
        print('The data has been updated from-' , datefrom,' till date -' ,updated_date)
        mainMenuChoice=int(input('Enter your choice ->  '))
        if mainMenuChoice==1:
            while True:
                print(import_export_menu)
                IOChoice=int(input('Enter your choice ->  '))
                if IOChoice==1:
                    df= pd.read_csv("csv1.csv" )
                    df['Active_Cases'] = df['Confirmed']-df['Recovered']-df['Deaths']
                    df.rename(columns={'Confirmed':'Total_Confirmed'},inplace=True)
                    df.loc[df['Country']=='Korea, South','Country']='South Korea'
                    print(df)
                elif IOChoice==2:
                    df.to_csv ("covid19.csv", index = False, header=True)
                    print('\nData Written in [covid19.csv] file.........\n\n')
                elif IOChoice==3:
                    print('\n*********-Back to Main menu-*********\n\n')
                    break
                else:
                    print('\n ❌ Wrong Choice ❌ \n')
        elif mainMenuChoice==2:
            while True:			
                print(manipulation_menu)	
                mch=int(input("Enter your choice"))	
                if mch==1:
                    col=df.columns				
                    print(col)				
                    print(df.head(1))			
                    j=0				
                    ninsert={}				
                    for i in col:
                        print("Enter ", col[j], " value")	
                        nval=input()				
                        ninsert[col[j]]=nval			

                        j=j+1

                    print(ninsert)
                    df = df.append(ninsert, ignore_index=True)
                    print("New row inserted")
                

                elif mch==2:
                    csvname=input('Enter location of csv ')
                    newdf=pd.read_csv(csvname)
                    print(newdf)
                elif mch==3:
                    break
                    
        elif mainMenuChoice==3:
            while True:
                print(analysis_menu)
                analysisChoice=int(input('Enter your choice ->  '))
                if analysisChoice==1:
                    d=str(input('enter in format 2020-MM-DD '))
                    print('The data has been updated from-' , datefrom,' till date -' ,updated_date)
                    if d in 'nN':
                               break
                    else :
                                 
                            dfd=df[df['Date']== d ]
                            print('Content of data frame ')
                            pd.set_option('display.expand_frame_repr',False)
                            pd.set_option('display.max_rows',1100)
                            print(dfd)
                            
                elif analysisChoice==2:
                    print('\nList of Columns are -')
                    for x in df.columns:
                        print(x)
                    print(' ')
                    clist=[]
                    while True:
                        c=str(input('\nEnter column name -> '))
                        clist.append(c)
                        c2=str(input('Want to give more column name-> [IF YOU DONT WANT WRITE N OR n] '))
                        
                        if c2 in 'nN':
                            break
                        else :
                            clist.append(c2)
                        break
                    a=df.columns[df.columns.isin(clist)]

                    
                    print('Details of Selected columns data')
                    print(df[a])

                    print()
                    print('NOTE- If the column is not displayed please check the column name entered')
                    print()
                    
                elif analysisChoice==3:
                    country_list=df['Country'].unique()
                    print(country_list)
                    c=str(input('Enter any country name '))
                    dfc=df[df['Country']== c]
                    print('Details of Selected Country')
                    print(dfc)
               
             
                elif analysisChoice==4:
                    a=(df['Date'].unique()).max()

                    maxdf=df.loc[df['Date']==a]

                    cov=maxdf.pivot('Country','Date',values='Total_Confirmed' )
                    cov=cov.sort_values(a,ascending=False)
                    b=cov.head()[a]
                    print('TOP 5 COUNTRIES WITH MOST CASES to date',updated_date )
                    print(b)
                elif analysisChoice==5:
                    a=(df['Date'].unique()).max()

                    maxdf=df.loc[df['Date']==a]

                    cov=maxdf.pivot('Country','Date',values='Total_Confirmed' )
                    cov=cov.sort_values(a)
                    b=cov.head()[a]
                    print('TOP 5 COUNTRIES on the basis of TOTAL CASES till date',updated_date)
                    print(b)
                elif analysisChoice== 6:
                    a=(df['Date'].unique()).max()

                    maxdf=df.loc[df['Date']==a]

                    cov=maxdf.pivot('Country','Date',values='Active_Cases' )
                    
                    cov=cov.sort_values(a,ascending=False)
                    b=cov.head()[a]
                    print('TOP 5 COUNTRIES WITH MOST Active Cases on date',updated_date )
                    print(b)
                elif analysisChoice==7:
                    a=(df['Date'].unique()).max()

                    maxdf=df.loc[df['Date']==a]

                    cov=maxdf.pivot('Country','Date',values='Active_Cases' )
                    cov=cov.sort_values(a)
                    b=cov.head()
                    print('TOP 5 COUNTRIES WITH LEAST Active Cases on date',updated_date)
                    print(b[a])
                elif analysisChoice== 8:
                    a=df.max(axis=0)
                    k=df[df['Date']== a['Date']]
                    b=k.iloc[:,2:6].sum()
                    print(b)
                elif analysisChoice==9:
                    print(df.info())
                elif analysisChoice==10:
                    print(df.describe())
                elif analysisChoice==11:
                     print('\n*********-Back to Main menu-*********\n\n')
                     break
                else:
                    print('\n   Wrong Choice \n')

        elif mainMenuChoice==4:
            while True:
                    print(plot_menu)
                    col=['c','lightpink','tomato']
                    graph=int(input('Enter your choice ->  '))
                    if graph==1:
                        countries = ['India', 'US', 'Brazil', 'France', 'Russia','Italy']
                        df1=df[df['Country'].isin(countries)]
                        covid = df1.pivot(index='Date', columns='Country', values='Total_Confirmed' )
                        plt.style.use(u'seaborn-darkgrid')
                        covid.plot(linewidth='3',color=['crimson','c','steelblue','saddlebrown','tomato','lightpink'])
                        plt.xlabel('MONTHS')
                        plt.ylabel('TOTAL CASES')
                        plt.title('COMPARISON BETWEEN COUNTRIES')

                        plt.show()
                    elif graph==2:

                        glist=[]
                        while True:
                             g=str(input('\nEnter country/countries name -> [IF YOU DONT WANT, TYPE N OR n]'))
                             if g in 'nN':
                               break
                             else :
                                 glist.append(g)
                        print('Select the value to graph- ')
                        print('A Confirmed Cases','B Recovered Cases'  , 'C Death Cases','D Cases overall',sep='/t')
                        
                        while True:

                            g12=str(input('SELECT A , B , C OR D '))

                            if g12 in 'aA' :
                                    plt.style.use(u'seaborn-darkgrid')
                                    df2=df[df['Country'].isin(glist)]
                                    covid = df2.pivot(index='Date', columns='Country', values='Active_Cases' )
                                    covid.plot(linewidth='3',color=['steelblue','tomato','lightpink','mediumvioletred','c'])
                                    plt.xlabel('MONTHS')
                                    plt.ylabel('Active Cases')
                                    plt.title('Active Cases Visualization ')
                                    plt.show()
                                    print('NOTE- If the country is not displayed please check the column name entered')
                                    print()
                                    break
                            if g12 in 'bB' :
                                    plt.style.use(u'seaborn-darkgrid')
                                    df2=df[df['Country'].isin(glist)]
                                    covid = df2.pivot(index='Date', columns='Country', values='Recovered' )
                                    covid.plot(linewidth='3',color=['steelblue','tomato','lightpink','mediumvioletred','c'])
                                    plt.xlabel('MONTHS')
                                    plt.ylabel('Recovered Cases')
                                    plt.title('Recovered Cases Visualization')
                                    plt.show()
                                    
                                    break
                            if g12 in 'cC' :
                                    plt.style.use(u'seaborn-darkgrid')
                                    df2=df[df['Country'].isin(glist)]
                                    covid = df2.pivot(index='Date', columns='Country', values='Deaths' )
                                    covid.plot(linewidth='3',color=['steelblue','tomato','lightpink','mediumvioletred','c'])
                                    plt.xlabel('MONTHS')
                                    plt.ylabel('Deaceased Cases')
                                    plt.title('Death Cases Visualization ')
                                    plt.show()
                                    break
                            if g12 in 'dD' :
                                    plt.style.use(u'seaborn-darkgrid')
                                    df2=df[df['Country'].isin(glist)]
                                    covid = df2.pivot(index='Date', columns='Country', values='Total_Confirmed' )
                                    covid.plot(linewidth='3',color=['steelblue','tomato','lightpink','mediumvioletred','c'])
                                    plt.xlabel('MONTHS')
                                    plt.ylabel('TOTAL Cases')
                                    plt.title('Overcall Cases Visualization')
                                    plt.show()
                                    break
                            else :
                                    print('WRONG CHOICE ')
                                    break
                    elif graph==3:
                        a=df.max(axis=0)
                        k=df[df['Date']== a['Date']]
                        b=k.iloc[:,3:6].sum()
                        plt.style.use(u'grayscale')
                        plt.pie(b,labels=[ 'Recovered', 'Deaths','Active Cases'],colors=col,shadow=True)
                        print(b)
                        plt.title('COMPARISON BETWEEN COUNTRIES')
                        plt.show()
                    elif graph==4:
                        a=df.max(axis=0)
                        k=df[df['Date']== a['Date']]
                        k=k.sort_values('Total_Confirmed',ascending=False)
                        top=k.head(5).iloc[:,0:3]
                        plt.style.use('dark_background')
                        top.plot.pie(x='Country',y='Total_Confirmed',cmap='cool',labels=top['Country'],shadow=True)
                        
                        #top.plot.bar(x='Country',y='Confirmed',legend=False,cmap='Blues')
                        
                        #color=['navy','mediumblue','dodgerblue','deepskyblue','skyblue']
                        plt.xlabel('COUNTRY')
                        plt.ylabel('TOAL CONFIRMED CASES')
                        plt.title('COMPARISON BETWEEN COUNTRIES - Total Confirmed ')
                        plt.show()
                    
                    elif graph==5:
                        a=df.max(axis=0)
                        k=df[df['Date']== a['Date']]
                        k=k.sort_values('Deaths',ascending=False)
                        top=k.head(5)
                        plt.style.use(u'seaborn-darkgrid')
                        plt.axes.titlesize : 24
                        plt.axes.labelsize : 20
                        top.plot.bar(x='Country',y='Deaths',legend=False,color=['navy','mediumblue','dodgerblue','deepskyblue','skyblue'],linewidth= 3)
                        plt.xlabel('COUNTRY')
                        plt.ylabel('DEATHS')
                        plt.title('COMPARISON BETWEEN COUNTRIES - Total Deaths')
                        plt.show()
                    elif graph==6:
                        a=df.max(axis=0)
                        k=df[df['Date']== a['Date']]
                        k=k.sort_values('Recovered',ascending=False)
                        top=k.head(5)
                        plt.style.use(u'dark_background')
                        plt.plot(top.Country,top.Recovered,linewidth='1',marker='H',markersize=15,mec='r',mfc='hotpink',ls='dashed')
                        plt.bar(top.Country,top.Recovered,width=0.05)
                        plt.xlabel('COUNTRY')
                        plt.ylabel('RECOVERED')
                        plt.title('COMPARISON BETWEEN COUNTRIES - Total Recovered')
                        plt.show()
                    elif graph==7 :
                        
                        fig,axs=plt.subplots(3,1)



                        dfw2.plot(x='Date',y='Recovered',linewidth='1',ax=axs[1],color='c')

                        dfw2.plot('Date','Deaths',linewidth='1',ax=axs[2],color='steelblue')

                        plt.title('WORLD CASES')
                        dfw2.plot('Date','Confirmed',linewidth='1',ax=axs[0],color='tomato')




                        plt.tight_layout()
                        plt.show()
                    elif graph==8:
                        plt.style.use(u'dark_background')
                        dfc=df[df['Country']== 'India']
                        plt.hist(dfc.Active_Cases,color='ivory')
                        
                        plt.show()
                    elif graph==9:
                        print('\n*********-Back to Main menu-*********\n\n')
                        break
                    else:
                        print('\n   Wrong Choice \n')
        elif mainMenuChoice==5:
            while True:
                        
                        print(sqlmenu)			
                        chmenu=int(input("Enter the choice "))	
                        if chmenu==1:			
                                                               
                                engine=create_engine('mysql+pymysql://root:12345@localhost:3306/jahnvi')
                                tablename=input("Enter the table name")
                                df.to_sql(tablename,engine,if_exists="replace",index=False)
                                print('Table ',tablename,' created in SQL ')
                                

                               
                        elif chmenu==2:
                                engine=create_engine('mysql://root:12345@localhost:3306/jahnvi')
                                a='''1. 'lockdowndate' - Lockdown Dates of Countries \n 2. 'statescovid' - India's State Wise Data'''
                                print('Covid dataset in SQL -' )
                                print(a)
                                tablename=input("Enter the table name")
                                if tablename== 'lockdowndate':
                                    se='SELECT * FROM {}'.format(tablename)
                                    dfnew=pd.read_sql_query(se, engine)
                                    print("Data Fetched")
                                    userin=input('Enter the Country name to get its Lockdown Date')
                                    print( dfnew[dfnew['Country']==userin].to_string(index=False) )
                                    
                                if tablename == 'statescovid' :
                                    
                                    se='SELECT * FROM {}'.format(tablename)
                                    dfnew=pd.read_sql_query(se, engine)
                                    print("Data Fetched")
                                    userin=input('Enter the State name to get its Lockdown Date')
                                    a=dfnew[dfnew['State']==userin].to_string(index=False)
                                    print(a)
                                    print(dfnew[dfnew['State']==userin].tail())
                                    
                        elif chmenu ==3:
                                break
                        else:
                            print('\n   Wrong Choice \n')
                                
                            
                    
        elif mainMenuChoice==6:
                    print(end)
                    break
        else:
                print('WRONG CHOICE ')
               

      
                 
                             
