import json
from os import write
from wsgiref import headers

import requests

import epub_builder
from downloader import deofuscator_helpers
from downloader import api_requests
from bs4 import BeautifulSoup
from downloader import img_descrambler
from PIL import Image
import cv2
import numpy as np
from downloader import deofuscator


session = requests.Session()
# url = 'https://www.amazon.co.jp/%E3%83%8A%E3%83%9F%E3%83%A4%E9%9B%91%E8%B2%A8%E5%BA%97%E3%81%AE%E5%A5%87%E8%B9%9F-%E8%A7%92%E5%B7%9D%E6%96%87%E5%BA%AB-%E6%9D%B1%E9%87%8E-%E5%9C%AD%E5%90%BE-ebook/dp/B086YT8NR6/ref=zg-te-pba_d_sccl_1_1/357-4252653-3830120?pd_rd_w=XRZh1&content-id=amzn1.sym.46270640-5101-4065-bf32-09e335aceee7&pf_rd_p=46270640-5101-4065-bf32-09e335aceee7&pf_rd_r=6TJPFKF6PCDTD62PC4TK&pd_rd_wg=9ka0Q&pd_rd_r=ba9cf061-6f87-4f20-9e05-b548767ff2ae&pd_rd_i=B086YT8NR6&psc=1'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
#     'From': 'youremail@domain.example'  # This is another valid field
# }
# print(requests.get(url, headers=headers).content)
username = 'test@test.com'
password = 'test'

bookId = '505068'
volumeId = '001'


cid = f'{bookId}_{volumeId}'
api_requests.login(session, username, password)\

content_info_json = api_requests.get_content_info(session, cid)
arrays = [deofuscator_helpers.get_array(content_info_json['items'][0]['stbl'], content_info_json['items'][0]['seed']),
         deofuscator_helpers.get_array(content_info_json['items'][0]['ttbl'], content_info_json['items'][0]['seed'])]

content = api_requests.get_content(session, cid,
                              content_info_json['items'][0]['p'],
                              content_info_json['ShopUserID'],
                              content_info_json['items'][0]['ContentDate'])

content = json.loads(content)
with open('arifureta.html', 'w', encoding='utf-8') as file:
    soup = BeautifulSoup(content['ttx'], 'html.parser')
    file.write(soup.prettify())


content = deofuscator.process_html(content['ttx'], content_info_json)

epub_builder.construct_epub(session, content, content_info_json)

epub_builder.compress_epub(content_info_json)