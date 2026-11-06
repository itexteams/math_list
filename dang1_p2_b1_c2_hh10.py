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


def bt_dang1_p2_b1_c2_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến

                du = ['\\True $\\overrightarrow{MN}=\\overrightarrow{QP}$',
                    '\\True $\\overrightarrow{NM}=\\overrightarrow{PQ}$',
                    '\\True $\\overrightarrow{QM}=\\overrightarrow{PN}$',
                    '\\True $\\overrightarrow{MQ}=\\overrightarrow{NP}$',
                    '\\True $\\left| \\overrightarrow{MN} \\right|=\\left| \\overrightarrow{PQ} \\right|$',
                    '\\True $\\left| \\overrightarrow{MQ} \\right|=\\left| \\overrightarrow{PN} \\right|$',
                    ]

                da1= random.choice(du)
                du.remove(da1)
                da2= random.choice(du)
                du.remove(da2)
                da3= random.choice(du)
                du.remove(da3)
                da4= random.choice(du)
                s = ['$\\overrightarrow{MN}=\\overrightarrow{QP}$',
                    '$\\overrightarrow{MN}=\\overrightarrow{PQ}$',
                    '$\\overrightarrow{MQ}=\\overrightarrow{PN}$',
                    '$\\overrightarrow{QM}=\\overrightarrow{NP}$',
                    '$\\left| \\overrightarrow{MN} \\right|=\\left| \\overrightarrow{AC} \\right|$',
                    '$\\left| \\overrightarrow{CA} \\right|=\\left| \\overrightarrow{PN} \\right|$',
                    ' $\\left| \\overrightarrow{AC} \\right|=\\left| \\overrightarrow{DC} \\right|$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                s.remove(das3)
                das4 = random.choice(s)
                list_dapan = [da1,da2,da3,da4,das1,das2,das3,das4]
                # Câu hỏi
                noidungcauhoi = '''Cho tứ giác $ABCD$ với $M,N,P,Q$ lần lượt là trung điểm của $AB,BC,CD,DA$.\n'''
                # Các đáp án
                da_d = random.choice(list_dapan)
                list_dapan.remove(da_d)
                da_s1 = random.choice(list_dapan)
                list_dapan.remove(da_s1)
                da_s2 = random.choice(list_dapan) 
                list_dapan.remove(da_s2)
                da_s3 = random.choice(list_dapan)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                                       '\\begin{center} \n'
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                '\\clip(-0.64,-1.42) rectangle (9.2,5.12);\n'
                '\\draw (1.3,2.5)-- (4.8,3.5);\n'
                '\\draw (4.8,3.5)-- (6.3,1.5);\n'
                '\\draw (6.3,1.5)-- (2.8,0.5);\n'
                '\\draw (2.8,0.5)-- (1.3,2.5);\n'
                '\\draw (0.8,1.)-- (7.8,3.);\n'
                '\\draw (0,1) node[anchor=north west] {$A$};\n'
                '\\draw (1.3,4.7) node[anchor=north west] {$B$};\n'
                '\\draw (7.9,3.6) node[anchor=north west] {$C$};\n'
                '\\draw (4.52,-0.08) node[anchor=north west] {$D$};\n'
                '\\draw (0.46,2.8) node[anchor=north west] {$M$};\n'
                '\\draw (4.74,4.34) node[anchor=north west] {$N$};\n'
                '\\draw (6.3,1.56) node[anchor=north west] {$P$};\n'
                '\\draw (2.16,0.4) node[anchor=north west] {$Q$};\n'
                '\\draw (0.8,1.)-- (1.8,4.);\n'
                '\\draw (1.8,4.)-- (7.8,3.);\n'
                '\\draw (7.8,3.)-- (4.8,0.);\n'
                '\\draw (4.8,0.)-- (0.8,1.);\n'
                '\\end{tikzpicture} \n'
                '\\end{center}'

                    'Xét tam giác $ABC$ có $MN$ là đường trung bình $\\Rightarrow \\heva{& MN//AC \\\\& MN=\\dfrac{1}{2}AC}$.\\\\ \n'
                        'Xét tam giác $ADC$ có $PQ$ là đường trung bình $\\Rightarrow \\heva{& PQ//AC \\\\& PQ=\\dfrac{1}{2}AC}$.\\\\ \n'
                        '$MN$ song song và bằng $PQ$. Khi đó $MNPQ$ là hình bình hành.\\\\ \n'
                        'Vậy\\\\ \n'
                        '\\hspace*{1cm}$\\overrightarrow{MN}=\\overrightarrow{QP}$, \\hspace*{0.5cm} $\\overrightarrow{NM}=\\overrightarrow{PQ}$.\\\\ \n'
                            '\\hspace*{1cm}$\\overrightarrow{QM}=\\overrightarrow{PN}$, \\hspace*{0.5cm} $\\overrightarrow{MQ}=\\overrightarrow{NP}$.\\\\ \n'
                            '\\hspace*{1cm}$\\left| \\overrightarrow{MN} \\right|=\\left| \\overrightarrow{PQ} \\right|$, \\hspace*{0.5cm} $\\left| \\overrightarrow{MQ} \\right|=\\left| \\overrightarrow{PN} \\right|$.'
                            )


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('1x', 'x').replace('+0x^2', '').replace('+0x', '').replace('+0', '')
            return content

