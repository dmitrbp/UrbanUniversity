number_of_completed_tasks = 12
number_of_spent_hours = 1.5
course_name = "Python"
time_per_task = number_of_spent_hours / number_of_completed_tasks
print("Курс: " + course_name + ",",
      "всего задач: " + str(number_of_completed_tasks) + ",",
      "затрачено часов: " + str(number_of_spent_hours) + ",",
      "среднее время выполнения: " + str(time_per_task) + " часа."
)