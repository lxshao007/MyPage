from django import forms
from mypage.models import Vistor

class VistorForm(forms.ModelForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Vistor
        fields = '__all__'




    def clean_botchatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher
