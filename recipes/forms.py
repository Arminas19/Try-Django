from django import forms
from .models import Recipe, RecipeIngredient


class RecipeForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    name = forms.CharField(help_text='This is your help! <a href="contact"> Contact Us </a>')
    desciption = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Recipe desciption"}))
    class Meta:
        model = Recipe 
        fields = ['name', 'desciption', 'direction']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "placeholder": f'Recipe {str(field)}',
                "class": 'form-control'
                # "hx-post": ".",
                # "hx-trigger": "keyup changed delay:500ms",
                # "hx-target": "#recipe-container",
                # "hx-swap": "OuterHTML"
            }
        self.fields[str(field)].widget.attrs.update(new_data)

        # self.fields['name'].label = ''
        # self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
        self.fields['desciption'].widget.attrs.update({'rows': '2'})
        self.fields['direction'].widget.attrs.update({'rows': '4'})

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient 
        fields = ['name', 'quantity', 'unit']