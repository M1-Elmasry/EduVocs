#!/usr/bin/env python3
"""module represents manager class"""
import requests
import json


supported_languages = {
    "Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Armenian": "hy",
    "Assamese": "as", "Aymara": "ay", "Azerbaijani": "az", "Bambara": "bm", "Basque": "eu",
    "Belarusian": "be", "Bengali": "bn", "Bhojpuri": "bho", "Bosnian": "bs", "Bulgarian": "bg",
    "Catalan": "ca", "Cebuano": "ceb", "Chinese (Simplified)": "zh-CN or zh (BCP-47)", "Chinese (Traditional)": "zh-TW (BCP-47)",
    "Corsican": "co", "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dhivehi": "dv",
    "Dogri": "doi", "Dutch": "nl", "English": "en", "Esperanto": "eo", "Estonian": "et",
    "Ewe": "ee", "Filipino (Tagalog)": "fil", "Finnish": "fi", "French": "fr", "Frisian": "fy",
    "Galician": "gl", "Georgian": "ka", "German": "de", "Greek": "el", "Guarani": "gn",
    "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha", "Hawaiian": "haw", "Hebrew": "he or iw",
    "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu", "Icelandic": "is", "Igbo": "ig",
    "Ilocano": "ilo", "Indonesian": "id", "Irish": "ga", "Italian": "it", "Japanese": "ja",
    "Javanese": "jv or jw", "Kannada": "kn", "Kazakh": "kk", "Khmer": "km", "Kinyarwanda": "rw",
    "Konkani": "gom", "Korean": "ko", "Krio": "kri", "Kurdish": "ku", "Kurdish (Sorani)": "ckb",
    "Kyrgyz": "ky", "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lingala": "ln",
    "Lithuanian": "lt", "Luganda": "lg", "Luxembourgish": "lb", "Macedonian": "mk", "Maithili": "mai",
    "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Maori": "mi",
    "Marathi": "mr", "Meiteilon (Manipuri)": "mni-Mtei", "Mizo": "lus", "Mongolian": "mn",
    "Myanmar (Burmese)": "my", "Nepali": "ne", "Norwegian": "no", "Nyanja (Chichewa)": "ny",
    "Odia (Oriya)": "or", "Oromo": "om", "Pashto": "ps", "Persian": "fa", "Polish": "pl",
    "Portuguese (Portugal, Brazil)": "pt", "Punjabi": "pa", "Quechua": "qu", "Romanian": "ro",
    "Russian": "ru", "Samoan": "sm", "Sanskrit": "sa", "Scots Gaelic": "gd", "Sepedi": "nso",
    "Serbian": "sr", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd", "Sinhala (Sinhalese)": "si",
    "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Spanish": "es", "Sundanese": "su",
    "Swahili": "sw", "Swedish": "sv", "Tagalog (Filipino)": "tl", "Tajik": "tg", "Tamil": "ta",
    "Tatar": "tt", "Telugu": "te", "Thai": "th", "Tigrinya": "ti", "Tsonga": "ts",
    "Turkish": "tr", "Turkmen": "tk", "Twi (Akan)": "ak", "Ukrainian": "uk", "Urdu": "ur",
    "Uyghur": "ug", "Uzbek": "uz", "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh",
    "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu"
}


def translate(text, source_lang, target_lang):
    """test"""
    url = "https://translate.google.com/translate_a/single"
    data = {
        "client": "gtx",
        "sl": source_lang,
        "tl": target_lang,
        "dt": ["t", "bd", "ex"],
        "dj": 1,
        "ie": "UTF-8",
        "oe": "UTF-8",
        "q": text,
    }
    response = requests.get(url, params=data)

    if response.status_code != 200:
        return f"Error Happend, response status code is {response.status_code}"

    translation = json.loads(response.text)["sentences"][0]["trans"]

    return translation
