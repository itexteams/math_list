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


def bt_dang11_p1_b2_c2_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            lis1=[28,30,32]
            lis2=[22,24,26]
            dai=random.choice(lis1)
            rong=random.choice(lis2)
            cao=random.choice(lis2)
            nua_rong=Rational(rong,2)
            nua_cao=Rational(cao,2)

            tien=randint(40,50)

            xo=Rational(dai,2)
            yo=nua_rong
            zo=0

            xb=dai
            yb=0
            zb=cao

            xn=0
            yn=nua_rong
            zn=0

            xm=dai
            ym=rong
            zm=nua_cao

            x0=(yb-yo)*(zn-zm)-(yn-ym)*(zb-zo)
            y0=-(xb-xo)*(zn-zm)+(xn-xm)*(zb-zo)
            z0=(xb-xo)*(yn-ym)-(xn-xm)*(yb-yo)
            do_dai=sqrt(x0**2+y0**2+z0**2)

            tu=abs(x0*(xn-xo)+y0*(yn-yo)+z0*(zn-zo))

            ij=tu/do_dai

            tong=ij*tien
            h1=tong    
            number = Decimal(float(h1))  # Số cần làm tròn
            kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)


            if dang=='1':

                du = ['$%s$ triệu' %(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$ triệu' %(latex(kq+1)),
                    '$%s$ triệu' %(latex(kq+2)),
                    '$%s$ triệu' %(latex(kq+3)),
                    '$%s$ triệu' %(latex(kq-1)),
                    '$%s$ triệu' %(latex(kq-2)),
                    '$%s$ triệu' %(latex(kq-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''\\immini{
                                Một thành phố muốn xây dựng một tòa nhà biểu tượng điểm nhấn của thành phố. Trên bàn thiết kế tòa nhà có hình dạng là một khối hộp chữ nhật, có chiều dài $%s$ m, chiều rộng $%s$ m và chiều cao $%s$ m. Lãnh đạo thành phố muốn xây dựng một cây cầu $IJ$ với một đầu cây cầu là điểm $I$ thuộc đường thẳng $a$ ($O$ là tâm của sàn tòa nhà), dầu còn lại của cây cầu là điểm $J$ thuộc đường thẳng $b$ (tham khảo hình vẽ minh hoạ). Chi phí xây dựng cây cầu có đơn giá $%s$ triệu đồng trên một mét dài. Vì vậy để đáp ứng bài toán kinh tế, nhà thiết kế phải chọn vị trí hai điểm $I, J$ sao cho độ dài cây cầu $IJ$ là ngắn nhất. Khi đó chi phí xây dựng cây cầu (làm tròn đến hàng đơn vị) là
                                }{\\scalebox{0.6}{ 
                                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-1.335604570852475,-0.9462243340801404) rectangle (7.020848769919218,5.488624002459635);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (1.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (6.,1.);
                    \\draw [line width=1.pt] (6.,1.)-- (5.,0.);
                    \\draw [line width=1.pt] (5.,0.)-- (0.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (1.,5.);
                    \\draw [line width=1.pt] (0.,0.)-- (0.,4.);
                    \\draw [line width=1.pt] (0.,4.)-- (1.,5.);
                    \\draw [line width=1.pt] (1.,5.)-- (6.,5.);
                    \\draw [line width=1.pt] (6.,5.)-- (5.,4.);
                    \\draw [line width=1.pt] (5.,4.)-- (0.,4.);
                    \\draw [line width=1.pt] (5.,4.)-- (5.,0.);
                    \\draw [line width=1.pt] (6.,5.)-- (6.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (5.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,4.)-- (3.,0.5);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.5,1.)-- (5.,2.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.6375998251464234,2.089466870662506)-- (4.085007451675388,1.3900049677835922);
                    \\draw (2.773090339511822,0.5) node[anchor=north west] {$O$};
                    \\draw (1.2,2.264878765096879) node[anchor=north west] {$I$};
                    \\draw (3.923524914413825,1.974109586824944) node[anchor=north west] {$J$};
                    \\draw (11.52144996404134,3.9336410056140703) node[anchor=north west] {$A$};
                    \\draw (12.58338957164319,3.1624705762841563) node[anchor=north west] {$B$};
                    \\draw (12.279978255185519,3.630229689156399) node[anchor=north west] {$C$};
                    \\draw (12.178841149699627,4.237052322071741) node[anchor=north west] {$D$};
                    \\draw (11.837503418684747,6.537921471875747) node[anchor=north west] {$A'$};
                    \\draw (12.178841149699627,4.679527158572512) node[anchor=north west] {$B'$};
                    \\draw (12.039777629656529,5.210496962373436) node[anchor=north west] {$C'$};
                    \\draw (11.812219142313275,5.74146676617436) node[anchor=north west] {$D'$};
                    \\draw [->,line width=1.pt] (-0.21045427232194458,2.1258152450537797) -- (-0.21045427232194458,3.984209558357015);
                    \\draw [->,line width=1.pt] (-0.21045427232194458,2.1258152450537797) -- (-0.21045427232194458,0.0019360298500816775);
                    \\draw [->,line width=1.pt] (2.128341292039271,-0.20033818112169885) -- (4.934895969272729,-0.14976962837875368);
                    \\draw [->,line width=1.pt] (2.128341292039271,-0.20033818112169885) -- (-0.03346433772163637,-0.16241176656448997);
                    \\draw [->,line width=1.pt] (5.592287154931016,0.3179894844934893) -- (6.123256958731941,0.9121699792230953);
                    \\draw [->,line width=1.pt] (5.592287154931016,0.3179894844934893) -- (5.2383072857304,-0.06127466107859958);
                    \\draw [->,line width=1.pt] (5.187738732987455,3.2383234053985737) -- (5.200380871173191,3.920998867428334);
                    \\draw [->,line width=1.pt] (5.187738732987455,3.2383234053985737) -- (5.187738732987455,2.0752466923108344);
                    \\draw [->,line width=1.pt] (2.229478397525161,1.152370604752085) -- (3.4810500779130544,1.1270863283806123);
                    \\draw [->,line width=1.pt] (2.229478397525161,1.152370604752085) -- (1.0411174080659489,1.152370604752085);
                    \\draw (12.368473222485672,2.593574357926023) node[anchor=north west] {$M$};
                    \\draw (12.393757498857145,1.88561461952479) node[anchor=north west] {$N$};
                    \\draw (-1.2,2.479795114254396) node[anchor=north west] {$%s$ m};
                    \\draw (2.065130601110589,-0.14976962837875368) node[anchor=north west] {$%s$ m};
                    \\draw (5.832487780460006,0.7351800446227871) node[anchor=north west] {$%s$ m};
                    \\draw (1.2,1.708624684924482) node[anchor=north west] {$%s$ m};
                    \\draw (5.1,3.3394605108844644) node[anchor=north west] {$%s$ m};
                    \\draw (0.573358295193706,3.845146038313916) node[anchor=north west] {$a$};
                    \\draw (4.479778994586222,1.835046066781845) node[anchor=north west] {$b$};
            \\end{tikzpicture} }}'''
                                %(latex(dai),latex(rong),latex(cao),latex(tien),
                                latex(cao),latex(rong),latex(dai),latex(nua_rong),latex(nua_cao)

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Gắn hệ trục tọa độ như hình vẽ \\\\
                        \\begin{center}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-1.5252366436385196,-1.1990670977948663) rectangle (7.374828639119834,6.133373049932186);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (1.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (6.,1.);
                    \\draw [line width=1.pt] (6.,1.)-- (5.,0.);
                    \\draw [line width=1.pt] (5.,0.)-- (0.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (1.,5.);
                    \\draw [line width=1.pt] (0.,0.)-- (0.,4.);
                    \\draw [line width=1.pt] (0.,4.)-- (1.,5.);
                    \\draw [line width=1.pt] (1.,5.)-- (6.,5.);
                    \\draw [line width=1.pt] (6.,5.)-- (5.,4.);
                    \\draw [line width=1.pt] (5.,4.)-- (0.,4.);
                    \\draw [line width=1.pt] (5.,4.)-- (5.,0.);
                    \\draw [line width=1.pt] (6.,5.)-- (6.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (5.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,4.)-- (3.,0.5);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.5,1.)-- (5.,2.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.6375998251464234,2.089466870662506)-- (4.085007451675388,1.3900049677835922);
                    \\draw (2.773090339511822,0.5) node[anchor=north west] {$O$};
                    \\draw (1.1,2.264878765096879) node[anchor=north west] {$I$};
                    \\draw (3.923524914413825,1.974109586824944) node[anchor=north west] {$J$};
                    \\draw (0.5,1.4178555066525471) node[anchor=north west] {$A$};
                    \\draw (-0.75,0.2674209317505441) node[anchor=north west] {$B$};
                    \\draw (4.960180245644201,0.03986244440729078) node[anchor=north west] {$C$};
                    \\draw (6.085330544174732,1.5948454412528552) node[anchor=north west] {$D$};
                    \\draw (0.3,5.475981864273899) node[anchor=north west] {$A'$};
                    \\draw (-0.3495177923650439,4.591032191272357) node[anchor=north west] {$B'$};
                    \\draw (4.732621758300948,4.628958605829567) node[anchor=north west] {$C'$};
                    \\draw (5.95890916231737,5.678256075245679) node[anchor=north west] {$D'$};
                    \\draw [->,line width=1.pt] (-0.21045427232194458,2.1258152450537797) -- (-0.21045427232194458,3.984209558357015);
                    \\draw [->,line width=1.pt] (-0.21045427232194458,2.1258152450537797) -- (-0.21045427232194458,0.0019360298500816775);
                    \\draw [->,line width=1.pt] (2.128341292039271,-0.20033818112169885) -- (4.934895969272729,-0.14976962837875368);
                    \\draw [->,line width=1.pt] (2.128341292039271,-0.20033818112169885) -- (-0.03346433772163637,-0.16241176656448997);
                    \\draw [->,line width=1.pt] (5.592287154931016,0.3179894844934893) -- (6.123256958731941,0.9121699792230953);
                    \\draw [->,line width=1.pt] (5.592287154931016,0.3179894844934893) -- (5.2383072857304,-0.06127466107859958);
                    \\draw [->,line width=1.pt] (5.187738732987455,3.2383234053985737) -- (5.200380871173191,3.920998867428334);
                    \\draw [->,line width=1.pt] (5.187738732987455,3.2383234053985737) -- (5.187738732987455,2.0752466923108344);
                    \\draw [->,line width=1.pt] (2.229478397525161,1.152370604752085) -- (3.4810500779130544,1.1270863283806123);
                    \\draw [->,line width=1.pt] (2.229478397525161,1.152370604752085) -- (1.0411174080659489,1.152370604752085);
                    \\draw (5.010748798387147,2.264878765096879) node[anchor=north west] {$M$};
                    \\draw (3.2408494523840647,1.1650127429378212) node[anchor=north west] {$N$};
                    \\draw (-1.28503601810953,2.479795114254396) node[anchor=north west] {$%s$ m};
                    \\draw (2.065130601110589,-0.14976962837875368) node[anchor=north west] {$%s$ m};
                    \\draw (5.832487780460006,0.7351800446227871) node[anchor=north west] {$%s$ m};
                    \\draw (1.2307494808519934,1.708624684924482) node[anchor=north west] {$%s$ m};
                    \\draw (5.187738732987455,3.3394605108844644) node[anchor=north west] {$%s$ m};
                    \\draw (0.573358295193706,3.845146038313916) node[anchor=north west] {$a$};
                    \\draw (4.479778994586222,1.835046066781845) node[anchor=north west] {$b$};
                    \\draw [->,line width=1.pt] (1.,5.) -- (0.9905488553230037,5.766751042545833);
                    \\draw [->,line width=1.pt] (6.,1.) -- (7.046133046290691,0.988022808337513);
                    \\draw [->,line width=1.pt] (0.,0.) -- (-0.5517920033368247,-0.5543180503223152);
                    \\draw (-0.8804875961659684,-0.13712749019301737) node[anchor=north west] {$x$};
                    \\draw (6.7553638680187555,1.6074875794385917) node[anchor=north west] {$y$};
                    \\draw (1.0664016844374216,5.893172424403196) node[anchor=north west] {$z$};
                \\end{tikzpicture}
            \\end{center}
                        Tọa độ các điểm $O(%s;%s;%s), B'(%s;%s;%s), N(%s;%s;%s), M(%s;%s;%s)$. \\\\
                        Các vectơ $\\vec{OB'}=(%s;%s;%s), \\vec{MN}=(%s;%s;%s)$. \\\\
                        Độ dài ngắn nhất của cây cầu $IJ$ tương ứng là khoảng cách giữa hai đường thẳng $a$ và $b$. \\\\ 
                        Ta có \\\\
                        $\\vec{ON}=(%s;%s;%s)$. \\\\
                        $\\left[\\vec{OB'}, \\vec{MN} \\right]=(%s;%s;%s)$ suy ra $\\left| \\left[\\vec{OB'}, \\vec{MN} \\right] \\right|=%s$. \\\\
                        Do đó $IJ=\\dfrac{\\left| \\left[\\vec{OB'}, \\vec{MN} \\right] \\cdot \\vec{ON} \\right|}{\\left| \\left[\\vec{OB'}, \\vec{MN} \\right] \\right|}=\\dfrac{%s}{%s}=%s$. \\\\
                        Vậy chi phí xây dựng cây cầu là $%s \\cdot %s =%s$ triệu đồng.'''
                        %(latex(cao),latex(rong),latex(dai),latex(nua_rong),latex(nua_cao),
                        latex(xo),latex(yo),latex(zo),
                        latex(xb),latex(yb),latex(zb),
                        latex(xn),latex(yn),latex(zn),
                        latex(xm),latex(ym),latex(zm),
                        latex(xb-xo),latex(yb-yo),latex(zb-zo),
                        latex(xn-xm),latex(yn-ym),latex(zn-zm),
                        latex(xn-xo),latex(yn-yo),latex(zn-zo),
                        latex(x0),latex(y0),latex(z0),latex(do_dai),
                        latex(tu),latex(do_dai),latex(ij),
                        latex(ij),latex(tien),latex(kq)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

