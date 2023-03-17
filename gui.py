import os
import time
import pyautogui
import shutil
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from PIL import Image, ImageFilter

root = Tk()
root.title("YoloV7 Train and Detection")
root.geometry("640x640")
root.configure(background="Light blue")

fila=''
#Labels
label0 = ttk.Label(text="YOLO Train and Detection",font="Arial,100", background="Light blue")
label0.place(relx=0.3, rely=0.05)

label1 = ttk.Label(text="Please select a weapon category:",font="Arial,25",background="Light blue")
label1.place(relx=0.0, rely=0.15)

label2 = ttk.Label(text="Please select a image source :",font="Arial,25",background="Light blue")
label2.place(relx=0.0, rely=0.3)

label3 = ttk.Label(text="Please select the blur intensity:",font="Arial,25",background="Light blue")
label3.place(relx=0.0, rely=0.45)



#Image


#Combobox
cmd=ttk.Combobox(root,width="35", values=("gl(online-video-cutter.com).mp4","g19.jpg","Browse file"))
cmb = ttk.Combobox(root, width="35", values=("Pistols","Knives","Axes","Heavy Firearms"))
cmd_batch=ttk.Combobox(root, width="35", values=("1","2","3","4","5","6","7","8"))
cmd_epochs=ttk.Combobox(root, width="35", values=("10","20","30","40","50","60","70","80","90","100"))
cma=ttk.Combobox(root,width="35", values=("1","2","3","4","5","6","7","8","9","10"))
cmb_cut = ttk.Combobox(root, width="35", values=("Left","Right","Top","Bottom"))
cma_cut=ttk.Combobox(root,width="35", values=("1","2","3","4","5","6","7","8","9","10"))
#browse

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Pictures",
                                                      "*.jpg*"),
                                                     ("Video",
                                                      "*.mp4*"),
                                                     ("all files",
                                                      "*.*")))
    fila=filename
    return(fila)

