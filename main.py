import os
import time
import shutil

if __name__ == '__main__':
    # args = sys.argv
    # src_dir = args[1]
    # dst_dir = args[2]
    src_dir = "hogehoge"
    dst_dir = "hogehoge"

    pdfs = []
    for r, _, f in os.walk(src_dir):
        for file in f:
            if file.endswith(".pdf"):
                pdfs.append(os.path.join(r, file))
    print("-----------------------------------")
    print("num of pdf is " + pdfs.__len__().__str__())
    print("-----------------------------------")
    for pdf in pdfs:
        shutil.copyfile(pdf, dst_dir + "/" + time.time().__str__() + ".pdf")
