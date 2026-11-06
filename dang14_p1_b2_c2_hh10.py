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


def bt_dang14_p1_b2_c2_hh10(self):
            # Khai báo biến
            d = ['$\\overrightarrow{GA}+\\overrightarrow{GD}=\\overrightarrow{GP}$',
            '$\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{GQ}$',
            '$\\overrightarrow{PA}+\\overrightarrow{PD}=\\overrightarrow{PG}$',
            '$\\overrightarrow{QB}+\\overrightarrow{QC}=\\overrightarrow{QG}$',	
            '$\\overrightarrow{AP}+\\overrightarrow{AG}=\\overrightarrow{AD}$',
            '$\\overrightarrow{BG}+\\overrightarrow{BQ}=\\overrightarrow{BC}$',
            '$\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}+\\overrightarrow{GD}=\\vec{0}$'

                ]
            da= random.choice(d)
            s = ['$\\overrightarrow{GA}+\\overrightarrow{GD}=\\overrightarrow{GI}$',
            '$\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{GJ}$',
            '$\\overrightarrow{PA}+\\overrightarrow{PD}=\\overrightarrow{PQ}$',
            '$\\overrightarrow{QB}+\\overrightarrow{QC}=\\overrightarrow{QP}$',
            '$\\overrightarrow{AP}+\\overrightarrow{AG}=\\overrightarrow{DA}$',
            '$\\overrightarrow{BG}+\\overrightarrow{BQ}=\\overrightarrow{CB}$',
                ]
            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)
            # Câu hỏi
            noidungcauhoi='''Cho tứ giác lồi $ABCD$ có $I, J$ lần lượt là trung điểm hai cạnh $AD$, $BC$ và $G$ là trung điểm $IJ$. Gọi $P$ là điểm đối xứng của $G$ qua $I$, $Q$ là điểm đối xứng của $G$ qua $J$. Khẳng định nào sau đây đúng? \n'''
            # Các đáp án
            da_d = ('\\True ' +str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=(
            '\\begin{center} \n'
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.7]\n'
            '\\clip(-0.02,-5.32) rectangle (13.5,3.52);\n'
            '\\draw (4.,1.)-- (10.,2.);\n'
            '\\draw (10.,2.)-- (8.,-4.);\n'
            '\\draw (8.,-4.)-- (4.,-2.);\n'
            '\\draw (4.,-2.)-- (4.,1.);\n'
            '\\draw (4.,-0.5)-- (9.,-1.);\n'
            '\\draw (10.,2.)-- (6.5,-0.75);\n'
            '\\draw (6.5,-0.75)-- (8.,-4.);\n'
            '\\draw (4.,1.)-- (6.5,-0.75);\n'
            '\\draw (6.5,-0.75)-- (4.,-2.);\n'
            '\\draw (4.,1.)-- (1.5,-0.25);\n'
            '\\draw (1.5,-0.25)-- (4.,-2.);\n'
            '\\draw (1.5,-0.25)-- (4.,-0.5);\n'
            '\\draw (11.5,-1.25)-- (10.,2.);\n'
            '\\draw (11.5,-1.25)-- (9.,-1.);\n'
            '\\draw (11.5,-1.25)-- (8.,-4.);\n'
            '\\draw (3.6,1.8) node[anchor=north west] {\\textit{A}};\n'
            '\\draw (10,2.6) node[anchor=north west] {\\textit{B}};\n'
            '\\draw (7.8,-4) node[anchor=north west] {\\textit{C}};\n'
            '\\draw (3.6,-2) node[anchor=north west] {\\textit{D}};\n'
            '\\draw (6,0.1) node[anchor=north west] {\\textit{G}};\n'
            '\\draw (0.9,0.3) node[anchor=north west] {\\textit{P}};\n'
            '\\draw (4,0.4) node[anchor=north west] {\\textit{I}};\n'
            '\\draw (8.5,0) node[anchor=north west] {\\textit{J}};\n'
            '\\draw (11.5,-0.7) node[anchor=north west] {\\textit{Q}};\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            'Hai tứ giác $AGDP$ và $BGCQ$ có hai đường chéo giao nhau tại trung điểm mỗi đường nên chúng là các hình bình hành. \\\\ \n'
            'Theo quy tắc hình bình hành ta có: \\\\ \n'
            '$\\overrightarrow{GA}+\\overrightarrow{GD}=\\overrightarrow{GP}$.\\\\ \n'
            '$\\overrightarrow{GB}+\\overrightarrow{GC}=\\overrightarrow{GQ}$.\\\\ \n'
            '$\\overrightarrow{PA}+\\overrightarrow{PD}=\\overrightarrow{PG}$.\\\\ \n'
            '$\\overrightarrow{QB}+\\overrightarrow{QC}=\\overrightarrow{QG}$.\\\\ \n'
            '$\\overrightarrow{AP}+\\overrightarrow{AG}=\\overrightarrow{AD}$.\\\\ \n'
            '$\\overrightarrow{BG}+\\overrightarrow{BQ}=\\overrightarrow{BC}$.\\\\ \n'
            '$\\overrightarrow{GA}+\\overrightarrow{GB}+\\overrightarrow{GC}+\\overrightarrow{GD}=\\left( \\overrightarrow{GA}+\\overrightarrow{GD}\\right)+\\left( \\overrightarrow{GB}+\\overrightarrow{GC} \\right)=\\overrightarrow{GP}+\\overrightarrow{GQ}=\\vec{0}$.'
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

