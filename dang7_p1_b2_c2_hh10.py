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


def bt_dang7_p1_b2_c2_hh10(self):
            # Khai báo biến
            a=randint(2,10)
            b=randint(2,10)
            while b>=a:
                a=randint(2,10)
                b=randint(2,10)
            om=Rational(a+b,2)
            kq=a+b
            kq1=a+b+1
            kq2=Rational(a+b,3)
            kq3=Rational(a+b+1,2)
            # Câu hỏi
            noidungcauhoi=('''Cho hình thang $ABCD$ có $AB$ song song với $CD$, biết $AB=%s, CD=%s$, $O$ là trung điểm của $AD$. Độ dài $\\left| \\overrightarrow{OB}+\\overrightarrow{OC} \\right|$ là \n'''
                        %(latex(a),latex(b)
                        ))
            # Các đáp án
            da_d = '\\True $%s$' %(latex(kq))
            da_s1 = '$%s$' %(latex(kq1))
            da_s2 = '$%s$' %(latex(kq2))
            da_s3 = '$%s$' %(latex(kq3))    
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=(
                    '\\begin{center} \n'    
                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=1] \n'
                        '\\clip(-0.5335288863827738,-0.5113563339282198) rectangle (6.5434290214984365,3.6177402297543164); \n'
                        '\\draw (1.,3.)-- (4.,3.); \n'
                        '\\draw (4.,3.)-- (6.,0.); \n'
                        '\\draw (1.,3.)-- (0.,0.); \n'
                        '\\draw (0.,0.)-- (6.,0.); \n'
                        '\\draw [->] (0.5,1.5) -- (4.,3.);  \n'
                        '\\draw [->] (0.5,1.5) -- (6.,0.); \n'
                        '\\draw [->] (0.5,1.5) -- (5.,1.5); \n'
                        '\\draw (-0.5,0.08448798032470317) node[anchor=north west] {$A$}; \n'
                        '\\draw (5.9,0.13675502543460868) node[anchor=north west] {$B$}; \n'
                        '\\draw (4.097331310354857,3.4295788673586567) node[anchor=north west] {$C$}; \n'
                        '\\draw (0.3,3.471392503446581) node[anchor=north west] {$D$}; \n'
                        '\\draw (-0.2,1.777940241885642) node[anchor=north west] {$O$}; \n'
                        '\\draw (5.111311985487025,1.8302072869955477) node[anchor=north west] {$M$}; \n'
                    '\\end{tikzpicture} \n'
                        '\\end{center} \n'

                    '$OM$ là đường trung bình của hình thang $ABCD$ nên ta có \\\\ \n'
                    '\\hspace*{1cm} $OM=\\dfrac{AB+CD}{2}=\\dfrac{%s+%s}{2}=%s$.\\\\ \n'
                    'Khi đó \\\\ \n'
                    '\\hspace*{1cm} $\\left| \\overrightarrow{OB}+\\overrightarrow{OC} \\right|=2 \\left| \\overrightarrow{OM}\\right| =2 \\cdot %s = %s$.'

                    %(latex(a),latex(b),latex(om),latex(om),latex(kq)
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

