from django import forms
from .models import review
# class details(forms.Form):
#     # user_name_1 = forms.CharField(label= "Enter the name",required=False ,max_length=20,error_messages = {"required":"error message"})
#     user_name_2 = forms.CharField(label='Enter the name' , max_length =20, required=True,
#     error_messages={
#         'required':'this is reuqest',
#         'max_length':'dont more then 20 characters'})
    
#     rating = forms.IntegerField(label="Enter the Rating", max_value=5, min_value=1, error_messages= {
#         "request":"This field is request",
        
#     } )
    
#     message = forms.CharField(widget=forms.Textarea)
    
#     # phone_number = forms.IntegerField(label= "Enter the phone number",required=False)
#     # email = forms.EmailField(label= "Enter the email",required=False)
        

class details(forms.ModelForm):
    class Meta:
        model = review
        fields = '__all__' #['user_name',rating]
        #exclude = []
        labels = {
            'user_name':'Your Name',
            'rating':'Enter the rating',
            'massage':'Enter the message',
        }