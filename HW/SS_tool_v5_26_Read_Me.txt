### SS tool v.5.26, XX/05/2018 ###






### SS tool v.5.25, 15/05/2018 ###

	- Fixed bug with wrongly adding TMAs for sites with 2 antennas.



### SS tool v.5.24, 14/05/2018 ###

	- Updated TMA dictionary, so DTMA1800 and DTMA 2100 no bom appear as STMA. Addressing the issue when different TMAs are installed on the same layer.



### SS tool v.5.23, 13/05/2018 ###

	- Compare the TMA number to the antenna number and write second TMA of a kind if available.



### SS tool v.5.22, 12/05/2018 ###

	- Added smoother error handling - reporting the error and keeping the window open.
	- Improved mechanism for adding the 2in4out TMAs, as some of them are added to the LTE only and some to both U&L. 
		Now 2in4out TMAs might be missed if it is added only to the UMTS, which should never be the case.
	- Added mechanism to add the boards of the BBUs if both BBUs are configured as sub-rack 0
	- Improved mechanism for adding BBUs so they can be added if both are configured as sub-rack 0.
		Bear in mind that the two BBUs might appear with swapped positions.
	- Add DC Stops based on the added combiners
		
Improvement points:

	
	-- Adjust the rows ( AC/DC RRU row has been added to the template)
	-- Fill in the PSUs
	-- Add the config descriptors - existing and target ( 1+1+1 ) ( in progress )




### SS tool v.5.21, 11/05/2018 ###

	- New way to export the U2k inventory, so the GSM can be completely covered
	- 2in4out TMAs appear with 2 different serials. An extra check was added to address this issue and cut the overall 2in4out tma count in half.
	- Adding TMAs for 4 sectors is now supported
	
	

### SS tool v.5.2, 08/05/2018 ###

The RNP NetSite file is : V:\Application\RadioPlanning01\Home\!reports\00_RNP_Summary	
The Site owners and NIS data is : V:\Application\RadioPlanning01\Home\!reports\00_NIS_Rev

We're now adding:
	- site owners and NIS data
	- BBUs
	- Combiners 
	
Disclaimer:

Most of the data the tool is adding is based on a precise guesswork and unreliable exports. It should be verified manually.



### SS tool v.5, 04/05/2018 ###

Adding feeders, based on the NetSite export. 
	- adds one entry per band that has feeder length given.
	
	
### SS tool v.5, 04/05/2018 ###

We are now adding also Huawei cabinets. 
Please pay attention that some cabinets appear without serial number  on the export. 
These will be labeled with '_NS' after the cabinet type.


### SS tool v.4, 25/03/2018 ###


What this tool does :

1. Makes copies of the given SS template and renames them according the given names-list.
2. Parses data from different sources and puts it on a dummy file as follows:
	- The RND entries for the selected SS.
	- The Board inventory export: 
		- BBU boards
		- RF modules
	- The RNP NetSite export:
		- Antennas
	- Parses the antenna export:
		- KA RCUs 
		- TMAs - CAUTION! - The tool adds TMAs sequentially based on their model, starting from sector 1. No accurate relation to the actual sector is available on the export. Please distribute the TMAs manually in case you do not have TMAs on all sectors. 

		
Prerequisites :

1. Download and install Python v.3.x.x . Do not forget to put the environmental variables check-box during the installation and to include pip. https://www.python.org/downloads/
2. It is a good idea to setup a virtual Python environment if you plan to run any other Python apps. Just skip this if you do not.
3. Install openpyxl - 'pip install openpyxl'. If it fails, you've probably  not followed the reminder of p.1. To fix it reinstall the Python. Include the above mentioned components this time :-)



Operation:

1. Update the content of the 'list.txt'. This file should contain the filenames of SS files you want to have in the end.
2. Run SS_tool_v2.py
3. Find the files in the 'output' folder.
	- The files that are properly named are the valid SS files. You should work on them.
	- The files with 'dummy_' prefix are the ones containing the RND and the hardware info. This is the copy-paste source. Sorry for the copy/paste - it's because of an openpyxl limitation.

	
	
Maintenance:

In order to work properly, the tool uses some extra resources that are available in the folder and are declared in the beginning of SS_tool_v2.py. 
The files that need to be available in the folder are:
	- Dummy SS template - This is an excel file with cleaned data validation. It is used as a template for the dummy file. You do not need to change it unless the template format is somehow updated.
	- Inventory export - This is a board inventory export. Please follow the screen-shot to make a fresh export regularly. Do not need to export 'cabinet' and 'slot', but I really don't feel like connecting to U2k for new screenshot right now.
	- List of target SS filenames - this is the one you update every time.
	- SS template - This is the real SS template that will be multiplied and renamed accordingly.
	- RND
	- The 'output' folder
	
Please keep your resource files updated. If any of the above mentioned files is renamed, please update the declaration in the beginning of SS_tool_v2.py.



Improvement plan:
	- Fill in the cabinets
	- Update the BBU0 / BBU1 selection algorithm, so it is based on the L / U in the site name. ( append u, l, ul, luto the list and if both )
	- Fill in the PSUs
	- Add the config descriptors - existing and target ( 1+1+1 )
	
	
