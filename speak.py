#! /bin/python3

from gtts import gTTS
import os
from PyPDF2 import PdfReader
class pdf():


    def convert_pdf_to_text(pdf_path, output_path):

        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_content = page.extract_text()
            text += page_content
        with open(output_path, "w") as f:
            f.write(text)
class speaking():
    def speak(i,lang="en"):

        # The text that you want to convert to audio
        with open(i,"r") as w:
            mytext = w.read()
        #mytext = 'Hello, this is some text that I want to convert to audio'

        # Language in which you want to convert
        language = input("enter the language according to gtts module support by default it is en")
        if language =="":
            Language="en"
        else:
            pass
        # Passing the text and language to the engine
        myobj = gTTS(text=mytext, lang=language, slow=False)

        # Saving the converted audio as an mp3 file
        myobj.save(i+".mp3")

        # Playing the converted file
        #os.system("mpg321 welcome.mp3")



#seting variables for input and output files
pdf_file = input("enter path of pdf ")
output_file_txt = input("enter the output text file :")#input("name of output file")
pdf_path=pdf_file+".pdf"
output_path=output_file_txt+".txt"

#now calling functions for pdf
pdf.convert_pdf_to_text(pdf_path, output_path)
speaking.speak(output_path)
print(f"PDF converted to text and saved to '{output_path}' and then its is converted in to audio file with the same name ")

