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


def bt_dang1_p1_b4_c5_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)

            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,5)
                b=randint(1,5)
                lism=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                m=random.choice(lism)
                n=randint(-9,9)
                pt=Eq((Rational(1,a))**(m*x+n),a**b)
                x0=Rational(-b-n,m)


                du = ['$x=%s$'%(latex(x0)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(x0+1)),
                    '$x=%s$'%(latex(x0+2)),
                    '$x=%s$'%(latex(x0+3)),
                    '$x=%s$'%(latex(x0-1)),
                    '$x=%s$'%(latex(x0-2)),
                    '$x=%s$'%(latex(x0-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $%s$ có nghiệm là'
                                %(latex(pt)
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
                        '\\hspace*{1cm} $%s \\Leftrightarrow %s=\\log_{\\tfrac{1}{%s}} {%s} \\Leftrightarrow %s=%s \\Leftrightarrow x=%s$.'
                        %(latex(pt),latex((m*x+n)),latex(a),latex(a**b),latex(m*x+n),latex(-b),latex(x0)
                        ))

            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                a=randint(2,5)
                b=randint(1,5)
                lism=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                m=random.choice(lism)
                n=randint(-9,9)
                pt=Eq(a**(m*x+n),a**b)
                x0=Rational(b-n,m)


                du = ['$x=%s$'%(latex(x0)),
                    ]
                da= random.choice(du)
                s = ['$x=%s$'%(latex(x0+1)),
                    '$x=%s$'%(latex(x0+2)),
                    '$x=%s$'%(latex(x0+3)),
                    '$x=%s$'%(latex(x0-1)),
                    '$x=%s$'%(latex(x0-2)),
                    '$x=%s$'%(latex(x0-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $%s$ có nghiệm là'
                                %(latex(pt)
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
                        '\\hspace*{1cm} $%s \\Leftrightarrow %s=\\log_{%s} {%s} \\Leftrightarrow %s=%s \\Leftrightarrow x=%s$.'
                        %(latex(pt),latex((m*x+n)),latex(a),latex(a**b),latex(m*x+n),latex(b),latex(x0)
                        ))
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                lisa=[3,5,7,9,11,13,15,17,19]
                lisb=[2,4,6,8,10,12,14,16,18,20]
                a=random.choice(lisa)
                b=random.choice(lisb)
                pt=Eq(a**x,b)


                du = ['$x=\\log_{%s} {%s} $'%(latex(a),latex(b)),
                    ]
                da= random.choice(du)
                s = ['$x=\\log_{%s} {%s} $'%(latex(a),latex(b+1)),
                    '$x=\\log_{%s} {%s} $'%(latex(a+1),latex(b)),
                    '$x=\\log_{%s} {%s} $'%(latex(a),latex(b+2)),
                    '$x=\\log_{%s} {%s} $'%(latex(a+2),latex(b)),
                    '$x=\\log_{%s} {%s} $'%(latex(a),latex(b+3)),
                    '$x=\\log_{%s} {%s} $'%(latex(a+3),latex(b)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $%s$ có nghiệm là'
                                %(latex(pt)
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
                        '\\hspace*{1cm} $%s \\Leftrightarrow x=\\log_{%s} {%s} $.'
                        %(latex(pt),latex(a),latex(b)
                        ))
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                lisa=[2,4,6,8,10,12,14,16,18,20]
                lisb=[3,5,7,9,11,13,15,17,19]
                a=random.choice(lisa)
                b=random.choice(lisb)
                pt=Eq(a**x,b)


                du = ['$x=\\log_{%s} {%s} $'%(latex(a),latex(b)),
                    ]
                da= random.choice(du)
                s = ['$x=\\log_{%s} {%s} $'%(latex(a),latex(b+1)),
                    '$x=\\log_{%s} {%s} $'%(latex(a+1),latex(b)),
                    '$x=\\log_{%s} {%s} $'%(latex(a),latex(b+2)),
                    '$x=\\log_{%s} {%s} $'%(latex(a+2),latex(b)),
                    '$x=\\log_{%s} {%s} $'%(latex(a),latex(b+3)),
                    '$x=\\log_{%s} {%s} $'%(latex(a+3),latex(b)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Phương trình $%s$ có nghiệm là'
                                %(latex(pt)
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
                        '\\hspace*{1cm} $%s \\Leftrightarrow x=\\log_{%s} {%s} $.'
                        %(latex(pt),latex(a),latex(b)
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

