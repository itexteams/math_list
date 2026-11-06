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


def bt_dang4_p1_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-3,0)
                x2=randint(1,3)

                f=x**2-(x1+x2)*x+x1*x2

                a=x2+1 
                b=a+2

                y=Rational(1,3)*x**3-Rational(x1+x2,2)*x**2+x1*x2*x

                fx1=Rational(1,3)*x1**3-Rational(x1+x2,2)*x1**2+x1*x2*x1
                fx2=Rational(1,3)*x2**3-Rational(x1+x2,2)*x2**2+x1*x2*x2
                kq=abs(fx2-fx1)

                du = ['$%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y=%s$ với trục hoành là'
                                %(latex(f)
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
                        '\\hspace*{1cm} $%s=0 \\Leftrightarrow \\hoac{& x=%s \\\\ & x=%s}$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        'Diện tích hình phẳng cần tìm là $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x=%s$.'
                        %(latex(f),latex(x1),latex(x2),
                            latex(x1),latex(x2),latex(f),latex(kq)
                        ))
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-9,-6)
                x2=randint(1,3)

                f=x**2-(x1+x2)*x+x1*x2

                a=randint(-5,0)
                b=x2+2

                y=Rational(1,3)*x**3-Rational(x1+x2,2)*x**2+x1*x2*x

                fa=Rational(1,3)*a**3-Rational(x1+x2,2)*a**2+x1*x2*a
                fx2=Rational(1,3)*x2**3-Rational(x1+x2,2)*x2**2+x1*x2*x2
                fb=Rational(1,3)*b**3-Rational(x1+x2,2)*b**2+x1*x2*b
                kq1=abs(fx2-fa)
                kq2=abs(fb-fx2)
                kq=kq1+kq2

                du = ['$%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$ là'
                                %(latex(f),latex(a),latex(b)
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
                        '\\hspace*{1cm} $%s=0 \\Leftrightarrow \\hoac{& x=%s \\\\ & x=%s}$. \\\\ \n'
                        'Nghiệm $x=%s$ thuộc đoạn $\\left[%s; %s \\right]$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        'Diện tích hình phẳng cần tìm là \\\\ \n'
                        '$S=\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x=\\left| \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)\\text{d}x \\right|+\\left|\\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)\\text{d}x \\right|=%s+%s=%s$.'
                        %(latex(f),latex(x1),latex(x2),
                        latex(x2),latex(a),latex(b),
                            latex(a),latex(b),latex(f),latex(a),latex(x2),latex(f),latex(x2),latex(b),latex(f),latex(kq1),latex(kq2),latex(kq)
                        ))
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-3,0)
                x2=randint(1,3)

                f=x**2-(x1+x2)*x+x1*x2

                a=x2+1 
                b=a+2

                y=Rational(1,3)*x**3-Rational(x1+x2,2)*x**2+x1*x2*x

                fa=Rational(1,3)*a**3-Rational(x1+x2,2)*a**2+x1*x2*a
                fx2=Rational(1,3)*x2**3-Rational(x1+x2,2)*x2**2+x1*x2*x2
                fb=Rational(1,3)*b**3-Rational(x1+x2,2)*b**2+x1*x2*b
                kq=abs(fb-fa)

                du = ['$%s$'%(latex(kq)),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq+1)),
                    '$%s$'%(latex(kq+2)),
                    '$%s$'%(latex(kq+3)),
                    '$%s$'%(latex(kq-1)),
                    '$%s$'%(latex(kq-2)),
                    '$%s$'%(latex(kq-3)),

                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y=%s$, trục hoành và hai đường thẳng $x=%s, x=%s$ là'
                                %(latex(f),latex(a),latex(b)
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
                        '\\hspace*{1cm} $%s=0 \\Leftrightarrow \\hoac{& x=%s \\\\ & x=%s}$. \\\\ \n'
                        'Các nghiệm của phương trình không thuộc đoạn $\\left[%s; %s \\right]$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        'Diện tích hình phẳng cần tìm là $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x=%s$.'
                        %(latex(f),latex(x1),latex(x2),
                        latex(a),latex(b),
                            latex(a),latex(b),latex(f),latex(kq)
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

