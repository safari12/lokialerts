import schedule
import time
import click
import importlib


class Scheduler:
    def __init__(self, jobs):
        self.jobs = jobs

    def run(self):
        click.echo('Scheduler started')
        for j in self.jobs:
            click.echo('Scheduled %s' % j.__class__.__name__)
            schedule.every(10).seconds.do(j.run)

        while True:
            schedule.run_pending()
            time.sleep(1)
