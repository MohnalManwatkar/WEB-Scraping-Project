# WEB-Scraping-Project

Scraping Top Repositories for Topics on GitHub
Introduction:

1) Introduction about web scraping

- Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser.
2) Introduction about GitHub and the problem statement

- GitHub is one of the largest code hosting platforms in the world, with millions of repositories and topics. As a data scientist or a business analyst, it is essential to keep track of the latest trends and topics in the software development industry. Web scraping the GitHub website for the top topics and their corresponding repositories can provide valuable insights into the current state of the industry.
- The problem at hand is to design and implement a web scraping project that can extract the top topics on GitHub along with the corresponding repositories. Once the data has been collected, it should be cleaned, transformed, and stored in a format that can be easily analyzed and visualized.
3) Tools :

- Python
- Requests
- BeautifulSoup
- Pandas
- os
​
Pick a website and describe your objective
Browse through different sites and pick on to scrape. Check the "Project Ideas" section for inspiration.
Identify the information you'd like to scrape from the site. Decide the format of the output CSV file.
Outline :
- we are going to scrape https://github.com/topics
- we will get a list of topics. For each topic, we will gettopic title, topic page URL and ttopic disciption
- For each ttopic, we will get the top 25 repositories in the topic from the topic page
- For each repository, we will grap the repo name, username, stars and repo url
- for each topic we will create csv owing formatefilein the following

  Repo Name, Username, Starts, Repo URL
  three.js,mrdoob,69700,http://github.com/mrdoob/three.js
  libgdx,libgdx,18300,http://github.com/libgdx/libgdx
Scrape the list of topics from GitHub
- use requests to download the page
- use BS4 to parse and extract information
- convert to a pandas dataframe
3) Tools :

- Python
- Requests
- BeautifulSoup
- Pandas
- os
