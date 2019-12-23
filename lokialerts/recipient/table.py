import click

from prettytable import PrettyTable


class RecipientTable:
    def __init__(self):
        self.field_names = [
            'ID',
            'Label',
            'Email'
        ]

    def show(self, recipients):
        if (len(recipients) > 0):
            table = PrettyTable()
            table.field_names = self.field_names
            table.border = True
            for r in recipients:
                table.add_row([
                    r.doc_id,
                    r['label'],
                    r['email']
                ])
            click.echo(table.get_string())
        else:
            click.echo('No recipients were added')
