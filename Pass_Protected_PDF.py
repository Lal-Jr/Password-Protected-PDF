from PyPDF2 import PdfFileWriter, PdfFileReader

def encrpyt(inputfile, outputfile, password):
    writer = PdfFileWriter()
    reader = PdfFileReader(inputfile)

    for page in range(reader.getnumPages()):
        writer.addPage(reader.getPage(page))
    
    writer.encrypt(user_pwd=password, use_128bit=True )
    with open(f"encrypted_{outputfile}", "wb") as pdf:
        writer.write(pdf)
        f.close()
    print(f"encrypted_{outputfile} Created...")

if __name__ == "main":
    inputfile = 'C:/Users/HAREESH/Documents/GitHub/Password-Protected-PDF/test'
    outputfile = 'C:/Users/HAREESH/Documents/GitHub/Password-Protected-PDF/test_encrypted'
    password = "laljr"
    encrpyt(inputfile,outputfile, password)   