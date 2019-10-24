import Question_Handler as QH

questions = QH.Unpack_Questions()

greatest_length = 0

for q in questions:
    if len(q[1]) > greatest_length:
        greatest_length = len(q[1])
    if len(q[2]) > greatest_length:
        greatest_length = len(q[2])

print(greatest_length)