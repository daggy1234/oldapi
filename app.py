from flask import Flask, render_template,request,send_file
from io import BytesIO
from PIL import Image
app = Flask(__name__)
import requests
def getimg(url):
    r = requests.get(url)
    if r.status_code == 200:
        # imgf = await aiofiles.open(f'avatar{name}.png', mode='wb')
        byt = r.content
        return (byt)
        # await imgf.close()
    else:
        return False
    del r

def getpixel(image: BytesIO):
    with Image.open(BytesIO(image)) as t:
        imgSmall = t.resize((32, 32), resample=Image.BILINEAR)
        # imgSmall = t.resize((256, 256))
        fim = imgSmall.resize(t.size, Image.NEAREST)
        retimg = BytesIO()
        fim.save(retimg, 'png')

    retimg.seek(0)
    return (retimg)
@app.route('/api/')
def index():
    return render_template("index.html")
@app.route('/api/test')
def fact():
    dict = {'success':True,'message':'yes this api works thank you very much'}
    return (dict)

@app.route('/api/pixelate',methods=['POST'])
def pixelate():
    if request.method == 'POST':
        url = request.headers.get('url')
        byt = getimg(url)
        if byt == False:
            return ('Error')
        else:
            img = getpixel(byt)
            return send_file(img,attachment_filename='pixeltest.png')
    else:
        url = 'https://images-ext-2.discordapp.net/external/zQAm-hCAKz262DbTQKg22uB1hJhdV51qEKktvjf8iTk/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/477034228366966785/24144b6e82274a0de160ec20aef2ed3f.webp?width=671&height=671'
        byt = getimg(url)
        if byt == False:
            return ('Error')
        else:
            img = getpixel(byt)
            return send_file(img)
@app.route('/api/testpixel')
def testpixelate():
    url = 'https://images-ext-2.discordapp.net/external/zQAm-hCAKz262DbTQKg22uB1hJhdV51qEKktvjf8iTk/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/477034228366966785/24144b6e82274a0de160ec20aef2ed3f.webp?width=671&height=671'
    byt = getimg(url)
    if byt == False:
        return ('Error')
    else:
        img = getpixel(byt)
        return send_file(img,mimetype='BytesIO')
if __name__ == '__main__':
    app.debug = True
    app.run()