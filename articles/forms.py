from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is already taken. Please pick another title.")
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data 
    #     title = cleaned_data.get('title')
    #     print("cleaned_data", cleaned_data)
    #     print("title", title)
    #     if title.lower().strip() == "new form":
    #         raise forms.ValidationError('This title is already taken.')
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print("all cleaned data", cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "new form":
            self.add_error('title', 'This title is already taken.')
            # raise forms.ValidationError('This title is already taken.')
        if 'new form' in content or 'new form' in title.lower():
            self.add_error('content', 'cannot use new form in content or title')
            raise forms.ValidationError('new form is allowed to be used.')

        return cleaned_data