📊 Exploratory Data Analysis (EDA) – CodeAlpha Internship
📌 Project Overview

This project is part of the CodeAlpha Data Analytics Internship.
Task 2: Exploratory Data Analysis (EDA) focuses on understanding, cleaning, and analyzing a dataset to uncover trends, patterns, and potential data issues.

For this task, I used the BooksToScrape dataset (1000 books, scraped in Task 1).
The dataset contains the following features:

Title → Book title

Price → Price of the book (£)

Availability → Stock status

Rating → Book rating (1–5 stars)

Link → Product page URL

🔎 Task Objectives

According to the CodeAlpha internship instructions, the goals of EDA are:

Ask meaningful questions before analysis

Explore the dataset structure, variables, and data types

Identify trends, patterns, and anomalies

Test hypotheses and validate assumptions using statistics

Detect potential data issues for further analysis

⚙️ Process Followed
1. Ask Questions

What is the average book price?

Which ratings are most common?

Do higher-rated books cost more?

How many books are in stock vs out of stock?

Are there any unusually expensive or cheap books?

2. Explore Structure

Dataset shape, column info, and summary statistics

Checked for duplicates and missing values (none found)

Verified data types

3. Trends & Anomalies

Price range identified (min, max, average)

Ratings distribution analyzed

Availability checked for variation

Outliers detected in pricing

4. Hypothesis Testing

Higher ratings → higher average price

Availability vs price comparison

Correlation between title length and price

5. Data Issues Detected

Availability column has low variation (mostly “In stock”)

Ratings distribution slightly imbalanced (3-star most common)

Outliers present in book prices above £50

📌 Key Insights

Dataset has 1000 rows × 5 columns, clean with no missing values or duplicates.

Average book price: ~£35 (min £10, max ~£55).

3-star ratings are the most common, while 5-star books have slightly higher average prices.

Almost all books are in stock, showing low variation in availability.

A few books priced above £50 act as outliers.

Title length has a very weak correlation with price.

📂 Files Included

EDA.ipynb → Jupyter Notebook with full EDA process

books_list.csv → Dataset (scraped in Task 1)

README.md → Project documentation (this file)

🚀 Next Steps

Task 3: Data Visualization → Convert insights into meaningful visualizations using Matplotlib/Seaborn.

🛠️ Tech Stack

Python

Pandas for data handling

NumPy for calculations

Jupyter Notebook for analysis

📌 Author

👤 Harish J
📍 Data Science Final-Year Student | Aspiring Data Analyst
🔗 www.linkedin.com/in/harish-j-056022277| https://github.com/Hari-710
