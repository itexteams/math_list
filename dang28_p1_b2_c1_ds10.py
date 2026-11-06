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


def bt_dang28_p1_b2_c1_ds10(self):
            #Khai báo biến
            a = randint(-4,-1) # a là số bất kỳ từ 1 đến 25
            b = randint(5,7) # b là số bất kỳ từ 1 đến 30
            c = randint(0,4) # a là số bất kỳ từ 1 đến 25
            d = randint(8,9) # b là số bất kỳ từ 1 đến 30
            e=20
            tha=['A','C','E','G','I','K','M','P','S','T','V']
            thb=['B','D','F','H','J','L','Q','U','X']
            thx =random.choice(tha)
            thy =random.choice(thb)
            list1=['giao1','giao2','giao3','giao4']
            rd = random.choice(list1)
            #Nội ung câu hỏi
            if rd=='giao1':
                noidungcauhoi = ('''Cho hai tập hợp $%s=\\left[ %s;%s \\right),%s=\\left( %s;+\\infty \\right)$. Khi đó $%s\\cap %s$ là tập nào sau đây?\n'''
                            %(str(thx),latex(a),latex(b),str(thy),latex(c),str(thx),str(thy)))
            # Các đáp án
                da_d = '\\True $%s\\cap %s = \\left( %s;%s \\right)$'%(str(thx),str(thy),latex(c),latex(b))
                da_s1 = '$%s\\cap %s = \\left( %s;%s \\right]$'%(str(thx),str(thy),latex(c),latex(b))
                da_s2 = '$%s\\cap %s = \\left[ %s;%s \\right)$'%(str(thx),str(thy),latex(c),latex(b))
                da_s3 = '$%s\\cap %s = \\left[ %s;+\\infty  \\right)$'%(str(thx),str(thy),latex(a))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Tập $%s\\cap %s$ là phần không bị gạch ở cả $%s$ và $%s$ nên $x\\in \\left( %s;%s \\right)$.\\\\ \n'
                '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s, %s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {[};\n'
                '\\draw (%s,0) node {)};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture} \n'
            '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s,%s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {(};\n'
                '\\draw (%s,0) node {)};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,%s}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture} \n'
            '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s, %s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {(};\n'
                '\\draw (%s,0) node {)};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture}'%(
                str(thx),str(thy),str(thx),str(thy),latex(c),latex(b),
                latex(a),latex(b),latex(a),latex(b),latex(a-0.2),latex(b+0.2),latex(b+0.4),
                                    latex(c),latex(e),latex(c),latex(e),latex(c-0.2),latex(e+0.2),latex(e+0.4),latex(e+0.8),
                                    latex(c),latex(b),latex(c),latex(b),latex(c-0.2),latex(b+0.2),latex(b+0.4)))

            if rd=='giao2':
                noidungcauhoi = ('''Cho hai tập hợp $%s=\\left[ %s;%s \\right),%s=\\left( %s;%s \\right]$. Khi đó $%s\\cap %s$ là tập nào sau đây?\n'''
                            %(str(thx),latex(a),latex(b),str(thy),latex(c),latex(d),str(thx),str(thy)))
            # Các đáp án
                da_d = '\\True $%s\\cap %s = \\left( %s;%s \\right)$'%(str(thx),str(thy),latex(c),latex(b))
                da_s1 = '$%s\\cap %s = \\left( %s;%s \\right]$'%(str(thx),str(thy),latex(c),latex(b))
                da_s2 = '$%s\\cap %s = \\left[ %s;%s \\right)$'%(str(thx),str(thy),latex(c),latex(b))
                da_s3 = '$%s\\cap %s = \\left[ %s;+\\infty  \\right)$'%(str(thx),str(thy),latex(a))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Tập $%s\\cap %s$ là phần không bị gạch ở cả $%s$ và $%s$ nên $x\\in \\left( %s;%s \\right)$. \\\\ \n'
                '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s, %s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {[};\n'
                '\\draw (%s,0) node {)};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture} \n'
            '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s,%s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {(};\n'
                '\\draw (%s,0) node {]};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture} \n'
            '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s, %s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {(};\n'
                '\\draw (%s,0) node {)};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture} '%(
                str(thx),str(thy),str(thx),str(thy),latex(c),latex(b),
                latex(a),latex(b),latex(a),latex(b),latex(a-0.2),latex(b+0.2),latex(b+0.4),
                                    latex(c),latex(d),latex(c),latex(d),latex(c-0.2),latex(d+0.2),latex(d+0.4),
                                    latex(c),latex(b),latex(c),latex(b),latex(c-0.2),latex(b+0.2),latex(b+0.4)))
            if rd=='giao3':
                noidungcauhoi = ('''Cho hai tập hợp $%s=\\left( -\\infty;%s \\right],%s=\\left( %s;%s \\right]$. Khi đó $%s\\cap %s$ là tập nào sau đây?\n'''
                            %(str(thx),latex(b),str(thy),latex(c),latex(d),str(thx),str(thy)))
            # Các đáp án
                da_d = '\\True $%s\\cap %s = \\left( %s;%s \\right]$'%(str(thx),str(thy),latex(c),latex(b))
                da_s1 = '$%s\\cap %s = \\left( %s;%s \\right)$'%(str(thx),str(thy),latex(c),latex(b))
                da_s2 = '$%s\\cap %s = \\left[ %s;%s \\right)$'%(str(thx),str(thy),latex(c),latex(b))
                da_s3 = '$%s\\cap %s = \\left[ %s;+\\infty  \\right)$'%(str(thx),str(thy),latex(a))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Tập $%s\\cap %s$ là phần không bị gạch ở cả $%s$ và $%s$ nên $x\\in \\left( %s;%s \\right]$. \\\\ \n'   
                '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s, %s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {()};\n'
                '\\draw (%s,0) node {]};    	\n'
                '\\foreach \\x in {%s,%s,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture} \n'
            '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s,%s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {(};\n'
                '\\draw (%s,0) node {]};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture} \n'
            '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s, %s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {(};\n'
                '\\draw (%s,0) node {]};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture}'%(
                str(thx),str(thy),str(thx),str(thy),latex(c),latex(b),
                latex(e),latex(b),latex(e),latex(b),latex(e-0.2),latex(e-0.4),latex(e),latex(b+0.2),latex(b+0.4),
                                    latex(c),latex(d),latex(c),latex(d),latex(c-0.2),latex(d+0.2),latex(d+0.4),
                                    latex(c),latex(b),latex(c),latex(b),latex(c-0.2),latex(b+0.2),latex(b+0.4)))
            if rd=='giao4':
                noidungcauhoi = ('''Cho hai tập hợp $%s=\\left( -\\infty;%s \\right),%s=\\left[ %s;+\\infty \\right)$. Khi đó $%s\\cap %s$ là tập nào sau đây?\n'''
                            %(str(thx),latex(b),str(thy),latex(c),str(thx),str(thy)))
            # Các đáp án
                da_d = '\\True $%s\\cap %s = \\left[ %s;%s \\right)$'%(str(thx),str(thy),latex(c),latex(b))
                da_s1 = '$%s\\cap %s = \\left( %s;%s \\right)$'%(str(thx),str(thy),latex(c),latex(b))
                da_s2 = '$%s\\cap %s = \\left( %s;%s \\right]$'%(str(thx),str(thy),latex(c),latex(b))
                da_s3 = '$%s\\cap %s = \\left( -\\infty ;+\\infty \\right)$'%(str(thx),str(thy))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
            # Nội dung lời giải
                loigiai=('Tập $%s\\cap %s$ là phần không bị gạch ở cả $%s$ và $%s$ nên $x\\in \\left[ %s;%s \\right)$.\\\\'
                '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s, %s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {(};\n'
                '\\draw (%s,0) node {)};    	\n'
                '\\foreach \\x in {%s,%s,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture} \n'
            '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s,%s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {[};\n'
                '\\draw (%s,0) node {]};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,%s}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture} \n'
            '\\begin{tikzpicture}\n'
                '\\draw [->] (-5,0)--(10,0) node[below] {$x$}; \n'
                '\\foreach \\x \\xtext in {%s, %s} \n'
                '\\draw (\\x,0.05)  (\\x,-0.05) node [below] {$\\xtext$};	\n'
                '\\draw (%s,0) node {[};\n'
                '\\draw (%s,0) node {)};    	\n'
                '\\foreach \\x in {-4.8,-4.6,...,%s} \n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
                '\\foreach \\x in {%s,%s,...,9.8}\n'
                '\\draw (\\x-0.1,-0.1)--(\\x+0.1,0.1);\n'
            '\\end{tikzpicture}'%(
                str(thx),str(thy),str(thx),str(thy),latex(c),latex(b),
                latex(e),latex(b),latex(e),latex(b),latex(e-0.2),latex(e-0.4),latex(e),latex(b+0.2),latex(b+0.4),
                                    latex(c),latex(e),latex(c),latex(e),latex(c-0.2),latex(e+0.2),latex(e+0.4),latex(e+0.8),
                                    latex(c),latex(b),latex(c),latex(b),latex(c-0.2),latex(b+0.2),latex(b+0.4)))
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
            '\\loigiai{\n'+str(loigiai)+'}'
                '\\end{ex}\n \\end{minipage} \n\n')    
            return content 

