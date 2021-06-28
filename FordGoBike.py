#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[2]:


df = pd.read_csv('/home/ahmed/Downloads/201902-fordgobike-tripdata.csv')
df.sample(5)


# In[3]:


df.duplicated().sum()


# In[4]:


df.isnull().sum()


# In[5]:


df.info()


# In[6]:


df.dropna(inplace=True)
df.info()


# In[7]:


df.head()


# In[8]:


df.describe()


# In[9]:


bin_edges = [60,315,487,726,1461]
bin_names = ['Short','Medium','Long','Very Long']
df['duration_class'] = pd.cut(df['duration_sec'], bin_edges, labels=bin_names)


# In[10]:


sum(df.start_station_id - df.end_station_id == 0)


# In[11]:


df.member_birth_year = 2019 - df.member_birth_year
df.member_birth_year


# In[12]:


df.member_gender.value_counts()


# In[13]:


df.drop(df[df['member_gender'] == 'Other'].index,inplace=True)


# Since nobody would start and end at the same point then we should drop those rows

# In[14]:


df.drop(df[df['start_station_name'] == df['end_station_name']].index,inplace=True)


# Dealing with outliers over the numerical values throughout our dataset columns that matter is important, so let's start truncating outliers

# First lets find out the InterQuartile Range (IQR) of each column

# In[15]:


duration_iqr = df.duration_sec.quantile(0.75) - df.duration_sec.quantile(0.25)
birth_year_iqr = df.member_birth_year.quantile(0.75) - df.member_birth_year.quantile(0.25)


# Now let's drop any row that is more than Q3+1.5(IQR) or less than Q1-1.5(IQR)

# In[16]:


df.drop(df[df['duration_sec'] < (df['duration_sec'].quantile(0.25) - duration_iqr*1.5)].index,inplace=True)
df.drop(df[df['duration_sec'] > (df['duration_sec'].quantile(0.75) + duration_iqr*1.5)].index,inplace=True)
df.drop(df[df['member_birth_year'] < (df['member_birth_year'].quantile(0.25) - duration_iqr*1.5)].index,inplace=True)
df.drop(df[df['member_birth_year'] > (df['member_birth_year'].quantile(0.75) + duration_iqr*1.5)].index,inplace=True)
df.info()


# Verifying these data has been cleaned of outliers

# In[17]:


sb.boxplot(data = df, y = 'member_birth_year');


# In[18]:


max(df.member_birth_year)


# Looks like it wasn't cleaned well so we will have to drop ages over 80

# In[19]:


df.drop(df[df['member_birth_year'] > 80].index,inplace=True)
df.head()


# In[20]:


df.start_time = pd.to_datetime(df.start_time)
df.end_time = pd.to_datetime(df.end_time)


# In[21]:


df.to_csv('CleanBikeShare.csv')


# # Questions to be asked from now over 
# 1. What are the most crowded stations in terms of start and end stations in bikeshare?
# 2. what conditions are affected by subscription?
# 3. Who're the most subscribers?
# 4. What are the peak times of bikeshare?
# 5. Is there any factor that affects a Simpson-Paradox throughout these times?!!
# 6. Which ages share bikes the most?
# 7. Are subscriptions affected by either of gender or age?
# 8. Why some users may not use bikeshare for their whole trip?
# 9. What is the most appearing round trip?
# 10. Is age a factor affecting share duration?
# 11. What ages affect bikeshare for all trip?
# 12. Is bikeshare over all trip affected by duration?

# ## Starting Data Exploration

# ### Univariante Exploration

# #### What are the most crowded stations in terms of start and end stations in bikeshare?

# In[22]:


plt.title("Most Start Stations")
plt.xlabel('Counts')
plt.ylabel('Start Stations')
plt.barh(df.start_station_name.value_counts().index[:10], df.start_station_name.value_counts()[:10]);


# In[23]:


plt.title("Most End Stations")
plt.xlabel('Counts')
plt.ylabel('End Stations')
plt.barh(df.end_station_name.value_counts().index[:10], df.end_station_name.value_counts()[:10]);


# Here We can see that Most people start bikesharing at the market street, also most people tend to go to San Francisco Caltrain Station 2. 

# In[24]:


df['start_end'] = df['start_station_name'] + ' to ' + df['end_station_name']
df.head()


# #### What is the most appearing round trip?

# In[25]:


