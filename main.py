from xhtml2pdf import pisa
import requests

def convert_url_to_pdf(url, pdf_path):
    try:

        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text


        with open(pdf_path, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)

        return not pisa_status.err

    except requests.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return False
    except IOError as e:
        print(f"An error occurred while writing the PDF file: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


url_to_fetch = input("Enter the valid URL: ")  # "https://google.com"


pdf_path = "google.pdf"


if convert_url_to_pdf(url_to_fetch, pdf_path):
    print(f"PDF generated and saved at {pdf_path}")
else:
    print("PDF generation failed")