from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username', 'password')


class ClassInformationForm(forms.ModelForm):
    ClassName = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "e.g Form Four"}))

    class Meta:
        model = ClassInformation
        fields = ('ClassName', 'ClassTeacher', 'TotalStudents', 'NumberOfSections')

    def clean_class_name(self):
        ClassName = self.cleaned_data.get("ClassName")
        if "CFE" in ClassName:
            return ClassName
        else:
            raise forms.ValidationError("This is not a a valid class name")


class EditClassInformationForm(forms.ModelForm):
    class Meta:
        model = ClassInformation
        fields = ('ClassName', 'ClassTeacher', 'TotalStudents', 'NumberOfSections')


class SectionInformationForm(forms.ModelForm):
    class Meta:
        model = SectionInformation
        fields = ('SectionTeacher', 'NameOfClass', 'NumberOfStudents', 'SectionName')


class EditSectionInformationForm(forms.ModelForm):
    class Meta:
        model = SectionInformation
        fields = ('SectionTeacher', 'NumberOfStudents', 'SectionName')


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('Name', 'NationalId', 'Responsibility', 'Address', 'Username', 'Password')


class EditTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('Name', 'NationalId', 'Responsibility', 'Address')


class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('SubjectName', 'SubjectCode', 'Author', 'Class', 'SubjectTeacher', 'Type', 'OtherNotes')


class EditSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('SubjectName', 'SubjectCode', 'Author', 'Class', 'SubjectTeacher', 'Type', 'OtherNotes')


class AddSyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ('SyllabusType', 'Subject', 'Class', 'Syllabus', 'Notes')


class EditSyllabusForm(forms.ModelForm):
    class Meta:
        model = Syllabus
        fields = ('SyllabusType', 'Subject', 'Class', 'Syllabus', 'Notes')


class AddHumanResourceForm(forms.ModelForm):
    class Meta:
        model = HumanResource
        fields = ('Name', 'NationalId', 'Designation', 'Phone', 'Address', 'Gender', 'Religion')


class EditHumanResourceForm(forms.ModelForm):
    class Meta:
        model = HumanResource
        fields = ('Name', 'Designation', 'Phone', 'Address')


class AddRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ('Class', 'Section', 'Subject', 'Day', 'Teacher', 'StartTime', 'EndTime', 'Address', 'RoomNumber')


class EditRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ('Class', 'Section', 'Subject', 'Day', 'Teacher', 'StartTime', 'EndTime', 'Address', 'RoomNumber')


class AddAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('School', 'AssignmentType', 'Subject', 'Class', 'Assignment', 'Notes')


class EditAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('School', 'AssignmentType', 'Subject', 'Class', 'Assignment', 'Notes')


class AddExamGradeForm(forms.ModelForm):
    class Meta:
        model = ExamGrade
        fields = ('School', 'ExamGrade', 'GradePoint', 'MarkFrom', 'MarkTo', 'Notes')


class EditExamGradeForm(forms.ModelForm):
    class Meta:
        model = ExamGrade
        fields = ('School', 'ExamGrade', 'GradePoint', 'MarkFrom', 'MarkTo', 'Notes')


class AddExamTermForm(forms.ModelForm):
    class Meta:
        model = ExamTerm
        fields = ('School', 'ExamTitle', 'StartDate', 'Notes')


class EditExamTermForm(forms.ModelForm):
    class Meta:
        model = ExamTerm
        fields = ('School', 'ExamTitle', 'StartDate', 'Notes')


class AddExamScheduleForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ('School', 'Exam', 'Class', 'Subject', 'ExamDate', 'StartTime', 'EndTime', 'RoomNumber', 'Notes')


class EditExamScheduleForm(forms.ModelForm):
    class Meta:
        model = ExamSchedule
        fields = ('School', 'Exam', 'Class', 'Subject', 'ExamDate', 'StartTime', 'EndTime', 'RoomNumber', 'Notes')


class AddExamSuggestionForm(forms.ModelForm):
    class Meta:
        model = ExamSuggestion
        fields = ('School', 'SuggestionTitle', 'Class', 'Subject', 'Suggestion', 'Notes')


