from django.shortcuts import render

def index(req):
    return render(req, 'index.html')

def chocolate(req,id):
    id = int(id)
    name = ['snickers','mars','nuts','kitkat','milka']
    img = ['img/0.jpg','img/1.jpg','img/2.jpg','img/3.jpg','img/4.jpg']
    text = ['ne tormozi','PROSTO KOSMOS','PROSTRO NUTS','EST PERERIV - EST KITKAT','MY-MY-MY KOROVKA']
    data={'id':id,'k1':name,'k2':img,'k3':text}
    return render (req,'prochokolad.html', context=data)