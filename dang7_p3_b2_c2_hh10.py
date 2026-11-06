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


def bt_dang7_p3_b2_c2_hh10(self):
            lisdang=['1','2','3']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến

                a = randint(20,50)
                b = randint(5,19)
                x0 = sqrt(a**2+b**2)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = (
                                'Một dòng sông chảy từ phía Tây sang Đông với vận tốc $%s$ (km/h) so với bờ, có một chiếc Ca nô chuyển động từ phía Bắc xuống phía Nam với vận tốc $%s$ (km/h) so với dòng nước. Vận tốc của ca nô so với bờ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục).  \n'
                %(latex(b),latex(a)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'

                        'Gọi vectơ vận tốc của Ca nô so với dòng nước là $\\overrightarrow{AB}$, vectơ vận tốc của dòng nước so với bờ là vectơ $\\overrightarrow{BC}$. \\\\ \n'
                        'Ta có vectơ vận tốc của Ca nô so với bờ là \\\\ \n'
                        '$\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\vec{F}=\\overrightarrow{AB}+\\overrightarrow{BC}=\\overrightarrow{AC}$. \\\\ \n'
                        '$\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\left| \\vec{F}\\right| = \\left|\\overrightarrow{AC} \\right|=AC =\\sqrt{ AB^{2}+AC^{2}}\\\\ \n'
                        '\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }=\\sqrt{%s^{2}+%s^{2}}=%s$ (km/h).\\\\ \n'
                        'Vậy vận tốc Ca nô so với bờ là $%s \\approx %s$.(km/h). \n'
                        '}{ \n'
                        '\\scalebox{0.8}{\\definecolor{ffqqqq}{rgb}{1.,0.,0.}  \n'
                        '\\definecolor{qqwuqq}{rgb}{0.,0.39215686274509803,0.}  \n'
                        '\\definecolor{zzttqq}{rgb}{0.6,0.2,0.}  \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\clip(-4,-4.7) rectangle (3,2); \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.1,1.6) -- (0.1,1.4) -- (0.9,1.4) -- (0.9,1.6) -- cycle; \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.2,1.2) -- (0.8,1.2) -- (0.8,1.) -- (0.2,1.) -- cycle; \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.2,0.8) -- (0.4,0.8) -- (0.4,0.4) -- (0.2,0.4) -- cycle; \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.8,0.8) -- (0.8,0.4) -- (0.6,0.4) -- (0.6,0.8) -- cycle; \n'
                            '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.1] (0.2,1.2) -- (0.8,1.2) -- (0.8,1.1268603412071911) -- (0.2,1.1328627445981796) -- cycle; \n'
                            '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.1] (0.2,0.8) -- (0.4,0.8) -- (0.4,0.7156957089244842) -- (0.2,0.7186969106199784) -- cycle; \n'
                            '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.1] (0.6,0.8) -- (0.6,0.727700515706461) -- (0.8,0.7216981123154725) -- (0.8,0.8) -- cycle; \n'
                            '\\draw [line width=1.pt] (0.1,1.6)-- (0.9,1.6); \n'
                            '\\draw [shift={(-2.4,0.825)},line width=1.pt]  plot[domain=5.721492420884941:6.1588303126328245,variable=\\t]({1.*3.4264595430268816*cos(\\t r)+0.*3.4264595430268816*sin(\\t r)},{0.*3.4264595430268816*cos(\\t r)+1.*3.4264595430268816*sin(\\t r)}); \n'
                            '\\draw [shift={(3.4,0.825)},line width=1.pt]  plot[domain=3.2659476481365544:3.703285539884438,variable=\\t]({1.*3.4264595430268847*cos(\\t r)+0.*3.4264595430268847*sin(\\t r)},{0.*3.4264595430268847*cos(\\t r)+1.*3.4264595430268847*sin(\\t r)}); \n'
                            '\\draw [line width=1.pt] (0.1,1.6)-- (0.1,1.4); \n'
                            '\\draw [line width=1.pt] (0.1,1.4)-- (0.9,1.4); \n'
                            '\\draw [line width=1.pt] (0.9,1.4)-- (0.9,1.6); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.1,1.6)-- (0.1,1.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.1,1.4)-- (0.9,1.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.9,1.4)-- (0.9,1.6); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.9,1.6)-- (0.1,1.6); \n'
                            '\\draw [line width=1.pt] (0.1,1.3)-- (0.9,1.3); \n'
                            '\\draw [line width=1.pt] (0.9,1.3)-- (0.9,0.4); \n'
                            '\\draw [line width=1.pt] (0.1,1.3)-- (0.1,0.4); \n'
                            '\\draw [shift={(0.5,0.7)},line width=1.pt,color=qqwuqq]  plot[domain=3.7850937623830774:5.639684198386302,variable=\\t]({1.*0.5*cos(\\t r)+0.*0.5*sin(\\t r)},{0.*0.5*cos(\\t r)+1.*0.5*sin(\\t r)}); \n'
                            '\\draw [line width=1.pt] (0.1,0.4)-- (0.18380882294802547,0.); \n'
                            '\\draw [line width=1.pt] (0.9,0.4)-- (0.8235484253822705,0.); \n'
                            '\\draw [shift={(0.503678624165148,0.15575789363733256)},line width=1.pt,color=qqwuqq]  plot[domain=3.5947390266983885:5.83003893407099,variable=\\t]({1.*0.3557769120685321*cos(\\t r)+0.*0.3557769120685321*sin(\\t r)},{0.*0.3557769120685321*cos(\\t r)+1.*0.3557769120685321*sin(\\t r)}); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,1.2)-- (0.8,1.2); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,1.2)-- (0.8,1.); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,1.)-- (0.2,1.); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,1.)-- (0.2,1.2); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,0.8)-- (0.4,0.8); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.4,0.8)-- (0.4,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.4,0.4)-- (0.2,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,0.4)-- (0.2,0.8); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,0.8)-- (0.8,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,0.4)-- (0.6,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.6,0.4)-- (0.6,0.8); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.6,0.8)-- (0.8,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,1.2)-- (0.8,1.2); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,1.2)-- (0.8,1.1268603412071911); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,1.1268603412071911)-- (0.2,1.1328627445981796); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,1.1328627445981796)-- (0.2,1.2); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,0.8)-- (0.4,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.4,0.8)-- (0.4,0.7156957089244842); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.4,0.7156957089244842)-- (0.2,0.7186969106199784); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,0.7186969106199784)-- (0.2,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.6,0.8)-- (0.6,0.727700515706461); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.6,0.727700515706461)-- (0.8,0.7216981123154725); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,0.7216981123154725)-- (0.8,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,0.8)-- (0.6,0.8); \n'
                            '\\draw [->,line width=1.pt] (0.5,-1.) -- (0.5,-4.); \n'
                            '\\draw [->,line width=1.pt] (0.5,-1.) -- (1.5,-4.); \n'
                            '\\draw [->,line width=1.pt] (0.5,-4.) -- (1.5,-4.); \n'
                            '\\draw (-0.1,-0.7585102591917087) node[anchor=north west] {$A$}; \n'
                            '\\draw (0.1373267107269127,-4) node[anchor=north west] {$B$}; \n'
                            '\\draw (1.4,-3.7731103896552742) node[anchor=north west] {$C$}; \n'
                            '\\draw (-1.2,-2.5) node[anchor=north west] {$%s \\text{ km/h}$};\n'
                            '\\draw (0.8,-4.2) node[anchor=north west] {$%s \\text{ km/h}$}; \n'
                            '\\draw [line width=1.pt] (0.,1.3)-- (0.,0.4); \n'
                            '\\draw [line width=1.pt] (1.,1.3)-- (1.,0.4); \n'
                            '\\draw [shift={(0.25,1.3)},line width=1.pt]  plot[domain=2.2142974355881813:3.1415926535897922,variable=\\t]({1.*0.25*cos(\\t r)+0.*0.25*sin(\\t r)},{0.*0.25*cos(\\t r)+1.*0.25*sin(\\t r)}); \n'
                            '\\draw [shift={(0.75,1.3)},line width=1.pt]  plot[domain=0.:0.9272952180016112,variable=\\t]({1.*0.25*cos(\\t r)+0.*0.25*sin(\\t r)},{0.*0.25*cos(\\t r)+1.*0.25*sin(\\t r)}); \n'
                        '\\end{tikzpicture}} \\\\ \n'
                        ' }'
                        %(latex(b),latex(a),latex(x0),latex(x0),latex(kq),latex(a),latex(b)
                            ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='2':
                # Khai báo biến

                a = randint(20,50)
                b = randint(5,19)
                x0 = sqrt(a**2+b**2)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = (
                                'Một dòng sông chảy từ phía Tây sang Đông với vận tốc $%s$ (km/h) so với bờ, có một chiếc Ca nô chuyển động từ phía Bắc xuống phía Nam với vận tốc $%s$ (km/h) so với bờ. Vận tốc của ca nô so với dòng nước bằng bao nhiêu? \n'
                %(latex(b),latex(x0)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'

                        'Gọi vectơ vận tốc của Ca nô so với bờ là $\\overrightarrow{AC}$, vectơ vận tốc của dòng nước so với bờ là vectơ $\\overrightarrow{BC}$. \\\\ \n'
                        'Ta có vectơ vận tốc của Ca nô so với dòng nước là \\\\ \n'
                        '$\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\left| \\vec{AB}\\right| = AB =\\sqrt{ AC^{2}-BC^{2}}\\\\ \n'
                        '\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }=\\sqrt{\\left(%s\\right)^{2}-%s^{2}}=%s$ (km/h).\\\\ \n'
                        'Vậy vận tốc Ca nô so với dòng nước là $%s$ (km/h). \n'
                        '}{ \n'
                        '\\scalebox{0.8}{\\definecolor{ffqqqq}{rgb}{1.,0.,0.}  \n'
                        '\\definecolor{qqwuqq}{rgb}{0.,0.39215686274509803,0.}  \n'
                        '\\definecolor{zzttqq}{rgb}{0.6,0.2,0.}  \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\clip(-4,-4.7) rectangle (3,2); \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.1,1.6) -- (0.1,1.4) -- (0.9,1.4) -- (0.9,1.6) -- cycle; \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.2,1.2) -- (0.8,1.2) -- (0.8,1.) -- (0.2,1.) -- cycle; \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.2,0.8) -- (0.4,0.8) -- (0.4,0.4) -- (0.2,0.4) -- cycle; \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.8,0.8) -- (0.8,0.4) -- (0.6,0.4) -- (0.6,0.8) -- cycle; \n'
                            '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.1] (0.2,1.2) -- (0.8,1.2) -- (0.8,1.1268603412071911) -- (0.2,1.1328627445981796) -- cycle; \n'
                            '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.1] (0.2,0.8) -- (0.4,0.8) -- (0.4,0.7156957089244842) -- (0.2,0.7186969106199784) -- cycle; \n'
                            '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.1] (0.6,0.8) -- (0.6,0.727700515706461) -- (0.8,0.7216981123154725) -- (0.8,0.8) -- cycle; \n'
                            '\\draw [line width=1.pt] (0.1,1.6)-- (0.9,1.6); \n'
                            '\\draw [shift={(-2.4,0.825)},line width=1.pt]  plot[domain=5.721492420884941:6.1588303126328245,variable=\\t]({1.*3.4264595430268816*cos(\\t r)+0.*3.4264595430268816*sin(\\t r)},{0.*3.4264595430268816*cos(\\t r)+1.*3.4264595430268816*sin(\\t r)}); \n'
                            '\\draw [shift={(3.4,0.825)},line width=1.pt]  plot[domain=3.2659476481365544:3.703285539884438,variable=\\t]({1.*3.4264595430268847*cos(\\t r)+0.*3.4264595430268847*sin(\\t r)},{0.*3.4264595430268847*cos(\\t r)+1.*3.4264595430268847*sin(\\t r)}); \n'
                            '\\draw [line width=1.pt] (0.1,1.6)-- (0.1,1.4); \n'
                            '\\draw [line width=1.pt] (0.1,1.4)-- (0.9,1.4); \n'
                            '\\draw [line width=1.pt] (0.9,1.4)-- (0.9,1.6); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.1,1.6)-- (0.1,1.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.1,1.4)-- (0.9,1.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.9,1.4)-- (0.9,1.6); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.9,1.6)-- (0.1,1.6); \n'
                            '\\draw [line width=1.pt] (0.1,1.3)-- (0.9,1.3); \n'
                            '\\draw [line width=1.pt] (0.9,1.3)-- (0.9,0.4); \n'
                            '\\draw [line width=1.pt] (0.1,1.3)-- (0.1,0.4); \n'
                            '\\draw [shift={(0.5,0.7)},line width=1.pt,color=qqwuqq]  plot[domain=3.7850937623830774:5.639684198386302,variable=\\t]({1.*0.5*cos(\\t r)+0.*0.5*sin(\\t r)},{0.*0.5*cos(\\t r)+1.*0.5*sin(\\t r)}); \n'
                            '\\draw [line width=1.pt] (0.1,0.4)-- (0.18380882294802547,0.); \n'
                            '\\draw [line width=1.pt] (0.9,0.4)-- (0.8235484253822705,0.); \n'
                            '\\draw [shift={(0.503678624165148,0.15575789363733256)},line width=1.pt,color=qqwuqq]  plot[domain=3.5947390266983885:5.83003893407099,variable=\\t]({1.*0.3557769120685321*cos(\\t r)+0.*0.3557769120685321*sin(\\t r)},{0.*0.3557769120685321*cos(\\t r)+1.*0.3557769120685321*sin(\\t r)}); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,1.2)-- (0.8,1.2); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,1.2)-- (0.8,1.); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,1.)-- (0.2,1.); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,1.)-- (0.2,1.2); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,0.8)-- (0.4,0.8); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.4,0.8)-- (0.4,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.4,0.4)-- (0.2,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,0.4)-- (0.2,0.8); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,0.8)-- (0.8,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,0.4)-- (0.6,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.6,0.4)-- (0.6,0.8); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.6,0.8)-- (0.8,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,1.2)-- (0.8,1.2); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,1.2)-- (0.8,1.1268603412071911); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,1.1268603412071911)-- (0.2,1.1328627445981796); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,1.1328627445981796)-- (0.2,1.2); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,0.8)-- (0.4,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.4,0.8)-- (0.4,0.7156957089244842); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.4,0.7156957089244842)-- (0.2,0.7186969106199784); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,0.7186969106199784)-- (0.2,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.6,0.8)-- (0.6,0.727700515706461); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.6,0.727700515706461)-- (0.8,0.7216981123154725); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,0.7216981123154725)-- (0.8,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,0.8)-- (0.6,0.8); \n'
                            '\\draw [->,line width=1.pt] (0.5,-1.) -- (0.5,-4.); \n'
                            '\\draw [->,line width=1.pt] (0.5,-1.) -- (1.5,-4.); \n'
                            '\\draw [->,line width=1.pt] (0.5,-4.) -- (1.5,-4.); \n'
                            '\\draw (-0.1,-0.7585102591917087) node[anchor=north west] {$A$}; \n'
                            '\\draw (0.1373267107269127,-4) node[anchor=north west] {$B$}; \n'
                            '\\draw (1.4,-3.7731103896552742) node[anchor=north west] {$C$}; \n'
                            '\\draw (1.1,-2.5) node[anchor=north west] {$%s \\text{ km/h}$};\n'
                            '\\draw (0.8,-4.2) node[anchor=north west] {$%s \\text{ km/h}$}; \n'
                            '\\draw [line width=1.pt] (0.,1.3)-- (0.,0.4); \n'
                            '\\draw [line width=1.pt] (1.,1.3)-- (1.,0.4); \n'
                            '\\draw [shift={(0.25,1.3)},line width=1.pt]  plot[domain=2.2142974355881813:3.1415926535897922,variable=\\t]({1.*0.25*cos(\\t r)+0.*0.25*sin(\\t r)},{0.*0.25*cos(\\t r)+1.*0.25*sin(\\t r)}); \n'
                            '\\draw [shift={(0.75,1.3)},line width=1.pt]  plot[domain=0.:0.9272952180016112,variable=\\t]({1.*0.25*cos(\\t r)+0.*0.25*sin(\\t r)},{0.*0.25*cos(\\t r)+1.*0.25*sin(\\t r)}); \n'
                        '\\end{tikzpicture}} \\\\ \n'
                        ' }'
                        %(latex(x0),latex(b),latex(a),latex(a),latex(x0),latex(b)
                            ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a))

            if dang=='3':
                # Khai báo biến

                a = randint(20,50)
                b = randint(5,19)
                x0 = sqrt(a**2+b**2)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = (
                                'Biết rằng có một chiếc Ca nô chuyển động trên dòng sông từ phía Bắc xuống phía Nam với vận tốc $%s$ (km/h) so với bờ và so với dòng nước bằng $%s$ (km/h). Dòng sông chảy từ phía Tây sang Đông với vận tốc bao nhiêu km/h so với bờ?  \n'
                %(latex(x0),latex(a)
                                ))

                # Nội dung lời giải
                loigiai = ('\\immini{ \n'

                        'Gọi vectơ vận tốc của Ca nô so với bờ là $\\overrightarrow{AC}$, so với dòng nước là vectơ $\\overrightarrow{AB}$. \\\\ \n'
                        'Ta có vectơ vận tốc của dòng nước so với bờ là \\\\ \n'
                        '$\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\left| \\vec{BC}\\right| = BC =\\sqrt{ AC^{2}-AB^{2}}\\\\ \n'
                        '\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }\\text{ }=\\sqrt{\\left(%s\\right)^{2}-%s^{2}}=%s$ (km/h).\\\\ \n'
                        'Vậy vận tốc dòng nước so với bờ là $%s$ (km/h). \n'
                        '}{ \n'
                        '\\scalebox{0.8}{\\definecolor{ffqqqq}{rgb}{1.,0.,0.}  \n'
                        '\\definecolor{qqwuqq}{rgb}{0.,0.39215686274509803,0.}  \n'
                        '\\definecolor{zzttqq}{rgb}{0.6,0.2,0.}  \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\clip(-4,-4.7) rectangle (3,2); \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.1,1.6) -- (0.1,1.4) -- (0.9,1.4) -- (0.9,1.6) -- cycle; \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.2,1.2) -- (0.8,1.2) -- (0.8,1.) -- (0.2,1.) -- cycle; \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.2,0.8) -- (0.4,0.8) -- (0.4,0.4) -- (0.2,0.4) -- cycle; \n'
                            '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.8,0.8) -- (0.8,0.4) -- (0.6,0.4) -- (0.6,0.8) -- cycle; \n'
                            '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.1] (0.2,1.2) -- (0.8,1.2) -- (0.8,1.1268603412071911) -- (0.2,1.1328627445981796) -- cycle; \n'
                            '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.1] (0.2,0.8) -- (0.4,0.8) -- (0.4,0.7156957089244842) -- (0.2,0.7186969106199784) -- cycle; \n'
                            '\\fill[line width=1.pt,color=ffqqqq,fill=ffqqqq,fill opacity=0.1] (0.6,0.8) -- (0.6,0.727700515706461) -- (0.8,0.7216981123154725) -- (0.8,0.8) -- cycle; \n'
                            '\\draw [line width=1.pt] (0.1,1.6)-- (0.9,1.6); \n'
                            '\\draw [shift={(-2.4,0.825)},line width=1.pt]  plot[domain=5.721492420884941:6.1588303126328245,variable=\\t]({1.*3.4264595430268816*cos(\\t r)+0.*3.4264595430268816*sin(\\t r)},{0.*3.4264595430268816*cos(\\t r)+1.*3.4264595430268816*sin(\\t r)}); \n'
                            '\\draw [shift={(3.4,0.825)},line width=1.pt]  plot[domain=3.2659476481365544:3.703285539884438,variable=\\t]({1.*3.4264595430268847*cos(\\t r)+0.*3.4264595430268847*sin(\\t r)},{0.*3.4264595430268847*cos(\\t r)+1.*3.4264595430268847*sin(\\t r)}); \n'
                            '\\draw [line width=1.pt] (0.1,1.6)-- (0.1,1.4); \n'
                            '\\draw [line width=1.pt] (0.1,1.4)-- (0.9,1.4); \n'
                            '\\draw [line width=1.pt] (0.9,1.4)-- (0.9,1.6); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.1,1.6)-- (0.1,1.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.1,1.4)-- (0.9,1.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.9,1.4)-- (0.9,1.6); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.9,1.6)-- (0.1,1.6); \n'
                            '\\draw [line width=1.pt] (0.1,1.3)-- (0.9,1.3); \n'
                            '\\draw [line width=1.pt] (0.9,1.3)-- (0.9,0.4); \n'
                            '\\draw [line width=1.pt] (0.1,1.3)-- (0.1,0.4); \n'
                            '\\draw [shift={(0.5,0.7)},line width=1.pt,color=qqwuqq]  plot[domain=3.7850937623830774:5.639684198386302,variable=\\t]({1.*0.5*cos(\\t r)+0.*0.5*sin(\\t r)},{0.*0.5*cos(\\t r)+1.*0.5*sin(\\t r)}); \n'
                            '\\draw [line width=1.pt] (0.1,0.4)-- (0.18380882294802547,0.); \n'
                            '\\draw [line width=1.pt] (0.9,0.4)-- (0.8235484253822705,0.); \n'
                            '\\draw [shift={(0.503678624165148,0.15575789363733256)},line width=1.pt,color=qqwuqq]  plot[domain=3.5947390266983885:5.83003893407099,variable=\\t]({1.*0.3557769120685321*cos(\\t r)+0.*0.3557769120685321*sin(\\t r)},{0.*0.3557769120685321*cos(\\t r)+1.*0.3557769120685321*sin(\\t r)}); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,1.2)-- (0.8,1.2); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,1.2)-- (0.8,1.); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,1.)-- (0.2,1.); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,1.)-- (0.2,1.2); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,0.8)-- (0.4,0.8); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.4,0.8)-- (0.4,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.4,0.4)-- (0.2,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.2,0.4)-- (0.2,0.8); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,0.8)-- (0.8,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.8,0.4)-- (0.6,0.4); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.6,0.4)-- (0.6,0.8); \n'
                            '\\draw [line width=1.pt,color=zzttqq] (0.6,0.8)-- (0.8,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,1.2)-- (0.8,1.2); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,1.2)-- (0.8,1.1268603412071911); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,1.1268603412071911)-- (0.2,1.1328627445981796); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,1.1328627445981796)-- (0.2,1.2); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,0.8)-- (0.4,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.4,0.8)-- (0.4,0.7156957089244842); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.4,0.7156957089244842)-- (0.2,0.7186969106199784); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.2,0.7186969106199784)-- (0.2,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.6,0.8)-- (0.6,0.727700515706461); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.6,0.727700515706461)-- (0.8,0.7216981123154725); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,0.7216981123154725)-- (0.8,0.8); \n'
                            '\\draw [line width=1.pt,color=ffqqqq] (0.8,0.8)-- (0.6,0.8); \n'
                            '\\draw [->,line width=1.pt] (0.5,-1.) -- (0.5,-4.); \n'
                            '\\draw [->,line width=1.pt] (0.5,-1.) -- (1.5,-4.); \n'
                            '\\draw [->,line width=1.pt] (0.5,-4.) -- (1.5,-4.); \n'
                            '\\draw (-0.1,-0.7585102591917087) node[anchor=north west] {$A$}; \n'
                            '\\draw (0.1373267107269127,-4) node[anchor=north west] {$B$}; \n'
                            '\\draw (1.4,-3.7731103896552742) node[anchor=north west] {$C$}; \n'
                            '\\draw (1.1,-2.5) node[anchor=north west] {$%s \\text{ km/h}$};\n'
                            '\\draw (-1.2,-2.5) node[anchor=north west] {$%s \\text{ km/h}$}; \n'
                            '\\draw [line width=1.pt] (0.,1.3)-- (0.,0.4); \n'
                            '\\draw [line width=1.pt] (1.,1.3)-- (1.,0.4); \n'
                            '\\draw [shift={(0.25,1.3)},line width=1.pt]  plot[domain=2.2142974355881813:3.1415926535897922,variable=\\t]({1.*0.25*cos(\\t r)+0.*0.25*sin(\\t r)},{0.*0.25*cos(\\t r)+1.*0.25*sin(\\t r)}); \n'
                            '\\draw [shift={(0.75,1.3)},line width=1.pt]  plot[domain=0.:0.9272952180016112,variable=\\t]({1.*0.25*cos(\\t r)+0.*0.25*sin(\\t r)},{0.*0.25*cos(\\t r)+1.*0.25*sin(\\t r)}); \n'
                        '\\end{tikzpicture}} \\\\ \n'
                        ' }'
                        %(latex(x0),latex(a),latex(b),latex(b),latex(x0),latex(a)
                            ))
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(b))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{\n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0', '')
            return content     

