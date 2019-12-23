import inquirer


def prompt_add():
    return inquirer.prompt({
        inquirer.Text('email', message='Enter email'),
        inquirer.Text('label', message='Enter label')
    })


def prompt_remove():
    return inquirer.prompt({
        inquirer.Text('id', message='Enter id of recipient to remove')
    })
