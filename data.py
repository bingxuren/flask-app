developer_data = {}
manager_data = {}


def setup():
    from .schema import Developer, Manager
    global developer_data, manager_data
    thomas = Developer(
        id='1000',
        name='Thomas Schlegel',
        teammates=['1001', '1002', '1003', '1004'],
        team_of=[1, 2, 3],
        gender='male',
    )

    bingxu = Developer(
        id='1001',
        name='Bingxu Ren',
        teammates=['1000', '1002', '1003'],
        team_of=[1, 2],
        gender='male',
    )

    carlos = Developer(
        id='1002',
        name='Carlos Torres',
        teammates=['1000', '1001', '1003'],
        team_of=[1, 2],
        gender='male',
    )

    macie = Developer(
        id='1003',
        name='Macie Kluting',
        teammates=['1000', '1001', '1002'],
        team_of=[1, 2],
        gender='female',
    )

    aaron = Developer(
        id='1004',
        name='Bingxu Ren',
        teammates=['1000', '1001', '1003'],
        team_of=[1, 2],
        gender='male',
    )

    developer_data = {
        '1000': thomas,
        '1001': bingxu,
        '1002': carlos,
        '1003': macie,
        '1004': aaron,
    }

    tony = Manager(
        id='2000',
        name='Tony Nigreli',
        teammates=['1000', '1001', '1002', '1003', '1004'],
        team_of=[3],
        role='project',
    )

    jarrod = Manager(
        id='2001',
        name='Jarrod Marshall',
        teammates=['1000', '1001', '1002', '1003', '1004'],
        team_of=[1, 2, 3],
        role='lead',
    )

    greg = Manager(
        id='2002',
        name='Greg Pierce',
        teammates=['1000', '2000', '2001', '1004'],
        team_of=[3],
        role='project',
    )

    manager_data = {
        '2000': tony,
        '2001': jarrod,
        '2002': greg,
    }


def get_developer(id):
    return developer_data.get(id)


def get_manager(id):
    return manager_data.get(id)


def get_employee(id):
    return developer_data.get(id) or manager_data.get(id)


def get_teammates(employee):
    return map(get_employee, employee.teammates)
