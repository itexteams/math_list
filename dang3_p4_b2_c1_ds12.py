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


def bt_dang3_p4_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=randint(1,100)
                f=(a*x-2*x**3)/3
                daoham=-2*x**2+Rational(a,3)
                x0=sqrt(a*6)/6
                f0=(a*x0-2*x0**3)/3

                number = Decimal(float(f0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một người dự định dùng hết $%s$ m$^2$ kính để làm một bể cá có dạng hình hộp chữ nhật không nắp, chiều dài gấp đôi chiều rộng (các mối ghép không đáng kể)$zz$ Tìm thể tích lớn nhất của bể cá (Làm tròn kết quả đến hàng phần chục)$zz$  \n'
                                %(latex(a)
                                ))                   
                # Nội dung lời giải
                loigiai = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                        '\\clip(0,-3) rectangle (9,4); \n'
                        '\\draw (1,1)-- (3,3); \n'
                        '\\draw (3,3)-- (8,3); \n'
                        '\\draw (8,3)-- (6,1); \n'
                        '\\draw (6,1)-- (1,1); \n'
                        '\\draw (1,1)-- (1,-2); \n'
                        '\\draw (1,-2)-- (6,-2); \n'
                        '\\draw (6,-2)-- (6,1); \n'
                        '\\draw (8,3)-- (8,0); \n'
                        '\\draw (8,0)-- (6,-2); \n'
                        '\\draw [dash pattern=on 2pt off 2pt] (3,3)-- (3,0); \n'
                        '\\draw [dash pattern=on 2pt off 2pt] (3,0)-- (8,0); \n'
                        '\\draw [dash pattern=on 2pt off 2pt] (3,0)-- (1,-2); \n'
                        '\\draw (3,-2) node[anchor=north west] {$a$}; \n'
                        '\\draw (7,-1) node[anchor=north west] {$b$}; \n'
                        '\\draw (8,2) node[anchor=north west] {$c$}; \n'
                    '\\end{tikzpicture} \n'
                '\\end{center} \n'
                            'Giả sử hình hộp chữ nhật có chiều dài, rộng, cao lần lượt là $a, b$ và $c$$zz$ Khi đó \\\\ \n'
                        '\\hspace*{1cm} Thể tích của bể cá là $V=abc$$zz$ \\\\ \n'
                        'Mặt khác theo giả thiết ta có \\\\ \n'
                        '\\hspace*{1cm} $\\heva{& ab+2bc+2ac =%s\\\\ & a=2b}  \\Leftrightarrow \\heva{& 2b^2+6bc =%s\\\\ & a=2b} \\Leftrightarrow \\heva{& c=\\dfrac{%s-2b^2}{6b}\\\\ & a=2b$zz$}$ \\\\ \n'
                        'Khi đó $V=2b^2 \\cdot \\dfrac{%s-2b^2}{6b}=\\dfrac{%sb-2b^3}{3}$$zz$ \\\\ \n'
                        'Xét hàm số $f(x)=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=%s$$zz$\\\\ \n'
                        '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow x=%s$$zz$\\\\ \n'
                        '\\hspace*{1cm} Bảng biến thiên \\\\ \n'
                        '\\hspace*{1cm}\\begin{tikzpicture} \n'
                        '\\tkzTabInit[espcl=2$zz$5,lgt=1$zz$5] \n'
                        '{$x$/1,$f\'(x)$/0$zz$7,$f(x)$/2$zz$1} \n'
                        '{$0$,$%s$,$+\\infty$} \n'
                        '\\tkzTabLine{,+,0,-,} \n'
                        '\\tkzTabVar{-/$0$,+/$%s$,-/$-\\infty$}  \n'
                        '\\end{tikzpicture} \\\\ \n'
                        'Từ bảng biến thiên ta thấy giá trị lớn nhất của hàm số $f(x)$ bằng $%s$$zz$ \\\\ \n'
                        'Vậy diện tích lớn nhất của tam giác $ABC$ là $%s \\approx %s$ m$^2$$zz$'

                        %(latex(a),latex(a),latex(a),latex(a),latex(a),
                            latex(f),
                            latex(daoham),
                            latex(x0),
                            latex(x0),
                            latex(f0),
                            latex(f0),
                            latex(f0), latex(kq)                                
                            ))                    
                #Đáp án

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content            

