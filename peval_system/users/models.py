from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

SEXCHOICES=(
    ('1', 'Male'),
    ('2', 'Female'),
)

CIVILSTATUSCHOICES=(
    ('1', 'Married'),
    ('2', 'Single'),
    ('3', 'Divorced'),
    ('4', 'Separated'),
    ('5', 'Widowed'),
)

FACULTYRANKCHOICES=(
    ('1', 'Instructor 1'),
    ('2', 'Instructor 2'),
    ('3', 'Instructor 3'),
    ('4', 'Instructor 4'),
    ('5', 'Instructor 5'),
    ('6', 'Instructor 6'),
    ('7', 'Instructor 7'),
    ('8', 'Assistant Professor 1'),
    ('9', 'Assistant Professor 2'),
    ('10', 'Assistant Professor 3'),
    ('11', 'Assistant Professor 4'),
    ('12', 'Assistant Professor 5'),
    ('13', 'Assistant Professor 6'),
    ('14', 'Assistant Professor 7'),
    ('15', 'Associate Professor 1'),
    ('16', 'Associate Professor 2'),
    ('17', 'Associate Professor 3'),
    ('18', 'Associate Professor 4'),
    ('19', 'Associate Professor 5'),
    ('20', 'Associate Professor 6'),
    ('21', 'Associate Professor 7'),
    ('22', 'Professor 1'),
    ('23', 'Professor 2'),
    ('24', 'Professor 3'),
    ('25', 'Professor 4'),
    ('26', 'Professor 5'),
    ('27', 'Professor 6'),
    ('28', 'Professor 7'),
    ('29', 'Professor 8'),
    ('30', 'Professor 9'),
    ('31', 'Professor 10'),
    ('32', 'Professor 11'),
    ('33', 'Professor 12'),
    ('34', 'University Professor'),
)

FACULTYCLASSIFICATIONCHOICES=(
    ('1', 'Full-time'),
    ('2', 'Part-time'),
)

FACULTYTENURECHOICES=(
    ('1', 'Temporary'),
    ('2', 'Permanent'),
)

FACULTYSTATUSCHOICES=(
    ('1', 'Active service'),
    ('2', 'On study leave with pay'),
    ('3', 'On study leave without pay'),
    ('4', 'On sabbatical leave'),
    ('5', 'On secondment'),
    ('6', 'Retired'),
    ('7', 'Resigned'),
    ('8', 'AWOL'),
)

DEPARTMENTCHOICES=(
    ('1', 'Mathematical and Computing Sciences Unit (MCSU)'),
    ('2', 'Chemistry Unit (CU)'),
    ('3', 'Physics and Geology Unit (PGU)'),
)

ROLECHOICES=(
    ('1', 'Faculty'),
    ('2', 'Unit Head'),
    ('3', 'Department Head'),
    ('4', 'Admin Clerk')
)

# class UserManager(BaseUserManager):
#     def create_user(self, email, alternative_email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         now = timezone.now()
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             alternative_email = alternative_email,           
#             is_active=True, 
#             is_staff = is_staff,           
#             last_login=now,
#             date_joined=now, 
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, alternative_email, password):
#         user=self.create_user(email = email, alternative_email = alternative_email, password = password)
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,      
            is_staff=is_staff,
            is_superuser=is_superuser,      
            is_active=True,            
            last_login=now,
            date_joined=now, 
            **extra_fields
        )
        user.set_unusable_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    # alternative_email = models.EmailField(max_length=254, unique=True)

    #Classification
    department = models.CharField(max_length=240, choices=DEPARTMENTCHOICES, default=DEPARTMENTCHOICES[0])
    faculty_rank = models.CharField(max_length=20, choices=FACULTYRANKCHOICES, default=FACULTYRANKCHOICES[0])
    faculty_classification = models.CharField(max_length=20, choices=FACULTYCLASSIFICATIONCHOICES, default=FACULTYCLASSIFICATIONCHOICES[0])
    faculty_tenure = models.CharField(max_length=20, choices=FACULTYTENURECHOICES, default=FACULTYTENURECHOICES[0])
    faculty_status = models.CharField(max_length=20, choices=FACULTYSTATUSCHOICES, default=FACULTYSTATUSCHOICES[0])
    role = models.CharField(max_length=20, choices=ROLECHOICES, default=ROLECHOICES[0])

    #boolean
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_Faculty = models.BooleanField(default=True)
    is_UnitHead = models.BooleanField(default=False)
    is_DepartmentHead = models.BooleanField(default=False) 
    is_Admin = models.BooleanField(default=False)

    #Personal Information
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    middle_name = models.CharField(max_length=254, null=True, blank=True)
    suffix = models.CharField(max_length=20, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEXCHOICES, default=SEXCHOICES[0])
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=254, null=True, blank=True)
    present_address = models.CharField(max_length=254, null=True, blank=True)
    permanent_address = models.CharField(max_length=254, null=True, blank=True)
    civil_status = models.CharField(max_length=10, choices=CIVILSTATUSCHOICES, default=CIVILSTATUSCHOICES[0])
    religion = models.CharField(max_length=254, null=True, blank=True)
    profile_photo = models.ImageField(blank = True, upload_to = None)

    #Contact Details
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    landline_number = models.CharField(max_length=20, null=True, blank=True)


    #Emergency Contact Details
    emergency_contact_name = models.CharField(max_length=254, null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=20, null=True, blank=True)
    emergency_contact_birthdate = models.DateField(null=True, blank=True)
    emergency_contact_relationship = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    
    def __str__(self):
        return "%s" % self.email
