# HCRIS-databuilder
More than 6,800 hospital specific cost reports and the python source code needed to generate them from larger, more complicated public files from the Centers for Medicare and Medicaid Services (CMS) Healthcare Cost Report Information System (HCRIS).  

## Purpose

CMS HCRIS provides quarterly updated annual healthcare cost report for thousands of Medicare-certified hospitals. These data are self-reported by hospitals, are made freely available to the public, and include information on costs, charges, utilization, payment, penalty, payroll, and general hospital characteristics. However, the largest and most up-to-date HCRIS files are too large for spreadsheet programs, lack meaningful feature labels, and can require specialized expertise to digest or comprehend. 
We democratized insights into hospital cost report data by developing this public repository of curated hospital-specific cost reports for more than 6,800 hospitals. Each report contains up to 2,771 features and spans all years from 2010 to present. These reports are used by the open-source [Hospital Cost Report Application] (https://hcris-app.herokuapp.com/).

## Files & Directories

<details><summary>generate_main_df.ipynb</summary>
This Jupyter notebook file is used to aggregate freely, publicly available SAS database files from the CMS website for the HCRIS [Hospital 2552-2010 form] (https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Cost-Reports/Hospital-2010-form). These files are combined with files on general hospital characteristics and geographical data. The SAS database files used by this jupyter notebook are too large to include in this repository; the user must acquire them from the [CMS site for the Hospital 2552-2010 form](https://www.cms.gov/Research-Statistics-Data-and-Systems/Downloadable-Public-Use-Files/Cost-Reports/Hospital-2010-form). The results of running this file are 1) a large dataframe containing all data for all hospital across all years from 2010 to present, and 2) >6,800 hospital-specific cost reports.
</details>

<details><summary>provider_data</summary>
This directory contains >6,800 hospital-specific cost reports. Because hospital names often change, each cost report file corresponds to a single CMS hospital ID number. Each ID number can correspond to multiple hospitals that existed between 2010 and the present.
</details>

<details><summary>GeoData</summary>
This directory contains files used by the `generate_main_df.ipynb` file to verify or fill in missing information for hospitals' state/territory and geographic coordinates.
</details>

<details><summary>crosswalk</summary>
This directory contains two files. The `2552-10 SAS FILE RECORD LAYOUT AND CROSSWALK TO 96 - 2021.xlsx` file is the downloaded CMS' HCRIS crosswalk with additional tabs and features added by us. The `2552-10 SAS FILE RECORD LAYOUT AND CROSSWALK TO 96 - 2021.csv` file is a machine readable crosswalk, which is used by the associated hospital cost report application and by the `generate_main_df.ipynb` file to add meaningful labels to alphanumeric cost report feature codes.
</details>

<details><summary>name_and_number.xlsx</summary>
This file contains all of the reported hospital names associated with each CMS hospital ID number. There are two columns (Original Label, Curated Label). The Original Labels represent the reported names, many of which were egregiously misspelled or were otherwise inconsistent (e.g., using the holding company name instead of the hospital name). The Curated Labels are those used in the cost reports generated by the `generate_main_df.ipynb` file.
</details>

<details><summary>name_and_number.csv</summary>
This file is used by the `generate_main_df.ipynb` file to replace incorrect reports of hospital names with correct names, it is nothing more a csv version of the above .xlsx file.
</details>


## Developer
Kenneth J. Locey, PhD. Senior Clinical Data Scientist. Center for Quality, Safety & Value Analytics. Rush University Medical Center. Chicago, IL, USA.
 