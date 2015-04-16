from Tkinter import *
import tkFileDialog, json

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
        self.btnQuit = Button(frame, text="Quit", fg="red", command=frame.quit).grid(row=3, columnspan=2)


        
    def openGeoJSON(self):
        print "hi! i'm going to open a geojson file!"
        file_path = tkFileDialog.askopenfilename()
        if file_path != "":
            print "Selected file: " + file_path
##            with open(file_path) as geojson_data:
##                def as_complex(dct):
##                    if '__complex__' in dct:
##                        return complex(dct['real'], dct['imag'])
##                        return dct
##
##                d = json.loads(geojson_data, object_hook=as_complex)
##                geojson_data.close()
##                print d
        else:
            print "no file selected"



root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional;
