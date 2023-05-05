import pandas as pd
import numpy as np


class ScoreCalculator:
    def __init__(self, file) -> None:
        self.file = file

    def read_excel(self) -> pd.DataFrame:
        '''Read and clean MS Teams generated excel data'''
        df = pd.read_excel(self.file)
        if not "Assignments" in df.columns:
            first_row = df.iloc[[0]].values.flatten().tolist()
            df.columns = first_row
            df.drop([0], inplace=True)
        df = df[['Full Name', 'Assignments', 'Points', 'Max Points']]
        return df

    def create_grades_table(self) -> pd.DataFrame:
        teams_sheet = self.read_excel()
        students = teams_sheet["Full Name"].unique()
        students = np.sort(students)
        grades_columns = teams_sheet["Assignments"].unique()
        grades_columns = np.append(grades_columns, "Name")[::-1]
        grades = pd.DataFrame(columns=grades_columns)
        grades["Name"] = students
        grades.set_index("Name", inplace=True)

        for student in grades.iterrows():
            student = student[0]
            for column in grades.columns:
                scores = teams_sheet[
                    (teams_sheet["Assignments"] == column)
                    & (teams_sheet["Full Name"] == student)
                ][["Full Name", "Points", "Max Points"]]
                scores[["Points", "Max Points"]] = scores[
                    ["Points", "Max Points"]
                ].astype(float)
                scores["grade_float"] = 10 / scores["Max Points"] * scores["Points"]
                scores["grade"] = scores["grade_float"].round(0).fillna(0.0).astype(int)
                grades[column][student] = scores["grade"].values[0]

        print(grades)
        if __name__ != "__main__":
            grades.to_excel("test_output.xlsx")
        else:
            grades.to_excel("output.xlsx")
        return grades # return for testing


if __name__ == "__main__":
    sc = ScoreCalculator("./grades.xlsx")
    sc.create_grades_table()
