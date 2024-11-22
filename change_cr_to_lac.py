# Let's first load the CSV file and inspect its contents to understand the structure and the column with prices.
import pandas as pd

# Load the CSV file
file_path = 'cleaned_house_prices.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
df.head()

# Function to convert Cr to Lac
def convert_to_lac(amount):
    amount = amount.strip()  # Remove any extra spaces
    if 'Cr' in amount:
        # Convert the value from Cr to Lac
        amount_value = float(amount.replace('Cr', '').strip()) * 100
    elif 'Lac' in amount:
        # If it's already in Lac, just return the value as float
        amount_value = float(amount.replace('Lac', '').strip())
    else:
        # If the format is unrecognized, return it as is
        return amount
    return amount_value

# Apply the function to the "Amount(in rupees)" column
df['Amount(in Lac)'] = df['Amount(in rupees)'].apply(convert_to_lac)

# Display the updated dataframe with the new "Amount(in Lac)" column
df[['Amount(in rupees)', 'Amount(in Lac)']].head()
# Step 4: Save the preprocessed data to a new file
output_file_path = 'updated_house_prices.csv'
df.to_csv(output_file_path, index=False)

output_file_path