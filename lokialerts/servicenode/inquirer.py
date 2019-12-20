import inquirer


def prompt_add():
    return inquirer.prompt([
        inquirer.Text('ip', message='Enter ip of service node'),
        inquirer.Text('label', message='Enter label of service node')
    ])


def prompt_remove():
    return inquirer.prompt([
        inquirer.Text('sn_id', message='Enter id to remove')
    ])
