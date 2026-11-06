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


def bt_dang22_p4_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='4':
                #Khai báo biến
                x=symbols('x')
                a=randint(1,5)
                b=randint(1,5)
                n=randint(-5,5)
                f1=a**2*x+b**2/(x+n)
                f=(a**2*x**2+a**2*n*x+b**2)/(x+n)

                dh=(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2)/(x+n)**2

                pt=Eq(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2,0)
                x1=solve(pt)[0]
                x2=solve(pt)[1]
                x0=min(x1,x2)

                p=x0-1
                q=Rational(x0-n,2)

                fp=(a**2*p**2+a**2*n*p+b**2)/(p+n)
                fq=(a**2*q**2+a**2*n*q+b**2)/(q+n)
                f0=(a**2*x0**2+a**2*n*x0+b**2)/(x0+n)

                gtnn=min(fp,fq,f0)

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x)=%s$. Tìm giá trị nhỏ nhất của hàm số trên đoạn $\\left[%s;%s\\right]$.'''
                                 %(latex(f),latex(p),latex(q)
                                 ))

                # Nội dung lời giải
                loigiai=('''$f'(x)=%s$\\\\
                         $f'(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{&x=%s \\\\&x=%s}$. \\\\
                          Ta có $f\\left(%s\\right)=%s; f\\left(%s\\right)=%s; f\\left(%s\\right)=%s$. \\\\
                              Vậy giá trị nhỏ nhất cần tìm là $\\underset{\\left[%s;%s\\right] }{\\mathop{\\max }}\\,f(x)=%s$. '''

                         %(latex(dh),
                           latex(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2),latex(x1),latex(x2),
                           latex(p),latex(fp),latex(q),latex(fq),latex(x0),latex(f0),
                           latex(p),latex(q),latex(gtnn)
                         ))
            if dang=='3':
                #Khai báo biến
                x=symbols('x')
                a=randint(1,5)
                b=randint(1,5)
                n=randint(-5,5)
                f1=a**2*x+b**2/(x+n)
                f=(a**2*x**2+a**2*n*x+b**2)/(x+n)

                dh=(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2)/(x+n)**2

                pt=Eq(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2,0)
                x1=solve(pt)[0]
                x2=solve(pt)[1]
                x0=min(x1,x2)

                p=x0-1
                q=Rational(x0-n,2)

                fp=(a**2*p**2+a**2*n*p+b**2)/(p+n)
                fq=(a**2*q**2+a**2*n*q+b**2)/(q+n)
                f0=(a**2*x0**2+a**2*n*x0+b**2)/(x0+n)

                gtln=max(fp,fq,f0)

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x)=%s$. Tìm giá trị lớn nhất của hàm số trên đoạn $\\left[%s;%s\\right]$.'''
                                 %(latex(f),latex(p),latex(q)
                                 ))

                # Nội dung lời giải
                loigiai=('''$f'(x)=%s$\\\\
                         $f'(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{&x=%s \\\\&x=%s}$. \\\\
                          Ta có $f\\left(%s\\right)=%s; f\\left(%s\\right)=%s; f\\left(%s\\right)=%s$. \\\\
                              Vậy giá trị lớn nhất cần tìm là $\\underset{\\left[%s;%s\\right] }{\\mathop{\\max }}\\,f(x)=%s$. '''

                         %(latex(dh),
                           latex(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2),latex(x1),latex(x2),
                           latex(p),latex(fp),latex(q),latex(fq),latex(x0),latex(f0),
                           latex(p),latex(q),latex(gtln)
                         ))
            if dang=='2':
                #Khai báo biến
                x=symbols('x')
                a=randint(1,5)
                b=randint(1,5)
                n=randint(-5,5)
                f1=a**2*x+b**2/(x+n)
                f=(a**2*x**2+a**2*n*x+b**2)/(x+n)

                dh=(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2)/(x+n)**2

                pt=Eq(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2,0)
                x1=solve(pt)[0]
                x2=solve(pt)[1]
                x0=max(x1,x2)

                p=Rational(x0-n,2)
                q=x0+1

                fp=(a**2*p**2+a**2*n*p+b**2)/(p+n)
                fq=(a**2*q**2+a**2*n*q+b**2)/(q+n)
                f0=(a**2*x0**2+a**2*n*x0+b**2)/(x0+n)

                gtnn=min(fp,fq,f0)

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x)=%s$. Tìm giá trị nhỏ nhất của hàm số trên đoạn $\\left[%s;%s\\right]$.'''
                                 %(latex(f),latex(p),latex(q)
                                 ))

                # Nội dung lời giải
                loigiai=('''$f'(x)=%s$\\\\
                         $f'(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{&x=%s \\\\&x=%s}$. \\\\
                          Ta có $f\\left(%s\\right)=%s; f\\left(%s\\right)=%s; f\\left(%s\\right)=%s$. \\\\
                              Vậy giá trị nhỏ nhất cần tìm là $\\underset{\\left[%s;%s\\right] }{\\mathop{\\max }}\\,f(x)=%s$. '''

                         %(latex(dh),
                           latex(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2),latex(x1),latex(x2),
                           latex(p),latex(fp),latex(q),latex(fq),latex(x0),latex(f0),
                           latex(p),latex(q),latex(gtnn)
                         ))

            if dang=='1':
                #Khai báo biến
                x=symbols('x')
                a=randint(1,5)
                b=randint(1,5)
                n=randint(-5,5)
                f1=a**2*x+b**2/(x+n)
                f=(a**2*x**2+a**2*n*x+b**2)/(x+n)

                dh=(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2)/(x+n)**2

                pt=Eq(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2,0)
                x1=solve(pt)[0]
                x2=solve(pt)[1]
                x0=max(x1,x2)

                p=Rational(x0-n,2)
                q=x0+1

                fp=(a**2*p**2+a**2*n*p+b**2)/(p+n)
                fq=(a**2*q**2+a**2*n*q+b**2)/(q+n)
                f0=(a**2*x0**2+a**2*n*x0+b**2)/(x0+n)

                gtln=max(fp,fq,f0)

                # Câu hỏi
                noidungcauhoi = ('''Cho hàm số $f(x)=%s$. Tìm giá trị lớn nhất của hàm số trên đoạn $\\left[%s;%s\\right]$.'''
                                 %(latex(f),latex(p),latex(q)
                                 ))

                # Nội dung lời giải
                loigiai=('''$f'(x)=%s$\\\\
                         $f'(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{&x=%s \\\\&x=%s}$. \\\\
                          Ta có $f\\left(%s\\right)=%s; f\\left(%s\\right)=%s; f\\left(%s\\right)=%s$. \\\\
                              Vậy giá trị lớn nhất cần tìm là $\\underset{\\left[%s;%s\\right] }{\\mathop{\\max }}\\,f(x)=%s$. '''

                         %(latex(dh),
                           latex(a**2*x**2+a**2*2*n*x+a**2*n**2-b**2),latex(x1),latex(x2),
                           latex(p),latex(fp),latex(q),latex(fq),latex(x0),latex(f0),
                           latex(p),latex(q),latex(gtln)
                         ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-')
            return content

