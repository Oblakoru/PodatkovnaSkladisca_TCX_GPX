import os
from sport_activities_features import GPXFile
import pandas as pd
import tcxparser
from sport_activities_features import GPXFile

# read GPX file

gpx_file = GPXFile()

activity = gpx_file.read_one_file("Sport4/Athlete1/riderx1.gpx")
integral_metrics = gpx_file.extract_integral_metrics("Sport4/Athlete1/riderx1.gpx")


for x in activity.keys():
    print(x)
print("--------------------------------------------------")
for y in integral_metrics.keys():
    print(y)

speeds = activity['speeds']
if len(speeds) > 0:
  total_speed = sum(speeds)
  num_items = len(speeds)
  avg_speed = total_speed / num_items


duration = integral_metrics.get('duration', None)
steps = integral_metrics.get('steps', None)

avg_cadence = None
max_cadence = None
if duration != None and steps != None:
    avg_cadence = (steps / duration) * 60
    max_cadence = (steps / duration) * 60


data = []
data.append({
    #"sportnik": index,
    'tipAktivnosti': activity['activity_type'],
    'zacetekAktivnosti': [max(activity["timestamps"]) if len(activity["timestamps"]) > 0 else None],
    'trajanjeAktivnosti': integral_metrics['duration'].total_seconds(),
    'razdaljaAktivnosti': integral_metrics['distance'] / 1000,
    'vzponAktivnosti': integral_metrics['ascent'],
    'kalorijeAktivnosti': integral_metrics['calories'],
    'tempoAktivnosti': avg_speed,
    'kadenceAvgAktivnosti': avg_cadence,
    'kadenceMaxAktivnosti': max_cadence
})

print(data)

#print(activity)
#print(integral_metrics)

# last_time = None
# timestamps = activity['timestamps']
# print(timestamps)
# if len(timestamps) > 0:
#     last_time = max(timestamps)
# avg_speed = None
# speeds = activity['speeds']
# if len(speeds) > 0:
#     total_speed = sum(speeds)
#     num_items = len(speeds)
#     avg_speed = total_speed / num_items
# avg_cadence = None
# max_cadence = None




# if (end == 'tcx'):
#     name = integral_metrics['activity_type']
# if (end == 'gpx'):
#     name = activity['activity_typ
# data = {
#     'atlete': os.path.basename(os.path.dirname(file)),
#     'activity_name': name,
#     'activity_time': last_time.strftime('%Y-%m-%d'),
#     'duration': duration,
#     'distance': integral_metrics.get('distance', None),
#     'max_altitude': integral_metrics.get('altitude_max', None),
#     'calories': integral_metrics.get('calories', None),
#     'avg_speed': avg_speed,
#     'avg_cadence': avg_cadence,
#     'max_cadence': max_cadence
#
# data_df = pd.DataFrame([data])
# with open(f'./{end}.csv', 'a', newline='\n') as f:
#     data_df.to_csv(f, header=f.tell() == 0, index=False)
# print(os.path.dirname(file))