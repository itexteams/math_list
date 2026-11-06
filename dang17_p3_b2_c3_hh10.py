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


def bt_dang17_p3_b2_c3_hh10(self):
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                xm=randint(-9,9)
                ym=randint(-9,9)
                xn=randint(-9,9)
                yn=randint(-9,9)

                xa=randint(-9,9)
                ya=randint(-9,9)

                xb=2*xm-xa
                yb=2*ym-ya
                xc=2*xn-xa
                yc=2*yn-ya

                while xc==xa or yc==ya or xb==xa or yb==ya or (xb-xa)/(xc-xa)==(yb-ya)/(yc-ya):
                    x=symbols('x')
                    y=symbols('y')
                    xm=randint(-9,9)
                    ym=randint(-9,9)
                    xn=randint(-9,9)
                    yn=randint(-9,9)

                    xa=randint(-9,9)
                    ya=randint(-9,9)

                    xb=2*xm-xa
                    yb=2*ym-ya
                    xc=2*xn-xa
                    yc=2*yn-ya

                ttab1=(xb-xa)*x+(yb-ya)*y-(xb-xa)*xm-(yb-ya)*ym
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((xb-xa),(yb-ya)),-(xb-xa)*xm-(yb-ya)*ym)
                # Rút gọn các hệ số
                hs_a1 = (xb-xa) // gcd
                hs_b1 = (yb-ya) // gcd
                hs_c1 = (-(xb-xa)*xm-(yb-ya)*ym)// gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                ttab = hs_a1*x+hs_b1*y+hs_c1

                dtcd1=(ya-yb)*x+(xb-xa)*y-(ya-yb)*xc-(xb-xa)*yc
                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd((ya-yb),(xb-xa)),-(ya-yb)*xc-(xb-xa)*yc)
                # Rút gọn các hệ số
                hs_a2 = (ya-yb) // gcd
                hs_b2 = (xb-xa) // gcd
                hs_c2 = (-(ya-yb)*xc-(xb-xa)*yc)// gcd
                #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                dtcd = hs_a2*x+hs_b2*y+hs_c2

                eq1 = Eq(hs_a1*x+hs_b1*y,-hs_c1)
                eq2 = Eq(hs_a2*x+hs_b2*y,-hs_c2)

                # Giải hệ phương trình
                solution = solve((eq1, eq2), (x, y))

                # Tách riêng nghiệm
                x_value = solution[x]
                y_value = solution[y]

                while (xc-x_value)*(xb-xa)<=0:
                    x=symbols('x')
                    y=symbols('y')
                    xm=randint(-9,9)
                    ym=randint(-9,9)
                    xn=randint(-9,9)
                    yn=randint(-9,9)

                    xa=randint(-9,9)
                    ya=randint(-9,9)

                    xb=2*xm-xa
                    yb=2*ym-ya
                    xc=2*xn-xa
                    yc=2*yn-ya

                    while xc==xa or yc==ya or (xb-xa)/(xc-xa)==(yb-ya)/(yc-ya):
                        x=symbols('x')
                        y=symbols('y')
                        xm=randint(-9,9)
                        ym=randint(-9,9)
                        xn=randint(-9,9)
                        yn=randint(-9,9)

                        xa=randint(-9,9)
                        ya=randint(-9,9)

                        xb=2*xm-xa
                        yb=2*ym-ya
                        xc=2*xn-xa
                        yc=2*yn-ya

                    ttab1=(xb-xa)*x+(yb-ya)*y-(xb-xa)*xm-(yb-ya)*ym
                    # Tìm ước chung lớn nhất (GCD) của các hệ số
                    gcd = math.gcd(math.gcd((xb-xa),(yb-ya)),-(xb-xa)*xm-(yb-ya)*ym)
                    # Rút gọn các hệ số
                    hs_a1 = (xb-xa) // gcd
                    hs_b1 = (yb-ya) // gcd
                    hs_c1 = (-(xb-xa)*xm-(yb-ya)*ym)// gcd
                    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                    ttab = hs_a1*x+hs_b1*y+hs_c1

                    dtcd1=(ya-yb)*x+(xb-xa)*y-(ya-yb)*xc-(xb-xa)*yc
                    # Tìm ước chung lớn nhất (GCD) của các hệ số
                    gcd = math.gcd(math.gcd((ya-yb),(xb-xa)),-(ya-yb)*xc-(xb-xa)*yc)
                    # Rút gọn các hệ số
                    hs_a2 = (ya-yb) // gcd
                    hs_b2 = (xb-xa) // gcd
                    hs_c2 = (-(ya-yb)*xc-(xb-xa)*yc)// gcd
                    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                    dtcd = hs_a2*x+hs_b2*y+hs_c2

                    eq1 = Eq(hs_a1*x+hs_b1*y,-hs_c1)
                    eq2 = Eq(hs_a2*x+hs_b2*y,-hs_c2)

                    # Giải hệ phương trình
                    solution = solve((eq1, eq2), (x, y))

                    # Tách riêng nghiệm
                    x_value = solution[x]
                    y_value = solution[y]


                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho ba điểm $A(%s;%s),B(%s;%s),C(%s;%s)$ Tọa độ điểm $D$ để tứ giác $ABCD$ là hình thang cân với hai đáy $AB,CD$ là $(a;b)$. Giá trị $a+b$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                                %(latex(xa),latex(ya),latex(xb),latex(yb),latex(xc),latex(yc))
                                )

                # Nội dung lời giải
                h1=2*x_value-xc+2*y_value-yc
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kqz=str(kq1).replace('.',',')
                loigiai = ('''\\begin{center} \n'''
                        '''\\scalebox{0.8}{ \n'''
                    '''\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-6.02,-1) rectangle (10,4.5);
                \\draw (2.,3.)-- (6.,3.);
                \\draw (6.,3.)-- (8.,0.);
                \\draw (2.,3.)-- (0.,0.);
                \\draw (0.,0.)-- (8.,0.);
                \\draw (4.,4.)-- (4.,-1.);
                \\draw (1.44,3.5) node[anchor=north west] {$A$};
                \\draw (-0.66,0.36) node[anchor=north west] {$D$};
                \\draw (6,3.5) node[anchor=north west] {$B$};
                \\draw (8.22,0.44) node[anchor=north west] {$C$};
                \\draw (4.16,4.32) node[anchor=north west] {$d$};
                \\draw (3.42,0.04) node[anchor=north west] {$F$};
                \\draw (3.36,3.5) node[anchor=north west] {$M$};
            \\end{tikzpicture}}\n'''
            '''\\end{center}\n'''
                    'Ta có $\\vec{AB}=(%s;%s)$. Lấy $M$ là trung điểm $AB$ ta được $M(%s;%s)$. Đường trung trực $d$ của cạnh $AB$ có phương trình là '
                        '$%s(x- %s)+ %s(y- %s)\\Leftrightarrow %s=0$  $(d)$.\\\\ \n '
                        'Đường thẳng $CD$ đi qua $C(%s;%s)$ và song song với $AB$ có vectơ chỉ phương $\\vec{AB}=(%s;%s)$\\\\ \n'
                        '$\\Rightarrow$ vectơ pháp tuyến $\\vec{u}=(%s;%s)$ có phương trình \\\\ \n'
                        '$CD: %s(x- %s)+ %s(y- %s)\\Leftrightarrow %s=0$.\\\\ \n '
                        'Giao điểm $F$ của hai đường thẳng $d$ và $CD$ có tọa độ là nghiệm của hệ $\\heva{& %s=0 \\\\ & %s=0}$\\\\ \n'
                        'Nên $F\\left(%s;%s\\right)$. Vì tứ giác $ABCD$ là hình thang cân với hai đáy $AB,CD$ nên $D$ là điểm đối xứng với $C$ qua $d$, do đó $F$ là trung điểm của đoạn $CD$. \\\\ \n'
                        'Gọi $D(x_D;y_D)$ ta có $\\heva{&\\dfrac{%s+x_D}{2}=%s \\\\ & \\dfrac{%s+x_D}{2}=%s}$ suy ra $D\\left(%s;%s\\right)$.\\\\ \n'
                        'Nhận thấy $\\vec{AB}=\\left(%s;%s\\right); \\vec{DC}=\\left(%s;%s\\right)$ cùng hướng nên $D\\left(%s;%s\\right)$ thỏa mãn.\\\\'
                        'Vậy $a+b \\approx %s$.'

                        %(latex(xb-xa),latex(yb-ya),latex(xm),latex(ym),
                            latex(xb-xa),latex(xm),latex(yb-ya),latex(ym),latex(ttab),
                            latex(xc),latex(yc),latex(xb-xa),latex(yb-ya),latex(ya-yb),latex(xb-xa),
                            latex(ya-yb),latex(xc),latex(xb-xa),latex(yc),latex(dtcd),
                            latex(ttab),latex(dtcd),latex(x_value),latex(y_value),
                            latex(xc),latex(x_value),latex(yc),latex(y_value),
                            latex(2*x_value-xc),latex(2*y_value-yc),latex(xb-xa),latex(yb-ya),latex(xc-x_value),latex(yc-y_value),latex(2*x_value-xc),latex(2*y_value-yc),
                            kqz

                            )
                        )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kqz)

                du = ['$\\left(%s;%s\\right)$'%(latex(2*x_value-xc),latex(2*y_value-yc)),

                    ]
                da = random.choice(du)
                s = ['$\\left(%s;%s\\right)$'%(latex(2*x_value-xc+1),latex(2*y_value-yc)),
                    '$\\left(%s;%s\\right)$'%(latex(2*x_value-xc),latex(2*y_value-yc+1)),
                    '$\\left(%s;%s\\right)$'%(latex(2*x_value-xc-1),latex(2*y_value-yc)),
                    '$\\left(%s;%s\\right)$'%(latex(2*x_value-xc),latex(2*y_value-yc-1)),



                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+ -', '-').replace('- -', '+')
            return content 

