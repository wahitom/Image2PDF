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

  