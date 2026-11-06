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


def bt_dang15_p4_b3_c1_ds11(self):
            # Khai báo biến
            x=symbols('x')
            y=symbols('y')

            a=randint(-9,9)
            b=randint(-9,9)
            c=randint(-9,9)
            m=2
            n=randint(-2,2)
            p=3

            hsa=(m**2+n**2-p**2)
            hsb=-2*(m*a+n*b-c*p)
            hsc=(a**2+b**2-c**2)

            delta=hsb**2-4*hsa*hsc

            while hsb**2-4*hsa*hsc<=0:
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                m=2
                n=randint(-2,2)
                p=3

            gtln=(-hsb-sqrt(delta))/(2*hsa)
            gtnn=(-hsb+sqrt(delta))/(2*hsa)

            tong=-Rational(hsb,hsa)
            tich=Rational(hsc,hsa)
            hieu=gtln-gtnn


            f=(a*sin(x)+b*cos(x)+c)/(m*sin(x)+n*cos(x)+p)
            vt1=m*y*sin(x)+n*y*cos(x)+p*y
            vp1=a*sin(x)+b*cos(x)+c

            vt2=(m*y-a)*sin(x)+(n*y-b)*cos(x)
            vp2=c-p*y

            vt3=(m**2+n**2-p**2)*y**2-2*(a*m+b*n-c*p)*y+a**2+b**2-c**2 

            lisdang=['1','2','3','4','5']
            dang=random.choice(lisdang)

            if dang=='5':
                d = [
                    '$%s$'%(latex(hieu)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(hieu+1)),
                    '$%s$'%(latex(hieu+2)),
                    '$%s$'%(latex(hieu+3)),
                    '$%s$'%(latex(hieu-1)),
                    '$%s$'%(latex(hieu-2)),
                    '$%s$'%(latex(hieu-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Tìm hiệu giá trị lớn nhất và nhỏ nhất của hàm số.'
                                %(latex(f)
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
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1.5cm} $y=%s \\Leftrightarrow %s=%s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s=%s$. \\\\ \n'
                        'Coi $x$ là biến số, $y$ là hằng số, phương trình có nghiệm khi và chỉ khi \\\\ \n'
                        '\\hspace*{1.5cm} $%s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\ge 0$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\le y \\le %s$. \\\\ \n'
                        'Vậy hiệu giá trị lớn nhất và nhỏ nhất của hàm số là $%s$.'
                        %(latex(f),latex(vt1),latex(vp1),
                        latex(vt2),latex(vp2),
                        latex((m*y-a)**2),latex((n*y-b)**2),latex((c-p*y)**2),
                        latex(m**2*y**2-2*m*a*y+a**2),latex(n**2*y**2-2*n*b*y+b**2),latex(c**2-2*c*p*y+p**2*y**2),
                        latex(vt3),
                        latex(gtnn),latex(gtln),
                        latex(hieu)               
                        ))

            if dang=='4':
                d = [
                    '$%s$'%(latex(tich)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(tich+1)),
                    '$%s$'%(latex(tich+2)),
                    '$%s$'%(latex(tich+3)),
                    '$%s$'%(latex(tich-1)),
                    '$%s$'%(latex(tich-2)),
                    '$%s$'%(latex(tich-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hàm số $y=%s$. Tính tích giá trị lớn nhất và nhỏ nhất của hàm số.'
                                %(latex(f)
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
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1.5cm} $y=%s \\Leftrightarrow %s=%s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s=%s$. \\\\ \n'
                        'Coi $x$ là biến số, $y$ là hằng số, phương trình có nghiệm khi và chỉ khi \\\\ \n'
                        '\\hspace*{1.5cm} $%s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\ge 0$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\le y \\le %s$. \\\\ \n'
                        'Vậy tích giá trị lớn nhất và nhỏ nhất của hàm số là $%s$.'
                        %(latex(f),latex(vt1),latex(vp1),
                        latex(vt2),latex(vp2),
                        latex((m*y-a)**2),latex((n*y-b)**2),latex((c-p*y)**2),
                        latex(m**2*y**2-2*m*a*y+a**2),latex(n**2*y**2-2*n*b*y+b**2),latex(c**2-2*c*p*y+p**2*y**2),
                        latex(vt3),
                        latex(gtnn),latex(gtln),
                        latex(tich)               
                        ))

            if dang=='3':
                d = [
                    '$%s$'%(latex(tong)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(tong+1)),
                    '$%s$'%(latex(tong+2)),
                    '$%s$'%(latex(tong+3)),
                    '$%s$'%(latex(tong-1)),
                    '$%s$'%(latex(tong-2)),
                    '$%s$'%(latex(tong-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=%s$. Tính tổng giá trị lớn nhất và nhỏ nhất của hàm số.'
                                %(latex(f)
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
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1.5cm} $y=%s \\Leftrightarrow %s=%s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s=%s$. \\\\ \n'
                        'Coi $x$ là biến số, $y$ là hằng số, phương trình có nghiệm khi và chỉ khi \\\\ \n'
                        '\\hspace*{1.5cm} $%s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\ge 0$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\le y \\le %s$. \\\\ \n'
                        'Vậy tổng giá trị lớn nhất và nhỏ nhất của hàm số là $%s$.'
                        %(latex(f),latex(vt1),latex(vp1),
                        latex(vt2),latex(vp2),
                        latex((m*y-a)**2),latex((n*y-b)**2),latex((c-p*y)**2),
                        latex(m**2*y**2-2*m*a*y+a**2),latex(n**2*y**2-2*n*b*y+b**2),latex(c**2-2*c*p*y+p**2*y**2),
                        latex(vt3),
                        latex(gtnn),latex(gtln),
                        latex(tong)

                        ))

            if dang=='2':
                d = [
                    '$%s$'%(latex(gtnn)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(gtnn+1)),
                    '$%s$'%(latex(gtnn+2)),
                    '$%s$'%(latex(gtnn+3)),
                    '$%s$'%(latex(gtnn-1)),
                    '$%s$'%(latex(gtnn-2)),
                    '$%s$'%(latex(gtnn-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tìm giá trị nhỏ nhất của hàm số $y=%s$.'
                                %(latex(f)
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
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1.5cm} $y=%s \\Leftrightarrow %s=%s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s=%s$. \\\\ \n'
                        'Coi $x$ là biến số, $y$ là hằng số, phương trình có nghiệm khi và chỉ khi \\\\ \n'
                        '\\hspace*{1.5cm} $%s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\ge 0$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\le y \\le %s$. \\\\ \n'
                        'Vậy giá trị nhỏ nhất của hàm số là $%s$.'
                        %(latex(f),latex(vt1),latex(vp1),
                        latex(vt2),latex(vp2),
                        latex((m*y-a)**2),latex((n*y-b)**2),latex((c-p*y)**2),
                        latex(m**2*y**2-2*m*a*y+a**2),latex(n**2*y**2-2*n*b*y+b**2),latex(c**2-2*c*p*y+p**2*y**2),
                        latex(vt3),
                        latex(gtnn),latex(gtln),
                        latex(gtnn)               
                        ))

            if dang=='1':
                d = [
                    '$%s$'%(latex(gtln)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(gtln+1)),
                    '$%s$'%(latex(gtln+2)),
                    '$%s$'%(latex(gtln+3)),
                    '$%s$'%(latex(gtln-1)),
                    '$%s$'%(latex(gtln-2)),
                    '$%s$'%(latex(gtln-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Tìm giá trị lớn nhất của hàm số $y=%s$.'
                                %(latex(f)
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
                loigiai=(
                        'Ta có \\\\ \n'
                        '\\hspace*{1.5cm} $y=%s \\Leftrightarrow %s=%s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s=%s$. \\\\ \n'
                        'Coi $x$ là biến số, $y$ là hằng số, phương trình có nghiệm khi và chỉ khi \\\\ \n'
                        '\\hspace*{1.5cm} $%s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s+%s \\ge %s$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\ge 0$ \\\\ \n'
                        '\\hspace*{1cm} $\\Leftrightarrow %s \\le y \\le %s$. \\\\ \n'
                        'Vậy giá trị lớn nhất của hàm số là $%s$.'
                        %(latex(f),latex(vt1),latex(vp1),
                        latex(vt2),latex(vp2),
                        latex((m*y-a)**2),latex((n*y-b)**2),latex((c-p*y)**2),
                        latex(m**2*y**2-2*m*a*y+a**2),latex(n**2*y**2-2*n*b*y+b**2),latex(c**2-2*c*p*y+p**2*y**2),
                        latex(vt3),
                        latex(gtnn),latex(gtln),
                        latex(gtln)               
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('{\\left(x \\right)}', ' x')
            return content

