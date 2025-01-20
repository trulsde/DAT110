from scipy.stats import t

# Task 1:
levels = [.9, .98, .95, .99]
sizes = [6, 21, 29, 12]
tasks = ['a', 'b', 'c', 'd']
# a)

for cl, n in zip(levels, sizes):
    print(f"Task {tasks[levels.index(cl)]}:")
    print(f"Critical t-value: {t.ppf(cl, n-1):.3f}\n")

# Task 2:
print("Task 2\n")
T_scores = [1.91, -3.45, 0.83, 2.13]
sizes = [11, 17, 7, 28]

for score, n in zip(T_scores, sizes):
    p_value = t.sf(abs(score), n-1)
    status = "keep"
    sign = ">="
    if p_value < 0.05:
        status = "reject"
        sign = "<"
    print(f"Task {tasks[T_scores.index(score)]}:")
    print(f"P-value: {p_value:.3f}\n{p_value} {sign} 0.05 => {status} null hypothesis\n")

# Task 3
