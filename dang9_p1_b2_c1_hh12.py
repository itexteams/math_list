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


def bt_dang9_p1_b2_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                x=symbols('x')
                y=symbols('y')
                z=symbols('z')

                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]

                x1=random.choice(lis)
                y1=random.choice(lis)
                z1=random.choice(lis)

                x2=random.choice(lis)
                y2=random.choice(lis)
                z2=random.choice(lis)

                x3=random.choice(lis)
                y3=random.choice(lis)
                z3=random.choice(lis)

                x4=random.choice(lis)
                y4=random.choice(lis)
                z4=random.choice(lis)

                while x1/y1==x2/y2 or x1/z1==x2/z2 or x2/y2==x3/y3 or x2/z2==x3/z3:
                    x1=random.choice(lis)
                    y1=random.choice(lis)
                    z1=random.choice(lis)

                    x2=random.choice(lis)
                    y2=random.choice(lis)
                    z2=random.choice(lis)

                    x3=random.choice(lis)
                    y3=random.choice(lis)
                    z3=random.choice(lis)

                    x4=random.choice(lis)
                    y4=random.choice(lis)
                    z4=random.choice(lis)

                hsx=x1*x+x2*y+x3*z
                hsy=y1*x+y2*y+y3*z
                hsz=z1*x+z2*y+z3*z

                # Định nghĩa ma trận hệ số (A) và vectơ kết quả (B)
                A = np.array([[x1, x2, x3], 
                            [y1, y2, y3], 
                            [z1, z2, z3]])

                B = np.array([x4, y4, z4])

                # Giải hệ phương trình
                solution = np.linalg.solve(A, B)
                # Chuyển đổi nghiệm thành phân số
                n1 = Rational(solution[0]).limit_denominator()
                n2 = Rational(solution[1]).limit_denominator()
                n3 = Rational(solution[2]).limit_denominator()

                d = [
                    '$%s$'%(latex(n1+n2+n3)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(n1+n2+n3+1)),
                    '$%s$'%(latex(n1+n2+n3+2)),
                    '$%s$'%(latex(n1+n2+n3+3)),
                    '$%s$'%(latex(n1+n2+n3-1)),
                    '$%s$'%(latex(n1+n2+n3-2)),
                    '$%s$'%(latex(n1+n2+n3-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho các vectơ $\\vec{a}=(%s;%s;%s), \\vec{b}=(%s;%s;%s), \\vec{c}=(%s;%s;%s)$ và $\\vec{d}=(%s;%s;%s)$. Biết rằng $\\vec{d}=x \\vec{a} +y \\vec{b} +z \\vec{c}$, với $x, y, z$ là các số thực. Tổng $x+y+z$ bằng \n'
                                %(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2),latex(x3),latex(y3),latex(z3),latex(x4),latex(y4),latex(z4)
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
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $x \\vec{a}=(%s; %s; %s)$. \\\\ \n'
                        '\\hspace*{1cm} $y \\vec{b}=(%s; %s; %s)$. \\\\ \n'
                        '\\hspace*{1cm} $y \\vec{c}=(%s; %s; %s)$. \\\\ \n'
                        '\\hspace*{1cm} $x \\vec{a}+y \\vec{b}+z \\vec{c}=(%s; %s; %s)$. \\\\ \n'
                        'Suy ra $\\vec{d}=x \\vec{a} +y \\vec{b}+z \\vec{c} \\Leftrightarrow \\heva{& %s=%s \\\\ & %s=%s \\\\ & %s=%s} \\Leftrightarrow \\heva{& x=%s \\\\ & y=%s \\\\ & z=%s.}$ \\\\ \n'
                        'Vậy $x+y+z=%s$.'
                        %(latex(x1*x),latex(y1*x),latex(z1*x),
                        latex(x2*y),latex(y2*y),latex(z2*y),
                        latex(x3*z),latex(y3*z),latex(z3*z),
                        latex(hsx),latex(hsy),latex(hsz),
                        latex(hsx),latex(x4),latex(hsy),latex(y4),latex(hsz),latex(z4),
                        latex(n1),latex(n2),latex(n3),
                        latex(n1+n2+n3)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

