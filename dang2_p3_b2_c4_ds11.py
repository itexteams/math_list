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


def bt_dang2_p3_b2_c4_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                lis=[1,4,9,16,25,36,49,64,81,100]
                a=random.choice(lis)
                c=randint(1,9)
                x0=randint(-9,9)
                b=c**2-a*x0
                tu=c-sqrt(a*x+b)
                tu1=c+sqrt(a*x+b)
                mau=x-x0

                f=tu/mau

                kq=Rational(-a,2*c)

                h1=kq 
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)=%s$$zz$ Giới hạn của hàm số tại điểm $x=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$'
                                %(latex(f),latex(x0)
                                ))

                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\underset{x \\to %s} \\lim f(x)=\\underset{x \\to %s} \\lim %s=\\underset{x \\to %s} \\lim \\dfrac{\\left(%s \\right)\\left(%s \\right)}{\\left(%s \\right)\\left(%s \\right)}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=\\underset{x \\to %s} \\lim \\dfrac{%s}{\\left(%s \\right)\\left(%s \\right)}=\\underset{x \\to %s} \\lim \\dfrac{%s(%s)}{\\left(%s \\right)\\left(%s \\right)}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=\\underset{x \\to %s} \\lim \\dfrac{%s}{%s}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=%s=%s$$zz$'

                        %(latex(x0),latex(x0),latex(f),latex(x0),latex(tu),latex(tu1),latex(mau),latex(tu1),
                        latex(x0),latex(c**2-a*x-b),latex(mau),latex(tu1),
                        latex(x0),latex(-a),latex(mau),latex(mau),latex(tu1),
                        latex(x0),latex(-a),latex(tu1),
                        latex(kq),latex(kq1)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq1))
            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                lis=[1,4,9,16,25,36,49,64,81,100]
                a=random.choice(lis)
                c=randint(1,9)
                x0=randint(-9,9)
                b=c**2-a*x0
                tu=c-sqrt(a*x+b)
                tu1=c+sqrt(a*x+b)
                mau=x-x0

                f=tu/mau

                kq=Rational(-a,2*c)

                h1=kq
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)=%s$$zz$ Giới hạn của hàm số tại điểm $x=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$'
                                %(latex(f),latex(x0)
                                ))

                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\underset{x \\to %s} \\lim f(x)=\\underset{x \\to %s} \\lim %s=\\underset{x \\to %s} \\lim \\dfrac{\\left(%s \\right)\\left(%s \\right)}{\\left(%s \\right)\\left(%s \\right)}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=\\underset{x \\to %s} \\lim \\dfrac{%s}{\\left(%s \\right)\\left(%s \\right)}=\\underset{x \\to %s} \\lim \\dfrac{%s(%s)}{\\left(%s \\right)\\left(%s \\right)}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=\\underset{x \\to %s} \\lim \\dfrac{%s}{%s}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=%s=%s$$zz$'

                        %(latex(x0),latex(x0),latex(f),latex(x0),latex(tu),latex(tu1),latex(mau),latex(tu1),
                        latex(x0),latex(c**2-a*x-b),latex(mau),latex(tu1),
                        latex(x0),latex(-a),latex(mau),latex(mau),latex(tu1),
                        latex(x0),latex(-a),latex(tu1),
                        latex(kq),latex(kq1)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq1))
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                lis=[1,4,9,16,25,36,49,64,81,100]
                a=random.choice(lis)
                c=randint(1,9)
                x0=randint(-9,9)
                b=c**2-a*x0
                tu=sqrt(a*x+b)-c
                tu1=sqrt(a*x+b)+c
                mau=x-x0

                f=mau/tu

                kq=Rational(2*c,a)

                h1=kq   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)=%s$$zz$ Giới hạn của hàm số tại điểm $x=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$'
                                %(latex(f),latex(x0)
                                ))

                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\underset{x \\to %s} \\lim f(x)=\\underset{x \\to %s} \\lim %s=\\underset{x \\to %s} \\lim \\dfrac{\\left(%s \\right)\\left(%s \\right)}{\\left(%s \\right)\\left(%s \\right)}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=\\underset{x \\to %s} \\lim \\dfrac{\\left(%s \\right)\\left(%s \\right)}{%s}=\\underset{x \\to %s} \\lim \\dfrac{\\left(%s \\right)\\left(%s \\right)}{%s(%s)}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=\\underset{x \\to %s} \\lim \\dfrac{%s}{%s}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=%s=%s$$zz$'

                        %(latex(x0),latex(x0),latex(f),latex(x0),latex(mau),latex(tu1),latex(tu),latex(tu1),
                        latex(x0),latex(mau),latex(tu1),latex(a*x+b-c**2),
                        latex(x0),latex(mau),latex(tu1),latex(a),latex(mau),
                        latex(x0),latex(tu1),latex(a),
                        latex(kq),latex(kq1)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                lis=[1,4,9,16,25,36,49,64,81,100]
                a=random.choice(lis)
                c=randint(1,9)
                x0=randint(-9,9)
                b=c**2-a*x0
                tu=sqrt(a*x+b)-c
                tu1=sqrt(a*x+b)+c
                mau=x-x0

                f=tu/mau

                kq=Rational(a,2*c)

                h1=kq
                number = Decimal(float(h1))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hàm số $f(x)=%s$$zz$ Giới hạn của hàm số tại điểm $x=%s$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$'
                                %(latex(f),latex(x0)
                                ))

                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\underset{x \\to %s} \\lim f(x)=\\underset{x \\to %s} \\lim %s=\\underset{x \\to %s} \\lim \\dfrac{\\left(%s \\right)\\left(%s \\right)}{\\left(%s \\right)\\left(%s \\right)}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=\\underset{x \\to %s} \\lim \\dfrac{%s}{\\left(%s \\right)\\left(%s \\right)}=\\underset{x \\to %s} \\lim \\dfrac{%s(%s)}{\\left(%s \\right)\\left(%s \\right)}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=\\underset{x \\to %s} \\lim \\dfrac{%s}{%s}$ \\\\ \n'
                        '\\hspace*{2.8cm} $=%s=%s$$zz$'

                        %(latex(x0),latex(x0),latex(f),latex(x0),latex(tu),latex(tu1),latex(mau),latex(tu1),
                        latex(x0),latex(a*x+b-c**2),latex(mau),latex(tu1),
                        latex(x0),latex(a),latex(mau),latex(mau),latex(tu1),
                        latex(x0),latex(a),latex(tu1),
                        latex(kq),latex(kq1)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content                   

