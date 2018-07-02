import graphene

class Query(graphene.ObjectType):
    greeting = graphene.String(name=graphene.String(default_value='stranger'))

    def say_hello(self, info, name):
        return 'hello %s' % name

schema = graphene.Schema(query=Query)

result = schema.execute('{ hello }')
print(result.data['hello'])
