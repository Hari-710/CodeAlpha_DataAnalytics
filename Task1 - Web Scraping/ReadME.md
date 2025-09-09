📘 Task 1 – Web Scraping (CodeAlpha Internship)
📌 Project Overview

This project was completed as part of my Data Analytics Internship at CodeAlpha.
The goal of Task 1 was to perform web scraping using Python and build a clean dataset for further analysis in the next tasks (EDA & Visualization).

I selected the BooksToScrape demo website, which is specifically designed for practicing scraping techniques.

🎯 Objectives

Use Python libraries (Requests, BeautifulSoup, Pandas)

Extract structured data from a website

Handle multiple pages (pagination)

Clean and transform the collected data

Save the dataset in CSV format

🛠️ Tools & Libraries

Python 3

Requests → Fetch HTML content

BeautifulSoup (bs4) → Parse and extract data

Pandas → Store, clean, and export data

📊 Data Collected

From each book, the following details were scraped:

Title – Book name

Price (£) – Converted to numeric (float)

Availability – Stock status

Rating (1–5) – Converted from star class → numeric scale

Link – Direct product URL

📂 Dataset

books_list.csv → Contains 1000 rows (all 50 pages from the website)

Example row:

Title	Price (£)	Availability	Rating	Link
A Light in the Attic	51.77	In stock	3	https://...
Sapiens: A Brief History...	54.23	In stock	5	https://...

🚀 How It Works

Loop through all 50 pages of books.toscrape.com.

Extract details from each book card.

Clean and transform:

Price → float (removed £ sign)

Rating → numeric scale (1–5)

Append data into a Pandas DataFrame.

Export final dataset to CSV.

📌 Usage

Clone the repo and run:

python app.py


The output will be saved as books_list.csv.

📎 Internship Context

This project is Task 1 of 3 in the CodeAlpha Data Analytics Internship:

Web Scraping ✅

Exploratory Data Analysis (EDA) 🔜

Data Visualization 🔜

📢 Credits

Internship by CodeAlpha

Practice website: Books to Scrape
