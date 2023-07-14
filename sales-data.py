#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("fct_invoice.csv")

df.head()


# In[4]:


json_df = pd.read_json("dim_customer.json")

json_df.head()


# # Easy

# 1. How many unique customers are in the dataset?

# In[5]:


result=len(df["customer_id"].unique())

print('There are',result, 'unique customers in the dataset')


# 2. What are the different categories of products available? How many unique categories are there?

# In[6]:


# diff categories available
df["category"].unique()


# In[7]:


# no. of unique categories
unique_no=len(df["category"].unique())

print('There are', unique_no,'unique categories in the data set')


# 3. Which payment method is the most popular? How many times was it used?

# In[8]:


most_pop=df["payment_method"].value_counts()
print(most_pop)


# In[9]:


print("The most popular method used is Cash and was used 44447 times")


# # Medium

# 1. What are the three most popular categories, by total sales?

# In[10]:


#step 01:
df["Total"] =df["quantity"]*df["price"]

df.head()


# In[11]:


#step 02:
df.groupby("category")["Total"].sum()


# In[12]:


#step 03
print('It has been found that the three most popular categories in terms of total sales are books, then clothing and cosmetics')


# 2. What are the total sales attributed to customers over the age of 45?

# In[13]:


#step 01:
new_df = df.merge(json_df, how="left", left_on = 'customer_id', right_on = 'id')

new_df.head()


# In[14]:


#step 02:
filtered_df= new_df[new_df['age'] >= 45]
filtered_df['Total'].sum()


# The total sales attributed to customers over the age of 45 is php 84,307,291.82

# 3. How is the data distributed across different invoice dates? Are there any seasonal trends or patterns? (Use a graph for this.)

# In[21]:


import matplotlib.pyplot as plt


# In[22]:


df['invoice_date']= pd.to_datetime(df['invoice_date'])
df['month'] = df['invoice_date'].dt.month
invoice_counts = df['month'].value_counts().sort_index()


# In[23]:


plt.plot(invoice_counts.index, invoice_counts.values, marker='o', linestyle='-', color='blue')

# Set labels and title
plt.xlabel('Month')
plt.ylabel('Invoice Count')
plt.title('Distribution of Invoices by Month')

# Display the graph
plt.show()


# In[24]:


df['invoice_date']= pd.to_datetime(df['invoice_date'])
df['year'] = df['invoice_date'].dt.year
invoice_counts = df['year'].value_counts().sort_index()

df.head(15)


# In[25]:


plt.plot(invoice_counts.index, invoice_counts.values, marker='o', linestyle='-', color='red')


plt.xlabel('Year')
plt.ylabel('Invoice Count')
plt.title('Distribution of Invoices by Year')


plt.show()


# # Hard

# 1. Create a pivot table showing the breakdown of sales across these dimensions, in this order: category, decade age range (e.g., 10-19, 20-29, and so forth).

# In[26]:


new_df.head()


# In[27]:


new_df['decade_age_range'] = new_df['age'] // 10 * 10

new_df.head()


# In[46]:


pivot1 = pd.pivot_table(new_df, values='Total', index='category', columns='decade_age_range', aggfunc=sum)
print(pivot1)