plt.figure(figsize=(10,10))
plt.xticks(rotation=90)
plt.bar(df.start_end.value_counts().index[:10],df.start_end.value_counts()[:10]);
plt.xlabel('Trip Round')
plt.ylabel('Counts')
plt.title('Most Trips in Bikeshare');


# #### Which ages share bikes the most?

# In[26]:


plt.hist(data = df, x = 'member_birth_year', bins = 10);
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title("Ages Histogram");


# Looks like most of bikesharers are of age 30 whereas our data set is a bit skewed 

# #### What are the peak times of bikeshare?

# In[27]:


sb.countplot(data = df, x = df.start_time.dt.hour, color =(0.31,0.46,0.7));
plt.title("Peak Times");


# looks life we are dealing peak times on 7-9 am and on 5 pm .. probably its the go to work and return times

# ### Bivariante Exploration

# #### Who're the most subscribers?

# In[28]:


sb.countplot(data = df, x = 'member_gender', hue = 'user_type', palette = 'Reds');
plt.title('Simple Gender-Subscription Relationship');


# Since most bikesharers are males so it was expected to see most subscribers as males as we see in this plot

# In[29]:


plt.figure(figsize=(15,5))
sb.countplot(data = df, x = df.start_time.dt.hour , hue = 'member_gender', palette = 'Blues');


# As we can see up here, there is no difference between both males and females peak sharing times

# #### Is bikeshare over all trip affected by duration?

# In[30]:


plt.figure(figsize=(10,10))
plt.title('Bikeshare for all ride effect on Duration')
sb.countplot(data = df, x = df.duration_class , hue = 'bike_share_for_all_trip', palette = 'Blues');


# Looks like Duration affects bikeshare as duration increases the bikeshare tend not to be used the whole trip while duration decreases the probability of using bikeshare for whole trip increases 

# #### Is age a factor affecting share duration?

# In[31]:


plt.figure(figsize=(20,5));
plt.title("Age-Duration Relationship");
sb.regplot(data=df, x=df.member_birth_year, y=df.duration_sec, line_kws={'color':'r'});


# So here it appears like there's a very weak relation between age and duration as so duration don't usually increase as age increases

# ### Multivariante Exploration

# #### Are subscriptions affected by either of gender or age?
# #### Is there any factor that affects a Simpson-Paradox throughout these times?!!

# In[32]:


sb.catplot(x="member_gender", y="member_birth_year",
                hue="user_type",
                data=df, kind="violin", split=True, width = 0.5);
plt.title('Gender-Subscription-Age Relationship');


# As we can see here, though most bikeshare users are of the males and most of them too are at the age of 30, but most subscribers of age 30 are females not males which could cause a simpson paradox if it wasn't explored to see it distributed

# #### What ages affect bikeshare for all trip?

# In[33]:


sb.catplot(x="member_gender", y="member_birth_year",
                hue="bike_share_for_all_trip",
                data=df, kind="violin", split=True, width = 0.5);
plt.title("Gender-Age-Full_Bikeshare Relation");


# Also we can see here that most bike sharers under 30 are the most to use bikeshare for their whole trip whilest over thirties till 50 tend to not use it for their whole trip 

# #### what conditions are affected by subscription?

# In[34]:


sb.catplot(x="bike_share_for_all_trip", y="member_birth_year",
                hue="user_type",
                data=df, kind="violin", split=True, width = 0.5);
plt.title('Age-Subscription-BikeShareAllTrip Relationship');


# As noticed here bikeshare over all trip is affected by subscription
# 
# This also answers another question:
# #### Why some users may not use bikeshare for their whole trip?
# Looks like the subscription status is a reason for not using bike share for the whole trip besides age

# ## Observation Summary
# 1. Most crowded stations are San Francisco Caltrain Station 2 and Market St
# 2. Most trips go around Berry St 4th and Harry Bridges Plaza
# 3. Most Bikesharers are of age 30
# 4. Peak times are on morning go to work and afternoon return
# 5. Most Bikesharers are males
# 6. Age doesn't affect share duration
# 6. Although most bikesharers are males and most bikesharers are of age 30 but females are the most subscribers of age 30
# 7. Simpson's paradox could happen assuming that most bikesharers of age 30 males are subscribers while its inversed here
# 7. Since most bikesharers are males so it's expected to see most subscribers as males as we see in the dataset
# 8. Bikeshare for all trip is affected by subscription
# 9. Most bike sharers under 30 are the most to use bikeshare for their whole trip
# 10. Age doesn't really affect share duration 
# 11. Duration affects bikeshare over trip

# In[ ]:




