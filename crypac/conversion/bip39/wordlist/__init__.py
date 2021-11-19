from pkg_resources import resource_string

def get_word_list(language):
	word_list = resource_string(__name__, language + '.txt')
	word_list = word_list.decode('utf-8').strip().split("\n")

	return word_list