import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses['class'].value_counts()
    classes_more_than_5 = class_counts[class_counts >= 5].reset_index()
    classes_more_than_5.columns = ['class', 'count']
    return classes_more_than_5[['class']]

def test_find_classes():
    data = {
        'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'class': ['Math', 'Science', 'Math', 'History', 'Science', 'Math', 'Math', 'History', 'Science', 'Math', 'Science', 'Math']
    }
    courses_df = pd.DataFrame(data)
    
    result_df = find_classes(courses_df)
    print(result_df)

test_find_classes()