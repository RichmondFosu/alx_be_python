#Prompt for task
task = input('Describe the task: ')
priority = input('What is the task priority? (high, medium, low): ').lower()
time_bound = input('Is the task time-bound? (yes or no): ').lower()


# Process task based on priority 
match priority:
    case 'high':
        message = f"{task} is a {priority} priority task "
    case 'medium':
        message = f"{task} is a {priority} priority task "
    case 'low':
        message = f"{task} is a {priority} priority task "

#based on time sensitivity
if time_bound == 'yes':
    message += 'that requires immediate attention today!'
else:
    message += '. Consider completing it in your free time.'

print('Reminder:', message)