#!/usr/bin/env python
# coding: utf-8

# ## Olympic dataset analysis
# 

# In[9]:

import streamlit as st
import pandas as pd
txns=pd.read_csv("C:/Users/mammu/Downloads/transaction_data.csv/olympic_data.csv",sep="\t")
txns.columns = ["ATHLETE","AGE","COUNTRY", "YEAR", "DATE", "TYPE_OF_SPORT", "GOLD_MEDAL", "SILVER_MEDAL", "BRONZE_MEDAL","TOTAL_NO_OF_MEDALS"]
txns.head()


# How many total medals (Gold + Silver + Bronze) did each athlete win?
# 
# Which athlete won the highest number of gold medals?
# 
# Which country has won the most total medals?
# 
# What is the total medal count per year?
# 
# How many medals has each country won in each sport?
# 
# Which sport contributes the most medals overall?
# 
# Which athlete has shown consistent performance across multiple Olympics?
# 
# What is the total number of medals won by each country over all years?
# 
# What percentage of total medals were gold, silver, and bronze?
# 
# What is the average age of medal winners?
# 
# Is there a relationship between athlete age and the number of medals won?
# 
# Which year had the highest number of gold medals awarded?
# 
# How does the medal count of the United States compare with other countries?
# 
# Which athletes have won medals in multiple Olympic years?
# 
# What is the total number of medals per sport category?
# 
# Which country dominates in swimming events?
# 
# Which athletes have won the same number of medals as Michael Phelps?
# 
# How many total medals were won in each Olympic year?
# 
# Which countries improved their performance in consecutive Olympic Games?
# 
# What is the average number of medals per athlete?
# 
# How many athletes won at least one gold medal?
# 
# Which sport has the most diverse set of medal-winning countries?
# 
# What is the medal-to-athlete ratio for each country?
# 
# Which country has the highest average gold medal count per year?
# 
# What is the proportion of gold medals to total medals for each country?
# 
# How many athletes participated for each country?
# 
# Which athletes are top performers by total medal count?
# 
# What is the trend of total medals for each sport over time?
# 
# How many medals did each country win in a particular year (e.g., 2012)?
# 
# Which country shows the greatest improvement in medal count compared to previous Olympics?
# 
# How many total medals were won by female vs. male athletes (if gender data is added)?
# 
# How old was the youngest and oldest medal winner?
# 
# Which athletes won only bronze medals?
# 
# Which athletes won medals in multiple sports?
# 
# How do gold medal counts vary across countries and years?

# In[10]:


# 1. Total medals by athlete
txns = txns.round({'GOLD_MEDAL':0, 'SILVER_MEDAL':0, 'BRONZE_MEDAL':0, 'Total':0})
txns.head()
b=(txns.groupby('ATHLETE')['TOTAL_NO_OF_MEDALS'].sum().sort_values(ascending=False))
b=b.reset_index()
b


# In[11]:


# 2. Athlete with highest number of gold medals
txns.groupby('ATHLETE')['GOLD_MEDAL'].sum().idxmax()


# In[12]:


#3.Country with the most total medals
c=txns.groupby('COUNTRY')['TOTAL_NO_OF_MEDALS'].sum().sort_values(ascending=False)
c=c.reset_index()
c


# In[13]:


#4.Total medal count per year
t=(txns.groupby('YEAR')['TOTAL_NO_OF_MEDALS'].sum().sort_values(ascending=False))
t=t.reset_index()
t


# In[14]:


#5.Medals won by each country in each sport
pd.pivot_table(txns, values='TOTAL_NO_OF_MEDALS', index='COUNTRY', columns='TYPE_OF_SPORT', aggfunc='sum', fill_value=0)


# In[15]:


#6.Sport contributing the most medals overall
b=txns.groupby('TYPE_OF_SPORT')['TOTAL_NO_OF_MEDALS'].sum().sort_values(ascending=False)
b=b.reset_index()
b.head()


# In[16]:


