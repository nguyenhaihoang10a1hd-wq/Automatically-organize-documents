# Vietnamese CV OCR & Image Organizer

## Project Overview
A Python tool that automates CV image organization by recognizing phone numbers using OCR and matching them with an Excel contact list.

## Features
- **OCR Recognition:** Uses PaddleOCR to extract Vietnamese text and phone numbers from CV images.
- **Excel Matching:** Matches recognized phone numbers with the `sdt` column in `CV.xlsx`.
- **Automatic Numbering:** Adds a corresponding sequence number to each matched image.
- **Image Organization:** Saves the numbered images into a designated output folder.

## Technologies
- Python
- PaddleOCR
- Pandas
- Pillow (PIL)

## Office Applications
- Organizing candidate CVs during recruitment.
- Matching scanned documents with Excel records.
- Reducing manual document sorting and numbering.
- Improving efficiency when processing large numbers of images.
