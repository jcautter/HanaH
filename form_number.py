import flet as ft
import re

class NumberFormatting:
    _formats:dict = {
       'CPF'            : "###.###.###-##"
       , 'CNPJ'         : '##.###.###/####-##'
       , 'TEL+DDD'      : "(##) #####-####"
       , 'TEL+DDI'      : "+## (##) #####-####"
       , 'CREDIT_CARD'  : '#### #### #### ####'
       , 'CSV'          : '###'
    }
    
    def __init__(self, fmt:str=None, text:str=None, replacing_string='0-9'):
        self._replacing_string = replacing_string
        if fmt:
            self._define_format(fmt)
        if text:
            self._replace(text, fmt)
        self._text = ''

    def _clear(self, text:str):
        return re.sub('[^{rs}]'.format(rs=self._replacing_string), '', text)
    
    def _to_fmt(self, text:str):
        return re.sub('[{rs}]'.format(rs=self._replacing_string), '#', text)
    
    def _check(self):
        return self._to_fmt(self._text) == self._fmt

    def _define_format(self, fmt:str):
        if fmt in self._formats:
            fmt = self._formats[fmt]
        elif '#' not in fmt:
            print('warning')
            fmt = ''
        self._fmt = fmt

    def _replace(self, text:str, fmt:str=None):
        if fmt:
            self._define_format(fmt)
        fmt = self._fmt
        size = len(text)
        if size > 0:
            last_carc = text[-1] if re.match('[{rs}]'.format(rs=self._replacing_string),text[-1]) else None
            text = self._clear(text)
            for c in text:
                fmt = fmt.replace("#", c, 1)
            if last_carc:
                size = max(
                    fmt.rindex(last_carc)+1
                    , size
                )
            self._text = fmt.split('#')[0][:size]
        else:
            self._text = ''
        return self._text
    
class FormInputTextNumberFormat(ft.Column, NumberFormatting):
    def __init__(self, label:str, fmt:str, key:str, required:bool=False, message:str=None, keyboard_type=ft.KeyboardType.NUMBER):
        ft.Column.__init__(self)
        NumberFormatting.__init__(self, fmt)
        self._build(label, key, keyboard_type)
        self._str_message = message

    def _build(self, label:str, key:str, keyboard_type):
        self._message = ft.Text(color='red')
        self._input = ft.TextField(
            label=label
            , on_change=self._on_change
            , keyboard_type=keyboard_type
        )
        self.controls=[ft.Container(key=key), self._input, self._message]

    def _on_change(self, e):
        e.control.value = self._replace(e.control.value)
        e.page.update()

    def _validate(self):
        resp = self._check()
        self._message.value = ''
        if not resp:
            self._message.value = self._str_message
        return resp
    
class FormInputText(ft.Column):
    def __init__(self, label:str, key:str, required:bool=False, message:str=None, keyboard_type=ft.KeyboardType.NONE):
        ft.Column.__init__(self)
        self._build(label, key, keyboard_type)
        self._str_message = message
        self._required = required

    def _build(self, label:str, key:str, keyboard_type):
        self._message = ft.Text(color='red')
        self._input = ft.TextField(
            label=label
            , on_change=self._on_change
            , keyboard_type=keyboard_type
        )
        self.controls=[ft.Container(key=key), self._input, self._message]

    def _on_change(self, e):
        pass
    
    def _validate(self):
        if self._required and len(self._message.value) > 1:
            self._message.value = 'Campo obrigatório'
            return False
        self._message.value = ''
        return True

def main(page: ft.Page):
    def teste(e):
        nome._validate()
        cpf._validate()
        cnpj._validate()
        tel_ddd._validate()
        tel_ddi._validate()
        cc._validate()
        csv._validate()
        e.page.update()

    bt = ft.FilledButton(text="Enviar", on_click=lambda e: teste(e))

    nome = FormInputText(label='Nome', key='nome')
    cpf = FormInputTextNumberFormat(label='CPF', fmt='CPF', key='CPF', message='CPF inválido')
    cnpj = FormInputTextNumberFormat(label='CNPJ', fmt='CNPJ', key='CNPJ', message='CNPJ inválido')
    tel_ddd = FormInputTextNumberFormat(label='Telefone (DDD)', fmt='TEL+DDD', key='TEL+DDD', message='Telefone DDD inválido')
    tel_ddi = FormInputTextNumberFormat(label='Telefone (DDI + DDD)', fmt='TEL+DDI', key='TEL+DDI', message='Telefone DDI inválido')
    cc = FormInputTextNumberFormat(label='Cartão de Crédito', fmt='CREDIT_CARD', key='CREDIT_CARD', message='Número do do cartão inválido')
    csv = FormInputTextNumberFormat(label='CSV', fmt='CSV', key='CSV', message='Código CSV inválido')

    page.add(
        nome
        , cpf
        , cnpj
        , tel_ddd
        , tel_ddi
        , cc
        , csv
        , bt
    )

ft.app(target=main)