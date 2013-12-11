

from PIL import Image
from StringIO import StringIO


from SHM.settings import MEDIA_ROOT
def change_img_size(ori_file):
    f = StringIO(ori_file.read())
    name = MEDIA_ROOT + '/' + 'big_img/mid_' + ori_file.name
    img = Image.open(f)
    if img.size[0] >  img.size[1]:  
        offset = 131  
        img = img.transform((img.size[1],img.size[1]), Image.EXTENT,(0,0,int(img.size[1]),img.size[1]))  
    else:  
        offset = 131 
        img = img.transform((img.size[0],img.size[0]), Image.EXTENT,(0,0,img.size[0],img.size[0]))
    img.save(name)
    server_path = 'big_img/mid_' + ori_file.name
    return server_path, server_path
