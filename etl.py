import csv

# Define the input and output file paths
input_file_path = 'stocks.txt'  # Replace with your input file path
output_file_path = 'stocks.csv'  # Replace with your desired output file path

# Read the space-separated file and write to a CSV file
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
    # Create a CSV writer
    csv_writer = csv.writer(output_file)

    # Iterate through each line in the input file
    for line in input_file:
        # Split the line by spaces to separate words
        words = line.strip().split()
        words[0] += ".BA"

        # Write the words as a row in the CSV file
        csv_writer.writerow(words)

print(f'Conversion complete. Data saved to {output_file_path}')