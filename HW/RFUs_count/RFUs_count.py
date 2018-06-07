import os
from xlrd import open_workbook


def count():

	rfus = 0 # 'MRFUd(1800)'
	rru_2t2r = 0 # 'RRU3938(1800 2T2R)'
	rru_4t4r = 0 # 'RRU3971 4T4R(1800)'
	rru_2t2r_sites = []

	for file in os.listdir('./input/'):
		wb = open_workbook(filename = './input/{}'.format(file)) # opening the SS
		sheet = wb.sheet_by_name('Site solution') #defining the SS sheet to read
		rfus_before_loop = rfus
		rru_2t2r_before_loop = rru_2t2r
		rru_4t4r_before_loop = rru_4t4r
		
		if sheet.cell_value(2, 4) == 'Position': # checking the version of the template. This is for the new version with position column.
		
			# adding the target config to the accounting
			
			if 'RFU' in  sheet.cell_value(35, 9):
				rfus += int(sheet.cell_value(35, 10))
			if 'RFU' in sheet.cell_value(35, 12) :
				rfus += int(sheet.cell_value(35, 13))
			if 'RRU3938' in sheet.cell_value(35, 9):
				rru_2t2r += int(sheet.cell_value(35, 10))
				rru_2t2r_sites.append(file)
			if 'RRU3938' in sheet.cell_value(35, 12):	
				rru_2t2r += int(sheet.cell_value(35, 13))
				rru_2t2r_sites.append(file)
			if 'RRU3971' in sheet.cell_value(35, 9) :
				rru_4t4r += int(sheet.cell_value(35, 10))
			if 'RRU3971' in sheet.cell_value(35, 12):
				rru_4t4r += int(sheet.cell_value(35, 13))
			
			
			#removing the existing config from the accounting
			
			if 'RFU' in sheet.cell_value(35, 2):
				rfus -= int(sheet.cell_value(35, 3))
			if 'RFU' in sheet.cell_value(35, 5):
				rfus -= int(sheet.cell_value(35, 6))
			if 'RRU3938' in sheet.cell_value(35, 2):
				rru_2t2r -= int(sheet.cell_value(35, 3))
			if 'RRU3938' in sheet.cell_value(35, 5):
				rru_2t2r -= int(sheet.cell_value(35, 6))	
			if 'RRU3971' in sheet.cell_value(35, 2):
				rru_4t4r -= int(sheet.cell_value(35, 3))
			if 'RRU3971' in sheet.cell_value(35, 5):
				rru_4t4r -= int(sheet.cell_value(35, 6))
		
		else: # and for the old version
			
			# adding the target config to the accounting
			
			if 'RFU' in  sheet.cell_value(35, 7):
				rfus += int(sheet.cell_value(35, 8))
			if 'RFU' in sheet.cell_value(35, 9) :
				rfus += int(sheet.cell_value(35, 10))
			if 'RRU3938' in sheet.cell_value(35, 7):
				rru_2t2r += int(sheet.cell_value(35, 8))
				rru_2t2r_sites.append(file)
			if 'RRU3938' in sheet.cell_value(35, 9):	
				rru_2t2r += int(sheet.cell_value(35, 10))
				rru_2t2r_sites.append(file)
			if 'RRU3971' in sheet.cell_value(35, 7) :
				rru_4t4r += int(sheet.cell_value(35, 8))
			if 'RRU3971' in sheet.cell_value(35, 9):
				rru_4t4r += int(sheet.cell_value(35, 10))
			
			
			#removing the existing config from the accounting
			
			if 'RFU' in sheet.cell_value(35, 2):
				rfus -= int(sheet.cell_value(35, 3))
			elif 'RFU' in sheet.cell_value(35, 4):
				rfus -= int(sheet.cell_value(35, 5))
			elif 'RRU3938' in sheet.cell_value(35, 2):
				rru_2t2r -= int(sheet.cell_value(35, 3))
			elif 'RRU3938' in sheet.cell_value(35, 4):
				rru_2t2r -= int(sheet.cell_value(35, 5))	
			elif 'RRU3971' in sheet.cell_value(35, 2):
				rru_4t4r -= int(sheet.cell_value(35, 3))
			elif 'RRU3971' in sheet.cell_value(35, 4):
				rru_4t4r -= int(sheet.cell_value(35, 5))
		
			# yield if the site doesn't add 1800 modules or the removed modules outnumber the added.
		if rfus_before_loop >= rfus and rru_2t2r_before_loop >= rru_2t2r and rru_4t4r_before_loop >= rru_4t4r:
			print('{} is suspicious as it does not add or only reduces 1800 modules \n'.format(file))
		
		
	print('')	
	print('Summary')	
	print('RFUs we will need are : {}'.format(rfus))
	print('RRU3938(1800 2T2R) we will need are : {}'.format(rru_2t2r))	
	print('RRU3971 4T4R(1800) we will need are : {}'.format(rru_4t4r))
	print('')
	print('The sites that use 1800 2t2r RRUs are:')
	for x in rru_2t2r_sites:
		print(x)

if __name__ == '__main__':
	count()
		
