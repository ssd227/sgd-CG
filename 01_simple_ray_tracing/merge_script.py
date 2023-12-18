from PIL import Image
r = Image.open('./pic/1.JPG')
g = Image.open('./pic/2.JPG')
b = Image.open('./pic/3.JPG')

# r.show()
# g.show()
# b.show()

im = Image.merge("RGB", (r, g, b))
im.show()
im.save("./pic/result_01.JPG", "JPEG")

list = [r, g, b]

for i in range(3):
    for j in range(3):
        for k in range(3):
            im = Image.merge("RGB", (list[i], list[j], list[k]))
            im.save("./pic/result/"+str(i)+str(j)+str(k)+'.jpg', "JPEG")
