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


def bt_dang3_p1_b3_c2_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x,y,z,t,s=symbols('x,y,z,t,s')
                a1=randint(-6,6)
                b1=randint(-6,6)
                c1=randint(-7,7)
                d1=randint(-15,15)
                a2=randint(-6,6)
                b2=randint(-6,6)
                c2=randint(-7,7)
                d2=randint(-15,15)
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-7,7)
                xb=randint(-6,6)
                yb=randint(-6,6)
                zb=randint(-7,7)
                while a1==0 or b1==0 or c1==0 or a2==0 or b2==0 or c2==0 or a1==b1 or xa==xb:
                    a1=randint(-6,6)
                    b1=randint(-6,6)
                    c1=randint(-7,7)
                    d1=randint(-15,15)
                    a2=randint(-6,6)
                    b2=randint(-6,6)
                    c2=randint(-7,7)
                    d2=randint(-15,15)
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-7,7)
                    xb=randint(-6,6)
                    yb=randint(-6,6)
                    zb=randint(-7,7)
                hd1=xa+a1*t
                td1=ya+b1*t
                cd1=za+c1*t
                hd2=xb+a2*s
                td2=yb+b2*s
                cd2=zb+c2*s
                tvh=abs(a1*a2+b1*b2+c1*c2)
                l1=sqrt(a1**2+b1**2+c1**2)
                l2=sqrt(a2**2+b2**2+c2**2)
                cos=nsimplify(tvh/(l1*l2))
                g=math.degrees(math.acos(cos))
                kq1=g
                kq_2=g-3
                kq_3=g-4
                kq_4=g-1
                kq_5=g-2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_2))  # Số cần làm tròn
                kq2 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_3))  # Số cần làm tròn
                kq3 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_4))  # Số cần làm tròn
                kq4 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_5))  # Số cần làm tròn
                kq5 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)


                du = ['$%s^{\\circ}$'%(latex(kq))
                    ]
                da= random.choice(du)
                s = ['$%s^{\\circ}$'%(latex(kq2)),
                    '$%s^{\\circ}$'%(latex(kq3)),
                    '$%s^{\\circ}$'%(latex(kq4)),
                    '$%s^{\\circ}$'%(latex(kq5))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =  ('Trong không gian $Oxyz$, cho hai đường thẳng $\\Delta_1: \\heva{&x=%s\\\\&y=%s\\\\&z=%s},\\Delta_2: \\heva{&x=%s\\\\&y=%s\\\\&z=%s}$zz$$ Góc giữa hai đường thẳng $\\Delta_1$ và đường thẳng $\\Delta_2$ (kết quả làm tròn đến hàng phần chục) bằng'
                                %(latex(hd1),latex(td1),latex(cd1),latex(hd2),latex(td2),latex(cd2)
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
                loigiai=('Đường thẳng $\\Delta_1$ có vectơ chỉ phương là $\\vec{u_1}=(%s;%s;%s)$$zz$\\\\ \n'
                            'Đường thẳng $\\Delta_2$ có vectơ chỉ phương là $\\vec{u_2}=(%s;%s;%s)$$zz$\\\\ \n'
                            'Ta có $\\cos \\left(\\Delta_1,\\Delta_2\\right)=\\dfrac{\\abs{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}\\cdot\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$$zz$\\\\ \n'
                            'Do đó $\\left(\\Delta_1,\\Delta_2\\right)\\approx %s^{\\circ}$$zz$'
                        %(latex(a1),latex(b1),latex(c1),
                        latex(a2),latex(b2),latex(c2),
                        latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),
                        latex(a1),latex(b1),latex(c1),
                        latex(a2),latex(b2),latex(c2),latex(cos),latex(kq)

                        ))
            if dang=='2':
                # Khai báo biến
                x,y,z,t=symbols('x,y,z,t')
                a1=randint(-6,6)
                b1=randint(-6,6)
                c1=randint(-7,7)
                d1=randint(-15,15)
                a2=randint(-6,6)
                b2=randint(-6,6)
                c2=randint(-7,7)
                d2=randint(-15,15)
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-7,7)
                xb=randint(-6,6)
                yb=randint(-6,6)
                zb=randint(-7,7)
                while a1==0 or b1==0 or c1==0 or a2==0 or b2==0 or c2==0 or a1==b1 or xa==xb:
                    a1=randint(-6,6)
                    b1=randint(-6,6)
                    c1=randint(-7,7)
                    d1=randint(-15,15)
                    a2=randint(-6,6)
                    b2=randint(-6,6)
                    c2=randint(-7,7)
                    d2=randint(-15,15)
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-7,7)
                    xb=randint(-6,6)
                    yb=randint(-6,6)
                    zb=randint(-7,7)
                hd1=x-xa
                td1=y-ya
                cd1=z-za
                hd2=x-xb
                td2=y-yb
                cd2=z-zb
                tvh=abs(a1*a2+b1*b2+c1*c2)
                l1=sqrt(a1**2+b1**2+c1**2)
                l2=sqrt(a2**2+b2**2+c2**2)
                cos=nsimplify(tvh/(l1*l2))
                g=math.degrees(math.acos(cos))
                kq1=g
                kq_2=g-3
                kq_3=g-4
                kq_4=g-1
                kq_5=g-2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_2))  # Số cần làm tròn
                kq2 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_3))  # Số cần làm tròn
                kq3 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_4))  # Số cần làm tròn
                kq4 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_5))  # Số cần làm tròn
                kq5 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)


                du = ['$%s^{\\circ}$'%(latex(kq))
                    ]
                da= random.choice(du)
                s = ['$%s^{\\circ}$'%(latex(kq2)),
                    '$%s^{\\circ}$'%(latex(kq3)),
                    '$%s^{\\circ}$'%(latex(kq4)),
                    '$%s^{\\circ}$'%(latex(kq5))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =  ('Trong không gian $Oxyz$, cho hai đường thẳng $$\\Delta_1: \\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s},\\Delta_2: \\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$zz$$$Góc giữa hai đường thẳng $\\Delta_1$ và đường thẳng $\\Delta_2$ (kết quả làm tròn đến hàng phần chục) bằng'
                                %(latex(hd1),latex(a1),latex(td1),latex(b1),latex(cd1),latex(c1),latex(hd2),latex(a2),latex(td2),latex(b2),latex(cd2),latex(c2)
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
                loigiai= ('Đường thẳng $\\Delta_1$ có vectơ chỉ phương là $\\vec{u_1}=(%s;%s;%s)$$zz$\\\\ \n'
                            'Đường thẳng $\\Delta_2$ có vectơ chỉ phương là $\\vec{u_2}=(%s;%s;%s)$$zz$\\\\ \n'
                            'Ta có $\\cos \\left(\\Delta_1,\\Delta_2\\right)=\\dfrac{\\abs{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}\\cdot\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$$zz$\\\\ \n'
                            'Do đó $\\left(\\Delta_1,\\Delta_2\\right)\\approx %s^{\\circ}$$zz$'
                        %(latex(a1),latex(b1),latex(c1),
                        latex(a2),latex(b2),latex(c2),
                        latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),
                        latex(a1),latex(b1),latex(c1),
                        latex(a2),latex(b2),latex(c2),latex(cos),latex(kq)

                        ))
            if dang=='3':
                # Khai báo biến
                x,y,z,t=symbols('x,y,z,t')
                a1=randint(-6,6)
                b1=randint(-6,6)
                c1=randint(-7,7)
                d1=randint(-15,15)
                a2=randint(-6,6)
                b2=randint(-6,6)
                c2=randint(-7,7)
                d2=randint(-15,15)
                xa=randint(-6,6)
                ya=randint(-6,6)
                za=randint(-7,7)
                xb=randint(-6,6)
                yb=randint(-6,6)
                zb=randint(-7,7)
                while a1==0 or b1==0 or c1==0 or a2==0 or b2==0 or c2==0 or a1==b1 or xa==xb:
                    a1=randint(-6,6)
                    b1=randint(-6,6)
                    c1=randint(-7,7)
                    d1=randint(-15,15)
                    a2=randint(-6,6)
                    b2=randint(-6,6)
                    c2=randint(-7,7)
                    d2=randint(-15,15)
                    xa=randint(-6,6)
                    ya=randint(-6,6)
                    za=randint(-7,7)
                    xb=randint(-6,6)
                    yb=randint(-6,6)
                    zb=randint(-7,7)
                hd1=xa+a1*t
                td1=ya+b1*t
                cd1=za+c1*t
                hd2=x-xb
                td2=y-yb
                cd2=z-zb
                tvh=abs(a1*a2+b1*b2+c1*c2)
                l1=sqrt(a1**2+b1**2+c1**2)
                l2=sqrt(a2**2+b2**2+c2**2)
                cos=nsimplify(tvh/(l1*l2))
                g=math.degrees(math.acos(cos))
                kq1=g
                kq_2=g-3
                kq_3=g-4
                kq_4=g-1
                kq_5=g-2
                number = Decimal(float(kq1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_2))  # Số cần làm tròn
                kq2 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_3))  # Số cần làm tròn
                kq3 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_4))  # Số cần làm tròn
                kq4 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                number = Decimal(float(kq_5))  # Số cần làm tròn
                kq5 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)


                du = ['$%s^{\\circ}$'%(latex(kq))
                    ]
                da= random.choice(du)
                s = ['$%s^{\\circ}$'%(latex(kq2)),
                    '$%s^{\\circ}$'%(latex(kq3)),
                    '$%s^{\\circ}$'%(latex(kq4)),
                    '$%s^{\\circ}$'%(latex(kq5))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi =  ('Trong không gian $Oxyz$, cho hai đường thẳng $$\\Delta_1: \\heva{&x=%s\\\\&y=%s\\\\&z=%s},\\Delta_2: \\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$zz$$$Góc giữa hai đường thẳng $\\Delta_1$ và đường thẳng $\\Delta_2$ ( kết quả làm tròn đến hàng phần chục) bằng'
                                %(latex(hd1),latex(td1),latex(cd1),latex(hd2),latex(a2),latex(td2),latex(b2),latex(cd2),latex(c2)
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
                loigiai= ('Đường thẳng $\\Delta_1$ có vectơ chỉ phương là $\\vec{u_1}=(%s;%s;%s)$$zz$\\\\ \n'
                            'Đường thẳng $\\Delta_2$ có vectơ chỉ phương là $\\vec{u_2}=(%s;%s;%s)$$zz$\\\\ \n'
                            'Ta có $\\cos \\left(\\Delta_1,\\Delta_2\\right)=\\dfrac{\\abs{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}\\cdot\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$$zz$\\\\ \n'
                            'Do đó $\\left(\\Delta_1,\\Delta_2\\right)\\approx %s^{\\circ}$$zz$'
                        %(latex(a1),latex(b1),latex(c1),
                        latex(a2),latex(b2),latex(c2),
                        latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),
                        latex(a1),latex(b1),latex(c1),
                        latex(a2),latex(b2),latex(c2),latex(cos),latex(kq)

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('--','+').replace('+-','-').replace('.',',').replace('$zz$','.')
            return content

