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


def bt_dang2_p1_b2_c3_hh10(self):
            # Khai báo biến
            x = symbols("x")
            y = symbols('y')
            t = symbols('t')

            hsa1 = randint(-9,9)   
            hsb1 = randint(-9,9)
            if hsa1==0 and hsb1==0:
                hsa1 = randint(-9,9)   
                hsb1 = randint(-9,9)
            hsc1 = randint(-9,9)
            #\\\\\\\\\\\\\\\\\\\\\\\Rút gọn các hệ số
            gcd = math.gcd(math.gcd(hsa1, hsb1), hsc1)
            # Rút gọn các hệ số
            a1 = hsa1 // gcd
            b1 = hsb1 // gcd
            c1 = hsc1 // gcd
            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            pt1 = Eq(a1*x+b1*y+c1,0)

            hsa2 = randint(-9,9)   
            hsb2 = randint(-9,9)
            if hsa2==0 and hsb2==0:
                hsa2 = randint(-9,9)   
                hsb2 = randint(-9,9)
            hsc3 = randint(-9,9)
            #\\\\\\\\\\\\\\\\\\\\\\\Rút gọn các hệ số
            gcd = math.gcd(math.gcd(hsa2, hsb2), hsc3)
            # Rút gọn các hệ số
            a2 = hsa2 // gcd
            b2 = hsb2 // gcd
            c3 = hsc3 // gcd
            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            pt2 = Eq(a2*x+b2*y+c3,0)

            d = a1*b2-a2*b1
            dx = -c1*b2+c3*b1
            dy = -a1*c3+a2*c1

            x0 = Rational(dx,d)
            y0 = Rational(dy,d)
            # Câu hỏi

            #Chuyển d1 về phương trình tham số
            x1 = randint(-9,9)
            if b1!=0:
                y1 = Rational(-c1-a1*x1,b1)
            ptts_x = Eq(x,x1+b1*t)
            ptts_y = Eq(y,y1-a1*t)
            noidungcauhoi='''Trong mặt phẳng tọa độ $(Oxy)$, cho hai đường thẳng $d_1: \\heva{& %s \\\\ & %s} $ và $d_2:%s$. Khẳng định nào sau đây là \\textbf{đúng}?''' %(latex(ptts_x), latex(ptts_y), latex(pt2))
            # Các đáp án
            if d!=0:
                da_d = 'Hai đường thẳng trùng nhau'
                da_s1 = 'Hai đường thẳng song song'
                da_s2 = '\\True Hai đường thẳng cắt nhau tại điểm $\\left( %s;%s \\right)$' %(latex(x0), latex(y0))
                da_s3 = 'Hai đường thẳng cắt nhau tại điểm $\\left( %s;%s \\right)$' %(latex(y0), latex(x0))
            if d==0 and (dx!=0 or dy!=0):
                da_d = 'Hai đường thẳng trùng nhau'
                da_s1 = '\\True Hai đường thẳng song song'
                da_s2 = 'Hai đường thẳng cắt nhau tại điểm $\\left( %s;%s \\right)$' %(latex(-a1), latex(c3))
                da_s3 = 'Hai đường thẳng cắt nhau tại điểm $\\left( %s;%s \\right)$' %(latex(b2), latex(-c1))
            if d==0 and (dx==0 and dy==0):
                da_d = '\\True Hai đường thẳng trùng nhau'
                da_s1 = 'True Hai đường thẳng song song'
                da_s2 = 'Hai đường thẳng cắt nhau tại điểm $\\left( %s;%s \\right)$' %(latex(-a2), latex(c1))
                da_s3 = 'Hai đường thẳng cắt nhau tại điểm $\\left( %s;%s \\right)$' %(latex(b1), latex(-c3))


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            if d!=0:
                loigiai=( 'Đường thẳng $d_1$ đi qua điểm $M \\left( %s;%s \\right) $ và có vectơ chỉ phương là $\\vec u= (%s;%s)$. \\\\'
                        'Suy ra vectơ pháp tuyến của $d_1$ là $\\vec n= (%s;%s)$. \\\\'
                        'Phương trình tổng quát của $d_1$ là $%s$. \\\\'
                    'Xét hệ phương trình $\\heva{& %s \\\\ & %s }$.\\\\'
                    'Giải hệ phương trình ta thấy hệ có một nghiệm $x= %s ; y= %s$. \\\\'
                    'Vậy hai đường thẳng cắt nhau tại điểm $\\left( %s;%s \\right)$.'
                    ) %(latex(x1), latex(y1), latex(b1), latex(-a1), latex(a1), latex(b1), latex(pt1), latex(pt1), latex(pt2), latex(x0), latex(y0), latex(x0), latex(y0))
            if d==0 and (dx!=0 or dy!=0):
                loigiai=( 'Đường thẳng $d_1$ đi qua điểm $M \\left( %s;%s \\right) $ và có vectơ chỉ phương là $\\vec u= (%s;%s)$. \\\\'
                        'Suy ra vectơ pháp tuyến của $d_1$ là $\\vec n= (%s;%s)$. \\\\'
                        'Phương trình tổng quát của $d_1$ là $%s$. \\\\'
                    'Xét hệ phương trình $\\heva{& %s \\\\ & %s }$.\\\\'
                    'Giải hệ phương trình ta thấy hệ vô nghiệm.\\\\'
                    'Vậy hai đường thẳng song song.'
                    ) %(latex(x1), latex(y1), latex(b1), latex(-a1), latex(a1), latex(b1), latex(pt1), latex(pt1), latex(pt2))     
            if d==0 and (dx==0 and dy==0):
                loigiai=( 'Đường thẳng $d_1$ đi qua điểm $M \\left( %s;%s \\right) $ và có vectơ chỉ phương là $\\vec u= (%s;%s)$. \\\\'
                        'Suy ra vectơ pháp tuyến của $d_1$ là $\\vec n= (%s;%s)$. \\\\'
                        'Phương trình tổng quát của $d_1$ là $%s$. \\\\'
                    'Xét hệ phương trình $\\heva{& %s \\\\ & %s }$.\\\\'
                    'Giải hệ phương trình ta thấy hệ vô số nghiệm.\\\\'
                    'Vậy hai đường thẳng trùng nhau.'
                    ) %(latex(x1), latex(y1), latex(b1), latex(-a1), latex(a1), latex(b1), latex(pt1),latex(pt1), latex(pt2))  

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('+-','-').replace('--','+').replace('-+','-')
            return content   

