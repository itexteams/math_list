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


def bt_dang8_p3_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x=symbols('x')
                a = randint(3,10)
                x1=Rational(a,6)
                x2=Rational(a,2)
                v = 4*x**3-(4*a)*x**2+(a**2)*x
                dhv = 12*x**2-8*a*x+a**2
                vmax = 4*(x1)**3-(4*a)*(x1)**2+(a**2)*(x1)
                vmax1 = 4*(x1)**3-(4*a)*(x1)**2+(a**2)*(x1)
                number = Decimal(float(vmax1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho một tấm nhôm có dạng hình vuông cạnh $%s$ dm$zz$ Bác Nam cắt ở bốn góc bốn hình vuông cùng có độ dài cạnh bằng $x$ dm, rồi gập tấm tôn như hình bên dưới để được một cái hộp có dạng hình hộp chữ nhật không có nắp$zz$'
                                ' Gọi $V$ là thể tích khối hộp đó tính theo $x$ dm$zz$ Giá trị lớn nhất của $V$ là bao nhiêu đề-xi-mét khối? (kết quả làm tròn đến hàng phần chục)$zz$ \\\\ \n'
                                '\\hspace*{4cm}\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0$zz$6] \n'
                '\\clip(5$zz$020490658350568,-2$zz$5) rectangle (21$zz$5,3$zz$3);\\\\ \n'
                '\\fill[fill=black,fill opacity=0$zz$25] (8,2) -- (9,2) -- (9,3) -- (8,3) -- cycle;\\\\ \n'
                '\\fill[fill=black,fill opacity=0$zz$25] (12,2) -- (13,2) -- (13,3) -- (12,3) -- cycle;\\\\ \n'
                '\\fill[fill=black,fill opacity=0$zz$25] (8,-2) -- (9,-2) -- (9,-1) -- (8,-1) -- cycle;\\\\ \n'
                '\\fill[fill=black,fill opacity=0$zz$25] (12,-2) -- (13,-2) -- (13,-1) -- (12,-1) -- cycle;\\\\ \n'
                '\\draw (9,-2)-- (9,-1);\\\\ \n'
                '\\draw (9,-1)-- (8,-1);\\\\ \n'
                '\\draw (8,-1)-- (8,-2);\\\\ \n'
                '\\draw (13,-1)-- (12,-1);\\\\ \n'
                '\\draw (12,-1)-- (12,-2);\\\\ \n'
                '\\draw (9,3)-- (12,3);\\\\ \n'
                '\\draw (8,2)-- (8,-1);\\\\ \n'
                '\\draw (9,-2)-- (12,-2);\\\\ \n'
                '\\draw (13,-1)-- (13,2);\\\\ \n'
                '\\draw (9,2)-- (12,2);\\\\ \n'
                '\\draw (12,2)-- (12,-1);\\\\ \n'
                '\\draw (12,-1)-- (9,-1);\\\\ \n'
                '\\draw (9,-1)-- (9,2);\\\\ \n'
                '\\draw [->] (7,1) -- (7,3);\\\\ \n'
                '\\draw [->] (7,0) -- (7,-2);\\\\ \n'
                '\\draw (16,3)-- (14,0);\\\\ \n'
                '\\draw (14,0)-- (18,0);\\\\ \n'
                '\\draw (18,0)-- (20,3);\\\\ \n'
                '\\draw (20,3)-- (16,3);\\\\ \n'
                '\\draw (16,3)-- (16,2);\\\\ \n'
                '\\draw (20,2)-- (18,-1);\\\\ \n'
                '\\draw (18,-1)-- (14,-1);\\\\ \n'
                '\\draw (14,-1)-- (14,0);\\\\ \n'
                '\\draw (18,0)-- (18,-1);\\\\ \n'
                '\\draw (20,2)-- (20,3);\\\\ \n'
                '\\draw (14$zz$666666666666666,0)-- (16,2);\\\\ \n'
                '\\draw (16,2)-- (19$zz$333333333333332,2);\\\\ \n'
                '\\draw [line width=1$zz$2pt,dash pattern=on 2pt off 2pt] (19$zz$333333333333332,2)-- (20,2);\\\\ \n'
                '\\draw [line width=1$zz$2pt,dash pattern=on 2pt off 2pt] (14$zz$666666666666666,0)-- (14,-1);\\\\ \n'
                '\\draw (7$zz$5,1) node[below left]{$%sdm$};\\\\ \n'
                '\\draw (14,2$zz$5) node[below left]{$x$};\\\\ \n'
                '\\draw (14,-1$zz$2) node[below left]{$x$};\\\\ \n'
                '\\draw (8,3)-- (9,3);\\\\ \n'
                '\\draw (9,3)-- (9,2);\\\\ \n'
                '\\draw (9,2)-- (8,2);\\\\ \n'
                '\\draw (8,2)-- (8,3);\\\\ \n'
                '\\draw (12,3)-- (13,3);\\\\ \n'
                '\\draw (13,3)-- (13,2);\\\\ \n'
                '\\draw (13,2)-- (12,2);\\\\ \n'
                '\\draw (12,2)-- (12,3);\\\\ \n'
                '\\draw (8,-1)-- (9,-1);\\\\ \n'
                '\\draw (9,-1)-- (9,-2);\\\\ \n'
                '\\draw (9,-2)-- (8,-2);\\\\ \n'
                '\\draw (8,-2)-- (8,-1);\\\\ \n'
                '\\draw (12,-1)-- (13,-1);\\\\ \n'
                '\\draw (13,-1)-- (13,-2);\\\\ \n'
                '\\draw (13,-2)-- (12,-2);\\\\ \n'
                '\\draw (12,-2)-- (12,-1);\\\\ \n'
                '\\end{tikzpicture}\\\\ \n'
                                %(latex(a),latex(a)))
                # Nội dung lời giải
                loigiai = ('Ta thấy độ dài $x$ dm của cạnh hình vuông thỏa mãn điều kiện $\\left(0<x<%s\\right)$$zz$\\\\ \n'
                        'Thể tích khối hộp là $V(x)=x\\cdot(%s-2x)^2= %s$ với $0<x<%s$$zz$\\\\ \n'
                        'Ta phải tìm $x_{0}\\in\\left(0;%s\\right)$ sao cho $V(x_{0})$ có giá trị lớn nhất$zz$\\\\ \n'
                        'Ta có $V\'(x)= %s$$zz$\\\\ \n'
                        '\\hspace*{1$zz$1cm}$V\'(x)=0 \\Leftrightarrow \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                        'Trên khoảng $\\left(0;%s\\right)$, ta có $V\'(x)=0$ khi $x=%s$$zz$\\\\ \n'
                        '''Bảng biến thiên \\\\ \n'''
                        '\\hspace*{5cm} \\begin{tikzpicture}    \n'
                        '\\tkzTabInit[espcl=2$zz$5,lgt=1$zz$5]   \n'
                        '{$x$/1,$V\'(x)$/0$zz$7,$V(x)$/2$zz$1}   \n'
                        '{$0$,$%s$,$%s$}   \n'
                        '\\tkzTabLine{,+,0,-,}   \n'
                        '\\tkzTabVar{-/0,+/$%s$,-/$0$}   \n'
                        '\\end{tikzpicture}   \\\\ \n'
                        'Từ bảng biến thiên ta thấy thể tích lớn nhất của hình hộp là \\\\ \n'
                        '$V=%s\\approx %s (dm^3)$$zz$ '
                        %(latex(x2),
                            latex(a),latex(v),latex(x2),
                            latex(x2),latex(dhv),latex(x1),latex(x2),
                            latex(x2),latex(x1),
                            latex(x1),latex(x2),
                            latex(vmax),
                            latex(vmax),latex(kq)))
            #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0','').replace('.',',').replace('$zz$','.')
            return content 

