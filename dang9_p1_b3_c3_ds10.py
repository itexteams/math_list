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


def bt_dang9_p1_b3_c3_ds10(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x1=randint(50,70)
                x2=randint(60,90)
                x3=randint(-10,30)
                x4=randint(80,100)
                dq=x2-x1
                m1=x1-1.5*dq
                m2=x2+1.5*dq
                while x1>=x2 or x3>=m1 or x4>=m2:
                    x1=randint(50,70)
                    x2=randint(60,90)
                    x3=randint(-10,20)
                    x4=randint(90,140)
                    dq=x2-x1
                    m1=x1-1.5*dq
                    m2=x2+1.5*dq

                # Câu hỏi
                noidungcauhoi = ('Một mẫu số liệu có tứ phân vị thứ nhất là $%s$ và tứ phân vị thứ ba là $%s$$zz$ Hãy kiểm tra '
                                'xem trong các giá trị $%s$ và $%s$ giá trị nào được xem là giá trị bất thường?'
                                %(latex(x1),latex(x2),latex(x3),latex(x4)))
                du = ['$%s$'%(latex(x3)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(x2)),
                    'Cả hai giá trị',
                    'Không có giá trị nào',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Ta có ${{\\Delta }_{Q}}=Q_1-Q_2=%s-%s=%s$$zz$\\\\ \n'
                        'Khi đó  $Q_1-1,5{\\Delta }_{Q}=%s-1,5\\cdot%s=%s$$zz$\\\\ \n'
                        '\\hspace*{1.37cm}$Q_2+1,5{\\Delta }_{Q}=%s+1,5\\cdot%s=%s$$zz$\\\\ \n'
                        'Nên trong hai giá trị đó thì giá trị $%s$ (nhỏ hơn $%s$) là giá trị bất thường$zz$'
                                %(latex(x2),latex(x1),latex(dq),latex(x1),latex(dq),latex(x1-1.5*dq),latex(x2),latex(dq),latex(x2+1.5*dq),
                                latex(x3),latex(x1-1.5*dq)
                                ))

            if dang=='2':
                # Khai báo biến
                x1=randint(50,70)
                x2=randint(60,90)
                x3=randint(20,50)
                x4=randint(80,100)
                dq=x2-x1
                m1=x1-1.5*dq
                m2=x2+1.5*dq
                while x1>=x2 or x3<=m1 or x4<=m2:
                    x1=randint(50,70)
                    x2=randint(60,90)
                    x3=randint(-10,20)
                    x4=randint(90,140)
                    dq=x2-x1
                    m1=x1-1.5*dq
                    m2=x2+1.5*dq

                # Câu hỏi
                noidungcauhoi = ('Một mẫu số liệu có tứ phân vị thứ nhất là $%s$ và tứ phân vị thứ ba là $%s$$zz$ Hãy kiểm tra '
                                'xem trong các giá trị $%s$ và $%s$ giá trị nào được xem là giá trị bất thường?'
                                %(latex(x1),latex(x2),latex(x3),latex(x4)))
                du = ['$%s$'%(latex(x4)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(x1)),
                    'Cả hai giá trị',
                    'Không có giá trị nào',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Ta có ${{\\Delta }_{Q}}=Q_1-Q_2=%s-%s=%s$$zz$\\\\ \n'
                        'Khi đó  $Q_1-1,5{\\Delta }_{Q}=%s-1,5\\cdot%s=%s$ \\\\ \n'
                        '\\hspace*{1.37cm} $Q_2+1,5{\\Delta }_{Q}=%s+1,5\\cdot%s=%s$$zz$\\\\ \n'
                        'Nên trong hai giá trị đó thì giá trị $%s$ (lớn hơn $%s$) là giá trị bất thường$zz$'
                                %(latex(x2),latex(x1),latex(dq),latex(x1),latex(dq),latex(x1-1.5*dq),latex(x2),latex(dq),latex(x2+1.5*dq),
                                latex(x4),latex(x2+1.5*dq)
                                ))

            if dang=='3':
                # Khai báo biến
                x1=randint(50,70)
                x2=randint(60,90)
                x3=randint(20,50)
                x4=randint(80,100)
                dq=x2-x1
                m1=x1-1.5*dq
                m2=x2+1.5*dq
                while x1>=x2 or x3<=m1 or x4<=m2:
                    x1=randint(50,70)
                    x2=randint(60,90)
                    x3=randint(-10,20)
                    x4=randint(90,140)
                    dq=x2-x1
                    m1=x1-1.5*dq
                    m2=x2+1.5*dq

                # Câu hỏi
                noidungcauhoi = ('Một mẫu số liệu có tứ phân vị thứ nhất là $%s$ và tứ phân vị thứ ba là $%s$$zz$ Hãy kiểm tra '
                                'xem trong các giá trị $%s$ và $%s$ giá trị nào được xem là giá trị bất thường?'
                                %(latex(x1),latex(x2),latex(x1-1.5*dq+1),latex(x2+1.5*dq-1)))
                du = ['Không có giá trị nào',
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(x1)),
                    'Cả hai giá trị',
                    '$%s$'%(latex(x2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Ta có ${{\\Delta }_{Q}}=Q_1-Q_2=%s-%s=%s$$zz$\\\\ \n'
                        'Khi đó  $Q_1-1,5{\\Delta }_{Q}=%s-1,5\\cdot%s=%s$$zz$ \\\\ \n' 
                            '\\hspace*{1.37cm}$Q_2+1,5{\\Delta }_{Q}=%s+1,5\\cdot%s=%s$$zz$\\\\ \n'
                        'Nên trong hai giá trị đó thì không có giá trị nào là giá trị bất thường$zz$'
                                %(latex(x2),latex(x1),latex(dq),latex(x1),latex(dq),latex(x1-1.5*dq),latex(x2),latex(dq),latex(x2+1.5*dq),

                                ))

            if dang=='4':
                # Khai báo biến
                x1=randint(50,70)
                x2=randint(60,90)
                x3=randint(20,50)
                x4=randint(80,100)
                dq=x2-x1
                m1=x1-1.5*dq
                m2=x2+1.5*dq
                while x1>=x2 or x3<=m1 or x4<=m2:
                    x1=randint(50,70)
                    x2=randint(60,90)
                    x3=randint(-10,20)
                    x4=randint(90,140)
                    dq=x2-x1
                    m1=x1-1.5*dq
                    m2=x2+1.5*dq

                # Câu hỏi
                noidungcauhoi = ('Một mẫu số liệu có tứ phân vị thứ nhất là $%s$ và tứ phân vị thứ ba là $%s$$zz$ Hãy kiểm tra '
                                'xem trong các giá trị $%s$ và $%s$ giá trị nào được xem là giá trị bất thường?'
                                %(latex(x1),latex(x2),latex(x1-1.5*dq-1),latex(x2+1.5*dq+1)))
                du = ['Cả hai giá trị',
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(x1)),
                    'Không có giá trị nào',
                    '$%s$'%(latex(x2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= ('Ta có ${{\\Delta }_{Q}}=Q_1-Q_2=%s-%s=%s$$zz$\\\\ \n'
                        'Khi đó  $Q_1-1,5{\\Delta }_{Q}=%s-1,5\\cdot%s=%s>%s$$zz$ \\\\ \n' 
                            '\\hspace*{1.37cm}$Q_2+1,5{\\Delta }_{Q}=%s+1,5\\cdot%s=%s<%s$$zz$\\\\ \n'
                        'Nên trong hai giá trị đó thì cả hai giá trị đều là giá trị bất thường$zz$'
                                %(latex(x2),latex(x1),latex(dq),latex(x1),latex(dq),latex(x1-1.5*dq),latex(x1-1.5*dq-1),latex(x2),latex(dq),latex(x2+1.5*dq),latex(x2+1.5*dq+1)

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace(',0', '')
            return content

