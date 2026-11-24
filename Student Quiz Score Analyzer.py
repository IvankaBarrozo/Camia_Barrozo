scores = []

for i in range(1,6):
    score = int(input(f"Enter quiz {i} score: "))
    scores.append(score)

num = len(scores)
total = sum(scores)
highest = max(scores)
lowest = min(scores)
ascending = sorted(scores)
descending = sorted(scores, reverse=True)
average = total / len(scores)


print("===== QUIZ SCORE REPORT =====")
print(f"Quiz Scores: {scores}")
print(f"Number or quizzes {len(scores)}")
print(f"Average score: {average}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Ascending: {ascending}")
print(f"Descending: {descending}")
print(f"Original Scores: {scores}")