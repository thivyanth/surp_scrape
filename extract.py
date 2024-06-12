import os
import pandas as pd
from bs4 import BeautifulSoup

# Directory where the HTML files are saved
input_folder = "domain_pages"

# List to hold all project details
all_project_details = []

# Iterate over each HTML file in the folder
for filename in os.listdir(input_folder):
    if filename.endswith(".html"):
        file_path = os.path.join(input_folder, filename)
        
        # Read the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
        
        # Select all project cards
        project_cards = soup.select("#project-cards > div.col > div.card")
        print(f"Number of project cards found in {filename}: {len(project_cards)}")
        
        for card in project_cards:
            project_name = card.select_one(".card-title").text.strip()
            professor_info = card.select_one(".card-body .card-text h6:nth-child(1)").text.strip()
            uid = card.select_one(".card-body .card-text h6:nth-child(2)").text.strip()
            
            # Create a dictionary to hold project details
            project_info = {
                "Project Name": project_name,
                "Professor": professor_info,
                "UID": uid
            }
            
            # Simulate clicking the details button to get more details (modal content)
            details_button = card.select_one(".btn-primary")
            modal_id = details_button['data-bs-target']
            modal_content = soup.select_one(f"{modal_id} .modal-content")
            
            if modal_content:
                modal_text = modal_content.select_one(".modal-body table")
                if modal_text:
                    rows = modal_text.select("tr")
                    for row in rows:
                        key = row.select_one("th").text.strip()
                        value = row.select_one("td").text.strip()
                        project_info[key] = value
            
            # Append the project details to the list
            all_project_details.append(project_info)

# Create DataFrame and save to CSV
df = pd.DataFrame(all_project_details)

# Print DataFrame in a nice format
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)

# Save to CSV
output_file = "project_details.csv"
df.to_csv(output_file, index=False)

print(f"Scraping complete. Data saved to {output_file}")
