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


def bt_dang11_p3_b5_c2_hh10(self):
            # Khai báo biến
            a=randint(1,15)
            i=randint(-3,3)
            if i==0:
                i=randint(-3,3)
            lis0=[30,45,60]
            g1=random.choice(lis0)
            g2=90-g1
            g3=180-g1
            g4=180-g2

            ac=a/tan(g1*pi/180)
            bc=a/sin(g1*pi/180)

            number1 = Decimal(float(a*bc*cos(g4*pi/180)))  # Số cần làm tròn
            kq1 = number1.quantize(Decimal('1E0'), rounding=ROUND_HALF_UP)

            number2 = Decimal(float(ac*bc*cos(g3*pi/180)))  # Số cần làm tròn
            kq2 = number2.quantize(Decimal('1E0'), rounding=ROUND_HALF_UP)

            number3 = Decimal(float(a*bc*cos(g2*pi/180)))  # Số cần làm tròn
            kq3 = number3.quantize(Decimal('1E0'), rounding=ROUND_HALF_UP)

            number4 = Decimal(float(ac*bc*cos(g1*pi/180)))  # Số cần làm tròn
            kq4 = number4.quantize(Decimal('1E0'), rounding=ROUND_HALF_UP)

            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)

            if dang=='4':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tam giác $ABC$ vuông tại $A$, cạnh $AB=%s$, $\\widehat{ACB}=%s^\\circ$. Tích $\\overrightarrow{BA} \\cdot \\overrightarrow{CB}$ bằng bao nhiêu? (kết quả làm tròn đến hàng đơn vị)\n'
                                %(latex(a),latex(g1)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Độ dài cạnh $AC=\\dfrac{%s}{\\tan %s^\\circ}=%s$.\\\\ \n'
                        'Cạnh $BC=\\dfrac{%s}{\\sin %s^\\circ}=%s$.\\\\ \n'
                        'Ta có \\\\ \n'
                        'Góc giữa hai vectơ $\\overrightarrow{BA}$ và $\\overrightarrow{CB}$ bằng $%s^\\circ$. \\\\ \n'
                        '$\\overrightarrow{BA} \\cdot \\overrightarrow{CB}=\\left| \\overrightarrow{BA} \\right| \\cdot \\left| \\overrightarrow{CB} \\right| \\cdot \\cos \\left( \\overrightarrow{BA},\\overrightarrow{CB} \\right)$ \\\\ \n'
                        '\\hspace*{1.6cm} $=BA \\cdot CB \\cdot \\cos \\left( \\overrightarrow{BA},\\overrightarrow{CB} \\right)$ \\\\ \n' 
                        '\\hspace*{1.6cm} $=%s \\cdot %s \\cdot \\cos %s^\\circ =%s$.' 
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1] \n'
                            '\\clip(-0.5420216198746927,-0.4891136984179073) rectangle (3.5893768418457284,4.788414659134633); \n'
                            '\\draw (0.,0.)-- (3.,0.); \n'
                            '\\draw (0.,0.)-- (0.,4.); \n'
                            '\\draw (0.,4.)-- (3.,0.); \n'
                            '\\draw (-0.5,0.16391380037015948) node[anchor=north west] {A}; \n'
                            '\\draw (3.0029848021176684,0.16391380037015948) node[anchor=north west] {B}; \n'
                            '\\draw (-0.5,4.5) node[anchor=north west] {C}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(latex(a),latex(g1),latex(ac),
                        latex(a),latex(g1),latex(bc),

                        latex(g4),
                        latex(a),latex(bc),latex(g4),
                        latex(kq1)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq1))

            if dang=='3':

                # Nội dung câu hỏi

                noidungcauhoi =  ('Cho tam giác $ABC$ vuông tại $A$, cạnh $AB=%s$, $\\widehat{ACB}=%s^\\circ$. Tích $\\overrightarrow{AC} \\cdot \\overrightarrow{CB}$ bằng bao nhiêu? (kết quả làm tròn đến hàng đơn vị)\n'
                                %(latex(a),latex(g1)
                                ))

                # Nội dung lời giải
                loigiai =('\\immini{ \n'
                        'Độ dài cạnh $AC=\\dfrac{%s}{\\tan %s^\\circ}=%s$.\\\\ \n'
                        'Cạnh $BC=\\dfrac{%s}{\\sin %s^\\circ}=%s$.\\\\ \n'
                        'Ta có \\\\ \n'
                        'Góc giữa hai vectơ $\\overrightarrow{AC}$ và $\\overrightarrow{CB}$ bằng $%s^\\circ$. \\\\ \n'
                        '$\\overrightarrow{AC} \\cdot \\overrightarrow{CB}=\\left| \\overrightarrow{AC} \\right| \\cdot \\left| \\overrightarrow{CB} \\right| \\cdot \\cos \\left( \\overrightarrow{AC},\\overrightarrow{CB} \\right)$ \\\\ \n'
                        '\\hspace*{1.6cm} $=AC \\cdot CB \\cdot \\cos \\left( \\overrightarrow{AC},\\overrightarrow{CB} \\right)$ \\\\ \n' 
                        '\\hspace*{1.6cm} $=%s \\cdot %s \\cdot \\cos %s^\\circ =%s$.' 
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1] \n'
                            '\\clip(-0.5420216198746927,-0.4891136984179073) rectangle (3.5893768418457284,4.788414659134633); \n'
                            '\\draw (0.,0.)-- (3.,0.); \n'
                            '\\draw (0.,0.)-- (0.,4.); \n'
                            '\\draw (0.,4.)-- (3.,0.); \n'
                            '\\draw (-0.5,0.16391380037015948) node[anchor=north west] {A}; \n'
                            '\\draw (3.0029848021176684,0.16391380037015948) node[anchor=north west] {B}; \n'
                            '\\draw (-0.5,4.5) node[anchor=north west] {C}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(latex(a),latex(g1),latex(ac),
                        latex(a),latex(g1),latex(bc),

                        latex(g3),
                        latex(ac),latex(bc),latex(g3),
                        latex(kq2)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq2))

            if dang=='2':

                # Nội dung câu hỏi
                noidungcauhoi =  ('Cho tam giác $ABC$ vuông tại $A$, cạnh $AB=%s$, $\\widehat{ACB}=%s^\\circ$. Tích $\\overrightarrow{BA} \\cdot \\overrightarrow{BC}$ bằng bao nhiêu? (kết quả làm tròn đến hàng đơn vị)\n'
                                %(latex(a),latex(g1)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Độ dài cạnh $AC=\\dfrac{%s}{\\tan %s^\\circ}=%s$.\\\\ \n'
                        'Cạnh $BC=\\dfrac{%s}{\\sin %s^\\circ}=%s$.\\\\ \n'
                        'Ta có \\\\ \n'
                        'Góc giữa hai vectơ $\\overrightarrow{BA}$ và $\\overrightarrow{BC}$ bằng $%s^\\circ$. \\\\ \n'
                        '$\\overrightarrow{BA} \\cdot \\overrightarrow{BC}=\\left| \\overrightarrow{BA} \\right| \\cdot \\left| \\overrightarrow{BC} \\right| \\cdot \\cos \\left( \\overrightarrow{BA},\\overrightarrow{BC} \\right)$ \\\\ \n'
                        '\\hspace*{1.6cm} $=BA \\cdot BC \\cdot \\cos \\left( \\overrightarrow{BA},\\overrightarrow{BC} \\right)$ \\\\ \n' 
                        '\\hspace*{1.6cm} $=%s \\cdot %s \\cdot \\cos %s^\\circ =%s$.' 
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1] \n'
                            '\\clip(-0.5420216198746927,-0.4891136984179073) rectangle (3.5893768418457284,4.788414659134633); \n'
                            '\\draw (0.,0.)-- (3.,0.); \n'
                            '\\draw (0.,0.)-- (0.,4.); \n'
                            '\\draw (0.,4.)-- (3.,0.); \n'
                            '\\draw (-0.5,0.16391380037015948) node[anchor=north west] {A}; \n'
                            '\\draw (3.0029848021176684,0.16391380037015948) node[anchor=north west] {B}; \n'
                            '\\draw (-0.5,4.5) node[anchor=north west] {C}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(latex(a),latex(g1),latex(ac),
                        latex(a),latex(g1),latex(bc),

                        latex(g2),
                        latex(a),latex(bc),latex(g2),
                        latex(kq3)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq3))

            if dang=='1':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tam giác $ABC$ vuông tại $A$, cạnh $AB=%s$, $\\widehat{ACB}=%s^\\circ$. Tích $\\overrightarrow{CA} \\cdot \\overrightarrow{CB}$ bằng bao nhiêu? (kết quả làm tròn đến hàng đơn vị)\n'
                                %(latex(a),latex(g1)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Độ dài cạnh $AC=\\dfrac{%s}{\\tan %s^\\circ}=%s$.\\\\ \n'
                        'Cạnh $BC=\\dfrac{%s}{\\sin %s^\\circ}=%s$.\\\\ \n'
                        'Ta có \\\\ \n'
                        'Góc giữa hai vectơ $\\overrightarrow{CA}$ và $\\overrightarrow{CB}$ bằng $%s^\\circ$. \\\\ \n'
                        '$\\overrightarrow{CA} \\cdot \\overrightarrow{CB}=\\left| \\overrightarrow{CA} \\right| \\cdot \\left| \\overrightarrow{CB} \\right| \\cdot \\cos \\left( \\overrightarrow{CA},\\overrightarrow{CB} \\right)$ \\\\ \n'
                        '\\hspace*{1.6cm} $=CA \\cdot CB \\cdot \\cos \\left( \\overrightarrow{CA},\\overrightarrow{CB} \\right)$ \\\\ \n' 
                        '\\hspace*{1.6cm} $=%s \\cdot %s \\cdot \\cos %s^\\circ =%s$.' 
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1] \n'
                            '\\clip(-0.5420216198746927,-0.4891136984179073) rectangle (3.5893768418457284,4.788414659134633); \n'
                            '\\draw (0.,0.)-- (3.,0.); \n'
                            '\\draw (0.,0.)-- (0.,4.); \n'
                            '\\draw (0.,4.)-- (3.,0.); \n'
                            '\\draw (-0.5,0.16391380037015948) node[anchor=north west] {A}; \n'
                            '\\draw (3.0029848021176684,0.16391380037015948) node[anchor=north west] {B}; \n'
                            '\\draw (-0.5,4.5) node[anchor=north west] {C}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(latex(a),latex(g1),latex(ac),
                        latex(a),latex(g1),latex(bc),
                        latex(g1),
                        latex(ac),latex(bc),latex(g1),
                        latex(kq4)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq4))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