class EditExamSuggestionForm(forms.ModelForm):
    class Meta:
        model = ExamSuggestion
        fields = ('School', 'SuggestionTitle', 'Class', 'Subject', 'Suggestion', 'Notes')


class AddLibraryBookForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ('School', 'BookTitle', 'ISBN_no', 'BookId', 'Edition', 'Author', 'Language', 'Price', 'Quantity',
                  'BookCover')


class EditLibraryBookForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = (
            'School', 'BookTitle', 'ISBN_no', 'BookId', 'Edition', 'Author', 'Language', 'Price', 'Quantity',
            'BookCover')


class AddVehicleForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ('School', 'VehicleNumber', 'VehicleModel', 'Driver', 'VehicleLicense', 'VehicleContact', 'Notes')


class EditVehicleForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ('School', 'VehicleNumber', 'VehicleModel', 'Driver', 'VehicleLicense', 'VehicleContact', 'Notes')


class AddRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('School', 'RouteTitle', 'StartRoute', 'EndRoute', 'Notes')


class EditRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('School', 'RouteTitle', 'StartRoute', 'EndRoute', 'Notes')


class AddHostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ('School', 'HostelName', 'HostType', 'Address', 'Notes')


class EditHostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = ('School', 'HostelName', 'HostType', 'Address', 'Notes')


class AddHostelRoomForm(forms.ModelForm):
    class Meta:
        model = HostelRoom
        fields = ('School', 'Room_no', 'Hostel', 'RoomType', 'CostPerSeat', 'SeatTotal', 'Notes')


class EditHostelRoomForm(forms.ModelForm):
    class Meta:
        model = HostelRoom
        fields = ('School', 'Room_no', 'Hostel', 'RoomType', 'CostPerSeat', 'SeatTotal', 'Notes')


class AddVisitorInfoForm(forms.ModelForm):
    class Meta:
        model = VisitorInfo
        fields = ('School', 'Name', 'Phone', 'ComingFrom', 'ToMeetUserType', 'ReasonToMeet', 'Notes')


class EditVisitorInfoForm(forms.ModelForm):
    class Meta:
        model = VisitorInfo
        fields = ('School', 'Name', 'Phone', 'ComingFrom', 'ToMeetUserType', 'ReasonToMeet', 'Notes')


class AddSalaryGradeForm(forms.ModelForm):
    class Meta:
        model = SalaryGrade
        fields = ('School', 'GradeName', 'BasicSalary', 'HouseRent', 'TransportAllowance', 'MedicalAllowance',
                  'OverTimeHourlyRate', 'ProvidentFund', 'HourlyRate', 'TotalAllowance', 'TotalDeduction', 'GrossPay',
                  'NetSalary', 'Notes')


class EditSalaryGradeForm(forms.ModelForm):
    class Meta:
        model = SalaryGrade
        fields = ('School', 'GradeName', 'BasicSalary', 'HouseRent', 'TransportAllowance', 'MedicalAllowance',
                  'OverTimeHourlyRate', 'ProvidentFund', 'HourlyRate', 'TotalAllowance', 'TotalDeduction', 'GrossPay',
                  'NetSalary', 'Notes')


class AddDiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ('School', 'Title', 'Amount', 'Notes')


class EditDiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ('School', 'Title', 'Amount', 'Notes')


class AddFeeTypeForm(forms.ModelForm):
    class Meta:
        model = FeeType
        fields = ('School', 'FeeType', 'FeeTitle', 'Notes')


class EditFeeTypeForm(forms.ModelForm):
    class Meta:
        model = FeeType
        fields = ('School', 'FeeType', 'FeeTitle', 'Notes')


class AddFeeCollectionForm(forms.ModelForm):
    class Meta:
        model = FeeCollection
        fields = (
            'School', 'Class', 'student_name', 'FeeType', 'FeeAmount', 'Month', 'IsApplicableDiscount', 'PaidStatus',
            'Notes')


class EditFeeCollectionForm(forms.ModelForm):
    class Meta:
        model = FeeCollection
        fields = (
            'School', 'Class', 'student_name', 'FeeType', 'FeeAmount', 'Month', 'IsApplicableDiscount', 'PaidStatus',
            'Notes')


