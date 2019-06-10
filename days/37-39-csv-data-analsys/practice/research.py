import os
import csv
import collections

data = []

# Record = collections.namedtuple(
#     "Record",
#     "RespondentID,"
#     "Do you celebrate Thanksgiving?,"
#     "What is typically the main dish at your Thanksgiving dinner?,"
#     "What is typically the main dish at your Thanksgiving dinner? - Other (please specify),"
#     "How is the main dish typically cooked?,How is the main dish typically cooked? - Other (please specify),"
#     "What kind of stuffing/dressing do you typically have?,"
#     "What kind of stuffing/dressing do you typically have? - Other (please specify),"
#     "What type of cranberry saucedo you typically have?,"
#     "What type of cranberry saucedo you typically have? - Other (please specify),"
#     "Do you typically have gravy?,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Brussel sprouts,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Carrots,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cauliflower,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Corn,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cornbread,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Fruit salad,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Green beans/green bean casserole,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Macaroni and cheese,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Mashed potatoes,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Rolls/biscuits,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Squash,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Vegetable salad,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Yams/sweet potato casserole,"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify),"
#     "Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify),"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Buttermilk,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Cherry,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Chocolate,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Coconut cream,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Key lime,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Peach,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Sweet Potato,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - None,"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify),"
#     "Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify),"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Apple cobbler,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Blondies,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Brownies,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Carrot cake,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cheesecake,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cookies,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Fudge,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Ice cream,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Peach cobbler,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - None,"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify),"
#     "Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify),"
#     "Do you typically pray before or after the Thanksgiving meal?,"
#     "How far will you travel for Thanksgiving?,"
#     "Will you watch any of the following programs on Thanksgiving? Please select all that apply. - Macy's Parade,"
#     "What's the age cutoff at your kids' table at Thanksgiving?,"
#     "Have you ever tried to meet up with hometown friends on Thanksgiving night?,"
#     "Have you ever attended a Friendsgiving?,"
#     "Will you shop any Black Friday sales on Thanksgiving Day?,"
#     "Do you work in retail?,"
#     "Will you employer make you work on Black Friday?,"
#     "How would you describe where you live?,"
#     "Age,"
#     "What is your gender?,"
#     "How much total combined money did all members of your HOUSEHOLD earn last year?,"
#     "US Region"
# )


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'data', 'thanksgiving-2015-poll-data.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)
            print(f"Selebrate - {record['Do you celebrate Thanksgiving?']}, main dish - {record['What is typically the main dish at your Thanksgiving dinner?']}")

        print(data[:4])


def parse_row(row):
    # record = Record(
    #     **row
    # )
    record = row
    return record