#7.Athletes who participated in multiple Olympic years
b=txns.groupby('ATHLETE')['YEAR'].nunique()[lambda x: x > 1]
b=b.reset_index()
b.head()


# In[17]:


#8.Total medal count by country
txns.groupby('COUNTRY')['TOTAL_NO_OF_MEDALS'].sum().sort_values(ascending=False)


# In[18]:


#9.Percentage of gold, silver, and bronze medals
medal_sum = txns[['GOLD_MEDAL','SILVER_MEDAL','BRONZE_MEDAL']].sum()
(medal_sum / medal_sum.sum()) * 100


# In[19]:


#10.Average age of medal winners
medal_winners = txns[(txns['GOLD_MEDAL'] > 0) | (txns['SILVER_MEDAL'] > 0) | (txns['BRONZE_MEDAL'] > 0)]
average_age = medal_winners['AGE'].mean()
print("Average age of medal winners:", average_age)


# In[20]:


#11.Relationship between athlete age and number of medals
relation = txns['AGE'].corr(txns['TOTAL_NO_OF_MEDALS'])
relation


# In[21]:


#12.Year with highest number of gold medals
txns.groupby('YEAR')['GOLD_MEDAL'].sum().idxmax()


# In[22]:


#13.Compare medal count of United States vs others
s=txns.groupby('COUNTRY')['TOTAL_NO_OF_MEDALS'].sum().sort_values(ascending=False)
s=s.reset_index()
s


# In[24]:


#14 Athletes who won medals in multiple Olympic years
multi_year_athletes = txns.groupby('ATHLETE')['YEAR'].nunique()
multi_year_athletes = multi_year_athletes[multi_year_athletes > 1]
multi_year_athletes.reset_index()


# In[25]:


#15 Total number of medals per sport category
medals = txns.groupby('TYPE_OF_SPORT')['TOTAL_NO_OF_MEDALS'].sum().reset_index()
medals


# In[26]:


#16 which country dominates in swimming events
swim = txns[txns['TYPE_OF_SPORT'] == 'Swimming']
print(swim.groupby('COUNTRY')['TOTAL_NO_OF_MEDALS'].sum().sort_values(ascending=False).head(1))


# In[27]:


#17 athletes with the same total number of medals as michael
michael = txns[txns['ATHLETE'] == 'Michael Phelps']['TOTAL_NO_OF_MEDALS'].sum()
same_as_michael = txns.groupby('ATHLETE')['TOTAL_NO_OF_MEDALS'].sum()
same_as_michael = same_as_michael[same_as_michael == michael]
same_as_michael


# In[28]:


#18 Total medals won in each Olympic year
total_medals = txns.groupby('YEAR')['TOTAL_NO_OF_MEDALS'].sum()
total_medals


# In[29]:


#19
country_perf = txns.groupby(['COUNTRY', 'YEAR'])['TOTAL_NO_OF_MEDALS'].sum().reset_index()
country_perf['Improved'] = country_perf.groupby('COUNTRY')['TOTAL_NO_OF_MEDALS'].diff() > 0
improved_countries = country_perf[country_perf['Improved']]['COUNTRY'].unique()
improved_countries


# In[30]:


20 #the average number of medals per athlete
average_medals = txns["TOTAL_NO_OF_MEDALS"].mean()
average_medals


# In[31]:


21 #athletes won at least one gold medal
athletes_with_gold = txns[txns["GOLD_MEDAL"] > 0]["ATHLETE"].nunique()
athletes_with_gold


# In[32]:


22 #sport has the most diverse set of medal-winning countries
country_diversity = txns.groupby("TYPE_OF_SPORT")["COUNTRY"].nunique().reset_index(name="countries")
most_diverse_sport = country_diversity.loc[country_diversity["countries"] == country_diversity["countries"].max()]
most_diverse_sport


# In[33]:


