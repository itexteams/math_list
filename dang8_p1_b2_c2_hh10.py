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


def bt_dang8_p1_b2_c2_hh10(self):
            #Khai báo biến
            a = randint(10,50) # b là số bất kỳ từ 1 đến 30
            b = Rational(a,2)
            x0 = Rational(a,3)
            S = {x0+1,x0+2,x0+3,x0-1,x0-2,x0-3}
            s1=S.pop()
            s2=S.pop()
            s3=S.pop()
            #Nội ung câu hỏi
            noidungcauhoi = ('''Gọi $G$ là trọng tâm tam giác vuông $ABC$, với cạnh huyền $BC=%s$. Độ dài của vectơ $\\overrightarrow{GB}+\\overrightarrow{GC}$ là \n'''
                            %(latex(a)))
            # Các đáp án
            da_d = '\\True $%s$'%(latex(x0))
            da_s1 = '$%s$'%(latex(s1))
            da_s2 = '$%s$'%(latex(s2))
            da_s3 = '$%s$'%(latex(s3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai =('Gọi $M$ là trung điểm $BC$.\\\\\n'
                        'Ta có $AM=\\dfrac{1}{2}BC=%s; AG=\\dfrac{2}{3}AM=%s$.\\\\\n' 
                        'Mặt khác $\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}=\\vec{0}\\Rightarrow \\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{AG}.$\\\\\n' 
                        'Suy ra $\\left| \\overrightarrow{GB}+\\overrightarrow{GC} \\right|=\\left| \\overrightarrow{AG} \\right|=AG=%s$.' 
                        %(latex(b),latex(x0),latex(x0)))
            hinhve = ('\\begin{center}\n'
                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.8] \n'
                '\\clip(-2.8739899218492977,-3.386525037656625) rectangle (13.477625404453399,4.771234484957983);\n'
                '\\draw (2.,3.)-- (2.,-2.);\n'
                '\\draw (2.,-2.)-- (9.,-2.);\n'
                '\\draw (9.,-2.)-- (2.,3.);\n'
                '\\draw (2.,-2.)-- (5.5,0.5);\n'
                '\\draw (2.,3.)-- (4.333333333333333,-0.3333333333333333);\n'
                '\\draw (4.333333333333333,-0.3333333333333333)-- (9.,-2.);\n'
                '\\draw (1.5839007907299145,-2.1051070595468087) node[anchor=north west] {A};\n'
                '\\draw (1.8,3.7) node[anchor=north west] {B};\n'
                '\\draw (9,-2) node[anchor=north west] {C};\n'
                '\\draw (5.5,1.2) node[anchor=north west] {M};\n'
                '\\draw (4.2,-0.5) node[anchor=north west] {G};\n'
                '\\end{tikzpicture}'
                '\\end{center}')
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'
                +hinhve+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac'). replace('1x','x').replace('-1x','-x'). replace('1y','y'). replace('.0',''). replace('+-','-')
            return content

