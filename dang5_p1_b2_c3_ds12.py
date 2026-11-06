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


def bt_dang5_p1_b2_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a=randint(-4,4)
                k=randint(1,4)
                b=a+k
                n=randint(1,3)
                while a==0:
                    x=symbols('x')
                    a=randint(-4,4)
                    k=randint(1,4)
                    b=a+k
                    n=randint(1,3)
                y=x**(n+1)
                y2=y.subs(x,b)
                y1=y.subs(x,a)
                kq=y2-y1


                du = ['$%s$'%(latex(kq))
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq+4)),
                    '$%s$'%(latex(kq+5)),
                    '$%s$'%(latex(kq+6))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle\\int\\limits_{%s}^{%s} %sx^{%s}\\text{d}x$ bằng'
                                %(latex(a),latex(b),latex(n+1),latex(n)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle\\int\\limits_{%s}^{%s} %sx^{%s}\\text{d}x=x^{%s}\\bigg|_{%s}^{%s}=\\left(%s\\right)^{%s}-\\left(%s\\right)^{%s}=%s$.'
                        %(latex(a),latex(b),latex(n+1),latex(n),latex(n+1),latex(a),latex(b),latex(b),latex(n+1),latex(a),latex(n+1),latex(kq))


                        )
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                m=randint(-9,9)
                a=randint(-4,4)
                k=randint(1,4)
                b=a+k
                n=randint(1,3)
                while a==0 or m==0:
                    x=symbols('x')
                    a=randint(-4,4)
                    k=randint(1,4)
                    b=a+k
                    n=randint(1,3)
                    m=randint(-9,9)
                y=x**(n+1)
                y2=y.subs(x,b)
                y1=y.subs(x,a)
                kq=nsimplify((y2-y1)*(m/(n+1)))


                du = ['$%s$'%(latex(kq))
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq+4)),
                    '$%s$'%(latex(kq+5)),
                    '$%s$'%(latex(kq+6))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle\\int\\limits_{%s}^{%s} %sx^{%s}\\text{d}x$ bằng'
                                %(latex(a),latex(b),latex(m),latex(n)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle\\int\\limits_{%s}^{%s} %sx^{%s}\\text{d}x=%sx^{%s}\\bigg|_{%s}^{%s}=%s\\left[\\left(%s\\right)^{%s}-\\left(%s\\right)^{%s}\\right]=%s$.'
                        %(latex(a),latex(b),latex(m),latex(n),latex(nsimplify(m/(n+1))),latex(n+1),latex(a),latex(b),latex(nsimplify(m/(n+1))),latex(b),latex(n+1),latex(a),latex(n+1),latex(kq))


                        )
            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                a=randint(0,1)
                k=randint(1,2)
                b=a+k
                e=randint(2,9)
                while e**b-e**a-1==0 or e**b-e**a-2==0 or e**b-e**a-3==0 or e**b-e**a-4==0:
                    x=symbols('x')
                    a=randint(0,1)
                    k=randint(1,2)
                    b=a+k
                    e=randint(2,9)

                du = ['$\\dfrac{%s}{\\ln%s}$'%(latex(e**b-e**a),latex(e))
                    ]
                da= random.choice(du)
                s = ['$\\dfrac{%s}{\\ln%s}$'%(latex(e**b+e**a),latex(e)),
                    '$\\dfrac{%s}{\\ln%s}$'%(latex(e**b-e**a-1),latex(e)),
                    '$\\dfrac{%s}{\\ln%s}$'%(latex(e**b-e**a-2),latex(e)),
                    '$\\dfrac{%s}{\\ln%s}$'%(latex(e**b-e**a-3),latex(e))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle\\int\\limits_{%s}^{%s} %s^x\\text{d}x$ bằng'
                                %(latex(a),latex(b),latex(e)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle\\int\\limits_{%s}^{%s} %s^x\\text{d}x=\\dfrac{%s^x}{\\ln%s}\\bigg|_{%s}^{%s}=\\dfrac{%s^%s}{\\ln%s}-\\dfrac{%s^%s}{\\ln%s}=\\dfrac{%s}{\\ln%s}$.'
                        %(latex(a),latex(b),latex(e),latex(e),latex(e),latex(a),latex(b),latex(e),latex(b),latex(e),latex(e),latex(a),latex(e),latex(e**b-e**a),latex(e))


                        )
            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,6)
                k=randint(1,5)
                b=a-k
                e=randint(2,20)
                while a==5 or a==1 or b==1 or b==5 or b<=0:
                    x=symbols('x')
                    a=randint(1,6)
                    k=randint(1,5)
                    b=a-k
                    e=randint(2,20)
                y1=nsimplify(math.sin(math.pi/a))
                y2=nsimplify(math.sin(math.pi/b))
                kq=e*(y2-y1)


                du = ['$%s$'%(latex(kq))
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(-kq)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*-2)),
                    '$%s$'%(latex(kq*3))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle\\int\\limits_{\\dfrac{\\pi}{%s}}^{\\dfrac{\\pi}{%s}} %s\\cos x\\text{d}x$ bằng'
                                %(latex(a),latex(b),latex(e)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle\\int\\limits_{\\dfrac{\\pi}{%s}}^{\\dfrac{\\pi}{%s}} %s\\cos x\\text{d}x=%s\\sin x\\bigg|_{\\dfrac{\\pi}{%s}}^{\\dfrac{\\pi}{%s}}=%s\\left[\\sin \\left(\\dfrac{\\pi}{%s}\\right)-\\sin \\left(\\dfrac{\\pi}{%s}\\right)\\right]=%s$.'
                        %(latex(a),latex(b),latex(e),latex(e),latex(a),latex(b),latex(e),latex(b),latex(a),latex(kq))


                        )
            if dang=='5':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,6)
                k=randint(1,5)
                b=a-k
                e=randint(2,20)
                while a==5 or a==1 or b==1 or a==2 or b==2 or b==5 or b<=0:
                    x=symbols('x')
                    a=randint(1,6)
                    k=randint(1,5)
                    b=a-k
                    e=randint(2,20)
                y1=nsimplify(math.cos(math.pi/a))
                y2=nsimplify(math.cos(math.pi/b))
                kq=-e*(y2-y1)


                du = ['$%s$'%(latex(kq))
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(-kq)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*-2)),
                    '$%s$'%(latex(kq*3))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle\\int\\limits_{\\dfrac{\\pi}{%s}}^{\\dfrac{\\pi}{%s}} %s\\sin x\\text{d}x$ bằng'
                                %(latex(a),latex(b),latex(e)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle\\int\\limits_{\\dfrac{\\pi}{%s}}^{\\dfrac{\\pi}{%s}} %s\\sin x\\text{d}x=-%s\\cos x\\bigg|_{\\dfrac{\\pi}{%s}}^{\\dfrac{\\pi}{%s}}=-%s\\left[\\cos \\left(\\dfrac{\\pi}{%s}\\right)-\\cos \\left(\\dfrac{\\pi}{%s}\\right)\\right]=%s$.'
                        %(latex(a),latex(b),latex(e),latex(e),latex(a),latex(b),latex(e),latex(b),latex(a),latex(kq))


                        )
            if dang=='6':
                # Khai báo biến
                x=symbols('x')
                a=0
                b=randint(1,6)
                e=randint(2,20)
                while b==1 or b==5 or b==2:
                    x=symbols('x')
                    a=0
                    b=randint(1,6)
                    e=randint(2,20)
                y1=0
                y2=nsimplify(math.tan(math.pi/b))
                kq=e*(y2-y1)


                du = ['$%s$'%(latex(kq))
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(-kq)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*-2)),
                    '$%s$'%(latex(kq*3))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle\\int\\limits_{%s}^{\\dfrac{\\pi}{%s}} \\dfrac{%s}{\\cos^2x}\\text{d}x$ bằng'
                                %(latex(a),latex(b),latex(e)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle\\int\\limits_{%s}^{\\dfrac{\\pi}{%s}} \\dfrac{%s}{\\cos^2x}\\text{d}x=%s\\tan x\\bigg|_{%s}^{\\dfrac{\\pi}{%s}}=%s\\left[\\tan \\left(\\dfrac{\\pi}{%s}\\right)-\\tan \\left(%s\\right)\\right]=%s$.'
                        %(latex(a),latex(b),latex(e),latex(e),latex(a),latex(b),latex(e),latex(b),latex(a),latex(kq))


                        )
            if dang=='7':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,6)
                k=randint(1,5)
                b=a-k
                e=randint(2,20)
                while a==5 or a==1 or b==1 or b==5 or b<=0 or a==2 or b==2:
                    x=symbols('x')
                    a=randint(1,6)
                    k=randint(1,5)
                    b=a-k
                    e=randint(2,20)
                y1=nsimplify(1/(math.tan(math.pi/a)))
                y2=nsimplify(1/(math.tan(math.pi/b)))
                kq=-e*(y2-y1)


                du = ['$%s$'%(latex(kq))
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(-kq)),
                    '$%s$'%(latex(kq*2)),
                    '$%s$'%(latex(kq*-2)),
                    '$%s$'%(latex(kq*3))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle\\int\\limits_{\\dfrac{\\pi}{%s}}^{\\dfrac{\\pi}{%s}} \\dfrac{%s}{\\sin^2x}\\text{d}x$ bằng'
                                %(latex(a),latex(b),latex(e)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle\\int\\limits_{\\dfrac{\\pi}{%s}}^{\\dfrac{\\pi}{%s}}\\dfrac{%s}{\\sin^2x}\\text{d}x=-%s\\cot x\\bigg|_{\\dfrac{\\pi}{%s}}^{\\dfrac{\\pi}{%s}}=-%s\\left[\\cot \\left(\\dfrac{\\pi}{%s}\\right)-\\cot \\left(\\dfrac{\\pi}{%s}\\right)\\right]=%s$.'
                        %(latex(a),latex(b),latex(e),latex(e),latex(a),latex(b),latex(e),latex(b),latex(a),latex(kq))


                        )
            if dang=='8':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,4)
                b=randint(2,9)
                while a==0:
                    x=symbols('x')
                    a=randint(1,4)


                du = ['$%se^{%s}-%s$'%(latex(b),latex(a),latex(b))
                    ]
                da= random.choice(du)
                s = ['$%se^{%s}-%s$'%(latex(b),latex(a),latex(-b)),
                    '$%se^{%s}-%s$'%(latex(-b),latex(a),latex(b)),
                    '$%se^{%s}-%s$'%(latex(-b),latex(a),latex(-b)),
                    '$%se^{%s}-%s$'%(latex(2*b),latex(a),latex(b))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle\\int\\limits_{0}^{%s} %se^{x}\\text{d}x$ bằng'
                                %(latex(a),latex(b)
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
                loigiai=('Ta có\\\\ \n'
                        '\\hspace*{1cm} $\\displaystyle\\int\\limits_{0}^{%s} %se^{x}\\text{d}x=%se^{x}\\bigg|_{0}^{%s}=%s\\left(e^{%s}-e^{0}\\right)=%se^{%s}-%s$.'
                        %(latex(a),latex(b),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b))


                        )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('--', '+').replace('+-', '-').replace('+1x', '+x').replace('-1x', '-x').replace('+1x', '+x').replace('-1x', '-x').replace('$1x', '$x').replace('+0', '').replace('=1x', '=x').replace('=-1x', '=-x').replace('x^{1}', 'x').replace('e^{1}', 'e').replace('1e', 'e')
            return content

