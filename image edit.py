pip install pillow
from PIL import Image
modiji = Image.open(r'C:\Users\ayush\Downloads\modiji.jpg')
modiji.size
king = Image.open(r"C:\Users\ayush\Downloads\king.jpg")
king.size
king = king.crop((0,0,1200,900))
king.size
king = king.rotate(180)
modiji.putalpha(250)
modiji
king = king.resize((1200,450))
king
modiji.paste(im=king,box=(0,450))
modiji
