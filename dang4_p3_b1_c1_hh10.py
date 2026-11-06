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


def bt_dang4_p3_b1_c1_hh10(self):
            # Khai báo biến
            lis=['1']
            dang=random.choice(lis)
            if dang=='1':
                # Khai báo biến
                lis0=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                m=random.choice(lis0)
                n=random.choice(lis0)
                while m>=n:
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

                kq1=Rational(a+b*(1/goc**2-1),c+d*(1/goc**2-1))    

                # Tạo phân số từ số thực
                frac = Fraction(kq1).limit_denominator()

                # Lấy tử số và mẫu số
                numerator = frac.numerator
                denominator = frac.denominator

                kq=numerator+denominator

                # Câu hỏi
                noidungcauhoi=('''Cho $\\sin a = %s$. Giá trị biểu thức $P=\\dfrac{%s \\tan a +%s\\cot a}{%s \\tan a +%s \\cot a}=\\dfrac{m}{n}$ với $m,n \\in \\mathbb{Z},n>0$ và $\\dfrac{m}{n}$ là phân số tối giản. Khi đó $m+n$ bằng bao nhiêu?'''
                            %(latex(goc),latex(a),latex(b),latex(c),latex(d)
                                ))

                # Nội dung lời giải
                loigiai=('Vì $\\sin a = %s$ nên $\\cot a \\ne 0 $, nhân cả tử và mẫu với $\\cot a$ ta có \\\\ \n'
                        '$P=\\dfrac{%s \\tan a +%s\\cot a}{%s \\tan a +%s \\cot a} =\\dfrac{%s \\tan a \\cot a +%s \\cot a \\cot a}{%s \\tan a \\cot a +%s \\cot a \\cot a} =\\dfrac{%s +%s \\cot^{2}a }{%s +%s \\cot^{2}a}$. \\\\ \n'
                        '$P=\\dfrac{%s +%s \\left( \\dfrac{1}{\\sin^{2}a} -1 \\right) }{%s +%s \\left( \\dfrac{1}{\\sin^{2}a} -1 \\right)} =\\dfrac{%s +%s \\left( \\dfrac{1}{\\left( %s \\right)^2} -1 \\right) }{%s +%s \\left( \\dfrac{1}{\\left( %s \\right)^2} -1 \\right)}=%s$.\\\\ \n'
                        'Suy ra $m=%s, n=%s$, vậy $m+n=%s$.'
                        %(latex(goc), latex(a),latex(b),latex(c),latex(d), latex(a),latex(b),latex(c),latex(d),latex(a),latex(b),latex(c),latex(d),
                        latex(a),latex(b),latex(c),latex(d),
                        latex(a),latex(b),latex(goc),latex(c),latex(d),latex(goc),latex(kq1),
                        latex(numerator),latex(denominator),latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='2':
                # Khai báo biến
                lis0=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
                m=random.choice(lis0)
                n=random.choice(lis0)
                while m>=n:
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

                kq1=Rational(a*(1/goc**2-1)+b,c*(1/goc**2-1)+d)      

                # Tạo phân số từ số thực
                frac = Fraction(kq1).limit_denominator()

                # Lấy tử số và mẫu số
                numerator = frac.numerator
                denominator = frac.denominator

                kq=numerator+denominator
                # Câu hỏi
                noidungcauhoi=('''Cho $\\cos a = %s$. Giá trị biểu thức $P=\\dfrac{%s \\tan a +%s\\cot a}{%s \\tan a +%s \\cot a}=\\dfrac{m}{n}$ với $m,n \\in \\mathbb{Z},n>0$ và $\\dfrac{m}{n}$ là phân số tối giản. Khi đó $m+n$ bằng bao nhiêu?'''
                            %(latex(goc),latex(a),latex(b),latex(c),latex(d)
                                ))

                # Nội dung lời giải
                loigiai=('Vì $\\cos a = %s$ nên $\\tan a \\ne 0 $, nhân cả tử và mẫu với $\\tan a$ ta có \\\\ \n'
                        '$P=\\dfrac{%s \\tan a +%s\\cot a}{%s \\tan a +%s \\cot a} =\\dfrac{%s \\tan a \\tan a +%s \\cot a \\tan a}{%s \\tan a \\tan a +%s \\cot a \\tan a} =\\dfrac{%s \\tan^{2}a +%s  }{%s \\tan^{2}a +%s}$. \\\\ \n'
                        '$P=\\dfrac{%s \\left( \\dfrac{1}{\\cos^{2}a} -1 \\right) +%s  }{%s \\left( \\dfrac{1}{\\cos^{2}a} -1 \\right) +%s } =\\dfrac{%s \\left( \\dfrac{1}{\\left( %s \\right)^2} -1 \\right) +%s  }{%s \\left( \\dfrac{1}{\\left( %s \\right)^2} -1 \\right) +%s }=%s$.\\\\ \n'
                        'Suy ra $m=%s, n=%s$, vậy $m+n=%s$.'
                        %(latex(goc), latex(a),latex(b),latex(c),latex(d), latex(a),latex(b),latex(c),latex(d),latex(a),latex(b),latex(c),latex(d),
                        latex(a),latex(b),latex(c),latex(d),
                        latex(a),latex(goc),latex(b),latex(c),latex(goc), latex(d),latex(kq1),
                        latex(numerator),latex(denominator),latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('-+','-').replace('+-', '-').replace('--', '+').replace('++', '+')
            return content   

