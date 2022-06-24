from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from .serializers import JobPostSerializer,JobPostSkillSetSerializer
from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]
    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        data = JobPost.objects.filter(
            Q(skillset__name__in= skills)
            )
        if data.exists():
            serializer = JobPostSerializer(data, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)


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

