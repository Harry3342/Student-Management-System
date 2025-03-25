from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study',
            'gpa': 'GPA',
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'})
        }



        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study',
            'gpa': 'GPA',
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        student_number = cleaned_data.get("student_number")
        email = cleaned_data.get("email")

        if not student_number:
            self.add_error('student_number', "Student number is required.")
        if not email:
            self.add_error('email', "Email is required.")



        model = Student
        fields = ['student_number', 'first_name','last_name', 'email', 'field_of_study', 'gpa']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study',
            'gpa': 'GPA',
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'field_of_study':forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'})
        }
