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


def bt_dang10_p4_b2_c4_ds10(self):
            #Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lis=[20,30,40,50,60,70,80,90,100,110,120,130,140,150]
                k=random.choice(lis)
                a=Rational(4*k,5)
                b=4*k
                c=k
                kq=Rational(a,(b/2)**2)*c**2


                du = ['$%s$ (m)'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$ (m)'%(latex(kq+1)),
                    '$%s$ (m)'%(latex(kq+2)),
                    '$%s$ (m)'%(latex(kq+3)),
                    '$%s$ (m)'%(latex(kq-1)),
                    '$%s$ (m)'%(latex(kq-2)),
                    '$%s$ (m)'%(latex(kq-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Một cây cầu treo có trọng lượng phân bố đều dọc theo chiều dài của nó. Cây cầu có trụ tháp đôi cao $%s$ m so với mặt của cây cầu và cách nhau $%s$ m. Các dây cáp có hình dạng đường parabol và được treo trên các đỉnh tháp. Các dây cáp chạm mặt cầu ở tâm của cây cầu. Gắn hệ trục tọa độ $(Oxy)$ như hình vẽ, tìm chiều cao của dây cáp tại điểm cách tâm của cây cầu $%s$ m (giả sử mặt của cây cầu là bằng phẳng).'
                                '}{'
                                '''  \\definecolor{ffxfqq}{rgb}{1.,0.4980392156862745,0.}
            \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
            \\definecolor{yqyqyq}{rgb}{0.5019607843137255,0.5019607843137255,0.5019607843137255}
            \\definecolor{zzttqq}{rgb}{0.6,0.2,0.}
            \\scalebox{0.6}{ 
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-5.2,-1.3729197327653766) rectangle (5.133065927384022,3.546164645082257);
                    \\fill[line width=1.pt ,color=zzttqq,fill=zzttqq,fill opacity=0.5] (-4.,0.) -- (-4.003597579827198,0.21108145653122887) -- (3.996505592390584,0.17903831965986255) -- (4.,0.) -- cycle;
                    \\fill[line width=1.pt ,color=zzttqq,fill=zzttqq,fill opacity=0.5] (-4.,3.) -- (-4.,-0.4) -- (-4.2,-0.4) -- (-4.2,3.) -- cycle;
                    \\fill[line width=1.pt ,color=zzttqq,fill=zzttqq,fill opacity=0.5] (4.,3.) -- (4.,-0.4) -- (4.2,-0.4) -- (4.2,3.) -- cycle;
                    \\fill[line width=1.pt ,color=yqyqyq,fill=yqyqyq,fill opacity=0.5] (3.8,-0.4) -- (4.4,-0.4) -- (4.4,-0.6) -- (3.8,-0.6) -- cycle;
                    \\fill[line width=1.pt ,color=yqyqyq,fill=yqyqyq,fill opacity=0.5] (-4.4,-0.4) -- (-3.8,-0.4) -- (-3.8,-0.6) -- (-4.4,-0.6) -- cycle;
                    \\draw [line width=1.pt ,color=zzttqq] (-4.,0.)-- (-4.003597579827198,0.21108145653122887);
                    \\draw [line width=1.pt ,color=zzttqq] (-4.003597579827198,0.21108145653122887)-- (3.996505592390584,0.17903831965986255);
                    \\draw [line width=1.pt ,color=zzttqq] (3.996505592390584,0.17903831965986255)-- (4.,0.);
                    \\draw [line width=1.pt ,color=zzttqq] (4.,0.)-- (-4.,0.);
                    \\draw [line width=1.pt ,color=zzttqq] (-4.,3.)-- (-4.,-0.4);
                    \\draw [line width=1.pt ,color=zzttqq] (-4.,-0.4)-- (-4.2,-0.4);
                    \\draw [line width=1.pt ,color=zzttqq] (-4.2,-0.4)-- (-4.2,3.);
                    \\draw [line width=1.pt ,color=zzttqq] (-4.2,3.)-- (-4.,3.);
                    \\draw [line width=1.pt ,color=zzttqq] (4.,3.)-- (4.,-0.4);
                    \\draw [line width=1.pt ,color=zzttqq] (4.,-0.4)-- (4.2,-0.4);
                    \\draw [line width=1.pt ,color=zzttqq] (4.2,-0.4)-- (4.2,3.);
                    \\draw [line width=1.pt ,color=zzttqq] (4.2,3.)-- (4.,3.);
                    \\draw [line width=1.pt ,color=yqyqyq] (3.8,-0.4)-- (4.4,-0.4);
                    \\draw [line width=1.pt ,color=yqyqyq] (4.4,-0.4)-- (4.4,-0.6);
                    \\draw [line width=1.pt ,color=yqyqyq] (4.4,-0.6)-- (3.8,-0.6);
                    \\draw [line width=1.pt ,color=yqyqyq] (3.8,-0.6)-- (3.8,-0.4);
                    \\draw [line width=1.pt ,color=yqyqyq] (-4.4,-0.4)-- (-3.8,-0.4);
                    \\draw [line width=1.pt ,color=yqyqyq] (-3.8,-0.4)-- (-3.8,-0.6);
                    \\draw [line width=1.pt ,color=yqyqyq] (-3.8,-0.6)-- (-4.4,-0.6);
                    \\draw [line width=1.pt ,color=yqyqyq] (-4.4,-0.6)-- (-4.4,-0.4);
                    \\draw [shift={(0.3348100726041409,4.92707450091433)},line width=1.pt ,color=ffqqqq]  plot[domain=3.5599118048120024:4.641752672640623,variable=\\t]({1.*4.743858608519496*cos(\\t r)+0.*4.743858608519496*sin(\\t r)},{0.*4.743858608519496*cos(\\t r)+1.*4.743858608519496*sin(\\t r)});
                    \\draw [shift={(-0.3348100726041409,4.92707450091433)},line width=1.pt ,color=ffqqqq]  plot[domain=4.783025288128757:5.864866155957377,variable=\\t]({1.*4.743858608519496*cos(\\t r)+0.*4.743858608519496*sin(\\t r)},{0.*4.743858608519496*cos(\\t r)+1.*4.743858608519496*sin(\\t r)});
                    \\draw [line width=1.pt ,color=ffxfqq] (-3.5100090698522193,0.23825326031607422)-- (-3.509002196102234,2.1469123220897077);
                    \\draw [line width=1.pt ,color=ffxfqq] (-2.9735263101483325,1.5272061393184275)-- (-2.9871290058847397,0.20701015383185986);
                    \\draw [line width=1.pt ,color=ffxfqq] (-2.493317311142619,1.118414631757433)-- (-2.4908618264409976,0.20502243482207186);
                    \\draw [line width=1.pt ,color=ffxfqq] (-1.9870192871538226,0.7902516956940664)-- (-2.0122842450819074,0.2031055686751062);
                    \\draw [line width=1.pt ,color=ffxfqq] (-1.481478046142483,0.5446902220856948)-- (-1.4893229296656063,0.20101093056262434);
                    \\draw [line width=1.pt ,color=ffxfqq] (-0.9925643056142766,0.372706075141795)-- (-0.993020252700624,0.19902306937317849);
                    \\draw [line width=1.pt ,color=ffxfqq] (1.0081656569953046,0.37728212242810244)-- (1.0010530029622524,0.19103612709415496);
                    \\draw [line width=1.pt ,color=ffxfqq] (1.481478046142474,0.5446902220856904)-- (1.4973201824059945,0.18904840808436693);
                    \\draw [line width=1.pt ,color=ffxfqq] (2.0006647837623994,0.7979400040852171)-- (2.0113834524981096,0.18698940967278302);
                    \\draw [line width=1.pt ,color=ffxfqq] (2.5027225252346037,1.1254165397312055)-- (2.5076861294630914,0.18500154848333716);
                    \\draw [line width=1.pt ,color=ffxfqq] (2.973526310148331,1.5272061393184266)-- (2.9862637108221817,0.1830846823363715);
                    \\draw [line width=1.pt ,color=ffxfqq] (3.499520855821278,2.1338504087683394)-- (3.5091895287172425,0.1809901864035475);
                    \\draw [->,line width=1.pt ] (-5.0072991382131935,0.2220052361613305) -- (5.023939482141669,0.17163918451101345);
                    \\draw [->,line width=1.pt ] (-0.0042713409483419685,-0.19771186092464504) -- (0.,3.5);
                    \\draw [line width=1.pt ,dash pattern=on 1pt off 1pt] (-4.,3.)-- (4.,3.);
                    \\draw [line width=1.pt ] (4.2,3.)-- (4.5,3.);
                    \\draw [line width=1.pt ] (-4.125893234332641,-0.6)-- (-4.13428757627436,-0.8944422420873644);
                    \\draw [line width=1.pt ] (4.108956210494237,-0.6)-- (4.117350552435957,-0.9112309259708035);
                    \\draw [line width=1.pt ] (2.,0.)-- (2.01037072506435,-0.21450054480808406);
                    \\draw [line width=1.pt ] (0.,-0.5)-- (-0.0042713409483419685,-0.9112309259708035);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (4.402758178454421,1.5063395532444157) -- (4.385969494570984,3.);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (4.402758178454421,1.5063395532444157) -- (4.402647399035171,0.1747586426688703);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (1.0030496920580039,-0.11376844150744993) -- (2.0062629434914525,-0.12953817430151165);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (1.0030496920580039,-0.11376844150744993) -- (-0.004174364245711937,-0.11375885696510535);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (1.9851876992391913,-0.8021044807284499) -- (4.114623434752381,-0.8101195621755717);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (1.9851876992391913,-0.8021044807284499) -- (-0.003224272029433095,-0.8104225085942109);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (-1.993730381135875,-0.8021044807284499) -- (-0.003224272029433095,-0.8104225085942109);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (-1.993730381135875,-0.8021044807284499) -- (-4.1318963517641,-0.810566994804902);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (2.0058901041012938,0.5001033374470178) -- (2.0006647837623994,0.7979400040852171);
                    \\draw [->,line width=1.pt ,dash pattern=on 1pt off 1pt] (2.0058901041012938,0.5001033374470178) -- (2.0113834524981096,0.186989409672783);
                    \\draw (1.8340895442882392,-0.7433440871364133) node[anchor=north west] {$%s$};
                    \\draw (-2.480602213755609,-0.7601327710198523) node[anchor=north west] {$%s$};
                    \\draw (4.276843049328628,0.23879392004476954) node[anchor=north west] {$%s$};
                    \\draw (-5.4,0.24718826198648905) node[anchor=north west] {$-%s$};
                    \\draw (0.7092477240978197,-0.055008047915413354) node[anchor=north west] {$%s$};
                    \\draw (2.7071011062270722,0.07930142315209882) node[anchor=north west] {$%s$};
                    \\draw (4.461518572046458,1.8337188889714766) node[anchor=north west] {$%s$};
                    \\draw (-0.6,3.076081496345964) node[anchor=north west] {$%s$};
                    \\draw (-0.6,0.7172714107227817) node[anchor=north west] {$O$};
                    \\draw (-4.4,3.546164645082257) node[anchor=north west] {$A$};
                    \\draw (3.907492003892968,3.579742012849135) node[anchor=north west] {$B$};
                    \\draw (-0.5,3.6217137225577325) node[anchor=north west] {$y$};
                    \\draw (4.696560146414606,0.7088770687810622) node[anchor=north west] {$x$};
            \\end{tikzpicture} }'''
                                '}'
                                %(latex(a),latex(b),latex(c),
                                latex(Rational(b,2)),latex(Rational(b,2)),latex(Rational(b,2)),latex(Rational(b,2)),
                                latex(c),latex(c),latex(a),latex(a)
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
                loigiai = ('Parabol có dạng $y=ax^2$ với $a>0$. \\\\ \n'
                        'Theo giả thiết, cây cầu có trụ tháp đôi cao $%s$ m so với mặt cầu và cách nhau $%s$ m nên ta có các điểm $A(%s;%s), B(%s;%s)$ thuộc parabol, ta có \\\\ \n'
                        '\\hspace*{1cm} $%s=a \\cdot %s \\Leftrightarrow a=%s$. \\\\ \n'
                        'Suy ra phương trình của parabol là $y=%s x^2$. \\\\ \n'
                        'Với $x=%s$ ta có $y=%s \\cdot %s^2=%s$. \\\\ \n'
                        'Vậy chiều cao của dây cáp tại điểm cách tâm của cây cầu $%s$ m là $%s$ m.'

                        %(latex(a),latex(b),
                            latex(-Rational(b,2)),latex(a),latex(Rational(b,2)),latex(a),
                            latex(a),latex((b/2)**2),latex(Rational(a,(b/2)**2)),
                            latex(Rational(a,(b/2)**2)),
                            latex(c),latex(Rational(a,(b/2)**2)), latex(c),latex(kq),
                            latex(c),latex(kq)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

