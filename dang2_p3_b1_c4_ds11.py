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


def bt_dang2_p3_b1_c4_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                u1=randint(1,9)
                a=randint(2,9)
                q=Rational(1,a)
                b=randint(-9,9)
                c=randint(-9,9)
                while  a==0 or a==1 or b==0 or c==0 or u1%(1-q)==0:
                    u1=randint(1,9)
                    a=randint(2,9)
                    q=Rational(1,a)
                    b=randint(-9,9)
                    c=randint(-9,9)
                e=gcd(u1,(1-q))
                t=nsimplify(u1/e)
                m=nsimplify((1-q)/e)
                x0=Rational(u1,(1-q))

                # Câu hỏi
                noidungcauhoi = ('Giá trị $T=%s+%s+%s+\\cdots + \\dfrac{%s}{%s^n}+\\cdots=\\dfrac{a}{b}$ khi đó $%sa+%sb$ bằng bao nhiêu?\n'
                                %(latex(u1),latex(u1*q),latex(u1*q*q),latex(u1),latex(a),latex(b),latex(c),
                                ))

                # Nội dung lời giải
                loigiai = ('Các số hạng của $T$ lập thành một cấp số nhân lùi vô hạn với số hạng đầu ${u}_{1}=%s$ và công bội $q=%s$$zz$ \\\\ \n'
                        'Khi đó $T=%s+%s+%s+\\cdots+ \\dfrac{%s}{%s^n}+\\cdots=\\dfrac{%s}{1-%s}=%s$ suy ra $a=%s; b=%s$$zz$\\\\ \n'
                        'Vậy $%s\\cdot%s+%s \\cdot %s=%s$$zz$'
                        %(latex(u1),latex(q),latex(u1),latex(u1*q),latex(u1*q*q),latex(u1),latex(a),latex(u1),latex(q),latex(x0),latex(t),latex(m),
                        latex(b),latex(t),latex(c),latex(m),latex(b*t+c*m),
                        )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(b*t+c*m))

            if dang=='2':
                # Khai báo biến
                u1=randint(1,9)
                a=randint(-9,-2)
                q=Rational(1,a)
                b=randint(-9,9)
                c=randint(-9,9)
                while  a==0 or a==1 or b==0 or c==0 or u1%(1-q)==0:
                    u1=randint(1,9)
                    a=randint(-9,-2)
                    q=Rational(1,a)
                    b=randint(-9,9)
                    c=randint(-9,9)
                e=gcd(u1,(1-q))
                t=nsimplify(u1/e)
                m=nsimplify((1-q)/e)
                x0=Rational(u1,(1-q))

                # Câu hỏi
                noidungcauhoi = ('Giá trị $T=%s+%s+%s+\\cdots + (-1)^n\\dfrac{%s}{%s^n}+\\cdots=\\dfrac{a}{b}$ khi đó $%sa+%sb$ bằng bao nhiêu?\n'
                                %(latex(u1),latex(u1*q),latex(u1*q*q),latex(u1),latex(-a),latex(b),latex(c),
                                ))

                # Nội dung lời giải
                loigiai = ('Các số hạng của $T$ lập thành một cấp số nhân lùi vô hạn với số hạng đầu ${u}_{1}=%s$ và công bội $q=%s$$zz$\\\\ \n'
                        'Khi đó $T=%s+%s+%s+\\cdots + (-1)^n\\dfrac{%s}{%s^n}+\\cdots=\\dfrac{%s}{1-\\left(%s\\right)}=%s$ suy ra $a=%s; b=%s$$zz$\\\\ \n'
                        'Vậy $%s\\cdot%s+%s \\cdot %s=%s$$zz$'
                        %(latex(u1),latex(q),latex(u1),latex(u1*q),latex(u1*q*q),latex(u1),latex(-a),latex(u1),latex(q),latex(x0),latex(t),latex(m),
                        latex(b),latex(t),latex(c),latex(m),latex(b*t+c*m),
                        )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(b*t+c*m))

            if dang=='3':
                # Khai báo biến
                u1=randint(1,9)
                a=randint(2,9)
                q=Rational(1,a)
                b=randint(-9,9)
                c=randint(-9,9)
                while  a==0 or a==1 or b==0 or c==0 or u1%(1-q)==0:
                    u1=randint(1,9)
                    a=randint(2,9)
                    q=Rational(1,a)
                    b=randint(-9,9)
                    c=randint(-9,9)
                e=gcd(u1,(1-q))
                t=nsimplify(u1/e)
                m=nsimplify((1-q)/e)
                x0=u1/(1-q)
                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Câu hỏi
                noidungcauhoi = ('Giá trị $T=%s+%s+%s+\\cdots + \\dfrac{%s}{%s^n}+\\cdots$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục)\n'
                                %(latex(u1),latex(u1*q),latex(u1*q*q),latex(u1),latex(a),
                                ))

                # Nội dung lời giải
                loigiai = ('Các số hạng của $T$ lập thành một cấp số nhân lùi vô hạn với số hạng đầu ${u}_{1}=%s$ và công bội $q=%s$$zz$ \\\\ \n'
                        'Khi đó $T=%s+%s+%s+\\cdots+ \\dfrac{%s}{%s^n}+\\cdots=\\dfrac{%s}{1-%s}=%s\\approx %s$$zz$'
                        %(latex(u1),latex(q),latex(u1),latex(u1*q),latex(u1*q*q),latex(u1),latex(a),latex(u1),latex(q),latex(x0),latex(kq1),
                        )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq1))

            if dang=='4':
                # Khai báo biến
                u1=randint(1,9)
                a=randint(-9,-2)
                q=Rational(1,a)
                b=randint(-9,9)
                c=randint(-9,9)
                while  a==0 or a==1 or b==0 or c==0 or u1%(1-q)==0:
                    u1=randint(1,9)
                    a=randint(-9,-2)
                    q=Rational(1,a)
                    b=randint(-9,9)
                    c=randint(-9,9)
                e=gcd(u1,(1-q))
                t=nsimplify(u1/e)
                m=nsimplify((1-q)/e)
                x0=Rational(u1,(1-q))
                number = Decimal(float(x0))  # Số cần làm tròn
                kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                # Câu hỏi
                noidungcauhoi = ('Giá trị $T=%s+%s+%s+\\cdots + (-1)^n\\dfrac{%s}{%s^n}+\\cdots$ bằng bao nhiêu? (kết quả làm tròn đến hàng phần chục)\n'
                                %(latex(u1),latex(u1*q),latex(u1*q*q),latex(u1),latex(-a),
                                ))

                # Nội dung lời giải
                loigiai = ('Các số hạng của $T$ lập thành một cấp số nhân lùi vô hạn với số hạng đầu ${u}_{1}=%s$ và công bội $q=%s$$zz$ \\\\ \n'
                        'Khi đó $T=%s+%s+%s+\\cdots + (-1)^n\\dfrac{%s}{%s^n}+\\cdots=\\dfrac{%s}{1-\\left(%s\\right)}=%s\\approx %s$$zz$'
                        %(latex(u1),latex(q),latex(u1),latex(u1*q),latex(u1*q*q),latex(u1),latex(-a),latex(u1),latex(q),latex(x0),latex(kq1),
                        )
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('+-', '-').replace('--', '+').replace('1a', 'a').replace('1b', 'b')
            return content                

