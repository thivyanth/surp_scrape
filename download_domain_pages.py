import os
import time
from selenium import webdriver

# List of domain URLs to scrape
domain_urls = [
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Aerospace",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=BSBE",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=C-MINDS",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Centre%20for%20Technology%20Alternatives%20for%20Rural%20Areas%20(CTARA)",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Chemical",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Civil",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Climate%20Studies",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Computer%20Science",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Earth%20Sciences",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Educational%20Technology",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Electrical",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Energy",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Environmental",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Koita%20Centre%20for%20Digital%20Health%20(KCDH)",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Mathematics",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Mechanical%20Engineering",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Metallurgy%20and%20Material%20Sciences%20(MEMS)",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Multidisciplinary",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Physics",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=School%20of%20Management%20(SOM)",
    "https://ugac-web-team-iitb.github.io/SURP--2024/main.html?domain=Systems%20and%20Control%20Engineering%20(SYSCON)"
]

# Set up Selenium WebDriver (make sure you have the appropriate WebDriver for your browser in PATH)
driver = webdriver.Chrome()

# Create a folder to store the HTML files
output_folder = "domain_pages"
os.makedirs(output_folder, exist_ok=True)

for url in domain_urls:
    print(f"Scraping URL: {url}")

    driver.get(url)
    
    # Wait for the page to load
    time.sleep(3)

    # Get the domain name from the URL
    domain_name = url.split('=')[-1].replace('%20', '_').replace('%28', '').replace('%29', '').replace(' ', '_')

    # Get the HTML content of the page
    html_content = driver.page_source

    # Save the HTML content to a file
    file_path = os.path.join(output_folder, f"{domain_name}.html")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Saved {domain_name} page to {file_path}")

# Close the browser
driver.quit()

print("All domain pages have been saved.")
