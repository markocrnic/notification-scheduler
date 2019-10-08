from crontab import CronTab

cron = CronTab(user='username')
job = cron.new(command='python test1.py')
job.minute.every(1)

cron.write()