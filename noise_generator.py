import pandas as pd
import numpy as np

class NoiseGenerator:
    @staticmethod
    def generate(df, csv_file=None):
        # Ensure 'Average Drinks per Day' is numeric
        df["Average Drinks per Day"] = pd.to_numeric(df["Average Drinks per Day"], errors="coerce").fillna(0)

        # Differential Privacy Parameters
        sensitivity = 1.0  # Sensitivity of the data
        base_epsilon = 1.0  # Epsilon for maximum noise (100% noise corresponds to base_epsilon=1.0)
        noise_levels = [i / 10 for i in range(1, 11)]  # Noise levels: 10% to 100% in increments of 10%

        # Add columns for each noise level
        for noise_level in noise_levels:
            epsilon = base_epsilon / noise_level  # Scale epsilon inversely with noise level
            column_name = f"Noisy Drinks {int(noise_level * 100)}%"
            df[column_name] = df["Average Drinks per Day"].apply(
                lambda x: NoiseGenerator.add_laplace_noise_clamped(x, epsilon, sensitivity, 0, 20)
            )

        # Save to CSV (optional)
        if csv_file is not None:
            df.to_csv(csv_file, index=False)
            print(f"Dataset with all noise levels saved as '{csv_file}'")

        return df

    # Function to add Laplace noise with clamping
    @staticmethod
    def add_laplace_noise_clamped(value, epsilon, sensitivity, lower_bound, upper_bound):
        scale = sensitivity / epsilon
        noise = np.random.laplace(0, scale)
        noisy_value = value + noise
        return np.clip(noisy_value, lower_bound, upper_bound)  # Clamp to range [lower_bound, upper_bound]


