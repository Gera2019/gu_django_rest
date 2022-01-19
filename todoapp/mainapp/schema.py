import graphene
from graphene_django import DjangoObjectType
from .models import Project, TodoNote, TodoUser


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoNoteType(DjangoObjectType):
    class Meta:
        model = TodoNote
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = TodoUser
        fields = '__all__'

class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_todonotes = graphene.List(TodoNoteType)
    all_users = graphene.List(UserType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todonotes(root, info):
        return TodoNote.objects.all()

    def resolve_all_users(root, info):
        return TodoUser.objects.all()

    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))

    def resolve_project_by_id(self, info, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return None

    todonotes_by_user_id = graphene.List(TodoNoteType, id=graphene.Int(required=False))
    todonotes_by_project_name = graphene.List(TodoNoteType, name=graphene.String(required=False))
    project_by_name = graphene.Field(ProjectType, name=graphene.String(required=True))

    def resolve_todonotes_by_user_id(self, info, id=None):
        todonotes = TodoNote.objects.all()
        if id:
            todonotes = todonotes.filter(userid__id=id)
        return todonotes



    def resolve_project_by_name(self, info, name):
        try:
            return Project.objects.get(name=name)
        except Project.DoesNotExist:
            return None

    def resolve_todonotes_by_project_name(self, info, name=None):
        todonotes = TodoNote.objects.all()
        # projects = Project.objects.all()
        if name:
            project = Project.objects.get(name=name)
            print('project', project)
            todonotes = todonotes.filter(projectid__id=project.id)
        return todonotes

class UserMutation(graphene.Mutation):
    class Arguments:
        age = graphene.Int(required=True)
        email = graphene.String()
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, age, email, id):
        user = TodoUser.objects.get(pk=id)
        user.email = email
        user.age = age
        user.save()
        return UserMutation(user=user)

class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
