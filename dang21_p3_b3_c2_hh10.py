
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


def bt_dang21_p3_b3_c2_hh10(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        n=random.choice([1,2,3,4,5])
        d1=random.choice([1,-1])
        d2=random.choice([1,-1])
        v1='AC' if d1==1 else 'CA'
        v2='PC' if d2==1 else 'CP'
        kq=Rational(n+2,2)*d1*d2
        xN=round((1.5+2.5*n)/(n+1),3)
        yN=round(3.2/(n+1),3)
        xP=round((3.0+5.0*n)/(n+2),3)
        yP=round(6.4/(n+2),3)
        xK=round((xP+5.0)/2,3)
        yK=round(yP/2,3)
        hinh=(
        '\\begin{center}\n'
        '\\begin{tikzpicture}[line width=1pt,>=stealth,scale=0.9]\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (5,0);\n'
        '\\coordinate (A) at (1.5,3.2);\n'
        '\\coordinate (M) at (2.5,0);\n'
        '\\coordinate (N) at (%s,%s);\n'
        '\\coordinate (P) at (%s,%s);\n'
        '\\coordinate (K) at (%s,%s);\n'
        '\\draw (A)--(B)--(C)--(A);\n'
        '\\draw (A)--(M) (B)--(P) (M)--(K);\n'
        '\\draw (1.2,-0.1)--(1.3,0.1);\n'
        '\\draw (3.7,-0.1)--(3.8,0.1);\n'
        '\\foreach \\p/\\pos in {A/above,B/below left,C/below right,M/below,N/left,P/above right,K/above right}{\n'
        '\\fill (\\p) circle (1.8pt) node[\\pos] {$\\p$};\n'
        '}\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        )%(xN,yN,xP,yP,xK,yK)
        if n==1:
            gt_N='và $N$ là trung điểm của $AM$'
            buoc_N='mà $N$ là trung điểm của $AM$ nên suy ra $P$ là trung điểm của $AK$, tức là $AP=PK$'
        else:
            gt_N='và điểm $N$ nằm trên đoạn $AM$ sao cho $NA=%sNM$'%(n)
            buoc_N='theo định lí Thales trong $\\triangle AMK$ ta có $\\dfrac{AP}{PK}=\\dfrac{AN}{NM}=%s\\Rightarrow AP=%sPK$'%(n,n)
        noidungcauhoi=('Cho tam giác $ABC$. Gọi $M$ là trung điểm của $BC$ %s. Đường thẳng $BN$ cắt $AC$ tại $P$. Biết rằng $\\overrightarrow{%s}=x\\overrightarrow{%s}$, giá trị của $x$ bằng bao nhiêu?\n'%(gt_N,v1,v2)).replace('- -','+').replace('+ -','-')
        loigiai=(hinh+'Kẻ $MK\\parallel BP\\ (K\\in AC)$. Do $M$ là trung điểm của $BC$ nên suy ra $K$ là trung điểm của $CP$, suy ra $PK=KC$ và $PC=2PK$.\\\\\nVì $MK\\parallel BP\\Rightarrow MK\\parallel NP$, %s.\\\\\nDo đó $AC=AP+PC=%sPK$, suy ra $\\dfrac{AC}{PC}=%s$.\\\\\nVậy $\\overrightarrow{%s}=%s\\overrightarrow{%s}\\Rightarrow x=%s$.'%(buoc_N,n+2,latex(Rational(n+2,2)),v1,latex(kq),v2,latex(kq))).replace('- -','+').replace('+ -','-')
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
    content = ('\\begin{minipage}{\\textwidth} \n'
    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
    '\\loigiai{ \n' +str(loigiai)+'}\n'
    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content
