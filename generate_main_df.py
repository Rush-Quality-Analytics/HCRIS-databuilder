import pandas as pd
import warnings
from IPython.utils import io
import sys
import csv
import re
import os


warnings.filterwarnings('ignore')


####################################################################################################
####################################################################################################

puf_df = pd.read_pickle('~/GitHub/HCRIS-databuilder/Filtered_PUF_data/FilteredEngineeredPUF_p5.pkl')
puf_df = puf_df.applymap(lambda x: x.decode() if isinstance(x, bytes) else x)


####################################################################################################
####################################################################################################


with io.capture_output() as captured: main_df = pd.read_sas('~/Desktop/HCRIS/hosp10-sas/prds_hosp10_yr2010.sas7bdat')
main_df['File Date'] = ['2010'] * main_df.shape[0]
main_df = main_df.applymap(lambda x: x.decode() if isinstance(x, bytes) else x)
main_df['rpt_rec_num'] = main_df['rpt_rec_num'].astype(int)
main_df['rpt_rec_num'] = main_df['rpt_rec_num'].astype(str)
print('2010: (rows, columns) =', main_df.shape)


yrs = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
for yr in yrs:
    with io.capture_output() as captured: tdf = pd.read_sas('~/Desktop/HCRIS/hosp10-sas/prds_hosp10_yr' + yr + '.sas7bdat')
    tdf['File Date'] = [yr] * tdf.shape[0]
    tdf = tdf.applymap(lambda x: x.decode() if isinstance(x, bytes) else x)
    tdf['rpt_rec_num'] = tdf['rpt_rec_num'].astype(int)
    tdf['rpt_rec_num'] = tdf['rpt_rec_num'].astype(str)

    main_df = pd.concat([main_df, tdf], ignore_index=True)
    print(yr + ': (rows, columns) =', main_df.shape)

del tdf


####################################################################################################
####################################################################################################


to_replace = ['rpt_rec_num', 'prvdr_num', 'fi_num', 'rpt_stus_cd', 'fi_creat_dt', 
              'fy_bgn_dt', 'fy_end_dt', 'util_cd', 'trnsmtl_num', 'state', 
              'st_cty_cd', 'census', 'region', 'proc_dt', 'msa', 'H3_1_HHA1_C10_15____',
              'H3_1_HHA1_C11_15____', 'sub3', 
             ]

replacement = ['RPT_REC_NUM', 'PRVDR_NUM', 'FI_NUM', 'RPT_STUS_CD', 'FI_CREAT_DT', 
               'FY_BGN_DT', 'FY_END_DT', 'UTIL_CODE', 'TRNSMTL_NUM', 'STATE', 
               'ST_CTY_CD', 'CENSUS', 'REGION', 'PROC_DT', 'MSA', 'H3_1_HHA1_C10_15',
               'H3_1_HHA1_C11_15', 'SUB3',
              ]

main_df.rename(columns = {to_replace[0]: replacement[0], to_replace[1]: replacement[1],
                           to_replace[2]: replacement[2], to_replace[3]: replacement[3],
                           to_replace[4]: replacement[4], to_replace[5]: replacement[5],
                           to_replace[6]: replacement[6], to_replace[7]: replacement[7],
                           to_replace[8]: replacement[8], to_replace[9]: replacement[9],
                           to_replace[10]: replacement[10], to_replace[11]: replacement[11],
                           to_replace[12]: replacement[12], to_replace[13]: replacement[13],
                           to_replace[14]: replacement[14], to_replace[15]: replacement[15],
                           to_replace[16]: replacement[16], to_replace[17]: replacement[17],
                         }, inplace = True)

main_df.drop(labels=['_NAME_', 'E_A_HOS_C1_68', 'E_A_HOS_C1_7090', 'E_A_HOS_C1_7091', 'E_A_HOS_C1_7093', 
                     'E_A_HOS_C1_7096', 'E_A_HOS_C1_93', 'E_A_HOS_C1_47', 'E_A_HOS_C1_49', 'E_A_HOS_C1_50', 
                     'E_A_HOS_C1_54', 'E_A_HOS_C1_59', 'E_A_HOS_C1_7094', 'E_A_HOS_C1_72', 'E_A_HOS_C1_7099', 
                     'E_A_HOS_C1_7097', 'E_A_HOS_C1_48', 'S2_1_C1_35', 'S2_1_C2_2'], axis=1, inplace=True)

