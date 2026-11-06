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


def bt_dang4_p1_b1_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='3':
                # Khai báo biến

                a=randint(2,9)
                b=randint(-9,9)

                while a==b or b==0 or a==-b:

                    a=randint(2,9)
                    b=randint(-9,9)


                du = ['$%sx^3+%sx^2+%sx+\\text{C}$'%(latex(nsimplify(a**2/3)),latex(a*b),latex(b*b))
                    ]
                da= random.choice(du)
                s = ['$%sx^3+%sx^2+%sx+\\text{C}$'%(latex(nsimplify(-a**2/3)),latex(a*b+1),latex(b*b+1)),
                    '$%sx^2+%sx+%s+\\text{C}$'%(latex(nsimplify(a**2)),latex(a*b+2),latex(b*b)),
                    '$%sx^3+%sx^2+%sx+\\text{C}$'%(latex(nsimplify(a)),latex(a*b+3),latex(b*b)),
                    '$%sx^3+%sx^2+%sx+\\text{C}$'%(latex(nsimplify(a**2/2)),latex(-a*b),latex(b*b+2))
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('$\\displaystyle \\int{\\left(%sx+%s\\right)^2 \\text{d}x}$ bằng'
                                %(latex(a),latex(b)
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
                loigiai=('Ta có\\\\ \n'
                        '\\begin{eqnarray*}\n'
                        '\\hspace*{1cm} \\displaystyle \\int{\\left(%sx+%s\\right)^2 \\text{d}x}&=&\\displaystyle \\int{\\left(%sx^2+%sx+%s\\right) \\text{d}x} \\\\ \n'
                        '&=&%sx^3+%sx^2+%sx+\\text{C}.\\\\ \n'
                        '\\end{eqnarray*}'
                        %(latex(a),latex(b),latex(a**2),latex(2*a*b),latex(b*b),
                        latex(nsimplify(a**2/3)),latex(a*b),latex(b*b))

                        )
            if dang=='2':
                # Khai báo biến
                lis1=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                x=symbols('x')
                a=random.choice(lis1)
                b=randint(-9,9)
                c=randint(-9,9)

                ham=2*a*x+b

                ng_h=a*x**2+b*x+c

                du = ['$%s$'%(latex(ng_h)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(a*x**2+(b-3)*x+c+1)),
                    '$%s$'%(latex(a*x**2+(b+1)*x+c+2)),
                    '$%s$'%(latex(a*x**2+(b+2)*x+c+3)),
                    '$%s$'%(latex(a*x**2+(b+3)*x+c-1)),
                    '$%s$'%(latex(a*x**2+(b-1)*x+c-2)),
                    '$%s$'%(latex(a*x**2+(b-2)*x+c-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hàm số $f(x)=%s$ có một nguyên hàm là \n'

                                %(latex(ham)

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
                loigiai=('Xét hàm số $F(x)=%s$. \\\\ \n'
                        'Ta có $F\'(x)=%s$ nên hàm số $F(x)$ là một nguyên hàm của hàm số $f(x)=%s$. \\\\ \n'

                        %(latex(ng_h),
                            latex(ham),latex(ham),
                        ))

            if dang=='1':
                # Khai báo biến
                lis1=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                x=symbols('x')
                a=random.choice(lis1)
                b=randint(-9,9)
                c=randint(-9,9)

                ham=2*a*x+b

                ng_h=a*x**2+b*x+c

                du = ['$y=%s$'%(latex(ham)),
                    ]
                da= random.choice(du)
                s = ['$y=%s$'%(latex(ham+1)),
                    '$y=%s$'%(latex(ham+2)),
                    '$y=%s$'%(latex(ham+3)),
                    '$y=%s$'%(latex(ham-1)),
                    '$y=%s$'%(latex(ham-2)),
                    '$y=%s$'%(latex(ham-3)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hàm số $F(x)=%s$ là một nguyên hàm của hàm số nào sau đây? \n'

                                %(latex(ng_h)

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
                loigiai=('Ta có $F\'(x)=%s$ nên hàm số $F(x)$ là một nguyên hàm của hàm số $y=%s$. \\\\ \n'

                        %(latex(ham),latex(ham),
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('{\\left(x \\right)}', ' x').replace('\\left(\\left|', ' \\left|').replace('\\right| \\right)', ' \\right|').replace('\\log', '\\ln').replace('+-', '-')
            return content

