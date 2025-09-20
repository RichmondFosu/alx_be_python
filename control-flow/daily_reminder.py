# Process task based on priority and time sensitivity
match priority:
    case 'high':
        message = f"{task} is a {priority} priority task "
    case 'medium':
        message = f"{task} is a {priority} priority task "
    case 'low':
        message = f"{task} is a {priority} priority task "

if time_bound == 'yes':
    message += 'that requires immediate attention today!'
else:
    message += '. Consider completing it in your free time.'

print('Reminder:', message)