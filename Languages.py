import config, pprint
# [Optional] Google-translate
try:
    from googletrans import Translator
    googletransInstall = True
except:
    googletransInstall = False

class Languages:

    codes = {
        "Afrikaans": "af",
        "Albanian": "sq",
        "Amharic": "am",
        "Arabic": "ar",
        "Armenian": "hy",
        "Azerbaijani": "az",
        "Basque": "eu",
        "Belarusian": "be",
        "Bengali": "bn",
        "Bosnian": "bs",
        "Bulgarian": "bg",
        "Catalan": "ca",
        "Cebuano": "ceb",
        "Chinese (Simplied)": "zh-CN",
        "Chinese (Traditional)": "zh-TW",
        "Corsican": "co",
        "Croatian": "hr",
        "Czech": "cs",
        "Danish": "da",
        "Dutch": "nl",
        "English": "en",
        "Esperanto": "eo",
        "Estonian": "et",
        "Finnish": "fi",
        "French": "fr",
        "Frisian": "fy",
        "Galician": "gl",
        "Georgian": "ka",
        "German": "de",
        "Greek": "el",
        "Gujarati": "gu",
        "Haitian Creole": "ht",
        "Hausa": "ha",
        "Hawaiian": "haw",
        "Hebrew he or": "iw",
        "Hindi": "hi",
        "Hmong": "hmn",
        "Hungarian": "hu",
        "Icelandic": "is",
        "Igbo": "ig",
        "Indonesian": "id",
        "Irish": "ga",
        "Italian": "it",
        "Japanese": "ja",
        "Javanese": "jv",
        "Kannada": "kn",
        "Kazakh": "kk",
        "Khmer": "km",
        "Korean": "ko",
        "Kurdish": "ku",
        "Kyrgyz": "ky",
        "Lao": "lo",
        "Latin": "la",
        "Latvian": "lv",
        "Lithuanian": "lt",
        "Luxembourgish": "lb",
        "Macedonian": "mk",
        "Malagasy": "mg",
        "Malay": "ms",
        "Malayalam": "ml",
        "Maltese": "mt",
        "Maori": "mi",
        "Marathi": "mr",
        "Mongolian": "mn",
        "Myanmar (Burmese)": "my",
        "Nepali": "ne",
        "Norwegian": "no",
        "Nyanja (Chichewa)": "ny",
        "Pashto": "ps",
        "Persian": "fa",
        "Polish": "pl",
        "Portuguese (Portugal, Brazil)": "pt",
        "Punjabi": "pa",
        "Romanian": "ro",
        "Russian": "ru",
        "Samoan": "sm",
        "Scots Gaelic": "gd",
        "Serbian": "sr",
        "Sesotho": "st",
        "Shona": "sn",
        "Sindhi": "sd",
        "Sinhala (Sinhalese)": "si",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Somali": "so",
        "Spanish": "es",
        "Sundanese": "su",
        "Swahili": "sw",
        "Swedish": "sv",
        "Tagalog (Filipino)": "tl",
        "Tajik": "tg",
        "Tamil": "ta",
        "Telugu": "te",
        "Thai": "th",
        "Turkish": "tr",
        "Ukrainian": "uk",
        "Urdu": "ur",
        "Uzbek": "uz",
        "Vietnamese": "vi",
        "Welsh": "cy",
        "Xhosa": "xh",
        "Yiddish": "yi",
        "Yoruba": "yo",
        "Zulu": "zu",
    }

    translation = {
        "menu1_app": "UniqueBible",
        "menu1_fullScreen": "Full Screen",
        "menu1_resize": "Resize",
        "menu1_topHalf": "Top Half",
        "menu1_leftHalf": "Left Half",
        "menu1_remoteControl": "Open / Close Remote Control",
        "menu1_setDefaultFont": "Configure Default Font and Size",
        "menu1_setChineseFont": "Configure Chinese Font",
        "menu1_setAbbreviations": "Configure Bible Abbreviations",
        "menu1_setMyFavouriteBible": "Configure my Favourite Bible",
        "menu1_setMyLanguage": "Configure my Language",
        "menu1_translateInterface": "Translate Program Interface into my Language",
        "menu1_toogleInterface": "Program Interface: English / My Translation",
        "menu1_wikiPages": "Wiki Pages",
        "menu1_update": "Update",
        "menu1_exit": "Exit",
        "menu2_view": "Layout",
        "menu2_all": "All Toolbars [Show / Hide]",
        "menu2_topOnly": "All Toolbars / Only Top Toolbar",
        "menu2_top": "Top Toolbar [Show / Hide]",
        "menu2_second": "Second Toolbar [Show / Hide]",
        "menu2_left": "Left Sidebar [Show / Hide]",
        "menu2_right": "Right Sidebar [Show / Hide]",
        "menu2_icons": "Toolbar Icons [Full-size / Standard]",
        "menu2_landscape": "Landscape / Portrait Orientation",
        "menu2_study": "Study Window [Resize / Hide]",
        "menu2_bottom": "Bottom Window [Show / Hide]",
        "menu2_hover": "Instant feature [Enable / Disable]",
        "menu2_larger": "Increase Font Size",
        "menu2_smaller": "Decrease Font Size",
        "menu2_format": "Formatted / Simple Style Bible",
        "menu2_subHeadings": "Add Paragraph headings on Simple Style Bible",
        "menu3_history": "History",
        "menu3_main": "Bible Window",
        "menu3_mainBack": "Previous Record",
        "menu3_mainForward": "Next Record",
        "menu3_study": "Study Window",
        "menu3_studyBack": "Previous Record",
        "menu3_studyForward": "Next Record",
        "menu4_further": "Further Study",
        "menu4_next": "Next Chapter",
        "menu4_previous": "Previous Chapter",
        "menu4_indexes": "Smart Indexes",
        "menu4_commentary": "Bible Commentary",
        "menu4_traslations": "Translations",
        "menu4_discourse": "Discourse Analysis",
        "menu4_words": "Individual Words",
        "menu4_tdw": "TDW Combo",
        "menu4_crossRef": "Cross References",
        "menu4_tske": "TSK (Enhanced edition)",
        "menu4_compareAll": "Compare All Versions",
        "menu4_compare": "Compare with ...",
        "menu4_parallel": "Parallel with ...",
        "menu5_search": "Search",
        "menu5_bible": "Bibles",
        "menu5_main": "Bible Window's Last Opened Bible",
        "menu5_study": "Study Window's Last Opened Bible",
        "menu5_dictionary": "The Last Opened Bible Dictionary",
        "menu5_encyclopedia": "The Last Opened Bible Encyclopedia",
        "menu5_book": "The Last Opened Reference Book",
        "menu5_characters": "Bible Charcters",
        "menu5_names": "Bible People Names",
        "menu5_locations": "Bible Locations",
        "menu5_topics": "Bible Topics",
        "menu5_lexicon": "Hebrew / Greek Lexicon",
        "menu5_3rdDict": "Third Party Dictionaries",
        "menu6_notes": "Notes",
        "menu6_mainChapter": "Bible Window's Bible Chapter Notes",
        "menu6_studyChapter": "Study Window's Bible Chapter Notes",
        "menu6_searchChapters": "Search Bible Chapter Notes",
        "menu6_mainVerse": "Bible Window's Bible Verse Notes",
        "menu6_studyVerse": "Study Window's Bible Verse Notes",
        "menu6_searchVerses": "Search Bible Verse Notes",
        "menu7_topics": "Bible Topics",
        "menu7_create": "Write a New Bible Topic",
        "menu7_open": "Open a Bible Topic File",
        "menu7_recent": "Recently Opened Files",
        "menu7_read": "Read Last Opened File",
        "menu7_edit": "Edit Last Opened File",
        "menu7_paste": "Paste from Clipboard",
        "menu8_resources": "Resources",
        "menu8_bibles": "Install Formatted Bible",
        "menu8_commentaries": "Install Bible Commentary",
        "menu8_datasets": "Install Marvel.bible Datasets",
        "menu8_plusLexicons": "Install BibleBentoPlus Lexicon",
        "menu8_plusDictionaries": "Install BibleBentoPlus Dictionary",
        "menu8_3rdParty": "Import 3rd Party Module",
        "menu8_3rdPartyInFolder": "Import Multiple 3rd Party Modules",
        "menu8_settings": "Import Settings",
        "menu8_tagFile": "Add Bible Reference Links to a File",
        "menu8_tagFiles": "Add Bible Reference Links to Multiple Files",
        "menu8_tagFolder": "Add Bible Reference Links to a Folder's Files",
        "menu9_information": "Information",
        "menu9_credits": "Sources",
        "menu9_contact": "Contact us",
        "context1_copy": "Copy",
        "context1_speak": "Speak",
        "context1_english": "Translate into English",
        "context1_tChinese": "翻譯成繁體中文",
        "context1_sChinese": "翻译成简体中文",
        "context1_my": "My Language",
        "context1_translate": "Translate into",
        "context1_pinyin": "翻译成汉语拼音",
        "context1_search": "Search",
        "context1_current": "Search in Current Book",
        "context1_favourite": "Search my Favourite Bible",
        "context1_original": "Search Hebrew / Greek Bible",
        "context1_lexicon": "Hebrew / Greek Lexicon",
        "context1_character": "Bible Character",
        "context1_name": "Bible Name",
        "context1_location": "Bible Location",
        "context1_topic": "Bible Topic",
        "context1_encyclopedia": "Bible Encyclopedia",
        "context1_dict": "Bible Dictionary",
        "context1_3rdDict": "3rd Party Dictionary",
        "context1_extract": "Extract All Bible References",
        "context1_command": "Run as Command",
        "bar1_title": "Top Toolbar",
        "bar2_title": "Second Toolbar",
        "bar3_title": "Left Toolbar",
        "bar4_title": "Right Toolbar",
        "bar2_enableBible": "Enable Bible Display on Study View",
        "bar2_disableBible": "Disable Bible Display on Study View",
        "bar1_menu": "Main View Bible Menu",
        "bar1_reference": "Main View Active Verse Features",
        "bar1_chapterNotes": "Main View Chapter Notes",
        "bar1_verseNotes": "Main View Verse Notes",
        "bar1_searchBible": "Search Last Opened Bible on Main View",
        "bar1_searchBibles": "Open Search Bible Menu",
        "bar1_command": "Command Line",
        "bar1_toolbars": "Show / Hide Other Toolbars",
        "bar2_menu": "Study View Bible Menu",
        "bar2_reference": "Study View Active Verse Features",
        "bar2_chapterNotes": "Study View Chapter Notes",
        "bar2_verseNotes": "Study View Verse Notes",
        "bar2_searchBible": "Search Last Opened Bible on Study View",
        "bar2_searchBibles": "Open Search Bible Menu",
        "bar2_commentary": "Commentary Menu",
        "bar2_books": "Books",
        "bar2_searchBooks": "Search Books",
        "bar2_newTopicNote": "Create a Topical Note",
        "bar2_openTopicNote": "Open Topical Notes",
        "bar2_readTopicNote": "Read Topical Notes",
        "bar2_editTopicNote": "Edit Topical Notes",
        "bar2_smallerFont": "Smaller Font Size",
        "bar2_defontFont": "Set Default Font & Size",
        "bar2_largerFont": "Larger Font Size",
        "bar3_prev": "Main View Previous History Record",
        "bar3_history": "Main View History",
        "bar3_next": "Main View Next History Record",
        "bar3_pdf": "Export to PDF",
        "bar3_format": "Formatted / Plain Bibles \n(only if both versions are installed)",
        "bar3_subheadings": "Add Sub-headings to Plain Bibles \n(only for plain versions)",
        "bar3_prevCh": "Preivous Chapter",
        "bar3_mainPassage": "Main Passage",
        "bar3_nextCh": "Next Chapter",
        "bar3_compareAll": "Compare All Versions",
        "bar3_parallel": "Compare / Parallel with ...",
        "bar3_mob": "Marvel Original Bible",
        "bar3_mib": "Marvel Interlinear Bible",
        "bar3_mtb": "Marvel Trilingual Bible",
        "bar3_mpb": "Marvel Parallel Bible",
        "bar3_mab": "Marvel Annotated Bible",
        "bar4_prev": "Study View Previous History Record",
        "bar4_history": "Study View History",
        "bar4_next": "Study View Next History Record",
        "bar4_pdf": "Export to PDF",
        "bar4_index": "Smart Indexes",
        "bar4_commentary": "Commentary",
        "bar4_xRef": "Cross References",
        "bar4_tske": "Treasury of Scripture Knowledge (Enhanced)",
        "bar4_translations": "Translations",
        "bar4_discource": "Discourse Features",
        "bar4_words": "Words",
        "bar4_combo": "Translations + Discourse Features + Words",
        "bar4_landscape": "Landscape / Portrait Mode",
        "bar4_resize": "Resize / Hide Study View",
        "bar4_hover": "Enable / Disable Hovering Feature",
        "bar4_bottom": "Show / Hide Bottom View",
        "note_title": "Note Editor Menu Bar",
        "note_create": "Create a New Topical Note \n[Shortcut: Ctrl/Cmd + N]",
        "note_open": "Open Topical Notes \n[Shortcut: Ctrl/Cmd + O]",
        "note_save": "Save \n[Shortcut: Ctrl/Cmd + S]",
        "note_saveAs": "Save as",
        "note_print": "Print",
        "note_toolbar": "Show / Hide Toolbar",
        "note_mode": "Rich / Plain Mode",
        "note_smaller": "Smaller Font Size",
        "note_larger": "Larger Font Size",
        "note_find": "Quick Search \n[Shortcut: Ctrl/Cmd + F]",
        "noteTool_title": "Toolbar",
        "noteTool_bold": "Bold \n[Shortcut: Ctrl/Cmd + B]",
        "noteTool_italic": "Italic \n[Shortcut: Ctrl/Cmd + I]",
        "noteTool_underline": "Underline \n[Shortcut: Ctrl/Cmd + U]",
        "noteTool_transform": "Transform Selected Text: \n[Shortcut: Ctrl/Cmd + M] \n \nBullet List, e.g.: \n* bullet one \n* bullet two \n \nNumbered List, e.g.: \n*1 numbered item one \n*2 numbered item two \n \nTable, e.g.: \n{one|two|three} \n{four|five|six}",
        "noteTool_left": "Left",
        "noteTool_centre": "Centre",
        "noteTool_right": "Right",
        "noteTool_justify": "Justify",
        "noteTool_delete": "Delete Formatting \n[Shortcut: Ctrl/Cmd + D]",
        "noteTool_hyperlink": "Add a Hyperlink",
        "noteTool_image": "Add an Image",
    }

    def translateInterface(self, language):
        print("translating interface into '{0}' ...".format(language))
        translator = Translator()
        code = self.codes[language]
        tempDict = {}
        for key, value in self.translation.items():
            tempDict[key] = value
            try:
                tempDict[key] = translator.translate(value, dest=code).text
            except:
                tempDict[key] = value
        config.translationLanguage = language
        config.translation = tempDict
        print("done.")

    def createTranslationTemplates(self):
        if googletransInstall:
            for code in self.codes.values():
                print("creating '{0}' template ...".format(code))
                translator = Translator()
                tempDict = {}
                for key, value in self.translation.items():
                    tempDict[key] = value
# Note: Attempted to use Google Translate to translate interface into all languages, but access is blocked in the middle of the operation.  It looks like Google blocks access by ip, when there are too many queries within a short time.
# Don't use the following 4 lines, or ip will be blocked for Google Translate
#                    try:
#                        tempDict[key] = translator.translate(value, dest=code).text
#                    except:
#                        tempDict[key] = value
                with open("translations.py", "a") as fileObj:
                    code = code.replace("-", "")
                    fileObj.write("uB{0} = {1}\n\n".format(code, pprint.pformat(tempDict)))


if __name__ == '__main__':
    Languages().createTranslationTemplates()