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


def bt_dang20_p4_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Cố định tên điểm theo chuẩn mẫu (không random điểm)
        diem_A, diem_B = "A", "B"
        
        # Random bộ 3 Pytago cho vận tốc (vn, v, vp)
        bo_van_toc = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)]
        v_n, v_thuc, v_p = random.choice(bo_van_toc)
        
        # Random chiều rộng sông AB sao cho chia hết cho v_thuc để thời gian t nguyên
        t_giay = randint(5, 25) * 10
        chieu_rong_AB = v_thuc * t_giay
    
        # Hình vẽ TikZ biểu diễn các vectơ vận tốc (nét 1pt, điểm 1pt, màu black)
        hinh_ve = ('\\begin{center}\n'
                   '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                   '\\coordinate (A) at (0,0);\n'
                   '\\coordinate (B) at (0,3);\n'
                   '\\coordinate (C) at (-2.25,3);\n'
                   '\\coordinate (D) at (2.25,3);\n'
                   '\\draw[line width=1pt] (-3.5,0)--(3.5,0) (-3.5,3)--(3.5,3);\n'
                   '\\draw[line width=1pt, dashed] (C)--(B) (A)--(D);\n'
                   '\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);\n'
                   '\\draw[line width=1pt, ->] (A)--(B) node[midway, right] {$\\overrightarrow{v}$};\n'
                   '\\draw[line width=1pt, ->] (A)--(C) node[midway, below left] {$\\overrightarrow{v_p}$};\n'
                   '\\draw[line width=1pt, ->] (C)--(B) node[midway, above] {$\\overrightarrow{v_n}$};\n'
                   '\\fill (A) circle (1pt) node[below] {$A$};\n'
                   '\\fill (B) circle (1pt) node[above] {$B$};\n'
                   '\\end{tikzpicture}\n'
                   '\\end{center}\n')
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Một chiếc phà muốn sang ngang một con sông rộng $%s\\,\\mathrm{m}$ theo hướng vuông góc với bờ sông (từ $%s$ đến $%s$). Vận tốc của dòng nước chảy xuôi theo bờ là $v_n = %s\\,\\mathrm{m/s}$. Người lái phà hướng mũi phà chếch ngược dòng nước để phà đi thẳng từ $%s$ đến $%s$ với vận tốc thực tế $v = %s\\,\\mathrm{m/s}$. Hãy biểu diễn các vectơ vận tốc và tính độ lớn vận tốc của phà so với nước ($v_p$) cũng như thời gian phà qua sông.'
                         %(str(chieu_rong_AB), diem_A, diem_B, str(v_n), diem_A, diem_B, str(v_thuc)))
        
        # Nội dung lời giải
        loigiai = ('%s'
                   '\\begin{itemize} \n'
                   '\\item Theo quy tắc cộng vận tốc, vectơ vận tốc thực tế $\\overrightarrow{v}$ (vuông góc bờ sông) là cạnh góc vuông, vectơ vận tốc dòng nước $\\overrightarrow{v_n}$ (dọc bờ sông) là cạnh góc vuông còn lại, và vectơ vận tốc phà so với nước $\\overrightarrow{v_p}$ là cạnh huyền của tam giác vuông vận tốc. \n'
                   '\\item Độ lớn vận tốc phà so với nước: $v_p = \\sqrt{v^2 + v_n^2} = \\sqrt{%s^2 + %s^2} = %s\\,\\mathrm{m/s}$. \n'
                   '\\item Thời gian phà qua sông: $t = \\dfrac{%s %s}{v} = \\dfrac{%s}{%s} = %s$ giây. \n'
                   '\\end{itemize}'
                   %(hinh_ve,
                     str(v_thuc), str(v_n), str(v_p),
                     diem_A, diem_B, str(chieu_rong_AB), str(v_thuc), str(t_giay)))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\loigiai{ \n' +str(loigiai)+'\n}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

