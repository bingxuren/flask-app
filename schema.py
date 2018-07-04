import graphene

from .data import get_developer, get_employee, get_manager, get_teammates


class Team(graphene.Enum):
    UI = 0
    FRONTEND = 1
    BACKEND = 2
    MANAGEMENT = 3


# noinspection PyTypeChecker
class Employee(graphene.Interface):
    id = graphene.ID()
    name = graphene.String()
    teammates = graphene.List(lambda: Employee)
    team_of = graphene.List(Team)

    def resolve_teammates(self, info):
        return [get_teammates(t) for t in self.teammates]


class Developer(graphene.ObjectType):

    class Meta:
        interfaces = (Employee, )

    gender = graphene.String()


class Manager(graphene.ObjectType):

    class Meta:
        interfaces = (Employee, )
    role = graphene.String()


class Query(graphene.ObjectType):
    employee = graphene.Field(Employee, id=graphene.String())
    developer = graphene.Field(Developer, id=graphene.String())
    manager = graphene.Field(Manager, id=graphene.String())

    def resolve_employee(self, info, id):
        return get_employee(id)

    def resolve_developer(self, info, id):
        return get_developer(id)

    def resolve_manager(self, info, id):
        return get_manager(id)


schema = graphene.Schema(query=Query)
