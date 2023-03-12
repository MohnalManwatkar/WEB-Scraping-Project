#!/usr/bin/env python
# coding: utf-8

# # Scraping Top Repositories for Topics on GitHub
# 
# 
# Introduction:
# 
# 1) Introduction about web scraping
# 
#     - Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser.
# 
# 
# 2) Introduction about GitHub and the problem statement
# 
#     - GitHub is one of the largest code hosting platforms in the world, with millions of repositories and topics. As a data scientist or a business analyst, it is essential to keep track of the latest trends and topics in the software development industry. Web scraping the GitHub website for the top topics and their corresponding repositories can provide valuable insights into the current state of the industry.
#     - The problem at hand is to design and implement a web scraping project that can extract the top topics on GitHub along with the corresponding repositories. Once the data has been collected, it should be cleaned, transformed, and stored in a format that can be easily analyzed and visualized.
# 
# 
# 3) Tools :
# 
#     - Python
#     - Requests
#     - BeautifulSoup
#     - Pandas
#     - os

# In[ ]:





# ### Pick a website and describe your objective
# 
# - Browse through different sites and pick on to scrape. Check the "Project Ideas" section for inspiration.
# - Identify the information you'd like to scrape from the site. Decide the format of the output CSV file.
# 

# # Outline :
#     - we are going to scrape https://github.com/topics
#     - we will get a list of topics. For each topic, we will gettopic title, topic page URL and ttopic disciption
#     - For each ttopic, we will get the top 25 repositories in the topic from the topic page
#     - For each repository, we will grap the repo name, username, stars and repo url
#     - for each topic we will create csv owing formatefilein the following
#     
#       Repo Name, Username, Starts, Repo URL
#       three.js,mrdoob,69700,http://github.com/mrdoob/three.js
#       libgdx,libgdx,18300,http://github.com/libgdx/libgdx

# ## Scrape the list of topics from GitHub
# 
#     - use requests to download the page
#     - use BS4 to parse and extract information
#     - convert to a pandas dataframe

# 3) Tools :
# 
#     - Python
#     - Requests
#     - BeautifulSoup
#     - Pandas
#     - os

# In[1]:


get_ipython().system('pip install requests --upgrade --quiet')


# In[2]:


import requests


# In[3]:


topics_url = 'https://github.com/topics'


# In[4]:


response = requests.get(topics_url)


# In[ ]:





# response status code HTTP
# - Informational responses (100 – 199)
# - Successful responses (200 – 299)
# - Redirection messages (300 – 399)
# - Client error responses (400 – 499)
# - Server error responses (500 – 599)

# In[5]:


response.status_code


# In[6]:


len(response.text)


# In[7]:


page_contents = response.text


# In[8]:


page_contents[:1000]


# In[9]:


import io
with io.open('webpage.html', "w", encoding="utf-8") as f:
    f.write(page_contents)


# In[ ]:





# ### Use Beautiful Soup to parse and extract information

# In[10]:


from bs4 import BeautifulSoup


# In[11]:


doc = BeautifulSoup(page_contents, 'html.parser')


# In[12]:


doc


# In[13]:


type(doc)


# In[14]:


p_tags = doc.find_all('p')


# In[15]:


len(p_tags)


# In[16]:


p_tags[:5]


# In[17]:


topic_title_tags = doc.find_all('p', {'class':"f3 lh-condensed mb-0 mt-1 Link--primary"})


# In[18]:


len(topic_title_tags)


# In[19]:


topic_title_tags[:5]


# In[ ]:





# In[20]:


topic_description_tags = doc.find_all('p',{'class':"f5 color-fg-muted mb-0 mt-1"})


# In[21]:


len(topic_description_tags)


# In[22]:


topic_description_tags[:5]


# In[23]:


topic_title_tags0 = topic_title_tags[0]


# In[24]:


topic_title_tags0.parent


# In[ ]:





# In[25]:


topic_link_tags = doc.find_all('a', {'class':"no-underline flex-1 d-flex flex-column"})


# In[26]:


topic_link_tags


# In[27]:


len(topic_link_tags)


# In[28]:


topic_link_tags[0]['href']


# In[29]:


topic0_url = "http://github.com" + topic_link_tags[0]['href']
print(topic0_url)


# In[30]:


topic_title_tags[0].text


# In[31]:


topic_title_tags[1].text


# In[32]:


topic_title_tags[2].text


# In[ ]:





# In[33]:


topic_titles = []

for tag in topic_title_tags:
    topic_titles.append(tag.text)
    
print(topic_titles)


# In[ ]:





# In[34]:


