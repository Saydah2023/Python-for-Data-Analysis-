#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install sqlalchemy')


# In[31]:


#1: Connect to your database server and print its
#version

import sqlite3
print('The server version is '+ sqlite3.sqlite_version)


# In[29]:


conn = sqlite3.connect("hospitals.db")


# In[8]:


cursor = conn.cursor()


# In[49]:


query = "SELECT * from Hospital"
cursor.execute(query)


# In[50]:


results = cursor.fetchall()


# In[34]:


#2: Fetch Hospital and Doctor Information using
#hospital Id and doctor Id

hospital_id = input("Enter hospital ID")
doctor_id = input("Enter doctor ID")

query_hospital = f"SELECT * from Hospital WHERE ID={hospital_id}"
query_doctor = f"SELECT * from Doctor WHERE DocID={doctor_id}"

cursor.execute(query_hospital)
print("Detail for the selected hospital:")
for row in cursor.fetchall():
    print(row)

print("Detail for the selected doctor:")
cursor.execute(query_doctor)
for row in cursor.fetchall():
    print(row)


# In[48]:


#3: Get the list Of doctors as per the given
#specialty and salary
doc_speciality = input("Enter the speciality:")
doc_salary = input("Enter the salary:")

query_speciality = f"SELECT DocName  FROM Doctor WHERE salary='{doc_salary}' AND Speciality='{doc_speciality}'"

cursor.execute(query_speciality)
print("Details of the selected doctors:")
for row in cursor.fetchall():
    print(row)


# In[43]:


# 4: Get a list of doctors from a given hospital
hosp_id = input("Enter the Hospital ID:")

query_doc = f"SELECT DocName FROM Doctor WHERE HospitalID={hosp_id}" 

cursor.execute(query_doc)
print("The list of Doctors:")
for row in cursor.fetchall():
    print(row)


# In[54]:


#5: Update doctor experience in years
update_query = f"UPDATE Doctor SET Exp='Experience in Years'"
print(update_query)
cursor.execute(update_query)
conn.commit()


# In[45]:




