import pandas as pd
import numpy as np

class MarketingDataETL:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def extract(self):
        self.data = pd.read_csv(self.file_path, sep=';')
        print("Data sebelum transform:")
        print(self.data)
        return self.data

    def transform(self):
        if 'purchase_date' in self.data.columns:
            self.data['purchase_date'] = pd.to_datetime(self.data['purchase_date'], errors='coerce')
            self.data = self.data.dropna(subset=['purchase_date'])
            print("Data setelah transform:")
            print(self.data)
            return self.data

    def store(self, output_file_path):
        if self.data is not None:
            try:
                self.data.to_csv(output_file_path, index=False)
                print(f"Data stored successfully as CSV in {output_file_path}.")
            except Exception as e:
                print(f"Failed to store data: {e}")
        else:
            print("No data to store.")

class TargetedMarketingETL(MarketingDataETL):
    def segment_customers(self):
        if self.data is not None:
            conditions = [
                (self.data['amount_spent'] < 100),
                (self.data['amount_spent'] >= 100) & (self.data['amount_spent'] < 200),
                (self.data['amount_spent'] >= 200)
            ]
            choices = ['Low Spending', 'Medium Spending', 'High Spending']
            self.data['spending_segment'] = np.select(conditions, choices)
            print("Customer segmentation based on spending:")
            print(self.data)
        else:
            print("No data to segment. Please extract data first.")

    def transform(self):
        super().transform()
        self.segment_customers()

    def store_segmented_data(self, output_file_path):
        if self.data is not None:
            super().store(output_file_path)
        else:
            print("No data to store.")

# Contoh penggunaan
file_path = "marketing_data.csv"
targeted_etl = TargetedMarketingETL(file_path)
targeted_etl.extract()
targeted_etl.transform()
targeted_etl.store("marketing_data_processed.csv")
targeted_etl.store_segmented_data("segmented_data.xlsx")
