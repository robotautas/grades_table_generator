import os
import pandas as pd
from grade_calculator import ScoreCalculator

import unittest


class TestScoreCalculator(unittest.TestCase):
    filename = "test_input.xlsx"

    def setUp(self) -> None:
        mock_values = {
            "Full Name": ["Jonas", "Antanas", "Petras", "Jonas", "Antanas", "Petras"],
            "Assignments": ["Quiz1", "Quiz1", "Quiz1", "Quiz2", "Quiz2", "Quiz2"],
            "Points": [25, 12, 17, 10, 4, 7],
            "Max Points": [30, 30, 30, 15, 15, 15],
        }
        self.input_data = pd.DataFrame(data=mock_values)
        self.input_data.to_excel(self.filename)
        sc = ScoreCalculator(self.filename)
        self.output_data = sc.create_grades_table()

    def test_output_column_qty(self):
        qty_cols = len(self.output_data.columns)
        qty_unique_assignments = len(self.input_data["Assignments"].unique())
        self.assertEqual(
            qty_cols,
            qty_unique_assignments,
            f"Unexpected number of columns in the output. Expected: 2, got {qty_cols}",
        )

    def test_student_name_qty(self):
        qty_names = self.output_data.shape[0]
        qty_unique_names = len(self.input_data["Full Name"].unique())
        self.assertEqual(
            qty_names,
            qty_unique_names,
            f"Unexpected number of students in the output. Expected: 3, got {qty_names}",
        )

    def test_quiz1(self):
        grades = self.output_data["Quiz1"]
        self.assertEqual(
            grades.tolist(),
            [4, 8, 6],
            f"Unexpected grades in Quiz1 column, expected [4, 8, 6], got {grades.tolist}",
        )

    def test_quiz2(self):
        grades = self.output_data["Quiz2"]
        self.assertEqual(
            grades.tolist(),
            [3, 7, 5],
            f"Unexpected grades in Quiz1 column, expected [4, 8, 6], got {grades.tolist}",
        )

    def test_antanas_grades(self):
        output_antanas_grades = self.output_data.loc["Antanas"].values.tolist()
        self.assertEqual(
            output_antanas_grades,
            [3, 4],
            f"Unexpected grades for student Antanas, expected [3, 4], got {output_antanas_grades}",
        )

    def tearDown(self) -> None:
        os.remove("./test_input.xlsx")
        os.remove("./test_output.xlsx")


if __name__ == '__main__':
    unittest.main()
