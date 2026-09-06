import pandas as pd
import random
import os

# Path to your dataset
data_path = os.path.join("data", "medicine_dataset.csv")

# Load dataset
df = pd.read_csv(data_path)

# Function to simulate stock values
def stock_by_type(row):
    dosage_form = str(row.get('Dosage_Form', '')).lower()
    if "tablet" in dosage_form:
        return random.randint(100, 500)
    elif "capsule" in dosage_form:
        return random.randint(50, 300)
    elif "syrup" in dosage_form:
        return random.randint(20, 100)
    else:
        return random.randint(5, 50)

# Apply stock generation
df['Stock'] = df.apply(stock_by_type, axis=1)

# Save to a new file inside /data
output_path = os.path.join("data", "medicine_dataset_with_stock.csv")
df.to_csv(output_path, index=False)

print(f"✅ Created: {output_path}")
