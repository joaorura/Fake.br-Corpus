from os import listdir
from os.path import isfile, join, abspath
from pandas import DataFrame

FAKE_PATH = abspath(r'C:\Users\jmess\Documents\Workspace\UFAL\Fake.br-Corpus\size_normalized_texts\fake')
TRUE_PATH = abspath(r'C:\Users\jmess\Documents\Workspace\UFAL\Fake.br-Corpus\size_normalized_texts\true')
PATH_SAVE = abspath(r'C:\Users\jmess\Documents\Workspace\UFAL\Fake.br-Corpus\csv_data\data.csv')

def get_files(path):
	onlyfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

	return onlyfiles


def read_txt_files(path):
	all_path = get_files(path)
	all_txt = []

	for i in all_path:
		f = open(i, "r", encoding='utf-8')
		text = f.read()
		all_txt.append(text)

	return all_txt

def main():
	fake_news = read_txt_files(FAKE_PATH)
	true_news = read_txt_files(TRUE_PATH)
	all_txt = fake_news + true_news
	fake_result = []

	for i in range(0, len(fake_news)):
		fake_result.append(1)

	for i in range(0, len(true_news)):
		fake_result.append(0)

	data = {
		'texto': all_txt,
		'fake_news': fake_result
	}

	df = DataFrame(data)
	df.to_csv(PATH_SAVE, index=False)


if __name__ == '__main__':
	main()
