from crontab import CronTab

if __name__ == "__main__":
    username = input('Please enter your computer\'s username: ')
    my_cron = CronTab(user=username)
    for job in my_cron:
        if job.comment == 'League-Bot':
            my_cron.remove(job)
            my_cron.write()