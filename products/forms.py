from django import forms


class ExcelUploadForm(forms.Form):
    file = forms.FileField(
        label='Choose Excel File (.xlsx)',
        help_text='Upload an Excel file with columns: product_id, name, category, price, quantity',
    )

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        if not uploaded_file.name.endswith('.xlsx'):
            raise forms.ValidationError('Only .xlsx files are allowed.')
        return uploaded_file


class ApprovedFilterForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Search name or category',
    }))
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'type': 'date',
    }))
    date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'type': 'date',
    }))
    per_page = forms.ChoiceField(required=False, choices=[
        ('5', '5 per page'),
        ('10', '10 per page'),
        ('25', '25 per page'),
    ], initial='10')
