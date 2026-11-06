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


def bt_dang11_p1_b4_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x = symbols('x')
                a = randint(-3,3)
                b = randint(-9,9)
                c = randint(-3,3)
                d = randint(-9,9)
                e = randint(-20,20)
                while a==0 or c==0 or b==0 or a*c<=0 or b/a>=d/c:
                    a = randint(-3,3)
                    b = randint(-9,9)
                    c = randint(-3,3)
                    d = randint(-9,9)
                    e = randint(-20,20)
                f=Rational(a*c,3)*x**3+Rational(a*d+b*c,-2)*x**2+b*d*x+e
                dhf=a*c*x**2+(-a*d-b*c)*x+b*d
                dhf2=2*a*c*x+(-a*d-b*c)
                x0=Rational(a*d+b*c,2*a*c)
                y0=Rational(a*c,3)*x0**3+Rational(a*d+b*c,-2)*x0**2+b*d*x0+e
                x1 = Rational(b,a)
                x2 = Rational(d,c)
                y1=Rational(a*c,3)*x1**3+Rational(a*d+b*c,-2)*x1**2+b*d*x1+e
                y2=Rational(a*c,3)*x2**3+Rational(a*d+b*c,-2)*x2**2+b*d*x2+e
                du = ['$\\left(%s;%s\\right)$'%(latex(x0),latex(y0)),
            ]
                da= random.choice(du)
                s = [' $\\left(%s;%s\\right)$'%(latex(x1),latex(x2)),
                    ' $\\left(%s;%s\\right)$'%(latex(x1),latex(y1)),
                    ' $\\left(%s;%s\\right)$'%(latex(x2),latex(y2))]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Tọa độ tâm đối xứng của đồ thị hàm số $y=%s$ là \n'''%(latex(f))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tập xác định: $\\mathscr{D}=\\mathbb{R}$.\\\\ \n'
                        '''Ta có $y'=%s$.\\\\ \n''' 
                        '''\\hspace*{1.1cm}$y''=%s$.\\\\ \n'''
                        '''\\hspace*{1.1cm}$y''=0\\Leftrightarrow %s=0\\Leftrightarrow x=%s$.\\\\ \n'''
                        '''Khi đó $y\\left(%s\\right)=%s$. \\\\ \n'''
                        'Vậy tọa độ tâm đối xứng của đồ thị hàm số đã cho là $\\left(%s;%s\\right)$. \\\\ \n'
                        %(latex(dhf),
                        latex(dhf2),
                        latex(dhf2),latex(x0),
                        latex(x0),latex(y0),
                        latex(x0),latex(y0)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('11x', '11fx').replace('21x', '21fx').replace('31x', '31fx').replace('41x', '41fx').replace('51x', '51fx').replace('61x', '61fx').replace('71x', '71fx').replace('81x', '81fx').replace('91x', '91fx').replace('101x', '101fx').replace('1x', 'x').replace('11fx', '11x').replace('21fx', '21x').replace('31fx', '31x').replace('41fx', '41x').replace('51fx', '51x').replace('61fx', '61x').replace('71fx', '71x').replace('81fx', '81x').replace('91fx', '91x').replace('101fx', '101x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content

