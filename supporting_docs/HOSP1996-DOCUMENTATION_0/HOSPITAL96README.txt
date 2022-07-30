HCRIS PRODUCTION NOTES FOR HOSPITAL COST REPORT DATA

1.  OVERVIEW
2.  INTRODUCTION
3.  NOTES
4.  Subscripting of Lines and Columns on the Worksheet forms:
5.  Cost Center Codes
6.  Extracting Data for the Intensive Care Unit Lines 
7.  Extracting Data for Lines on Worksheet S-3, Part I
8.  Extracting Data for Lines on Worksheet D-1
9.  Extracting Data for Lines on Worksheet G-2
10. Files and Contents
11. NPI ADDITION
12. SET UP GUIDANCE
13. DISCLAIMER OF WARRANTY



1. OVERVIEW: 

CMS now stores the HCRIS cost report files in a relational database.  

The foremost characteristic of this database is the fact that data 
elements will be distributed in flat files aligned with the database table 
in which they reside in our database.  

You will be able to access the entire set of HCRIS Cost Report data that
is submitted to HCRIS by a Fiscal Intermediary on behalf of a provider.  The 
major benefit for all users is the ability to use Relational Database Technology
to quickly exclude certain fields of data or perform cross-sectional analysis.


The following website contains the cost reporting reimbursement manuals and 
electronic cost reporting specifications for provider cost reports:    
http://www.cms.hhs.gov/Manuals/
 


2. INTRODUCTION:  

The CMS Form 2552-96 Hospital Cost Report(HOSP96) data files contain cost reports with 
fiscal years ending on or after September 30, 1996.  The data files contain 
the highest level of Medicare cost report status.  If HCRIS has both an as 
submitted report and a final settled report for a hospital for a particular year, 
the data files will only contain the final settled report.   If HCRIS has an as 
submitted, final settled, and reopened report for a hospital for a 
particular year, the data files will contain the reopened cost report. 

It is possible for 1 Hospital to submit 2 or more cost reports for a given year
for the same cost report status.  This may happen if a hospital changes
its FY, or if there is a CHOW (Change of Ownership) during the year.  We have
also found cost reports that were sent in error with an incorrect FYB or
FYE.  For the most part, HCRIS trys to eliminate these incorrect submissions by
contacting the FI and deleting a cost report that the FI identifies as incorrect. 

If you have any questions about this product, please contact the HCRIS staff via 
e-mail at HCRIS@cms.hhs.gov, and include the word "Hospital" in the subject line.



3. NOTES: 

The data included with this release includes all years (from FY 1996 through Current).    

To use the Hospital cost report data, you first need to determine the data that 
you are interested in by reviewing the cost report forms and the data specifications.
You will need to know the Worksheet code, line, and column from the cost report form.  
For example, if you wanted to extract the number of hospital beds, you will need to 
determine where this information is collected in the report and use these elements 
as parameters to pull the data from the HOSP_RPT_NMRC table.   The number of beds 
is collected on Worksheet S-3,Part I, Line 12, Column 1 so you would create the 
following condition:  
     Worksheet Code ='S300001' 
     Line Number ='01200'
     Column Number ='0100'    
*Note: Refer to the file named HOSP96_2552-96_Worksheet_Codes.pdf to determine worksheet 
codes.  Line Numbers are 5 positions, and Column Numbers are 4 positions.



4.  Subscripting of Lines and Columns on the Worksheet forms:

Many lines on the worksheet forms can be subscripted.  For example, the worksheet 
form may show line 6, but it is possible that data relating to that line could be 
reported on lines 00600 thru 00699.  Keep that in mind when extracting data for a 
particular line. 




5.  Cost Center Codes:

Refer to the file named HOSPITAL96CostCenterCodes.pdf to understand the connection between worksheet 
line numbers and cost center codes and worksheet column numbers and cost center codes.

The page named Line Codes in the HOSPITAL96CostCenterCodes.pdf file lists the cost center codes to 
use for the worksheets that collect data for cost center lines.  The page named 
Column Codes lists the cost center codes to use for the worksheets that collect 
data for cost center columns.    

The cost center codes are actually the line numbers for the cost center line  
coded worksheets which are all listed in the HOSPITAL96CostCenterCodes.pdf  file in the sheet named Line 
Codes. For example if you are extracting data for Worksheet A, Line 1, Column 1, you 
have to make sure you extract all the possible codes for Line 1.  Look at the 
HOSPITAL96CostCenterCodes.pdf file in the sheet named Line Codes to find the cost center codes to use
for Line 1.  For Line 1, extract lines/codes 00100 thru 00149.  

The cost center codes are the column numbers for the cost center column coded 
worksheets which are listed in the HOSPITAL96CostCenterCodes.pdf in the sheet named Column Codes.  
FOr example, if you are extracting data for Worksheet B, Part I, Column 1, you have 
to extract all the possible codes for Column 1.  Look at the HOSPITAL96CostCenterCodes.pdf file
in the sheet named Column Codes to find the cost center codes to use for Column 1.  
For Column 1, extract Columns 0100 thru 0149.  



