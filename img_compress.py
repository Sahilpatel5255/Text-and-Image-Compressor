from PIL import Image
import os

class EfficientImageCompressor:
    def __init__(self):
        pass

    def compress_image(self, image_path, compression_level="medium", max_size=None):
        """
        Compress the image using JPEG compression with selectable levels and optional resizing.
        
        :param image_path: Path to the input image file.
        :param compression_level: Level of compression ('low', 'medium', 'high').
        :param max_size: Tuple (width, height) to resize the image (optional).
        :return: Path to the compressed image.
        """
        # Set JPEG quality based on the compression level
        compression_levels = {
            "low": 90,    # Low compression, high quality
            "medium": 60, # Medium compression, balanced quality
            "high": 30    # High compression, lower quality
        }
        quality = compression_levels.get(compression_level.lower(), 60)  # Default to medium

        try:
            # Open the image
            img = Image.open(image_path)

            # Resize the image if max_size is provided
            if max_size:
                img.thumbnail(max_size, Image.Resampling.LANCZOS)

            # Set the output path to a .jpg if not provided
            filename, ext = os.path.splitext(image_path)
            output_path = f"{filename}_compressed_{compression_level}.jpg"

            # Save the image with JPEG compression
            img.save(output_path, "JPEG", quality=quality, optimize=True)
            print(f"Image successfully compressed at {compression_level} level and saved at {output_path}")
            return output_path
        except Exception as e:
            print(f"Error compressing image: {e}")
            return None
