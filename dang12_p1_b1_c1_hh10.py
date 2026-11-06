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


def bt_dang12_p1_b1_c1_hh10(self):
            # Khai báo biến
            lis0=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
            m=random.choice(lis0)
            n=random.choice(lis0)
            while abs(m)>=abs(n):
                m=random.choice(lis0)
                n=random.choice(lis0)

            goc=Rational(m,n)

            lis=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
            a=random.choice(lis)
            b=random.choice(lis)
            c=random.choice(lis)
            d=random.choice(lis)
            while a*d-b*c==0 or c*goc+d==0 or c+d*goc==0:
                a=random.choice(lis)
                b=random.choice(lis)
                c=random.choice(lis)
                d=random.choice(lis)

            kq=Rational(a+b*(1/goc**2-1),c+d*(1/goc**2-1))    
            kq1=Rational(a*(1/goc**2-1)+b,c*(1/goc**2-1)+d)      
            lis=['1','2']
            dang=random.choice(lis)
            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\sin a = %s$. Giá trị biểu thức $P=\\dfrac{%s \\tan a +%s\\cot a}{%s \\tan a +%s \\cot a}$ là  \n'''
                            %(latex(goc),latex(a),latex(b),latex(c),latex(d)
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
                loigiai=('Vì $\\sin a = %s$ nên $\\cot a \\ne 0 $, nhân cả tử và mẫu với $\\cot a$ ta có \\\\ \n'
                        '$P=\\dfrac{%s \\tan a +%s\\cot a}{%s \\tan a +%s \\cot a} =\\dfrac{%s \\tan a \\cot a +%s \\cot a \\cot a}{%s \\tan a \\cot a +%s \\cot a \\cot a} =\\dfrac{%s +%s \\cot^{2}a }{%s +%s \\cot^{2}a}$. \\\\ \n'
                        '$P=\\dfrac{%s +%s \\left( \\dfrac{1}{\\sin^{2}a} -1 \\right) }{%s +%s \\left( \\dfrac{1}{\\sin^{2}a} -1 \\right)} =\\dfrac{%s +%s \\left( \\dfrac{1}{\\left( %s \\right)^2} -1 \\right) }{%s +%s \\left( \\dfrac{1}{\\left( %s \\right)^2} -1 \\right)}=%s$.'
                        %(latex(goc), latex(a),latex(b),latex(c),latex(d), latex(a),latex(b),latex(c),latex(d),latex(a),latex(b),latex(c),latex(d),
                        latex(a),latex(b),latex(c),latex(d),
                        latex(a),latex(b),latex(goc),latex(c),latex(d),latex(goc),latex(kq)
                            ))
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\cos a = %s$. Giá trị biểu thức $P=\\dfrac{%s \\tan a +%s\\cot a}{%s \\tan a +%s \\cot a}$ là  \n'''
                            %(latex(goc),latex(a),latex(b),latex(c),latex(d)
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
                loigiai=('Vì $\\cos a = %s$ nên $\\tan a \\ne 0 $, nhân cả tử và mẫu với $\\tan a$ ta có \\\\ \n'
                        '$P=\\dfrac{%s \\tan a +%s\\cot a}{%s \\tan a +%s \\cot a} =\\dfrac{%s \\tan a \\tan a +%s \\cot a \\tan a}{%s \\tan a \\tan a +%s \\cot a \\tan a} =\\dfrac{%s \\tan^{2}a +%s  }{%s \\tan^{2}a +%s}$. \\\\ \n'
                        '$P=\\dfrac{%s \\left( \\dfrac{1}{\\cos^{2}a} -1 \\right) +%s  }{%s \\left( \\dfrac{1}{\\cos^{2}a} -1 \\right) +%s } =\\dfrac{%s \\left( \\dfrac{1}{\\left( %s \\right)^2} -1 \\right) +%s  }{%s \\left( \\dfrac{1}{\\left( %s \\right)^2} -1 \\right) +%s }=%s$. '
                        %(latex(goc), latex(a),latex(b),latex(c),latex(d), latex(a),latex(b),latex(c),latex(d),latex(a),latex(b),latex(c),latex(d),
                        latex(a),latex(b),latex(c),latex(d),
                        latex(a),latex(goc),latex(b),latex(c),latex(goc), latex(d),latex(kq1)
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

