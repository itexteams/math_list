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


def bt_dang17_p1_b1_c1_hh10(self):
            # Khai báo biến  
            lis=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
            a=random.choice(lis)
            lis0=[a,-a]
            b=random.choice(lis0)
            c=random.choice(lis)
            while c**2-2*a*b-3*a**2<=0:
                c=random.choice(lis)
                a=random.choice(lis)
            kq=Rational(c**2-2*a*b,a**2)

            kq11=Rational(c**2-2*a*a,a**2)
            kq1=Rational(c*(kq11-1),a)
            lis=['4']
            dang=random.choice(lis)
            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Cho $%s \\tan a +%s \\cot a =%s$. Giá trị $\\tan^{2} a + \\cot^{2} a$ là  \n'''
                            %(latex(a),latex(b),latex(c)
                                ))
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(kq))
                da_s1 = '$P=%s$'%(latex(kq+1))
                da_s2 = '$P=%s$'%(latex(kq-1))
                da_s3 = '$P=%s$'%(latex(kq-2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\left( %s \\tan a +%s \\cot a \\right)^2=(%s)^2 \\Leftrightarrow %s \\tan^{2}a +%s \\tan  a \\cot a +%s \\cot^{2}a =%s$\\\\ \n'
                        '$\\Leftrightarrow  %s \\left( \\tan^{2} a + \\cot^{2} a \\right) +%s \\tan  a \\cot a =%s \\Leftrightarrow \\tan^{2} a + \\cot^{2} a =\\dfrac{%s-%s}{%s} =%s$.'
                        %(latex(a),latex(b),latex(c),latex(a**2),latex(2*a*b),latex(b**2),latex(c**2),
                        latex(a**2),latex(2*a*b),latex(c**2),latex(c**2),latex(2*a*b),latex(a**2),latex(kq),
                            ))
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Cho $%s \\tan a +%s \\cot a =%s$. Giá trị $\\tan^{3} a + \\cot^{3} a$ là  \n'''
                            %(latex(a),latex(a),latex(c)
                                ))
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(kq1))
                da_s1 = '$P=%s$'%(latex(kq1+1))
                da_s2 = '$P=%s$'%(latex(kq1-1))
                da_s3 = '$P=%s$'%(latex(kq1-2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\tan a + \\cot a = %s$.\\\\ \n'
                        '$\\left( %s \\tan a +%s \\cot a \\right)^2=(%s)^2 \\Leftrightarrow %s \\tan^{2}a +%s \\tan  a \\cot a +%s \\cot^{2}a =%s$\\\\ \n'
                        '$\\Leftrightarrow  %s \\left( \\tan^{2} a + \\cot^{2} a \\right) +%s \\tan  a \\cot a =%s \\Leftrightarrow \\tan^{2} a + \\cot^{2} a =\\dfrac{%s-%s}{%s} =%s$.\\\\ \n'
                        'Suy ra \\\\ \n'
                        '$\\tan^{3} a + \\cot^{3} a = \\left( \\tan a + \\cot a \\right) \\left( \\tan^{2} a + \\cot^{2} a - \\tan a \\cot a \\right) = \\left( \\tan a + \\cot a \\right) \\left( \\tan^{2} a + \\cot^{2} a -1 \\right)$\\\\ \n'
                        '$\\tan^{3} a + \\cot^{3} a = %s \\left( %s -1 \\right) =%s$.'
                        %(latex(Rational(c,a)),
                            latex(a),latex(a),latex(c),latex(a**2),latex(2*a*a),latex(a**2),latex(c**2),
                        latex(a**2),latex(2*a*a),latex(c**2),latex(c**2),latex(2*a*a),latex(a**2),latex(kq11),
                        latex(Rational(c,a)),latex(kq11),latex(kq1)
                            ))
            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('''Cho $%s \\tan a +%s \\cot a =%s$. Giá trị $\\tan^{4} a + \\cot^{4} a$ là  \n'''
                            %(latex(a),latex(b),latex(c)
                                ))
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(kq**2-2))
                da_s1 = '$P=%s$'%(latex(kq**2-2+1))
                da_s2 = '$P=%s$'%(latex(kq**2-2-1))
                da_s3 = '$P=%s$'%(latex(kq**2-2-2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\left( %s \\tan a +%s \\cot a \\right)^2=(%s)^2 \\Leftrightarrow %s \\tan^{2}a +%s \\tan  a \\cot a +%s \\cot^{2}a =%s$\\\\ \n'
                        '$\\Leftrightarrow  %s \\left( \\tan^{2} a + \\cot^{2} a \\right) +%s \\tan  a \\cot a =%s \\Leftrightarrow \\tan^{2} a + \\cot^{2} a =\\dfrac{%s-%s}{%s} =%s$.\\\\ \n'
                        'Mặt khác \\\\ \n'
                        '$\\left( \\tan^{2} a + \\cot^{2} a \\right)^2 = \\tan^{4}a + \\cot^{4}a +2 \\tan^{2}a \\cot^{2}a = \\tan^{4}a + \\cot^{4}a +2$.\\\\ \n'
                        'Suy ra \\\\ \n'
                        '$\\tan^{4}a + \\cot^{4}a = \\left( \\tan^{2} a + \\cot^{2} a \\right)^2 -2 = \\left( %s \\right)^2 -2 =%s$.'
                        %(latex(a),latex(b),latex(c),latex(a**2),latex(2*a*b),latex(b**2),latex(c**2),
                        latex(a**2),latex(2*a*b),latex(c**2),latex(c**2),latex(2*a*b),latex(a**2),latex(kq),
                        latex(kq),latex(kq**2-2)
                            ))
            if dang=='4':
                # Câu hỏi
                noidungcauhoi=('''Cho $%s \\tan a +%s \\cot a =%s$. Giá trị $\\tan^{6} a + \\cot^{6} a$ là  \n'''
                            %(latex(a),latex(b),latex(c)
                                ))
                # Các đáp án
                da_d = '\\True $P=%s$'%(latex(kq**2-3*kq))
                da_s1 = '$P=%s$'%(latex(kq**2-3*kq+1))
                da_s2 = '$P=%s$'%(latex(kq**2-3*kq-1))
                da_s3 = '$P=%s$'%(latex(kq**2-3*kq-2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có \\\\ \n'
                        '$\\left( %s \\tan a +%s \\cot a \\right)^2=(%s)^2 \\Leftrightarrow %s \\tan^{2}a +%s \\tan  a \\cot a +%s \\cot^{2}a =%s$\\\\ \n'
                        '$\\Leftrightarrow  %s \\left( \\tan^{2} a + \\cot^{2} a \\right) +%s \\tan  a \\cot a =%s \\Leftrightarrow \\tan^{2} a + \\cot^{2} a =\\dfrac{%s-%s}{%s} =%s$.\\\\ \n'
                        'Mặt khác \\\\ \n'
                        '\\begin{eqnarray*} \n'
                        '\\left( \\tan^{2}a +\\cot^{2}a \\right)^3&=&\\tan^{6}a +\\cot^{6}a +3 \\tan^{4}a \\cot^{2}a +3 \\tan^{2}a \\cot^{4}a \\\\ \n'
                        '&=&\\tan^{6}a +\\cot^{6}a +3 \\tan^{2}a \\cot^{2}a \\left( \\tan^{2}a +\\cot^{2}a \\right) \\\\ \n'
                        '&=&\\tan^{6}a +\\cot^{6}a +3 \\left( \\tan^{2}a +\\cot^{2}a \\right). \\\\ \n'
                        '\\end{eqnarray*} \n'
                        'Suy ra \\\\ \n'
                        '$\\tan^{6}a + \\cot^{6}a = \\left( \\tan^{2} a + \\cot^{2} a \\right)^3 -3 \\left( \\tan^{2}a +\\cot^{2}a \\right) = \\left( %s \\right)^2 -3 \\cdot %s =%s$.'
                        %(latex(a),latex(b),latex(c),latex(a**2),latex(2*a*b),latex(b**2),latex(c**2),
                        latex(a**2),latex(2*a*b),latex(c**2),latex(c**2),latex(2*a*b),latex(a**2),latex(kq),
                        latex(kq),latex(kq),latex(kq**2-3*kq)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('--','+')
            return content

