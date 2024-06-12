
class WordWriter():
    def __init__(self, document):
        self.document = document



    def write(self, value, output_path):
        array_elements = value
        for element in array_elements:
            self.document.add_paragraph(element)
        self.document.save(output_path)