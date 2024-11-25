from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    name1='Ivan'
    courses1={'progr':['a','b'], 'course2':['c','d']}

    def setUp(self):
        self.student1 = Student(self.name1, {'progr':['a','b'], 'course2':['c','d']})
        self.student2 = Student('Gosho')

    def test_init(self):
        self.assertEqual(self.name1, self.student1.name)
        self.assertEqual(self.courses1, self.student1.courses)
        self.assertEqual({}, self.student2.courses)
        self.assertIsInstance(self.student1.name, str)
        self.assertIsInstance(self.student1.courses, dict)

    def test_enroll_existing_course(self):
        result=self.student1.enroll('progr', ['w','e'], 'Y')
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'progr':['a','b', 'w','e'], 'course2':['c','d']}, self.student1.courses)

    def test_enroll_not_existing_course_add_notes_with_Y(self):
        result=self.student1.enroll('c#', ['w','e'], 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertIn('c#', self.student1.courses)
        self.assertEqual(['w','e'], self.student1.courses['c#'])

    def test_enroll_not_existing_course_empty_string(self):
        result=self.student1.enroll('c#', ['w','e'], '')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertIn('c#', self.student1.courses)
        self.assertEqual(['w','e'], self.student1.courses['c#'])

    def test_not_existing_course_no_notes(self):
        result = self.student1.enroll('c#', ['w', 'e'], 'N')
        self.assertEqual("Course has been added.", result)
        self.assertIn('c#', self.student1.courses)
        self.assertEqual([], self.student1.courses['c#'])

    def test_add_notes_success(self):
        result=self.student1.add_notes('progr', 's')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['a','b', 's'], self.student1.courses['progr'])

    def test_add_notes_failure(self):
        with self.assertRaises(Exception) as context:
            self.student2.add_notes('progr', 's')
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_leave_success(self):
        result=self.student1.leave_course('progr')
        self.assertEqual("Course has been removed", result)
        self.assertNotIn('progr', self.student1.courses)

    def test_leave_failure(self):
        with self.assertRaises(Exception) as context:
            self.student1.leave_course('rr')
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))


if __name__ == '__main__':
    main()
