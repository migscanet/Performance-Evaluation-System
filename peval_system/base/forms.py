from django import forms
from .models import *
<<<<<<< HEAD
from users.models import User, FacultyProfile, UnitHeadProfile, DepartmentHeadProfile, AdminProfile

class EducationalAttainmentForm(forms.ModelForm):
    class Meta:
        model = AddEducationalAttainment
        fields = [
            'institution',
            'degree',
            'certification',
            'major',
            'specialization',
            'degree_type',
            'start_date',
            'end_date',
            'proof',
            'is_approved',
            'is_verified',
            'comments_remarks'
        ]

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = AddWorkExperience
        fields = [
            'is_within',
            'employer_name',
            'position',
            'start_date',
            'end_date',
            'description',
            'proof',
            'is_approved',
            'is_verified',
            'comments_remarks'
        ]

class AccomplishmentsEventsForm(forms.ModelForm):
    class Meta:
        model = AddAccomplishmentsEvents
        fields = [
            'accomplishment_title',
            'type',
            'description',
            'start_date',
            'end_date',
            'date_created',
            'image',
            'comments_remarks',
            'is_verified',
            'is_approved'
        ]

class PublicationsForm(forms.ModelForm):
    class Meta:
        model = AddPublications
        fields = [
            'is_dpsm',
            'publication_name',
            'citation',
            'url',
            'date_published',
            'is_approved',
            'is_verified',
            'comments_remarks',
            'publication_type',
            'publication_location',
            'volume_issue_num',
            'publication_url',
            'publication_doi',
            'publication_isbn',
            'is_isi',
            'is_elseviers_scopus',
            'is_ched_recognized',
            'other_collection',
            'is_funded_up_gaa',
            'uiob',
            'proof_publication',
            'proof_utilization',
            'is_presented'
        ]

class TrainingSeminarsForm(forms.ModelForm):
    class Meta:
        model = AddTrainingSeminars
        fields = [
            'training_name',
            'role',
            'remarks',
            'start_date',
            'end_date',
            'proof',
            'is_approved',
            'is_verified'
            'comments_remarks'
        ]

class ResearchGrantsForm(forms.ModelForm):
    class Meta:
        model = AddResearchGrants
        fields  = [
            'is_dpsm',
            'research_name',
            'sponsor_name',
            'grant_amount',
            'project_start_date',
            'project_end_date',
            'actual_start_date',
            'actual_end_date',
            'research_progress',
            'is_approved',
            'is_verified',
            'comments_remarks'
        ]

class LicensureExamForm(forms.ModelForm):
    model = AddLicensureExam
    fields = [
        'exam_name',
        'rank',
        'license_number',
        'date_exam',
        'proof',
        'is_approved',
        'is_verified',
        'comments_remarks'
    ]

class ConferenceWorkshopsForm(forms.ModelForm):
    model = AddConferenceWorkshops
    fields = [
        'event_name',
        'paper_title',
        'presentaiton_type',
        'conference_title',
        'organizer_name',
        'conference_location',
        'conference_venue',
        'start_date',
        'end_date',
        'presentation_date',
        'fund_source',
        'uriob',
        'is_verified',
        'is_approved',
        'comments_remarks'
    ]

class FacultyServiceRecordForm(models.Model):
    model = FacultyServiceRecord
    fields = [
        'course_code',
        'section',
        'semester',
        'school_year',
        'days',
        'time',
        'number_students',
        'comments'
    ]
=======

class EducAttForm(forms.ModelForm):
    class Meta:
        model = EducationalAttainment
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks' ]

class WorkExpForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class AccEventsForm(forms.ModelForm):
    class Meta:
        model = AccomplishmentsEvents
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks', 'date_created']

class PubForm(forms.ModelForm):
    class Meta:
        model = Publications
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class ResearchGrantsForm(forms.ModelForm):
    class Meta:
        model = ResearchGrants
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class LicExamForm(forms.ModelForm):
    class Meta:
        model = LicensureExam
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class TrainSemForm(forms.ModelForm):
    class Meta:
        model = TrainingSeminars
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class ConfWorkForm(forms.ModelForm):
    class Meta:
        model = ConferenceWorkshops
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class ExtServForm(forms.ModelForm):
    class Meta:
        model = ExtensionServices
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']

class FacultyServRecForm(forms.ModelForm):
    class Meta:
        model = FacultyServiceRecord
        #exclude = ('blood_requisition_request',)
        exclude = ['user', 'is_approved', 'is_verified', 'comments_remarks']


>>>>>>> d655bb4b763119d03bf45f6346477afa881f40f6
