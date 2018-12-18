# only_my_railgun
这个工程是上课点名系统的基本原型，这里尝试使用了开源库face_Recognition，完成了主要的人脸检测和识别的功能
face_recognition是使用了Dlib的人脸识别进行构筑，提供了方便的人脸检测和识别功能
face_count.py中主要调用了face_locations的方法，进行人脸位置的标注并记录了其人脸识别的个数。作为功能一：大致获得教室人数然后判断是否需要点名
face_load.py中主要调用了face_encodings的方法，进行人脸的编码,之后将编码存入本地。face_locations方法在这里主要进行的是人脸的标定，以便于确认是否可以录入。
face_rec.py主要是调用了compare_faces进行人脸比对，通过截取当前帧的编码和本地编码进行对照，完成了人脸识别。输出没有上课的同学名字。
music.py主要是使用了pygame的音频播放功能，这里是想在以后对代码稍作修改，对于face_rec的拍照截取的方法更改为按帧截取。布置到树莓派上面可以作为简易的宿舍门禁系统。但是实时的识别在电脑上测试后效果不佳，卡顿较为严重。官方样例中给出的优化方法是用户看到的视频在处理时采取1/4的剪裁，减小了运算量。实测这样的方法对于流畅度提升不明显，考虑采用跳帧的方法进行尝试。
关于准确度方面，这里有两个参数可以考虑。
第一：compare_faces的tolerance参数，官方建议的参数为0.6。这里推测欧美人与亚洲人的面部特征相差较大，故调整到0.37.使用者可根据自己需要调节tolerance
第二：face_encodings的第三个参数,范围为1~100，这里我选择了4.这个参数主要控制的是人脸编码的采样精细程度。但是数值越高速度越慢.
关于face_recognition的原理，这里参考了博客https://www.cnblogs.com/AdaminXie/p/9884096.html，
