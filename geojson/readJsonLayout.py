from Tkinter import *
import tkFileDialog, json, os
from datetime import datetime

#class GeoJSON:
    

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.btnLoad = Button(frame, text="Load GeoJSON", command=self.openGeoJSON).grid(row=0)
        self.lblAttr = Label(frame, text="Attributes:").grid(row=1, sticky=W, padx=5)
        self.lstAttr = Listbox(frame, selectmode=EXTENDED)
        self.lstAttr.grid(row=2)

        for item in ["attr1", "attr2", "attr3", "attr4"]:
            self.lstAttr.insert(END, item)

        self.lblAction = Label(frame, text="Actions:").grid(row=1, column=1, sticky=W, padx=5)
        self.btnDelAttr = Button(frame, text="Delete attributes").grid(row=2, column=1, sticky=N, padx=5)
        self.btnOtherAction = Button(frame, text="Other action").grid(row=2, column=1, sticky=N, padx=5, pady=30)
        ##self.btnQuit = Button(frame, text="Quit", fg="red", command=frame.quit).grid(row=3, columnspan=2)


        
    def openGeoJSON(self):
        print "hi! i'm going to open a geojson file!"
        file_path = tkFileDialog.askopenfilename()
        if file_path != "":
            print "Selected file: " + file_path

            file_size_b = os.path.getsize(file_path)
            file_size_KB = file_size_b/1000
            file_size_MB = file_size_KB/1000
            print "File size: ~" + str(file_size_KB) + " KB (~ " + str(file_size_MB) + " MB)"
            
            start_time = datetime.now()
            print "Start process: " + str(start_time)
            data = json.loads(open(file_path).read().decode('utf-8-sig'))
            ##file_path.close() ## close file?
            print json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))
            end_time = datetime.now()
            print "End process: " + str(end_time)
            duration = end_time - start_time
            print "Duration: " + str(duration)
        else:
            print "no file selected"


root = Tk()

app = App(root)

root.mainloop()
#root.destroy() # optional;
