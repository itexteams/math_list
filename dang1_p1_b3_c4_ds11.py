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


def bt_dang1_p1_b3_c4_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                lis1=[1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
                a1=random.choice(lis1)
                b1=random.choice(lis1)
                c1=random.choice(lis1)
                hs1=a1*x**2+b1*x+c1

                a2=random.choice(lis1)
                b2=random.choice(lis1)
                c2=random.choice(lis1)
                d2=random.choice(lis1)
                hs2=(a2*x+b2)/(c2*x+d2)

                a3=random.choice(lis1)
                b3=random.choice(lis1)
                hs3=sqrt(a3*x+b3)

                a4=random.choice(lis1)
                b4=random.choice(lis1)
                hs4=tan(a4*x+pi/b4)

                a5=random.choice(lis1)
                b5=random.choice(lis1)
                hs5=cot(a5*x+pi/b5)

                a6=random.choice(lis1)
                b6=random.choice(lis1)
                hs6=sin(a6*x+pi/b6)

                a7=random.choice(lis1)
                b7=random.choice(lis1)
                hs7=cos(a7*x+pi/b7)

                a8=random.choice(lis1)
                b8=random.choice(lis1)
                hs8=a8*x+b8

                #NHập đáp án đúng vào đây
                du = ['$y=%s$'%(latex(hs1)),
                    '$y=%s$'%(latex(hs6)),
                    '$y=%s$'%(latex(hs7)),
                    '$y=%s$'%(latex(hs8)),
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có \\\\ \n'
                        'Hàm số $y=%s$ có tập xác định là $\\mathscr{D}=\\mathbb{R}$ nên liên tục trên $\\mathbb{R}$.'%(latex(hs1) )),
                    ('Ta có \\\\ \n'
                            'Hàm số $y=%s$ có tập xác định là $\\mathscr{D}=\\mathbb{R}$ nên liên tục trên $\\mathbb{R}$.'%(latex(hs6) )),
                    ('Ta có \\\\ \n'
                            'Hàm số $y=%s$ có tập xác định là $\\mathscr{D}=\\mathbb{R}$ nên liên tục trên $\\mathbb{R}$.'%(latex(hs7) )),
                    ('Ta có \\\\ \n'
                            'Hàm số $y=%s$ có tập xác định là $\\mathscr{D}=\\mathbb{R}$ nên liên tục trên $\\mathbb{R}$.'%(latex(hs8) )),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$y=%s$'%(latex(hs2)),
                    '$y=%s$'%(latex(hs3)),
                    '$y=%s$'%(latex(hs4)),
                    '$y=%s$'%(latex(hs5)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hàm số nào sau đây liên trục trên $\\mathbb{R}$?'
                                %(
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
                loigiai= shuffled_solutions[0]


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

