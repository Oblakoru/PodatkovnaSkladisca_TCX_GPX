import os
from sport_activities_features import GPXFile
import pandas as pd
import tcxparser
from sport_activities_features import GPXFile


gpx_file = GPXFile()
data = []
# activity = gpx_file.read_one_file("Sport4/Athlete10/riderx1.gpx")
# integral_metrics = gpx_file.extract_integral_metrics("Sport4/Athlete10/riderx1.gpx")
# speeds = activity['speeds']
#
# print(integral_metrics['activity_type'])
#
# data.append({
#     'tipAktivnosti': integral_metrics['activity_type'],
#     'zacetekAktivnosti': [max(activity["timestamps"]) if len(activity["timestamps"]) > 0 else None],
#     'trajanjeAktivnosti': integral_metrics['duration'].total_seconds(),
#     'razdaljaAktivnosti': integral_metrics['distance'] / 1000,
#     'vzponAktivnosti': integral_metrics['ascent'],
#     'kalorijeAktivnosti': integral_metrics['calories'],
#     'kadenceAvgAktivnosti': None,
#     'kadenceMaxAktivnosti': None,
# })

#Tule maš sam za GPX parsat in shranit v CSV

index = 5
for i, folder_name in enumerate(os.listdir("Sport4")):
    # Join the directory path and folder name to get the full path
    full_path = os.path.join("Sport4", folder_name)
    data = []
    for root, dirs, files in os.walk(full_path):
        for datoteka in files:
            file_path = os.path.join(root, datoteka)
            if os.path.isfile(file_path):
                try:
                    activity = gpx_file.read_one_file(file_path)
                    integral_metrics = gpx_file.extract_integral_metrics(file_path)
                    speeds = activity['speeds']
                    if len(speeds) > 0:
                        total_speed = sum(speeds)
                        num_items = len(speeds)
                        avg_speed = total_speed / num_items

                    data.append({
                        "sportnik": index,
                        'tipAktivnosti': activity['activity_type'],
                        'zacetekAktivnosti': [max(activity["timestamps"]) if len(activity["timestamps"]) > 0 else None],
                        'trajanjeAktivnosti': integral_metrics['duration'].total_seconds(),
                        'razdaljaAktivnosti': integral_metrics['distance'] / 1000,
                        'vzponAktivnosti': integral_metrics['ascent'],
                        'kalorijeAktivnosti': integral_metrics['calories'],
                        'tempoAktivnosti': avg_speed,
                        'kadenceAvgAktivnosti': None,
                        'kadenceMaxAktivnosti': None,
                    })
                except:
                    print(f"Error pri {file_path}")
            print(f"Prebrane datoteke: {file_path}",)

    df = pd.DataFrame(data)
    df.fillna(0.0, inplace=True)

    df.to_csv(f"{index}.csv", index=False)

    index += 1



