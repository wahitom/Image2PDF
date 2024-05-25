# first install tkinter for this project and import it here 
import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas 
from PIL import Image
import os

# cleare class component to handle everything
class ImageToPDFConverter:
    def __init__(self, root):
        # initialize the root first
        self.root = root

        # create necessary variables
        # 1. Create an mage variable to store our images as empty array
        self.image_paths =[]
        # 2. Create a pdf variable
        self.output_pdf_name = tk.StringVar() #because this is going to be a string 
        # 3. Create a variable for the selected images list using Listbox
        self.selected_images_listbox = tk.Listbox(root, selectmode = tk.MULTIPLE)

        # for the UI interface
        self.initialize_ui()

    # define the initialize_ui instance
    # title
    def initialize_ui(self):
        # create title for the app
        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Arial", 16, "bold"))

        # pack the title_label variables into tkinter
        title_label.pack(pady=10)

    # select image button
        select_images_button= tk.Button(self.root, text="Select Image", command=self.select_images)
        select_images_button.pack(pady=(0, 10 ))
        
        self.selected_images_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

    # output pdf name
        label = tk.Label(self.root, text="Enter output PDF name:")
        label.pack()

    # input section for user to type in pdf 
        pdf_name_entry = tk.Entry(self.root, textvariable= self.output_pdf_name, width = 40, justify='center')
        pdf_name_entry.pack()

    # convert to pdf button
        convert_button = tk.Button(self.root, text="Coonvert to PDF", command=self.convert_images_to_pdf)
        convert_button.pack(pady=(20, 40))

    # define the select_image function
    def select_images(self):
        # specify what types of images are acceeptable 
        self.image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.png; *.jpg; *.jpeg")])

        #store the names of the selected images in a variable
        self.update_selected_images_listbox()
    
    def update_selected_images_listbox(self):
        # check if there are any images selected and delete them
        self.selected_images_listbox.delete(0, tk.END)

        # write a loop to store the selected images in image_paths
        for image_path in self.image_paths:
            #  use split to delete the image paths and just leave the image name
            _, image_path = os.path.split(image_path)

            self.selected_images_listbox.insert(tk.END, image_path)

    # initialize our convert images to pdf when the convert button is clicked
    def convert_images_to_pdf(self):
        # check if user has given any name in the output textbox
        if not self.image_paths: 
            return
        
        #  default output file name 
        output_pdf_path = self.output_pdf_name.get() + ".pdf" if self.output_pdf_name.get() else "output.pdf"

        # initialize the page size for the pdf because the normal page size is 600-800px
        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))

        #  insert images one by one inside the pdf using for loop
        for image_path in self.image_paths:
            img = Image.open(image_path)

            # initializing a wdth and height for our image
            available_width = 540
            available_height = 720

            #  mean value of our available width by the image width and getting the new width and height
            scale_factor = min(available_width/ img.width, available_height/ img.height)
            new_width = img.width * scale_factor
            new_height = img.height* scale_factor

            # place the image in the center of the page
            x_centered = (612 - new_width) / 2
            y_centered = (792 - new_height) / 2

            # Color of the pdf, plecement
            pdf.setFillColorRGB(255, 255, 255)
            pdf.rect(0, 0, 612, 792, fill=True)

            pdf.drawInlineImage(img, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()
        
        # save the pdf
        pdf.save()
