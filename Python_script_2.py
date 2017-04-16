#!/usr/bin/Python

# This script automate the task of changing the clock period and running the synthesis.script again and again, to meet the timing constraints for designs (adder in 
# this case) with different timing models such as RCA, Carry-Look-Ahead adder, CSA-UEQ, CSA-EQ

import os

import re

import sys																			# This import statement is used to write to the file using sys.stdout statement


outline = []																		# Global List declaration for storing the changed values that will be mapped to the original file later on.

counter = 0																			# Global variable counter

positive_attempt = 1																# This global variable is taken to see if the clock period can be decreased to increase the frequency and stop when further decreasing the value results in time violation.

def run_synthesis():
	global positive_attempt
	
	#os.system('dc_shell -xg -f synthesis.script | tee report.txt')					# This command will run synthesis on the machine that has dc_shell installed.
	
	#os.system('ls -l')
	
	count = 0
	
	flag = 0
	
	report = open('report.txt', 'r+')
	
	for abc in report:
		#print abc
		if 'slack (MET)' in abc:
			count += 1
			
	if count < 5:
		positive_attempt = 0
		print "Timing violation occured"
		#convert = 1
		
		#file_conversion(convert)
		
		change_clk(count)

		run_synthesis()																# COMMENT THIS LINE WHEN RUNNING WITHOUT ACTUAL REPORT.TXT FILE GENERATED FROM THE SYNTHESIZER EVERYTIME
		
		#file_conversion(convert)
		
		#if (flag == 0 and counter <3):
		#	run_synthesis()
			
		#	counter += 1
		
	elif count == 5 and positive_attempt!=0:
		change_clk(count)
		
		run_synthesis()
		
	else:
		print "All done with a smile"
		flag = 1
		
			
	print count
	
	report.close()
	
	
	
	
def file_conversion(convert):
	if convert ==1:
		base = os.path.splitext('synthesis.script')[0]
		os.rename('synthesis.script', base + '.txt')
		convert = 0
		
	else:
		base = os.path.splitext('synthesis.txt')[0]
		os.rename('synthesis.txt', base + '.script')

	
	
def change_clk(count2):
	script = open('synthesis.script', 'r+')
	
	global outline
	
	for xyz in script:
		if 'create_clock' in xyz:
			value	= re.search(r'\d+\.\d+|\d+', xyz).group()   	# Use of regular expression to extract float value or integer value from the string.
			
			value_f = float(value)									# Also, we need to do casting as re.search returns a string but we need a float value.
			
			#print xyz 
			
			if count2 == 5:
				new_value = value_f - 0.2
				
			else:
				new_value = value_f + 0.2
			
			#print new_value
			
			new_value = str(new_value)
			
			xyz = xyz.replace(value, new_value)
			
			print xyz
			
			
		write_to_file(xyz)
		
	outline = []													# It is necessary to flush the global list, otherwise the addition will keep on happening in the script file instead of overwriting it.
		
	script.close()
			
			
			
def write_to_file(value):

	global outline											# We have to declare outline as global list otherwise it will be initialised to null every time this function is called.
	
	outline.append(value)
	
	orig_stdout = sys.stdout								# This is used to redirect the stdout so that it does not get buffered and print function can work properly
			
	file1 = open('synthesis.script', 'w')
			
	sys.stdout = file1
	
	for item in outline:
		sys.stdout.write(item)
		
		
	sys.stdout = orig_stdout
	
	file1.close()
	
	
run_synthesis()

############################## RUN THE BELOW GIVEN CODE WHEN THERE IS NO REAL  REPORT.TXT FILE ######################################

#def run_arbiter():
#	global counter
#	
#	if counter < 3:
#		run_synthesis()
#		counter += 1
#
#
#while counter<3:
#	run_arbiter()

#####################################################################################################################################