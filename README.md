# grades_table_generator
Convert MS Teams excel of students grades to more convenient format and recalculate grades with base of 10

input like:
|       | **Full Name** | **Assignments** | **Points** | **Max Points** |
| ----- | ------------- | --------------- | ---------- | -------------- |
| **0** | Jonas         | Quiz1           | 25         | 30             |
| **1** | Antanas       | Quiz1           | 12         | 30             |
| **2** | Petras        | Quiz1           | 17         | 30             |
| **3** | Jonas         | Quiz2           | 10         | 15             |
| **4** | Antanas       | Quiz2           | 4          | 15             |
| **5** | Petras        | Quiz2           | 7          | 15             |

output like:

| **Name**    | **Quiz2** | **Quiz1** |
| ----------- | --------- | --------- |
| **Antanas** | 3         | 4         |
| **Jonas**   | 7         | 8         |
| **Petras**  | 5         | 6         |



pip install pandas and openpyxl.
Download excel file from team grades section, rename to 'grades.xlsx'. Put in same folder as this script.
Run the program (python ./grade_calculator). If everything is ok, you'll find output file in the same directory ;)
Created for personal usage, not sure if teams generates these excels the same for other folks.
