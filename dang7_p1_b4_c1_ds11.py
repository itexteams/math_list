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


def bt_dang7_p1_b4_c1_ds11(self):
            # Khai báo biến
            lisdang=['6','7','8','9']
            dang=random.choice(lisdang)

            if dang=='9':
                x=symbols('x')
                m=randint(-9,9)
                n=randint(-9,9)
                # SỬA TẠI ĐÂY: Thêm điều kiện n == 0 vào vòng lặp để tránh mẫu số bằng 0
                while abs(m) <= abs(n) or n == 0:
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)
                g=acos(a)

                d = [
                    'Vô nghiệm',
                    ]
                da= random.choice(d)
                s = [
                    '$x=k2 \\pi, k \\in \\mathbb{Z} $',
                    '$x=\\dfrac{\\pi}{2}+k\\pi, k \\in \\mathbb{Z} $',
                    '$x=\\dfrac{\\pi}{3}+k\\pi, k \\in \\mathbb{Z} $',
                    '$x=k \\pi, k \\in \\mathbb{Z} $',
                    '$x=\\dfrac{\\pi}{6}+k2 \\pi, k \\in \\mathbb{Z} $',

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $\\cos x =%s$ có nghiệm là  \n'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta thấy $\\left| %s \\right|>1$ nên phương trình vô nghiệm. \\\\ \n'

                        %(latex(a)
                        ))

            if dang=='8':
                x=symbols('x')
                lisa=[0]
                a=random.choice(lisa)
                g=acos(a)

                d = [
                    '$x=%s+k \\pi, k \\in \\mathbb{Z} $'%(latex(g)),
                    ]
                da= random.choice(d)
                s = [
                    '$x=%s+k 2\\pi, k  \\in \\mathbb{Z} $'%(latex(g)),
                    '$x=%s+k \\pi, k \\in \\mathbb{Z} $'%(latex(2*g)),
                    '$x=%s+k 2\\pi, k \\in \\mathbb{Z} $'%(latex(3*g)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $\\cos x =%s$ có nghiệm là  \n'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\cos x =%s \\Leftrightarrow  \\cos x = \\cos %s \\Leftrightarrow  x=%s+k \\pi, k \\in \\mathbb{Z}$. \\\\ \n'

                        %(latex(a),latex(g),latex(g)
                        ))

            if dang=='7':
                x=symbols('x')
                lisa=[1,-1]
                a=random.choice(lisa)
                g=acos(a)

                d = [
                    '$x=%s+k 2 \\pi, k \\in \\mathbb{Z} $'%(latex(g)),
                    ]
                da= random.choice(d)
                s = [
                    '$x=%s+k\\pi, k \\in \\mathbb{Z} $'%(latex(-g)),
                    '$x=%s+k 5 \\pi, k \\in \\mathbb{Z} $'%(latex(g)),
                    '$x=%s+k 3 \\pi, k \\in \\mathbb{Z} $'%(latex(-g)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $\\cos x =%s$ có nghiệm là  \n'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\cos x =%s \\Leftrightarrow  \\cos x = \\cos \\left( %s \\right) \\Leftrightarrow  x=%s+k 2 \\pi, k \\in \\mathbb{Z}$. \\\\ \n'

                        %(latex(a),latex(g),latex(g)
                        ))

            if dang=='6':
                x=symbols('x')
                lisa=[Rational(1,2),sqrt(2)/2,sqrt(3)/2,-Rational(1,2),-sqrt(2)/2,-sqrt(3)/2]
                a=random.choice(lisa)
                g=acos(a)

                d = [
                    '$\\hoac{&x=%s+k2\\pi \\\\& x=%s+k2\\pi} (k \\in \\mathbb{Z}) $'%(latex(g),latex(-g)),
                    ]
                da= random.choice(d)
                s = [
                    '$\\hoac{&x=%s+k2\\pi \\\\& x=%s+k2\\pi} (k \\in \\mathbb{Z}) $'%(latex(g),latex(pi-g)),
                    '$\\hoac{&x=%s+k2\\pi \\\\& x=%s+k\\pi} (k \\in \\mathbb{Z}) $'%(latex(g),latex(pi-g)),
                    '$\\hoac{&x=%s+k2\\pi \\\\& x=%s+k\\pi} (k \\in \\mathbb{Z}) $'%(latex(g),latex(-g)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $\\cos x =%s$ có nghiệm là  \n'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\cos x =%s \\Leftrightarrow  \\cos x = \\cos %s \\Leftrightarrow \\hoac{&x=%s+k2\\pi \\\\ & x=-%s+k2\\pi} \\Leftrightarrow \\hoac{&x=%s+k2\\pi \\\\& x=%s+k2\\pi} (k \\in \\mathbb{Z})$. \\\\ \n'

                        %(latex(a),latex(g),latex(g),latex(g),latex(g),latex(-g)
                        ))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('0+k', 'k')
            return content

