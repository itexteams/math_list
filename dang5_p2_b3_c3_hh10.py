import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang5_p2_b3_c3_hh10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                a=randint(1,5) 
                b=randint(-5,-1) 
                r=randint(2,9)

                xa=randint(-5,5) 
                ya=randint(-5,5) 

                xia=xa-a
                yia=ya-b
                while sqrt(xia**2+yia**2)<=r:
                    a=randint(1,5) 
                    b=randint(-5,-1) 
                    r=randint(2,9)

                    xa=randint(-5,5) 
                    ya=randint(-5,5) 

                    xia=xa-a
                    yia=ya-b
                ia=sqrt(xia**2+yia**2)

                xb=randint(-5,5) 
                yb=randint(-5,5) 
                xib=xb-a
                yib=yb-b
                while sqrt(xib**2+yib**2)<=r:
                    xb=randint(-5,5) 
                    yb=randint(-5,5) 
                    xib=xb-a
                    yib=yb-b
                ib=sqrt(xib**2+yib**2)
                d=ib-r
                h1=d   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Hình vẽ bên mô phỏng một trạm thu phát sóng điện thoại di động đặt ở vị trí $I$ có tọa độ $(%s;%s)$ trong mặt phẳng tọa độ (đơn vị trên hai trục là ki-lô-mét), trạm thu phát sóng đó được thiết kế với bán kinh phủ sóng là $%s$ kmzz}
                                {\\definecolor{ffqqqq}{rgb}{1zz,0zz,0zz}
                \\definecolor{qqwuqq}{rgb}{0zz,0zz39215686274509803,0zz}
                \\definecolor{zzttqq}{rgb}{0zz6,0zz2,0zz}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                \\clip(-0zz39226459637762473,0zz020091550108097413) rectangle (3zz381033322435105,5zz53886061503824);
                \\fill[line width=1zzpt,color=zzttqq,fill=zzttqq,fill opacity=0zz49000000953674316] (0zz8374247001591985,0zz5217860933384039) hh (2zz1493330055545115,0zz5151935892911912) hh (2zz1460477602761103,0zz4195032198997574) hh (0zz8323070999695319,0zz41456434523695074) hh cycle;
                \\fill[line width=1zzpt,color=qqwuqq,fill=qqwuqq,fill opacity=0zz5] (1zz083410160511483,3zz1388739079463996) hh (1zz203576239401387,3zz137538729292068) hh (1zz2053405992446238,2zz5484005992669303) hh (1zz0778652447841697,2zz551112840851195) hh cycle;
                \\fill[line width=1zzpt,color=qqwuqq,fill=qqwuqq,fill opacity=0zz44999998807907104] (1zz787423769296626,3zz1476506165578066) hh (1zz9243890458206623,3zz1462671289161483) hh (1zz9225496929633998,2zz5466380974485396) hh (1zz794902006512873,2zz547836998399678) hh cycle;
                \\draw [line width=1zzpt,color=zzttqq] (0zz8374247001591985,0zz5217860933384039)hh (2zz1493330055545115,0zz5151935892911912);
                \\draw [line width=1zzpt,color=zzttqq] (2zz1493330055545115,0zz5151935892911912)hh (2zz1460477602761103,0zz4195032198997574);
                \\draw [line width=1zzpt,color=zzttqq] (2zz1460477602761103,0zz4195032198997574)hh (0zz8323070999695319,0zz41456434523695074);
                \\draw [line width=1zzpt,color=zzttqq] (0zz8323070999695319,0zz41456434523695074)hh (0zz8374247001591985,0zz5217860933384039);
                \\draw [line width=1zzpt] (0zz5560968708755173,0zz40431984388817843)hh (2zz4032359947652173,0zz40431984388817843);
                \\draw [line width=1zzpt] (1zz503374043936915,3zz5978789203068167)hh (1zz4948377440279876,3zz426098023230701);
                \\draw [line width=1zzpt] (1zz4948377440279876,3zz426098023230701)hh (1zz556467887195877,3zz426098023230701);
                \\draw [line width=1zzpt] (1zz4948377440279876,3zz426098023230701)hh (1zz433207600860098,3zz429949907178694);
                \\draw [line width=1zzpt] (1zz433207600860098,3zz429949907178694)hh (0zz9903920949236239,0zz5210174129627032);
                \\draw [line width=1zzpt] (1zz556467887195877,3zz426098023230701)hh (2zz0124902227711927,0zz5158812414659817);
                \\draw [line width=1zzpt] (1zz1024654108080014,0zz520454230470822)hh (1zz2926147413106248,0zz840929471095494);
                \\draw [line width=1zzpt] (1zz2926147413106248,0zz840929471095494)hh (1zz7205908804292263,0zz840929471095494);
                \\draw [line width=1zzpt] (1zz7205908804292263,0zz840929471095494)hh (1zz8972581705822718,0zz5164602970046195);
                \\draw [line width=1zzpt] (1zz9805065743759267,0zz7199926260202867)hh (1zz1055170073539808,1zz277293094759806);
                \\draw [line width=1zzpt] (1zz0228153316118007,0zz7340113246606017)hh (1zz86324959346876,1zz2621123381645927);
                \\draw [line width=1zzpt] (1zz86324959346876,1zz2621123381645927)hh (1zz182308379737286,1zz7817490485521787);
                \\draw [line width=1zzpt] (1zz1055170073539808,1zz277293094759806)hh (1zz7885236009242422,1zz7784010139267137);
                \\draw [line width=1zzpt] (1zz7885236009242422,1zz7784010139267137)hh (1zz2493881008876278,2zz2224074671062266);
                \\draw [line width=1zzpt] (1zz182308379737286,1zz7817490485521787)hh (1zz7460712021950797,2zz216098630344012);
                \\draw [line width=1zzpt] (1zz7460712021950797,2zz216098630344012)hh (1zz3469609177066375,2zz620766748064911);
                \\draw [line width=1zzpt] (1zz2493881008876278,2zz2224074671062266)hh (1zz682430290223319,2zz622238495825316);
                \\draw [line width=1zzpt] (1zz3469609177066375,2zz620766748064911)hh (1zz6341713961429578,2zz930214295398577);
                \\draw [line width=1zzpt] (1zz682430290223319,2zz622238495825316)hh (1zz3833809288361254,2zz928868609023656);
                \\draw [line width=1zzpt] (1zz3833809288361254,2zz928868609023656)hh (1zz581546728778579,3zz1666675689545993);
                \\draw [line width=1zzpt] (1zz6341713961429578,2zz930214295398577)hh (1zz3925524046312217,3zz162878813724546);
                \\draw [line width=1zzpt] (1zz3925524046312217,3zz162878813724546)hh (1zz5022804088015975,3zz303181786692734);
                \\draw [line width=1zzpt] (1zz5022804088015975,3zz303181786692734)hh (1zz581546728778579,3zz1666675689545993);
                \\draw [line width=1zzpt] (1zz3833809288361254,2zz928868609023656)hh (1zz2581549083214236,2zz9374150198160116);
                \\draw [line width=1zzpt] (1zz3353558744643248,2zz6704283452384785)hh (1zz2581549083214236,2zz6704283452384785);
                \\draw [line width=1zzpt] (1zz6341713961429578,2zz930214295398577)hh (1zz7470943605597986,2zz927764899048149);
                \\draw [line width=1zzpt] (1zz674084022000957,2zz675502224267881)hh (1zz682430290223319,2zz622238495825316);
                \\draw [line width=1zzpt] (1zz674084022000957,2zz675502224267881)hh (1zz7543449635163886,2zz678645902579399);
                \\draw [line width=1zzpt] (1zz0834101605114825,3zz1388739079463988)hh (1zz2497576323308808,3zz137025602703961);
                \\draw [line width=1zzpt] (1zz2497576323308808,3zz137025602703961)hh (1zz2516059375733184,2zz5474162303663186);
                \\draw [line width=1zzpt] (1zz2516059375733184,2zz5474162303663186)hh (1zz0778652447841692,2zz5511128408511943);
                \\draw [line width=1zzpt] (1zz0778652447841692,2zz5511128408511943)hh (1zz0834101605114825,3zz1388739079463988);
                \\draw [line width=1zzpt] (1zz2035762394013871,3zz1375387292920665)hh (1zz2053405992446242,2zz548400599266929);
                \\draw [line width=1zzpt] (1zz7414068268193243,3zz1481154341585875)hh (1zz9243890458206623,3zz1462671289161497);
                \\draw [line width=1zzpt] (1zz9243890458206623,3zz1462671289161497)hh (1zz9225407405782247,2zz5437196198814434);
                \\draw [line width=1zzpt] (1zz9225407405782247,2zz5437196198814434)hh (1zz7506483530315131,2zz5492645356087564);
                \\draw [line width=1zzpt] (1zz7506483530315131,2zz5492645356087564)hh (1zz7414068268193243,3zz1481154341585875);
                \\draw [line width=1zzpt] (1zz7876284116231718,3zz1476485494635993)hh (1zz7949020065128736,2zz5478369983996805);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz083410160511483,3zz1388739079463996)hh (1zz203576239401387,3zz137538729292068);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz203576239401387,3zz137538729292068)hh (1zz2053405992446238,2zz5484005992669303);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz2053405992446238,2zz5484005992669303)hh (1zz0778652447841697,2zz551112840851195);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz0778652447841697,2zz551112840851195)hh (1zz083410160511483,3zz1388739079463996);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz787423769296626,3zz1476506165578066)hh (1zz9243890458206623,3zz1462671289161483);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz9243890458206623,3zz1462671289161483)hh (1zz9225496929633998,2zz5466380974485396);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz9225496929633998,2zz5466380974485396)hh (1zz794902006512873,2zz547836998399678);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz794902006512873,2zz547836998399678)hh (1zz787423769296626,3zz1476506165578066);
                \\draw [line width=1zzpt,dashed,color=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (0zz3642210718545354cm);
                \\draw [line width=1zzpt,dashed,color=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (0zz680438268306968cm);
                \\draw [line width=1zzpt,dashed,color=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (1zz0706472277806847cm);
                \\draw [line width=1zzpt,color=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (1zz4774469873354086cm);
                \\begin{scriptsize}
                \\draw [fill=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (2zz5pt);
                \\end{scriptsize}
                \\end{tikzpicture}}'''                 
                                %(latex(a),latex(b),latex(r)
                                    ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True $(x-%s)^2+(y-%s)^2=%s$ là phương trình đường tròn mô tả ranh giới bên ngoài của vùng phủ sóng' %(latex(a),latex(a),latex(r**2))
                nb_da_1_s = '$(x-%s)^2+(y-%s)^2=%s$ là phương trình đường tròn mô tả ranh giới bên ngoài của vùng phủ sóng' %(latex(a),latex(a),latex(r**2+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('''Phương trình đường tròn mô tả ranh giới bên ngoài của vùng phủ sóng là \\\\
                                $(x-%s)^2+(y-%s)^2=%s$zz'''
                            %(latex(a),latex(a),latex(r**2)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Người dùng điện thoại ở vị trí $A(%s;%s)$ sẽ không sử dụng được dịch vụ của trạm này' %(latex(xa),latex(ya))  
                th_da_1_s = 'Người dùng điện thoại ở vị trí $A(%s;%s)$ sẽ sử dụng được dịch vụ của trạm này' %(latex(xa),latex(ya))   
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('''Ta có $\\vec{IA}=(%s;%s)$ suy ra khoảng cách $IA=%s>R$zz \\\\
                                Vậy người dùng điện thoại ở vị trí $A(%s;%s)$ sẽ không sử dụng được dịch vụ của trạm nàyzz'''       
                            %(latex(xia),latex(yia),latex(ia),
                            latex(xa),latex(ya)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Khoảng cách lớn nhất giữa hai điểm trong vùng phủ sóng của trạm thu phát sóng này là $%s$ km' %(latex(2*r))  
                vd_da_1_s = 'Khoảng cách lớn nhất giữa hai điểm trong vùng phủ sóng của trạm thu phát sóng này là $%s$ km' %(latex(2*r+1))  
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('''Khoảng cách lớn nhất giữa hai điểm trong vùng phủ sóng của trạm thu phát sóng này là $%s$ kmzz'''       
                            %(latex(2*r)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Theo đường chim bay, khoảng cách ngắn nhất để một người ở vị trí $B(%s;%s)$ di chuyển được tới vùng phủ sóng là $%s$ km' %(latex(xb),latex(yb),latex(kq))  
                vdc_da_1_s = 'Theo đường chim bay, khoảng cách ngắn nhất để một người ở vị trí $B(%s;%s)$ di chuyển được tới vùng phủ sóng là $%s$ km' %(latex(xb),latex(yb),latex(kq+1)) 
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('''Ta có $\\vec{IB}=(%s;%s)$ suy ra khoảng cách $IB=%s>R$zz \\\\
                                Vậy theo đường chim bay, khoảng cách ngắn nhất để một người ở vị trí $B(%s;%s)$ di chuyển được tới vùng phủ sóng là $d=IB-R=%s-%s=%s \\approx %s$ kmzz'''       
                            %(latex(xib),latex(yib),latex(ib),
                            latex(xb),latex(yb),
                            latex(ib),latex(r),latex(d),latex(kq)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='1':
                a=randint(1,5) 
                b=randint(-5,-1) 
                r=randint(2,9)

                xa=randint(-5,5) 
                ya=randint(-5,5) 

                xia=xa-a
                yia=ya-b
                while sqrt(xia**2+yia**2)>r:
                    a=randint(1,5) 
                    b=randint(-5,-1) 
                    r=randint(2,9)

                    xa=randint(-5,5) 
                    ya=randint(-5,5) 

                    xia=xa-a
                    yia=ya-b
                ia=sqrt(xia**2+yia**2)

                xb=randint(-5,5) 
                yb=randint(-5,5) 
                xib=xb-a
                yib=yb-b
                while sqrt(xib**2+yib**2)<=r:
                    xb=randint(-5,5) 
                    yb=randint(-5,5) 
                    xib=xb-a
                    yib=yb-b
                ib=sqrt(xib**2+yib**2)
                d=ib-r
                h1=d   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Hình vẽ bên mô phỏng một trạm thu phát sóng điện thoại di động đặt ở vị trí $I$ có tọa độ $(%s;%s)$ trong mặt phẳng tọa độ (đơn vị trên hai trục là ki-lô-mét), trạm thu phát sóng đó được thiết kế với bán kinh phủ sóng là $%s$ kmzz}
                                {\\definecolor{ffqqqq}{rgb}{1zz,0zz,0zz}
                \\definecolor{qqwuqq}{rgb}{0zz,0zz39215686274509803,0zz}
                \\definecolor{zzttqq}{rgb}{0zz6,0zz2,0zz}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                \\clip(-0zz39226459637762473,0zz020091550108097413) rectangle (3zz381033322435105,5zz53886061503824);
                \\fill[line width=1zzpt,color=zzttqq,fill=zzttqq,fill opacity=0zz49000000953674316] (0zz8374247001591985,0zz5217860933384039) hh (2zz1493330055545115,0zz5151935892911912) hh (2zz1460477602761103,0zz4195032198997574) hh (0zz8323070999695319,0zz41456434523695074) hh cycle;
                \\fill[line width=1zzpt,color=qqwuqq,fill=qqwuqq,fill opacity=0zz5] (1zz083410160511483,3zz1388739079463996) hh (1zz203576239401387,3zz137538729292068) hh (1zz2053405992446238,2zz5484005992669303) hh (1zz0778652447841697,2zz551112840851195) hh cycle;
                \\fill[line width=1zzpt,color=qqwuqq,fill=qqwuqq,fill opacity=0zz44999998807907104] (1zz787423769296626,3zz1476506165578066) hh (1zz9243890458206623,3zz1462671289161483) hh (1zz9225496929633998,2zz5466380974485396) hh (1zz794902006512873,2zz547836998399678) hh cycle;
                \\draw [line width=1zzpt,color=zzttqq] (0zz8374247001591985,0zz5217860933384039)hh (2zz1493330055545115,0zz5151935892911912);
                \\draw [line width=1zzpt,color=zzttqq] (2zz1493330055545115,0zz5151935892911912)hh (2zz1460477602761103,0zz4195032198997574);
                \\draw [line width=1zzpt,color=zzttqq] (2zz1460477602761103,0zz4195032198997574)hh (0zz8323070999695319,0zz41456434523695074);
                \\draw [line width=1zzpt,color=zzttqq] (0zz8323070999695319,0zz41456434523695074)hh (0zz8374247001591985,0zz5217860933384039);
                \\draw [line width=1zzpt] (0zz5560968708755173,0zz40431984388817843)hh (2zz4032359947652173,0zz40431984388817843);
                \\draw [line width=1zzpt] (1zz503374043936915,3zz5978789203068167)hh (1zz4948377440279876,3zz426098023230701);
                \\draw [line width=1zzpt] (1zz4948377440279876,3zz426098023230701)hh (1zz556467887195877,3zz426098023230701);
                \\draw [line width=1zzpt] (1zz4948377440279876,3zz426098023230701)hh (1zz433207600860098,3zz429949907178694);
                \\draw [line width=1zzpt] (1zz433207600860098,3zz429949907178694)hh (0zz9903920949236239,0zz5210174129627032);
                \\draw [line width=1zzpt] (1zz556467887195877,3zz426098023230701)hh (2zz0124902227711927,0zz5158812414659817);
                \\draw [line width=1zzpt] (1zz1024654108080014,0zz520454230470822)hh (1zz2926147413106248,0zz840929471095494);
                \\draw [line width=1zzpt] (1zz2926147413106248,0zz840929471095494)hh (1zz7205908804292263,0zz840929471095494);
                \\draw [line width=1zzpt] (1zz7205908804292263,0zz840929471095494)hh (1zz8972581705822718,0zz5164602970046195);
                \\draw [line width=1zzpt] (1zz9805065743759267,0zz7199926260202867)hh (1zz1055170073539808,1zz277293094759806);
                \\draw [line width=1zzpt] (1zz0228153316118007,0zz7340113246606017)hh (1zz86324959346876,1zz2621123381645927);
                \\draw [line width=1zzpt] (1zz86324959346876,1zz2621123381645927)hh (1zz182308379737286,1zz7817490485521787);
                \\draw [line width=1zzpt] (1zz1055170073539808,1zz277293094759806)hh (1zz7885236009242422,1zz7784010139267137);
                \\draw [line width=1zzpt] (1zz7885236009242422,1zz7784010139267137)hh (1zz2493881008876278,2zz2224074671062266);
                \\draw [line width=1zzpt] (1zz182308379737286,1zz7817490485521787)hh (1zz7460712021950797,2zz216098630344012);
                \\draw [line width=1zzpt] (1zz7460712021950797,2zz216098630344012)hh (1zz3469609177066375,2zz620766748064911);
                \\draw [line width=1zzpt] (1zz2493881008876278,2zz2224074671062266)hh (1zz682430290223319,2zz622238495825316);
                \\draw [line width=1zzpt] (1zz3469609177066375,2zz620766748064911)hh (1zz6341713961429578,2zz930214295398577);
                \\draw [line width=1zzpt] (1zz682430290223319,2zz622238495825316)hh (1zz3833809288361254,2zz928868609023656);
                \\draw [line width=1zzpt] (1zz3833809288361254,2zz928868609023656)hh (1zz581546728778579,3zz1666675689545993);
                \\draw [line width=1zzpt] (1zz6341713961429578,2zz930214295398577)hh (1zz3925524046312217,3zz162878813724546);
                \\draw [line width=1zzpt] (1zz3925524046312217,3zz162878813724546)hh (1zz5022804088015975,3zz303181786692734);
                \\draw [line width=1zzpt] (1zz5022804088015975,3zz303181786692734)hh (1zz581546728778579,3zz1666675689545993);
                \\draw [line width=1zzpt] (1zz3833809288361254,2zz928868609023656)hh (1zz2581549083214236,2zz9374150198160116);
                \\draw [line width=1zzpt] (1zz3353558744643248,2zz6704283452384785)hh (1zz2581549083214236,2zz6704283452384785);
                \\draw [line width=1zzpt] (1zz6341713961429578,2zz930214295398577)hh (1zz7470943605597986,2zz927764899048149);
                \\draw [line width=1zzpt] (1zz674084022000957,2zz675502224267881)hh (1zz682430290223319,2zz622238495825316);
                \\draw [line width=1zzpt] (1zz674084022000957,2zz675502224267881)hh (1zz7543449635163886,2zz678645902579399);
                \\draw [line width=1zzpt] (1zz0834101605114825,3zz1388739079463988)hh (1zz2497576323308808,3zz137025602703961);
                \\draw [line width=1zzpt] (1zz2497576323308808,3zz137025602703961)hh (1zz2516059375733184,2zz5474162303663186);
                \\draw [line width=1zzpt] (1zz2516059375733184,2zz5474162303663186)hh (1zz0778652447841692,2zz5511128408511943);
                \\draw [line width=1zzpt] (1zz0778652447841692,2zz5511128408511943)hh (1zz0834101605114825,3zz1388739079463988);
                \\draw [line width=1zzpt] (1zz2035762394013871,3zz1375387292920665)hh (1zz2053405992446242,2zz548400599266929);
                \\draw [line width=1zzpt] (1zz7414068268193243,3zz1481154341585875)hh (1zz9243890458206623,3zz1462671289161497);
                \\draw [line width=1zzpt] (1zz9243890458206623,3zz1462671289161497)hh (1zz9225407405782247,2zz5437196198814434);
                \\draw [line width=1zzpt] (1zz9225407405782247,2zz5437196198814434)hh (1zz7506483530315131,2zz5492645356087564);
                \\draw [line width=1zzpt] (1zz7506483530315131,2zz5492645356087564)hh (1zz7414068268193243,3zz1481154341585875);
                \\draw [line width=1zzpt] (1zz7876284116231718,3zz1476485494635993)hh (1zz7949020065128736,2zz5478369983996805);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz083410160511483,3zz1388739079463996)hh (1zz203576239401387,3zz137538729292068);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz203576239401387,3zz137538729292068)hh (1zz2053405992446238,2zz5484005992669303);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz2053405992446238,2zz5484005992669303)hh (1zz0778652447841697,2zz551112840851195);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz0778652447841697,2zz551112840851195)hh (1zz083410160511483,3zz1388739079463996);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz787423769296626,3zz1476506165578066)hh (1zz9243890458206623,3zz1462671289161483);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz9243890458206623,3zz1462671289161483)hh (1zz9225496929633998,2zz5466380974485396);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz9225496929633998,2zz5466380974485396)hh (1zz794902006512873,2zz547836998399678);
                \\draw [line width=1zzpt,color=qqwuqq] (1zz794902006512873,2zz547836998399678)hh (1zz787423769296626,3zz1476506165578066);
                \\draw [line width=1zzpt,dashed,color=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (0zz3642210718545354cm);
                \\draw [line width=1zzpt,dashed,color=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (0zz680438268306968cm);
                \\draw [line width=1zzpt,dashed,color=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (1zz0706472277806847cm);
                \\draw [line width=1zzpt,color=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (1zz4774469873354086cm);
                \\begin{scriptsize}
                \\draw [fill=ffqqqq] (1zz503374043936915,3zz5978789203068167) circle (2zz5pt);
                \\end{scriptsize}
                \\end{tikzpicture}}'''                 
                                %(latex(a),latex(b),latex(r)
                                    ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True $(x-%s)^2+(y-%s)^2=%s$ là phương trình đường tròn mô tả ranh giới bên ngoài của vùng phủ sóng' %(latex(a),latex(a),latex(r**2))
                nb_da_1_s = '$(x-%s)^2+(y-%s)^2=%s$ là phương trình đường tròn mô tả ranh giới bên ngoài của vùng phủ sóng' %(latex(a),latex(a),latex(r**2+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('''Phương trình đường tròn mô tả ranh giới bên ngoài của vùng phủ sóng là \\\\
                                $(x-%s)^2+(y-%s)^2=%s$zz'''
                            %(latex(a),latex(a),latex(r**2)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Người dùng điện thoại ở vị trí $A(%s;%s)$ sẽ sử dụng được dịch vụ của trạm này' %(latex(xa),latex(ya))  
                th_da_1_s = 'Người dùng điện thoại ở vị trí $A(%s;%s)$ sẽ không sử dụng được dịch vụ của trạm này' %(latex(xa),latex(ya))   
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('''Ta có $\\vec{IA}=(%s;%s)$ suy ra khoảng cách $IA=%s<R$zz \\\\
                                Vậy người dùng điện thoại ở vị trí $A(%s;%s)$ sẽ sử dụng được dịch vụ của trạm nàyzz'''       
                            %(latex(xia),latex(yia),latex(ia),
                            latex(xa),latex(ya)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Khoảng cách lớn nhất giữa hai điểm trong vùng phủ sóng của trạm thu phát sóng này là $%s$ km' %(latex(2*r))  
                vd_da_1_s = 'Khoảng cách lớn nhất giữa hai điểm trong vùng phủ sóng của trạm thu phát sóng này là $%s$ km' %(latex(2*r+1))  
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('''Khoảng cách lớn nhất giữa hai điểm trong vùng phủ sóng của trạm thu phát sóng này là $%s$ kmzz'''       
                            %(latex(2*r)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Theo đường chim bay, khoảng cách ngắn nhất để một người ở vị trí $B(%s;%s)$ di chuyển được tới vùng phủ sóng là $%s$ km' %(latex(xb),latex(yb),latex(kq))  
                vdc_da_1_s = 'Theo đường chim bay, khoảng cách ngắn nhất để một người ở vị trí $B(%s;%s)$ di chuyển được tới vùng phủ sóng là $%s$ km' %(latex(xb),latex(yb),latex(kq+1)) 
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('''Ta có $\\vec{IB}=(%s;%s)$ suy ra khoảng cách $IB=%s>R$zz \\\\
                                Vậy theo đường chim bay, khoảng cách ngắn nhất để một người ở vị trí $B(%s;%s)$ di chuyển được tới vùng phủ sóng là $d=IB-R=%s-%s=%s \\approx %s$ kmzz'''       
                            %(latex(xib),latex(yib),latex(ib),
                            latex(xb),latex(yb),
                            latex(ib),latex(r),latex(d),latex(kq)
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('--', '+').replace('1x', 'x').replace('1y', 'y').replace('.', ',').replace('zz', '.').replace('hh', '--')
            return content   

