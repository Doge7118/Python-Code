import pandas as pd # type: ignore

# Set pandas display options to show more content
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

url = "https://raw.githubusercontent.com/msikorski93/Meteorite-Landings/refs/heads/main/meteorite-landings.csv"

try:
    df = pd.read_csv(url)
    print("DataFrame Info:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("\nFirst 5 rows of the DataFrame:")
    print(df.head())
    print("\nLast 5 rows of the DataFrame:")
    print(df.tail())
    print("\nPrinting the summary statistics of the DataFrame")
    print(df.describe())

    print("\nPrinting the shape of the DataFrame")
    print(df.shape)
    print("\nPrinting the columns of the DataFrame")
    print(df.columns.tolist())
    print("\nPrinting the index of the DataFrame")
    print(df.index)
    print("\nUnique values in the 'recclass' column:")
    recclass_unique = df['recclass'].unique()
    print(f"Number of unique recclass values: {len(recclass_unique)}")
    print("First 10 recclass values:")
    for i, value in enumerate(recclass_unique[:10]):
        print(f"{i+1}: {value}")
    if len(recclass_unique) > 10:
        print("... (truncated)")
        print("Last 5 recclass values:")
        for i, value in enumerate(recclass_unique[-5:], len(recclass_unique)-4):
            print(f"{i}: {value}")

    print("\nTop 5 biggest meteorites by mass:")
    top_5_biggest = df.nlargest(5, 'mass')[['name', 'mass', 'year', 'recclass', 'fall']]
    for i, (_, row) in enumerate(top_5_biggest.iterrows(), 1):
        print(f"{i}. {row['name']}: {row['mass']:,.1f} grams ({row['recclass']}, {row['fall']}, {int(row['year']) if pd.notna(row['year']) else 'Unknown year'})")

    print("\nMeteorites that fell per decade:")
    # Filter for meteorites that 'Fell' (not 'Found') and have valid year data
    fell_meteorites = df[(df['fall'] == 'Fell') & pd.notna(df['year'])]

    # Create decade column
    fell_meteorites = fell_meteorites.copy()
    fell_meteorites['decade'] = (fell_meteorites['year'] // 10) * 10

    # Count meteorites per decade and sort by decade
    decade_counts = fell_meteorites['decade'].value_counts().sort_index(ascending=False)

    print(f"Total meteorites that fell (with known years): {len(fell_meteorites):,}")
    print("\nBreakdown by decade:")
    for decade, count in decade_counts.items():
        decade_start = int(decade)
        decade_end = int(decade + 9)
        meteorite_word = "meteorite" if count == 1 else "meteorites"
        print(f"{decade_start}s ({decade_start}-{decade_end}): {count:,} {meteorite_word}")

    print("\nCreating world map visualization of meteorite fall locations...")

    # Filter data for meteorites with valid coordinates that actually fell in North America
    # North America bounds: latitude 15-85°N, longitude -170 to -50°W
    map_data = df[(df['fall'] == 'Fell') & 
                  pd.notna(df['reclat']) & 
                  pd.notna(df['reclong']) &
                  (df['reclat'].between(15, 85)) &
                  (df['reclong'].between(-170, -50))]

    print(f"Plotting {len(map_data):,} meteorites with valid coordinates on world map...")

    # Create a folium map centered on the world
    import folium

    # Create base map centered on North America
    world_map = folium.Map(
        location=[50, -100],  # Center on North America
        zoom_start=3,
        tiles='OpenStreetMap'
    )

    # Add markers for each meteorite fall location
    # Limit to first 1000 points to avoid performance issues
    sample_data = map_data.head(1000) if len(map_data) > 1000 else map_data

    for idx, row in sample_data.iterrows():
        # Create popup text with meteorite information
        popup_text = f"""
        <b>{row['name']}</b><br>
        Mass: {row['mass']:,.1f}g<br>
        Year: {int(row['year']) if pd.notna(row['year']) else 'Unknown'}<br>
        Class: {row['recclass']}<br>
        Coordinates: ({row['reclat']:.3f}, {row['reclong']:.3f})
        """

        # Determine marker size based on mass (log scale for better visualization)
        if pd.notna(row['mass']) and row['mass'] > 0:
            import math
            marker_size = min(max(3, math.log10(row['mass']) * 2), 15)
        else:
            marker_size = 3

        # Add marker to map
        folium.CircleMarker(
            location=[row['reclat'], row['reclong']],
            radius=marker_size,
            popup=folium.Popup(popup_text, max_width=200),
            color='red',
            fillColor='orange',
            fillOpacity=0.7,
            weight=1
        ).add_to(world_map)

    # Save the map
    map_filename = 'meteorite_falls_world_map.html'
    world_map.save(map_filename)
    print(f"World map saved as '{map_filename}'")
    print(f"Displaying {len(sample_data):,} meteorite fall locations on the map")
    if len(map_data) > 1000:
        print(f"Note: Showing first 1,000 out of {len(map_data):,} meteorites for performance")

    print("Interactive map complete - showing only North American meteorite falls")


except Exception as e:
    print(f"Error reading CSV from URL: {e}")