topic_description = []

for i in topic_description_tags:
    topic_description.append(i.text.strip())
    
print(topic_description[:5])


# In[35]:


topic_urls = []
base_url = 'http://github.com'

for i in topic_link_tags:
    topic_urls.append(base_url + i['href'])
    
print(topic_urls)


# In[36]:


import pandas as pd


# In[37]:


# to convert this dataset / information into tanular formate 

topic_dictionary = {
    'title':topic_titles,
    'description':topic_description,
    'url':topic_urls
}


# In[38]:


topic_dictionary


# In[39]:


topics_df = pd.DataFrame(topic_dictionary)


# In[40]:


topics_df


# In[ ]:





# ### Create CSV file(s) with the extracted information

# In[41]:


topics_df.to_csv('git_topics.csv', index = None)


# In[ ]:





# # Getting information out of a topic page

# In[42]:


topic_page_url = topic_urls[0]
topic_page_url


# In[43]:


response = requests.get(topic_page_url)


# In[53]:


response.status_code


# In[45]:


len(response.text)


# In[46]:


topic_doc2 = BeautifulSoup(response.text, 'html.parser')


# In[47]:


repo_tags = topic_doc2.find_all('h3', {'class':"f3 color-fg-muted text-normal lh-condensed"})


# In[48]:


len(repo_tags)


# In[49]:


repo_tags


# In[50]:


a_tags = repo_tags[0].find_all('a')


# In[51]:


a_tags[0]


# In[52]:


a_tags[0].text.strip()


# In[54]:


a_tags[1].text.strip()


# In[55]:


a_tags[1]['href']


# In[56]:


base_url = 'http://github.com'
repo_url = base_url + a_tags[1]['href']
print(repo_url)


# In[57]:


star_tags = topic_doc2.find_all('span',{'class':"Counter js-social-count"})


# In[58]:


len(star_tags)


# In[59]:


star_tags[0]


# In[60]:


star_tags[0].text.strip()[:-1]


# In[61]:


def convert_star_tags(stars_str):
    stars_str = stars_str.strip()
    if stars_str[-1] == 'k' :
        return int(float(stars_str[:-1])*1000)
    return int(stars_str)


# In[62]:


print('stars:')
convert_star_tags(star_tags[0].text.strip())


# In[ ]:





# In[63]:


def get_repo_info(h3_tag, star_tag):
    #return all the required info about a repository
    a_tags = h3_tag.find_all('a')
    username = a_tags[0].text.strip()
    repo_name = a_tags[1].text.strip()
    stars = convert_star_tags(star_tags[0].text.strip())
    repo_url = base_url + a_tags[1]['href']
    return username, repo_name, stars, repo_url


# In[64]:


get_repo_info(repo_tags[0], star_tags[0])


# In[65]:


star_tags[0].text


# In[66]:


topic_repos_dictionary = {
    'username':[],
    'repo_name':[],
    'stars':[],
    'repo_url':[]
}

for i in range (len(repo_tags)):
    repo_info = get_repo_info(repo_tags[i], star_tags[i])
    topic_repos_dictionary['username'].append(repo_info[0])
    topic_repos_dictionary['repo_name'].append(repo_info[1])
    topic_repos_dictionary['stars'].append(repo_info[2])
    topic_repos_dictionary['repo_url'].append(repo_info[3])


# In[67]:


topic_repos_dictionary


# In[68]:


topic_repos_df = pd.DataFrame(topic_repos_dictionary)


# In[69]:


topic_repos_df


# In[ ]:





# In[ ]:





# 
# 
# # final code

# In[70]:


def get_topic_page(topic_urls):
    
    #Download the page
    response = requests.get(topic_urls)
    
    #check the successful response
    if response.status_code !=200:
        raise Exception('Failed to load page {}'.format(topic_urls))
        
    #parse using BeautifulSoup
    topic_doc = BeautifulSoup(response.text, 'html.parser')
    
    return topic_doc
 
    ######################################################################################

def get_repo_info(h3_tag, star_tag):
    #return all the required info about a repository
    a_tags = h3_tag.find_all('a')
    username = a_tags[0].text.strip()
    repo_name = a_tags[1].text.strip()
    stars = convert_star_tags(star_tags[0].text.strip())
    repo_url = base_url + a_tags[1]['href']
    return username, repo_name, stars, repo_url
   
    ########################################################################################