print('main_df.shape:', main_df.shape)

####################################################################################################
####################################################################################################


common_features = list(filter(lambda x:x in list(puf_df), list(main_df)))
print(common_features)

main_df['RPT_REC_NUM'] = main_df['RPT_REC_NUM'].astype(int)
main_df['RPT_REC_NUM'] = main_df['RPT_REC_NUM'].astype(str)
main_df = main_df.merge(puf_df, how='outer', on=common_features)
del puf_df

main_df.sort_values(by='Reconstructed HAC penalty', inplace=True, ascending=False)
print(main_df.shape)


####################################################################################################
####################################################################################################


crosswalk_df = pd.read_csv('~/GitHub/HCRIS-databuilder/crosswalk/2552-10 SAS FILE RECORD LAYOUT AND CROSSWALK TO 96 - 2021.csv', sep=',')
crosswalk_labels = crosswalk_df['10_FIELD_NAME'].tolist()
crosswalk_labels = [str(x).strip(' ') for x in crosswalk_labels]
crosswalk_df['10_FIELD_NAME'] = crosswalk_labels




####################################################################################################
####################################################################################################


main_df_col_labels = list(main_df)
main_df_col_labels = [str(x).strip(' ') for x in main_df_col_labels]

print('\nNumber of labels in the crosswalk:', len(crosswalk_labels))
print('Number of unique labels in the crosswalk:', len(list(set(crosswalk_labels))))

print('\nNumber of labels in the main_df:', len(main_df_col_labels))
print('Number of unique labels in the main_df:', len(list(set(main_df_col_labels))))

shared_labels = list(set(main_df_col_labels) & set(crosswalk_labels))
print('\nNumber of labels shared between the main dataframe and the crosswalk:', len(shared_labels))
shared_labels.append('File Date')

dif = set(main_df_col_labels).difference(crosswalk_labels)
print('\n' + str(len(dif)) + ' labels in main dataframe but not in crosswalk:')
print(dif)

dif = set(crosswalk_labels).difference(main_df_col_labels)
print('\n' + str(len(dif)) + ' labels in crosswalk but not in main dataframe:')
print(dif)

del main_df_col_labels
del dif



####################################################################################################
####################################################################################################

add_labels = ['Line 19 Subtotal', 
              'Reconstructed HAC penalty', 
              'HAC penalty imputed from E_A_HOS_C1_59',
              'Reconstructed IPPS payment (post HAC penalty)', 
              'Reconstructed IPPS payment (pre HAC penalty)',
              ]

main_df = main_df[main_df.columns[main_df.columns.isin(shared_labels + add_labels)]]
del shared_labels

main_df = main_df.dropna(axis=1, how='all')
main_df = main_df.dropna(axis=0, how='all')
print('main_df.shape (columns and rows with no data removed):', main_df.shape)

CODE = []
FIELD_DESCRIPTION = []
TYPE = []
SUBTYPE = []

col_labels = list(main_df)

for lab in col_labels:
    if lab == 'File Date':
        CODE.append('File Date')
        FIELD_DESCRIPTION.append('File Date')
        TYPE.append('File Date')
        SUBTYPE.append('File Date')
        
        
    elif lab in add_labels:
        CODE.append('')
        FIELD_DESCRIPTION.append(lab)
        TYPE.append('CALCULATION OF REIMBURSEMENT SETTLEMENT (PPS)')
        SUBTYPE.append('IMPUTED/HYPOTHETICAL')
        
    else:
        df_sub = crosswalk_df[crosswalk_df['10_FIELD_NAME'] == lab]
        CODE.append(df_sub['10_FIELD_NAME'].iloc[0])
        
        x = df_sub['FIELD DESCRIPTION '].iloc[0]
        if x == "" or pd.isnull(x):
            FIELD_DESCRIPTION.append('No Description')
            
        else:
            FIELD_DESCRIPTION.append(x)
        
        x = df_sub['TYPE'].iloc[0]
        if x == "" or pd.isnull(x):
            TYPE.append('No Description')
        else:
            TYPE.append(x)
        
        x = df_sub['SUBTYPE'].iloc[0]
        if x == "" or pd.isnull(x):
                SUBTYPE.append('')
        else:
            SUBTYPE.append(x)

