from PIL import Image
import os

def convert_jpeg_to_png(input_path, output_path):
    try:
        # Read JPEG
        with Image.open(input_path) as img:
            # Convert to PNG
            img = img.convert('RGB')
            
            # Save PNG
            img.save(output_path, 'PNG')
        
        print(f"Successfully converted {input_path} to {output_path}")
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    print("JPEG to PNG Converter")
    
    while True:
        # Input JPEG file
        input_file = input("Enter the path to the JPEG file (or 'q' to quit): ").strip()
        
        if input_file.lower() == 'q':
            print("Thank you for using the JPEG to PNG Converter. Goodbye!")
            break
        
        if not os.path.isfile(input_file) or not input_file.lower().endswith(('.jpg', '.jpeg')):
            print("Error: Invalid JPEG file. Please provide a valid JPEG file path.")
            continue
        
        # Generate output PNG file path
        output_file = os.path.splitext(input_file)[0] + '.png'
        
        # Convert JPEG to PNG
        if convert_jpeg_to_png(input_file, output_file):
            print(f"Output PNG file: {output_file}")
        else:
            print("Conversion failed. Please try again with a different file.")

if __name__ == "__main__":
    main()
