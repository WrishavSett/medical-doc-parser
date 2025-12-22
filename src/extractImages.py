import os

def _extract_images_from_pdf(
        pdf_path, 
        output_path="output/pdf_images/"):
    
    try:
        from pdf2image import convert_from_path
    except ImportError:
        raise ImportError("pdf2image not found. Install via 'pip install pdf2image==1.17.0'.")
    
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]  # Base filename without extension
    output_dir = os.path.join(output_path, pdf_name)            # PDF specific directory

    os.makedirs(output_path, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        pages = convert_from_path(pdf_path, dpi=300)
    except Exception as e:
        raise RuntimeError(f"Error converting PDF to images: {e}")

    for i, page in enumerate(pages, start=1):
        page.save(f"{output_dir}/page_{i}.png", "PNG")

    return output_dir