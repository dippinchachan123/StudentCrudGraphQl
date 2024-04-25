import graphene
from graphene_django.types import DjangoObjectType
from .models import Student


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    student = graphene.Field(StudentType, id=graphene.Int())

    def resolve_all_students(self, info):
        return Student.objects.all()

    def resolve_student(self, info, id):
        return Student.objects.get(pk=id)


class CreateStudent(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        age = graphene.Int()
        rollno = graphene.String()
        student_class = graphene.String()
        gender = graphene.String()

    student = graphene.Field(StudentType)

    def mutate(self, info, name, age, rollno, student_class, gender):
        student = Student.objects.create(
            name=name,
            age=age,
            rollno=rollno,
            student_class=student_class,
            gender=gender,
        )
        return CreateStudent(student=student)


class UpdateStudent(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        age = graphene.Int()
        rollno = graphene.String()
        student_class = graphene.String()
        gender = graphene.String()

    student = graphene.Field(StudentType)

    def mutate(self, info, id, **kwargs):
        student = Student.objects.get(pk=id)
        for key, value in kwargs.items():
            setattr(student, key, value)
        student.save()
        return UpdateStudent(student=student)


class DeleteStudent(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    student = graphene.Field(StudentType)

    def mutate(self, info, id):
        student = Student.objects.get(pk=id)
        student.delete()
        return DeleteStudent(student=student)


class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
