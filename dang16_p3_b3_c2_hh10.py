
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


def bt_dang11_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        a0=randint(2,8)
        while True:
            q1=random.choice([2,4])
            p1=randint(5,21)
            p=Rational(p1,q1)
            if p.q>1 and 2<=float(p)<=5.5:
                break
        while True:
            q2=random.choice([2,4])
            p2=randint(3,13)
            q=Rational(p2,q2)
            if q.q>1 and 1.5<=float(q)<=3.5:
                break
        OM_val=p*a0
        ON_val=q*a0
        h1=simplify(sqrt(OM_val**2+ON_val**2))
        number=Decimal(float(h1))
        kq=number.quantize(Decimal('0.1'),rounding=ROUND_HALF_UP)
        kq_vn=str(kq).replace('.','{,}')
        xM=round(float(p),2)
        yN=round(float(q),2)
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.85]\n'
        '\\coordinate (O) at (0,0);\n'
        '\\coordinate (A) at (1,0);\n'
        '\\coordinate (B) at (0,1);\n'
        '\\coordinate (M) at (%s,0);\n'
        '\\coordinate (N) at (0,%s);\n'
        '\\draw[->] (O)--(M);\n'
        '\\draw[->] (O)--(N);\n'
        '\\draw[->] (O)--(A);\n'
        '\\draw[->] (O)--(B);\n'
        '\\draw (A)--(B) (M)--(N);\n'
        '\\foreach \\p/\\pos in {O/below left,A/below,B/left,M/below right,N/above left}{\n'
        '\\fill (\\p) circle (1.8pt) node[\\pos] {$\\p$};\n'
        '}\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )%(xM,yN)
        noidungcauhoi=('Cho tam giác $OAB$ vuông cân tại $O$ với $OA=OB=%s$. Tính độ dài của vectơ $\\vec{u}=%s\\overrightarrow{OA}-%s\\overrightarrow{OB}$ (kết quả làm tròn đến một chữ số sau dấu phẩy).\n'%(a0,latex(p),latex(q))).replace('- -','+').replace('+ -','-')
        loigiai=(hinh+'Dựng điểm $M, N$ sao cho: $\\overrightarrow{OM}=%s\\overrightarrow{OA}$, $\\overrightarrow{ON}=%s\\overrightarrow{OB}$. Suy ra $OM=%s$, $ON=%s$.\\\\\nKhi đó $|\\vec{u}|=\\left|\\overrightarrow{OM}-\\overrightarrow{ON}\\right|=\\left|\\overrightarrow{NM}\\right|=MN=\\sqrt{OM^2+ON^2}=\\sqrt{\\left(%s\\right)^2+\\left(%s\\right)^2}=%s\\approx %s$.'%(latex(p),latex(q),latex(OM_val),latex(ON_val),latex(OM_val),latex(ON_val),latex(h1),kq_vn)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
