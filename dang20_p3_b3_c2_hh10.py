
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


def bt_dang15_p3_b3_c2_hh10(self):
    lisdang=['1','2']
    dang=random.choice(lisdang)
    c1=randint(1,5)
    c2=randint(-5,5)
    while c2==0:
        c2=randint(-5,5)
    a_sym,b_sym=symbols('a b')
    bieuthuc=c1*a_sym+c2*b_sym
    hinh=(
    '\\begin{center}\n'
    '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
    '\\coordinate (B) at (0,0);\n'
    '\\coordinate (C) at (5,0);\n'
    '\\coordinate (A) at (2.5,4.33);\n'
    '\\coordinate (O) at (2.5,1.443);\n'
    '\\coordinate (I) at (2.2,2.2);\n'
    '\\coordinate (M) at (0.93,0);\n'
    '\\coordinate (N) at (3.47,0);\n'
    '\\coordinate (P) at (3.73,2.2);\n'
    '\\coordinate (Q) at (2.965,3.525);\n'
    '\\coordinate (R) at (1.735,3.005);\n'
    '\\coordinate (S) at (1.27,2.2);\n'
    '\\coordinate (D) at (2.2,0);\n'
    '\\coordinate (E) at (3.348,2.862);\n'
    '\\coordinate (F) at (1.502,2.602);\n'
    '\\draw (A)--(B)--(C)--cycle;\n'
    '\\draw[dashed] (A)--(2.5,0) (B)--(3.75,2.165);\n'
    '\\draw (M)--(Q) (P)--(S) (N)--(R);\n'
    '\\draw (I)--(D) (I)--(E) (I)--(F);\n'
    '\\draw (2.2,0.22)--(2.42,0.22)--(2.42,0);\n'
    '\\draw (3.448,2.689)--(3.275,2.589)--(3.175,2.762);\n'
    '\\draw (1.402,2.429)--(1.575,2.329)--(1.675,2.502);\n'
    '\\foreach \\p/\\pos in {A/above,B/below left,C/below right,O/below,I/below right,M/below,N/below,P/right,Q/above right,R/above left,S/left,D/below,E/above right,F/above left}{\n'
    '\\fill (\\p) circle (1.5pt) node[\\pos] {$\\p$};\n'
    '}\n'
    '\\end{tikzpicture}\n'
    '\\end{center}\n'
    )
    if dang=='1':
        m=random.choice([1,3,5,7])
        tyso=Rational(3*m,2)
        a_val=tyso.p
        b_val=tyso.q
        kq=c1*a_val+c2*b_val
        vt='\\overrightarrow{ID}+\\overrightarrow{IE}+\\overrightarrow{IF}' if m==1 else '%s\\left(\\overrightarrow{ID}+\\overrightarrow{IE}+\\overrightarrow{IF}\\right)'%(m)
        noidungcauhoi=('Cho tam giác đều $ABC$ có tâm $O$. Gọi $I$ là một điểm tùy ý bên trong tam giác $ABC$. Hạ $ID,IE,IF$ tương ứng vuông góc với $BC,CA,AB$. Giả sử $%s=\\dfrac{a}{b}\\overrightarrow{IO}$ với $a,b\\in\\mathbb{N}^*$ và $\\dfrac{a}{b}$ là phân số tối giản. Tính giá trị của biểu thức $%s$.\n'%(vt,latex(bieuthuc))).replace('- -','+').replace('+ -','-')
        buoc_cuoi='Suy ra $%s=%s\\overrightarrow{IO}\\Rightarrow a=%s, b=%s$. Do đó $%s=%s$.'%(vt,latex(tyso),a_val,b_val,latex(bieuthuc),kq)
    if dang=='2':
        n=random.choice([1,2,4,5])
        tyso=Rational(2*n,3)
        a_val=tyso.p
        b_val=tyso.q
        kq=c1*a_val+c2*b_val
        vt='\\overrightarrow{IO}' if n==1 else '%s\\overrightarrow{IO}'%(n)
        noidungcauhoi=('Cho tam giác đều $ABC$ có tâm $O$. Gọi $I$ là một điểm tùy ý bên trong tam giác $ABC$. Hạ $ID,IE,IF$ tương ứng vuông góc với $BC,CA,AB$. Giả sử $%s=\\dfrac{a}{b}\\left(\\overrightarrow{ID}+\\overrightarrow{IE}+\\overrightarrow{IF}\\right)$ với $a,b\\in\\mathbb{N}^*$ và $\\dfrac{a}{b}$ là phân số tối giản. Tính giá trị của biểu thức $%s$.\n'%(vt,latex(bieuthuc))).replace('- -','+').replace('+ -','-')
        buoc_cuoi='Suy ra $\\overrightarrow{IO}=\\dfrac{2}{3}\\left(\\overrightarrow{ID}+\\overrightarrow{IE}+\\overrightarrow{IF}\\right)\\Rightarrow %s=%s\\left(\\overrightarrow{ID}+\\overrightarrow{IE}+\\overrightarrow{IF}\\right)\\Rightarrow a=%s, b=%s$. Do đó $%s=%s$.'%(vt,latex(tyso),a_val,b_val,latex(bieuthuc),kq)
    loigiai=(hinh+'Qua điểm $I$ dựng các đoạn $MQ\\parallel AB, PS\\parallel BC, NR\\parallel CA$.\\\\\nVì $ABC$ là tam giác đều nên các tam giác $IMN, IPQ, IRS$ cũng là tam giác đều.\\\\\nSuy ra $D, E, F$ lần lượt là trung điểm của $MN, PQ, RS$.\\\\\nKhi đó: $\\overrightarrow{ID}+\\overrightarrow{IE}+\\overrightarrow{IF}=\\dfrac{1}{2}\\left(\\overrightarrow{IM}+\\overrightarrow{IN}\\right)+\\dfrac{1}{2}\\left(\\overrightarrow{IP}+\\overrightarrow{IQ}\\right)+\\dfrac{1}{2}\\left(\\overrightarrow{IR}+\\overrightarrow{IS}\\right)$\\\\\n$=\\dfrac{1}{2}\\left[\\left(\\overrightarrow{IQ}+\\overrightarrow{IR}\\right)+\\left(\\overrightarrow{IM}+\\overrightarrow{IS}\\right)+\\left(\\overrightarrow{IN}+\\overrightarrow{IP}\\right)\\right]=\\dfrac{1}{2}\\left(\\overrightarrow{IA}+\\overrightarrow{IB}+\\overrightarrow{IC}\\right)=\\dfrac{3}{2}\\overrightarrow{IO}$.\\\\\n%s'%(buoc_cuoi)).replace('- -','+').replace('+ -','-')
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
