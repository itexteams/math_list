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


def bt_dang6_p3_b2_c5_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                a=random.choice(lis)
                b=random.choice(lis)
                n=randint(2,9)
                m=randint(2,9)
                p=randint(2,9)
                kq=n+Rational(1,m)*a-p*b

                du = ['$%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq+4)),
                    '$%s$'%(latex(kq+5)),
                    '$%s$'%(latex(kq+6)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\log_a b=%s, \\log_a c=%s$. Giá trị biểu thức $P=\\log_a \\left( \\dfrac{a^%s \\sqrt[%s]{b}}{c^%s} \\right)$ bằng bao nhiêu?'
                                %(latex(a),latex(b),latex(n),latex(m),latex(p)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $P=\\log_a \\left( \\dfrac{a^%s \\sqrt[%s]{b}}{c^%s} \\right)=\\log_a a^%s \\sqrt[%s]{b} -\\log_a c^%s=\\log_a a^%s +\\log_a b^{\\tfrac{1}{%s}} -\\log_a c^%s$ \\\\ \n'
                        '\\hspace*{1cm} $P=%s \\log_a a +%s\\log_a b-%s \\log_a c=%s +%s \\cdot (%s) -%s \\cdot (%s)=%s$.'
                        %(latex(n),latex(m),latex(p),latex(n),latex(m),latex(p),latex(n),latex(m),latex(p),
                        latex(n),latex(Rational(1,m)),latex(p),
                        latex(n),latex(Rational(1,m)),latex(a),latex(p),latex(b),latex(kq)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            if dang=='2':
                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                a=random.choice(lis)
                b=random.choice(lis)
                n=randint(2,9)
                m=randint(2,9)
                p=randint(2,9)
                kq=n*a+m*b-p

                du = ['$%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq+4)),
                    '$%s$'%(latex(kq+5)),
                    '$%s$'%(latex(kq+6)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\log_a b=%s, \\log_a c=%s$. Giá trị biểu thức $Q=\\log_a \\left( \\dfrac{b^%s c^%s}{a^%s} \\right)$ bằng bao nhiêu?'
                                %(latex(a),latex(b),latex(n),latex(m),latex(p)
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $Q=\\log_a \\left( \\dfrac{b^%s c^%s}{a^%s} \\right)=\\log_a b^%s c^%s -\\log_a a^%s=\\log_a b^%s +\\log_a c^%s -\\log_a a^%s$ \\\\ \n'
                        '\\hspace*{1cm} $Q=%s \\log_a b +%s\\log_a c-%s \\log_a a=%s \\cdot (%s)+%s \\cdot (%s)-%s=%s$.'
                        %(latex(n),latex(m),latex(p),latex(n),latex(m),latex(p),latex(n),latex(m),latex(p),
                        latex(n),latex(m),latex(p),
                        latex(n),latex(a),latex(m),latex(b),latex(p),latex(kq)
                        ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

