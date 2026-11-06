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


def bt_dang10_p4_b2_c1_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='6':
                m=randint(1,9)
                n=randint(1,9)
                while abs(n)<=abs(m):
                    m=randint(1,9)
                    n=randint(1,9)
                a=Rational(m,n)

                kq=(2*sqrt(1/(a**2)-1))/(1-(1/(a**2)-1))


                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+2*(a/i)*sqrt(1-a**2))),
                    '$%s$'%(latex(kq+2*(a/j)*sqrt(1-a**2))),
                    '$%s$'%(latex(kq+2*(a/k)*sqrt(1-a**2))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\cos a = %s$ với $a \\in \\left(0; \\dfrac{\\pi}{2} \\right)$. Tính giá trị $\\tan 2a$.'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $1+\\tan^2 a = \\dfrac{1}{\\cos^2 a} \\Leftrightarrow \\tan^2 a= \\dfrac{1}{\\cos^2 a}-1=\\dfrac{1}{%s}-1=%s \\Leftrightarrow \\tan a = \\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(0; \\dfrac{\\pi}{2} \\right)$ nên $\\tan a >0$ suy ra $\\tan a = %s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\tan 2a = \\dfrac{2 \\tan a}{1-\\tan^2 a} =\\dfrac{2 \\cdot %s}{1-%s}=%s$. \\\\ \n'

                        %(
                        latex(a**2),latex(1/(a**2)-1),latex(sqrt(1/(a**2)-1)),
                        latex(sqrt(1/(a**2)-1)),
                        latex(sqrt(1/(a**2)-1)),latex(1/(a**2)-1),latex(kq),
                        ))
            if dang=='5':
                m=randint(-9,9)
                n=randint(-9,9)
                while abs(n)<=abs(m):
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)

                kq=2*a**2-1
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(2*(a+i)**2-1)),
                    '$%s$'%(latex(2*(a+j)**2-1)),
                    '$%s$'%(latex(2*(a+k)**2-1)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\cos a = %s$. Tính giá trị $\\cos 2a$.'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\cos 2a = 2 \\cos^2 a-1=2 \\left( %s \\right)^2-1=%s$. \\\\ \n'

                        %(latex(a),latex(2*a**2-1)
                        ))

            if dang=='4':
                m=randint(1,9)
                n=randint(1,9)
                while abs(n)<=abs(m):
                    m=randint(1,9)
                    n=randint(1,9)
                a=Rational(m,n)

                kq=2*a*sqrt(1-a**2)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(2*(a+i)*sqrt(1-a**2))),
                    '$%s$'%(latex(2*(a+j)*sqrt(1-a**2))),
                    '$%s$'%(latex(2*(a+k)*sqrt(1-a**2))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\cos a = %s$ với $a \\in \\left(0; \\dfrac{\\pi}{2} \\right)$. Tính giá trị $\\sin 2a$.'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\sin^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\sin a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(0; \\dfrac{\\pi}{2} \\right)$ nên $\\sin a >0$ suy ra $\\sin a = %s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\sin 2a = 2 \\sin a \\cos a = 2 \\cdot \\left(%s\\right) \\cdot %s = %s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(sqrt(1-a**2)),
                        latex(sqrt(1-a**2)),
                        latex(sqrt(1-a**2)),latex(a),latex(kq)
                        ))

            if dang=='3':
                m=randint(1,9)
                n=randint(1,9)
                while abs(n)<=abs(m):
                    m=randint(1,9)
                    n=randint(1,9)
                a=Rational(m,n)

                kq=(2*sqrt(1/(1-a**2)-1))/(1-(1/(1-a**2)-1))


                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(kq+2*(a/i)*sqrt(1-a**2))),
                    '$%s$'%(latex(kq+2*(a/j)*sqrt(1-a**2))),
                    '$%s$'%(latex(kq+2*(a/k)*sqrt(1-a**2))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\sin a = %s$ với $a \\in \\left(0; \\dfrac{\\pi}{2} \\right)$. Tính giá trị $\\tan 2a$.'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\cos^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s$. \\\\ \n'
                        '\\hspace*{1cm} $1+\\tan^2 a = \\dfrac{1}{\\cos^2 a} \\Leftrightarrow \\tan^2 a= \\dfrac{1}{\\cos^2 a}-1=\\dfrac{1}{%s}-1=%s \\Leftrightarrow \\tan a = \\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(0; \\dfrac{\\pi}{2} \\right)$ nên $\\tan a >0$ suy ra $\\tan a = %s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\tan 2a = \\dfrac{2 \\tan a}{1-\\tan^2 a} =\\dfrac{2 \\cdot %s}{1-%s}=%s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),
                        latex(1-a**2),latex(1/(1-a**2)-1),latex(sqrt(1/(1-a**2)-1)),
                        latex(sqrt(1/(1-a**2)-1)),
                        latex(sqrt(1/(1-a**2)-1)),latex(1/(1-a**2)-1),latex(kq),
                        ))

            if dang=='2':
                m=randint(-9,9)
                n=randint(-9,9)
                while abs(n)<=abs(m):
                    m=randint(-9,9)
                    n=randint(-9,9)
                a=Rational(m,n)

                kq=1-2*a**2
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(1-2*(a+i)**2)),
                    '$%s$'%(latex(1-2*(a+j)**2)),
                    '$%s$'%(latex(1-2*(a+k)**2)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\sin a = %s$. Tính giá trị $\\cos 2a$.'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\cos 2a = 1-2 \\sin^2 a=1-2 \\left( %s \\right)^2=%s$. \\\\ \n'

                        %(latex(a),latex(1-2*a**2)
                        ))

            if dang=='1':
                m=randint(1,9)
                n=randint(1,9)
                while abs(n)<=abs(m):
                    m=randint(1,9)
                    n=randint(1,9)
                a=Rational(m,n)

                kq=2*a*sqrt(1-a**2)
                i=randint(-5,5)
                j=randint(-5,5)
                k=randint(-5,5)
                while i==j or j==k or i==k or i==0 or j==0 or k==0:
                    i=randint(-5,5)
                    j=randint(-5,5)
                    k=randint(-5,5)

                d = [
                    '$%s$'%(latex(kq)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(2*(a+i)*sqrt(1-a**2))),
                    '$%s$'%(latex(2*(a+j)*sqrt(1-a**2))),
                    '$%s$'%(latex(2*(a+k)*sqrt(1-a**2))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho $\\sin a = %s$ với $a \\in \\left(0; \\dfrac{\\pi}{2} \\right)$. Tính giá trị $\\sin 2a$.'
                                %(latex(a))
                            ) 

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $\\sin^2 a +\\cos^2 a =1 \\Leftrightarrow \\cos^2 a=1-\\sin^2 a =1-\\left(%s \\right)^2 =%s \\Leftrightarrow \\cos a =\\pm %s$. \\\\ \n'
                        '\\hspace*{1cm} Vì $a \\in \\left(0; \\dfrac{\\pi}{2} \\right)$ nên $\\cos a >0$ suy ra $\\cos a = %s$. \\\\ \n'
                        'Suy ra \\\\ \n'
                        '\\hspace*{1cm} $\\sin 2a = 2 \\sin a \\cos a = 2 \\cdot \\left(%s\\right) \\cdot %s = %s$. \\\\ \n'

                        %(latex(a),latex(1-a**2),latex(sqrt(1-a**2)),
                        latex(sqrt(1-a**2)),
                        latex(a),latex(sqrt(1-a**2)),latex(kq)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content


