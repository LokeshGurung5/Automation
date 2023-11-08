#Title: PDF merger
#first, put this file in a new folder with the pdfs you want to merge 
# pip install pikepdf
from glob import glob #used as a function
from pikepdf import Pdf 

new_pdf = Pdf.new() #creating new PDf(Pdf.new)

for file in glob("*.pdf"): #collecting the files in the folder which ends with .pdf
    old_pdf = Pdf.open(file) #open all the pdfs in the folder
    new_pdf.pages.extend(old_pdf.pages) #extending all the pdf in the new pdf 
new_pdf.save("Self reflection.pdf") #to saving the function and naming the new pdf
#Self reflection.pdf is the name of the merged pdf which can be renamed as you like but should end with .pdf 

#youtube copy link: https://youtu.be/VeW6Y8EOQHw?si=yXKp0HaMQ1u3mt_u
# hello i am lokesh 
