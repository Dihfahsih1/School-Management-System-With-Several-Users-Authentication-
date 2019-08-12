from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class Teacher(models.Model):
    Name = models.CharField(max_length=130)
    NationalId = models.CharField(max_length=130)
    Responsibility = models.CharField(max_length=130)
    Address = models.CharField(max_length=130)
    Username = models.CharField(max_length=130)
    Password = models.CharField(max_length=130)

    def __str__(self):
        return self.Name


class School(models.Model):
    SchoolCode = models.CharField(max_length=130)
    SchoolName = models.CharField(max_length=130)
    Address = models.CharField(max_length=130)
    Phone = models.CharField(max_length=130)
    DateOfRegistration = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.SchoolName


class Guardian(models.Model):
    school_title = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    role = models.CharField(default="guardian", max_length=15)
    guardian_name = models.CharField(max_length=200)
    guardian_email = models.CharField(max_length=130)
    guardian_address = models.CharField(max_length=30, blank=True)
    guardian_tel = models.CharField(max_length=30, blank=True)
    guardian_religion = models.CharField(max_length=30, blank=True)
    guardian_image = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.guardian_name


class Student(models.Model):
    choices = (('female', 'female'), ('male', 'male'))
    school = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    guardian_name = models.ManyToManyField(Guardian)
    role = models.CharField(default="student", max_length=15)
    student_name = models.CharField(max_length=100)
    student_username = models.CharField(max_length=100)
    student_gender = models.CharField(max_length=10, choices=choices, blank=False, null=True)
    student_religion = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100)
    student_phone = models.CharField(max_length=15)
    student_address = models.CharField(max_length=100)
    student_birth_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    student_health_condition = models.CharField(max_length=100)
    student_reg_no = models.CharField(max_length=100)
    student_admission_no = models.CharField(max_length=100)
    student_admission_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    student_previous_class = models.CharField(max_length=100)
    student_previous_school = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to="gallery")
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name + ' - ' + self.student_reg_no


class HumanResource(models.Model):
    choices = (('female', 'female'), ('male', 'male'))
    Name = models.CharField(max_length=130)
    NationalId = models.CharField(max_length=130)
    Designation = models.CharField(max_length=130)
    Phone = models.CharField(max_length=130)
    Gender = models.CharField(max_length=10, choices=choices, blank=False, null=True)
    Address = models.CharField(max_length=130)
    Religion = models.CharField(max_length=130)

    def __str__(self):
        return self.Name


class Login(models.Model):
    username = models.CharField(max_length=130)
    password = models.CharField(max_length=30, blank=True)


class ClassInformation(models.Model):
    ClassName = models.CharField(max_length=130)
    ClassTeacher = models.CharField(max_length=30, blank=True)
    TotalStudents = models.PositiveIntegerField(blank=True)
    NumberOfSections = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.ClassName


class SectionInformation(models.Model):
    NameOfClass = models.ForeignKey(ClassInformation, on_delete=models.PROTECT, blank=True, null=True)
    SectionName = models.CharField(max_length=130)
    SectionTeacher = models.CharField(max_length=30, blank=True)
    NumberOfStudents = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.SectionName


class Subject(models.Model):
    choices = (
        ('Compulsory', 'Compulsory'), ('Options', 'Options')
    )
    SubjectName = models.CharField(max_length=130)
    SubjectCode = models.CharField(max_length=130)
    Author = models.CharField(max_length=130)
    Class = models.ForeignKey(ClassInformation, on_delete=models.PROTECT, blank=True, null=True)
    SubjectTeacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True, null=True)
    Type = models.CharField(max_length=130, choices=choices, blank=False)
    OtherNotes = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.SubjectName


class Syllabus(models.Model):
    SyllabusType = models.CharField(max_length=130)
    Class = models.ForeignKey(ClassInformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subject, on_delete=models.PROTECT, blank=True, null=True)
    Syllabus = models.FileField(max_length=130, blank=False)
    Notes = models.TextField(max_length=100)

    def __str__(self):
        return self.Syllabus


class Routine(models.Model):
    choices = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'),
               ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
               ('Friday', 'Friday'), ('Saturday', 'Saturday'),
               ('Sunday', 'Sunday'))
    Class = models.ForeignKey(ClassInformation, on_delete=models.PROTECT, blank=True, null=True)
    Section = models.ForeignKey(SectionInformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subject, on_delete=models.PROTECT, blank=True, null=True)
    Day = models.CharField(max_length=10, choices=choices, blank=False, null=True)
    Teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, blank=True, null=True)
    StartTime = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    EndTime = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    Address = models.CharField(max_length=130)
    RoomNumber = models.CharField(max_length=130)


