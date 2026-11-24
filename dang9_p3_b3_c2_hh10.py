
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


def bt_dang9_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        ds_vantoc=[20,25,30,35,40,45,50,55,60,65,70,75,80]
        while True:
            v1=random.choice(ds_vantoc)
            v2=random.choice(ds_vantoc)
            tyso=Rational(v2,v1)
            a=tyso.p
            b=tyso.q
            if b>1:
                break
        m=randint(1,5)
        n=randint(-5,5)
        while n==0:
            n=randint(-5,5)
        a_sym,b_sym=symbols('a b')
        bieuthuc=m*a_sym+n*b_sym
        kq=m*a+n*b
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.85]\n'
        '\\begin{scope}[shift={(0,3.2)}]\n'
        '\\foreach \\ang in {0,90,180,270}{\n'
        '\\fill[black] (0,0)--(\\ang:1.2)--(\\ang+22.5:0.35)--cycle;\n'
        '\\draw (0,0)--(\\ang:1.2)--(\\ang-22.5:0.35)--cycle;\n'
        '}\n'
        '\\foreach \\ang in {45,135,225,315}{\n'
        '\\fill[black] (0,0)--(\\ang:0.85)--(\\ang+22.5:0.25)--cycle;\n'
        '\\draw (0,0)--(\\ang:0.85)--(\\ang-22.5:0.25)--cycle;\n'
        '}\n'
        '\\fill[white] (0,0) circle (0.18);\n'
        '\\draw (0,0) circle (0.18);\n'
        '\\node[above] at (0,1.2) {\\scriptsize BẮC};\n'
        '\\node[below] at (0,-1.2) {\\scriptsize NAM};\n'
        '\\node[right] at (1.2,0) {\\scriptsize ĐÔNG};\n'
        '\\node[left] at (-1.2,0) {\\scriptsize TÂY};\n'
        '\\node[above right] at (45:0.85) {\\tiny ĐÔNG BẮC};\n'
        '\\node[above left] at (135:0.85) {\\tiny TÂY BẮC};\n'
        '\\node[below left] at (225:0.85) {\\tiny TÂY NAM};\n'
        '\\node[below right] at (315:0.85) {\\tiny ĐÔNG NAM};\n'
        '\\end{scope}\n'
        '\\draw (-4.5,0)--(4.5,0);\n'
        '\\draw (-4.5,-0.45)--(4.5,-0.45);\n'
        '\\draw[dashed] (-4.3,-0.225)--(4.3,-0.225);\n'
        '\\draw (-3.1,0.18) circle (0.18);\n'
        '\\draw (-2.3,0.18) circle (0.18);\n'
        '\\draw (-3.1,0.18)--(-2.7,0.48)--(-2.3,0.18);\n'
        '\\draw (-2.45,0.72)--(-2.3,0.18);\n'
        '\\draw (-2.6,0.72)--(-2.35,0.72);\n'
        '\\draw (-2.95,0.52)--(-2.65,0.52);\n'
        '\\draw (-2.8,0.52)--(-2.8,0.88);\n'
        '\\draw (-2.8,0.82)--(-2.48,0.72);\n'
        '\\draw (-2.8,1.02) circle (0.14);\n'
        '\\draw[->] (-2.0,0.55)--(-0.6,0.55) node[midway,above] {$\\overrightarrow{v_1}$};\n'
        '\\draw (3.1,0.18) circle (0.18);\n'
        '\\draw (2.3,0.18) circle (0.18);\n'
        '\\draw (3.1,0.18)--(2.7,0.48)--(2.3,0.18);\n'
        '\\draw (2.45,0.72)--(2.3,0.18);\n'
        '\\draw (2.6,0.72)--(2.35,0.72);\n'
        '\\draw (2.95,0.52)--(2.65,0.52);\n'
        '\\draw (2.8,0.52)--(2.8,0.88);\n'
        '\\draw (2.8,0.82)--(2.48,0.72);\n'
        '\\draw (2.8,1.02) circle (0.14);\n'
        '\\draw[->] (2.0,0.55)--(0.6,0.55) node[midway,above] {$\\overrightarrow{v_2}$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )
        noidungcauhoi=('Một người đi xe máy từ Tây sang hướng Đông với vận tốc $%s\\text{ km/h}$ được biểu thị bởi vectơ $\\overrightarrow{v_1}$ và một người khác đi xe máy từ hướng Đông sang hướng Tây với vận tốc $%s\\text{ km/h}$ được biểu thị bởi vectơ $\\overrightarrow{v_2}$. Biết rằng $\\overrightarrow{v_2}=-\\dfrac{a}{b}\\overrightarrow{v_1}$ ($a,b\\in\\mathbb{N}^*$), $\\dfrac{a}{b}$ là phân số tối giản. Tính $%s$.\n'%(v1,v2,latex(bieuthuc))+hinh).replace('- -','+').replace('+ -','-')
        loigiai=('Ta có: $\\overrightarrow{v_2}$ ngược hướng với $\\overrightarrow{v_1}$ và có độ lớn bằng $\\dfrac{%s}{%s}=%s$ lần độ lớn vectơ $\\overrightarrow{v_1}$.\\\\\nVì vậy $\\overrightarrow{v_2}=-%s\\overrightarrow{v_1}\\Rightarrow\\begin{cases} a=%s \\\\ b=%s \\end{cases}\\Rightarrow %s=%s$.'%(v2,v1,latex(tyso),latex(tyso),a,b,latex(bieuthuc),kq)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
