const cav = document.getElementById('cav')
const ctx = cav.getContext('2d')

var img = document.getElementById('img')
cav.width = img.width
cav.height = img.height

ctx.drawImage(img, 0,0)
var imgdata = ctx.getImageData(0,0,img.width,img.height)
console.log(imgdata)