class Assignment(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    AssignmentType = models.CharField(max_length=130)
    Class = models.ForeignKey(ClassInformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subject, on_delete=models.PROTECT, blank=True, null=True)
    Deadline = models.DateField(max_length=130, blank=False)
    Assignment = models.FileField(max_length=130, blank=False)
    Notes = models.TextField(max_length=100)

    def __str__(self):
        return self.Assignment


class ExamGrade(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    ExamGrade = models.CharField(max_length=130)
    GradePoint = models.IntegerField()
    MarkFrom = models.PositiveIntegerField()
    MarkTo = models.PositiveIntegerField()
    Notes = models.TextField(max_length=100)

    def __str__(self):
        return self.ExamGrade


class ExamTerm(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    ExamTitle = models.CharField(max_length=130)
    StartDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    Notes = models.TextField(max_length=100)

    def __str__(self):
        return self.ExamTitle


class ExamSchedule(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Exam = models.ForeignKey(ExamTerm, on_delete=models.PROTECT, blank=True, null=True)
    Class = models.ForeignKey(ClassInformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subject, on_delete=models.PROTECT, blank=True, null=True)
    ExamDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    StartTime = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    EndTime = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    RoomNumber = models.CharField(max_length=100, blank=True)
    Notes = models.TextField(max_length=100)

    def __str__(self):
        return self.ExamDate


class ExamSuggestion(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    SuggestionTitle = models.CharField(max_length=130)
    Exam = models.ForeignKey(ExamTerm, on_delete=models.PROTECT, blank=True, null=True)
    Class = models.ForeignKey(ClassInformation, on_delete=models.PROTECT, blank=True, null=True)
    Subject = models.ForeignKey(Subject, on_delete=models.PROTECT, blank=True, null=True)
    Suggestion = models.FileField(max_length=130, blank=False)
    Notes = models.TextField(max_length=100)

    def __str__(self):
        return self.SuggestionTitle


class Library(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    BookTitle = models.CharField(max_length=130)
    ISBN_no = models.CharField(max_length=130)
    BookId = models.CharField(max_length=130)
    Edition = models.CharField(max_length=130)
    Author = models.CharField(max_length=130)
    Language = models.CharField(max_length=130)
    Price = models.CharField(max_length=130)
    Quantity = models.CharField(max_length=130)
    BookCover = models.ImageField(upload_to="gallery")


class Transport(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    VehicleNumber = models.CharField(max_length=130)
    VehicleModel = models.CharField(max_length=130)
    Driver = models.CharField(max_length=130)
    VehicleLicense = models.CharField(max_length=130)
    VehicleContact = models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)


class Route(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    RouteTitle = models.CharField(max_length=130)
    StartRoute = models.CharField(max_length=130)
    EndRoute = models.CharField(max_length=130)
    Notes = models.TextField(max_length=100)

    def __str__(self):
        return self.RouteTitle


class Hostel(models.Model):
    choices = (('Boys', 'Boys'), ('Girls', 'Girls'), ('Combined', 'Combined'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    HostelName = models.CharField(max_length=130)
    HostType = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    Address = models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)

    def __str__(self):
        return self.HostelName


class HostelRoom(models.Model):
    choices = (('AC', 'AC'), ('No AC ', 'No AC'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Room_no = models.CharField(max_length=130)
    Hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT, blank=True, null=True)
    RoomType = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    SeatTotal = models.PositiveIntegerField()
    CostPerSeat = models.PositiveIntegerField()
    Notes = models.TextField(max_length=110)

    def __str__(self):
        return self.Room_no


class VisitorInfo(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Name = models.CharField(max_length=130)
    Phone = models.CharField(max_length=130)
    ComingFrom = models.CharField(max_length=130)
    ToMeetUserType = models.CharField(max_length=130)
    ReasonToMeet = models.CharField(max_length=130)
    Notes = models.TextField(max_length=110)

    def __str__(self):
        return self.Name


class SalaryGrade(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    GradeName = models.CharField(max_length=130)
    BasicSalary = models.PositiveIntegerField()
    HouseRent = models.PositiveIntegerField()
    TransportAllowance = models.PositiveIntegerField()
    MedicalAllowance = models.PositiveIntegerField()
    OverTimeHourlyRate = models.PositiveIntegerField()
    ProvidentFund = models.CharField(max_length=50)
    HourlyRate = models.IntegerField()
    TotalAllowance = models.PositiveIntegerField()
    TotalDeduction = models.PositiveIntegerField()
    GrossPay = models.PositiveIntegerField()
    NetSalary = models.PositiveIntegerField()
    Notes = models.TextField(max_length=110)

    def __str__(self):
        return self.NetSalary


class Discount(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Title = models.CharField(max_length=130)
    Amount = models.PositiveIntegerField()
    Notes = models.TextField(max_length=110)

    def __str__(self):
        return self.Title


class FeeType(models.Model):
    choices = (('General Fee', 'General Fee'), ('Transport', 'Transport'), ('Hostel', 'Hostel'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    FeeTitle = models.CharField(max_length=130)
    FeeType = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    Notes = models.TextField(max_length=110)

    def __str__(self):
        return self.FeeTitle


class Income(models.Model):
    method = (('Cheque', 'Cheque'), ('Cash', 'Cash'))
    head = (('General', 'General'), ('Others', 'Others'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    IncomeHead = models.CharField(max_length=130, choices=head, blank=False, null=True)
    PaymentMethod = models.CharField(max_length=130, choices=method, blank=False, null=True)
    Amount = models.CharField(max_length=130)
    Date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    Notes = models.TextField(max_length=50)

    def __str__(self):
        return self.IncomeHead


class Expenditure(models.Model):
    method = (('Cheque', 'Cheque'), ('Cash', 'Cash'))
    head = (('General', 'General'), ('Others', 'Others'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    ExpenditureHead = models.CharField(max_length=130, choices=head, blank=False, null=True)
    ExpenditureMethod = models.CharField(max_length=130, choices=method, blank=False, null=True)
    Amount = models.CharField(max_length=130)
    Date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    Notes = models.TextField(max_length=50)

    def __str__(self):
        return self.ExpenditureHead


class Events(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    EventTitle = models.CharField(max_length=130)
    EventFor = models.CharField(max_length=130)
    EventPlace = models.CharField(max_length=130)
    Amount = models.PositiveIntegerField()
    FromDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    ToDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    Image = models.ImageField(upload_to="gallery")
    Notes = models.TextField(max_length=50)

    def __str__(self):
        return self.EventTitle


class Notice(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    NoticeTitle = models.CharField(max_length=130)
    NoticeDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    NoticeFor = models.CharField(max_length=130)
    Notice = models.TextField(max_length=130)

    def __str__(self):
        return self.NoticeTitle


class News(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    NewsTitle = models.CharField(max_length=130)
    Date = models.CharField(max_length=130, default="02-July-2019")
    Image = models.ImageField(upload_to="gallery")
    News = models.TextField(max_length=130)

    def __str__(self):
        return self.NewsTitle


class Holiday(models.Model):
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    HolidayTitle = models.CharField(max_length=130)
    FromDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    ToDate = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    Notes = models.TextField(max_length=50)

    def __str__(self):
        return self.HolidayTitle


class Profile(models.Model):
    sex = (('female', 'female'), ('male', 'male'))
    Name = models.CharField(max_length=130)
    Phone = models.CharField(max_length=130)
    PresentAddress = models.CharField(max_length=130)
    PermanentAddress = models.CharField(max_length=130)
    Gender = models.CharField(max_length=130, choices=sex, blank=False)
    DateOfBirth = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    Religion = models.CharField(max_length=130)
    Email = models.CharField(max_length=130)
    Photo = models.ImageField(upload_to="gallery")
    Resume = models.ImageField(upload_to="gallery")
    OtherInfo = models.TextField(max_length=120)


class FeeCollection(models.Model):
    fee = (('General Fee', 'General Fee'), ('Transport', 'Transport'), ('Hostel', 'Hostel'))
    choices = (('Yes', 'Yes'), ('No', 'No'))
    status = (('Paid', 'Paid'), ('Unpaid', 'Unpaid'))
    School = models.ForeignKey(School, on_delete=models.PROTECT, blank=True, null=True)
    Class = models.ForeignKey(ClassInformation, on_delete=models.PROTECT, blank=True, null=True)
    student_name = models.ForeignKey(Student, on_delete=models.PROTECT, blank=True, null=True)
    FeeType = models.CharField(max_length=130, choices=fee, blank=False, null=True)
    FeeAmount = models.PositiveIntegerField()
    Month = models.CharField(max_length=130)
    IsApplicableDiscount = models.CharField(max_length=130, choices=choices, blank=False, null=True)
    PaidStatus = models.CharField(max_length=130, choices=status, blank=False, null=True)
    Notes = models.TextField(max_length=60)

    def __str__(self):
        return self.PaidStatus


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a user name")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    given_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    IDtypes = (('NationalId', 'NationalId'),
               ('Passport', 'Passport'),
               ('DrivingPermit', 'DrivingPermit')
               )
    ID_type = models.CharField(max_length=100, blank=False, choices=IDtypes)
    ID_number = models.CharField(max_length=100)
    date_Of_Birth = models.CharField(max_length=100)
    P_O_Box = models.CharField(max_length=100)
    Area_Of_Residence = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Registered_PhoneNumber = models.CharField(max_length=100)
    next_of_kin = models.CharField(max_length=100)
    Next_Of_Kin_Physical_Address = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    Photo = models.ImageField(max_length=100)
    School = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyAccountManager()

    def __str__(self):
        return self.email + "|" + self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class AccountRight(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=False)
    can_edit = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)
    can_register = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    def _str_(self):
        return str(self.user)
