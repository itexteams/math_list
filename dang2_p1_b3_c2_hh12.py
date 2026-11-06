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


def bt_dang2_p1_b3_c2_hh12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a1=randint(-6,6)
                b1=randint(-6,6)
                c1=randint(-7,7)
                d1=randint(-15,15)
                a2=randint(-6,6)
                b2=randint(-6,6)
                c2=randint(-7,7)
                d2=randint(-15,15)

                while a1**2+b1**2+c1**2==0 or a2**2+b2**2+c2**2==0:
                    a1=randint(-6,6)
                    b1=randint(-6,6)
                    c1=randint(-7,7)
                    d1=randint(-15,15)
                    a2=randint(-6,6)
                    b2=randint(-6,6)
                    c2=randint(-7,7)
                    d2=randint(-15,15)
                pt1=a1*x+b1*y+c1*z+d1
                pt2=a2*x+b2*y+c2*z+d2
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
                noidungcauhoi =   ('Trong không gian $Oxyz$, cho hai mặt phẳng $$(P):%s=0,(Q):%s=0$zz$$$Góc giữa hai mặt phẳng $(P)$ và $(Q)$ (kết quả làm tròn đến hàng phần chục) bằng'
                                %(latex(pt1),latex(pt2)
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
                loigiai= ('Các mặt phẳng $(P),(Q)$ tương ứng có các vectơ pháp tuyến là $\\vec{n_1}=(%s;%s;%s),\\vec{n_2}=(%s;%s;%s)$$zz$\\\\ \n'
                            'Ta có $\\cos \\left((P),(Q)\\right)=\\dfrac{\\abs{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}\\cdot\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$$zz$\\\\ \n'
                            'Do đó $\\left((P),(Q)\\right)\\approx %s^{\\circ}$$zz$'
                        %(latex(a1),latex(b1),latex(c1),
                            latex(a2),latex(b2),latex(c2),
                            latex(a1),latex(a2),latex(b1),latex(b2),latex(c1),latex(c2),
                            latex(a1),latex(b1),latex(c1),
                            latex(a2),latex(b2),latex(c2),latex(cos),latex(kq)

                            ))
            if dang=='2':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a1=randint(-6,6)
                b1=randint(-6,6)
                c1=randint(-7,7)
                d1=randint(-15,15)
                a2=randint(-6,6)
                b2=randint(-6,6)
                c2=randint(-7,7)
                d2=randint(-15,15)

                while a1**2+b1**2+c1**2==0 or a2**2+b2**2+c2**2==0:
                    a1=randint(-6,6)
                    b1=randint(-6,6)
                    c1=randint(-7,7)
                    d1=randint(-15,15)
                    a2=randint(-6,6)
                    b2=randint(-6,6)
                    c2=randint(-7,7)
                    d2=randint(-15,15)
                pt1=a1*x+b1*y+c1*z+d1
                pt2=a2*x+b2*y+c2*z+d2
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
                noidungcauhoi =   ('Trong không gian $Oxyz$, cho hai mặt phẳng $$(P):%s=0,(Q):%s=0$zz$$$Góc giữa hai mặt phẳng $(P)$ và $(Q)$ (kết quả làm tròn đến hàng phần chục) bằng'
                                %(latex(pt1),latex(pt2)
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
                loigiai= ('Các mặt phẳng $(P),(Q)$ tương ứng có các vectơ pháp tuyến là $\\vec{n_1}=(%s;%s;%s),\\vec{n_2}=(%s;%s;%s)$$zz$\\\\ \n'
                            'Ta có $\\cos \\left((P),(Q)\\right)=\\dfrac{\\abs{%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}\\cdot\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%s$$zz$\\\\ \n'
                            'Do đó $\\left((P),(Q)\\right)\\approx %s^{\\circ}$$zz$'
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

