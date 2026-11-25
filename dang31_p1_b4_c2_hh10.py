
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


def bt_dang31_p1_b4_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        tA,tB,tC=random.choice([('A','B','C'),('M','N','P')])
        a,b,c=random.choice([(3,4,5),(4,3,5),(6,8,10),(8,6,10),(5,12,13),(12,5,13)])
        xA=randint(-4,4)
        yA=randint(-4,4)
        s1=random.choice([-1,1])
        s2=random.choice([-1,1])
        xB=xA
        yB=yA+s1*a
        xC=xA+s2*b
        yC=yA
        dyAB=s1*a
        dxAC=s2*b
        dxBC=s2*b
        dyBC=-s1*a
        P=a+b+c
        tich_vh=b*b
        cos_sai=Rational(b,c)
        cos_dung=Rational(-b,c)
        du=['$\\cos\\left(\\overrightarrow{%s%s};\\overrightarrow{%s%s}\\right)=%s$'%(tA,tC,tC,tB,latex(cos_sai).replace('\\frac','\\dfrac'))]
        da=random.choice(du)
        s=['$\\Delta %s%s%s$ vuông'%(tA,tB,tC),'Chu vi tam giác $\\Delta %s%s%s$ bằng $P=%s$'%(tA,tB,tC,latex(P)),'$\\overrightarrow{%s%s}\\cdot\\overrightarrow{%s%s}=%s$'%(tA,tC,tB,tC,latex(tich_vh))]
        das1=random.choice(s)
        s.remove(das1)
        das2=random.choice(s)
        s.remove(das2)
        das3=random.choice(s)
        noidungcauhoi=('''Cho tam giác $%s%s%s$ có $%s(%s; %s)$, $%s(%s; %s)$, $%s(%s; %s)$. Trong các khẳng định sau, khẳng định nào sai?\n'''%(tA,tB,tC,tA,latex(xA),latex(yA),tB,latex(xB),latex(yB),tC,latex(xC),latex(yC))).replace('- -','+').replace('+ -','-')
        da_d=('\\True '+str(da)).replace('- -','+').replace('+ -','-')
        da_s1=str(das1).replace('- -','+').replace('+ -','-')
        da_s2=str(das2).replace('- -','+').replace('+ -','-')
        da_s3=str(das3).replace('- -','+').replace('+ -','-')
        list_1=[da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)
        l1='Ta có: $\\overrightarrow{%s%s}=(0; %s) \\Rightarrow %s%s=%s$; $\\overrightarrow{%s%s}=(%s; 0) \\Rightarrow %s%s=%s$; $\\overrightarrow{%s%s}=(%s; %s) \\Rightarrow %s%s=%s$. \\\\ '%(tA,tB,latex(dyAB),tA,tB,latex(a),tA,tC,latex(dxAC),tA,tC,latex(b),tB,tC,latex(dxBC),latex(dyBC),tB,tC,latex(c))
        l2='Do $%s%s^2+%s%s^2=%s%s^2$ nên $\\Delta %s%s%s$ vuông và chu vi tam giác $P=%s$. \\\\ '%(tA,tB,tA,tC,tB,tC,tA,tB,tC,latex(P))
        l3='Mặt khác, $\\overrightarrow{%s%s}\\cdot\\overrightarrow{%s%s}=%s \\Rightarrow \\cos\\left(\\overrightarrow{%s%s};\\overrightarrow{%s%s}\\right)=\\dfrac{-\\overrightarrow{%s%s}\\cdot\\overrightarrow{%s%s}}{%s%s\\cdot %s%s}=\\dfrac{-%s}{%s\\cdot %s}=%s$.'%(tA,tC,tB,tC,latex(tich_vh),tA,tC,tC,tB,tA,tC,tB,tC,tA,tC,tC,tB,latex(tich_vh),latex(b),latex(c),latex(cos_dung).replace('\\frac','\\dfrac'))
        loigiai=(l1+l2+l3).replace('- -','+').replace('+ -','-').replace('--','+').replace('+-','-')
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
