import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    race_count

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelor_count = df[df['education'] == 'Bachelors'].shape[0]
    
    percentage_bachelors = (bachelor_count/total_people) * 100
    percentage_bachelors

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_degrees = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    total_advanced = len(advanced_degrees)
    more_than_50k = advanced_degrees[advanced_degrees['salary'] == '>50K'].shape[0]

    percentage_above_50K = (more_than_50k / total_advanced) * 100 if total_advanced > 0 else 0
    percentage_above_50K

    # What percentage of people without advanced education make more than 50K?
    non_advanced_degrees = df[~df['education'].isin(["Bachelor's", "Master's", "Doctorate"])]
    total_non_advanced = len(non_advanced_degrees)
    more_than_50K = non_advanced_degrees[non_advanced_degrees['salary'] == '>50K'].shape[0]

    percentage_above_50K = (more_than_50K / total_non_advanced) * 100 if total_non_advanced > 0 else 0
    percentage_above_50K

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(["Bachelor's", "Master's", "Doctorate"])]
    lower_education = df[~df['education'].isin(["Bachelor's", "Master's", "Doctorate"])]

    # percentage with salary >50K
    higher_education = df[df['education'].isin(["Bachelor's", "Master's", "Doctorate"])]
    total_higher_education = len(higher_education)
    higher_education_rich_count = higher_education[higher_education['salary'] == '>50K'].shape[0]
    higher_education_rich = (higher_education_rich_count / total_higher_education) * 100 if total_higher_education > 0 else 0

    lower_education = df[~df['education'].isin(["Bachelor's", "Master's", "Doctorate"])]
    total_lower_education = len(lower_education)
    lower_education_rich_count = lower_education[lower_education['salary'] == '>50K'].shape[0]
    lower_education_rich = (lower_education_rich_count / total_lower_education) * 100 if total_lower_education > 0 else 0

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]

    min_min_workers = len(min_workers)
    rich_count = min_workers[min_workers['salary'] == '>50K'].shape[0]
    rich_percentage = (rich_count / min_min_workers) * 100 if min_min_workers > 0 else 0

    # What country has the highest percentage of people that earn >50K?
    rich_counts = df[df['salary'] == '>50K'].groupby('native-country').size()

    total_counts = df.groupby('native-country').size()

    rich_percentage = (rich_counts / total_counts) * 100

    highest_earning_country = rich_percentage.idxmax()
    highest_earning_country_percentage = rich_percentage.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    top_IN_occupation = india_high_earners['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
