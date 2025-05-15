from django.urls import path
from .views import (
    SkillListCreateView, SkillDetailView,
    InternshipListCreateView, InternshipDetailView,
    UserSkillListCreateView, UserSkillDetailView,
    UserInternshipListCreateView, UserInternshipDetailView,
)

urlpatterns = [
    # Skill endpoints
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
    path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill-detail'),

    # Internship endpoints
    path('internships/', InternshipListCreateView.as_view(), name='internship-list-create'),
    path('internships/<int:pk>/', InternshipDetailView.as_view(), name='internship-detail'),

    # UserSkill endpoints
    path('user-skills/', UserSkillListCreateView.as_view(), name='user-skill-list-create'),
    path('user-skills/<int:pk>/', UserSkillDetailView.as_view(), name='user-skill-detail'),

    # UserInternship endpoints
    path('user-internships/', UserInternshipListCreateView.as_view(), name='user-internship-list-create'),
    path('user-internships/<int:pk>/', UserInternshipDetailView.as_view(), name='user-internship-detail'),
]
