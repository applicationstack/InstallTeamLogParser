import xlrd
import sys
import re

class compareKnownissues():
	def __init__(self, founderrors, knownerrorspath):
		self.founderrors = founderrors
		self.knownerrorspath = knownerrorspath
	def compare(self):
		workbook = xlrd.open_workbook(Known_Install_log_Issues)
		sheet = workbook.sheet_by_index(0)
		data = [sheet.cell_value(row, 0)for row in range(sheet.nrows)]
		#txt files read if already on computer, created if not
		knownerrorsTXT = open('KnownErrors.txt', 'w')
		unknownerrorsTXT = open('UnknownErrors.txt', 'w')
		#get Keyword column from Excel sheet
		keywordColumn = sheet.col(0)
		
		for line in ErrorArray :
        #it is printing everything multiple times to unknownErrors now
			hit = False
			for i in keywordColumn :
					value = i.value
					if value in line :
						hit = True
					elif not line.__contains__(value) :
						pass
			if hit :
				knownerrorsTXT.write(line)
				knownerrorsTXT.write("\n")
			else :
				unknownerrorsTXT.write(line)
				unknownerrorsTXT.write("\n")
		knownerrorsTXT.close()
		unknownerrorsTXT.close()
		

#Grab location of setupengine and Known Install Log Issues files
#setupengine = 'setupengineKnownErrors.log'
setupengine = 'setupengineUnknownErrors.log'
#TODO: need to make it so that Excel sheet is accessed from \\vanhome.van.sap.corp\automation\install\Automation_Results
Known_Install_log_Issues = 'Known_Install_log_Issues_.xlsx'

#ErrorArray = all errors read from setupengine.log
ErrorArray = []
ErrorDescription= []
unknownerrorsDescription = open('UnknownErrorsDescription.txt', 'w')

with open(setupengine, 'r') as lines:
	lines = lines.readlines()
	lineBefore = ""
	lineAfter = ""
	index = 0
	Description = ''
	
	for line in lines:
		if re.match("(.*)(E|e)rror:(.*)", line):
			index = lines.index(line)
			lineBefore = lines[index-1]
			lineAfter = lines[index+1]
			ErrorDescription.append(lineBefore)
			ErrorDescription.append(line)
			ErrorDescription.append(lineAfter)
			ErrorArray.append(line)
		else:
			pass
	Description = ''.join(ErrorDescription)
	unknownerrorsDescription.write(Description)
#Actual comparison and results
x = compareKnownissues(ErrorArray, Known_Install_log_Issues)
x.compare()
print ErrorArray


#Absolute paths on Risa's home computer (Mac)
#/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser/setupengineKnownErrors.log
#/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser/setupengineUnknownErrors.log
#/Users/risanewyear-ramirez/Desktop/LogParserWorkTermProject/logparser/Known_Install_log_Issues_.xlsx

#Absolute paths on Risa's work computer (Windows)
#'C:\Users\I841251\Desktop\logparser\setupengineKnownErrors.log'
#'C:\Users\I841251\Desktop\logparser\setupengineUnknownErrors.log'
#'C:\Users\I841251\Desktop\logparser\Known_Install_log_Issues_.xlsx'