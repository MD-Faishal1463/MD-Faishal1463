import pandas as pd

def calculate_demographic_data(print_data=True):
    # read the dataset
    df = pd.read_csv("adult.data.csv")

    # 1. number of each race
    race_count = df['race'].value_counts()

    # 2. average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. percentage with Bachelors
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. advanced education filter
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # 5. percentage with salary >50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 6. min work hours
    min_work_hours = df['hours-per-week'].min()

    # 7. rich percentage among min workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. country with highest % of >50K
    country_counts = df['native-country'].value_counts()
    country_rich = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percent = (country_rich / country_counts * 100).sort_values(ascending=False)

    highest_earning_country = country_rich_percent.index[0]
    highest_earning_country_percentage = round(country_rich_percent.iloc[0], 1)

    # 9. most popular occupation in India >50K
    india_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
        ['occupation']
        .value_counts()
    )
    top_IN_occupation = india_occupation.index[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    # return answers for testing
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
