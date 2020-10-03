from PyPDF2 import PdfFileWriter, PdfFileReader

def secure_pdf(inputFile, password):
    writer = PdfFileWriter()
    reader = PdfFileReader(inputFile)
    for page in range(reader.numPages):
        writer.addPage(reader.getPage(page))
    writer.encrypt(password)

    # writer.encrypt(user_pwd=password, use_128bit=True )

    with open(f"encrypted_{inputFile}", "wb") as f:
        writer.write(f)
        f.close()
    print(f"encrypted_{inputFile} Created...")


if __name__ == "__main__":
    inputF = 'test.pdf'
    password = "laljr"
    secure_pdf(inputF, password)
