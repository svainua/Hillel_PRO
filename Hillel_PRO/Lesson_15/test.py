import pandas

data = pandas.read_csv("currency_list.csv")
data_dict = data.to_dict()


def from_short_to_long(short: str) -> str:
    reverse_dict = {v: k for k, v in data_dict["currency code"].items()}
    value_to_find = short
    key = reverse_dict.get(value_to_find)

    return data_dict["currency name"][key]


currency_short_name = input(
    "what is the currency short name you would like to check?: \n"
).upper()
print(from_short_to_long(currency_short_name))
