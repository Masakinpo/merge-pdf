import PyPDF2
import os
import sys

if __name__ == '__main__':
    # args = sys.argv
    # if args.__len__() == 1:
    #     print("please specify path")
    #     sys.exit(1)
    #
    # path = args[1]
    path = "/Users/Masaki/Dropbox/private/確定申告/2020/領収書"
    # print(path)

    pdfs = []
    for r, _, f in os.walk(path):
        for file in f:
            if '.pdf' in file:
                pdfs.append(os.path.join(r, file))

    writer = PyPDF2.PdfFileWriter()
    for pdf in pdfs:
        reader = PyPDF2.PdfFileReader(str(pdf))
        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))

    # 保存
    with open("merged.pdf", "wb") as f:
        writer.write(f)
