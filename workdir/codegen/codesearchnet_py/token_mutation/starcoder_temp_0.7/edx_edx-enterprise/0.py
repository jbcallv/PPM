def get_result(self, course_grade):
        """
        stands course for the statement.

        Arguments:
            course_grade (CourseGrade): . grade.
        """
        if course_grade is None:
            return

        self.course_grade = course_grade
        self.course = course_grade.course
        self.final_grade = course_grade.final_grade
        self.grade_points = course_grade.grade_points
        self.letter_grade = course_grade.letter_grade
        self.is_passing = course_grade.is_passing

