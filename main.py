
import os
import pandas as pd
from sport_activities_features import GPXFile
from sport_activities_features.tcx_manipulation import TCXFile
import tcxparser


# Class for reading TCX files
tcx_file = TCXFile()

data = []
for root, dirs, files in os.walk("Test"):
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
   print(df)



### Convert

for root, dirs, files in os.walk("TestGTX"):
   for datoteka in files:
        file_path = os.path.join(root, datoteka)

        gpx_file = GPXFile()
        podatki = gpx_file.read_one_file(file_path)
        for x in podatki:
            print(x)
        integral_metrics = gpx_file.extract_integral_metrics(file_path)

        print(integral_metrics)
        #data = gpx_file.read_one_file(file_path)
#














