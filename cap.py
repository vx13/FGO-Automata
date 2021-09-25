import uiautomator2 as u2
d = u2.connect()

img = d.screenshot()
x, y = img.size
if x/y > 1920/1080:
    edge = ((x-y*1920/1080)/2, 0)
else:
    edge = (0, (y-x*1080/1920)/2)
    
print(edge)
out = img.crop((edge[0], edge[1], x-edge[0], y-edge[1]))
out = out.resize((1920, 1080))
out.save('scr.png')