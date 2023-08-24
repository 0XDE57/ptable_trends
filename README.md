Modification of https://github.com/arosen93/ptable_trends

- add new coolwarm color palette
- force data scaling to always be 0-1 instead of low=min(data), high=max(data) because data set may not always contain data with absolute values of 0-1
- modify rendering to support custom data: insert a blank row, and take over elements to insert custom data not in the table of elements.
- export directly as PNG to file instead of opening HTML page
- scripted to process any .csv file in a given folder and produce a PNG for each CSV file.
