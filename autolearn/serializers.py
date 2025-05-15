from rest_framework import serializers
from .models import Skill, Internship, UserSkill, UserInternship

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description', 'proficiency_level']

class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = ['id', 'title', 'company', 'start_date', 'end_date', 'status']

class UserSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)
    skill_id = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), source='skill', write_only=True)
    
    class Meta:
        model = UserSkill
        fields = ['id', 'skill', 'skill_id', 'progress', 'last_updated']

class UserInternshipSerializer(serializers.ModelSerializer):
    internship = InternshipSerializer(read_only=True)
    internship_id = serializers.PrimaryKeyRelatedField(queryset=Internship.objects.all(), source='internship', write_only=True)

    class Meta:
        model = UserInternship
        fields = ['id', 'internship', 'internship_id', 'application_status', 'notes']
