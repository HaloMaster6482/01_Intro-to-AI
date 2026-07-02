def introduction():
  print("Welcome to the score check system, User. What is your name?")
  name = input()
  print(f"Hello, {name}!")
  return name


def get_subject_scores():
  subjects = ["English", "Mathematics", "Science"]
  subject_scores = []

  for subject in subjects:
    # Convert the input to an integer
    subject_scores.append(int(input(f"Enter your score (%) in {subject}: ")))

  return subject_scores

def give_result(student_name, subject_score):
  mean = sum(subject_score) / len(subject_score)
  if mean == 100:
    print("Congratulations on getting a perfect score!!! :) :)")
  elif mean >= 90:
    print("Good job! :)")
  elif mean >= 50:
    print("Congrats on passing in the exams! :|")
  else:
    print("You are a failiure! Try again next year. :(")

def main():
  name = introduction()
  subject_scores = get_subject_scores()
  give_result(name, subject_scores)

main()