import pandas as pd

def truncate_columns(file_path, output_path, max_digits_dict):
    # Load the Excel file
    df = pd.read_excel(file_path)

    # Truncate columns based on max_digits_dict
    for column_index, max_digits in max_digits_dict.items():
        df.iloc[:, column_index] = df.iloc[:, column_index].astype(str).str.slice(0, max_digits)

    # Save the modified DataFrame to a new Excel file
    df.to_excel(output_path, index=False)

    print(f"Truncated columns have been successfully saved to {output_path}")

if __name__ == "__main__":
    file_path = "path/to/your/input_file.xlsx"  # Change this to the path of your input Excel file
    output_path = "path/to/your/output_file.xlsx"  # Change this to the path where you want to save the output Excel file
    max_digits_dict = {
        1: 4, 
        2: 4, 
        4: 7, 
        5: 4, 
        6: 4, 
        26: 6, 
        28: 5, 
        29: 5, 
        31: 5, 
        32: 5, 
        37: 5, 
        48: 7, 
        62: 7, 
        65: 9, 
        66: 9, 
        68: 5, 
        69: 9, 
        70: 9, 
        71: 7, 
        72: 5, 
        73: 7, 
        74: 7, 
        76: 4, 
        77: 5, 
        78: 5, 
        82: 6, 
        83: 6, 
        86: 6, 
        114: 5, 
        115: 5, 
        130: 3, 
        131: 7, 
        134: 7, 
        136: 5, 
        138: 7, 
        142: 5, 
        144: 5, 
        146: 5, 
        147: 7, 
        148: 6, 
        149: 5
    }
    truncate_columns(file_path, output_path, max_digits_dict)
