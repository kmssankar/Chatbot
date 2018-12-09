from django import forms
class Fleetform(forms.Form):
    FleetId  = forms.CharField(label='Fleet Id',max_length=05)
    Modelnum = forms.CharField(label='Model Year', max_length=04)
    Modelnum = forms.CharField(label='Model Number', max_length=04)
    Selldlr  = forms.CharField(label='Sell Dealer', max_length=05)
    Shipdlr  = forms.CharField(label='Ship Dealer', max_length=05)
    Quantity = forms.IntegerField(label='Quantity',initial=0)
    EDlvDate = forms.DateField(label='E Dlvry Date')
    
class LoginForm(forms.Form):
    username  = forms.CharField(label='User Name',max_length=15)
    password  = forms.CharField(widget=forms.PasswordInput(),label='Password',max_length=15)

    
        
    
    