#! /usr/bin/env python

import os
import pandas as pd
import skbio as sk
import sys


input_files = sys.argv[1:]
print(input_files)
output_path = "./result/taxonomy"


for i, file in enumerate(input_files):

    file_name = os.path.splitext(os.path.basename(file))[0]
    file_name = file_name.split("_")[0]
    if i < 1:
        df = pd.read_csv(file, sep="\t")
        df = df[df.taxRank =='species']
        sum_reads = df['numUniqueReads'].sum()
        df[f'{file_name}'] = df['numUniqueReads']*100/sum_reads
        df = df[['name',f'{file_name}','taxID']]
    else:
        df_file = pd.read_csv(file, sep="\t")
        sum_reads = df_file['numUniqueReads'].sum()
        df_file[f'{file_name}'] = df_file['numUniqueReads']*100/sum_reads
        df_file = df_file[df_file['taxRank'] =='species']
        df_file = df_file[['name', f'{file_name}','taxID']]
        df = pd.merge(df, df_file, on=['name','taxID'], how='outer')
        
df = df.fillna(0)
column_to_move = df.pop("taxID")
df.insert(1, "taxID", column_to_move)

df['Genus'] = df['name'].str.split(' ').str[0]
column_to_move = df.pop("Genus")
df.insert(0, "Genus", column_to_move)
df.rename(columns = {'name':'Species'}, inplace = True)

print(df)
print("IT TAKES TIME")

# create df for genus report
genus = df.copy()
genus = genus.drop(['Species', 'taxID'], axis=1)

#create df for vertical table with first row as Shannon indexes
sp = df.drop(['Genus','taxID'],axis=1)
sp_t = sp.set_index('Species').T
sp_t["Shannon"] = '' 
col = len(sp_t.columns)-1

#create list for Shannon indexes
shannon = []

for i in range(len(sp_t)):
    sp_t['Shannon'].values[i]=sk.diversity.alpha.shannon(counts=list(sp_t.iloc[i,0:col]), base=2)
    shannon.append(sk.diversity.alpha.shannon(counts=list(sp_t.iloc[i,0:col]), base=2))
    
sp_t.to_csv(f'{output_path}' + '/Species_Shannon_hor.csv', index=True)
print("Done Species_Shannon_hor.csv")
# add to df row with shannon index (first 3 cells - just character & others shannon list
df.loc[-1] = ['-', 'Shannon', '-'] + shannon
df.index = df.index + 1  # shifting index
df.sort_index(inplace=True)

df.to_csv(f'{output_path}' + '/species_report_vert.csv', index=False)
print("Done species_report_vert.csv")
genus = genus.groupby('Genus').sum()


genus.to_csv(f'{output_path}' + '/genus_report.csv', index=True)

print("Done genus_report.csv")