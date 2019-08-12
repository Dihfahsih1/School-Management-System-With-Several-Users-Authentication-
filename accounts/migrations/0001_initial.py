# Generated by Django 2.2.4 on 2019-08-08 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('surname', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('given_name', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('ID_type', models.CharField(choices=[('NationalId', 'NationalId'), ('Passport', 'Passport'), ('DrivingPermit', 'DrivingPermit')], max_length=100)),
                ('ID_number', models.CharField(max_length=100)),
                ('date_Of_Birth', models.CharField(max_length=100)),
                ('P_O_Box', models.CharField(max_length=100)),
                ('Area_Of_Residence', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=100)),
                ('Registered_PhoneNumber', models.CharField(max_length=100)),
                ('next_of_kin', models.CharField(max_length=100)),
                ('Next_Of_Kin_Physical_Address', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('Photo', models.ImageField(upload_to='')),
                ('School', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassName', models.CharField(max_length=130)),
                ('ClassTeacher', models.CharField(blank=True, max_length=30)),
                ('TotalStudents', models.PositiveIntegerField(blank=True)),
                ('NumberOfSections', models.PositiveIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='guardian', max_length=15)),
                ('guardian_name', models.CharField(max_length=200)),
                ('guardian_email', models.CharField(max_length=130)),
                ('guardian_address', models.CharField(blank=True, max_length=30)),
                ('guardian_tel', models.CharField(blank=True, max_length=30)),
                ('guardian_religion', models.CharField(blank=True, max_length=30)),
                ('guardian_image', models.FileField(upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HostelName', models.CharField(max_length=130)),
                ('HostType', models.CharField(choices=[('Boys', 'Boys'), ('Girls', 'Girls'), ('Combined', 'Combined')], max_length=130, null=True)),
                ('Address', models.CharField(max_length=130)),
                ('Notes', models.TextField(max_length=110)),
            ],
        ),
        migrations.CreateModel(
            name='HumanResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=130)),
                ('NationalId', models.CharField(max_length=130)),
                ('Designation', models.CharField(max_length=130)),
                ('Phone', models.CharField(max_length=130)),
                ('Gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=10, null=True)),
                ('Address', models.CharField(max_length=130)),
                ('Religion', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=130)),
                ('password', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=130)),
                ('Phone', models.CharField(max_length=130)),
                ('PresentAddress', models.CharField(max_length=130)),
                ('PermanentAddress', models.CharField(max_length=130)),
                ('Gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=130)),
                ('DateOfBirth', models.DateField(blank=True)),
                ('Religion', models.CharField(max_length=130)),
                ('Email', models.CharField(max_length=130)),
                ('Photo', models.ImageField(upload_to='gallery')),
                ('Resume', models.ImageField(upload_to='gallery')),
                ('OtherInfo', models.TextField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SchoolCode', models.CharField(max_length=130)),
                ('SchoolName', models.CharField(max_length=130)),
                ('Address', models.CharField(max_length=130)),
                ('Phone', models.CharField(max_length=130)),
                ('DateOfRegistration', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectName', models.CharField(max_length=130)),
                ('SubjectCode', models.CharField(max_length=130)),
                ('Author', models.CharField(max_length=130)),
                ('Type', models.CharField(choices=[('Compulsory', 'Compulsory'), ('Options', 'Options')], max_length=130)),
                ('OtherNotes', models.TextField(blank=True, max_length=200)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ClassInformation')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=130)),
                ('NationalId', models.CharField(max_length=130)),
                ('Responsibility', models.CharField(max_length=130)),
                ('Address', models.CharField(max_length=130)),
                ('Username', models.CharField(max_length=130)),
                ('Password', models.CharField(max_length=130)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=130)),
                ('Phone', models.CharField(max_length=130)),
                ('ComingFrom', models.CharField(max_length=130)),
                ('ToMeetUserType', models.CharField(max_length=130)),
                ('ReasonToMeet', models.CharField(max_length=130)),
                ('Notes', models.TextField(max_length=110)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleNumber', models.CharField(max_length=130)),
                ('VehicleModel', models.CharField(max_length=130)),
                ('Driver', models.CharField(max_length=130)),
                ('VehicleLicense', models.CharField(max_length=130)),
                ('VehicleContact', models.CharField(max_length=130)),
                ('Notes', models.TextField(max_length=100)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SyllabusType', models.CharField(max_length=130)),
                ('Syllabus', models.FileField(max_length=130, upload_to='')),
                ('Notes', models.TextField(max_length=100)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ClassInformation')),
                ('Subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='SubjectTeacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Teacher'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='student', max_length=15)),
                ('student_name', models.CharField(max_length=100)),
                ('student_username', models.CharField(max_length=100)),
                ('student_gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=10, null=True)),
                ('student_religion', models.CharField(max_length=100)),
                ('student_email', models.CharField(max_length=100)),
                ('student_phone', models.CharField(max_length=15)),
                ('student_address', models.CharField(max_length=100)),
                ('student_birth_date', models.DateField(blank=True)),
                ('student_health_condition', models.CharField(max_length=100)),
                ('student_reg_no', models.CharField(max_length=100)),
                ('student_admission_no', models.CharField(max_length=100)),
                ('student_admission_date', models.DateField(blank=True)),
                ('student_previous_class', models.CharField(max_length=100)),
                ('student_previous_school', models.CharField(max_length=100)),
                ('student_image', models.ImageField(upload_to='gallery')),
                ('is_favorite', models.BooleanField(default=False)),
                ('guardian_name', models.ManyToManyField(to='accounts.Guardian')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='SectionInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SectionName', models.CharField(max_length=130)),
                ('SectionTeacher', models.CharField(blank=True, max_length=30)),
                ('NumberOfStudents', models.PositiveIntegerField(blank=True)),
                ('NameOfClass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ClassInformation')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GradeName', models.CharField(max_length=130)),
                ('BasicSalary', models.PositiveIntegerField()),
                ('HouseRent', models.PositiveIntegerField()),
                ('TransportAllowance', models.PositiveIntegerField()),
                ('MedicalAllowance', models.PositiveIntegerField()),
                ('OverTimeHourlyRate', models.PositiveIntegerField()),
                ('ProvidentFund', models.CharField(max_length=50)),
                ('HourlyRate', models.IntegerField()),
                ('TotalAllowance', models.PositiveIntegerField()),
                ('TotalDeduction', models.PositiveIntegerField()),
                ('GrossPay', models.PositiveIntegerField()),
                ('NetSalary', models.PositiveIntegerField()),
                ('Notes', models.TextField(max_length=110)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10, null=True)),
                ('StartTime', models.TimeField(blank=True)),
                ('EndTime', models.TimeField(blank=True)),
                ('Address', models.CharField(max_length=130)),
                ('RoomNumber', models.CharField(max_length=130)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ClassInformation')),
                ('Section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.SectionInformation')),
                ('Subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Subject')),
                ('Teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RouteTitle', models.CharField(max_length=130)),
                ('StartRoute', models.CharField(max_length=130)),
                ('EndRoute', models.CharField(max_length=130)),
                ('Notes', models.TextField(max_length=100)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NoticeTitle', models.CharField(max_length=130)),
                ('NoticeDate', models.DateField(blank=True)),
                ('NoticeFor', models.CharField(max_length=130)),
                ('Notice', models.TextField(max_length=130)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NewsTitle', models.CharField(max_length=130)),
                ('Date', models.CharField(default='02-July-2019', max_length=130)),
                ('Image', models.ImageField(upload_to='gallery')),
                ('News', models.TextField(max_length=130)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookTitle', models.CharField(max_length=130)),
                ('ISBN_no', models.CharField(max_length=130)),
                ('BookId', models.CharField(max_length=130)),
                ('Edition', models.CharField(max_length=130)),
                ('Author', models.CharField(max_length=130)),
                ('Language', models.CharField(max_length=130)),
                ('Price', models.CharField(max_length=130)),
                ('Quantity', models.CharField(max_length=130)),
                ('BookCover', models.ImageField(upload_to='gallery')),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IncomeHead', models.CharField(choices=[('General', 'General'), ('Others', 'Others')], max_length=130, null=True)),
                ('PaymentMethod', models.CharField(choices=[('Cheque', 'Cheque'), ('Cash', 'Cash')], max_length=130, null=True)),
                ('Amount', models.CharField(max_length=130)),
                ('Date', models.DateField(blank=True)),
                ('Notes', models.TextField(max_length=50)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='HostelRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_no', models.CharField(max_length=130)),
                ('RoomType', models.CharField(choices=[('AC', 'AC'), ('No AC ', 'No AC')], max_length=130, null=True)),
                ('SeatTotal', models.PositiveIntegerField()),
                ('CostPerSeat', models.PositiveIntegerField()),
                ('Notes', models.TextField(max_length=110)),
                ('Hostel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Hostel')),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.AddField(
            model_name='hostel',
            name='School',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School'),
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HolidayTitle', models.CharField(max_length=130)),
                ('FromDate', models.DateField(blank=True)),
                ('ToDate', models.DateField(blank=True)),
                ('Notes', models.TextField(max_length=50)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.AddField(
            model_name='guardian',
            name='school_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School'),
        ),
        migrations.CreateModel(
            name='FeeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FeeTitle', models.CharField(max_length=130)),
                ('FeeType', models.CharField(choices=[('General Fee', 'General Fee'), ('Transport', 'Transport'), ('Hostel', 'Hostel')], max_length=130, null=True)),
                ('Notes', models.TextField(max_length=110)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='FeeCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FeeType', models.CharField(choices=[('General Fee', 'General Fee'), ('Transport', 'Transport'), ('Hostel', 'Hostel')], max_length=130, null=True)),
                ('FeeAmount', models.PositiveIntegerField()),
                ('Month', models.CharField(max_length=130)),
                ('IsApplicableDiscount', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=130, null=True)),
                ('PaidStatus', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=130, null=True)),
                ('Notes', models.TextField(max_length=60)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ClassInformation')),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
                ('student_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExpenditureHead', models.CharField(choices=[('General', 'General'), ('Others', 'Others')], max_length=130, null=True)),
                ('ExpenditureMethod', models.CharField(choices=[('Cheque', 'Cheque'), ('Cash', 'Cash')], max_length=130, null=True)),
                ('Amount', models.CharField(max_length=130)),
                ('Date', models.DateField(blank=True)),
                ('Notes', models.TextField(max_length=50)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='ExamTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExamTitle', models.CharField(max_length=130)),
                ('StartDate', models.DateField(blank=True)),
                ('Notes', models.TextField(max_length=100)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='ExamSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SuggestionTitle', models.CharField(max_length=130)),
                ('Suggestion', models.FileField(max_length=130, upload_to='')),
                ('Notes', models.TextField(max_length=100)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ClassInformation')),
                ('Exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ExamTerm')),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
                ('Subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='ExamSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExamDate', models.DateField(blank=True)),
                ('StartTime', models.TimeField(blank=True)),
                ('EndTime', models.TimeField(blank=True)),
                ('RoomNumber', models.CharField(blank=True, max_length=100)),
                ('Notes', models.TextField(max_length=100)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ClassInformation')),
                ('Exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ExamTerm')),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
                ('Subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='ExamGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExamGrade', models.CharField(max_length=130)),
                ('GradePoint', models.IntegerField()),
                ('MarkFrom', models.PositiveIntegerField()),
                ('MarkTo', models.PositiveIntegerField()),
                ('Notes', models.TextField(max_length=100)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventTitle', models.CharField(max_length=130)),
                ('EventFor', models.CharField(max_length=130)),
                ('EventPlace', models.CharField(max_length=130)),
                ('Amount', models.PositiveIntegerField()),
                ('FromDate', models.DateField(blank=True)),
                ('ToDate', models.DateField(blank=True)),
                ('Image', models.ImageField(upload_to='gallery')),
                ('Notes', models.TextField(max_length=50)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=130)),
                ('Amount', models.PositiveIntegerField()),
                ('Notes', models.TextField(max_length=110)),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssignmentType', models.CharField(max_length=130)),
                ('Deadline', models.DateField(max_length=130)),
                ('Assignment', models.FileField(max_length=130, upload_to='')),
                ('Notes', models.TextField(max_length=100)),
                ('Class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.ClassInformation')),
                ('School', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.School')),
                ('Subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='AccountRight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_edit', models.BooleanField(default=False)),
                ('can_view', models.BooleanField(default=False)),
                ('can_register', models.BooleanField(default=False)),
                ('can_delete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]