23 #the medal-to-athlete ratio for each country
country_stats = (txns.groupby("COUNTRY").agg(TOTAL_NO_OF_MEDALS=("TOTAL_NO_OF_MEDALS", "sum"),Athletes=("ATHLETE", "nunique")).reset_index())
country_stats["Medal_to_Athlete_Ratio"] = country_stats["TOTAL_NO_OF_MEDALS"] / country_stats["Athletes"]
country_stats.head(10)


# In[34]:


24 #country has the highest average gold medal count per year
txns.groupby(["COUNTRY", "YEAR"])["GOLD_MEDAL"].sum().groupby("COUNTRY").mean().idxmax()


# In[35]:


#25
gold_ratio = txns.groupby('COUNTRY')[['GOLD_MEDAL', 'TOTAL_NO_OF_MEDALS']].sum()
gold_ratio['Proportion'] = gold_ratio['GOLD_MEDAL'] / gold_ratio['TOTAL_NO_OF_MEDALS']
gold_ratio[['Proportion']]


# In[36]:


26 # athletes participated for each country
txns.groupby("COUNTRY")["ATHLETE"].nunique().sort_values(ascending=False).reset_index()


# In[37]:


# 27Filter rows where TOTAL_NO_OF_MEDALS is not null
medal_winners = txns[txns['TOTAL_NO_OF_MEDALS'].notnull()]
athlete_medals = (
    medal_winners.groupby('ATHLETE')['TOTAL_NO_OF_MEDALS']
    .sum()
    .reset_index()
)
athlete_medals.columns = ['Athlete', 'Total_Medals']
top_athletes = athlete_medals.sort_values(by='Total_Medals', ascending=False)
top_athletes.head(10)


# In[38]:


#28 What is the trend of total medals for each sport over time?
sport_trends = txns.groupby(['TYPE_OF_SPORT', 'YEAR'])['TOTAL_NO_OF_MEDALS'].sum().reset_index()
sport_trends.columns = ['Sport', 'Year', 'Total_Medals']
sport_trends.head()


# In[39]:


#29
txns_2012 = txns[txns['YEAR'] == 2012]
medals_2012 = txns_2012.groupby('COUNTRY')['TOTAL_NO_OF_MEDALS'].sum().reset_index()
medals_2012.columns = ['COUNTRY', 'Total_Medals']
medals_2012.sort_values(by='Total_Medals', ascending=False).head(10)


# In[40]:


#30
medal_counts = txns.groupby(['COUNTRY', 'YEAR'])['TOTAL_NO_OF_MEDALS'].sum().reset_index(name='Total_Medals')
medal_counts = medal_counts.sort_values(['COUNTRY', 'YEAR'])
medal_counts.head()


# In[41]:


#32
medal_winners = txns[txns['TOTAL_NO_OF_MEDALS'].notnull()]
youngest = medal_winners.loc[medal_winners['AGE'].idxmin(), ['ATHLETE', 'AGE', 'TOTAL_NO_OF_MEDALS', 'TYPE_OF_SPORT', 'YEAR']]
oldest = medal_winners.loc[medal_winners['AGE'].idxmax(), ['ATHLETE', 'AGE', 'TOTAL_NO_OF_MEDALS', 'TYPE_OF_SPORT', 'YEAR']]
medal_winners.reset_index()


# In[42]:


#33
bronze_only = txns[(txns['BRONZE_MEDAL'] > 0) & (txns['GOLD_MEDAL'] == 0) & (txns['SILVER_MEDAL'] == 0)][['ATHLETE','COUNTRY','YEAR']]
bronze_only.head()


# In[43]:


#34
multi_sport_athletes = txns.groupby('ATHLETE')['TYPE_OF_SPORT'].nunique().reset_index()
multi_sport_athletes = multi_sport_athletes[multi_sport_athletes['TYPE_OF_SPORT'] > 1]
multi_sport_athletes.head()


# In[44]:


#35
gold_trends = txns.groupby(['COUNTRY', 'YEAR'])['GOLD_MEDAL'].sum().reset_index()
gold_trends.head()


# In[ ]:





# In[ ]:







