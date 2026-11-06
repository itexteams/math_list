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


def bt_dang16_p1_b1_c4_ds10(self):
            #Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a=randint(1,9)
                b=randint(-9,9)
                c=randint(-9,-1)
                d=randint(-9,9)
                e=randint(-9,9)
                f=randint(-9,9)
                g=randint(-9,9)
                h=randint(-9,9)
                k=randint(-9,9)
                while a==0 or c==0 or e==0 or g==0 or h==0 or k>=-b/a or k>=-d/c:
                    x=symbols('x')
                    a=randint(1,9)
                    b=randint(-9,9)
                    c=randint(-9,-1)
                    d=randint(1,9)
                    e=randint(1,9)
                    f=randint(-9,9)
                    g=randint(-9,9)
                    h=randint(-9,9)
                    k=randint(-9,9)


                fx=a*x+b
                gx=c*x+d
                hx=e*x+f
                tx=g*x+h
                dau1=('+','-')
                dau=random.choice(dau1)
                x1=Rational(-b,a)
                x2=Rational(-d,c)
                x3=Rational(-f,e)
                # Câu hỏi
                noidungcauhoi = ('Tập xác định của hàm số $y=f(x)=\\heva{& \\dfrac{%s}{%s} &\\text{khi  } x\\le %s \\\\ & \\sqrt{%s} & \\text{khi  } x>%s}$ là'
                                %(latex(tx),latex(fx),latex(k),latex(gx),latex(k)))
                du = ['$\\mathscr{D}=\\left(-\\infty; %s\\right]$'%(latex(x2)),

                    ]
                da= random.choice(du)
                s = ['$\\mathscr{D}=\\left(-\\infty; %s\\right]$'%(latex(-x2)),
                    '$\\mathscr{D}=\\mathbb{R}\\backslash \\left\\{%s\\right\\}$'%(latex(x1)),
                    '$\\mathscr{D}=\\left(-\\infty; %s\\right] \\backslash \\left\\{%s\\right\\}$'%(latex(x2),latex(k)),
                    '$\\mathscr{D}=\\left( %s;+\\infty \\right)$'%(latex(x2)),
                    '$\\mathscr{D}=\\left( -\\infty,%s \\right)$'%(latex(x2)),
                    '$\\mathscr{D}=\\left[ %s;%s\\right]$'%(latex(x1),latex(x2)),

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
                loigiai=('Với $x\\le %s$ thì $%s\\ne0$ nên hàm số xác định với mọi $x\\le%s$. \\\\ \n'
                        'Với $x>%s$ hàm số xác định khi $%s\\ge0 \\Leftrightarrow x\\le%s$.\\\\ \n'
                        'Vậy tập xác định của hàm số là $\\mathscr{D}=\\left( -\\infty;%s \\right] \\cup \\left (%s;%s\\right]=\\left(-\\infty; %s\\right]$.'
                        %(latex(k),latex(fx),latex(k),
                        latex(k),latex(gx),latex(x2),
                        latex(k),latex(k),latex(x2),latex(x2),
                        )
                        )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+') 
            return content

