import cv2
import face_recognition as fr
import numpy as np
import pickle 
from os import path
from PIL import Image

class face_load:

	def _init_(self):
		self.name = 'name'
		self.sn   = 'sn'
		self.name_dict = {'sn':'name'}
		self.coding_dict = {'sn','coding'}
		
	def new_student_load(self):
		self.name = input("Your name ")
		self.sn   = input("Your sn ")
		self.name_dict = self.load_sn()
		self.name_dict[self.sn] = self.name
		self.save_dict(self.name_dict)
		
	def load_sn(self):
		if not path.exists('name.txt'):
			dict = {'sn':'name'}
			self.save_dict(dict)
		with open("name.txt",'rb') as f:
			dict = pickle.load(f)
			return dict
			
	def load_coding(self):
		if not path.exists('coding.txt'):
			dict = {'sn':'coding'}
			self.save_dict(dict)
		with open("coding.txt",'rb') as f:
			dict = pickle.load(f)
			return dict
		
	def save_dict(self,dict):
		file_name = dict['sn'] + ".txt"
		with open(file_name,'wb') as f:
			pickle.dump(dict,f)
			
	def coding_load(self,face_img):
		coding = fr.face_encodings(face_img,None,4)[0]
		if len(coding) != 128:
			print("No face detected, please try again")
		else:
			self.coding_dict = self.load_coding()
			self.coding_dict[self.sn] = coding
			self.save_dict(self.coding_dict)
			print("The classmate "+self.name+" has successfully entered")
		
	#完成输入，调用摄像头进行拍照1
	def load_camera(self):
		cap = cv2.VideoCapture(0)
		cap.set(3, 480)
		cap.set(4, 640)
		while cap.isOpened():
			flag, img_rd = cap.read()
			key = cv2.waitKey(1)
			#RGB
			frame = img_rd[:, :, ::-1]
			#获取人脸的位置
			faces = fr.face_locations(frame)
			faces_num = len(faces)
	
			font = cv2.FONT_HERSHEY_SIMPLEX
	
			if faces_num == 1:
				#获取头像位置
				for (top,right,bottom,left) in faces:
					cv2.rectangle(img_rd, (left, top), (right, bottom), (0, 128, 0  ), 2)
				
				cv2.putText(img_rd, "press 'S': save", (20, 450), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
				#保存人物图片并进行编码储存
				if key == ord("s"):
					face_image = frame[top:bottom, left:right]
					pil_image = Image.fromarray(face_image)
					img_name = self.name+'.jpg'
					pil_image.save(img_name)
					self.coding_load(face_image)
			else:
				cv2.putText(img_rd, "No face detected,please face the camera", (20, 450), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
				
			if key == ord("q"):
				break	
				
			cv2.putText(img_rd, "press 'Q': quit", (20, 400), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
			cv2.namedWindow("camera", 1)
			cv2.imshow("camera", img_rd)
				
				
		cap.release()
		cv2.destroyAllWindows()
		
	def show(self):
		self.new_student_load()
		self.load_camera()
	
