from email.policy import default
from django.db import models
from users.models import User
from datetime import datetime

SEMESTERCHOICES=(
    ('1', 'First Semester'),
    ('2', 'Second Semester'),
    ('3', 'Mid Year'),
)

DAYCHOICES=(
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
)

PUBLICATIONTYPECHOICES=(
    ('1', 'Peer-reviewed journal article'),
    ('2', 'Book/Monograph'),
    ('3', 'Edited/peer-reviewed book chapter'),
    ('4', 'Peer-reviewed conference paper publication'),
)

PUBLISHERTYPECHOICES=(
    ('1', 'Commercial'),
    ('2', 'Learned society and association'),
)

LOCATIONPUBLISHERCHOICES=(
    ('1', 'Local'),
    ('2', 'International'),
)

PRESENTATIONTYPECHOICES=(
    ('1', 'Oral Presentation'),
    ('2', 'Poster Presentation'),
)

CONFERENCELOCATIONCHOICES=(
    ('1', 'International/in-house'),
    ('2', 'Local/regional'),
    ('3', 'National'),
    ('4', 'International')
)

ACCOMPLISHMENTREPORTCHOICES=(
    ('1', 'Academic Affairs'),
    ('2', 'Student Concerns'),
    ('3', 'International Linkages'),
    ('4', 'Conferences/Workshops'),
    ('5', 'Extension Services (Trainings/Seminars/Workshops conducted)'),
    ('6', 'Research Grants'),
    ('7', 'Publications'),
    ('8', 'Planned Activities and Announcements')
)

class AddEducationalAttainment(models.Model):
    institution = models.CharField(max_length=240)
    degree = models.CharField(max_length=240)
    certification = models.CharField(max_length=240)
    major = models.CharField(max_length=240)
    specialization = models.CharField(max_length=240)
    degree_type = models.CharField(max_length=10)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    proof = models.FileField(upload_to ='uploads/')
    is_approved = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    comments_remarks = models.CharField(max_length=400)

class AddWorkExperience(models.Model):
    is_within = models.BooleanField(default=False)
    employer_name = models.CharField(max_length=240)
    position = models.CharField(max_length=240)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    #Check if max_length should be bigger
    description = models.CharField(max_length=500)
    proof = models.FileField(upload_to ='uploads/')
    is_approved = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    comments_remarks = models.CharField(max_length=400)

class AddAccomplishmentsEvents(models.Model):
    user = models.ForeignKey(User, related_name='addAccomplishmentsEvents', on_delete = models.CASCADE)
    accomplishment_title = models.CharField(max_length=240)
    type = models.CharField(max_length=240, choices=ACCOMPLISHMENTREPORTCHOICES, default=ACCOMPLISHMENTREPORTCHOICES[0])
    description = models.CharField(max_length=500)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    image = models.ImageField()
    comments_remarks = models.CharField(max_length=400)
    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

class AddPublications(models.Model):
    user = models.ForeignKey(User, related_name='addPublications', on_delete = models.CASCADE)
    is_dpsm = models.BooleanField(default=False)
    publication_name = models.CharField(max_length=240)
    citation = models.CharField(max_length=240)
    url = models.URLField(max_length = 240)
    date_published = models.DateField(null=True, blank=True)
    # proof = models.FileField(upload_to ='uploads/')
    is_approved = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    comments_remarks = models.CharField(max_length=400)
    publication_type = models.CharField(max_length=240, choices=PUBLICATIONTYPECHOICES, default=PUBLICATIONTYPECHOICES[0])
    conference_name = models.CharField(max_length=240)
    publisher_name = models.CharField(max_length=240)
    publisher_type = models.CharField(max_length=240, choices=PUBLISHERTYPECHOICES, default=PUBLISHERTYPECHOICES[0])
    publisher_location = models.CharField(max_length=20, choices=LOCATIONPUBLISHERCHOICES, default=LOCATIONPUBLISHERCHOICES[0])
    volume_issue_num = models.CharField(max_length=240)
    publication_url = models.URLField(max_length=250)
    publication_doi = models.CharField(max_length=240)
    publication_isbn = models.CharField(max_length=240)
    is_isi = models.BooleanField(default=False)
    is_elseviers_scopus = models.BooleanField(default=False)
    is_ched_recognized = models.BooleanField(default=False)
    other_collection = models.CharField(max_length=240)
    is_funded_up_gaa = models.BooleanField(default=False)
    uiob = models.CharField(max_length=500)
    proof_publication = models.FileField(upload_to ='uploads/')
    proof_utilization = models.FileField(upload_to ='uploads/')
    is_presented = models.BooleanField(default=False)



