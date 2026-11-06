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


def bt_dang10_p3_b1_c5_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                x=symbols('x')
                a=randint(2,9)
                k=a**2
                i=randint(2,9)
                m=i**2-2
                bt1=k**x+k**(-x)

                a1=randint(2,9)
                a2=randint(-9,9)
                b1=randint(2,9)
                b2=randint(-9,9)
                while a2==0 or a2==1 or a2==-1 or b2==0 or b2==1 or b2==-1 or b1+b2*sqrt(m+2)==0:
                    a1=randint(2,9)
                    a2=randint(-9,9)
                    b1=randint(2,9)
                    b2=randint(-9,9)

                bt2=(a1+a2*(a**x)+a2*(a**(-x)))/(b1+b2*(a**x)+b2*(a**(-x)))
                bt3=(a1+a2*(a**x+a**(-x)))/(b1+b2*(a**x+a**(-x)))

                kq1=Rational(a1+a2*sqrt(m+2),b1+b2*sqrt(m+2))
                tu_so = kq1.numerator
                mau_so = kq1.denominator
                kq=abs(tu_so)+abs(mau_so)

                du = ['$%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $%s=%s$. Khi đó giá trị biểu thức $P=%s=\\dfrac{a}{b}$ với $\\dfrac{a}{b}$ là phân số tối giản và $a, b \\in \\mathbb{Z}$. Tổng $\\left|a\\right| + \\left|b\\right|$ bằng bao nhiêu?'
                                %(latex(bt1),latex(m),latex(bt2)
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
                        '\\hspace*{1cm} $%s=%s \\Leftrightarrow \\left( %s^x+%s^{-x} \\right)^2=%s \\Rightarrow %s^x+%s^{-x}=%s$ (vì $%s^x+%s^{-x}>0$).\\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $P=\\dfrac{%s+%s (%s^x+%s^{-x})}{%s+%s (%s^x+%s^{-x})}=\\dfrac{%s+%s \\cdot %s}{%s+%s \\cdot %s}=%s$. \\\\ \n'
                        'Vậy $a=%s, b=%s$ và $a+b=%s$.'
                        %(latex(bt1),latex(m),
                        latex(a),latex(a),latex(m+2),latex(a),latex(a),latex(sqrt(m+2)),
                        latex(a),latex(a),
                        latex(a1),latex(a2),latex(a),latex(a),
                        latex(b1),latex(b2),latex(a),latex(a),
                        latex(a1),latex(a2),latex(sqrt(m+2)),
                        latex(b1),latex(b2),latex(sqrt(m+2)),
                        latex(kq1),
                        latex(a1+a2*sqrt(m+2)),latex(b1+b2*sqrt(m+2)),latex(kq)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            if dang=='2':
                x=symbols('x')
                a=randint(2,9)
                k=a**2
                i=randint(2,9)
                m=i**2-2
                bt1=k**x+k**(-x)

                a1=randint(2,9)
                a2=randint(-9,9)
                b1=randint(2,9)
                b2=randint(-9,9)
                while a2==0 or a2==1 or a2==-1 or b2==0 or b2==1 or b2==-1:
                    a1=randint(2,9)
                    a2=randint(-9,9)
                    b1=randint(2,9)
                    b2=randint(-9,9)

                bt2=(a1+a2*(a**x)+a2*(a**(-x)))/(b1+b2*(a**x)+b2*(a**(-x)))
                bt3=(a1+a2*(a**x+a**(-x)))/(b1+b2*(a**x+a**(-x)))

                kq=Rational(a1+a2*sqrt(m+2),b1+b2*sqrt(m+2))

                du = ['$%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $%s=%s$. Giá trị biểu thức $P=%s$ bằng bao nhiêu?'
                                %(latex(bt1),latex(m),latex(bt2)
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
                        '\\hspace*{1cm} $%s=%s \\Leftrightarrow \\left( %s^x+%s^{-x} \\right)^2=%s \\Rightarrow %s^x+%s^{-x}=%s$ (vì $%s^x+%s^{-x}>0$).\\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $P=\\dfrac{%s+%s (%s^x+%s^{-x})}{%s+%s (%s^x+%s^{-x})}=\\dfrac{%s+%s \\cdot %s}{%s+%s \\cdot %s}=%s$.'
                        %(latex(bt1),latex(m),
                        latex(a),latex(a),latex(m+2),
                        latex(a),latex(a),latex(sqrt(m+2)),
                        latex(a),latex(a),
                        latex(a1),latex(a2),latex(a),latex(a),
                        latex(b1),latex(b2),latex(a),latex(a),
                        latex(a1),latex(a2),latex(sqrt(m+2)),
                        latex(b1),latex(b2),latex(sqrt(m+2)),
                        latex(kq)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

