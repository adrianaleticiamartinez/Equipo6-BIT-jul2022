import pandas as pandasForSortingCSV
  
csvDataCliente = pandasForSortingCSV.read_csv("baseClientesHackaton2022.csv")

csvData.sort_values(["idCliente"], 
                    axis=0,
                    ascending=[True], 
                    inplace=True)
  
print(csvDataCliente)
