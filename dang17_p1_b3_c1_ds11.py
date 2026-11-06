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


def bt_dang17_p1_b3_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5']
            dang=random.choice(lisdang)


            if dang=='1':
                # Khai báo biến
                x=symbols('x')

                a=randint(-9,9)
                b=Rational(1-2,1*a)
                c=Rational(1,a)
                while a==1 or a==0:
                    a=randint(2,9)
                    b=Rational(1-2,1*a)
                    c=Rational(1,a)

                du = ['$\\left(%s\\pi;0\\right)$'%(latex(c))
                    ]
                da= random.choice(du)
                s = ['$\\left(%s\\pi;1\\right)$'%(latex(c)),
                    '$\\left(%s\\pi;\\dfrac{\\sqrt{1}}{2}\\right)$'%(latex(c+1)),
                    '$\\left(%s\\pi;\\dfrac{\\sqrt{3}}{2}\\right)$'%(latex(c-1)),
                    '$\\left(%s\\pi;\\dfrac{1}{2}\\right)$'%(latex(c)),
                    '$\\left(%s\\pi;\\dfrac{\\sqrt{2}}{2}\\right)$'%(latex(c)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Đồ thị của hàm số $y=\\sin(x+%s\\pi)$ đi qua điểm nào sau đây?'%(latex(b)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Với $x=%s\\pi \\Rightarrow y=\\sin(%s\\pi+%s\\pi)=\\sin0=0$.\\\\ \n'
                        'Vậy đồ thị hàm số đi qua điểm $\\left(%s\\pi;0\\right)$. \\\\ \n'%(latex(c),latex(c),latex(b),latex(c))

                        )

            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                S=(2,3,4,6,-2,-3,-4,-6)
                d=random.choice(S)
                a=randint(-9,9)
                b=Rational(a-d,d*a)
                c=Rational(1,a)

                while a==0 or a==d:
                    S=(2,3,4,6,-2,-3,-4,-6)
                    d=random.choice(S)
                    a=randint(2,9)
                    b=Rational(a-d,d*a)
                    c=Rational(1,a)
                x0=sin(math.pi*(b+c))

                du = ['$\\left(%s\\pi;%s\\right)$'%(latex(c),latex(x0))
                    ]
                da= random.choice(du)
                s = [
                    '$\\left(%s\\pi;%s\\right)$'%(latex(-c),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(c-1),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(c+1),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(Rational(2*c+1,2)),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(Rational(2*c-1,2)),latex(x0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Đồ thị của hàm số $y=\\sin(x+%s\\pi)$ đi qua điểm nào sau đây?'%(latex(b)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Với $x=%s\\pi \\Rightarrow y=\\sin(%s\\pi+%s\\pi)=\\sin(%s\\pi)=%s$.\\\\ \n'
                        'Vậy đồ thị hàm số đi qua điểm $\\left(%s\\pi;%s\\right)$. \\\\ \n'%(latex(c),latex(c),latex(b),latex(c+b),latex(x0),latex(c),latex(x0))
                        )

            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                S=(2,3,4,6,-2,-3,-4,-6)
                d=random.choice(S)
                a=randint(-9,9)
                b=Rational(a-d,d*a)
                c=Rational(1,a)

                while a==0 or a==d:
                    S=(2,3,4,6,-2,-3,-4,-6)
                    d=random.choice(S)
                    a=randint(2,9)
                    b=Rational(a-d,d*a)
                    c=Rational(1,a)
                x0=cos(math.pi*(b+c))

                du = ['$\\left(%s\\pi;%s\\right)$'%(latex(c),latex(x0))
                    ]
                da= random.choice(du)
                s = ['$\\left(%s\\pi;%s\\right)$'%(latex(c+1),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(c-1),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(Rational(2*c+1,2)),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(Rational(2*c-1,2)),latex(x0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Đồ thị của hàm số $y=\\cos(x+%s\\pi)$ đi qua điểm nào sau đây?'%(latex(b)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Với $x=%s\\pi \\Rightarrow y=\\cos(%s\\pi+%s\\pi)=\\cos(%s\\pi)=%s$.\\\\ \n'
                        'Vậy đồ thị hàm số đi qua điểm $\\left(%s\\pi;%s\\right)$. \\\\ \n'%(latex(c),latex(c),latex(b),latex(c+b),latex(x0),latex(c),latex(x0))

                        )

            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                S=(2,3,4,6,-2,-3,-4,-6)
                d=random.choice(S)
                a=randint(-9,9)
                b=Rational(a-d,d*a)
                c=Rational(1,a)

                while a==0 or b+c==1/2 or b+c==-1/2 or a==d:
                    S=(2,3,4,6,-2,-3,-4,-6)
                    d=random.choice(S)
                    a=randint(2,9)
                    b=Rational(a-d,d*a)
                    c=Rational(1,a)
                x0=tan(math.pi*(b+c))

                du = ['$\\left(%s\\pi;%s\\right)$'%(latex(c),latex(x0))
                    ]
                da= random.choice(du)
                s = ['$\\left(%s\\pi;%s\\right)$'%(latex(-c),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(c),latex(-x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(Rational(2*c+1,2)),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(Rational(2*c-1,2)),latex(x0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Đồ thị của hàm số $y=\\tan(x+%s\\pi)$ đi qua điểm nào sau đây?'%(latex(b)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Với $x=%s\\pi \\Rightarrow y=\\tan(%s\\pi+%s\\pi)=\\tan(%s\\pi)=%s$.\\\\ \n'
                        'Vậy đồ thị hàm số đi qua điểm $\\left(%s\\pi;%s\\right)$. \\\\ \n'%(latex(c),latex(c),latex(b),latex(c+b),latex(x0),latex(c),latex(x0))

                        )
            if dang=='5':
                # Khai báo biến
                x=symbols('x')
                S=(2,3,4,6,-2,-3,-4,-6)
                d=random.choice(S)
                a=randint(-9,9)
                b=Rational(a-d,d*a)
                c=Rational(1,a)

                while a==0 or a==d:
                    S=(2,3,4,6,-2,-3,-4,-6)
                    d=random.choice(S)
                    a=randint(2,9)
                    b=Rational(a-d,d*a)
                    c=Rational(1,a)
                x0=cot(math.pi*(b+c))

                du = ['$\\left(%s\\pi;%s\\right)$'%(latex(c),latex(x0))
                    ]
                da= random.choice(du)
                s = ['$\\left(%s\\pi;%s\\right)$'%(latex(-c),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(c),latex(-x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(Rational(2*c+1,2)),latex(x0)),
                    '$\\left(%s\\pi;%s\\right)$'%(latex(Rational(2*c-1,2)),latex(x0)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Đồ thị của hàm số $y=\\cot(x+%s\\pi)$ đi qua điểm nào sau đây?'%(latex(b)))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Với $x=%s\\pi \\Rightarrow y=\\cot(%s\\pi+%s\\pi)=\\cot(%s\\pi)=%s$.\\\\ \n'
                        'Vậy đồ thị hàm số đi qua điểm $\\left(%s\\pi;%s\\right)$. \\\\ \n'%(latex(c),latex(c),latex(b),latex(c+b),latex(x0),latex(c),latex(x0))
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
                '\\end{ex}\n \\end{minipage} \n\n ').replace('1.73205080756888', '\\sqrt{3}').replace('\\frac', '\\dfrac').replace('6.12323399573677 \\cdot 10^{-17}', '0').replace('+-', '-').replace('--', '+').replace('0\\pi', '0').replace('1\\pi', '\\pi').replace('.0', '').replace('+0', '').replace('0.707106781186548', '\\dfrac{\\sqrt{2}}{2}').replace('0.866025403784439', '\\dfrac{\\sqrt{3}}{2}').replace('0.707106781186547', '\\dfrac{\\sqrt{2}}{2}').replace('0.5', '\\dfrac{1}{2}').replace('\\dfrac{1}{2}77350269189626', '\\dfrac{\\sqrt{3}}{3}')

            return content

