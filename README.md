# Python-script-to-automate-the-task-of-timing-analysis-for-RTL-designs-Timing-closure-
Python script to check and fix timing violation for the RTL design in order to meet the timing requirements.

User needs to enter the command to run this python file which will eventually call "run_synthesis()" commands and start synthesis.

Step-1: This script determines whether slack is MET (and there are no timing violations in the design) or not. 

Step-2: If the slack is violated, then this script automatically takes the access of synthesis script and change the clock period (either increment or decrement) by 0.1. 

Step-3: After changing the clock period, script automatically runs the synthesis commands to perform synthesis again. 

Step-4: It does this in a repeated looping manner until the slack is MET. 

Step-5 report.txt is the result file. If there is no file as “report.txt” initially then it will first run the synthesis script. 

Step-6: However if the report.txt exists then it will directly start with checking the slack violation.
