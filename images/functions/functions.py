import re

def find_cpf(text):
    """Function to find CPFs in the extracted text.
    \nReturns a list of found CPFs or False if none found.
    \nTo be found, the value should be in the format xxx.xxx.xxx-xx.
    \nExample:
    text = text extracted from the image
    CPFs = find_cpf(text)"""
    cpf_list = re.findall('[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}', text)
    if len(cpf_list) > 0:
        return cpf_list
    else:
        return False

def find_date(text):
    """Function to find dates in the extracted text.
    \nReturns a list of found dates or False if none found.
    \nTo be found, the value should be in the format xx/xx/xxxx.
    \nExample:
    text = text extracted from the image
    dates = find_date(text)"""
    date_list = re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}', text)
    if len(date_list) > 0:
        return date_list
    else:
        return False

def find_bad_words(text):
    """Function to find occurrences of 'bad' words in the extracted text.
    \nSkips repeated words. Returns an int and a float.
    \nRespectively, the count of 'bad' words found and the percentage of them in the whole text.
    \nExample:
    text = text extracted from the image
    count, percentage = find_bad_words(text)"""
    count_bad = 0
    bad_words = open("functions/bad_words.txt").read()
    bad_words = bad_words.split("\n")
    text_words = set(re.split('[,;.?!/-: ]', text))
    for word in text_words:
        if word.upper() in bad_words:
            count_bad += 1
    percentage = calculate_percentage(count_bad, len(text_words))
    return count_bad, percentage

def find_good_words(text):
    """Function to find occurrences of 'good' words in the extracted text.
    \nSkips repeated words. Returns an int and a float.
    \nRespectively, the count of 'good' words found and the percentage of them in the whole text.
    \nExample:
    text = text extracted from the image
    count, percentage = find_good_words(text)"""
    count_good = 0
    good_words = open("functions/good_words.txt").read()
    good_words = good_words.split("\n")
    text_words = set(re.split('[,;.?!/-: ]', text))
    for word in text_words:
        if word.upper() in good_words:
            count_good += 1
    percentage = calculate_percentage(count_good, len(text_words))
    return count_good, percentage

def calculate_percentage(count, total):
    """Function to calculate the percentage of good/bad words.
    \nReturns a float, the percentage.
    \nExample:
    count = count of good/bad words
    total = total word count in the text
    percentage = calculate_percentage(count, total)"""
    percentage = (count / total) * 100
    return percentage

def summarize_cpf(cpf_list):
    """Function to format CPFs as a string.
    \nReturns a string.
    \nExample:
    cpf_list = list of CPFs found in the text
    CPF_summary = summarize_cpf(cpf_list)"""
    cpf_summary = ". ".join(cpf_list)
    return cpf_summary

def summarize_dates(date_list):
    """Function to format dates as a string.
    \nReturns a string.
    \nExample:
    date_list = list of dates found in the text
    DATES_summary = summarize_dates(date_list)"""
    dates_summary = ". ".join(date_list)
    return dates_summary