SUBTYPE = pd.Series(SUBTYPE).fillna('').tolist()
TYPE = pd.Series(TYPE).fillna('').tolist()


for i, val in enumerate(SUBTYPE):
    if val == 'File Date':
        continue
    elif val == 'IMPUTED/HYPOTHETICAL' and CODE[i] == '':
        SUBTYPE[i] = str(FIELD_DESCRIPTION[i]) + ' (IMPUTED/HYPOTHETICAL)'
    elif val == '':
        SUBTYPE[i] = str(FIELD_DESCRIPTION[i]) + ' ' + '(' + str(CODE[i]) + ')'
    else:
        SUBTYPE[i] = str(val) + ' ' + str(FIELD_DESCRIPTION[i]) + ' (' + str(CODE[i]) + ')'



df2 = pd.DataFrame([col_labels, FIELD_DESCRIPTION, TYPE, SUBTYPE], columns=col_labels)
main_df = pd.concat([df2, main_df])
del df2

main_df.columns = pd.MultiIndex.from_arrays(main_df.iloc[0:4].values)
main_df = main_df.iloc[4:]

del col_labels
del FIELD_DESCRIPTION
del TYPE
del SUBTYPE


####################################################################################################
####################################################################################################

CMS_Gen_Info_df = pd.read_csv('~/GitHub/HCRIS-databuilder/GeoData/Hospital_General_Information.tsv', sep='\t')
print(list(CMS_Gen_Info_df))




####################################################################################################
####################################################################################################

hospital_ls = main_df.iloc[:, (main_df.columns.get_level_values(0) == 'S2_1_C1_3')].T.values.tolist()[0]
id_ls = main_df.iloc[:, (main_df.columns.get_level_values(0) == 'PRVDR_NUM')].T.values.tolist()[0]

print(hospital_ls[0:4])
print(id_ls[0:4])


lats = []
lons = []
Htypes = []
Ctypes = []

misses = 0
hits = 0
for i, h in enumerate(hospital_ls):
    
    fid = id_ls[i]
    
    try:
        df = CMS_Gen_Info_df[CMS_Gen_Info_df['Facility ID'] == fid]
            
        loc = df['Location'].iloc[0]
        loc = loc.replace("POINT (","") 
        loc = loc.replace(")","")
        loc = loc.split(" ")
            
        lat = loc[1]
        lon = loc[0]
        lats.append(lat)
        lons.append(lon)
        
        htype = df['Hospital Type'].iloc[0]
        Htypes.append(htype)
        ctype = df['Hospital Ownership'].iloc[0]
        Ctypes.append(ctype)
        
        del df
        
    except:
        lats.append(float('NaN'))
        lons.append(float('NaN'))
        Htypes.append(float('NaN'))
        Ctypes.append(float('NaN'))






for i, val in enumerate(lats):
    if pd.isnull(val): 
        continue
    else:
        print(val, lons[i], Htypes[i], Ctypes[i])
    if i > 10:
        break
    
    
    
    
    
    
main_df[('Lat', 'Lat', 'Lat', 'Lat')] = lats
main_df[('Lon', 'Lon', 'Lon', 'Lon')] = lons
main_df[('Control type, text', 'Control type, text', 'Control type, text', 'Control type, text')] = Ctypes
main_df[('Hospital type, text', 'Hospital type, text', 'Hospital type, text', 'Hospital type, text')] = Htypes
main_df[('Num and Name', 'Num and Name', 'Num and Name', 'Num and Name')] = main_df[('S2_1_C1_3', 'Hospital Name ', 'No Description', 'Hospital Name  (S2_1_C1_3)')].astype(str) +' (' + main_df[('PRVDR_NUM', 'Hospital Provider Number ', 'HOSPITAL IDENTIFICATION INFORMATION', 'Hospital Provider Number  (PRVDR_NUM)')].astype(str) + ')'   

del lats
del lons
del Ctypes
del Htypes


####################################################################################################
####################################################################################################

badnames = ['20994', float('NaN'), '-0007', '1', '330354', '4499 ACUSHNET AVENUE OPERATING COMPA',
           '4499 ACUSHNET AVENUE OPERATING COMPM']

