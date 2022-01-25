from django.forms import ModelForm
from django import forms
from datetime import date
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Crime,CAQS,Answer,Question,StationUser, Case,Suspect,Evidence,RIBStation,Officer,Reporter,MurderQuestions,ViolentQuestions,RobberyQuestions


class RibOfficerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
        
    def __init__(self, *args, **kwargs):
        super(RibOfficerRegistrationForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None
    def save(self, commit=True):
        user = super(RibOfficerRegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            
        return user



class StationNameRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
        
    def __init__(self, *args, **kwargs):
        super(StationNameRegistrationForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username','email','password1','password2']:
            self.fields[fieldname].help_text = None
    def save(self, commit=True):
        user = super(StationNameRegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            
        return user


class DateInput(forms.DateInput):
    input_type = 'date'

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        # fields = '__all__'
        fields = ('case_name','crimeType','victim_name','reporter_name','reporter_phone','victim_address','case_desc','stationuser', 'suspects')
        labels = {
            'case_name':'Case Code',
            'crimeType':'Type Of Crime',
            'victim_name':'Victim Name',
            'reporter_name':'Reporter Name',
            'reporter_phone':'Reporter Phone',
            'victim_address':'Address of the Victim',
            'case_desc':'Case Description',
            'stationuser':'Case Officer',
            }
class RibstationForm(forms.ModelForm):
    class Meta:
        model = RIBStation
        fields = ('user','station_name','province')
        labels = {
            'user':'Station Commander',
            'station_name':'Station Name',
            'province':'Province',
            }

class SuspectForm(forms.ModelForm):
    class Meta:
        model = Suspect
        # fields = '__all__'
        fields = ('suspectNID','f_name','l_name','gender','dob','phone','relation','father_name','mother_name','province','district','cell','village','ribstation','note')
        labels = {
            'suspectNID':'Suspect Id',
            'f_name':'First Name',
            'l_name':'Last Name',
            'gender':'Gender',
            'dob':'Date Of Birth',
            'phone':'Phone Number',            
            'relation':'Relation to Crime',
            'father_name':'Father Name',
            'mother_name':'Mother Name',
            'province':'Province',
            'district':'District',
            'cell':'Cell',
            'village':'Village',
            'ribstation':'RIBStation',
            'note':'Short Note',
            }

class EvidenceForm(forms.ModelForm):
    class Meta:
        model = Evidence
        # fields = '__all__'
        fields = ('evidenceCategory','evidence_note','officerimage','points')
        labels = {
            'evidenceCategory':'Evidence Category',
            'evidence_note':'Short note',
            'officerimage':'Evidence Photo',
            'points':'Points Gainned',
            }

class OfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        # fields = '__all__'
        fields = ('user','OfficerNationalId','f_name','l_name','gender','phone','email','rank','recruit_year','officerimage')
        labels = {
            'user':'User Name',
            'OfficerNationalId':'Officer ID',
            'f_name':'Fist Name',
            'l_name':'Last Name',
            'gender':'Gender',
            'phone':'Phone',
            'email':'Email',
            'rank':'Rank',
            'recruit_year':'Join RIB Year',
            'officerimage':'Officer Photo',
            }

class StationUserForm(forms.ModelForm):
    class Meta:
        model = StationUser
        # fields = '__all__'
        fields = ('user','nationalId','f_name','l_name','gender','phone','email','rank','recruit_year','officerimage')
        labels = {
            'user':'User Name',
            'nationalId':'Officer ID',
            'f_name':'Fist Name',
            'l_name':'Last Name',
            'gender':'Gender',
            'phone':'Phone',
            'email':'Email',
            'rank':'Rank',
            'recruit_year':'Join RIB Year',
            'officerimage':'Officer Photo',
            }

class ReporterForm(forms.ModelForm):
    class Meta:
        model = Reporter
        # fields = '__all__'
        fields = ('reporterNID','f_name','l_name','gender','email','phone','relation','vote','note')
        labels = {
            'reporterNID':'Reporter Id',
            'f_name':'First Name',
            'l_name':'Last Name',
            'gender':'Gender',
            'email':'Email',
            'phone':'Phone Number',            
            'relation':'Your Relation with suspect',
            'vote':'Are you linking suspect to the case(Guilty)',
            'note':'Short Note',
            # 'suspect':'Who are you Reporting',
            }


class MurderQuestionaireForm(forms.ModelForm):
    class Meta:
        model = MurderQuestions
        # fields = '__all__'
        fields = ('reporterNID',
        'q1','q2','q3',
        'q4','q5','q6',
        'q7','q8',
        'q9','q10','q11',
        'q12','q13','q14','q15','q16','case','note', 'suspect')
        labels = {
            'reporterNID':'What is  your id?',
            'q1':'Have you been suspected before?',
            'case':'On which case have you suspected Before?',
            'q13':'Why are you suspected to this case?',
            'q2':'Where were you when the crime was taking place?',
            'q3':'Do you have relationship with the Victm?',
            'q4':'Did you know the victim before?',
            'q5':'For how long have you been known eachother?',            
            'q9':'What do you know about the victm?',
            'q6':'Have you talked to the victim before his/her death?',
            'q7':'Have you ever had conflicts with the victim?',
            'q8':'When have you lastly seen the Victim?',
            'q11':'Are you really Related to this Crime?',
            'q12':'How many marks can you get out of 10 the be the suspected Person?',
            'q10':'Do you have any witnesses that can prove your innocence?',
            'q15':'What are the witnesses names and their phone Number? Ex:Yves0784960500',
            'q14':'What were you two doing when you were together with the victim?',
            'q16':'How many times did you usually meet with the victim in a week?',
            'note':'Short Note on how the victim has been killed',
            'suspect': 'Suspect'
            
            }
        
class ViolentQuestionaireForm(forms.ModelForm):
    class Meta:
        model = ViolentQuestions
        # fields = '__all__'
        fields = ('reporterNID','q1','q2','q3',
        'q4','q5','q6',
        'q7','q8',
        'q9','q10','q11',
        'q12','q13','q14','q15','q16','case','note', 'suspect')
        labels = {
            'reporterNID':'What is  your id?',
            'q1':'Have you been suspected before?',
            'case':'On which case have you suspected Before?',
            'q13':'Why are you suspected to this case?',
            'q2':'Where were you when the crime was taking place?',
            'q3':'Do you have relationship with the Victm?',
            'q4':'Did you know the victim before?',
            'q5':'For how long have you been known eachother?',            
            'q9':'What do you know about the victm?',
            'q6':'Have you talked to the victim before his/her death?',
            'q7':'Have you ever had conflicts with the victim?',
            'q8':'When have you lastly seen the Victim?',
            'q11':'Are you really Related to this Crime?',
            'q12':'How many marks can you get out of 10 the be the suspected Person?',
            'q10':'Do you have any witnesses that can prove your innocence?',
            'q15':'What are the witnesses names and their phone Number? Ex:Yves0784960500',
            'q14':'What were you two doing when you were together with the victim?',
            'q16':'How many times did you usually meet with the victim in a week?',
            'note':'Short Note on how the victim has been killed',
            'suspect': 'Suspect'
             }

class RobberyQuestionaireForm(forms.ModelForm):
    class Meta:
        model = RobberyQuestions
        # fields = '__all__'
        fields = ('suspect',
        'q1','q2','q3',
        'q4','q5','q6',
        'q7','q8',
        'q9','q10','q11',
        'q12','q13','q14','q15','q16','case','note', 'suspect')
        labels = {
            'suspect':'What is  your id?',
            'q1':'Have you been suspected before?',
            'case':'On which case have you suspected Before?',
            'q13':'Why are you suspected to this case?',
            'q2':'Where were you when the crime was taking place?',
            'q3':'Do you have relationship with the Victm?',
            'q4':'Did you know the victim before?',
            'q5':'For how long have you been known eachother?',            
            'q9':'What do you know about the victm?',
            'q6':'Have you talked to the victim before his/her death?',
            'q7':'Have you ever had conflicts with the victim?',
            'q8':'When have you lastly seen the Victim?',
            'q11':'Are you really Related to this Crime?',
            'q12':'How many marks can you get out of 10 the be the suspected Person?',
            'q10':'Do you have any witnesses that can prove your innocence?',
            'q15':'What are the witnesses names and their phone Number? Ex:Yves0784960500',
            'q14':'What were you two doing when you were together with the victim?',
            'q16':'How many times did you usually meet with the victim in a week?',
            'note':'Short Note on how the victim has been killed',
            'suspect': 'Suspect'
            }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('questionName',)
        labels = {
            'questionName':'Describe the Question To Be Asked',
            }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('AnswerName',)
        labels = {
            'AnswerName':'Predict an Answer To Be Answered',
            }

class CAQSForm(forms.ModelForm):
    class Meta:
        model = CAQS
        fields = ('suspect','crime','question','answer')
        labels = {
            'suspect':'What is your name? ',
            'crime':'Which case are you against To?',
            'question':'Question',
            'answer':'Your Answer',

            
            }

class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ('crimeName',)
        labels = {
            'crimeName':'Describe the Crime Name',
            }