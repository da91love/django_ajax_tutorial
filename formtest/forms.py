from django import forms


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=20, label='名前', help_text='英字のみ', widget=forms.TextInput(attrs={
        'placeholder': 'Name',
    }))
    age = forms.IntegerField(min_value=0, max_value=120, label='年齢', help_text='0以上120以下', widget=forms.NumberInput(attrs={
        'placeholder': '0',
    }))

    # city = forms.ModelChoiceField(required=True, label='都市', widget=forms.TextInput(attrs={
    #         'id': 'selectItems',
    #         'name': 'selectItems',
    #         'placeholder': 'Where is your city'}))

    # city = forms.MultipleChoiceField(required=True, choices=c, label="都市", widget=forms.TextInput(attrs={
    #         'id': 'selectItems',
    #         'name': 'selectItems',
    #         'placeholder': 'Where is your city'}))

    STAFF_BUSINESS_TYPES = {
        (1, "Foo"),
        (2, "Bar"),
        (3, "Cat"),
        (4, "Dog")
    }

    city = forms.MultipleChoiceField(required=True, choices=STAFF_BUSINESS_TYPES, label="都市", widget=forms.SelectMultiple(
        attrs={
            'id': 'selectItems',
            'class':'form-control',
            'name': 'selectItems',
            'placeholder': 'Where is your city'})
    )


    def clean_name(self):
        print('pass clean_name')
        name = self.cleaned_data['name']

        isallalpha = True
        for c in name:
            if not c.isalpha():
                isallalpha = False
                break

        if not isallalpha:
            raise forms.ValidationError('英字以外が含まれています。')

        return name

    def clean_age(self):
        """
        ちなみにフィールドの属性 min_value, max_valueで入力範囲を制限できる。
        それらを設定したらこのバリデーションは不要？
        """
        print('pass clean_age')
        age = self.cleaned_data['age']

        if age < 0 or age > 120:
            raise forms.ValidationError('範囲外です。')

        return age