def checkcmbo():

     if os.path.exists('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp') and os.path.exists('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp2'):
         shutil.rmtree('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp')
         shutil.rmtree('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp2')
     if cmb.get() == "Pistols" and not cmd.get()=="Browse file" :
         val=cmd.get()
         OriImage = Image.open(val)
         gaussImage=OriImage.filter(ImageFilter.GaussianBlur(int(cma.get())))
         val2 = 'pistol'
         gaussImage.save('blur_' + val2 + '.jpg')
         vals=val.split('.')
         value = "python detect.py --weights yolov7_pistol.pt --conf 0.5 --img-size 640 --source " + val +" --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         value = "python detect.py --weights yolov7_pistol.pt --conf 0.5 --img-size 640 --source " + "blur_pistol.jpg" + " --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         with open('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp/labels/'+vals[0]+'.txt', 'r') as file:
             data = file.read().replace('\n', '')
             print(data)
     elif cmb.get() == "Pistols" and  cmd.get()=="Browse file" :
            val = browseFiles()
            OriImage = Image.open(val)
            gaussImage = OriImage.filter(ImageFilter.GaussianBlur(int(cma.get())))
            val2='pistol'
            vals = val.replace('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/','')
            vals=vals.split('.')
            gaussImage.save('blur_'+val2+'.jpg')
            value = "python detect.py --weights yolov7_pistol.pt --conf 0.5 --img-size 640 --source " + val +" --view-img --save-txt --no-trace --save-txt"
            stream = os.popen(value)
            out = stream.read()
            pyautogui.alert(out)
            value = "python detect.py --weights yolov7_pistol.pt --conf 0.5 --img-size 640 --source " + "blur_pistol.jpg" + " --view-img --no-trace --save-txt"
            stream = os.popen(value)
            out = stream.read()
            pyautogui.alert(out)
            with open('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp/labels/' + vals[0] + '.txt', 'r') as file:
                data = file.read().replace('\n', '')
                print(data)

     if cmb.get() == "Knives"and not cmd.get()=="Browse file":
         val = cmd.get()
         OriImage = Image.open(val)
         gaussImage = OriImage.filter(ImageFilter.GaussianBlur(int(cma.get())))
         val2='knife'
         vals=val.split('.')
         gaussImage.save('blur_'+val2+'.jpg')
         value = "python detect.py --weights yolov7_knife.pt --conf 0.5 --img-size 640 --source "+ val+" --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         value = "python detect.py --weights yolov7_knife.pt --conf 0.5 --img-size 640 --source " + "blur_knife.jpg" + " --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         with open('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp/labels/'+vals[0]+'.txt', 'r') as file:
             data = file.read().replace('\n', '')
             print(data)
     elif cmb.get() == "Knives" and  cmd.get()=="Browse file" :
         val = browseFiles()
         OriImage = Image.open(val)
         gaussImage = OriImage.filter(ImageFilter.GaussianBlur(int(cma.get())))
         val2='knife'
         vals = val.replace('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/', '')
         vals=val.split('.')
         gaussImage.save('blur_'+val2+'.jpg')
         value = "python detect.py --weights yolov7_knife.pt --conf 0.5 --img-size 640 --source " + val +" --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         value = "python detect.py --weights yolov7_knife.pt --conf 0.5 --img-size 640 --source " + "blur_knife.jpg" + " --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         with open('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp/labels/'+vals[0]+'.txt', 'r') as file:
             data = file.read().replace('\n', '')
             print(data)

     if cmb.get() == "Axes" and not cmd.get()=="Browse file":
         val = cmd.get()
         OriImage = Image.open(val)
         gaussImage = OriImage.filter(ImageFilter.GaussianBlur(int(cma.get())))
         val2='hatchet'
         vals=val.split('.')
         gaussImage.save('blur_'+val2+'.jpg')
         value = "python detect.py --weights yolov7_hatchet.pt --conf 0.5 --img-size 640 --source "+ val +" --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         value = "python detect.py --weights yolov7_hatchet.pt --conf 0.5 --img-size 640 --source " + "blur_hatchet.jpg" + " --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         with open('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp/labels/'+vals[0]+'.txt', 'r') as file:
             data = file.read().replace('\n', '')
             print(data)
     elif cmb.get() == "Axes" and  cmd.get()=="Browse file" :
         val = browseFiles()
         OriImage = Image.open(val)
         gaussImage = OriImage.filter(ImageFilter.GaussianBlur(int(cma.get())))
         val2='hatchet'
         vals = val.replace('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/', '')
         vals=val.split('.')
         gaussImage.save('blur_'+val2+'.jpg')
         value = "python detect.py --weights yolov7_hatchet.pt --conf 0.5 --img-size 640 --source " + val +" --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         value = "python detect.py --weights yolov7_hatchet.pt --conf 0.5 --img-size 640 --source " + "blur_hatchet.jpg" + " --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         with open('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp/labels/'+vals[0]+'.txt', 'r') as file:
             data = file.read().replace('\n', '')
             print(data)

     if cmb.get() =="Heavy Firearms" and not cmd.get()=="Browse file":
         val = cmd.get()
         OriImage = Image.open(val)
         gaussImage = OriImage.filter(ImageFilter.GaussianBlur(int(cma.get())))
         val2='Military'
         vals=val.split('.')
         gaussImage.save('blur_'+val2+'.jpg')
         value = "python detect.py --weights yolov7_Military.pt --conf 0.5 --img-size 640 --source  "+ val +"--view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         value = "python detect.py --weights yolov7_Military.pt --conf 0.5 --img-size 640 --source " + "blur_Military.jpg" + " --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         with open('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp/labels/'+vals[0]+'.txt', 'r') as file:
             data = file.read().replace('\n', '')
             print(data)
     elif cmb.get() == "Heavy Firearms" and  cmd.get()=="Browse file" :
         val = browseFiles()
         OriImage = Image.open(val)
         gaussImage = OriImage.filter(ImageFilter.GaussianBlur(int(cma.get())))
         val2='Military'
         vals = val.replace('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/', '')
         vals=val.split('.')
         gaussImage.save('blur_'+val2+'.jpg')
         value = "python detect.py --weights yolov7_Military.pt --conf 0.5 --img-size 640 --source " + val +" --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         value = "python detect.py --weights yolov7_Military.pt --conf 0.5 --img-size 640 --source " + "blur_Military.jpg" + " --view-img --no-trace --save-txt"
         stream = os.popen(value)
         out = stream.read()
         pyautogui.alert(out)
         with open('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp/labels/'+vals[0]+'.txt', 'r') as file:
             data = file.read().replace('\n', '')
             print(data)

     with open('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp2/labels/blur_'+val2+'.txt', 'r') as file:
         data1 = file.read().replace('\n', '')
         print(data1)

def delete():
    shutil.rmtree('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp')
    shutil.rmtree('C:/Users/ASUS/Desktop/proiecte/yolo/yolov7_custom/runs/detect/exp2')

btn = ttk.Button(root, text="Run selection",  width=30,command=checkcmbo)
btn2=ttk.Button(root, text="Delete runs",  width=30,command=delete)
# btn3=ttk.Button(root, text="Cut",  width=30,command=cut)
cmb.place(relx="0.0",rely="0.2")
cma.place(relx="0.0",rely="0.50")
cmd.place(relx="0.0",rely="0.35")
btn.place(relx="0.0",rely="0.6")
btn2.place(relx="0.0",rely="0.7")



root.mainloop()
