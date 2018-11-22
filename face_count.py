import cv2
import face_recognition as fr


class face_count:
	def _init_():
		pass
	def load_camera(self):
		cap = cv2.VideoCapture(0+ cv2.CAP_DSHOW)
		cap.set(3, 480)
		cap.set(4, 640)
		max_faces_num = 0
 
		while cap.isOpened():
			flag, img_rd = cap.read()
			key = cv2.waitKey(1)
	
			#取灰度
			img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)
	
			#获取人脸的位置
			faces = fr.face_locations(img_gray)
			faces_num = len(faces)
			max_faces_num = max(max_faces_num,faces_num)
	
			font = cv2.FONT_HERSHEY_SIMPLEX
	
			if faces_num != 0:
				for (top,right,bottom,left) in faces:
					cv2.rectangle(img_rd, (left, top), (right, bottom), (128, 128, 128), 2)
			
			#为了避免环境因素和人的移动等造成的点名人数不精确，这里取最大faces_num作为输出
			ft = "There are "+ str(max_faces_num) +" hentai here"
			cv2.putText(img_rd, "press 'Q': quit", (20, 400), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
			cv2.putText(img_rd, ft, (20, 450), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
	
			cv2.namedWindow("camera", 1)
			cv2.imshow("camera", img_rd)
			if key == ord("q"):
				break
		
		cap.release()
		cv2.destroyAllWindows()
		
	def show(self):
		self.load_camera()
