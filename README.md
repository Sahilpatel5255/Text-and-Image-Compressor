#Text and Image Compression Tool

This project is a Text and Image Compression Tool that allows users to compress text files using Huffman Coding and images using the Pillow (PIL) library. The tool comes with a simple GUI interface built using Tkinter that supports drag-and-drop functionality, making it user-friendly for anyone looking to quickly compress files.

Features
Text Compression:

Compress text files using Huffman coding for efficient storage.
Decompression functionality is also provided, allowing users to restore the original text from the compressed file.
Image Compression:

Compress image files (JPEG format) with selectable compression levels (low, medium, high).
Optionally resize images before compressing to further reduce file size.
Drag-and-Drop:

Easily drag and drop files into the application for quick compression.
User-Friendly GUI:

Built using Tkinter with a clean and simple interface.
Includes options for text or image compression selection.
Technologies Used
Python
Tkinter: For building the GUI.
Pillow (PIL): For handling image compression.
Huffman Coding: Custom Python implementation for text compression.

##Usage

###Text Compression:

Drag and drop a text file or use the "Browse File" button to select a file.
Choose "Text Compression" from the compression type options.
Click the "Compress" button to compress the file.
The compressed file will be saved with the .huff extension.

###Image Compression:

Drag and drop an image file (JPEG format) or use the "Browse File" button to select a file.
Choose "Image Compression" from the compression type options.
Select a compression level (low, medium, or high).
Click the "Compress" button to compress the image.
The compressed image will be saved as a JPEG file with a suffix indicating the compression level.
Decompression (for text files):

Select a .huff compressed text file.
Click the "Decompress" button to restore the original text.

##Project Structure


compression_folder
1.huffman.py                   # Huffman coding implementation
2.img_compress.py              # Image compression class (PIL based)
3.gui file.py                   # Main Tkinter GUI application
4.README.md                    # Project documentation

##Screenshots
gui 
<img width="1277" alt="compression_desc" src="https://github.com/user-attachments/assets/eaadb7f6-fcba-49c0-9617-256950878313">




Future Improvements
Support for more image formats (PNG, BMP, etc.).
Batch processing for compressing multiple files at once.
Include additional compression algorithms for text.
Contributions
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.
