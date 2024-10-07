import tkinter as tk
from tkinter import filedialog, messagebox, StringVar
from tkinterdnd2 import TkinterDnD, DND_FILES  # Drag and drop functionality
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# importing the text compressor module
from huffman import huffman
# importing the image compressor module (Assuming this module exists)
from img_compress import EfficientImageCompressor  # Replace with your actual image compressor class

class CompressionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Text and Image Compression")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f0f0")

        # Title
        self.title_label = tk.Label(root, text="Text and Image Compression", font=("Arial", 24, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.file_path = None

        # Drag and Drop Frame
        self.drop_frame = tk.Frame(root, width=500, height=150, bg="#ffffff", relief="groove", bd=2)
        self.drop_frame.pack(pady=10)
        self.drop_frame.pack_propagate(False)

        self.drop_label = tk.Label(self.drop_frame, text="Drag & Drop a file here", font=("Arial", 14), bg="#ffffff")
        self.drop_label.pack(expand=True)

        # Enable Drag and Drop
        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.on_file_drop)

        # Browse Button
        self.browse_button = tk.Button(root, text="Browse File", font=("Arial", 14), command=self.browse_file)
        self.browse_button.pack(pady=10)

        # Compression Type Selection
        self.compression_type_label = tk.Label(root, text="Select Compression Type", font=("Arial", 14), bg="#f0f0f0")
        self.compression_type_label.pack(pady=5)

        self.compression_type = StringVar(value=None)
        self.text_radio = tk.Radiobutton(root, text="Text Compression", variable=self.compression_type, value="text", font=("Arial", 12), bg="#f0f0f0", command=self.show_decompress_button)
        self.image_radio = tk.Radiobutton(root, text="Image Compression", variable=self.compression_type, value="image", font=("Arial", 12), bg="#f0f0f0", command=self.show_image_compression_options)
        self.text_radio.pack()
        self.image_radio.pack()

        # Compression Level for Images (hidden by default)
        self.compression_level_label = tk.Label(root, text="Image Compression Level", font=("Arial", 14), bg="#f0f0f0")
        self.compression_level_dropdown = None
        self.compression_level = StringVar(value="medium")

        # Compress and Decompress Buttons
        self.compress_button = tk.Button(root, text="Compress", font=("Arial", 14), command=self.compress_file)
        self.compress_button.pack(pady=20)

        # Decompress Button (hidden by default)
        self.decompress_button = tk.Button(root, text="Decompress", font=("Arial", 14), command=self.decompress_text_file)
        self.decompress_button.pack_forget()  # Hidden by default

    def on_file_drop(self, event):
        self.file_path = event.data
        self.update_drop_label()

    def browse_file(self):
        filetypes = (("All Files", "*.*"),)
        self.file_path = filedialog.askopenfilename(title="Select a File", filetypes=filetypes)
        if self.file_path:
            self.update_drop_label()

    def update_drop_label(self):
        """Update the drop label to show the selected file path."""
        self.drop_label.config(text=os.path.basename(self.file_path) if self.file_path else "Drag & Drop a file here")

    def compress_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file")
            return

        compression_type = self.compression_type.get()

        if compression_type == "text":
            self.compress_text_file(self.file_path)
        elif compression_type == "image":
            compression_level = self.compression_level.get()
            self.compress_image_file(self.file_path, compression_level)

    def compress_text_file(self, file_path):
        try:
            compressor = huffman()  # Initialize the Huffman class without arguments
            output_path = compressor.compress_file(file_path)  # Use the new method
            messagebox.showinfo("Success", f"Text file compressed and saved at {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error compressing text file: {e}")

    def compress_image_file(self, file_path, compression_level):
        try:
            compressor = EfficientImageCompressor()  # Initialize your image compressor
            output_path = compressor.compress_image(file_path, compression_level)
            messagebox.showinfo("Success", f"Image compressed and saved at {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error compressing image: {e}")

    def show_image_compression_options(self):
        self.compression_level_label.pack(pady=5)

        if self.compression_level_dropdown is None:
            self.compression_level_dropdown = tk.OptionMenu(self.root, self.compression_level, "low", "medium", "high")
            self.compression_level_dropdown.pack()

        self.compress_button.config(text="Compress Image")
        self.decompress_button.pack_forget()  # Hide decompress button

    def show_decompress_button(self):
        self.decompress_button.pack()

    def decompress_text_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file to decompress")
            return

        try:
            compressor = huffman()  # Initialize the Huffman class without arguments
            output_text = compressor.decompress_file(self.file_path)  # Use the new method
            output_file_path = self.file_path.replace('.huff', '.txt')  # Change the output file extension
            with open(output_file_path, 'w') as output_file:
                output_file.write(output_text)
            messagebox.showinfo("Success", f"File decompressed and saved at {output_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error decompressing text file: {e}")

if __name__ == "__main__":
    root = TkinterDnD.Tk()  # Use TkinterDnD for drag-and-drop functionality
    app = CompressionGUI(root)
    root.mainloop()
