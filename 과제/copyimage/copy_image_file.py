import os

def copy_image_file(file):
    buffer = 4096 # 4KB 
    name, ext = os.path.splitext(file) # 확장자랑 본문을 나눔
    with open(file, 'rb') as fr: 
        with open(name+"_copy"+ext, 'wb') as fw:
            while True:
                chunk = fr.read(buffer) # 4kb 만큼만 읽음

                if not chunk:
                    break # 청크가 비어있으면(더이상 읽을 게 없다면(다 읽었다면)) break

                fw.write(chunk) # 넣기

copy_image_file("i_am_gosu.gif")
copy_image_file("Charlotte.jpg")
copy_image_file("etrgo.png")