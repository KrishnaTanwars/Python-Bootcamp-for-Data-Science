marks = [1,2,6,8,9]
extra_marks = [56,89,78,75]
print(marks)
marks.append(56) # Change the original list
marks.extend(extra_marks)
marks.pop()
print(marks)