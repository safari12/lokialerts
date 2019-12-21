import click


from lokialerts.container import sn_db, sn_inquirer, sn_table, scheduler


@click.group()
def cli():
    pass


@cli.command()
def add_service_node():
    sn = sn_inquirer.prompt_add()
    sn_nodes = sn_db.add(sn)
    sn_table.show(sn_nodes)


@cli.command()
def remove_service_node():
    sn_nodes = sn_db.all()
    sn_table.show(sn_nodes)
    result = sn_inquirer.prompt_remove()
    sn_id = int(result['sn_id'])
    deleted_sn = sn_db.remove(sn_id)
    click.echo("Successfully removed %s" % deleted_sn['label'])


@cli.command()
def show_service_nodes():
    sn_nodes = sn_db.all()
    sn_table.show(sn_nodes)


@cli.command()
def run_scheduler():
    scheduler.run()
