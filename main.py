import os
import pandas as pd
from sport_activities_features.tcx_manipulation import TCXFile
import tcxparser
tcx_file = TCXFile()


#Vsak sportnik ima svoj folder, v katerem so njegove aktivnosti
for index, folder_name in enumerate(os.listdir("Sport5")):
    full_path = os.path.join("Sport5", folder_name)
    data = []
    for root, dirs, files in os.walk(full_path):
        for datoteka in files:
            file_path = os.path.join(root, datoteka)
            if os.path.isfile(file_path):
                try:
                    integral_metrics = tcxparser.TCXParser(file_path)
                    tipAktivnosti = integral_metrics.activity_type
                    zacetekAktivnosti = integral_metrics.started_at
                    trajanjeAktivnosti = integral_metrics.duration
                    razdaljaAktivnosti = integral_metrics.distance / 1000
                    vzponAktivnosti = integral_metrics.ascent
                    kalorijeAktivnosti = integral_metrics.calories
                    tempoAktivnosti = integral_metrics.pace
                    kadenceAvgAktivnosti = integral_metrics.cadence_avg
                    kadenceMaxAktivnosti = integral_metrics.cadence_max
                    data.append({
                        "sportnik": index,
                        'tipAktivnosti': tipAktivnosti,
                        'zacetekAktivnosti': zacetekAktivnosti,
                        'trajanjeAktivnosti': trajanjeAktivnosti,
                        'razdaljaAktivnosti': razdaljaAktivnosti,
                        'vzponAktivnosti': vzponAktivnosti,
                        'kalorijeAktivnosti': kalorijeAktivnosti,
                        'tempoAktivnosti': tempoAktivnosti,
                        'kadenceAvgAktivnosti': kadenceAvgAktivnosti,
                        'kadenceMaxAktivnosti': kadenceMaxAktivnosti
                    })
                except:
                    print(f"Error pri {file_path}")

    df = pd.DataFrame(data)
    df.fillna(0.0, inplace=True)
    df.to_csv(f"{full_path}.csv", index=False)




















