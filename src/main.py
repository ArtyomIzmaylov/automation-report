from extractor import DataExcelExtractor
from cleaner import DataCleaner
from transformer import ArrayTransformer
from writer import WordWriter
from docx import Document

extractor = DataExcelExtractor()
transformer = ArrayTransformer()
pathToExcelFile = 'input/students.xlsx'
extract_data = extractor.extract(pathToExcelFile, 'Students')
cleaner = DataCleaner(extract_data)

clean_data = cleaner.clean(1)
tasks_array = transformer.transform(clean_data, clean_data.columns[1])
prefixed_list = ["{}.".format(i+1) + item for i, item in enumerate(tasks_array)]
wordWriter = WordWriter(Document(), '{placeholder}')
result_string = ''.join(prefixed_list)

wordWriter.rewriteNew(tasks_array, 'output/output.docx')
