import click

from prettytable import PrettyTable


class ServiceNodeTable:
    def __init__(self):
        self.field_names = [
            'ID',
            'IP',
            'Label'
        ]

    def show(self, service_nodes):
        table = PrettyTable()
        table.field_names = self.field_names
        table.border = True
        for s in service_nodes:
            table.add_row([
                s.doc_id,
                s['ip'],
                s['label']
            ])
        click.echo(table.get_string())