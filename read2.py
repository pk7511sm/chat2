#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#轉換
def convert(lines):
	count_Allen_words = 0
	allen_sticker_count = 0
	count_Allen_picture = 0
	count_Viki_words = 0
	Viki_sticker_count = 0
	count_Viki_picture = 0
	for line in lines:
		s = line.split(' ')
		name = s[1]
		if name == "Allen":
			if s[2] =='照片':
				allen_sticker_count += 1
			elif s[2] == "圖片":
				count_Allen_picture += 1
			for words in s[2:]:
				count_Allen_words += len(words)
		elif name == "Viki":
			if s[2] =='照片':
				Viki_sticker_count += 1
			elif s[2] == "圖片":
				count_Viki_picture += 1
			for words in s[2:]:
				count_Viki_words += len(words)
	print("Allen一共有", allen_sticker_count, "張照片")
	print("Allen一共有", count_Allen_picture, "張圖片")
	print("Allen一共有", count_Allen_words, "個字")
	print("Viki一共有", Viki_sticker_count, "張照片")
	print("Viki一共有", 	count_Viki_picture, "張圖片")
	print("Viki一共有", 	count_Viki_words, "個字")

#寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding= 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	convert(lines)
	write_file('output2.txt', lines)

if __name__ == "__main__":
	main()

