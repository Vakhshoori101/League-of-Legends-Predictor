from crontab import CronTab
import os

if __name__ == "__main__":
    username = input('Please enter your computer\'s username: ')
    python_path = input('Enter python interpreter path: ')
    current_directory = os.getcwd()
    my_cron = CronTab(user=username)
    job = my_cron.new(command=f'cd {current_directory} && {python_path} main.py >> output.txt')
    job.minute.every(5)
    my_cron.write()