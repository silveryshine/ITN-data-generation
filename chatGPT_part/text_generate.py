import argparse
import json
import os
import re
from datetime import time, datetime

import openai


def main_dep(openai_key:str, input_dir:str, output_dir:str):
    openai.api_key = openai_key
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Do you know about text normalization that converts text from written to spoken form?"},
        {"role": "assistant", "content": """Yes, I'm familiar with text normalization techniques used to convert text from written form to spoken form. Text normalization is the process of transforming text into a standard or normalized format, typically to improve the quality and consistency of text-to-speech (TTS) systems.
In the context of converting written text to spoken form, text normalization involves handling various aspects such as expanding abbreviations, resolving acronyms, converting numbers and symbols into spoken words, handling punctuation, and adapting the text to match natural language patterns and prosody.
Here are some common techniques used in text normalization:
Abbreviation Expansion: Text normalization involves expanding abbreviations and converting them into their full forms. For example, "Mr." could be expanded to "Mister," or "Dr." to "Doctor."
Acronym Resolution: Acronyms are often converted into their spoken equivalents. For instance, "NASA" could be pronounced as "N-A-S-A" or "National Aeronautics and Space Administration" depending on the context.
Number Conversion: Text normalization involves converting numeric values into their spoken form. For example, "123" might be pronounced as "one hundred twenty-three."
Symbol Handling: Symbols like punctuation marks or special characters are typically omitted or converted into appropriate verbal cues. For instance, "!" could be pronounced as "exclamation mark" or simply as "bang."
Capitalization Handling: Capitalized words are often normalized to match spoken language patterns. For example, "USA" might be pronounced as "U-S-A" or "United States of America" depending on the context.
Emphasis and Prosody: Text normalization can add prosodic information, such as emphasis or intonation, to enhance the naturalness and expressiveness of the spoken output. This involves analyzing the structure and context of the text to determine appropriate stress patterns and intonation.
Text normalization is an important step in the development of high-quality TTS systems. It helps ensure that the spoken output sounds natural, intelligible, and conforms to the expectations of the target language or dialect."""},
        {"role": "user", "content": "Can you convert the following text: Doctor Dan is in room 241 and will be free at 2:30pm today"},
        # {"role": "assistant",
        #  "content": "The World Series in 2020 was played in Arlington, Texas at the Globe Life Field."},
        # {"role": "user", "content": "Who was the MVP of the series?"},
        # {"role": "assistant",
        #  "content": "Corey Seager of the Los Angeles Dodgers was named the MVP of the 2020 World Series."},
        # {"role": "user", "content": "Has any team won three consecutive championships?"},
        # {"role": "assistant",
        #  "content": "Yes, the New York Yankees won three consecutive World Series championships from 1998 to 2000."},
        # Add more questions and answers as needed
    ]

    # Make the API request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        # temperature=0
    )

    # Extract assistant's reply from the API response
    assistant_reply = response['choices'][0]['message']['content']
    print(assistant_reply)

    conversation.append({"role": "assistant",
         "content": assistant_reply})
    conversation.append({"role": "user",
                         "content": "can you extract the converted written and spoken form word pairs out into JSON format?"})

    response2 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        # temperature=0
    )
    assistant_reply2 = response2['choices'][0]['message']['content']
    print(assistant_reply2)

    conversation.append({"role": "assistant",
                         "content": assistant_reply2})
    conversation.append({"role": "user",
                         "content": "do you know Google text normalization dataset?"})
    conversation.append({"role": "assistant",
                         "content": """Yes, I'm familiar with the Google Text Normalization Dataset. The Google Text Normalization Dataset is a publicly available dataset released by Google that consists of written and spoken form pairs for text normalization tasks. It is designed to facilitate research and development in text normalization and related areas, such as natural language processing (NLP) and speech synthesis.
The dataset covers a wide range of text normalization challenges, including handling abbreviations, acronyms, numbers, symbols, and other linguistic variations. It provides a valuable resource for training and evaluating text normalization models and algorithms.
The Google Text Normalization Dataset is typically used by researchers and developers to train and evaluate text normalization systems, including those used in text-to-speech (TTS) applications. It helps improve the accuracy and effectiveness of text normalization processes and contributes to the development of more natural and fluent speech synthesis systems.
Researchers and developers can access the Google Text Normalization Dataset through the Google AI Datasets platform, where it can be downloaded and utilized for various text normalization tasks."""})
    conversation.append({"role":"user",
                         "content":"please add types to the written and spoken form word pairs. The typs should be the ones that used in google text normalization dataset with no extension. Each pair only need one type"})

    response3 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        # temperature=0
    )
    assistant_reply3 = response3['choices'][0]['message']['content']
    print(assistant_reply3)



