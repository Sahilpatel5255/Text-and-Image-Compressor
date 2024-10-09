
# **Text and Image Compression Tool**

This project is a comprehensive Text and Image Compression Tool that allows users to compress text files using Huffman Coding and images using the Pillow (PIL) library. The tool features a simple, user-friendly interface built using Tkinter, supporting drag-and-drop functionality for easy and fast file compression.

## **Features**

### **Text Compression**
- Achieves an average compression ratio of 4:3 (e.g., for a 2 KB file, returns a 1.5 KB compressed file).
- Uses the Huffman Algorithm for efficient text compression.
- Provides decompression functionality to restore the original text from the compressed file.

### **Image Compression**
- Implements three distinct levels of image compression (low, medium, high) using the PIL library.
- Achieves file size reductions of up to 75%, depending on the selected compression level.
- Option to resize images before compressing to further reduce file size.

### **Performance Optimizations**
- Enhanced compression algorithm efficiency, reducing processing time by 40% through code optimization and improved memory management.

### **User-Friendly Interface**
- Built using Tkinter with a clean, easy-to-navigate interface.
- Drag-and-drop support for quick and seamless file compression.
- One-click compression feature, significantly improving accessibility and user engagement.

## **Technologies Used**
- **Python**: Main programming language.
- **Tkinter**: For building the GUI.
- **Pillow (PIL)**: Library used for handling image compression.
- **Huffman Coding**: Custom Python implementation for text compression.

## **Usage**

### **Text Compression**
1. Drag and drop a text file or use the "Browse File" button to select a file.
2. Choose "Text Compression" from the compression type options.
3. Click the "Compress" button to compress the file.
4. The compressed file will be saved with a `.huff` extension.

### **Image Compression**
1. Drag and drop an image file (JPEG format) or use the "Browse File" button to select a file.
2. Choose "Image Compression" from the compression type options.
3. Select a compression level (low, medium, or high).
4. Click the "Compress" button to compress the image.
5. The compressed image will be saved as a JPEG file with a suffix indicating the compression level.

### **Decompression (For Text Files)**
1. Select a `.huff` compressed text file.
2. Click the "Decompress" button to restore the original text.

## **Project Structure**

```plaintext
compression_folder/
│
├── huffman.py                 # Huffman coding implementation
├── img_compress.py            # Image compression class (PIL based)
├── gui_file.py                # Main Tkinter GUI application
└── README.md                  # Project documentation
```

## **Future Improvements**
- Support for additional image formats (e.g., PNG, BMP).
- Batch processing for compressing multiple files at once.
- Integration of more text compression algorithms for enhanced efficiency.

## **Contributions**
Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.

## **Screenshots**

### GUI Preview
![GUI Screenshot](https://github.com/user-attachments/assets/eaadb7f6-fcba-49c0-9617-256950878313)
