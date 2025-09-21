📚 Book Store Data Analytics – CodeAlpha Internship

This repository contains my work completed as part of the CodeAlpha Data Analytics Internship. The project focuses on extracting, analyzing, and visualizing data from the BooksToScrape demo website.

The internship was divided into three main tasks:

Web Scraping

Exploratory Data Analysis (EDA)

Data Visualization

📘 Task 1 – Web Scraping
📌 Project Overview

The goal of Task 1 was to perform web scraping using Python and build a clean dataset for further analysis. I selected the BooksToScrape website, which is designed for practicing scraping techniques.

🎯 Objectives

Use Python libraries (Requests, BeautifulSoup, Pandas)

Extract structured data (Title, Price, Availability, Rating, Link)

Handle multiple pages (pagination)

Clean and transform the collected data

Save dataset in CSV format

🛠️ Tools & Libraries

Python 3

Requests → Fetch HTML content

BeautifulSoup → Parse and extract data

Pandas → Store, clean, and export data

📊 Data Collected

Title – Book name

Price (£) – Converted to float

Availability – Stock status

Rating (1–5) – Extracted from star class

Link – Product URL

📂 Output File: books_list.csv with 1000 rows (50 pages)

📊 Task 2 – Exploratory Data Analysis (EDA)
📌 Project Overview

In Task 2, I explored the dataset scraped in Task 1 to uncover trends, patterns, and anomalies.

🔎 Objectives

Ask meaningful analytical questions

Explore dataset structure and variables

Identify trends, patterns, anomalies

Test hypotheses with statistics

Detect potential data quality issues

⚙️ Process Followed

Exploration: Shape, summary statistics, datatypes, duplicates

Trends: Average price, rating distribution, stock variation

Hypothesis Testing: Relation between rating and price

Anomalies: Outliers detected in high-priced books

📌 Key Insights

Dataset: 1000 rows × 5 columns, no missing values/duplicates

Avg price ~ £35 (min ~£10, max ~£55)

3-star ratings most common, 5-star books slightly more expensive

Almost all books are in stock → low variation in availability

Some outliers above £50

📂 Output File: EDA.ipynb

📈 Task 3 – Data Visualization
📌 Project Overview

Task 3 focused on creating visualizations from the EDA results to highlight patterns, relationships, and anomalies.

🎯 Objectives

Present results visually

Detect patterns, outliers, and relationships

Focus on storytelling through visuals

🛠️ Tools & Libraries

Python

Pandas → Data manipulation

Matplotlib → Static visualizations

Seaborn → Statistical plots

📈 Visualizations Created

Price Analysis

Histogram (distribution)

Boxplot (outliers)

Top 10 Most Expensive Books (bar chart)

Rating Analysis

Rating Counts (bar chart)

Boxplot: Price vs Rating

Average Price by Rating (bar chart)

Availability Analysis

In-stock vs Out-of-stock (bar chart)

💡 Key Insights

Most books fall between £20–£40

Higher rating ≠ higher price always

Majority of books are in stock

📂 Output File: task3_visualization.ipynb

📂 Repository Structure
📁 BookStore-Data-Analytics
│── 📄 README.md                 # Main consolidated project README (this file)
│── 📂 Task 1 - Web Scraping
│     └── scraping_code.py
│     └── task1_readme.md
│── 📂 Task 2 - EDA
│     └── eda_code.py
│     └── task2_readme.md
│── 📂 Task 3 - Visualization
│     └── visualization_code.py
│     └── task3_readme.md
│── 📄 books_list.csv            # Final dataset (1000 books)

🛠️ Tech Stack

Python 3

BeautifulSoup, Requests → Web Scraping

Pandas, NumPy → EDA

Matplotlib, Seaborn → Data Visualization

📌 Internship Context

This project was completed as part of my Data Analytics Internship at CodeAlpha:

Task 1 → Web Scraping ✅

Task 2 → Exploratory Data Analysis ✅

Task 3 → Data Visualization ✅

✍️ Author

👤 Harish J
📍 Data Science Final-Year Student | Aspiring Data Analyst
🔗 LinkedIn : www.linkedin.com/in/harish-j-056022277| GitHub : https://github.com/Hari-710
