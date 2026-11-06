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


def bt_dang6_p1_b3_c2_hh10(self):
            # Khai báo biến
            lis1=[2,3,4,5,6,7,8,9,10,-2,-3,-4,-5,-6,-7,-8,-9]
            a=random.choice(lis1)
            b=random.choice(lis1)
            while b-a==0:
                a=random.choice(lis1)
                b=random.choice(lis1)
            c=random.choice(lis1)
            d=random.choice(lis1)
            lis2=['A','B','C','D','E','F','G','H','K','M','N','P','Q','O']
            d1=random.choice(lis2) #O
            lis2.remove(d1) 
            d2=random.choice(lis2) #M
            lis2.remove(d2)
            d3=random.choice(lis2) #N

            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho $\\vec{a} \\ne \\vec{0}$ và điểm $%s$. Gọi $%s, %s$ là hai điểm thỏa mãn $\\overrightarrow{%s%s}=%s \\vec{a}$ và $\\overrightarrow{%s%s}=%s \\vec{a}$. Khi đó  \n'
                                %(str(d1),str(d2),str(d3),str(d1),str(d2),latex(a),str(d1),str(d3),latex(b)
                                ))
                # Các đáp án
                da_d = '\\True $\\overrightarrow{%s%s}=%s \\vec{a}$' %(str(d2),str(d3),latex(b-a))
                da_s1 = '$\\overrightarrow{%s%s}=%s \\vec{a}$' %(str(d2),str(d3),latex(a-b))
                da_s2 = '$\\overrightarrow{%s%s}=%s \\vec{a}$' %(str(d2),str(d3),latex(b+a))
                da_s3 = '$\\overrightarrow{%s%s}=%s \\vec{a}$' %(str(d2),str(d3),latex(b-a+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\overrightarrow{%s%s}=\\overrightarrow{%s%s}-\\overrightarrow{%s%s}=%s \\vec{a}-(%s \\vec{a})=%s \\vec{a}$.'
                        %(str(d2),str(d3),str(d1),str(d3),str(d1),str(d2),latex(b),latex(a),latex(b-a)
                        ))
            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho $\\vec{a} \\ne \\vec{0}$ và điểm $%s$. Gọi $%s, %s$ là hai điểm thỏa mãn $\\overrightarrow{%s%s}=%s \\vec{a}$ và $\\overrightarrow{%s%s}=%s \\vec{a}$. Khi đó  \n'
                                %(str(d1),str(d2),str(d3),str(d1),str(d2),latex(a),str(d1),str(d3),latex(b)
                                ))
                # Các đáp án
                da_d = '\\True $%s\\overrightarrow{%s%s}+%s \\overrightarrow{%s%s}=%s \\vec{a}$' %(latex(c),str(d1),str(d2),latex(d),str(d1),str(d3),latex(c*a+d*b))
                da_s1 = '$%s\\overrightarrow{%s%s}+%s \\overrightarrow{%s%s}=%s \\vec{a}$' %(latex(c),str(d1),str(d2),latex(d),str(d1),str(d3),latex(c*a-d*b))
                da_s2 = '$%s\\overrightarrow{%s%s}+%s \\overrightarrow{%s%s}=%s \\vec{a}$' %(latex(c),str(d1),str(d2),latex(d),str(d1),str(d3),latex(d*a+c*b))
                da_s3 = '$%s\\overrightarrow{%s%s}+%s \\overrightarrow{%s%s}=%s \\vec{a}$' %(latex(c),str(d1),str(d2),latex(d),str(d1),str(d3),latex(d*a-c*b))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$%s\\overrightarrow{%s%s}+%s \\overrightarrow{%s%s} =%s (%s \\vec{a})+%s (%s \\vec{a})=%s \\vec{a}$.'
                        %(latex(c),str(d1),str(d2),latex(d),str(d1),str(d3),latex(c),latex(a),latex(d),latex(b),latex(c*a+d*b)
                        ))
            if dang=='3':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho $\\vec{a} \\ne \\vec{0}$ và điểm $%s$. Gọi $%s, %s$ là hai điểm thỏa mãn $\\overrightarrow{%s%s}=%s \\vec{a}$ và $\\overrightarrow{%s%s}=%s \\vec{a}$. Khi đó  \n'
                                %(str(d1),str(d2),str(d3),str(d1),str(d2),latex(a),str(d1),str(d3),latex(b)
                                ))
                # Các đáp án
                da_d = '\\True $\\overrightarrow{%s%s}=%s\\overrightarrow{%s%s}$' %(str(d2),str(d3),latex(Rational(b-a,a)),str(d1),str(d2))
                da_s1 = '$\\overrightarrow{%s%s}=%s\\overrightarrow{%s%s}$' %(str(d2),str(d3),latex(Rational(b,a)),str(d1),str(d2))
                da_s2 = '$\\overrightarrow{%s%s}=%s\\overrightarrow{%s%s}$' %(str(d2),str(d3),latex(Rational(b-a+1,b)),str(d1),str(d2))
                da_s3 = '$\\overrightarrow{%s%s}=%s\\overrightarrow{%s%s}$' %(str(d2),str(d3),latex(Rational(b+a,b)),str(d1),str(d2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\overrightarrow{%s%s}=\\overrightarrow{%s%s}-\\overrightarrow{%s%s}=%s \\vec{a}-(%s \\vec{a})=%s \\vec{a}$.\\\\ \n'
                        'Do đố \\\\ \n'
                        '$\\overrightarrow{%s%s}=%s\\overrightarrow{%s%s}$.'
                        %(str(d2),str(d3),str(d1),str(d3),str(d1),str(d2),latex(b),latex(a),latex(b-a),
                        str(d2),str(d3),latex(Rational(b-a,a)),str(d1),str(d2)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-')
            return content

