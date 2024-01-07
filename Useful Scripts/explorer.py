import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# URL of your job site
url = 'place_your_url_here'

# List of job titles
jobs = ["Cybersecurity", "Cybersecurity Analyst", "System Administrator"]

# Creating an empty DataFrame to store the data
data = pd.DataFrame(columns=['Job Title', 'Date', 'Time', 'Region', 'Sponsor'])

# Iterating over job titles
for job in jobs:
    response = requests.get(f'{url}/search?q={job}')
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting information from the page
    for job_info in soup.find_all('div', class_='job-info'):
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        region = job_info.find('span', class_='region').text.strip()
        sponsor = 'Yes' if job_info.find('span', class_='sponsor') else 'No'

        # Adding data to the DataFrame
        data = data.append({'Job Title': job, 'Date': date_time.split()[0], 'Time': date_time.split()[1],
                            'Region': region, 'Sponsor': sponsor}, ignore_index=True)

# Saving the data to an Excel file
data.to_excel('job_data.xlsx', index=False)

# Displaying the data
print(data)

# Creating a chart
chart = data.groupby(['Date']).size().plot(kind='bar', title='Jobs per Date')
