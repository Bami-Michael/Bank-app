from django import forms
from django.forms import ModelForm 
from .models import Transaction, Member,Guest,Idme,Bank,Contact_us
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User






class transferform(ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
        exclude = ["user", "status","narrative","timestamp"]
        labels = {'source':'Debit Account', 'name': 'Beneficiary Name', 'bank': 'Beneficiary Bank',
                  'acc':'Account Number', 'rout': 'Routine Number', 'amount':'Amount', 'memo':'Purpose'                 
        }

        widgets = {
            'source': forms.TextInput(attrs={'class':'form-control' }),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name','autocomplete': 'off'}),
             
            'acc': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'','autocomplete': 'off'}),
            'rout': forms.NumberInput(attrs={'class':'form-control','autocomplete': 'off'}),
            'amount': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'$','autocomplete': 'off'}),
            'memo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Optional','autocomplete': 'off'})
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['source'].disabled = True
        self.fields['bank'].strip = False


class profileform(ModelForm):
    class Meta:
        model = Member
        fields = ["fname", "lname", "ssn", "address","phone","country","email","accounttype","pix","DOB","city","state","postcode"]
                      
        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off', }),
            'lname': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off', }),
            'email': forms.EmailInput(attrs={'class':'form-control','autocomplete': 'off'}),
            'pix': forms.FileInput(attrs={'class':'form-control'}),
            'ssn': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off' }),
            'address': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}),
            'city': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}),
            'state': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}),
            'postcode': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}),
            'phone': forms.NumberInput(attrs={'class':'form-control','autocomplete': 'off' }),
            'country': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off' }),
            'accounttype': forms.TextInput(attrs={'class':'form-control'}),
            'DOB': forms.DateInput(attrs={'class':'form-control','autocomplete': 'off', }),
           
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accounttype'].disabled = True
        self.fields['fname'].disabled = True
        self.fields['lname'].disabled = True
        self.fields['ssn'].disabled = True
        self.fields['DOB'].disabled = True
        

    



class guestform(ModelForm):
    class Meta:
        model = Guest
        fields = ["fname", "lname","DOB", "ssn", "address","city","state","postcode","phone","country","email","accounttype","idfront",'idback',
                  'products','marketing','policy']
                      
        widgets = {
            'accounttype': forms.TextInput(attrs={'class':'form-control'}),
            'fname': forms.TextInput(attrs={'class':'form-control' }),
            'lname': forms.TextInput(attrs={'class':'form-control' }),
            'DOB': forms.TextInput(attrs={'class':'form-control', 'placeholder':'DD/MM/YY' }),           
            'ssn': forms.NumberInput(attrs={'class':'form-control','autocomplete': 'off' }),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}),
            'state': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}),
            'postcode': forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}),
            'country': forms.TextInput(attrs={'class':'form-control' }),
            'phone': forms.NumberInput(attrs={'class':'form-control' }),           
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'idfront': forms.FileInput(attrs={'class':'form-control'}),
            'idback': forms.FileInput(attrs={'class':'form-control'}),
            'products': forms.CheckboxInput(),
            'marketing': forms.CheckboxInput(),
            'policy': forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accounttype'].disabled = True
        self.fields['products'].required = True
        self.fields['marketing'].required = True
        self.fields['policy'].required = True



class settingsform(ModelForm):
    class Meta:
        model = Member
        fields = ["Changes", "products", "Marketing"]
                      
        widgets = {
            'Changes': forms.CheckboxInput(),
            'products': forms.CheckboxInput(),
            'Marketing': forms.CheckboxInput(),
        }



class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control","type":"password"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control","type":"password"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control","type":"password"})

    class Meta:
        fields = ["old_password", "new_password1", "new_password2"]




class idme_field(ModelForm):
    class Meta:
        model = Idme
        fields = ["email", "password"]

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email','autocomplete': 'off' }),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password'}),

        }





class bank_form(ModelForm):
    class Meta:
        model = Bank
        fields = ["name"]

        widgets = {
            'name': forms.Select(attrs={'class':'form-control', 'placeholder':'Bank Selectz','autocomplete': 'off' }),

        }




class Contact_form(ModelForm):
    class Meta:
        model = Contact_us
        fields = ["name",'email','subject','message']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name','autocomplete': 'off' }),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email','autocomplete': 'off' }),
            'subject': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject','autocomplete': 'off'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message','autocomplete': 'off'}),
            

        }








'''

        <option value="Bank of America"></option>
              <option value="Bank of America"></option>
              <option value="Wells Fargo"></option>  
              <option value="Capital One"></option>
              <option value="JPMorgan Chase & Co"></option>  
              <option value="PNC Bank"></option>
              <option value="U.S. Bancorp"></option>  
              <option value="U.S. Bank Branch"></option>
              <option value="Bank of New York"></option>  
              <option value="M&T Bank"></option>
              <option value="Fifth Third Bank"></option>  
              <option value="Goldman Sachs"></option>
              <option value="SunTrust Banks"></option>  
              <option value="Citigroup"></option>
              <option value="Chase Bank"></option>  
              <option value="Comerica"></option>
              <option value="Ally Bank"></option>  
              <option value="Huntington Bank"></option>
              <option value="State Street Corporation"></option>  
              <option value="Morgan Stanley"></option>
              <option value="MUFG Union Bank"></option>  
              <option value="Discover Bank"></option>
              <option value="Citizens Bank"></option>  
              <option value="Citibank"></option>
              <option value="TD Bank"></option>  
              <option value="American Express National Bank"></option>
              <option value="HSBC Bank USA"></option>  
              <option value="BMO Harris Bank"></option>
              <option value="Truist Bank"></option>  
              <option value="First Citizens Bank"></option>
              <option value="Santander Bank"></option>  
              <option value="FirstBank"></option>
              <option value="KeyBank"></option>  
              <option value="Woodforest National Bank"></option>
              <option value="Bank of the West"></option>  
'''