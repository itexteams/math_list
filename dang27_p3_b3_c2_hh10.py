
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


def bt_dang22_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        m=random.choice([1,2,3,4,5])
        a_val=2*m+2
        b_val=2*m+1
        c1=randint(1,5)
        c2=randint(-5,5)
        while c2==0:
            c2=randint(-5,5)
        a_sym,b_sym=symbols('a b')
        bieuthuc=c1*a_sym+c2*b_sym
        kq=c1*a_val+c2*b_val
        xI=round((2*m+2.5)/(m+1),3)
        yI=round(3.6*m/(m+1),3)
        xK=round((4*m+5)/(2*m+1),3)
        yK=round(7.2*m/(2*m+1),3)
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (5,0);\n'
        '\\coordinate (A) at (2,3.6);\n'
        '\\coordinate (M) at (2.5,0);\n'
        '\\coordinate (I) at (%s,%s);\n'
        '\\coordinate (K) at (%s,%s);\n'
        '\\draw (A)--(B)--(C)--cycle;\n'
        '\\draw (A)--(M) (B)--(K);\n'
        '\\foreach \\p/\\pos in {A/above,B/below left,C/below right,M/below,I/below right,K/above right}{\n'
        '\\fill (\\p) circle (1.8pt) node[\\pos] {$\\p$};\n'
        '}\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )%(xI,yI,xK,yK)
        if m==1:
            gt_I='Gọi $I$ là trung điểm của $AM$'
            buoc1='Ta có $2\\overrightarrow{BI}=\\overrightarrow{BA}+\\overrightarrow{BM}=\\overrightarrow{BA}+\\dfrac{1}{2}\\overrightarrow{BC}\\Rightarrow 4\\overrightarrow{BI}=2\\overrightarrow{BA}+\\overrightarrow{BC}\\qquad (1)$.'
        else:
            gt_I='Lấy điểm $I$ trên đoạn $AM$ sao cho $IM=%sIA$'%(m)
            buoc1='Vì $I$ thuộc đoạn $AM$ và $IM=%sIA$ nên $%s\\overrightarrow{IA}+\\overrightarrow{IM}=\\overrightarrow{0}\\Rightarrow %s\\overrightarrow{BI}=%s\\overrightarrow{BA}+\\overrightarrow{BM}=%s\\overrightarrow{BA}+\\dfrac{1}{2}\\overrightarrow{BC}\\Rightarrow %s\\overrightarrow{BI}=%s\\overrightarrow{BA}+\\overrightarrow{BC}\\qquad (1)$.'%(m,m,m+1,m,m,a_val,2*m)
        noidungcauhoi=('Cho tam giác $ABC$ có trung tuyến $AM$. %s và lấy điểm $K$ trên cạnh $AC$ sao cho $AK=\\dfrac{1}{%s}AC$. Biết rằng $\\overrightarrow{BK}=\\dfrac{a}{b}\\overrightarrow{BI}$ với $a,b\\in\\mathbb{N}^*$ và $\\dfrac{a}{b}$ là phân số tối giản. Tính giá trị của biểu thức $%s$.\n'%(gt_I,b_val,latex(bieuthuc))).replace('- -','+').replace('+ -','-')
        loigiai=(hinh+'%s\\\\\nTa có $\\overrightarrow{BK}=\\overrightarrow{BA}+\\overrightarrow{AK}=\\overrightarrow{BA}+\\dfrac{1}{%s}\\overrightarrow{AC}=\\overrightarrow{BA}+\\dfrac{1}{%s}\\left(\\overrightarrow{BC}-\\overrightarrow{BA}\\right)=\\dfrac{%s}{%s}\\overrightarrow{BA}+\\dfrac{1}{%s}\\overrightarrow{BC}$\\\\\n$\\Rightarrow %s\\overrightarrow{BK}=%s\\overrightarrow{BA}+\\overrightarrow{BC}\\qquad (2)$.\\\\\nTừ $(1)$ và $(2)$ $\\Rightarrow %s\\overrightarrow{BK}=%s\\overrightarrow{BI}\\Rightarrow\\overrightarrow{BK}=\\dfrac{%s}{%s}\\overrightarrow{BI}$.\\\\\nSuy ra $a=%s$, $b=%s$. Vậy $%s=%s$.'%(buoc1,b_val,b_val,2*m,b_val,b_val,b_val,2*m,b_val,a_val,a_val,b_val,a_val,b_val,latex(bieuthuc),kq)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
