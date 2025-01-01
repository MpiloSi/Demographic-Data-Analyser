# Demographic Data Analyzer

This project is a Demographic Data Analyzer that uses Python and Pandas to analyze demographic data extracted from the 1994 Census database. The goal of this project is to answer various demographic-related questions by processing and analyzing the dataset.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Features

- Analyze demographic data using Pandas.
- Calculate statistics such as:
  - Percentage of people with a Bachelor's degree.
  - Average age of men.
  - Percentage of people with advanced education earning more than $50K.
  - Minimum number of hours worked per week.
  - Most popular occupation for those earning >50K in India.
  - Highest earning country based on percentage of people earning >50K.

## Technologies Used

- Python 3.x
- Pandas library for data manipulation and analysis

## Installation

To run this project, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

git clone https://github.com/freeCodeCamp/boilerplate-demographic-data-analyzer.git
cd boilerplate-demographic-data-analyzer


### Step 2: Install Dependencies

You will need to install the Pandas library. You can do this using pip:

pip install pandas


## Usage

To use the Demographic Data Analyzer, run the `main.py` script. This script will execute the analysis and print the results to the console.

### Example Command Line Usage

1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
   python main.py


## Functionality

The main functionalities of this project include:

1. **Reading Data**: The program reads demographic data from `adult.data.csv`.
2. **Data Analysis**: It calculates various statistics based on the dataset, including:
   - The number of individuals of each race.
   - The average age of male individuals.
   - The percentage of individuals with a Bachelor's degree.
   - The percentage of individuals with advanced education earning more than $50K.
   - The percentage of individuals without advanced education earning more than $50K.
   - The minimum hours worked per week and related salary statistics.
   - The country with the highest percentage of individuals earning >50K.
