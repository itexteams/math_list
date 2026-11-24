
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


def bt_dang12_p3_b3_c2_hh10(self):
    lisdang=['1','2']
    dang=random.choice(lisdang)
    d1=random.choice([1,-1])
    d2=random.choice([1,-1])
    v_ij='IJ' if d1==1 else 'JI'
    v_ae='AE' if d2==1 else 'EA'
    arrow_ij='(I)--(J)' if d1==1 else '(J)--(I)'
    arrow_ae='(A)--(E)' if d2==1 else '(E)--(A)'
    hinh=(
    '\\begin{center}\n'
    '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
    '\\coordinate (A) at (0,2.5);\n'
    '\\coordinate (B) at (1.5,4);\n'
    '\\coordinate (C) at (4.2,2.6);\n'
    '\\coordinate (D) at (3.3,0.8);\n'
    '\\coordinate (E) at (1.0,-0.2);\n'
    '\\coordinate (M) at (0.75,3.25);\n'
    '\\coordinate (N) at (2.85,3.3);\n'
    '\\coordinate (P) at (3.75,1.7);\n'
    '\\coordinate (Q) at (2.15,0.3);\n'
    '\\coordinate (I) at (2.25,2.475);\n'
    '\\coordinate (J) at (2.5,1.8);\n'
    '\\draw (A)--(B)--(C)--(D)--(E);\n'
    '\\draw[->] %s;\n'
    '\\draw (M)--(P) (N)--(Q);\n'
    '\\draw[->] %s;\n'
    '\\foreach \\p/\\pos in {A/left,B/above,C/right,D/below right,E/below left,M/above left,N/above right,P/right,Q/below,I/above,J/below right}{\n'
    '\\fill (\\p) circle (1.8pt) node[\\pos] {$\\p$};\n'
    '}\n'
    '\\end{tikzpicture}\n'
    '\\end{center}\n'
    )%(arrow_ae,arrow_ij)
    if dang=='1':
        t=randint(1,6)
        m=4*t
        kq=t*d1*d2
        noidungcauhoi=('Cho ngũ giác $ABCDE$. Gọi $M,N,P,Q$ lần lượt là trung điểm các cạnh $AB,BC,CD,DE$. Gọi $I$ và $J$ lần lượt là trung điểm các đoạn $MP$ và $NQ$. Biết rằng $%s\\overrightarrow{%s}=k\\overrightarrow{%s}$. Tìm giá trị của $k$.\n'%(m,v_ij,v_ae)).replace('- -','+').replace('+ -','-')
        buoc_cuoi='Từ $\\overrightarrow{IJ}=\\dfrac{1}{4}\\overrightarrow{AE}$ suy ra $%s\\overrightarrow{%s}=%s\\overrightarrow{%s}$. Vậy $k=%s$.'%(m,v_ij,kq,v_ae,kq)
    if dang=='2':
        m=randint(1,6)
        hs='' if m==1 else str(m)
        kq=4*m*d1*d2
        noidungcauhoi=('Cho ngũ giác $ABCDE$. Gọi $M,N,P,Q$ lần lượt là trung điểm các cạnh $AB,BC,CD,DE$. Gọi $I$ và $J$ lần lượt là trung điểm các đoạn $MP$ và $NQ$. Biết rằng $%s\\overrightarrow{%s}=k\\overrightarrow{%s}$. Tìm giá trị của $k$.\n'%(hs,v_ae,v_ij)).replace('- -','+').replace('+ -','-')
        buoc_cuoi='Từ $\\overrightarrow{IJ}=\\dfrac{1}{4}\\overrightarrow{AE}\\Rightarrow\\overrightarrow{AE}=4\\overrightarrow{IJ}$, suy ra $%s\\overrightarrow{%s}=%s\\overrightarrow{%s}$. Vậy $k=%s$.'%(hs,v_ae,kq,v_ij,kq)
    loigiai=(hinh+'Ta có: $2\\overrightarrow{IJ}=\\overrightarrow{IQ}+\\overrightarrow{IN}=\\overrightarrow{IM}+\\overrightarrow{MQ}+\\overrightarrow{IP}+\\overrightarrow{PN}=\\overrightarrow{MQ}+\\overrightarrow{PN}$.\\\\\n$\\begin{cases} \\overrightarrow{MQ}=\\overrightarrow{MA}+\\overrightarrow{AE}+\\overrightarrow{EQ} \\\\ \\overrightarrow{MQ}=\\overrightarrow{MB}+\\overrightarrow{BD}+\\overrightarrow{DQ} \\end{cases}\\Rightarrow 2\\overrightarrow{MQ}=\\overrightarrow{AE}+\\overrightarrow{BD}\\Leftrightarrow\\overrightarrow{MQ}=\\dfrac{1}{2}\\left(\\overrightarrow{AE}+\\overrightarrow{BD}\\right)$, $\\overrightarrow{PN}=-\\dfrac{1}{2}\\overrightarrow{BD}$.\\\\\nSuy ra: $2\\overrightarrow{IJ}=\\dfrac{1}{2}\\left(\\overrightarrow{AE}+\\overrightarrow{BD}\\right)-\\dfrac{1}{2}\\overrightarrow{BD}=\\dfrac{1}{2}\\overrightarrow{AE}\\Rightarrow\\overrightarrow{IJ}=\\dfrac{1}{4}\\overrightarrow{AE}$.\\\\\n%s'%(buoc_cuoi)).replace('- -','+').replace('+ -','-')
    dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
