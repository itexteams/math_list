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


def bt_dang45_p1_b4_c5_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='4':
                x=symbols('x')
                lis=[2,3,4,5]
                i=random.choice(lis)
                lis.remove(i)
                k=random.choice(lis)
                m=randint(2,9)
                a=m**i
                b=Rational(1,m**k)

                kq=-Rational(k,i)

                lis1=[1,2,3,4,5,6,7,8,9]
                a1=random.choice(lis1)
                lis1.remove(a1)
                b1=random.choice(lis1)
                f=a1*x+b1
                x0=Rational(kq-b1,a1)

                h1=x0
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                du = ['$\\left(-\\infty;%s \\right]$'%(latex(x0)),
                    ]
                da= random.choice(du)
                s = ['$\\left[%s;+\\infty \\right)$'%(latex(x0)),

                    '$\\left(-\\infty;%s \\right)$'%(latex(x0)),
                    '$\\left(%s;+\\infty \\right)$'%(latex(x0)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Bất phương trình $%s^{%s} \\le %s$ có tập nghiệm là'
                                %(latex(a),latex(f),latex(b)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $%s^{%s} \\le %s \\Leftrightarrow %s \\le \\log_{%s} %s \\Leftrightarrow %s \\le %s \\Leftrightarrow x \\le %s$. \\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s \\right]$.'
                        %(latex(a),latex(f),latex(b),latex(f),latex(a),latex(b),latex(f),latex(kq),latex(x0),
                        latex(x0)
                        ))

            if dang=='3':
                x=symbols('x')
                lis=[2,3,4,5]
                i=random.choice(lis)
                lis.remove(i)
                k=random.choice(lis)
                m=randint(2,9)
                a=m**i
                b=Rational(1,m**k)

                kq=-Rational(k,i)

                lis1=[1,2,3,4,5,6,7,8,9]
                a1=random.choice(lis1)
                lis1.remove(a1)
                b1=random.choice(lis1)
                f=a1*x+b1
                x0=Rational(kq-b1,a1)

                h1=x0
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                du = ['$\\left(-\\infty;%s \\right)$'%(latex(x0)),
                    ]
                da= random.choice(du)
                s = ['$\\left[%s;+\\infty \\right)$'%(latex(x0)),

                    '$\\left(-\\infty;%s \\right]$'%(latex(x0)),
                    '$\\left(%s;+\\infty \\right)$'%(latex(x0)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Bất phương trình $%s^{%s}<%s$ có tập nghiệm là'
                                %(latex(a),latex(f),latex(b)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $%s^{%s}<%s \\Leftrightarrow %s<\\log_{%s} %s \\Leftrightarrow %s<%s \\Leftrightarrow x<%s$. \\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(-\\infty;%s \\right)$.'
                        %(latex(a),latex(f),latex(b),latex(f),latex(a),latex(b),latex(f),latex(kq),latex(x0),
                        latex(x0)
                        ))

            if dang=='2':
                x=symbols('x')
                lis=[2,3,4,5]
                i=random.choice(lis)
                lis.remove(i)
                k=random.choice(lis)
                m=randint(2,9)
                a=m**i
                b=Rational(1,m**k)

                kq=-Rational(k,i)

                lis1=[1,2,3,4,5,6,7,8,9]
                a1=random.choice(lis1)
                lis1.remove(a1)
                b1=random.choice(lis1)
                f=a1*x+b1
                x0=Rational(kq-b1,a1)

                h1=x0
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                du = ['$\\left[%s;+\\infty \\right)$'%(latex(x0)),
                    ]
                da= random.choice(du)
                s = ['$\\left(%s;+\\infty \\right)$'%(latex(x0)),
                    '$\\left(-\\infty;%s \\right)$'%(latex(x0)),
                    '$\\left(-\\infty;%s \\right]$'%(latex(x0)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Bất phương trình $%s^{%s} \\ge %s$ có tập nghiệm là'
                                %(latex(a),latex(f),latex(b)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $%s^{%s} \\ge %s \\Leftrightarrow %s \\ge \\log_{%s} %s \\Leftrightarrow %s \\ge %s \\Leftrightarrow x \\ge %s$. \\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left[%s;+\\infty \\right)$.'
                        %(latex(a),latex(f),latex(b),latex(f),latex(a),latex(b),latex(f),latex(kq),latex(x0),
                        latex(x0)
                        ))

            if dang=='1':
                x=symbols('x')
                lis=[2,3,4,5]
                i=random.choice(lis)
                lis.remove(i)
                k=random.choice(lis)
                m=randint(2,9)
                a=m**i
                b=Rational(1,m**k)

                kq=-Rational(k,i)

                lis1=[1,2,3,4,5,6,7,8,9]
                a1=random.choice(lis1)
                lis1.remove(a1)
                b1=random.choice(lis1)
                f=a1*x+b1
                x0=Rational(kq-b1,a1)

                h1=x0
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                du = ['$\\left(%s;+\\infty \\right)$'%(latex(x0)),
                    ]
                da= random.choice(du)
                s = ['$\\left[%s;+\\infty \\right)$'%(latex(x0)),
                    '$\\left(-\\infty;%s \\right)$'%(latex(x0)),
                    '$\\left(-\\infty;%s \\right]$'%(latex(x0)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Bất phương trình $%s^{%s}>%s$ có tập nghiệm là'
                                %(latex(a),latex(f),latex(b)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $%s^{%s}>%s \\Leftrightarrow %s>\\log_{%s} %s \\Leftrightarrow %s>%s \\Leftrightarrow x>%s$. \\\\ \n'
                        'Vậy bất phương trình có tập nghiệm là $\\left(%s;+\\infty \\right)$.'
                        %(latex(a),latex(f),latex(b),latex(f),latex(a),latex(b),latex(f),latex(kq),latex(x0),
                        latex(x0)
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

