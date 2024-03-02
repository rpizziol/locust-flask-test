import pandas as pd
from dateutil import parser
import re

from datetime import datetime
import pytz


def remove_text_inside_parentheses(input_string):
    # Regular expression pattern to match text inside parentheses
    # pattern = r'\([^)]*\)'
    # Use re.sub() to replace the matched text with an empty string
    result_string = input_string[:25]# re.sub(pattern, '', input_string)
    return result_string


def datetime_string_to_epoch(datetime_string):
    # Specify the format of the core datetime information
    datetime_format = "%a %b %d %Y %H:%M:%S"

    # Parse the datetime string
    parsed_datetime = pd.to_datetime(datetime_string, format=datetime_format, utc=True)

    print(parsed_datetime)

    return int(parsed_datetime)


input_csv_file = 'GCP-CPU-usage.csv'
df = pd.read_csv(input_csv_file)

# Rename columns
df.columns.values[0] = 'Time'
df.columns.values[1] = 'CPU'

df.dropna(inplace=True)

df['Time'] = df['Time'].apply(remove_text_inside_parentheses)

print(df.tail())

# Obtain time in HH:MM format
df['Time'] = df['Time'].apply(datetime_string_to_epoch)


print(df.tail())



# Example usage
# datetime_string = "Tue Feb 27 2024 15:41:00 GMT+0100"
# epoch_time = datetime_string_to_epoch(datetime_string)
# print(epoch_time)

# def extract_date_time(text):
#     # Regex pattern to match the HH:MM time format
#     #pattern = r'\b\d{2}:\d{2}\b'
#     pattern = r'\b\d{2}\s\d{2}:\d{2}\b'
#
#     # Find all matches in the text
#     times = re.findall(pattern, text)
#
#     # Replace each occurrence in the original text with just the found time
#     # Assuming you want to replace the entire text with the found times joined by a separator
#     # If multiple times are found, they are joined by a space. Adjust as necessary.
#     time_text = ' '.join(times)
#
#     return time_text