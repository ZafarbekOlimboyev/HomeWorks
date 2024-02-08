from pdf2image import convert_from_path
from multiprocessing import Pool

def pdf_to_jpg(pdf_data):
    pdf_path, output_folder, pdf_number = pdf_data
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        output_path = f"{output_folder}/{pdf_number}-mavzu_{i}.jpg"
        image.save(output_path, "JPEG")
        print(f"{pdf_number}-mavzu_{i}.jpg saved")

def process_pdf(pdfs):
    with Pool() as pool:
        pool.map(pdf_to_jpg, pdfs)

def main():
    pdfs = [(f"pdfs/{i}-mavzu.pdf", "JPEGS_MP", i) for i in range(1, 13)]
    process_pdf(pdfs)

if __name__ == "__main__":
    main()