main_df = main_df[~main_df[('S2_1_C1_3', 'Hospital Name ', 'No Description', 'Hospital Name  (S2_1_C1_3)')].isin(badnames)]





####################################################################################################
####################################################################################################

tdf = main_df.filter(items=[('Lat', 'Lat', 'Lat', 'Lat'),
                             ('Lon', 'Lon', 'Lon', 'Lon'),
                             ('Control type, text', 'Control type, text', 'Control type, text', 'Control type, text'),
                             ('Hospital type, text', 'Hospital type, text', 'Hospital type, text', 'Hospital type, text'),
                             ('Num and Name', 'Num and Name', 'Num and Name', 'Num and Name'),
                             ('S3_1_C2_27', 'Total Facility', 'NUMBER OF BEDS', 'Total Facility (S3_1_C2_27)'),
                             ('S2_1_C2_2', 'Hospital State', 'No Description', 'Hospital State (S2_1_C2_2)'),
                            ], axis=1)

tdf.to_pickle('~/GitHub/HCRIS-databuilder/GenDat4App/GenDat4App_p4.pkl', protocol=4)

del tdf



####################################################################################################
####################################################################################################


main_df[('FY_END_DT', 'Fiscal Year End Date ', 'HOSPITAL IDENTIFICATION INFORMATION', 'Fiscal Year End Date  (FY_END_DT)')] = pd.to_datetime(main_df[('FY_END_DT', 'Fiscal Year End Date ', 'HOSPITAL IDENTIFICATION INFORMATION', 'Fiscal Year End Date  (FY_END_DT)')])
main_df = main_df.sort_values(by=[('Num and Name', 'Num and Name', 'Num and Name', 'Num and Name'),
                     ('FY_END_DT', 'Fiscal Year End Date ', 'HOSPITAL IDENTIFICATION INFORMATION', 'Fiscal Year End Date  (FY_END_DT)')],
                     ascending=[True, True])


####################################################################################################
####################################################################################################


numNname = sorted(list(set(main_df[('Num and Name', 'Num and Name', 'Num and Name', 'Num and Name')].tolist())))

for i, val in enumerate(numNname):
    prvdr = re.sub('\ |\?|\.|\!|\/|\;|\:', '', val)

    tdf = main_df[main_df[('Num and Name', 'Num and Name', 'Num and Name', 'Num and Name')] == val]
    tdf.to_csv('~/GitHub/HCRIS-databuilder/provider_data/' + prvdr + '.csv')
    del tdf
    
    
####################################################################################################
####################################################################################################

main_df.to_pickle('~/GitHub/HCRIS-databuilder/hcris_all_data/HCRIS_p4.pkl', protocol=4)


####################################################################################################
####################################################################################################


report_categories = list(set(main_df.columns.get_level_values(2).tolist()))
report_categories = [x for x in report_categories if str(x) != 'nan']
report_categories = [x for x in report_categories if str(x) != 'Lat']
report_categories = [x for x in report_categories if str(x) != 'Lon']
report_categories = [x for x in report_categories if str(x) != 'Num and Name']
report_categories = [x for x in report_categories if str(x) != 'Hospital type, text']
#report_categories = [x for x in report_categories if str(x) != '']
report_categories = [x for x in report_categories if str(x) != 'HOSPITAL IDENTIFICATION INFORMATION']

report_categories = [x for x in report_categories if str(x) != 'Control type, text']
report_categories = [x for x in report_categories if str(x) != 'HOSPITAL IDENTIFICATION INFORMATION']
report_categories = [x for x in report_categories if str(x) != 'HOSPITAL IDENTIFICATION INFORMATION']
report_categories.sort()


cwd = os.getcwd()  # Get the current working directory (cwd)
print(cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))


with open("/Users/kenlocey/GitHub/HCRIS-databuilder/GenDat4App/report_categories.csv", 'w+', newline='') as OUT:
    writer = csv.writer(OUT)
    writer.writerow(report_categories)
    
    
sub_categories = list(set(main_df.columns.get_level_values(3).tolist()))
sub_categories.sort()

with open('/Users/kenlocey/GitHub/HCRIS-databuilder/GenDat4App/sub_categories.csv', 'w+', newline='') as OUT:
    writer = csv.writer(OUT)
    writer.writerow(sub_categories)






    



