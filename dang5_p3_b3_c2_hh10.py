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


def bt_dang5_p3_b3_c2_hh10(self):
            # Khai báo biến
            lis1=[1,2,3,4,5,6,7,8,9,10]
            a=random.choice(lis1)
            b=random.choice(lis1)
            while b<=a:
                a=random.choice(lis1)
                b=random.choice(lis1)
            lis2=['A','B','C','D','E','F','G','H','K','M','N','P','Q']
            d1=random.choice(lis2)
            lis2.remove(d1)
            d2=random.choice(lis2)
            lis2.remove(d2)
            d3=random.choice(lis2)
            h1=a/b
            number = Decimal(float(h1))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq1=str(kq).replace('.', ',')

            h2=(b-a)/a
            number2 = Decimal(float(h2))  # Số cần làm tròn
            kq2 = number2.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq22=str(kq2).replace('.', ',')

            h3=b/(b-a)
            number3 = Decimal(float(h3))  # Số cần làm tròn
            kq3 = number3.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq33=str(kq3).replace('.', ',')

            h4=a/(b-a)
            number4 = Decimal(float(h4))  # Số cần làm tròn
            kq4 = number4.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq44=str(kq4).replace('.', ',')

            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho các điểm $%s, %s, %s$ như hình vẽ sau \\\\ \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.99]   \n'
                                        '\\clip(-0.9199699165200613,-0.8106969377167468) rectangle (%s.577215034044792,0.40817055424625076); \n'
                                        '\\draw (0.,0.)-- (%s.,0.); \n'
                                        '\\draw (0,0) node[anchor=north] {$%s$}; \n'
                                        '\\draw (%s,0) node[anchor=north] {$%s$}; \n'
                                        '\\draw (%s,0) node[anchor=north] {$%s$}; \n'
                                        '\\begin{scriptsize} \n'
                                            '\\foreach \\x in {0,1,...,%s} \\fill (\\x,0) circle (0.99pt); \n'
                                        '\\end{scriptsize} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Biết $\\overrightarrow{%s%s}=k \\overrightarrow{%s%s}$. Giá trị của $k$ bằng bao nhiêu?'

                                %(str(d1),str(d3),str(d2),
                                    latex(b),
                                    latex(b),
                                    str(d1),
                                    latex(b),
                                    str(d2),
                                    latex(a),
                                    str(d3),
                                    latex(b),
                                    str(d1),str(d3),str(d1),str(d2)
                                    )
                                )

                # Nội dung lời giải
                loigiai=('Từ hình vẽ ta có \\\\ \n'
                        '$%s%s=%s, %s%s=%s$. \\\\\n'
                        'Hai vectơ $\\overrightarrow{%s%s}$ và $\\overrightarrow{%s%s}$ cùng hướng. \\\\ \n'
                        'Do đó $\\dfrac{\\overrightarrow{%s%s}}{\\overrightarrow{%s%s}}=%s \\Leftrightarrow \\overrightarrow{%s%s}=%s \\overrightarrow{%s%s}$. \\\\'
                        'Suy ra $k=%s \\approx %s$.'
                        %(str(d1),str(d3),latex(a),str(d1),str(d2),latex(b),
                        str(d1),str(d3),str(d1),str(d2),
                        str(d1),str(d3),str(d1),str(d2),latex(Rational(a,b)),str(d1),str(d3),latex(Rational(a,b)),str(d1),str(d2),
                        latex(Rational(a,b)),str(kq1)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq1))
            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho các điểm $%s, %s, %s$ như hình vẽ sau \\\\ \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.99]   \n'
                                        '\\clip(-0.9199699165200613,-0.8106969377167468) rectangle (%s.577215034044792,0.40817055424625076); \n'
                                        '\\draw (0.,0.)-- (%s.,0.); \n'
                                        '\\draw (0,0) node[anchor=north] {$%s$}; \n'
                                        '\\draw (%s,0) node[anchor=north] {$%s$}; \n'
                                        '\\draw (%s,0) node[anchor=north] {$%s$}; \n'
                                        '\\begin{scriptsize} \n'
                                            '\\foreach \\x in {0,1,...,%s} \\fill (\\x,0) circle (0.99pt); \n'
                                        '\\end{scriptsize} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Biết $\\overrightarrow{%s%s}=m \\overrightarrow{%s%s}$. Giá trị của $m$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'

                                %(str(d1),str(d3),str(d2),
                                    latex(b),
                                    latex(b),
                                    str(d1),
                                    latex(b),
                                    str(d2),
                                    latex(a),
                                    str(d3),
                                    latex(b),
                                    str(d3),str(d2),str(d3),str(d1)
                                    )
                                )


                # Nội dung lời giải
                loigiai=('Từ hình vẽ ta có \\\\ \n'
                        '$%s%s=%s, %s%s=%s$. \\\\\n'
                        'Hai vectơ $\\overrightarrow{%s%s}$ và $\\overrightarrow{%s%s}$ ngược hướng. \\\\ \n'
                        'Do đó $\\dfrac{\\overrightarrow{%s%s}}{\\overrightarrow{%s%s}}=-\\dfrac{%s}{%s} \\Leftrightarrow \\overrightarrow{%s%s}=-%s \\overrightarrow{%s%s}$.\\\\'
                        'Suy ra $m=%s \\approx %s$.'

                        %(str(d3),str(d2),latex(b-a),str(d3),str(d1),latex(a),
                        str(d3),str(d1),str(d3),str(d1),
                        str(d3),str(d2),str(d3),str(d1),latex(b-a),latex(a),str(d3),str(d2),latex(Rational(b-a,a)),str(d3),str(d1),
                        latex(Rational(b-a,a)),str(kq22)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq22))
            if dang=='3':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho các điểm $%s, %s, %s$ như hình vẽ sau \\\\ \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.99]   \n'
                                        '\\clip(-0.9199699165200613,-0.8106969377167468) rectangle (%s.577215034044792,0.40817055424625076); \n'
                                        '\\draw (0.,0.)-- (%s.,0.); \n'
                                        '\\draw (0,0) node[anchor=north] {$%s$}; \n'
                                        '\\draw (%s,0) node[anchor=north] {$%s$}; \n'
                                        '\\draw (%s,0) node[anchor=north] {$%s$}; \n'
                                        '\\begin{scriptsize} \n'
                                            '\\foreach \\x in {0,1,...,%s} \\fill (\\x,0) circle (0.99pt); \n'
                                        '\\end{scriptsize} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Biết $\\overrightarrow{%s%s}=a \\overrightarrow{%s%s}$. Giá trị của $a$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'

                                %(str(d1),str(d3),str(d2),
                                    latex(b),
                                    latex(b),
                                    str(d1),
                                    latex(b),
                                    str(d2),
                                    latex(a),
                                    str(d3),
                                    latex(b),
                                    str(d1),str(d2),str(d2),str(d3)
                                    )
                                )

                # Nội dung lời giải
                loigiai=('Từ hình vẽ ta có \\\\ \n'
                        '$%s%s=%s, %s%s=%s$. \\\\\n'
                        'Hai vectơ $\\overrightarrow{%s%s}$ và $\\overrightarrow{%s%s}$ ngược hướng. \\\\ \n'
                        'Do đó $\\dfrac{\\overrightarrow{%s%s}}{\\overrightarrow{%s%s}}=-\\dfrac{%s}{%s} \\Leftrightarrow \\overrightarrow{%s%s}=-%s \\overrightarrow{%s%s}$.'
                        'Suy ra $a=%s \\approx %s$.'

                        %(str(d1),str(d2),latex(b),str(d2),str(d3),latex(b-a),
                        str(d1),str(d2),str(d2),str(d3),
                        str(d1),str(d2),str(d2),str(d3),latex(b),latex(b-a),str(d1),str(d2),latex(Rational(b,b-a)),str(d2),str(d3),
                        latex(Rational(b,b-a)),str(kq33)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq33))
            if dang=='4':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho các điểm $%s, %s, %s$ như hình vẽ sau \\\\ \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.99]   \n'
                                        '\\clip(-0.9199699165200613,-0.8106969377167468) rectangle (%s.577215034044792,0.40817055424625076); \n'
                                        '\\draw (0.,0.)-- (%s.,0.); \n'
                                        '\\draw (0,0) node[anchor=north] {$%s$}; \n'
                                        '\\draw (%s,0) node[anchor=north] {$%s$}; \n'
                                        '\\draw (%s,0) node[anchor=north] {$%s$}; \n'
                                        '\\begin{scriptsize} \n'
                                            '\\foreach \\x in {0,1,...,%s} \\fill (\\x,0) circle (0.99pt); \n'
                                        '\\end{scriptsize} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Biết $\\overrightarrow{%s%s}=a \\overrightarrow{%s%s}$. Giá trị của $a$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'

                                %(str(d1),str(d3),str(d2),
                                    latex(b),
                                    latex(b),
                                    str(d1),
                                    latex(b),
                                    str(d2),
                                    latex(a),
                                    str(d3),
                                    latex(b),
                                    str(d1),str(d3),str(d3),str(d2)
                                    )
                                )

                # Nội dung lời giải
                loigiai=('Từ hình vẽ ta có \\\\ \n'
                        '$%s%s=%s, %s%s=%s$. \\\\\n'
                        'Hai vectơ $\\overrightarrow{%s%s}$ và $\\overrightarrow{%s%s}$ cùng hướng. \\\\ \n'
                        'Do đó $\\dfrac{\\overrightarrow{%s%s}}{\\overrightarrow{%s%s}}=\\dfrac{%s}{%s} \\Leftrightarrow \\overrightarrow{%s%s}=-%s \\overrightarrow{%s%s}$.\\\\'
                        'Suy ra $a=%s \\approx %s$.'
                        %(str(d1),str(d3),latex(a),str(d3),str(d2),latex(b-a),
                        str(d1),str(d3),str(d3),str(d2),
                        str(d1),str(d3),str(d3),str(d2),latex(a),latex(b-a),str(d1),str(d3),latex(Rational(a,b-a)),str(d3),str(d2),
                        latex(Rational(a,b-a)),str(kq44)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq44))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('=-1','=-').replace('=1','=')
            return content

