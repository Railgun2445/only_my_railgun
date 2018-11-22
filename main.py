import face_count as fc
import face_rec as fr
import face_load as fl


A = fc.face_count()
B = fl.face_load()
C = fr.face_rec()

def print_line():
	print('\n')
	print('欢迎使用，我们的宗旨是调戏学生娱乐自己')
	print('A:看看来了多少个hentai')
	print('B:又一个hentai要来上我的课')
	print('C:调戏hentai的时刻到了')
	print('Q:算了算了，放你们一马')
	print('\n')

if __name__ == '__main__':
	while (1):
		print_line()
		str = input('我的选择是:')
		if str == 'a':
			A.show()
		elif str == 'b':
			B.show()
		elif str == 'c':
			C.show()
		elif str == 'q':
			print('bye')
			break
		else:
			print('请正确输入')
		
		