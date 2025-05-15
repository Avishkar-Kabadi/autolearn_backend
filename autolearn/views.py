from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema

from .models import Skill, Internship, UserSkill, UserInternship
from .serializers import SkillSerializer, InternshipSerializer, UserSkillSerializer, UserInternshipSerializer


# --- Skill Views ---
class SkillListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="List all skills",
        responses={200: SkillSerializer(many=True)},
    )
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new skill",
        request_body=SkillSerializer,
        responses={201: SkillSerializer},
    )
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SkillDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Get skill by ID",
        responses={200: SkillSerializer, 404: 'Not Found'}
    )
    def get(self, request, pk):
        skill = self.get_object(pk)
        if not skill:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update skill by ID",
        request_body=SkillSerializer,
        responses={200: SkillSerializer, 400: 'Bad Request', 404: 'Not Found'}
    )
    def put(self, request, pk):
        skill = self.get_object(pk)
        if not skill:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete skill by ID",
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self, request, pk):
        skill = self.get_object(pk)
        if not skill:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Internship Views ---
class InternshipListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="List all internships",
        responses={200: InternshipSerializer(many=True)},
    )
    def get(self, request):
        internships = Internship.objects.all()
        serializer = InternshipSerializer(internships, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new internship",
        request_body=InternshipSerializer,
        responses={201: InternshipSerializer},
    )
    def post(self, request):
        serializer = InternshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InternshipDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Internship.objects.get(pk=pk)
        except Internship.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Get internship by ID",
        responses={200: InternshipSerializer, 404: 'Not Found'}
    )
    def get(self, request, pk):
        internship = self.get_object(pk)
        if not internship:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = InternshipSerializer(internship)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update internship by ID",
        request_body=InternshipSerializer,
        responses={200: InternshipSerializer, 400: 'Bad Request', 404: 'Not Found'}
    )
    def put(self, request, pk):
        internship = self.get_object(pk)
        if not internship:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = InternshipSerializer(internship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete internship by ID",
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self, request, pk):
        internship = self.get_object(pk)
        if not internship:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        internship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- UserSkill Views ---
class UserSkillListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="List your skills with progress",
        responses={200: UserSkillSerializer(many=True)},
    )
    def get(self, request):
        user_skills = UserSkill.objects.filter(user=request.user)
        serializer = UserSkillSerializer(user_skills, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Add a skill to your profile with progress",
        request_body=UserSkillSerializer,
        responses={201: UserSkillSerializer},
    )
    def post(self, request):
        serializer = UserSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSkillDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return UserSkill.objects.get(pk=pk, user=user)
        except UserSkill.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Get your skill progress by ID",
        responses={200: UserSkillSerializer, 404: 'Not Found'}
    )
    def get(self, request, pk):
        user_skill = self.get_object(pk, request.user)
        if not user_skill:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSkillSerializer(user_skill)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update your skill progress by ID",
        request_body=UserSkillSerializer,
        responses={200: UserSkillSerializer, 400: 'Bad Request', 404: 'Not Found'}
    )
    def put(self, request, pk):
        user_skill = self.get_object(pk, request.user)
        if not user_skill:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSkillSerializer(user_skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete your skill progress by ID",
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self, request, pk):
        user_skill = self.get_object(pk, request.user)
        if not user_skill:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        user_skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- UserInternship Views ---
class UserInternshipListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="List your internships with progress",
        responses={200: UserInternshipSerializer(many=True)},
    )
    def get(self, request):
        user_internships = UserInternship.objects.filter(user=request.user)
        serializer = UserInternshipSerializer(user_internships, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Add an internship to your profile with progress",
        request_body=UserInternshipSerializer,
        responses={201: UserInternshipSerializer},
    )
    def post(self, request):
        serializer = UserInternshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInternshipDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return UserInternship.objects.get(pk=pk, user=user)
        except UserInternship.DoesNotExist:
            return None

    @swagger_auto_schema(
        operation_description="Get your internship progress by ID",
        responses={200: UserInternshipSerializer, 404: 'Not Found'}
    )
    def get(self, request, pk):
        user_internship = self.get_object(pk, request.user)
        if not user_internship:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserInternshipSerializer(user_internship)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update your internship progress by ID",
        request_body=UserInternshipSerializer,
        responses={200: UserInternshipSerializer, 400: 'Bad Request', 404: 'Not Found'}
    )
    def put(self, request, pk):
        user_internship = self.get_object(pk, request.user)
        if not user_internship:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserInternshipSerializer(user_internship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete your internship progress by ID",
        responses={204: 'No Content', 404: 'Not Found'}
    )
    def delete(self, request, pk):
        user_internship = self.get_object(pk, request.user)
        if not user_internship:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        user_internship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
