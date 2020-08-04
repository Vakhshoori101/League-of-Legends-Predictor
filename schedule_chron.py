from crontab import CronTab

if __name__ == "__main__":
    my_cron = CronTab(user='Rostam Vakhshoori')
    job = my_cron.new(command='cd /Users/rostamvakhshoori/Desktop/GitHub/League-of-Legends-Predictor && /usr/local/bin/python3.7 main.py >> output.txt')
    job.minute.every(5)
    my_cron.write()