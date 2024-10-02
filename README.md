# Stock Price Analysis

A project that performs stock price analysis using Python, AWS services, and Apache Kafka. The data is scraped from the web and stored in an S3 bucket, with AWS Glue handling ETL operations. Data is then queried using Amazon Athena and visualized through AWS QuickSight.

## Table of Contents
- [Features](#features)
- [Architecture Diagram](#architecture-diagram)
- [Installation](#installation)

  
## Features
Scrape real-time stock prices from the web.
Store stock data in AWS S3 for long-term storage.
Send stock data messages to Apache Kafka for real-time streaming and further analysis.
Technologies
Python: Used for web scraping (BeautifulSoup).
AWS S3: For storing scraped data.
Apache Kafka: For streaming and storing data messages.
BeautifulSoup: For scraping stock price data from the web.

## Architecture Diagram
![Architecture Diagram](https://github.com/shahdarshil123/stock_DEP/blob/master/Stock%20Data%20Pipeline.png)

## Installation

### Prerequisites

Ensure the following are installed and set up:
- Python 3.8+
- AWS CLI configured with appropriate permissions for S3, Glue, Athena
- Apache Kafka
- Kafka Python package (`kafka-python`)
- BeautifulSoup (`bs4`)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shahdarshil123/stock_DEP.git
   
2. **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Set up AWS credentials: Ensure your AWS credentials are configured to allow access to your S3 bucket.**
      ```bash
      aws configure

4. **Start Apache Kafka: Follow the instructions from the Apache Kafka Documentation to start Kafka services.**

5. **Run the web scraping script: This script collects stock data and stores it in S3 and Kafka.**
     ```bash
      python web_scraper.py
6. **Check Kafka topics: Verify that the data messages are being stored in the Kafka topic.**
    ```bash
    kafka-console-consumer --topic stock-prices --bootstrap-server localhost:9092 --from-beginning

7. **Create AWS Glue Crawler:** Use AWS Glue to crawl the data stored in the S3 bucket and create a metadata catalog.

8. **ETL Process using Glue:** Set up an ETL job in AWS Glue to process the data from S3 and make it queryable in Athena.

9. **Query Data using Amazon Athena:** Use Athena to run SQL queries on the processed data



