import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    if person.empty:
        return
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)

def test_delete_duplicate_emails():
    # Test Case 1: Basic scenario with one duplicate email
    print("\n--- Test Case 1: Basic Duplicates ---")
    data1 = {'id': [3, 1, 2], 'email': ['c@d.com', 'a@b.com', 'a@b.com']}
    person1 = pd.DataFrame(data1)
    print("Initial DataFrame:\n", person1)
    delete_duplicate_emails(person1)
    print("Final DataFrame:\n", person1) # Expected: Rows with id 1 and 3

    # Test Case 2: No duplicate emails
    print("\n--- Test Case 2: No Duplicates ---")
    data2 = {'id': [3, 1, 2], 'email': ['c@d.com', 'a@b.com', 'e@f.com']}
    person2 = pd.DataFrame(data2)
    print("Initial DataFrame:\n", person2)
    delete_duplicate_emails(person2)
    print("Final DataFrame:\n", person2) # Expected: All rows, sorted by id

    # Test Case 3: All emails are duplicates
    print("\n--- Test Case 3: All Duplicates ---")
    data3 = {'id': [3, 2, 1], 'email': ['a@b.com', 'a@b.com', 'a@b.com']}
    person3 = pd.DataFrame(data3)
    print("Initial DataFrame:\n", person3)
    delete_duplicate_emails(person3)
    print("Final DataFrame:\n", person3) # Expected: Only the row with id 1

    # Test Case 4: Empty DataFrame
    print("\n--- Test Case 4: Empty DataFrame ---")
    data4 = {'id': [], 'email': []}
    person4 = pd.DataFrame(data4)
    print("Initial DataFrame:\n", person4)
    delete_duplicate_emails(person4)
    print("Final DataFrame:\n", person4) # Expected: Empty DataFrame

    # Test Case 5: DataFrame with a single row
    print("\n--- Test Case 5: Single Row ---")
    data5 = {'id': [1], 'email': ['test@test.com']}
    person5 = pd.DataFrame(data5)
    print("Initial DataFrame:\n", person5)
    delete_duplicate_emails(person5)
    print("Final DataFrame:\n", person5) # Expected: The same single row

    # Test Case 6: Multiple groups of duplicates
    print("\n--- Test Case 6: Multiple Duplicate Groups ---")
    data6 = {'id': [1, 2, 3, 4, 5], 'email': ['x@y.com', 'a@b.com', 'x@y.com', 'c@d.com', 'a@b.com']}
    person6 = pd.DataFrame(data6)
    print("Initial DataFrame:\n", person6)
    delete_duplicate_emails(person6)
    print("Final DataFrame:\n", person6) # Expected: Rows with id 1, 2, and 4

    # Test Case 7: IDs are already sorted
    print("\n--- Test Case 7: IDs Already Sorted ---")
    data7 = {'id': [1, 2, 3], 'email': ['a@b.com', 'c@d.com', 'a@b.com']}
    person7 = pd.DataFrame(data7)
    print("Initial DataFrame:\n", person7)
    delete_duplicate_emails(person7)
    print("Final DataFrame:\n", person7) # Expected: Rows with id 1 and 2

    # Test Case 8: IDs in reverse sorted order
    print("\n--- Test Case 8: IDs in Reverse Order ---")
    data8 = {'id': [3, 2, 1], 'email': ['a@b.com', 'c@d.com', 'a@b.com']}
    person8 = pd.DataFrame(data8)
    print("Initial DataFrame:\n", person8)
    delete_duplicate_emails(person8)
    print("Final DataFrame:\n", person8) # Expected: Rows with id 1 and 2

    # Test Case 9: DataFrame with additional columns
    print("\n--- Test Case 9: With Additional Columns ---")
    data9 = {'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Carol'], 'email': ['a@b.com', 'c@d.com', 'a@b.com']}
    person9 = pd.DataFrame(data9)
    print("Initial DataFrame:\n", person9)
    delete_duplicate_emails(person9)
    print("Final DataFrame:\n", person9) # Expected: Rows for Alice (id 1) and Bob (id 2)

    # Test Case 10: Case-sensitive email check
    print("\n--- Test Case 10: Case-Sensitive Emails ---")
    data10 = {'id': [1, 2, 3], 'email': ['john@test.com', 'John@test.com', 'jane@test.com']}
    person10 = pd.DataFrame(data10)
    print("Initial DataFrame:\n", person10)
    delete_duplicate_emails(person10)
    print("Final DataFrame:\n", person10) # Expected: All three rows are kept, as emails are unique

test_delete_duplicate_emails()