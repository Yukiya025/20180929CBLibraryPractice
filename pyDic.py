def to_ru():
    from googletrans import Translator
    translator = Translator()
    ru_ja = translator.translate('солдат', 'ja')
    print(ru_ja.text)