
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


def bt_dang3_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        c=random.choice([2,4,6,8,10,12,14,16])
        m=random.choice([1,2,3])
        bo=c//2
        h1=m*c*sqrt(3)
        number=Decimal(float(h1))
        kq=number.quantize(Decimal('0.1'),rounding=ROUND_HALF_UP)
        kq_vn=str(kq).replace('.','{,}')
        hs='' if m==1 else str(m)
        vt='%s\\overrightarrow{AB}+%s\\overrightarrow{AD}'%(hs,hs)
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
        '\\coordinate (A) at (-2.6,0);\n'
        '\\coordinate (C) at (2.6,0);\n'
        '\\coordinate (B) at (0,1.5);\n'
        '\\coordinate (D) at (0,-1.5);\n'
        '\\coordinate (O) at (0,0);\n'
        '\\draw[->] (A)--(B) node[midway,above left] {$%s$};\n'
        '\\draw[->] (A)--(D);\n'
        '\\draw (B)--(C)--(D) (A)--(C) (B)--(D);\n'
        '\\draw (-1.36,0.65)--(-1.24,0.85);\n'
        '\\draw (-1.36,-0.65)--(-1.24,-0.85);\n'
        '\\draw (-2.6,0) ++(-30:0.75) arc (-30:30:0.75);\n'
        '\\node at (-1.55,-0.32) {\\scriptsize $60^\\circ$};\n'
        '\\foreach \\p/\\pos in {A/left,B/above,C/right,D/below,O/below right}{\n'
        '\\fill (\\p) circle (1.8pt) node[\\pos] {$\\p$};\n'
        '}\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )%(c)
        noidungcauhoi=('Cho hình thoi $ABCD$ tâm $O$, cạnh bằng $%s$ và góc $\\widehat{BAD}=60^\\circ$. Tính độ dài vectơ $%s$ (kết quả làm tròn đến một chữ số sau dấu phẩy).\n'%(c,vt)).replace('- -','+').replace('+ -','-')
        loigiai=(hinh+'Tam giác $ABD$ cân tại $A$ và có góc $\\widehat{BAD}=60^\\circ$ nên $\\triangle ABD$ đều, suy ra $BD=%s$ và $BO=%s$.\\\\\nTa có $\\left|%s\\right|=%s\\left|\\overrightarrow{AB}+\\overrightarrow{AD}\\right|=%s\\left|\\overrightarrow{AC}\\right|=%sAO=%s\\sqrt{AB^2-BO^2}=%s\\sqrt{%s-%s}=%s\\sqrt{3}\\approx %s$.'%(c,bo,vt,hs,hs,2*m,2*m,2*m,c**2,bo**2,m*c,kq_vn)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
