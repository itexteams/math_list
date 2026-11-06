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


def bt_dang9_p1_b2_c2_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                lisv=[5,10,15,20,25]
                v=random.choice(lisv)

                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong = xe1 + xe2 + xe3 + xe4 + xe5        

                lisk=[1,3,5,7]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)
                phuong_sai=Rational(xe1*x1**2+xe2*x2**2+xe3*x3**2+xe4*x4**2+xe5*x5**2,tong)-xtb**2
                do_lech=sqrt(phuong_sai)

                kq=xtb


                du = ['$\\bar{x}=%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(kq+1)),
                    '$\\bar{x}=%s$'%(latex(kq+2)),
                    '$\\bar{x}=%s$'%(latex(kq+3)),
                    '$\\bar{x}=%s$'%(latex(kq-1)),
                    '$\\bar{x}=%s$'%(latex(kq-2)),
                    '$\\bar{x}=%s$'%(latex(kq-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Một vườn thú ghi lại tuổi thọ (năm) của một số con hổ, kết quả được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Tuổi thọ (năm) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số con hổ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5)
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
                loigiai=('Cỡ mẫu $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm số liệu là \\\\ \n'
                        '\\hspace*{1cm} $x_1=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_2=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_3=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_4=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $x_5=\\dfrac{%s+%s}{2}=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{1}{%s}\\left( %s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s \\right)=%s$. \\\\ \n'

                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                        latex(v),latex(v+k),latex(x1),
                        latex(v+k),latex(v+2*k),latex(x2),
                        latex(v+2*k),latex(v+3*k),latex(xe3),
                        latex(v+3*k),latex(v+4*k),latex(x4),
                        latex(v+4*k),latex(v+5*k),latex(x5),
                        latex(tong),latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(xtb),
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0', '')
            return content

