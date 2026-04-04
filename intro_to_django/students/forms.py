from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    def clean_score(self):
        score = self.cleaned_data["score"]
        if score < 0 or score > 100:
            raise forms.ValidationError("Score must be between 0 and 100")
        return score

    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 0 or age > 100:
            raise forms.ValidationError("Age must be between 0 and 100")
        return age

    def clean_hours_study(self):
        hours_study = self.cleaned_data["hours_study"]
        if hours_study < 0 or hours_study > 8:
            raise forms.ValidationError("Hours study must be between 0 and 8")
        return hours_study