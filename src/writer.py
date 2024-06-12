
class WordWriter():
    def __init__(self, document, placeholder):
        self.document = document
        self.placeholder = placeholder

    def rewrite(self, value, output_path):
        for paragraph in self.document.paragraphs:
            if self.placeholder in paragraph.text:
                paragraph.text = paragraph.text.replace(self.placeholder, str(value))

        self.document.save(output_path)

    def rewriteNew(self, value, output_path):
        array_elements = value
        for element in array_elements:
            self.document.add_paragraph(element)
        self.document.save(output_path)