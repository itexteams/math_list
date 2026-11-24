
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


def bt_dang10_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        m0=random.choice([1,2,3])
        n0=random.choice([2,3,4,5])
        a_val=Rational(1,2*(m0+1))
        b_val=Rational(1,2*(n0+1))
        k1=random.choice([1,2,3])
        k2=random.choice([-3,-2,-1,1,2,3])
        c1=2*(m0+1)*k1
        c2=2*(n0+1)*k2
        a_sym,b_sym=symbols('a b')
        bieuthuc=c1*a_sym+c2*b_sym
        kq=c1*a_val+c2*b_val
        xM=round(1.9*(1-1/(m0+1)),3)
        yM=round(3.2*(1-1/(m0+1)),3)
        xN=round(1.9+3.1/(n0+1),3)
        yN=round(3.2*(1-1/(n0+1)),3)
        xK=round((xM+xN)/2,3)
        yK=round((yM+yN)/2,3)
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (5,0);\n'
        '\\coordinate (A) at (1.9,3.2);\n'
        '\\coordinate (M) at (%s,%s);\n'
        '\\coordinate (N) at (%s,%s);\n'
        '\\coordinate (K) at (%s,%s);\n'
        '\\draw (A)--(B)--(C)--cycle;\n'
        '\\draw (M)--(N);\n'
        '\\draw[->] (A)--(K);\n'
        '\\foreach \\p/\\pos in {A/above,B/below left,C/below right,M/left,N/above right,K/below}{\n'
        '\\fill (\\p) circle (1.8pt) node[\\pos] {$\\p$};\n'
        '}\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )%(xM,yM,xN,yN,xK,yK)
        gt_M='Gọi $M$ là trung điểm của $AB$' if m0==1 else 'Gọi $M$ là điểm thuộc $AB$ sao cho $\\overrightarrow{BM}=%s\\overrightarrow{MA}$'%(m0)
        buoc_M='Ta có $M$ là trung điểm $AB$ nên $\\overrightarrow{AM}=\\dfrac{1}{2}\\overrightarrow{AB}$' if m0==1 else 'Ta có $\\overrightarrow{BM}=%s\\overrightarrow{MA}\\Rightarrow\\overrightarrow{AM}=\\dfrac{1}{%s}\\overrightarrow{AB}$'%(m0,m0+1)
        noidungcauhoi=('Cho tam giác $ABC$. %s, $N$ là điểm thuộc $AC$ sao cho $\\overrightarrow{CN}=%s\\overrightarrow{NA}$ và $K$ là trung điểm của $MN$. Biết rằng $\\overrightarrow{AK}=a\\overrightarrow{AB}+b\\overrightarrow{AC}$ với $a,b\\in\\mathbb{R}$. Tính giá trị của biểu thức $%s$.\n'%(gt_M,n0,latex(bieuthuc))).replace('- -','+').replace('+ -','-')
        loigiai=(hinh+'%s; $\\overrightarrow{CN}=%s\\overrightarrow{NA}\\Rightarrow\\overrightarrow{AN}=\\dfrac{1}{%s}\\overrightarrow{AC}$.\\\\\nDo đó $\\overrightarrow{AK}=\\dfrac{1}{2}\\left(\\overrightarrow{AM}+\\overrightarrow{AN}\\right)=%s\\overrightarrow{AB}+%s\\overrightarrow{AC}$.\\\\\nSuy ra $a=%s$, $b=%s$. Khi đó $%s=%s$.'%(buoc_M,n0,n0+1,latex(a_val),latex(b_val),latex(a_val),latex(b_val),latex(bieuthuc),kq)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
