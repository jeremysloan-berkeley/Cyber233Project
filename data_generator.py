import random
import pandas as pd
import numpy as np

class DataGenerator:
    @staticmethod
    def generate(num_records, csv_file = None):
        # Categories
        countries = ['United States', 'Canada', 'Mexico', 'India', 'Germany', 'China', 'Australia']
        genders = ['Male', 'Female', 'Non-Binary']
        employment_status = ['Unemployed', 'Part-Time', 'Full-Time', 'Self-Employed']

        # Generate synthetic data
        data = {
            "Age": [random.randint(18, 80) for _ in range(num_records)],
            "Country of Birth": [random.choice(countries) for _ in range(num_records)],
            "Gender": [random.choice(genders) for _ in range(num_records)],
            "Employment Status": [random.choice(employment_status) for _ in range(num_records)]
        }

        drinks_per_day = []
        for i in range(num_records):
            scale = DataGenerator.get_random_num_scale(data['Age'][i], data['Gender'][i], data['Employment Status'][i])
            drinks_per_day.append(round(np.random.exponential(scale=scale), 1))

        data["Average Drinks per Day"] = drinks_per_day

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Save to CSV (optional)
        if csv_file is not None:
            df.to_csv(csv_file, index=False)
            print(f"Created {csv_file}")

        return df

    @staticmethod
    def get_random_num_scale(age, gender, empl_stat):
        scale = 1.5

        scale += DataGenerator.get_age_adjustment(age)
        scale += DataGenerator.get_gender_adjustment(gender)
        scale += DataGenerator.get_empl_stat_adjustment(empl_stat)

        return scale

    @staticmethod
    def get_age_adjustment(age):
        if 30 <= age <= 39:
            return 1.0

        return 0.0

    @staticmethod
    def get_gender_adjustment(gender):
        if gender == 'Male':
            return 1.0

        return 0.0

    @staticmethod
    def get_empl_stat_adjustment(empl_stat):
        if empl_stat == 'Unemployed':
            return 1.0

        return 0.0
