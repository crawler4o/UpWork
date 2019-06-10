How to use:

1. Get the provided cell data files and fill in the 'AP' column ( '4T4T' XOR '2T2R' ). Will need to unhide some cells.
2. Put the files in the 'input' folder
3. Run 'Cell_Creator.py'
4. Find the prepared LTE RNP cell data files in the 'output' folder.
5. Open the file in excel and make sure it's OK. Save, or CME will not import it!
5. Remove at least the files from the output folder before next usage.

Limitations:
Only LTE cells, only standard 3900.
___________________________________________________________________________________________

How to setup the environment:

1. Install Python 3.x. Put the 'Add Python to the Path' checkbox during the installation. https://www.python.org/downloads/
2. Install the necessary packages to run this tool by running the following commands in 'CommandPrompt'. Disconnect the iAccess first.
    pip install pandas
