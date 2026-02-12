import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path):
    """
    Reads a CSV file and converts it to a JSON file.
    """
    data = []
    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Convert numeric fields
                if 'amount' in row:
                    try:
                        row['amount'] = float(row['amount'])
                    except ValueError:
                        pass # Keep as string if not a number
                if 'nrv' in row:
                    try:
                        row['nrv'] = float(row['nrv'])
                    except ValueError:
                        pass
                
                data.append(row)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        print(f"Successfully converted {csv_file_path} to {json_file_path}")
        print(f"Processed {len(data)} items.")

    except FileNotFoundError:
        print(f"Error: File not found at {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Default paths based on project structure
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    csv_path = os.path.join(project_root, 'data', 'foods.csv')
    json_path = os.path.join(project_root, 'data', 'foods.json')

    print(f"Looking for CSV at: {csv_path}")
    csv_to_json(csv_path, json_path)