def get_topic_repos(topic_doc):
      
    #get h3 tags contaning repo title, repo URL and username
    repo_tags = topic_doc.find_all('h3', {'class':"f3 color-fg-muted text-normal lh-condensed"})
    
    #get star tags
    star_tags = topic_doc.find_all('span',{'class':"Counter js-social-count"})
    
    ###########################################################################################
    
    topic_repos_dictionary = {
        'username':[],
        'repo_name':[],
        'stars':[],
        'repo_url':[]
    }
    
    #get repo info
    for i in range (len(repo_tags)):
        repo_info = get_repo_info(repo_tags[i], star_tags[i])
        topic_repos_dictionary['username'].append(repo_info[0])
        topic_repos_dictionary['repo_name'].append(repo_info[1])
        topic_repos_dictionary['stars'].append(repo_info[2])
        topic_repos_dictionary['repo_url'].append(repo_info[3])
        
    return pd.DataFrame(topic_repos_dictionary)
    
    ###########################################################################################

# if the fille is exists then skip it otherwise download it  

'''def scrape_topic(topic_url, topic_name):
    topic_df = get_topic_repos(get_topic_page(topic_url))
    topic_df.to_csv(topic_name + '.csv', index = None)'''



import os

def scrape_topic(topic_url, path):
    if os.path.exists(path):
        print("The file {} already exists. Skipping...".format(path))
        return
    topic_df = get_topic_repos(get_topic_page(topic_url))
    topic_df.to_csv( path, index = None)
    


# In[ ]:





# In[71]:


url4 = topic_urls[4]
print(url4)


# In[72]:


topic4_doc = get_topic_page(url4)


# In[73]:


topic4_repos = get_topic_repos(topic4_doc)


# In[74]:


topic4_repos


# In[ ]:





# In[75]:


# we can do this in one line code 

get_topic_repos(get_topic_page(topic_urls[5]))


# In[76]:


get_topic_repos(get_topic_page(topic_urls[6]))


# In[ ]:





# 
# write a single function to:
#  1. Get the list of topics from the topics page
#  2. Get the list of top repos from the individual topic pages
#  3. For each topic, create a CSV of the top repos for the topic
#  

# In[77]:


def get_topic_titles(doc):
    topic_title_tags = doc.find_all('p', {'class':"f3 lh-condensed mb-0 mt-1 Link--primary"})
    topic_titles = []
    for tag in topic_title_tags:
        topic_titles.append(tag.text)
    return topic_titles

##########################################################################################################################
    
def get_topic_description(doc):
    topic_description_tags = doc.find_all('p',{'class':"f5 color-fg-muted mb-0 mt-1"})
    
    topic_description = []
    for i in topic_description_tags:
        topic_description.append(i.text.strip())
    return topic_description

###########################################################################################################################

def get_topic_url(doc):    
    topic_link_tags = doc.find_all('a', {'class':"no-underline flex-1 d-flex flex-column"})
    
    topic_urls = []
    base_url = 'http://github.com'

    for i in topic_link_tags:
        topic_urls.append(base_url + i['href'])

    return topic_urls  
        
#############################################################################################################################        
   
def scrape_topics():
    
    topics_url = 'https://github.com/topics'
    response = requests.get(topics_url)
    
    #check the successful response
    if response.status_code !=200:
        raise Exception('Failed to load page {}'.format(topics_url))
        
    topics_dict = {
        'title' : get_topic_titles(doc),
        'description' : get_topic_description(doc),
        'url' : get_topic_url(doc)
        
    }
        
    return pd.DataFrame(topics_dict)
    
    


# In[ ]:





# In[78]:


scrape_topics()


# In[79]:


for index, row in topics_df.iterrows():
    print(row['url'],' - ',row['title'])


# In[ ]:





# In[80]:


def scrape_topics_repos():
    print('Scrping list of topics')
    topics_df = scrape_topics()
    for index, row in topics_df.iterrows():
        print('Scraping top repositories for "{}"' .format(row['title']))
        scrape_topic(row['url'], row['title'])


# In[81]:


scrape_topics_repos()


# In[82]:


#  Create new folder and store the data

def scrape_topics_repos():
    print('Scrping list of topics')
    topics_df = scrape_topics()
    
    os.makedirs('GitHub_Web_Scraping_Project', exist_ok=True)
    
    for index, row in topics_df.iterrows():
        print('Scraping top repositories for "{}"' .format(row['title']))
        scrape_topic(row['url'], 'GitHub_Web_Scraping_Project/{}.csv'.format(row['title']))


# # 

# Let's run it to scrape the top repos for all the topics on the first page of http://github.com/topics

# In[83]:


scrape_topics_repos()


# # 

# ########################################################################################################################
# we can check that the CSVs were created properly

# In[ ]:




