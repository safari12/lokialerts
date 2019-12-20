import click


from lokialerts.container import service_node_db, service_node_inquirer, service_node_table


@click.group()
def cli():
    pass


@cli.command()
def add_service_node():
    sn = service_node_inquirer.prompt_add()
    sn_nodes = service_node_db.add(sn)
    service_node_table.show(sn_nodes)


@cli.command()
def show_service_nodes():
    sn_nodes = service_node_db.all()
    service_node_table.show(sn_nodes)