class AddTrainingSeminars(models.Model):
    training_name = models.CharField(max_length=240)
    role = models.CharField(max_length=240)
    remarks = models.CharField(max_length=240)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    proof = models.FileField(upload_to ='uploads/')
    is_approved = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    comments_remarks = models.CharField(max_length=400)

# class AddAccomplishments(models.Model):
#     position = models.CharField(max_length=240)
#     organization_name = models.CharField(max_length=240)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)
#     is_within = models.BooleanField(default=False)
#     contributions_profession = models.CharField(max_length=240)
#     contributions_nation = models.CharField(max_length=240)
#     contributions_world = models.CharField(max_length=240)
#     description = models.CharField(max_length=240)
#     proof = models.FileField(upload_to ='uploads/')
#     is_approved = models.BooleanField(default=False)
#     is_verified = models.BooleanField(default=False)
#     comments_remarks = models.CharField(max_length=400)

class AddResearchGrants(models.Model):
    user = models.ForeignKey(User, related_name='addResearchGrants', on_delete = models.CASCADE)
    is_dpsm = models.BooleanField(default=False)
    research_name = models.CharField(max_length=240)
    sponsor_name = models.CharField(max_length=240)
    grant_amount = models.CharField(max_length=240)
    project_start_date = models.DateField(null=True, blank = True)
    project_end_date = models.DateField(null=True, blank = True)
    actual_start_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    research_progress = models.CharField(max_length=240)
    is_approved = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    comments_remarks = models.CharField(max_length=400)

class AddLicensureExam(models.Model):
    exam_name = models.CharField(max_length=240)
    rank = models.CharField(max_length=240)
    license_number = models.CharField(max_length=20)
    date_exam = models.DateField(null=True, blank=True)
    proof = models.FileField(upload_to ='uploads/')
    is_approved = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    comments_remarks = models.CharField(max_length=400)

class AddConferenceWorkshops(models.Model):
    user = models.ForeignKey(User, related_name='addConferenceWorkshops', on_delete = models.CASCADE)
    event_name = models.CharField(max_length=240)
    paper_title = models.CharField(max_length=240)
    presentation_type = models.CharField(max_length=20, choices=PRESENTATIONTYPECHOICES, default=PRESENTATIONTYPECHOICES[0])
    conference_title = models.CharField(max_length=240)
    organizer_name = models.CharField(max_length=240)
    conference_location = models.CharField(max_length=240, choices=CONFERENCELOCATIONCHOICES, default=CONFERENCELOCATIONCHOICES[0])
    conference_venue = models.CharField(max_length=240)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    presentation_date = models.DateField(null=True, blank=True)
    fund_source = models.CharField(max_length=240)
    uriob = models.CharField(max_length=500)
    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    comments_remarks = models.CharField(max_length=500)

class AddExtensionServices(models.Model):
    user = models.ForeignKey(User, related_name='addExtensionServices', on_delete=models.CASCADE)
    training_title = models.CharField(max_length=240)
    venue = models.CharField(max_length=240)
    date = models.DateField(null=True, blank =True)
    number_participants = models.IntegerField(null=True, blank=True)
    target_beneficiary = models.CharField(max_length=240)
    fund_source = models.CharField(max_length=240)
    is_verified = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    attached_evaluation = models.FileField(upload_to ='uploads/')
    comments_remarks = models.CharField(max_length=400)

class FacultyServiceRecord(models.Model):
    #Foreignkey of SET
    course_code = models.CharField(max_length=5)
    section = models.CharField(max_length=4)
    semester = models.CharField(max_length=10, choices=SEMESTERCHOICES, default=SEMESTERCHOICES[0])
    school_year = models.CharField(max_length=4)
    days = models.CharField(max_length=10, choices=DAYCHOICES, default=DAYCHOICES[0])
    time = models.TimeField(null=True, blank=True)
    number_students = models.IntegerField(null=True, blank=True)
    comments_remarks = models.CharField(max_length=400)


