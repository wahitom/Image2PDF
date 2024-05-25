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

   