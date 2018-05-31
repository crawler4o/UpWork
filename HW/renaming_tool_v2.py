import shutil, os, csv

def rename():
	for file in os.listdir('./input/'):
		print(file)
		with open('sites.csv', 'r') as f:
			sites_dict = csv.reader(f)
			
			for line in sites_dict:
				#print (file[:5])
				#print (line)
				if str(file[:5]) in str(line[0]):
					dest_file = ''.join('./output/'+ line[1] + '-' + file[:10] + '_TSSR_' + file[11:])
					#print(dest_file)
					src_file = './input/' + file
					shutil.copyfile(src_file, dest_file)
					

if __name__ == '__main__':
	rename()
