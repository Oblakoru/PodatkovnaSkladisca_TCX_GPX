
import os
import pandas as pd
from sport_activities_features import GPXFile
from sport_activities_features.tcx_manipulation import TCXFile
import tcxparser
from sqlalchemy import create_engine
tcx_file = TCXFile()


#data = []

for index, folder_name in enumerate(os.listdir("Sport5")):
    # Join the directory path and folder name to get the full path
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
    #df['kadenceAvgAktivnosti'] = df['kadenceAvgAktivnosti'].astype(float)

    #df_biking = df[df['tipAktivnosti'] == 'biking']
    #df_biking.to_csv(f"{full_path}.csv")
    df.to_csv(f"{full_path}.csv", index=False)




        #kilometrina = ["tipAktivnosti", "zacetekAktivnosti", "trajanjeAktivnosti", "razdaljaAktivnosti",
        #               "tempoAktivnosti"]
        #
        #ostali = ["kalorijeAktivnosti", "vzponAktivnosti", "kadenceAvgAktivnosti"]
        #
        #df_kilometrina = df_biking[kilometrina]
        #df_ostali = df_biking[ostali]
        #
        ## Example for MySQL: 'mysql://username:password@localhost:3306/your_database'
        #povezava = ('mysql+mysqlconnector://root:root@localhost:3308/skladisca_kolesar'
        #            engine = create_engine(povezava, echo=True)
        #df_kilometrina.to_sql('dim_kilometrina', con=engine, if_exists='replace', index
        #df_ostali.to_sql('dim_ostali', con=engine, if_exists='replace', index=False)




# for root, dirs, files in os.walk("Test"):
#    for datoteka in files:
#         file_path = os.path.join(root, datoteka)
#         if os.path.isfile(file_path):
#            try:
#
#                integral_metrics = tcxparser.TCXParser(file_path)
#
#                tipAktivnosti = integral_metrics.activity_type
#                zacetekAktivnosti = integral_metrics.started_at
#                trajanjeAktivnosti = integral_metrics.duration
#                razdaljaAktivnosti = integral_metrics.distance / 1000
#                vzponAktivnosti = integral_metrics.ascent
#                kalorijeAktivnosti = integral_metrics.calories
#                tempoAktivnosti = integral_metrics.pace
#                kadenceAvgAktivnosti = integral_metrics.cadence_avg
#                kadenceMaxAktivnosti = integral_metrics.cadence_max
#
#                data.append({
#                    'tipAktivnosti': tipAktivnosti,
#                    'zacetekAktivnosti': zacetekAktivnosti,
#                    'trajanjeAktivnosti': trajanjeAktivnosti,
#                    'razdaljaAktivnosti': razdaljaAktivnosti,
#                    'vzponAktivnosti': vzponAktivnosti,
#                    'kalorijeAktivnosti': kalorijeAktivnosti,
#                    'tempoAktivnosti': tempoAktivnosti,
#                    'kadenceAvgAktivnosti': kadenceAvgAktivnosti,
#                    'kadenceMaxAktivnosti': kadenceMaxAktivnosti
#                })
#
#
#            except:
#                print(f"Error pri {file_path}")
#
#
#
#
#    df = pd.DataFrame(data)
#
#    df.fillna(0.0, inplace=True)
#    df['kadenceAvgAktivnosti'] = df['kadenceAvgAktivnosti'].astype(float)
#
#    ##
#    df_biking = df[df['tipAktivnosti'] == 'biking']
#
#    kilometrina = ["tipAktivnosti",  "zacetekAktivnosti", "trajanjeAktivnosti", "razdaljaAktivnosti", "tempoAktivnosti" ]
#
#    ostali = [ "kalorijeAktivnosti", "vzponAktivnosti", "kadenceAvgAktivnosti" ]
#
#    df_kilometrina = df_biking[kilometrina]
#    df_ostali = df_biking[ostali]
#
#    # Example for MySQL: 'mysql://username:password@localhost:3306/your_database'
#    povezava = ('mysql+mysqlconnector://root:root@localhost:3308/skladisca_kolesar')
#
#    engine = create_engine(povezava, echo=True)
#
#    df_kilometrina.to_sql('dim_kilometrina', con=engine, if_exists='replace', index=False)
#    df_ostali.to_sql('dim_ostali', con=engine, if_exists='replace', index=False)



















