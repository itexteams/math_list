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


def bt_dang11_p1_b2_c2_hh10(self):
            # Khai báo biến
            a = randint(2,20)
            kq=sqrt(10*a**2)/2
            kq1=sqrt(10*a**2)
            kq2=sqrt(10*a**2)/4
            kq3=sqrt(10*a**2)/8

            #Nội ung câu hỏi
            noidungcauhoi = ('''Cho tam giác $ABC$ vuông cân tại $A$ có $BC=%s a\\sqrt{2}$, $M$ là trung điểm của $BC$. Độ dài của vecctơ $\\overrightarrow{BA}+\\overrightarrow{BM}$ là \n'''
                            %(latex(a)))
            # Các đáp án
            da_d = '\\True $%s a$'%(latex(kq))
            da_s1 = '$%s a$'%(latex(kq1))
            da_s2 = '$%s a$'%(latex(kq2))
            da_s3 = '$%s a$'%(latex(kq3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=(
                    '\\begin{center} \n'    
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1]  \n'
                        '\\clip(-0.7007959793002955,-0.8817355241054591) rectangle (6.7014850841062295,3.6211357459192843); \n'
                        '\\draw (0.,0.)-- (3.,3.); \n'
                        '\\draw (3.,3.)-- (6.,0.); \n'
                        '\\draw (6.,0.)-- (0.,0.); \n'
                        '\\draw (3.,0.)-- (6.,3.); \n'
                        '\\draw (6.,3.)-- (3.,3.); \n'
                        '\\draw (6.,3.)-- (6.,0.); \n'
                        '\\draw (0.,0.)-- (6.,3.); \n'
                        '\\draw (2.714796618206276,3.643100971626722) node[anchor=north west] {$A$}; \n'
                        '\\draw (-0.68114372222591784,0.21652576126642956) node[anchor=north west] {$B$}; \n'
                        '\\draw (6.002354441420285,0.0298213427532085) node[anchor=north west] {$C$}; \n'
                        '\\draw (2.8575705853046216,-0.08000478578398036) node[anchor=north west] {$M$}; \n'
                        '\\draw (6.152354441420285,3.4234487145523445) node[anchor=north west] {$N$}; \n'
                        '\\draw (2.8220138771706353,2.8220138771706353)-- (3.0332923909641236,2.6217179762308658); \n'
                        '\\draw (3.0332923909641236,2.6217179762308658)-- (3.19480459451291,2.80519540548709); \n'
                    '\\end{tikzpicture} \n'
                        '\\end{center} \n'

                    'Dựng hình bình hành $ABMN$.\\\\\n'
                    'Suy ra $\\left| \\overrightarrow{BA}+\\overrightarrow{BM} \\right|=\\left| \\overrightarrow{BN} \\right|= BN$. \\\\ \n'
                    'Ta có \\\\ \n'
                    '$NC=AM=\\dfrac{1}{2}BC=\\dfrac{%s a \\sqrt{2}}{2} \\Rightarrow BN=\\sqrt{BC^2+NC^2}=%s a$.'
                    %(latex(a),latex(kq)
                        )
                    )
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

