class DataProcessUtils:
    # Convert JSON list of dicts to CSV
    def json_dict_to_csv(self, json_data, output_path):
        import pandas as pd
        if not json_data:
            raise ValueError("Empty JSON data")
        try:
            df = pd.DataFrame(json_data)
            df.to_csv(output_path, index=False)
            return df
        except Exception as e:
            raise ValueError(f"Invalid data: {e}")