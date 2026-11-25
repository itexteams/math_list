
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


def bt_dang14_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        p,q=random.choice([(1,3),(2,3),(1,4),(3,4),(2,5),(3,5),(4,5)])
        r,s=random.choice([(1,4),(2,5),(3,5),(1,3),(2,7)])
        a_val=Rational(1,2)
        b_val=Rational(p,2*q)
        c1=random.choice([1,2,3,4])
        c2=random.choice([-3,-2,-1,1,2,3])
        m=2*c1
        n=2*q*c2
        a_sym,b_sym=symbols('a b')
        bieuthuc=m*a_sym+n*b_sym
        kq=m*a_val+n*b_val
        xD=round(5.0*p/q,3)
        xI=round((1.3+xD)/2,3)
        yI=1.75
        xM=round(1.3+3.7*r/s,3)
        yM=round(3.5*(1-r/s),3)
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (5,0);\n'
        '\\coordinate (A) at (1.3,3.5);\n'
        '\\coordinate (D) at (%s,0);\n'
        '\\coordinate (I) at (%s,%s);\n'
        '\\coordinate (M) at (%s,%s);\n'
        '\\draw (A)--(B)--(C)--cycle;\n'
        '\\draw (A)--(D) (B)--(I);\n'
        '\\foreach \\p/\\pos in {A/above,B/below left,C/below right,D/below,I/right,M/above right}{\n'
        '\\fill (\\p) circle (1.8pt) node[\\pos] {$\\p$};\n'
        '}\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )%(xD,xI,yI,xM,yM)
        noidungcauhoi=('Cho tam giác $ABC$. Gọi $D$ là điểm sao cho $\\overrightarrow{BD}=\\dfrac{%s}{%s}\\overrightarrow{BC}$ và $I$ là trung điểm của đoạn $AD$, $M$ là điểm thỏa mãn $\\overrightarrow{AM}=\\dfrac{%s}{%s}\\overrightarrow{AC}$. Biết rằng $\\overrightarrow{BI}=a\\overrightarrow{BA}+b\\overrightarrow{BC}$ với $a,b\\in\\mathbb{R}$. Giá trị của biểu thức $%s$ bằng bao nhiêu?\n'%(p,q,r,s,latex(bieuthuc))).replace('- -','+').replace('+ -','-')
        loigiai=(hinh+'Ta có: $I$ là trung điểm của đoạn $AD$ nên $\\overrightarrow{BI}=\\dfrac{1}{2}\\left(\\overrightarrow{BA}+\\overrightarrow{BD}\\right)=\\dfrac{1}{2}\\left(\\overrightarrow{BA}+\\dfrac{%s}{%s}\\overrightarrow{BC}\\right)=\\dfrac{1}{2}\\overrightarrow{BA}+%s\\overrightarrow{BC}$.\\\\\nSuy ra $a=\\dfrac{1}{2}$, $b=%s$. Khi đó $%s=%s$.'%(p,q,latex(b_val),latex(b_val),latex(bieuthuc),kq)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