class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('School', 'IncomeHead', 'PaymentMethod', 'Amount', 'Date', 'Notes')


class EditIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('School', 'IncomeHead', 'PaymentMethod', 'Amount', 'Date', 'Notes')


class AddExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ('School', 'ExpenditureHead', 'ExpenditureMethod', 'Amount', 'Date', 'Notes')


class EditExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ('School', 'ExpenditureHead', 'ExpenditureMethod', 'Amount', 'Date', 'Notes')


class AddEventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('School', 'EventTitle', 'EventFor', 'EventPlace', 'FromDate', 'ToDate', 'Image', 'Notes')


class EditEventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('School', 'EventTitle', 'EventFor', 'EventPlace', 'FromDate', 'ToDate', 'Image', 'Notes')


class AddNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('School', 'NoticeTitle', 'NoticeDate', 'NoticeFor', 'Notice')


class EditNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('School', 'NoticeTitle', 'NoticeDate', 'NoticeFor', 'Notice')


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('School', 'NewsTitle', 'Date', 'Image', 'News')


class EditNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('School', 'NewsTitle', 'Date', 'Image', 'News')


class AddHolidaysForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ('School', 'HolidayTitle', 'FromDate', 'ToDate', 'Notes')


class EditHolidaysForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ('School', 'HolidayTitle', 'FromDate', 'ToDate', 'Notes')


class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Name', 'Phone', 'PresentAddress', 'PermanentAddress', 'Gender',
                  'DateOfBirth', 'Religion', 'Email', 'Photo', 'Resume', 'OtherInfo')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Name', 'Phone', 'PresentAddress', 'PermanentAddress', 'Gender',
                  'DateOfBirth', 'Religion', 'Email', 'Photo', 'Resume', 'OtherInfo')


class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('SchoolName', 'SchoolCode', 'Address', 'Phone', 'DateOfRegistration')


class EditSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('SchoolName', 'SchoolCode', 'Address', 'Phone', 'DateOfRegistration')


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['role',
                  'student_name',
                  'student_username',
                  'student_gender',
                  'student_religion',
                  'student_email',
                  'student_phone',
                  'student_address',
                  'student_birth_date',
                  'student_health_condition',
                  'student_admission_no',
                  'student_admission_date',
                  'student_reg_no',
                  'student_previous_school',
                  'student_previous_class',
                  'student_image',
                  ]

        readonly_fields = 'role'


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name',
                  'student_username',
                  'student_gender',
                  'student_religion',
                  'student_email',
                  'student_phone',
                  'student_address',
                  'student_birth_date',
                  'student_health_condition',
                  'student_admission_no',
                  'student_admission_date',
                  'student_reg_no',
                  'student_previous_school',
                  'student_previous_class',
                  'student_image',
                  ]


class AddGuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ['school_title',
                  'role',
                  'guardian_name',
                  'guardian_email',
                  'guardian_address',
                  'guardian_tel',
                  'guardian_religion',
                  'guardian_image',
                  'is_favorite'
                  ]


class EditGuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = [
            'school_title',
            'guardian_name',
            'guardian_email',
            'guardian_address',
            'guardian_tel',
            'guardian_religion',
            'guardian_image',
            'is_favorite'
        ]


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2', 'surname',
                  'middle_name', 'given_name', 'nationality', 'ID_type',
                  'ID_number', 'date_Of_Birth', 'P_O_Box', 'Area_Of_Residence', 'District',
                  'Registered_PhoneNumber', 'next_of_kin', 'Next_Of_Kin_Physical_Address',
                  'relationship', 'Photo', 'School'
                  )


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password',)

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid login')


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'Photo')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email"%s"is already in use.' % email)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username"%s"is already in use.' % username)

    def clean_photo(self):
        photo = self.cleaned_data['photo']
        try:
            Account.objects.exclude(pk=self.instance.pk).get(photo=photo)
        except Account.DoesNotExist:
            return photo
        raise forms.ValidationError('photo"%s"is already in use.' % photo)


class AccountRightForm(forms.ModelForm):
    class Meta:
        model = AccountRight
        fields = ('user', 'can_delete', 'can_edit', 'can_register', 'can_view')
