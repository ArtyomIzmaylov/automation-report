from extractor import DataExcelExtractor
from cleaner import DataCleaner
from transformer import ArrayTransformer
from writer import WordWriter
from docx import Document
from dotenv import load_dotenv
import os


def main():

    extractor = DataExcelExtractor()
    transformer = ArrayTransformer()
    #######
    ##### подтягиваем .env-шки
    load_dotenv()
    path_to_input_file = os.getenv('INPUT_PATH')
    path_to_output_file = os.getenv('OUTPUT_PATH')
    sheet_name = os.getenv('SHEET_NAME')
    column_number_to_clean = os.getenv('COLUMN_NUMBER_TO_CLEAN')
    ########

    cleaner = DataCleaner(extractor.extract(path_to_input_file, sheet_name))
    clean_data = cleaner.clean(column_number_to_clean)
    tasks_array = transformer.transform(clean_data, clean_data.columns[column_number_to_clean])
    word_writer = WordWriter(Document())

    word_writer.write(tasks_array, path_to_output_file)

if __name__ == "__main__":
    main()
