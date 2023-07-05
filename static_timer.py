import datetime
import os
import time

# Expected time
expected_time_string = "2023-08-11 23:59:00"

class color:
    GREEN = '\033[92m'

os.system('cls')

# Get the current time
current_time = datetime.datetime.now()
date_format = '%Y-%m-%d %H:%M:%S'

formatted_current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

while True:
    # Get the current time
    current_time = datetime.datetime.now()
    date_format = '%Y-%m-%d %H:%M:%S'

    formatted_current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    # Define and format the expected time
    formatted_expected_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    # Comparing current time with expected time
    current_time_string = str(formatted_current_time)
    math_current_time = datetime.datetime.strptime(current_time_string, date_format)
    math_expected_time = datetime.datetime.strptime(expected_time_string, date_format)

    difference_time = math_expected_time - math_current_time
    formatted_difference_time = difference_time

    # Tell user the difference
    print(color.GREEN + str(difference_time))
    time.sleep(1)