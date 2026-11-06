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


def bt_dang3_p3_b4_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                tcd=randint(-5,-1)
                tcn=-tcd
                c=randint(1,5)
                m=randint(-3,3)
                n=randint(-3,3)
                p=randint(-3,3)
                while m==0 or n==0 or p==0:
                    m=randint(-3,3)
                    n=randint(-3,3)
                    p=randint(-3,3)
                d=-c*tcd
                a=c*tcn
                b=2*d*tcn
                gox=2*tcd
                goy=-2*tcd
                x0=m*a+n*b+p*d

                #Nội ung câu hỏi
                noidungcauhoi = ('\\immini{'
                    'Cho hàm số $y=\\dfrac{ax+b}{%sx+d}$ có đồ thị như hình vẽ bên. Giá trị biểu thức $T=%sa+%sb+%sd$ bằng bao nhiêu?'
            '}{'
               '\\scalebox{0.8}{\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]'
                                '\\tikzset{every node/.style={scale=1}}'
                                '\\draw[->] (-6.1,0)--(2.1,0) node[below left] {$x$};'
                                '\\draw[->] (0,-3.1)--(0,5.1) node[below left] {$y$};'
                                '\\draw (0,1) node [below left] {$%s$};'#Tiệm cận ngang
                                '\\draw (-1,0) node [below left] {$%s$};'#Tiệm cận đứng
                                '\\draw (0,0) node [below left] {$O$};'
                                '\\draw (0,2) node [below left] {$%s$};'#Giao oy
                                '\\draw (-2,0) node [below left] {$%s$};'#Giao ox
                                '\\draw[thin] (-6,1)--(2,1);'
                                '\\begin{scope}'
                                '\\clip (-6,-3) rectangle (2,5);'
                                '\\draw[samples=200,domain=-6:5,smooth,variable=\\x] plot (\\x,{(1*(\\x)+2)/(1*(\\x)+1)});'
                                '\\end{scope}'
                                '\\end{tikzpicture}}}'
                                %(latex(c),latex(m),latex(n),latex(p),
                                    latex(tcn),latex(tcd),latex(goy),latex(gox)))

                # Nội dung lời giải
                loigiai=(
                         'Dựa vào hàm số và đồ thị ta có \\\\ \n'
                         'Tiệm cận ngang $y=\\dfrac{a}{%s}\\Rightarrow\\dfrac{a}{%s}= %s \\Leftrightarrow a=%s$.\\hspace {1 cm}$(1)$ \\\\ \n'
                         'Giao trục $Ox$ tại điểm có hoành độ $x_0=\\dfrac{-b}{a} \\Rightarrow \\dfrac{-b}{a}=%s\\Leftrightarrow b=%s\\cdot %s\\Leftrightarrow b=%s$.\\hspace {1 cm} $(2)$\\\\ \n'
                         'Tiệm cận đứng $x=\\dfrac{-d}{%s} \\Rightarrow \\dfrac{-d}{%s}=%s\\Leftrightarrow d=%s$.\\hspace {1 cm}$(3)$\\\\ \n'
                         'Thay $(1);(2);(3)$ vào $T$ ta được $T=%s\\cdot%s+%s\\cdot %s+%s\\cdot%s=%s$. \\\\ \n'
                         %(latex(c),latex(c),latex(tcn),latex(a),
                           latex(gox),latex(-gox),latex(a),latex(b),
                           latex(c),latex(c),latex(tcd),latex(d),
                                          latex(m),latex(a),latex(n),latex(b),latex(p),latex(d),latex(x0))
                         )

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(x0))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('+0', '').replace('1x', 'x').replace('.0', '').replace('1a', 'a').replace('1b', 'b').replace('1c', 'c').replace('1d', 'd')
            return content   

