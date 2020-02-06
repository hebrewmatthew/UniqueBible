import config, pprint, platform
from translations import translations
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
        "menu1_setDefaultFont": "Select Default Font and Size",
        "menu1_setChineseFont": "Select Chinese Font",
        "menu1_setAbbreviations": "Select Bible Abbreviations",
        "menu1_setMyFavouriteBible": "Select my Favourite Bible",
        "menu1_setMyLanguage": "Select my Language",
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
        "menu3_main": "Bible Window's History",
        "menu3_mainBack": "Bible Window's Previous Record",
        "menu3_mainForward": "Bible Window's Next Record",
        "menu3_study": "Study Window's History",
        "menu3_studyBack": "Study Window's Previous Record",
        "menu3_studyForward": "Study Window's Next Record",
        "menu4_further": "Further Study",
        "menu4_book": "Book Features",
        "menu4_chapter": "Chapter Features",
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
        "menu4_compareAll": "Compare All Bible Versions",
        "menu4_moreComparison": "Comparison / Parallel Reading / Difference",
        "menu5_search": "Search",
        "menu5_bible": "Bibles",
        "menu5_main": "Bible Window's Last Opened Bible",
        "menu5_study": "Study Window's Last Opened Bible",
        "menu5_dictionary": "The Last Opened Bible Dictionary",
        "menu5_encyclopedia": "The Last Opened Bible Encyclopedia",
        "menu5_book": "The Last Opened Reference Book",
        "menu5_selectBook": "Reference Book",
        "menu5_favouriteBook": "My Favourite Reference Books",
        "menu5_allBook": "All Reference Books",
        "menu5_characters": "Bible Characters",
        "menu5_names": "Bible People Names",
        "menu5_locations": "Bible Locations",
        "menu5_topics": "Bible Topics",
        "menu5_lastTopics": "The Last Opened Bible Topics",
        "menu5_allTopics": "All Bible Topics",
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
        "menu8_settings": "Select Import Options",
        "menu8_tagFile": "Add Bible Reference Links to a File",
        "menu8_tagFiles": "Add Bible Reference Links to Multiple Files",
        "menu8_tagFolder": "Add Bible Reference Links to a Folder's Files",
        "menu9_information": "Information",
        "menu9_credits": "Sources",
        "menu9_contact": "Contact us",
        "menu10_books": "Books",
        "menu10_dialog": "Open a Reference Book",
        "menu10_addFavourite": "Add a Favourite Reference Book",
        "menu10_displayContent": "Display Content: Study / New Window",
        "menu10_bookOnNew": "Further book content will be opened on a new window.",
        "menu10_bookOnStudy": "Further book content will be opened on Study Window.",
        "context1_copy": "Copy",
        "context1_speak": "Speak",
        "context1_english": "Translate into English",
        "context1_tChinese": "翻譯成繁體中文",
        "context1_sChinese": "翻译成简体中文",
        "context1_my": "My Language",
        "context1_translate": "Translate into",
        "context1_pinyin": "翻译成汉语拼音",
        "context1_search": "Search",
        "context1_current": "Search Opened Bible Book",
        "context1_favourite": "Search my Favourite Bible",
        "context1_original": "Search Hebrew / Greek Bible",
        "context1_originalLexicon": "Search Hebrew / Greek Lexicon",
        "context1_favouriteBooks": "Search my Favourite Reference Books",
        "context1_allBooks": "Search All Reference Books",
        "context1_encyclopedia": "Bible Encyclopedia",
        "context1_dict": "Bible Dictionary",
        "context1_extract": "Extract All Bible References",
        "context1_command": "Run as Command",
        "bar1_title": "Top Toolbar",
        "bar2_title": "Second Toolbar",
        "bar3_title": "Left Sidebar",
        "bar4_title": "Right Sidebar",
        "bar2_enableBible": "Open Bible References on Study Window",
        "bar2_disableBible": "Open Bible References on Bible Window",
        "bar1_menu": "Select / Search Bible Window's Bible",
        "bar1_reference": "Bible Window's Bible Reference",
        "bar1_chapterNotes": "Bible Window's Bible Chapter Notes",
        "bar1_verseNotes": "Bible Window's Bible Verse Notes",
        "bar1_searchBible": "Search Bible Window's Last Opened Bible",
        "bar1_searchBibles": "Search Bible Window's Bible",
        "bar1_command": "Type your command here",
        "bar1_toolbars": "Show / Hide Other Toolbars",
        "bar2_menu": "Select / Search Study Window's Bible",
        "bar2_reference": "Study Window's Bible Reference",
        "bar2_chapterNotes": "Study Window's Bible Chapter Notes",
        "bar2_verseNotes": "Study Window's Bible Verse Notes",
        "bar2_searchBible": "Search Study Window's Last Opened Bible",
        "bar2_searchBibles": "Search Study Window's Bible",
        "bar2_searchBooks": "Search Reference Book",
        "bar3_pdf": "Export to PDF",
        "note_title": "Note Editor Menu Bar",
        "note_save": "Save",
        "note_saveAs": "Save as",
        "note_print": "Print",
        "note_toolbar": "Show / Hide Toolbar",
        "note_mode": "Rich Format / Plain Mode",
        "noteTool_title": "Toolbar",
        "noteTool_bold": "Bold Font",
        "noteTool_italic": "Italic Font",
        "noteTool_underline": "Underline Style",
        "noteTool_trans0": "Transform Selected Text",
        "noteTool_trans1": "For example, create a bullet list:",
        "noteTool_trans2": "For example, create a numbered list:",
        "noteTool_trans3": "For example, create a table:",
        "noteTool_no1": "one",
        "noteTool_no2": "two",
        "noteTool_no3": "three",
        "noteTool_no4": "four",
        "noteTool_no5": "five",
        "noteTool_no6": "six",
        "noteTool_left": "Align Left",
        "noteTool_centre": "Align Centre",
        "noteTool_right": "Align Right",
        "noteTool_justify": "Justify Text",
        "noteTool_delete": "Delete Formatting",
        "noteTool_hyperlink": "Add a Hyperlink",
        "noteTool_image": "Add an Image",
        "tabBible": "Bible",
        "tabStudy": "Tool",
        "message_done": "Done.",
        "message_fail": "Failed to complete the last operation!",
        "message_invalid": "Entered command is invalid!",
        "message_missing": "Missing component:",
        "message_installFirst": "Install it first and try again.",
        "message_restart": "Restart this application to apply the new changes.",
        "message_run": "Before you can run this feature, you need to:",
        "message_selectWord": "Select a word or some words.",
        "message_setLanguage": "Select your language.",
        "message_translateFirst": "Translate program interface into your language.",
        "message_improveTrans": "To improve the quality of interface translation, you may close this application first and manually edit this file:",
        "message_newInterfaceItems": "Added new translated items of program interface.",
        "message_migration": "Some of your files are old.  We are helping you to upgrade those files.",
        "message_noReference": "Found no bible reference.",
        "message_noSupport": "It looks like that this feature does not work on your device.",
        "message_newerFile": "This file has a newer version:",
        "message_installFrom": "Install from menu:",
        "message_downloadAllFiles": "It takes time to complete this operation.",
        "message_noSupportedFile": "No valid file.",
        "message_tagged": "Tagged file is prefixed with:",
        "message_willBeNoticed": "You will receive another message when the operation is done.",
        "html_searchBible2": "Search Bible:",
        "html_searchBibles2": "Search Multiple Bibles:",
        "html_features": "Special Features:",
        "html_and": "and:",
        "html_showCompare": "Show Comparison",
        "html_showParallel": "Show Parallel Reading",
        "html_showDifference": "Show Difference",
        "html_current": "Current Selection:",
        "html_bibles": "Bible Version:",
        "html_book": "Bible Book:",
        "html_chapter": "Bible Chapter:",
        "html_verse": "Bible Verse:",
        "html_open": "open",
        "html_openHere": "open HERE",
        "html_openMain": "open on Bible Window",
        "html_openStudy": "open on Study Window",
        "html_introduction": "Introduction",
        "html_overview": "Overview",
        "html_summary": "Summary",
        "html_chapterIndex": "Bible Characters & Locations",
        "html_timelines": "Timelines",
        "message_remarks": "Remarks:",
        "message_cancel": "Cancel",
        "message_install": "Download and Install",
        "message_downloadHelper": "Download Helper",
        "message_searchMorphology": "Search Morphology",
        "import_linebreak": "Additional linebreak for each bible verse",
        "import_strongNo": "Allow search for Strong's numbers",
        "import_morphCode": "Allow search for morphology codes",
        "import_rtl": "Old Testament Text Direction: Right-to-left",
        "message_addFavouriteVersion": "Add as a parallel version for reading multiple bible verse references:",
        "search_notFound": "[no result]",
        "menu11_multimedia": "Multimedia",
        "menu11_images": "Images",
        "menu11_music": "Music",
        "menu11_video": "Video",
        "menu11_setupDownload": "Instructions to Setup YouTube Downloader",
        "menu11_youtube": "Download YouTube Audio / Video",
        "youtube_back": "Back",
        "youtube_forward": "Forward",
        "youtube_mp3": "Download Audio in mp3 Format",
        "youtube_mp4": "Download Video in mp4 Format",
        "youtube_address": "Enter a YouTube address:",
        "youtube_copy": "Copy Opened Link",
        "menu9_donate": "Donate to us",
        "menu8_moreBooks": "Download More Reference Books",
        "menu1_moreConfig": "Select More ...",
        "message_readWiki": "Read Wiki pages for more information:",
        "menu1_tabNo": "Select Number of Tabs",
        "menu5_last3rdDict": "The Last Opened Third Party Dictionary",
        "menu8_marvelData": "Database Files",
    }

    def translateInterface(self, language):
        code = self.codes[language]
        print(code)
        if code in translations:
            print("available")
            config.translationLanguage = language
            return True
        elif not platform.system() == "Windows":
            print("translating interface into '{0}' ...".format(language))
            translator = Translator()
            tempDict = {}
            for key, value in self.translation.items():
                tempDict[key] = value
                try:
                    tempDict[key] = translator.translate(value, dest=code).text
                except:
                    tempDict[key] = value
            config.translationLanguage = language
            config.translation = tempDict
            print("Done")
            return True
        return False

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
