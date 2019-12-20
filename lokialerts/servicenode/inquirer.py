import inquirer


def prompt_add():
    return inquirer.prompt([
        inquirer.Text('ip', message='Enter ip of service node'),
        inquirer.Text('label', message='Enter label of service node')
    ])
