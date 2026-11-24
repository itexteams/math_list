
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


def bt_dang25_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        k=random.choice([2,3])
        a_val=Rational(k,3)
        b_val=Rational(3-2*k,3)
        p=random.choice([1,2,3,4])
        q=random.choice([-4,-3,-2,-1,1,2,3,4])
        m=3*p
        n=3*q
        a_sym,b_sym=symbols('a b')
        bieuthuc=m*a_sym+n*b_sym
        kq=m*a_val+n*b_val
        xH=round(1.967*k,3)
        yH=round(0.9*k,3)
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.8]\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (4.6,0);\n'
        '\\coordinate (A) at (1.3,2.7);\n'
        '\\coordinate (M) at (2.3,0);\n'
        '\\coordinate (G) at (1.967,0.9);\n'
        '\\coordinate (H) at (%s,%s);\n'
        '\\draw[->] (A)--(B);\n'
        '\\draw[->] (A)--(C);\n'
        '\\draw[->] (A)--(H);\n'
        '\\draw (B)--(C) (A)--(M) (B)--(H);\n'
        '\\foreach \\p/\\pos in {A/above,B/below left,C/below right,M/below,G/above left,H/above right}{\n'
        '\\fill (\\p) circle (1.8pt) node[\\pos] {$\\p$};\n'
        '}\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )%(xH,yH)
        gt_H='là điểm đối xứng với $B$ qua $G$' if k==2 else 'thỏa mãn $\\overrightarrow{BH}=%s\\overrightarrow{BG}$'%(k)
        noidungcauhoi=('Cho tam giác $ABC$. Gọi $G$ là trọng tâm và $H$ %s. Biết rằng $\\overrightarrow{AH}=a\\overrightarrow{AC}+b\\overrightarrow{AB}$ với $a,b\\in\\mathbb{R}$. Tính giá trị của biểu thức $%s$.\n'%(gt_H,latex(bieuthuc))).replace('- -','+').replace('+ -','-')
        buoc_h='Vì $H$ là điểm đối xứng với $B$ qua $G$ nên $\\overrightarrow{BH}=2\\overrightarrow{BG}$.' if k==2 else 'Theo giả thiết ta có $\\overrightarrow{BH}=%s\\overrightarrow{BG}$.'%(k)
        loigiai=(hinh+'%s\\\\\nTa có $\\overrightarrow{AH}=\\overrightarrow{AB}+\\overrightarrow{BH}=\\overrightarrow{AB}+%s\\overrightarrow{BG}=\\overrightarrow{AB}+%s\\left(\\overrightarrow{AG}-\\overrightarrow{AB}\\right)=%s\\overrightarrow{AG}+%s\\overrightarrow{AB}$.\\\\\nVì $G$ là trọng tâm $\\triangle ABC$ nên $\\overrightarrow{AG}=\\dfrac{1}{3}\\left(\\overrightarrow{AB}+\\overrightarrow{AC}\\right)$, suy ra $\\overrightarrow{AH}=%s\\left(\\overrightarrow{AB}+\\overrightarrow{AC}\\right)+%s\\overrightarrow{AB}=%s\\overrightarrow{AC}+%s\\overrightarrow{AB}$.\\\\\nDo đó $a=%s$, $b=%s$. Khi đó $%s=%s$.'%(buoc_h,k,k,k,1-k,latex(Rational(k,3)),1-k,latex(a_val),latex(b_val),latex(a_val),latex(b_val),latex(bieuthuc),kq)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
