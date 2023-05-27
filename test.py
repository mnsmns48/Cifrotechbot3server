import yadisk
from config import hidden_vars as hv

y = yadisk.YaDisk(token=hv.yatoken)

print(y.get_download_link('/Photo/18315.jpg'))