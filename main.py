import flet as ft
from pdf2docx import Converter
import os

def main(page: ft.Page):
    page.title = "PDF to WORD Converter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    status_text = ft.Text("")

    def on_file_picked(e: ft.FilePickerResultEvent):
        if not e.files:
            return
        
        pdf_path = e.files[0].path
        docx_path = pdf_path.rsplit(".", 1)[0] + ".docx"
        
        status_text.value = "Converting PDF to editable DOCX... Please wait."
        page.update()

        try:
            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
            status_text.value = f"Saved to: {docx_path}"
        except Exception as ex:
            status_text.value = f"Error: {ex}"
        
        page.update()

    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    page.add(
        ft.Text("PDF to WORD Converter", size=26, weight=ft.FontWeight.BOLD),
        ft.Text("Convert PDF to editable DOCX with layout & images preserved."),
        ft.ElevatedButton(
            "Select PDF File",
            bgcolor="#e5322d",
            color="white",
            on_click=lambda _: file_picker.pick_files(allowed_extensions=["pdf"])
        ),
        status_text
    )

ft.app(target=main)
