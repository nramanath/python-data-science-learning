def horizontal_line(length=50, characterToPrint="_"):
    for _ in range(length):
        print characterToPrint,
        # , ensures that printing is done in the same line
    print "\n"

subjects = ['maths', 'computer science', 'machine learning', 'analytics']
marks = [100, 98, 85, 75]

packedData = zip(subjects, marks)

print packedData

# usually asterisk does the unpacking into lists, and its done as a neat trick

unpackedData_subjects, unpackedData_marks = zip(
    *[('maths', 100), ('computer science', 98), ('machine learning', 85), ('analytics', 75)])

horizontal_line()
print unpackedData_subjects
print unpackedData_marks
