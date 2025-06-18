import os

#user input for which year they want to analyze
year = input("Enter the year you want to analyze (2017 or 2018): ").strip()
folder = f"WakaNats{year}"

# To check if folder exists
if os.path.exists(folder):
    files = os.listdir(folder)

    # This code only takes files that are lif
    lif_files = [file for file in files if file.lower().endswith('.lif')]
   
    # Outputs the number of lif files
    print(f"Found {len(lif_files)} .lif files in {folder}")
else:
    print(f"Folder '{folder}' was not found")