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


def bt_dang9_p1_b1_c1_hh10(self):
            #Khai báo biến
            a = randint(1,20) # a là số bất kỳ từ 1 đến 25
            b=Rational(1,(1+(a)**2))
            c=sqrt(1-b)
            d=sqrt(b)
            list3=['dang1','dang2','dang3','dang4','dang5','dang6','dang7','dang8',]
            rd = random.choice(list3)
            #Nội ung câu hỏi
            if rd=='dang1':
                noidungcauhoi = ('''Cho $\\tan\\alpha=%s$, với $0^\\circ<\\alpha<90^\\circ$. Giá trị của $\\cos\\alpha$ là\n'''
                            %(latex(a)))
            # Các đáp án
                da_d = '\\True $%s$'%(latex(d))
                da_s1 = '$%s$'%(latex(-d))
                da_s2 = '$%s$'%(latex(1/d))
                da_s3 = '$%s$'%(latex(-1/d))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $1+\\tan^2\\alpha=\\dfrac{1}{\\cos^2\\alpha }\\Leftrightarrow \\cos^2\\alpha=\\dfrac{1}{1+\\tan^2\\alpha}$\\\\ \n'
                        '$\\Leftrightarrow\\cos^2\\alpha=\\dfrac{1}{1+\\left(%s\\right)^2}= %s\\Leftrightarrow \\cos\\alpha = \\pm %s$.\\\\ \n'
                        'Vì $0^\\circ<\\alpha<90^\\circ$ nên $\\cos\\alpha>0 \\Rightarrow \\cos\\alpha=%s$ \\\\ \n'
                        'Vậy $\\cos\\alpha=%s$.'
                    %(latex(a),latex(b),latex(d),latex(d),latex(d)))
            if rd=='dang2':
                noidungcauhoi = ('''Cho $\\cot\\alpha=%s$, với $0^\\circ<\\alpha<90^\\circ$. Giá trị của $\\sin\\alpha$ là\n'''
                            %(latex(a)))
            # Các đáp án
                da_d = '\\True $%s$'%(latex(d))
                da_s1 = '$%s$'%(latex(-d))
                da_s2 = '$%s$'%(latex(1/d))
                da_s3 = '$%s$'%(latex(-1/d))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $1+\\cot^2\\alpha=\\dfrac{1}{\\sin^2\\alpha }\\Leftrightarrow \\sin^2\\alpha=\\dfrac{1}{1+\\cot^2\\alpha}$\\\\ \n'
                        '$\\Leftrightarrow\\sin^2\\alpha=\\dfrac{1}{1+\\left(%s\\right)^2}= %s\\Leftrightarrow \\sin\\alpha = \\pm %s$.\\\\ \n'
                        'Vì $0^\\circ<\\alpha<90^\\circ$ nên $\\sin\\alpha>0 \\Rightarrow \\sin\\alpha=%s$ \\\\ \n'
                        'Vậy $\\sin\\alpha=%s$.'
                    %(latex(a),latex(b),latex(d),latex(d),latex(d)))
            if rd=='dang3':
                noidungcauhoi = ('''Cho $\\tan\\alpha=%s$, với $90^\\circ<\\alpha<180^\\circ$. Giá trị của $\\cos\\alpha$ là\n'''
                            %(latex(-a)))
            # Các đáp án
                da_d = '\\True $%s$'%(latex(-d))
                da_s1 = '$%s$'%(latex(d))
                da_s2 = '$%s$'%(latex(1/d))
                da_s3 = '$%s$'%(latex(-1/d))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $1+\\tan^2\\alpha=\\dfrac{1}{\\cos^2\\alpha }\\Leftrightarrow \\cos^2\\alpha=\\dfrac{1}{1+\\tan^2\\alpha}$\\\\ \n'
                        '$\\Leftrightarrow\\cos^2\\alpha=\\dfrac{1}{1+\\left(-%s\\right)^2}= %s\\Leftrightarrow \\cos\\alpha = \\pm %s$.\\\\ \n'
                        'Vì $90^\\circ<\\alpha<180^\\circ$ nên $\\cos\\alpha<0 \\Rightarrow \\cos\\alpha=-%s$ \\\\ \n'
                        'Vậy $\\cos\\alpha=-%s$.'
                    %(latex(a),latex(b),latex(d),latex(d),latex(d)))
            if rd=='dang4':
                noidungcauhoi = ('''Cho $\\cot\\alpha=%s$, với $90^\\circ<\\alpha<180^\\circ$. Giá trị của $\\sin\\alpha$ là\n'''
                            %(latex(-a)))
            # Các đáp án
                da_d = '\\True $%s$'%(latex(d))
                da_s1 = '$%s$'%(latex(-d))
                da_s2 = '$%s$'%(latex(1/d))
                da_s3 = '$%s$'%(latex(-1/d))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $1+\\cot^2\\alpha=\\dfrac{1}{\\sin^2\\alpha }\\Leftrightarrow \\sin^2\\alpha=\\dfrac{1}{1+\\cot^2\\alpha}$\\\\ \n'
                        '$\\Leftrightarrow\\sin^2\\alpha=\\dfrac{1}{1+\\left(-%s\\right)^2}= %s\\Leftrightarrow \\sin\\alpha = \\pm %s$.\\\\ \n'
                        'Vì $90^\\circ<\\alpha<180^\\circ$ nên $\\sin\\alpha>0 \\Rightarrow \\sin\\alpha=%s$ \\\\ \n'
                        'Vậy $\\sin\\alpha=%s$.'
                    %(latex(a),latex(b),latex(d),latex(d),latex(d)))

            if rd=='dang5':
                noidungcauhoi = ('''Cho $\\tan\\alpha=%s$, với $0^\\circ<\\alpha<90^\\circ$. Giá trị của $\\sin\\alpha$ là\n'''
                            %(latex(a)))
            # Các đáp án
                da_d = '\\True $%s$'%(latex(c))
                da_s1 = '$%s$'%(latex(-c))
                da_s2 = '$%s$'%(latex(1/c))
                da_s3 = '$%s$'%(latex(-1/c))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $1+\\tan^2\\alpha=\\dfrac{1}{\\cos^2\\alpha }\\Leftrightarrow \\cos^2\\alpha=\\dfrac{1}{1+\\tan^2\\alpha}$\\\\ \n'
                        '$\\Leftrightarrow\\cos^2\\alpha=\\dfrac{1}{1+\\left(%s\\right)^2}= %s$.\\\\ \n'
                        'Mặt khác $\\sin^2\\alpha=1-\\cos^2\\alpha\\Leftrightarrow \\sin^2\\alpha=1-\\left(%s\\right)=%s\\Leftrightarrow \\sin\\alpha=\\pm%s$.\\\\ \n'
                        'Vì $0^\\circ<\\alpha<90^\\circ$ nên $\\sin\\alpha>0$ \\\\ \n'
                        'Vậy $\\sin\\alpha=%s$.'
                    %(latex(a),latex(b),
                    latex(b),latex(1-b),latex(c),latex(c)))
            if rd=='dang6':
                noidungcauhoi = ('''Cho $\\cot\\alpha=%s$, với $0^\\circ<\\alpha<90^\\circ$. Giá trị của $\\cos\\alpha$ là\n'''
                            %(latex(a)))
            # Các đáp án
                da_d = '\\True $%s$'%(latex(c))
                da_s1 = '$%s$'%(latex(-c))
                da_s2 = '$%s$'%(latex(1/c))
                da_s3 = '$%s$'%(latex(-1/c))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $1+\\cot^2\\alpha=\\dfrac{1}{\\sin^2\\alpha }\\Leftrightarrow \\sin^2\\alpha=\\dfrac{1}{1+\\cot^2\\alpha}$\\\\ \n'
                        '$\\Leftrightarrow\\sin^2\\alpha=\\dfrac{1}{1+\\left(%s\\right)^2}= %s$.\\\\ \n'
                        'Mặt khác $\\cos^2\\alpha=1-\\sin^2\\alpha\\Leftrightarrow \\cos^2\\alpha=1-\\left(%s\\right)=%s\\Leftrightarrow \\cos\\alpha=\\pm%s$.\\\\ \n'
                        'Vì $0^\\circ<\\alpha<90^\\circ$ nên $\\cos\\alpha>0$ \\\\ \n'
                        'Vậy $\\cos\\alpha=%s$.'
                    %(latex(a),latex(b),
                    latex(b),latex(1-b),latex(c),latex(c)))
            if rd=='dang7':
                noidungcauhoi = ('''Cho $\\tan\\alpha=%s$, với $90^\\circ<\\alpha<180^\\circ$. Giá trị của $\\sin\\alpha$ là\n'''
                            %(latex(-a)))
            # Các đáp án
                da_d = '\\True $%s$'%(latex(c))
                da_s1 = '$%s$'%(latex(-c))
                da_s2 = '$%s$'%(latex(1/c))
                da_s3 = '$%s$'%(latex(-1/c))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $1+\\tan^2\\alpha=\\dfrac{1}{\\cos^2\\alpha }\\Leftrightarrow \\cos^2\\alpha=\\dfrac{1}{1+\\tan^2\\alpha}$\\\\ \n'
                        '$\\Leftrightarrow\\cos^2\\alpha=\\dfrac{1}{1+\\left(-%s\\right)^2}= %s$.\\\\ \n'
                        'Mặt khác $\\sin^2\\alpha=1-\\cos^2\\alpha\\Leftrightarrow \\sin^2\\alpha=1-\\left(%s\\right)=%s\\Leftrightarrow \\sin\\alpha=\\pm%s$.\\\\ \n'
                        'Vì $90^\\circ<\\alpha<180^\\circ$ nên $\\sin\\alpha>0$ \\\\ \n'
                        'Vậy $\\sin\\alpha=%s$.'
                    %(latex(a),latex(b),
                    latex(b),latex(1-b),latex(c),latex(c)))
            if rd=='dang8':
                noidungcauhoi = ('''Cho $\\cot\\alpha=%s$, với $90^\\circ<\\alpha<180^\\circ$. Giá trị của $\\cos\\alpha$ là\n'''
                            %(latex(-a)))
            # Các đáp án
                da_d = '\\True $%s$'%(latex(-c))
                da_s1 = '$%s$'%(latex(c))
                da_s2 = '$%s$'%(latex(1/c))
                da_s3 = '$%s$'%(latex(-1/c))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Ta có: $1+\\cot^2\\alpha=\\dfrac{1}{\\sin^2\\alpha }\\Leftrightarrow \\sin^2\\alpha=\\dfrac{1}{1+\\cot^2\\alpha}$\\\\ \n'
                        '$\\Leftrightarrow\\sin^2\\alpha=\\dfrac{1}{1+\\left(-%s\\right)^2}= %s$.\\\\ \n'
                        'Mặt khác $\\cos^2\\alpha=1-\\sin^2\\alpha\\Leftrightarrow \\cos^2\\alpha=1-\\left(%s\\right)=%s\\Leftrightarrow \\cos\\alpha=\\pm%s$.\\\\ \n'
                        'Vì $90^\\circ<\\alpha<180^\\circ$ nên $\\cos\\alpha<0$ \\\\ \n'
                        'Vậy $\\cos\\alpha=%s$.'
                    %(latex(a),latex(b),
                    latex(b),latex(1-b),latex(c),latex(-c)))
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n {'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n }'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n') .replace('--','').replace('\\frac','\\dfrac').replace('+-','-').replace('++','+')     
            return content   

