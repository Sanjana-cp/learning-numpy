import numpy as np
marks=np.array([[85,78,92,88],[72,80,75,70],[90,88,95,92],[60,65,70,68],[88,90,85,87]])
#normalisation
# min_value=np.min(marks)
# print(min_value)

# max_value=np.max(marks)
# print(max_value)

# sub= marks-min_value
# print(sub)

# range=max_value-min_value

# new=sub/range
# print(new)


# math_avg=np.min(marks,axis=0)
# print(math_avg)

# math_avg2=np.max(marks,axis=0)
# print(math_avg2)

# sub_avg=marks-math_avg
# print(sub_avg)

# range2=math_avg-math_avg2

# final=sub_avg/range2

mean=np.mean(marks,axis=0)
# print(mean)

stand=np.std(marks,axis=0)
# print(stand)

z_score1=marks-mean
# print(z_score1)

z_score2=z_score1/stand
# print(z_score2)

table=np.sum(z_score2,axis=1)
# print(table)

tup=z_score2.shape
print(tup[1])

table=table/tup[1]
print(table)

for i in table:
    if i>= +1:
        print("the student is strong")
    elif i<= -1:
        print("the student is weak")
    else:
        print("student is average")
