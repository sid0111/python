import fitz  # PyMuPDF

def edit_pdf_text_terminal():
    pdf_path = input("Enter the path to the PDF file: ")
    old_text = input("Enter the text to find: ")
    new_text = input("Enter the new text to replace with: ")
    output_path = input("Enter the output PDF file name: ")

    doc = fitz.open(pdf_path)
    total_replacements = 0

    for page_num in range(len(doc)):
        page = doc[page_num]

        text_instances = page.search_for(old_text)

        for inst in text_instances:
            # Get the exact font size from the text blocks (optional accuracy step)
            blocks = page.get_text("dict")["blocks"]
            font_size = 12  # default fallback
            for b in blocks:
                for l in b.get("lines", []):
                    for s in l.get("spans", []):
                        if old_text in s["text"]:
                            font_size = s["size"]  # get the original font size
                            break

            # Draw white rectangle over old text
            page.draw_rect(inst, fill=(1, 1, 1))

            # Write new text at the same position with the same font size
            page.insert_text(inst[:2], new_text, fontsize=font_size, color=(0, 0, 0))

            total_replacements += 1

    if total_replacements > 0:
        doc.save(output_path)
        print(f"\n✅ Done. Replaced {total_replacements} instance(s) of '{old_text}' in '{output_path}'.")
    else:
        print(f"\n⚠️ No instances of '{old_text}' found in the document.")

if __name__ == "__main__":
    edit_pdf_text_terminal()
