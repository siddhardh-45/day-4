reg = 668
print("  your register number is :", reg)
n = int(input("Enter number of  scores: "))
scores = []
for i in range(n):
    scores += [int(input("Enter the score: "))]
low_risk = []
medium_risk = []
high_risk = []
critical_risk = []
ignored_count = 0
valid_count = 0
removed_count = 0

for score in scores:
    if score < 0:
        ignored_count += 1
    elif 0 <= score <= 30:
        low_risk += [score]
        valid_count += 1
    elif 31 <= score <= 60:
        medium_risk += [score]
        valid_count += 1
    elif 61 <= score <= 100:
        high_risk += [score]
        valid_count += 1
    else:
        critical_risk += [score]
        valid_count += 1
if  reg% 2== 0:
    removed_count = len(low_risk)
    low_risk = []
else:
    removed_count = len(critical_risk)
    critical_risk = []
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)
print("Total Valid Entries:", valid_count)
print("Total Ignored Entries:", ignored_count)
print("Entries Removed Due to Personalization:", removed_count)




