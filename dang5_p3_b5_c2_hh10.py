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


def bt_dang5_p3_b5_c2_hh10(self):
            # Khai báo biến
            i=randint(-3,3)
            if i==0:
                i=randint(-3,3)

            lis0=['A','B','C','D','E','H','P','Q','M','N']
            d1=random.choice(lis0)
            lis0.remove(d1)
            d2=random.choice(lis0)
            lis0.remove(d2)
            d3=random.choice(lis0)
            lis0.remove(d3)
            d4=random.choice(lis0)

            lis1=[0,30,45,60,120,135,150,180]
            g11=random.choice(lis1)
            lis1.remove(g11)
            g12=random.choice(lis1)
            lis1.remove(g12)
            g13=random.choice(lis1)

            lis2=[90,30,45,60,120,135,150,180]
            g21=random.choice(lis2)
            lis2.remove(g21)
            g22=random.choice(lis2)
            lis2.remove(g22)
            g23=random.choice(lis2)

            lis3=[90,30,45,60,120,135,150,0]
            g31=random.choice(lis3)
            lis3.remove(g31)
            g32=random.choice(lis3)
            lis3.remove(g32)
            g33=random.choice(lis3)

            lis4=[90,30,180,60,120,135,150,0]
            g41=random.choice(lis4)
            lis4.remove(g41)
            g42=random.choice(lis4)
            lis4.remove(g42)
            g43=random.choice(lis4)

            lis5=[90,30,180,60,120,0,150,45]
            g51=random.choice(lis5)
            lis5.remove(g51)
            g52=random.choice(lis5)
            lis5.remove(g52)
            g53=random.choice(lis5)


            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='1':

                # Nội dung câu hỏi
                noidungcauhoi =('Cho hình vuông $%s%s%s%s$ có tâm $O$. Số đo góc giữa hai vectơ $\\left( \\overrightarrow{O%s} ,\\overrightarrow{%s%s} \\right)$ bằng bao nhiêu độ?\n'
                                %(str(d1),str(d2),str(d3),str(d4),str(d1),str(d2),str(d3)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{O%s} ,\\overrightarrow{%s%s} \\right)=\\left( \\overrightarrow{%sO} ,\\overrightarrow{%s%s} \\right)=180^\\circ-45^\\circ=135^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-0.8380232407345299,-0.6189929273354552) rectangle (4.7125915027899605,4.709102739611209); \n'
                            '\\draw (0.,4.)-- (4.,4.); \n'
                            '\\draw (4.,4.)-- (4.,0.); \n'
                            '\\draw (4.,0.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (4.,0.); \n'
                            '\\draw (4.,4.)-- (0.,0.); \n'
                            '\\draw (-0.3435364038949316,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.756293811345413,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.810181531873924,4.562961953823491) node[anchor=north west] {%s}; \n'
                            '\\draw (-0.30644989113196175,4.624772808428441) node[anchor=north west] {%s}; \n'
                            '\\draw (1.7187408746462304,2.68391197383302) node[anchor=north west] {O}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(str(d1),str(d2),str(d3),str(d3),str(d2),str(d3),
                        str(d1),str(d2),str(d3),str(d4),
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(135))


            if dang=='2':

                # Nội dung câu hỏi
                noidungcauhoi =('Cho hình vuông $%s%s%s%s$ có tâm $O$. Số đo góc giữa hai vectơ $\\left( \\overrightarrow{O%s} ,\\overrightarrow{%s%s} \\right)$ bằng bao nhiêu độ?\n'
                                %(str(d1),str(d2),str(d3),str(d4),str(d2),str(d4),str(d1)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{O%s} ,\\overrightarrow{%s%s} \\right)=\\left( \\overrightarrow{%sO} ,\\overrightarrow{%s%s} \\right)=\\widehat{%s%sO}=45^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-0.8380232407345299,-0.6189929273354552) rectangle (4.7125915027899605,4.709102739611209); \n'
                            '\\draw (0.,4.)-- (4.,4.); \n'
                            '\\draw (4.,4.)-- (4.,0.); \n'
                            '\\draw (4.,0.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (4.,0.); \n'
                            '\\draw (4.,4.)-- (0.,0.); \n'
                            '\\draw (-0.3435364038949316,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.756293811345413,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.810181531873924,4.562961953823491) node[anchor=north west] {%s}; \n'
                            '\\draw (-0.30644989113196175,4.624772808428441) node[anchor=north west] {%s}; \n'
                            '\\draw (1.7187408746462304,2.68391197383302) node[anchor=north west] {O}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(str(d2),str(d4),str(d1),str(d4),str(d4),str(d1),str(d1),str(d4),
                        str(d1),str(d2),str(d3),str(d4),
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(45))

            if dang=='3':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình vuông $%s%s%s%s$ có tâm $O$. Số đo góc giữa hai vectơ $\\left( \\overrightarrow{O%s} ,\\overrightarrow{O%s} \\right)$ bằng bao nhiêu độ?\n'
                                %(str(d1),str(d2),str(d3),str(d4),str(d1),str(d4),
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{O%s} ,\\overrightarrow{O%s} \\right)=\\widehat{%sO%s}=90^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-0.8380232407345299,-0.6189929273354552) rectangle (4.7125915027899605,4.709102739611209); \n'
                            '\\draw (0.,4.)-- (4.,4.); \n'
                            '\\draw (4.,4.)-- (4.,0.); \n'
                            '\\draw (4.,0.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (4.,0.); \n'
                            '\\draw (4.,4.)-- (0.,0.); \n'
                            '\\draw (-0.3435364038949316,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.756293811345413,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.810181531873924,4.562961953823491) node[anchor=north west] {%s}; \n'
                            '\\draw (-0.30644989113196175,4.624772808428441) node[anchor=north west] {%s}; \n'
                            '\\draw (1.7187408746462304,2.68391197383302) node[anchor=north west] {O}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(str(d1),str(d4),str(d1),str(d4),
                        str(d1),str(d2),str(d3),str(d4),
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(90))

            if dang=='4':

                # Nội dung câu hỏi

                noidungcauhoi = ('Cho hình vuông $%s%s%s%s$ có tâm $O$. Số đo góc giữa hai vectơ $\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)$ bằng bao nhiêu độ?\n'
                                %(str(d1),str(d2),str(d3),str(d4),str(d2),str(d4),str(d4),str(d3)
                                ))

                # Nội dung lời giải
                loigiai =('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)=180^\\circ-45^\\circ =135^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-0.8380232407345299,-0.6189929273354552) rectangle (4.7125915027899605,4.709102739611209); \n'
                            '\\draw (0.,4.)-- (4.,4.); \n'
                            '\\draw (4.,4.)-- (4.,0.); \n'
                            '\\draw (4.,0.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (4.,0.); \n'
                            '\\draw (4.,4.)-- (0.,0.); \n'
                            '\\draw (-0.3435364038949316,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.756293811345413,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.810181531873924,4.562961953823491) node[anchor=north west] {%s}; \n'
                            '\\draw (-0.30644989113196175,4.624772808428441) node[anchor=north west] {%s}; \n'
                            '\\draw (1.7187408746462304,2.68391197383302) node[anchor=north west] {O}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(str(d2),str(d4),str(d4),str(d3),
                        str(d1),str(d2),str(d3),str(d4),
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(135))

            if dang=='5':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình vuông $%s%s%s%s$ có tâm $O$. Số đo góc giữa hai vectơ $\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)$ bằng bao nhiêu độ?\n'
                                %(str(d1),str(d2),str(d3),str(d4),str(d4),str(d2),str(d4),str(d3)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)=\\widehat{%s%s%s}=45^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-0.8380232407345299,-0.6189929273354552) rectangle (4.7125915027899605,4.709102739611209); \n'
                            '\\draw (0.,4.)-- (4.,4.); \n'
                            '\\draw (4.,4.)-- (4.,0.); \n'
                            '\\draw (4.,0.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (4.,0.); \n'
                            '\\draw (4.,4.)-- (0.,0.); \n'
                            '\\draw (-0.3435364038949316,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.756293811345413,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.810181531873924,4.562961953823491) node[anchor=north west] {%s}; \n'
                            '\\draw (-0.30644989113196175,4.624772808428441) node[anchor=north west] {%s}; \n'
                            '\\draw (1.7187408746462304,2.68391197383302) node[anchor=north west] {O}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(str(d4),str(d2),str(d4),str(d3),str(d2),str(d4),str(d3),
                        str(d1),str(d2),str(d3),str(d4),
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(45))

            if dang=='6':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình vuông $%s%s%s%s$ có tâm $O$. Số đo góc giữa hai vectơ $\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)$ bằng bao nhiêu độ?\n'
                                %(str(d1),str(d2),str(d3),str(d4),str(d1),str(d4),str(d3),str(d2)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)=180^\\circ$. Hai vectơ ngược hướng. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-0.8380232407345299,-0.6189929273354552) rectangle (4.7125915027899605,4.709102739611209); \n'
                            '\\draw (0.,4.)-- (4.,4.); \n'
                            '\\draw (4.,4.)-- (4.,0.); \n'
                            '\\draw (4.,0.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (4.,0.); \n'
                            '\\draw (4.,4.)-- (0.,0.); \n'
                            '\\draw (-0.3435364038949316,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.756293811345413,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.810181531873924,4.562961953823491) node[anchor=north west] {%s}; \n'
                            '\\draw (-0.30644989113196175,4.624772808428441) node[anchor=north west] {%s}; \n'
                            '\\draw (1.7187408746462304,2.68391197383302) node[anchor=north west] {O}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(str(d1),str(d4),str(d3),str(d2),
                        str(d1),str(d2),str(d3),str(d4),
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(180))

            if dang=='7':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình vuông $%s%s%s%s$ có tâm $O$. Số đo góc giữa hai vectơ $\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)$ bằng bao nhiêu độ?\n'
                                %(str(d1),str(d2),str(d3),str(d4),str(d1),str(d2),str(d4),str(d3)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)=0^\\circ$. Hai vectơ cùng hướng. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-0.8380232407345299,-0.6189929273354552) rectangle (4.7125915027899605,4.709102739611209); \n'
                            '\\draw (0.,4.)-- (4.,4.); \n'
                            '\\draw (4.,4.)-- (4.,0.); \n'
                            '\\draw (4.,0.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (4.,0.); \n'
                            '\\draw (4.,4.)-- (0.,0.); \n'
                            '\\draw (-0.3435364038949316,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.756293811345413,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.810181531873924,4.562961953823491) node[anchor=north west] {%s}; \n'
                            '\\draw (-0.30644989113196175,4.624772808428441) node[anchor=north west] {%s}; \n'
                            '\\draw (1.7187408746462304,2.68391197383302) node[anchor=north west] {O}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(str(d1),str(d2),str(d4),str(d3),
                        str(d1),str(d2),str(d3),str(d4),
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(0))

            if dang=='8':

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình vuông $%s%s%s%s$ có tâm $O$. Số đo góc giữa hai vectơ $\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)$ bằng bao nhiêu độ?\n'
                                %(str(d1),str(d2),str(d3),str(d4),str(d1),str(d2),str(d1),str(d4)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'
                        'Ta có \\\\ \n'
                        '$\\left( \\overrightarrow{%s%s} ,\\overrightarrow{%s%s} \\right)=\\widehat{%s%s%s}=90^\\circ$. \\\\ \n'
                        '} \n'
                        '{ \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                            '\\clip(-0.8380232407345299,-0.6189929273354552) rectangle (4.7125915027899605,4.709102739611209); \n'
                            '\\draw (0.,4.)-- (4.,4.); \n'
                            '\\draw (4.,4.)-- (4.,0.); \n'
                            '\\draw (4.,0.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (0.,0.); \n'
                            '\\draw (0.,4.)-- (4.,0.); \n'
                            '\\draw (4.,4.)-- (0.,0.); \n'
                            '\\draw (-0.3435364038949316,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.756293811345413,0) node[anchor=north west] {%s}; \n'
                            '\\draw (3.810181531873924,4.562961953823491) node[anchor=north west] {%s}; \n'
                            '\\draw (-0.30644989113196175,4.624772808428441) node[anchor=north west] {%s}; \n'
                            '\\draw (1.7187408746462304,2.68391197383302) node[anchor=north west] {O}; \n'
                        '\\end{tikzpicture} \n'
                        '} \n'

                        %(str(d1),str(d2),str(d1),str(d4),str(d2),str(d1),str(d4),
                        str(d1),str(d2),str(d3),str(d4),
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(90))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

