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


def bt_dang7_p1_b3_c1_ds12(self):
            # Khai báo biến    
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='4':
                tcn=randint(1,9)
                tcd=tcn
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Tiệm cận đứng của đồ thị hàm số là')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-3.1)--(0,5.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (1,0) node [below left] {$%s$}; \n'
                                '\\draw (0,1) node [below left] {$%s$}; \n'
                                '\\draw[thin] (1.01,-3)--(1.01,5); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-3) rectangle (5,5); \n'
                                '\\draw[samples=200,domain=-3:0.99,smooth,variable=\\x] plot (\\x,{(1*(\\x)+-2)/(1*(\\x)+-1)}); \n'
                                '\\draw[samples=200,domain=1.01:5,smooth,variable=\\x] plot (\\x,{(1*(\\x)+-2)/(1*(\\x)+-1)}); \n'
                                '\\draw[thin] (-3,1/1)--(5,1/1); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(tcd),latex(tcn)
                                ))                                   
                # Các đáp án
                da_d = ' $y=%s$' %(latex(tcn))
                da_s1 = '$y=%s$' %(latex(tcn+1))
                da_s2 = '$x=%s$' %(latex(tcd-2))
                da_s3 = '\\True $x=%s$' %(latex(tcd))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy đồ thị hàm số có tiệm cận đứng là $x=%s$. \\\\ \n'
                        %(latex(tcd))
                        )
            if dang=='3':
                tcn=randint(1,9)
                tcd=tcn
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Tiệm cận ngang của đồ thị hàm số là')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-3.1)--(0,5.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (1,0) node [below left] {$%s$}; \n'
                                '\\draw (0,1) node [below left] {$%s$}; \n'
                                '\\draw[thin] (1.01,-3)--(1.01,5); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-3) rectangle (5,5); \n'
                                '\\draw[samples=200,domain=-3:0.99,smooth,variable=\\x] plot (\\x,{(1*(\\x)+-2)/(1*(\\x)+-1)}); \n'
                                '\\draw[samples=200,domain=1.01:5,smooth,variable=\\x] plot (\\x,{(1*(\\x)+-2)/(1*(\\x)+-1)}); \n'
                                '\\draw[thin] (-3,1/1)--(5,1/1); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(tcd),latex(tcn)
                                ))                               
                # Các đáp án
                da_d = '\\True $y=%s$' %(latex(tcn))
                da_s1 = '$y=%s$' %(latex(tcn+1))
                da_s2 = '$x=%s$' %(latex(tcd-1))
                da_s3 = '$x=%s$' %(latex(tcd))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy đồ thị hàm số có tiệm cận ngang là $y=%s$. \\\\ \n'
                        %(latex(tcn))
                        )
            if dang=='2':
                tcn=randint(1,9)
                tcd=-2*tcn
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Tiệm cận đứng của đồ thị hàm số là')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-6.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-3.1)--(0,4.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below left] {$%s$}; \n'
                                '\\draw (0,1) node [below left] {$%s$}; \n'
                                '\\draw[thin] (-1.99,-3)--(-1.99,4); \n'
                                '\\begin{scope} \n'
                                    '\\clip (-6,-3) rectangle (2,4); \n'
                                    '\\draw[samples=200,domain=-6:-2.01,smooth,variable=\\x] plot (\\x,{(1*(\\x)+1)/(1*(\\x)+2)}); \n'
                                    '\\draw[samples=200,domain=-1.99:2,smooth,variable=\\x] plot (\\x,{(1*(\\x)+1)/(1*(\\x)+2)}); \n'
                                    '\\draw[thin] (-6,1/1)--(2,1/1); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'

                                %(latex(tcd),latex(tcn)
                                ))                                   
                # Các đáp án
                da_d = ' $y=%s$' %(latex(tcn-2))
                da_s1 = '$y=%s$' %(latex(tcn))
                da_s2 = '$x=%s$' %(latex(tcd+1))
                da_s3 = '\\True $x=%s$' %(latex(tcd))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy đồ thị hàm số có tiệm cận đứng là $x=%s$. \\\\ \n'
                        %(latex(tcd))
                        )
            if dang=='1':
                tcn=randint(1,9)
                tcd=-2*tcn
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Tiệm cận ngang của đồ thị hàm số là')
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-6.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-3.1)--(0,4.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below left] {$%s$}; \n'
                                '\\draw (0,1) node [below left] {$%s$}; \n'
                                '\\draw[thin] (-1.99,-3)--(-1.99,4); \n'
                                '\\begin{scope} \n'
                                    '\\clip (-6,-3) rectangle (2,4); \n'
                                    '\\draw[samples=200,domain=-6:-2.01,smooth,variable=\\x] plot (\\x,{(1*(\\x)+1)/(1*(\\x)+2)}); \n'
                                    '\\draw[samples=200,domain=-1.99:2,smooth,variable=\\x] plot (\\x,{(1*(\\x)+1)/(1*(\\x)+2)}); \n'
                                    '\\draw[thin] (-6,1/1)--(2,1/1); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                %(latex(tcd),latex(tcn)
                                ))                                   
                # Các đáp án
                da_d = '\\True $y=%s$' %(latex(tcn))
                da_s1 = '$y=%s$' %(latex(tcn-3))
                da_s2 = '$x=%s$' %(latex(tcd+2))
                da_s3 = '$x=%s$' %(latex(tcd))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy đồ thị hàm số có tiệm cận ngang là $y=%s$. \\\\ \n'
                        %(latex(tcn))
                        )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n \\immini{'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n }{'+hinhve+ '} \n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

