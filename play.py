import io
import base64
from IPython.display import HTML

def play():
    video = io.open('img/gd.mp4', 'r+b').read()
    encoded = base64.b64encode(video)
    return HTML(data='''<video alt="test" controls>
                        <source src="data:video/mp4;base64,{0}" type="video/mp4" />
                                     </video>'''.format(encoded.decode('ascii')))

if __name__=='__main__':
    play()
