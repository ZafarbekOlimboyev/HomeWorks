from pdf2image import convert_from_path

def pdf_to_jpg(pdf_path, output_folder,pdf_number):
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        output_path = f"{output_folder}/{pdf_number}-mavzu_{i}.jpg"
        image.save(output_path, "JPEG")
        print(f"{pdf_number}-mavzu_{i}.jpg saved")

def pdf_p(out_floder):
    for i in range(1,13):
        pdf_to_jpg(f"pdfs/{i}-mavzu.pdf",out_floder,i)

if __name__ == "__main__":
    pdf_p("JPEGS_SP")