6.  Extracting Data for the Intensive Care Unit Cost Centers: 

The Intensive Care Unit cost centers are also reported on the following worksheets:  
S-3, Part I, Lines 6-10; D-1, Part II, Lines 43-47;  D-6, Part I, Lines 2-6; and G-2, 
Part I, Lines 10-14.  When extracting data for these lines, do not use the actual 
line number. Use the following cost center codes/line numbers when extracting data:   
     Intensive Care Unit:  	   	02600-02619
     Coronary Care Unit:   	   	02700-02719
     Burn Intensive Care Unit:     	02800-02819
     Surgical Intensive Care Unit: 	02900-02919
     Other Special Care Unit:	   	02140-02159, 02080-02099, 02060-02079, 
                                   	02180-02199, 02040-02059, 02120-02139

For example, on the worksheet form the Intensive Care Cost Center is on Line 6; 
however, do not use Line 6, use Lines/Codes 02600 thru 02619. 

See the HOSP96_CSTCDS.xls file to see the meanings of the other special care unit 
Lines/Codes.

 

7.  Extracting Data for Lines on Worksheet S-3, Part I:

Lines 14, 18, 20, 21, 23, and 24 can be subscripted to account for more than one
hospital based component.  For example you may see Lines 14 and 14.01. Line
14 is for Subprovider I data and Line 14.01 is for Subprovider II data.  
A hospital can have more than one subprovider.   

If you are extracting data for Line 21, do not include Lines 02140-02159 or 
02180-02199 or 02120-02139 in your extraction for this line.  
These lines/codes are actually for Line 10 (Other Special Care Unit Cost Center)
(See above in Number 5).

If you are extracting data for Line 20, do not include Lines 02080-02099 or 
02060-02079 or 02040-02059 in your extraction for this line.  These
lines/codes are actually for Line 10 (Other Special Care Unit Cost Center)
(see above in Number 5).

Lines 02300 thru 02309 represent a CORF (Comprehensive Outpatient Rehab Facility).
Lines 02310 thru 02319 represent a CMHC (Community Mental Health Center).
Lines 02320 thru 02329 represent a OPT (Outpatient Physical Therapy).
Lines 02330 thru 02339 represent a OOT (Outpatient Occupational Therapy).
Lines 02340 thru 02349 represent a OSP (Outpatient Speech Pathology). 


Lines 02400 thru 02409 and 02435 thru 02450 represent a RHC (Rural Health Clinic).
Lines 02410 thru 02434 reprsent a FQHC (Federally Qualified Health Center).  

If you are extracting data for Worksheet S-3, Part I, Lines 26, 26.01, 27,27.01, and 
28, do not use the actual line numbers because you would be getting data for 
Intensive Care Unit, Coronary Care Unit, and Burn Intensive Unit cost 
centers.  Use the following lines: 
     Line 26:    06200 
     Line 26.01: 06201
     Line 26.02: 06202
     Line 27:    06500
     Line 27.01: 06501
     Line 27.02: 06502
     Line 28:    06800
     Line 29:    06900



8.  Extracting Data for Lines on WOrksheet D-1:

If you are extracting data for Line 20, do not include Lines 02080-02099 or 
02060-02079 or 02040-02059 in your extraction for this line.  
These lines/codes are actually for Line
47 (Other Special Care Unit Cost Center)
(See above in Number 5).  

If you are extracting data for Line 21, do not include Lines 02140-02159 or 
02180-02199 or 02120-02139 in your extraction for this line.  
These lines/codes are actually for Line 47 (Other Special Care Unit Cost Center)
(See above in Number 5).  



9.  Extracting Data for Lines on Worksheet G-2:

If you are extracting data for Line 20, Column 1, do not include Lines 02080-02099 or 
02060-02079 or 02040-02059 in your data extraction.  These lines/codes are actually 
for Line 14 (Other Special Care Unit Cost Center)
(See Number 5 above).  


10. FILES AND CONTENTS: 

10.1 Hospital Data Files : Hospital96_FYYYY.ZIP

	Compressed files containing 4 text(csv) files with the raw 
	data for the fiscal year XXXX to be loaded into the HOSP_RPT, HOSPF_ALPHANMRC, HOSP_NMRC and HOSP_ROLLUP tables. 
	These files contain data elements that are separated by commas.  

10.2 Hospital Report Files : HOSP96_REPORTS.zip

	HOSP96_RECORD_COUNTS.csv - A csv file containing a list of the record counts per fiscal year.    

	HOSP96_COST_REPORT_STATUS_COUNTS.csv - A csv file containing the counts of cost reports per type and fiscal year.  

	HOSP96_PRVDR_ID_INFO.csv - A csv file containing one line of identifying data for each HOSP provider.

