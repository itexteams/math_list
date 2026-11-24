
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


def bt_dang18_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        while True:
            m=random.choice([3,6])
            n=random.choice([-6,-3,3,6])
            p=random.choice([-6,-3,3,6])
            a_val=(2*m+2*n-4*p)//3
            b_val=(-2*m+4*n-2*p)//3
            if a_val!=0 or b_val!=0:
                break
        k1=randint(1,5)
        k2=randint(-5,5)
        while k2==0:
            k2=randint(-5,5)
        a_sym,b_sym=symbols('a b')
        bieuthuc_tinh=k1*a_sym+k2*b_sym
        kq=k1*a_val+k2*b_val
        def dinh_dang_hs(hs,ten_vt,dau_tien=False):
            if hs==1:
                return ten_vt if dau_tien else '+'+ten_vt
            if hs==-1:
                return '-'+ten_vt
            if hs>0:
                return ('%s%s'%(hs,ten_vt)) if dau_tien else ('+%s%s'%(hs,ten_vt))
            return '%s%s'%(hs,ten_vt)
        to_hop=(dinh_dang_hs(m,'\\overrightarrow{AB}',True)+dinh_dang_hs(n,'\\overrightarrow{BC}')+dinh_dang_hs(p,'\\overrightarrow{CA}')).replace('- -','+').replace('+ -','-')
        ket_qua_uv=''
        if a_val!=0:
            ket_qua_uv+=dinh_dang_hs(a_val,'\\vec{u}',True)
        if b_val!=0:
            ket_qua_uv+=dinh_dang_hs(b_val,'\\vec{v}',a_val==0)
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
        '\\coordinate (A) at (0,0);\n'
        '\\coordinate (B) at (5,0);\n'
        '\\coordinate (C) at (1.5,3.8);\n'
        '\\coordinate (K) at (3.25,1.9);\n'
        '\\coordinate (M) at (0.75,1.9);\n'
        '\\coordinate (G) at (2.167,1.267);\n'
        '\\draw (A)--(B)--(C)--cycle;\n'
        '\\draw (A)--(K) (B)--(M);\n'
        '\\foreach \\p/\\pos in {A/below left,B/below right,C/above,K/above right,M/above left,G/below}{\n'
        '\\fill (\\p) circle (1.8pt) node[\\pos] {$\\p$};\n'
        '}\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )
        noidungcauhoi=('Cho $AK$ và $BM$ là hai trung tuyến của tam giác $ABC$, trọng tâm $G$. Đặt $\\vec{u}=\\overrightarrow{AK}$, $\\vec{v}=\\overrightarrow{BM}$. Biết rằng $%s=a\\vec{u}+b\\vec{v}$ với $a,b\\in\\mathbb{R}$. Tính giá trị của biểu thức $%s$.\n'%(to_hop,latex(bieuthuc_tinh))).replace('- -','+').replace('+ -','-')
        buoc_thay=(dinh_dang_hs(m,'\\left(\\dfrac{2}{3}\\vec{u}-\\dfrac{2}{3}\\vec{v}\\right)',True)+dinh_dang_hs(n,'\\left(\\dfrac{2}{3}\\vec{u}+\\dfrac{4}{3}\\vec{v}\\right)')+dinh_dang_hs(p,'\\left(-\\dfrac{4}{3}\\vec{u}-\\dfrac{2}{3}\\vec{v}\\right)')).replace('- -','+').replace('+ -','-')
        loigiai=(hinh+'Ta có:\\\\\n$\\bullet\\ \\overrightarrow{AB}=\\overrightarrow{AG}+\\overrightarrow{GB}=\\dfrac{2}{3}\\overrightarrow{AK}-\\dfrac{2}{3}\\overrightarrow{BM}=\\dfrac{2}{3}\\vec{u}-\\dfrac{2}{3}\\vec{v}$.\\\\\n$\\bullet\\ \\overrightarrow{BC}=2\\overrightarrow{BK}=2\\left(\\overrightarrow{BG}+\\overrightarrow{GK}\\right)=2\\left(\\dfrac{2}{3}\\overrightarrow{BM}+\\dfrac{1}{3}\\overrightarrow{AK}\\right)=\\dfrac{2}{3}\\vec{u}+\\dfrac{4}{3}\\vec{v}$.\\\\\n$\\bullet\\ \\overrightarrow{CA}=-\\left(\\overrightarrow{AK}+\\dfrac{1}{2}\\overrightarrow{BC}\\right)=-\\dfrac{4}{3}\\vec{u}-\\dfrac{2}{3}\\vec{v}$.\\\\\nSuy ra $%s=%s=%s$.\\\\\nDo đó $a=%s$, $b=%s$. Vậy $%s=%s$.'%(to_hop,buoc_thay,ket_qua_uv,a_val,b_val,latex(bieuthuc_tinh),kq)).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
