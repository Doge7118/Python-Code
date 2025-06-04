
import urllib.request
import csv

def fetch_and_print_planets():
    url = "https://gist.githubusercontent.com/fusion0202/23624d74061c4236587447f4a97761af/raw/75c80179590249c7bd3c8f966c5d2b2d221b6c64/planets.csv"
    
    try:
        # Fetch the CSV data from the URL
        with urllib.request.urlopen(url) as response:
            csv_data = response.read().decode('utf-8')
        
        # Parse and print the CSV data
        csv_reader = csv.reader(csv_data.splitlines())
        total_diameter = 0
        
        print("Planet Diameters:")
        print("-" * 30)
        
        for i, row in enumerate(csv_reader):
            if i == 0:  # Header row
                print(f"{row[0]} - {row[1]}")
            else:  # Data rows
                print(f"{row[0]} - {row[1]} km")
                # Add to total (remove any non-numeric characters and convert to float)
                diameter_str = row[1].replace(',', '')  # Remove commas if any
                try:
                    total_diameter += float(diameter_str)
                except ValueError:
                    pass  # Skip if can't convert to number
        
        print("\n" + "=" * 40)
        print("Would you like me to add the diameters?")
        print("Yes / No")
        
        user_input = input().strip().lower()
        if user_input in ['yes', 'y']:
            print(f"\nTotal sum of all planet diameters: {total_diameter:,.1f} km")
        elif user_input in ['no', 'n']:
            print("Okay, not showing the sum.")
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")
            
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_and_print_planets()
