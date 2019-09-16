from pyPdf  import PdfFileReader, PdfFileWriter
from pyPdf.generic import NameObject, createStringObject

inpfn = raw_input('Enter PDF path : ')

fin = file(inpfn, 'rb')
pdf_in = PdfFileReader(fin)

writer = PdfFileWriter()

for page in range(pdf_in.getNumPages()):
    writer.addPage(pdf_in.getPage(page))

infoDict = writer._info.getObject()

info = pdf_in.documentInfo
for key in info:
    infoDict.update({NameObject(key): createStringObject(info[key])})

# add the grade
list_of_data_to_delete = ['/CreationDate','/Author','/Creator','/ModDate','/Producer','/Title']
for item in list_of_data_to_delete:
    try:
        infoDict.update({NameObject(item): createStringObject(u'')})
    except:
        print("can't delete : ",i)

fout = open('outputFile.pdf', 'wb')

writer.write(fout)
fin.close()
fout.close()
