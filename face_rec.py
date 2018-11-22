import cv2
import face_recognition as fr
import numpy as np
import pickle 
from music import music_player

class face_rec:
	def _init_():
		self.name_dict = {'sn':'name'}
		self.coding_dict = {'sn','coding'}
		
	def load_sn(self):
		with open("name.txt",'rb') as f:
			self.name_dict = pickle.load(f)
			
	def load_coding(self):
		with open("coding.txt",'rb') as f:
			self.coding_dict = pickle.load(f)
			if len(self.coding_dict)==1:
				raise (Exception,"No registered students")
			del self.coding_dict['sn']
	#创建点名册
	def mk_name_list(self):
		name_list={}
		for key in self.name_dict.keys():
			name_list[key]=False
		del name_list['sn']
		return name_list
		
	def codings_get(self,face_img):
		codings = fr.face_encodings(face_img,None,4)
		return codings
	
	def face_compare(self,codings,name_list):
		for sn,face_coding in self.coding_dict.items():
			mc = fr.compare_faces(codings, face_coding,tolerance=0.37)
			for rs in mc :
				if rs:
					name_list[sn]=True
				
				
		for sn,match in name_list.items():
			if not match:
				name = self.name_dict[sn]
				print("Student "+name+" did not attend class,his student number is "+sn)	
			else:
				music_player(sn)

				
	def take_a_photo(self):
		cap = cv2.VideoCapture(0)
		cap.set(3, 480)
		cap.set(4, 640)
		while cap.isOpened():
			flag, img_rd = cap.read()
			frame = img_rd[:, :, ::-1]
			key = cv2.waitKey(1)	
			font = cv2.FONT_HERSHEY_SIMPLEX	
			
			cv2.putText(img_rd, "press 'Q': quit", (20, 400), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
			cv2.putText(img_rd, "press 'S': save", (20, 450), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)	
			

			if key == ord("s"):
				codings = self.codings_get(frame)
				if len(codings) < 1:
					print("No face detected")
				else:
					name_list = self.mk_name_list()
					self.face_compare(codings,name_list)	
					print(name_list)
					print("done")
				
			cv2.namedWindow("camera", 1)
			cv2.imshow("camera", img_rd)
			if key == ord("q"):
				break
				
		cap.release()
		cv2.destroyAllWindows()
		
	def show(self):
		self.load_sn()
		try :
			self.load_coding()
		except (Exception,err):
			print (err)
		self.take_a_photo()