def chat_with_GPT(in_str:str, openai_key: str) -> dict:
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user",
         "content": "Do you know about text normalization that converts text from written to spoken form?"},
        {"role": "assistant",
         "content": """Yes, I'm familiar with text normalization, which is the process of converting written text into spoken form. Text normalization is an important step in natural language processing (NLP) tasks such as speech synthesis, voice assistants, and other applications that involve converting written text into spoken words.
    The goal of text normalization is to transform written text, which often includes abbreviations, acronyms, symbols, and other non-standard forms, into a more standardized and phonetically correct spoken form. This process helps ensure that the synthesized speech sounds natural and is easily understandable to human listeners.
    Text normalization involves several subtasks, including:
    1. Expansion of abbreviations and acronyms: Abbreviations and acronyms are expanded into their full forms. For example, "NLP" might be expanded to "natural language processing."
    2. Number normalization: Numeric expressions are converted into their spoken form. For example, "123" might be converted to "one hundred twenty-three."
    3. Symbol handling: Special symbols, punctuation marks, and other non-alphanumeric characters are processed appropriately. For example, "3.14" might be converted to "three point one four."
    4. Date and time normalization: Dates and times are converted into spoken form, adhering to the appropriate formats. For example, "2023-05-31" might be converted to "May 31, 2023."
    5. Phonemic conversion: Words or phrases that are written in a non-standard form but are pronounced differently are converted into their phonetically correct spoken form. For example, "wanna" might be converted to "want to."
    Text normalization can be achieved using various techniques, including rule-based methods, statistical models, and machine learning approaches. These methods rely on linguistic resources, such as dictionaries, language models, and phonetic representations, to accurately convert written text into spoken form.
    It's worth noting that text normalization can be a challenging task due to the inherent ambiguity and variability of written language. Different regions, dialects, and languages may require specific normalization rules and adaptations to accurately convert text to spoken form."""},
        {"role": "user",
         "content": "Can you convert the following text: Doctor Dan is in room 241 and will be free at 2:30pm on Jan 3rd, 2023."},
        {"role": "assistant",
         "content": """Sure! Here's the converted text:
    "Doctor Dan is in room two four one and will be free at two thirty p.m. on January thrid, 2023." """},
        {"role": "user",
         "content": "In ITN research, the words are marked in diverse types. Here are the commonly used types: PLAIN, DATE, LETTERS, CARDINAL, VERBATIM, DECIMAL, MEASURE, MONEY, ORDINAL, TIME, ELECTRONIC, DIGIT, FRACTION, TELEPHONE, ADDRESS, PUNCT. A widely used dataset called Google text normalization dataset uses this group of types."},
        {"role": "assistant",
         "content": """Thank you for providing the commonly used types in text normalization research. These types are indeed widely used in various text normalization tasks, including the Google text normalization dataset. Here's a brief description of each type:
    1. PLAIN: Represents plain words or phrases that do not require any special normalization. These are typically regular words found in the text.
    2. DATE: Represents expressions related to dates, such as "2023-05-31" or "May 31, 2023."
    3. LETTERS: Represents sequences of letters, often used for alphabetic characters or words.
    4. CARDINAL: Represents cardinal numbers, such as "123" or "one hundred twenty-three."
    5. VERBATIM: Represents words or phrases that should be read exactly as they are written, without any modifications or normalizations.
    6. DECIMAL: Represents decimal numbers, such as "3.14" or "three point one four."
    7. MEASURE: Represents expressions related to measurements, such as "10 cm" or "5 kilograms."
    8. MONEY: Represents expressions related to currency or monetary values, such as "$10" or "5 euros."
    9. ORDINAL: Represents ordinal numbers, such as "1st," "2nd," or "third."
    10. TIME: Represents expressions related to time, such as "2:30 p.m." or "12:00 PM."
    11. ELECTRONIC: Represents electronic-related expressions, such as URLs, email addresses, or usernames.
    12. DIGIT: Represents individual digits, typically used for numerical digits in isolation.
    13. FRACTION: Represents fractions, such as "1/2" or "three-fourths."
    14. TELEPHONE: Represents telephone numbers, such as "555-123-4567."
    15. ADDRESS: Represents address-related expressions, such as street addresses or postal codes.
    16. PUNCT: Represents punctuation marks, such as commas, periods, or question marks.
    These types help categorize and handle different forms of text in the normalization process, enabling more accurate and consistent conversion of written text into spoken form."""},
        {"role": "user",
         "content": "can you extract the converted written and spoken form word pairs out into JSON format? Also add type for each word pair"},
        {"role": "assistant",
         "content": """Certainly! Here's an example of how the converted word pairs, along with their types, can be represented in JSON format:
    ```json
    {
      "word_pairs": [
        {
          "written": "Doctor",
          "spoken": "Doctor",
          "type": "PLAIN"
        },
        {
          "written": "Dan",
          "spoken": "Dan",
          "type": "PLAIN"
        },
        {
          "written": "is",
          "spoken": "is",
          "type": "PLAIN"
        },
        {
          "written": "in",
          "spoken": "in",
          "type": "PLAIN"
        },
        {
          "written": "room",
          "spoken": "room",
          "type": "PLAIN"
        },
        {
          "written": "241",
          "spoken": "two forty-one",
          "type": "CARDINAL"
        },
        {
          "written": "and",
          "spoken": "and",
          "type": "PLAIN"
        },
        {
          "written": "will",
          "spoken": "will",
          "type": "PLAIN"
        },
        {
          "written": "be",
          "spoken": "be",
          "type": "PLAIN"
        },
        {
          "written": "free",
          "spoken": "free",
          "type": "PLAIN"
        },
        {
          "written": "at",
          "spoken": "at",
          "type": "PLAIN"
        },
        {
          "written": "2:30pm",
          "spoken": "two thirty p.m.",
          "type": "TIME"
        },
        {
          "written": "on",
          "spoken": "on",
          "type": "PLAIN"
        },
        {
          "written": "Jan 3rd, 2023",
          "spoken": "January thrid, twenty twenty three",
          "type": "DATE"
        },
        {
          "written": ".",
          "spoken": ".",
          "type": "PUNCT"
        }
      ]
    }
    ```
    In this example, the "word_pairs" array contains individual word pairs, each represented as an object with three properties: "written" for the written form of the word, "spoken" for the spoken form of the word, and "type" indicating the type of the word according to the given classification. """},
        {"role": "user",
         "content": "Now do the same procedure on following sentence: " + in_str},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        # temperature=0
    )
    assistant_reply = response['choices'][0]['message']['content']
    print(assistant_reply)

    regex_str = '```json[\S\s]*```'
    find = re.findall(regex_str, assistant_reply)
    result_json = find[0][7:-4]
    # print(result_json)
    result = json.loads(result_json)
    # print(result)
    return result