10.3 Hospital Documentation Files : HOSP_DOCUMENTATION.ZIP

	HOSP96_HCRIS_File_Data_Elements.pdf:  A .pdf file that lists all the fields HCRIS collects if reported by the provider.  
	Refer to this file to determine if a line item on the cost report is alpha or numeric.

	HOSP96_PROVIDER_CONTROL_TYPE_CODES.csv:  A csv file that contains the meanings of the 
	Provider control type codes.

	HOSP96_TYPE_OF_HOSPITAL.txt:  A text file that contains the meanings of the type of 
	hospital codes on Worksheet S-2, Line 19.  These codes are the same for S-2, 
	Line 20 and subscripts (type of subprovider codes)

	HOSP96_URBAN_RURAL_INDICATORS.txt:  A text file that contains the codes for Urban 
	or Rural hospital on Worksheet S-2, Line 21, Column 1. 

	HOSP96_ROLLUP_README.txt - A description of the Hosp_Rpt_Rollup file.  

	HOSP96_ROLLUP_REQUIREMENTS.csv - A csv file containing all the fields that make up the Hosp_Rpt_Rollup file.  

	hosp96_README.txt - This readme file.

	HOSP96_HCRIS_File_Data_Elements.pdf or .xls - File containing the data fields collected by HCRIS if reported by the hospital.  
	This file comes in both a .pdf and .xls format.  
	Refer to this file to determine if a line item on the cost report is alpha or numeric.  

	HOSP96_2252-96WORKSHEET_CODES.pdf - A .pdf File containing codes for the worksheets.  

	HOSPITAL96CostCenterCodes.pdf - A .pdf File containing the description of cost center codes.  .

10.4 HCRIS Documentation Files : HOSP_DOCUMENTATION.ZIP

	HCRIS_FACILITY_NUMBERING.csv:  A csv file containing information on how to identify the type of facility by the last four positions of the provider number.  

	HCRIS_STATE_CODES.csv:  A csv file contains all the state codes for each state.

	HCRIS_TABLE_DESCRIPTIONS_AND_SQL.txt - A text file containing the descriptions of the tables, and an ANSI SQL Program (non-Database specific) Containing the DDL scripts to create the 4 tables that comprise the HCRIS HOSPITAL Database.

	HCRIS_DATA_DICTIONARY.csv:  A csv file that contains the meanings of the data elements in the Rpt file, the Alphnmrc file, the Nmrc file, 
	and the Rollup_Data file.  

	HCRIS_Data_Model.pdf - A .pdf file that contains a diagram of the tables.  The columns are listed in the exact order they appear in the files.  


 

The hospital cost reporting worksheet forms can be found at http://www.cms.gov/COSTREPORTS/.  Scroll down to Provider Reimbursement Manual, Part II.  
Then scroll down to Chapter 36.  
The forms list all the data fields in the cost report.  Refer to the HCRIS File Data Elements file to determine the fields HCRIS collects
if reported by the hospital.    



11.  NPI ADDITION:
Effective with the 6/30/2006 release, a column has been added to the 
HOSP_RPT file named NPI which stands for National Provider Identifier.  
This column will be used when CMS begins receiving the NPI on cost reports.
    


12. SET UP GUIDANCE:  

It is important to note that the datafiles you will be provided are not restricted 
for use in one given database platform or even a database management system for 
that matter.  
You will likely be able to use your existing tools or utilities to access the data, 
given the ability of those tools to handle files up to the size of the largest 
datafile 
and files containing data arranged in CSV or Comma Separated value format.  
You will, however, need to re-program, re-direct, or adjust any programs, 
utilities or 
other automated routines previously used with HCRIS files, to the new data 
specifications.  

If you choose to modify your existing programs, please be certain to examine the 
individual datafile and corresponding database table structure carefully or else 
you may not achieve valid results or even be able to access the data. If you 
choose to use a relational or desktop database management system, please be 
mindful of the sizes of the various datafiles.   



13. DISCLAIMER OF WARRANTY:    

The Centers for Medicare & Medicaid Services shall retain no responsibility for 
the data recipients inability to load, examine, or otherwise use the published data 
for 
the HCRIS system.  

The information in these files is subject to change, and should be reviewed for 
each release.  

(c) 2012 Centers for Medicare & Medicaid Services, All rights reserved.  
www.cms.hhs.gov

---------------------------------------------------------------------------------
Note: PROVIDER CONTROL TYPE CODE

The provider control type codes are in 2 places in the file, and they are as follows:

The Hosp_Rpt file contains the column called Provdr_Ctrl_Type_Cd. 
It is also in the Hosp_Rpt_Nmrc file.  You have to extract the following:
Worksheet Code = S200000
Line_Num = 01800
Col_Num = 0100


	
