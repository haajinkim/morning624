from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from .serializers import JobPostSerializer
from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        # job_type = int(request.data.get("job_type", ""))
        # company = request.data.get("company", "")
        # job_description = request.data.get("job_descriptionm","")
        # salary = request.data.get("salary","")
        jobpostserializer =JobPostSerializer(data= request.data)
        jobpostserializer.is_valid(raise_exception=True)
        jobpostserializer.save()
        return Response(jobpostserializer.data,status=status.HTTP_200_OK)

