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


def bt_dang3_p1_b4_c4_ds10(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-9,9)
                x2=randint(-9,9)
                while x1==x2 or x1==x2+1:
                    x1=randint(-9,9)
                    x2=randint(-9,9)
                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]
                d=random.choice(lis1)
                e=random.choice(lis)
                a=1+d**2 
                b=2*d*e-x1-x2
                c=x1*x2+e**2
                while True:
                    x = symbols('x')
                    x1 = random.randint(-9, 9)
                    x2 = random.randint(-9, 9)

                    # Đảm bảo x1 và x2 không bằng nhau
                    while x1 == x2:
                        x1 = random.randint(-9, 9)
                        x2 = random.randint(-9, 9)

                    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]
                    lis1=[1,2,3,4,5,6,7,8,9]
                    d=random.choice(lis1)
                    e=random.choice(lis)
                    a=1+d**2 
                    b=2*d*e-x1-x2
                    c=x1*x2+e**2

                    # Kiểm tra điều kiện
                    condition1 = d*x1+e<0
                    condition2 = d*x2+e<0

                    if condition1 and condition2:
                        break  # Thoát vòng lặp nếu cả hai điều kiện xảy ra

                f1=a*x**2+b*x+c
                f2=d*x+e
                f22=d**2*x**2+2*d*e*x+e**2
                f=x**2-(x1+x2)*x+x1*x2

                du = ['Vô nghiệm',
                    ]
                da= random.choice(du)
                s = ['$x=%s, x=%s$'%(latex(x1),latex(x2+1)),
                    '$x=%s$'%(latex(x2)),
                    '$x=%s$'%(latex(x2+1)),
                    '$x=%s, x=%s$'%(latex(x1),latex(x2)),        
                    '$x=%s$'%(latex(x1)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $\\sqrt{%s}=%s$ có nghiệm là'
                                %(latex(f1),latex(f2)
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
                loigiai=('Bình phương hai vế của phương trình, ta được \n'
                        '$$%s=%s.$$ \n'
                        'Sau khi thu gọn ta được $%s=0$. Từ đó $x=%s$ hoặc $x=%s$. \\\\ \n'
                        'Thay lần lượt hai giá trị này của $x$ vào phương trình đã cho ta thấy không thỏa mãn. \\\\ \n'
                        'Vậy phương trình đã cho vô nghiệm.'
                        %(latex(f1),latex(f22),
                        latex(f),latex(x1),latex(x2),
                        ))

            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-9,9)
                x2=randint(-9,9)
                while x1==x2 or x1==x2+1:
                    x1=randint(-9,9)
                    x2=randint(-9,9)
                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]
                d=random.choice(lis1)
                e=random.choice(lis)
                a=1+d**2 
                b=2*d*e-x1-x2
                c=x1*x2+e**2
                while True:
                    x = symbols('x')
                    x1 = random.randint(-9, 9)
                    x2 = random.randint(-9, 9)

                    # Đảm bảo x1 và x2 không bằng nhau
                    while x1 == x2:
                        x1 = random.randint(-9, 9)
                        x2 = random.randint(-9, 9)

                    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]
                    lis1=[1,2,3,4,5,6,7,8,9]
                    d=random.choice(lis1)
                    e=random.choice(lis)
                    a=1+d**2 
                    b=2*d*e-x1-x2
                    c=x1*x2+e**2

                    # Kiểm tra điều kiện
                    condition1 = d*x1+e>0
                    condition2 = d*x2+e<0

                    if condition1 and condition2:
                        break  # Thoát vòng lặp nếu cả hai điều kiện xảy ra

                f1=a*x**2+b*x+c
                f2=d*x+e
                f22=d**2*x**2+2*d*e*x+e**2
                f=x**2-(x1+x2)*x+x1*x2

                du = ['$x=%s$'%(latex(x1)),
                    ]
                da= random.choice(du)
                s = ['$x=%s, x=%s$'%(latex(x1),latex(x2+1)),
                    '$x=%s$'%(latex(x2)),
                    '$x=%s$'%(latex(x2+1)),
                    '$x=%s, x=%s$'%(latex(x1),latex(x2)),
                    'Vô nghiệm',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $\\sqrt{%s}=%s$ có nghiệm là'
                                %(latex(f1),latex(f2)
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
                loigiai=('Bình phương hai vế của phương trình, ta được \n'
                        '$$%s=%s.$$ \n'
                        'Sau khi thu gọn ta được $%s=0$. Từ đó $x=%s$ hoặc $x=%s$. \\\\ \n'
                        'Thay lần lượt hai giá trị này của $x$ vào phương trình đã cho ta thấy $x=%s$ thỏa mãn. \\\\ \n'
                        'Vậy nghiệm của phương trình đã cho là $x=%s$.'
                        %(latex(f1),latex(f22),
                        latex(f),latex(x1),latex(x2),
                        latex(x1),latex(x1),
                        ))

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-9,9)
                x2=randint(-9,9)
                while x1==x2 or x1==x2+1:
                    x1=randint(-9,9)
                    x2=randint(-9,9)
                lis=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                lis1=[1,2,3,4,5,6,7,8,9]
                d=random.choice(lis1)
                e=random.choice(lis)
                a=1+d**2 
                b=2*d*e-x1-x2
                c=x1*x2+e**2
                while True:
                    x = symbols('x')
                    x1 = random.randint(-9, 9)
                    x2 = random.randint(-9, 9)

                    # Đảm bảo x1 và x2 không bằng nhau
                    while x1 == x2:
                        x1 = random.randint(-9, 9)
                        x2 = random.randint(-9, 9)

                    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]
                    lis1=[1,2,3,4,5,6,7,8,9]
                    d=random.choice(lis1)
                    e=random.choice(lis)
                    a=1+d**2 
                    b=2*d*e-x1-x2
                    c=x1*x2+e**2

                    # Kiểm tra điều kiện
                    condition1 = d*x1+e>0
                    condition2 = d*x2+e>0

                    if condition1 and condition2:
                        break  # Thoát vòng lặp nếu cả hai điều kiện xảy ra

                f1=a*x**2+b*x+c
                f2=d*x+e
                f22=d**2*x**2+2*d*e*x+e**2
                f=x**2-(x1+x2)*x+x1*x2

                du = ['$x=%s, x=%s$'%(latex(x1),latex(x2)),
                    ]
                da= random.choice(du)
                s = ['$x=%s, x=%s$'%(latex(x1),latex(x2+1)),
                    '$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(x2)),
                    '$x=%s$'%(latex(x2+1)),
                    'Vô nghiệm',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $\\sqrt{%s}=%s$ có nghiệm là'
                                %(latex(f1),latex(f2)
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
                loigiai=('Bình phương hai vế của phương trình, ta được \n'
                        '$$%s=%s.$$ \n'
                        'Sau khi thu gọn ta được $%s=0$. Từ đó $x=%s$ hoặc $x=%s$. \\\\ \n'
                        'Thay lần lượt hai giá trị này của $x$ vào phương trình đã cho ta thấy cả hai nghiệm thỏa mãn. \\\\ \n'
                        'Vậy nghiệm của phương trình đã cho là $x=%s$ và $x=%s$.'
                        %(latex(f1),latex(f22),
                        latex(f),latex(x1),latex(x2),
                        latex(x1),latex(x2),
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

