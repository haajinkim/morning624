from rest_framework import serializers
from .models import Company, JobPost, JobPostSkillSet
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields= ["company_name","business_area"]


class JobPostSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSkillSet    
        fields= ["skill_set","job_post"]       
    def create(self, validated_data):
            print(validated_data)

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ["job_type","company","job_description","salary"]

    def create(self, validated_data):
            job_post = JobPost(**validated_data)
            company = validated_data.pop('company')
            new_company,_ =JobPost.objects.get_or_create(id=company.id)
            JobPost.company=new_company 
            # add 는 many to many 에서 list를 풀은것을 짚어넣어야함
            # one to mnay 는 바로 = 집어 넣을 수 잇음.(object)
            # add 는 id값
            job_post.save()
            return job_post
