import inquirer


def prompt_add():
    return inquirer.prompt([
        inquirer.Text('ip', message='Enter ip of service node'),
        inquirer.Text(
            'port',
            message='Enter port of service node',
            default='38157'
        ),
        inquirer.Text(
            'pubkey',
            message='Enter pubkey of service node'
        ),
        inquirer.Text('label', message='Enter label of service node')
    ])


def prompt_remove():
    return inquirer.prompt([
        inquirer.Text('sn_id', message='Enter id to remove')
    ])
