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


def bt_dang6_p4_b2_c1_hh10(self):
            # Khai báo biến
            lis1=[5,6,7,8,9,10,11,12,13,14,15]
            a=random.choice(lis1)
            b=random.choice(lis1)
            c=random.choice(lis1)
            while a+b-c<=0 or a+c-b<=0 or b+c-a<=0:
                a=random.choice(lis1)
                b=random.choice(lis1)
                c=random.choice(lis1)
            bm=a-2
            kq=c**2+bm**2-2*c*bm*Rational(c**2+a**2-b**2,2*c*a)    
            kq1=c**2+bm**2+c*bm*Rational(c**2+a**2-b**2,2*c*a)  
            kq2=c**2+bm**2+4*c*bm*Rational(c**2+a**2-b**2,2*c*a)  
            kq3=c**2+bm**2+3*c*bm*Rational(c**2+a**2-b**2,2*c*a)  

            lis=['1']
            dang=random.choice(lis)
            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $AB=%s, BC=%s, AC=%s$. Một điểm $M$ nằm trên cạnh $BC$ sao cho $BM = %s$. Tính độ dài đoạn thẳng $AM$.'''
                            %(latex(c),latex(a),latex(b),latex(bm)
                            ))
                # Các đáp án
                da_d = '\\True $AM = %s$' %(latex(sqrt(kq)))
                da_s1 = '$AM = %s$' %(latex(sqrt(kq1)))
                da_s2 = '$AM = %s$' %(latex(sqrt(kq2)))
                da_s3 = '$AM = %s$' %(latex(sqrt(kq3)))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('\\begin{center} \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                        '\\draw (0,0) node[below left]{$B$}; \n'
                        '\\draw (3,4) node[above left]{$A$}; \n'
                        '\\draw (6,0) node[below right]{$C$}; \n'
                        '\\draw (4,0) node[below right]{$M$}; \n'
                        '\\coordinate (B) at (0,0); \n'
                        '\\coordinate (A) at (3,4); \n'
                        '\\coordinate (C) at (6,0); \n'
                        '\\coordinate (M) at (4,0); \n'
                        '\\draw[name path=AB] (A)--(B) --(C) -- (A) -- (M);  \n'
                        '\\end{tikzpicture} \n'
                        '\\end{center} \n'
                        'Ta có \\\\ \n'
                        '$\\cos B = \\dfrac{c^2+a^2-b^2}{2ca} = \\dfrac{AB^2+BC^2-CA^2}{2AB \\cdot BC} = \\dfrac{%s^2+%s^2-%s^2}{2 \\cdot %s \\cdot %s} =%s$. \\\\ \n'
                        'Áp dụng định lí cosin cho tam giác $ABM$, ta có\\\\ \n'
                        '$AM^2 = AB^2 +BM^2 -2AB \\cdot BM \\cos B = %s^2 +%s^2 -2 \\cdot %s \\cdot %s \\cdot %s = %s$. \\\\ \n'
                        'Vậy $AM = %s$.'
                        %(latex(c),latex(a),latex(b),latex(c),latex(a), latex(Rational(c**2+a**2-b**2,2*c*a)), #cosB
                        latex(c),latex(bm),latex(c),latex(bm),latex(Rational(c**2+a**2-b**2,2*c*a)),latex(kq),latex(sqrt(kq))
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.00','').replace('\\frac','\\dfrac').replace('{,}0','')
            return content

