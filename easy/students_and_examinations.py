import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_combinations = pd.merge(students, subjects, how='cross')

    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    
    result = pd.merge(all_combinations, exam_counts, how='outer', on=['student_id', 'subject_name']).fillna(0).sort_values(['student_id', 'subject_name'], ascending=True)
    
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]

def test_students_and_examinations():
    students = pd.DataFrame({
        'student_id': [1, 2],
        'student_name': ['Alice', 'Bob']
    })

    subjects = pd.DataFrame({
        'subject_name': ['Math', 'Science']
    })

    examinations = pd.DataFrame({
        'student_id': [1, 1, 2],
        'subject_name': ['Math', 'Science', 'Math']
    })

    expected_output = pd.DataFrame({
        'student_id': [1, 1, 2, 2],
        'student_name': ['Alice', 'Alice', 'Bob', 'Bob'],
        'subject_name': ['Math', 'Science', 'Math', 'Science'],
        'attended_exams': [1.0, 1.0, 1.0, 0.0]
    })

    result = students_and_examinations(students, subjects, examinations)
    print(result)
    assert result.equals(expected_output), "Test case failed!"

test_students_and_examinations()