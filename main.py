from file.file2text import read_file_into_text

import configparser

config = configparser.ConfigParser()

def run_job():
    config.read('resources/config.ini')

    # Read the file into the text
    text = read_file_into_text( config)
    print(text)


if __name__ == '__main__':
    run_job()

