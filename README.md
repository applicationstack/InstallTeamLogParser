-Setupengine Log Parser Documentation-
by Risa Newyear-Ramirez

Introduction
----------------
This document is meant to be a guide for the SAP Install Team to using the setupengine.log parsing tools for the purposes of testing.
It describes how the tools can be used to generate visualizations of the time taken to install certain components, and to gather all the
'error:' tags in the log to sort them by known or unknown errors.

What is included with this project
-----------------------------------
-compareIssues.py
-CoordinateParser.py
-coordinates.csv
-ErrorReportingToolGUI.py
-Known_Install_log_Issues.xlsx (Latest version from shared Install Automation folder)
-KnownErrors.txt
-main.py
-step_duration.csv
-StepParser.py
-steps.txt
-UnknownErrors.txt

The project will also require a setupengine.log to be in the same directory.

Using the setupengine parser to create steps and Lumira Visualization (from Salman Tariq's documentation)
----------------------------------------------------------------------------------------------------------
The StepParser.py python class is responsible for opening the steps.txt file, parsing the steps listed and using them to get the minutes needed to
execute each step.
Each line in the steps.txt file represents a step. For example the last step currently is represented by the following line:

*** END CHECKING PRODUCT SEQUENCE ***,** UNCACHING DUs...,Third Product Sequence

We can break the above line into 3 parts as divided by the commas:
-The first part represents the starting line for that step
-The second part represents the ending line for that step
-The third part is just a name to represent that step

The steps.txt file can be modified to add/remove as many steps you want, given that each line has a unique start/end pair i.e the pair is not repeated anywhere 
else in the setupengine log.

The main.py is the entry point for the entire program. It is executed via the shell (cmd.exe or windows powershell)  with a single argument, which is the path to 
the setupengine.log. With the above folder structure i.e the setupengine.log and the main.py file in the same folder, the following command needs to be run:

python.exe  .\main.py  .\setupengine.log

The main.py script parses the setupengine.log file and passes it to the StepParser.py, which uses it to compile a list of steps and their respective durations in the 
form of the step_duration.csv file. As a side effect, the StepParser.py uses CoordinateParser.py to compile a list of all the coordinates in the setpengine.log file in 
their respective duration in the form of coordinates.csv.

In order to create a visualization in Lumira:
1. Start Lumira, either click on the Acquire Data or the New Dataset button
2. Load the step_duration.csv file
3. Create dataset
4. Set Duration as the measure
5. Select steps as a Dimension
6. Set legends (Start Time and End Time)
7. You can use different charts from the panel on the right (e.g Line Chart, Pie Chart).

Using the setupengine parser to search for errors
--------------------------------------------------
The compareIssues.py python class is responsible for opening up a setupengine.log file, parsing for lines marked with 'error:', and saving them to either a Known Errors
or an Unknown Errors text file depending on whether the error matches keywords in the Known_Errors_log_Issues.xlsx file.

The script looks for the setupengine.log and Known_Errors_log_Issues.xlsx in the same directory as the project.
If text files for Known Errors and Unknown Errors are not present in the same directory, they are created when the script is run for the first time.