def main(openai_key:str, input_dir:str, output_dir:str):
    openai.api_key = openai_key
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    track_fp = open(os.path.join(output_dir, "completed.txt"), 'r')
    completed = track_fp.readlines()
    track_fp.close()

    track_fp = open(os.path.join(output_dir, "completed.txt"), 'a')

    out_fp = open(os.path.join(output_dir, "result" + str(datetime.now().timestamp()) + ".txt"), "w")

    for file_name in os.listdir(input_dir):
        if file_name in completed:
            continue
        print(file_name)
        with open(os.path.join(input_dir, file_name), 'r') as in_fp:
            lines = in_fp.readlines()
            for line in lines:
                line = " ".join(line.split()[2:])
                print(line)
                try:
                    transformation_dict = chat_with_GPT(line, openai_key)
                    # print(transformation_dict)
                    for sub_dict in transformation_dict["word_pairs"]:
                        out_fp.write(sub_dict["type"] + "\t" + sub_dict["written"] + "\t" + sub_dict["spoken"] + "\n")
                    out_fp.write("<eos>\t<eos>\n")
                    out_fp.flush()
                except:
                    pass
        track_fp.write(file_name + '\n')
    out_fp.close()




if __name__=="__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--json", required=True)
    # args = parser.parse_args()
    #
    # with open(args.json, "r") as j_obj:
    #     config = json.load(j_obj)

    config = {
        "api_key" : "",
        "input_dir" : r"D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\segmented_text_with_times",
        "output_dir": r"D:\study\singaporeMasters\master_project\term2\data\youtube_crawler\Chris@HoneyMoneySG\chatGPT",
    }


    main(config["api_key"], config["input_dir"],config["output_dir"])