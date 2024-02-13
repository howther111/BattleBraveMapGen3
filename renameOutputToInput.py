import os
try:
    is_csvfile = os.path.isfile("input_map_csv.csv")
    if is_csvfile:
        os.remove("input_map_csv.csv")

    is_pngfile = os.path.isfile("input_map.png")
    if is_pngfile:
        os.remove("input_map.png")

    os.rename("output_map_csv.csv", "input_map_csv.csv")
    os.rename("output_map.png", "input_map.png")

except Exception as e:
    print(e)