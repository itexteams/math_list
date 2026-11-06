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


def bt_dang10_p1_b3_c1_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)

            if dang=='6':
                # Khai báo biến
                lis=[1,-1,2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                x1=random.choice(lis)
                y1=random.choice(lis)
                z1=random.choice(lis)
                m1=random.choice(lis)
                m2=2*z1-m1
                while m2==m1+1 or m2==m1+2 or m2==m1+3 or m2==m1-1 or m2==m1-2 or m2==m1-3:
                    x1=random.choice(lis)
                    y1=random.choice(lis)
                    z1=random.choice(lis)
                    m1=random.choice(lis)
                    m2=2*z1-m1
                d=sqrt((x1)**2+y1**2+(m1-z1)**2)
                d1=(x1)**2+y1**2+(m1-z1)**2
                m=symbols('m')
                bt=m**2-2*z1*m+x1**2+y1**2+z1**2

                du = ['$M(0;0;%s)$'%(latex(m2)),
                    ]
                da= random.choice(du)
                s = ['$M(0;0;%s)$'%(latex(m2+1)),
                    '$M(0;0;%s)$'%(latex(m2+2)),
                    '$M(0;0;%s)$'%(latex(m2+3)),
                    '$M(0;0;%s)$'%(latex(m2-1)),
                    '$M(0;0;%s)$'%(latex(m2-2)),
                    '$M(0;0;%s)$'%(latex(m2-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $A(%s;%s;%s)$. Điểm $M$ thuộc trục $Oz$ thỏa mãn $AM=%s$ là  \n'
                                %(latex(x1),latex(y1),latex(z1),latex(d)
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
                loigiai=('Gọi $M(0;0;m)$ thuộc trục $Oz$, ta có \\\\ \n'
                        '\\hspace*{1cm} $\\vec{AM}=(%s;%s;m+%s)$ suy ra $AM=\\sqrt{(%s)^2+(%s)^2+(m+%s)^2}=\\sqrt{%s}$. \\\\ \n'
                        '\\hspace*{1cm} $AM=%s \\Leftrightarrow %s=%s \\Leftrightarrow \\hoac{& m=%s \\\\ & m=%s}$. \\\\ \n'
                        'Vậy điểm thỏa mãn bài toán là $M_1 (0;0;%s)$ và $M_2 (0;0;%s)$.'

                        %(latex(-x1),latex(-y1),latex(-z1),latex(-x1),latex(-y1),latex(-z1),latex(bt),
                        latex(d),latex(bt),latex(d1),latex(m1),latex(m2),
                        latex(m1),latex(m2)

                        ))

            if dang=='5':
                # Khai báo biến
                lis=[1,-1,2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                x1=random.choice(lis)
                y1=random.choice(lis)
                z1=random.choice(lis)
                m1=random.choice(lis)
                m2=2*z1-m1
                while m2==m1+1 or m2==m1+2 or m2==m1+3 or m2==m1-1 or m2==m1-2 or m2==m1-3:
                    x1=random.choice(lis)
                    y1=random.choice(lis)
                    z1=random.choice(lis)
                    m1=random.choice(lis)
                    m2=2*z1-m1
                d=sqrt((x1)**2+y1**2+(m1-z1)**2)
                d1=(x1)**2+y1**2+(m1-z1)**2
                m=symbols('m')
                bt=m**2-2*z1*m+x1**2+y1**2+z1**2

                du = ['$M(0;0;%s)$'%(latex(m1)),
                    ]
                da= random.choice(du)
                s = ['$M(0;0;%s)$'%(latex(m1+1)),
                    '$M(0;0;%s)$'%(latex(m1+2)),
                    '$M(0;0;%s)$'%(latex(m1+3)),
                    '$M(0;0;%s)$'%(latex(m1-1)),
                    '$M(0;0;%s)$'%(latex(m1-2)),
                    '$M(0;0;%s)$'%(latex(m1-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $A(%s;%s;%s)$. Điểm $M$ thuộc trục $Oz$ thỏa mãn $AM=%s$ là  \n'
                                %(latex(x1),latex(y1),latex(z1),latex(d)
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
                loigiai=('Gọi $M(0;0;m)$ thuộc trục $Oz$, ta có \\\\ \n'
                        '\\hspace*{1cm} $\\vec{AM}=(%s;%s;m+%s)$ suy ra $AM=\\sqrt{(%s)^2+(%s)^2+(m+%s)^2}=\\sqrt{%s}$. \\\\ \n'
                        '\\hspace*{1cm} $AM=%s \\Leftrightarrow %s=%s \\Leftrightarrow \\hoac{& m=%s \\\\ & m=%s}$. \\\\ \n'
                        'Vậy điểm thỏa mãn bài toán là $M_1 (0;0;%s)$ và $M_2 (0;0;%s)$.'

                        %(latex(-x1),latex(-y1),latex(-z1),latex(-x1),latex(-y1),latex(-z1),latex(bt),
                        latex(d),latex(bt),latex(d1),latex(m1),latex(m2),
                        latex(m1),latex(m2)

                        ))

            if dang=='4':
                # Khai báo biến
                lis=[1,-1,2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                x1=random.choice(lis)
                y1=random.choice(lis)
                z1=random.choice(lis)
                m1=random.choice(lis)
                m2=2*y1-m1
                while m2==m1+1 or m2==m1+2 or m2==m1+3 or m2==m1-1 or m2==m1-2 or m2==m1-3:
                    x1=random.choice(lis)
                    y1=random.choice(lis)
                    z1=random.choice(lis)
                    m1=random.choice(lis)
                    m2=2*y1-m1
                d=sqrt((x1)**2+(m1-y1)**2+z1**2)
                d1=(x1)**2+(m1-y1)**2+z1**2
                m=symbols('m')
                bt=m**2-2*y1*m+x1**2+y1**2+z1**2

                du = ['$M(0;%s;0)$'%(latex(m2)),
                    ]
                da= random.choice(du)
                s = ['$M(0;%s;0)$'%(latex(m2+1)),
                    '$M(0;%s;0)$'%(latex(m2+2)),
                    '$M(0;%s;0)$'%(latex(m2+3)),
                    '$M(0;%s;0)$'%(latex(m2-1)),
                    '$M(0;%s;0)$'%(latex(m2-2)),
                    '$M(0;%s;0)$'%(latex(m2-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $A(%s;%s;%s)$. Điểm $M$ thuộc trục $Oy$ thỏa mãn $AM=%s$ là \n'
                                %(latex(x1),latex(y1),latex(z1),latex(d)
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
                loigiai=('Gọi $M(0;m;0)$ thuộc trục $Oy$, ta có \\\\ \n'
                        '\\hspace*{1cm} $\\vec{AM}=(%s;m+%s;%s)$ suy ra $AM=\\sqrt{(%s)^2+(m+%s)^2+(%s)^2}=\\sqrt{%s}$. \\\\ \n'
                        '\\hspace*{1cm} $AM=%s \\Leftrightarrow %s=%s \\Leftrightarrow \\hoac{& m=%s \\\\ & m=%s}$. \\\\ \n'
                        'Vậy điểm thỏa mãn bài toán là $M_1 (0;%s;0)$ và $M_2 (0;%s;0)$.'

                        %(latex(-x1),latex(-y1),latex(-z1),latex(-x1),latex(-y1),latex(-z1),latex(bt),
                        latex(d),latex(bt),latex(d1),latex(m1),latex(m2),
                        latex(m1),latex(m2)

                        ))

            if dang=='3':
                # Khai báo biến
                lis=[1,-1,2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                x1=random.choice(lis)
                y1=random.choice(lis)
                z1=random.choice(lis)
                m1=random.choice(lis)
                m2=2*y1-m1
                while m2==m1+1 or m2==m1+2 or m2==m1+3 or m2==m1-1 or m2==m1-2 or m2==m1-3:
                    x1=random.choice(lis)
                    y1=random.choice(lis)
                    z1=random.choice(lis)
                    m1=random.choice(lis)
                    m2=2*y1-m1
                d=sqrt((x1)**2+(m1-y1)**2+z1**2)
                d1=(x1)**2+(m1-y1)**2+z1**2
                m=symbols('m')
                bt=m**2-2*y1*m+x1**2+y1**2+z1**2

                du = ['$M(0;%s;0)$'%(latex(m1)),
                    ]
                da= random.choice(du)
                s = ['$M(0;%s;0)$'%(latex(m1+1)),
                    '$M(0;%s;0)$'%(latex(m1+2)),
                    '$M(0;%s;0)$'%(latex(m1+3)),
                    '$M(0;%s;0)$'%(latex(m1-1)),
                    '$M(0;%s;0)$'%(latex(m1-2)),
                    '$M(0;%s;0)$'%(latex(m1-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $A(%s;%s;%s)$. Điểm $M$ thuộc trục $Oy$ thỏa mãn $AM=%s$ là  \n'
                                %(latex(x1),latex(y1),latex(z1),latex(d)
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
                loigiai=('Gọi $M(0;m;0)$ thuộc trục $Oy$, ta có \\\\ \n'
                        '\\hspace*{1cm} $\\vec{AM}=(%s;m+%s;%s)$ suy ra $AM=\\sqrt{(%s)^2+(m+%s)^2+(%s)^2}=\\sqrt{%s}$. \\\\ \n'
                        '\\hspace*{1cm} $AM=%s \\Leftrightarrow %s=%s \\Leftrightarrow \\hoac{& m=%s \\\\ & m=%s}$. \\\\ \n'
                        'Vậy điểm thỏa mãn bài toán là $M_1 (0;%s;0)$ và $M_2 (0;%s;0)$.'

                        %(latex(-x1),latex(-y1),latex(-z1),latex(-x1),latex(-y1),latex(-z1),latex(bt),
                        latex(d),latex(bt),latex(d1),latex(m1),latex(m2),
                        latex(m1),latex(m2)

                        ))

            if dang=='2':
                # Khai báo biến
                lis=[1,-1,2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                x1=random.choice(lis)
                y1=random.choice(lis)
                z1=random.choice(lis)
                m1=random.choice(lis)
                m2=2*x1-m1
                while m2==m1+1 or m2==m1+2 or m2==m1+3 or m2==m1-1 or m2==m1-2 or m2==m1-3:
                    x1=random.choice(lis)
                    y1=random.choice(lis)
                    z1=random.choice(lis)
                    m1=random.choice(lis)
                    m2=2*x1-m1
                d=sqrt((m1-x1)**2+y1**2+z1**2)
                d1=(m1-x1)**2+y1**2+z1**2
                m=symbols('m')
                bt=m**2-2*x1*m+x1**2+y1**2+z1**2

                du = ['$M(%s;0;0)$'%(latex(m2)),
                    ]
                da= random.choice(du)
                s = ['$M(%s;0;0)$'%(latex(m2+1)),
                    '$M(%s;0;0)$'%(latex(m2+2)),
                    '$M(%s;0;0)$'%(latex(m2+3)),
                    '$M(%s;0;0)$'%(latex(m2-1)),
                    '$M(%s;0;0)$'%(latex(m2-2)),
                    '$M(%s;0;0)$'%(latex(m2-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $A(%s;%s;%s)$. Điểm $M$ thuộc trục $Ox$ thỏa mãn $AM=%s$ là  \n'
                                %(latex(x1),latex(y1),latex(z1),latex(d)
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
                loigiai=('Gọi $M(m;0;0)$ thuộc trục $Ox$, ta có \\\\ \n'
                        '\\hspace*{1cm} $\\vec{AM}=(m+%s;%s;%s)$ suy ra $AM=\\sqrt{(m+%s)^2+(%s)^2+(%s)^2}=\\sqrt{%s}$. \\\\ \n'
                        '\\hspace*{1cm} $AM=%s \\Leftrightarrow %s=%s \\Leftrightarrow \\hoac{& m=%s \\\\ & m=%s}$. \\\\ \n'
                        'Vậy điểm thỏa mãn bài toán là $M_1 (%s;0;0)$ và $M_2 (%s;0;0)$.'

                        %(latex(-x1),latex(-y1),latex(-z1),latex(-x1),latex(-y1),latex(-z1),latex(bt),
                        latex(d),latex(bt),latex(d1),latex(m1),latex(m2),
                        latex(m1),latex(m2)

                        ))

            if dang=='1':
                # Khai báo biến
                lis=[1,-1,2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                x1=random.choice(lis)
                y1=random.choice(lis)
                z1=random.choice(lis)
                m1=random.choice(lis)
                m2=2*x1-m1
                while m2==m1+1 or m2==m1+2 or m2==m1+3 or m2==m1-1 or m2==m1-2 or m2==m1-3:
                    x1=random.choice(lis)
                    y1=random.choice(lis)
                    z1=random.choice(lis)
                    m1=random.choice(lis)
                    m2=2*x1-m1
                d=sqrt((m1-x1)**2+y1**2+z1**2)
                d1=(m1-x1)**2+y1**2+z1**2
                m=symbols('m')
                bt=m**2-2*x1*m+x1**2+y1**2+z1**2

                du = ['$M(%s;0;0)$'%(latex(m1)),
                    ]
                da= random.choice(du)
                s = ['$M(%s;0;0)$'%(latex(m1+1)),
                    '$M(%s;0;0)$'%(latex(m1+2)),
                    '$M(%s;0;0)$'%(latex(m1+3)),
                    '$M(%s;0;0)$'%(latex(m1-1)),
                    '$M(%s;0;0)$'%(latex(m1-2)),
                    '$M(%s;0;0)$'%(latex(m1-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho điểm $A(%s;%s;%s)$. Điểm $M$ thuộc trục $Ox$ thỏa mãn $AM=%s$ là  \n'
                                %(latex(x1),latex(y1),latex(z1),latex(d)
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
                loigiai=('Gọi $M(m;0;0)$ thuộc trục $Ox$, ta có \\\\ \n'
                        '\\hspace*{1cm} $\\vec{AM}=(m+%s;%s;%s)$ suy ra $AM=\\sqrt{(m+%s)^2+(%s)^2+(%s)^2}=\\sqrt{%s}$. \\\\ \n'
                        '\\hspace*{1cm} $AM=%s \\Leftrightarrow %s=%s \\Leftrightarrow \\hoac{& m=%s \\\\ & m=%s}$. \\\\ \n'
                        'Vậy điểm thỏa mãn bài toán là $M_1 (%s;0;0)$ và $M_2 (%s;0;0)$.'

                        %(latex(-x1),latex(-y1),latex(-z1),latex(-x1),latex(-y1),latex(-z1),latex(bt),
                        latex(d),latex(bt),latex(d1),latex(m1),latex(m2),
                        latex(m1),latex(m2)

                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

