import requests
import collections


def convert_common_letters_to_p0mp(c_letters, user_input):
    def fun(str_letter):
        return next(c_letter for c_letter in c_letters if (c_letter[0] == str_letter))

    return map(fun, list(user_input))


def get_total_letter_count(p_letters):
    # doe je ding
    return map(lambda c_letter: c_letter[1], p_letters)


response = requests.get('https://p0mp.com')


common_letters = collections.Counter(str(response.content)).most_common()
p0mp_letters = list(convert_common_letters_to_p0mp(common_letters, 'weyland'))
p0mp_letter_totals = list(get_total_letter_count(p0mp_letters))
total_numbers = sum(p0mp_letter_totals)

print(response)
print(f"""
	Response status:
	{response.status_code}

	Response content:
	{common_letters}

	Response content2:
	{p0mp_letters}

	Response content3:
	{p0mp_letter_totals}

	Response total letter count numbers total numbers:
	{total_numbers}

	Response encoding:
	{response.encoding}
""")
