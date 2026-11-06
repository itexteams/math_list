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


def bt_dang8_p1_b1_c2_hh10(self):
            # Khai báo biến
            d = ['$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CB} $',
                ]
            da= random.choice(d)
            s = ['$\\overrightarrow{BP},\\overrightarrow{PN},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CB} $',
                '$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{NB},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CB} $',
                '$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{PM},\\overrightarrow{CP},\\overrightarrow{CB} $',
                '$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CM} $',
                '$\\overrightarrow{BA},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CB} $',
                '$\\overrightarrow{BP},\\overrightarrow{PM},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CB} $',
                '$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BN},\\overrightarrow{NM},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CB} $',
                '$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{AB},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CB} $',
                '$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{MP},\\overrightarrow{CP},\\overrightarrow{CB} $',
                '$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{PB},\\overrightarrow{CA},\\overrightarrow{CB} $',
                '$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CM} $',
                ]
            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            dz1 = ['$\\overrightarrow{AN},\\overrightarrow{NC},\\overrightarrow{AC},\\overrightarrow{NA},\\overrightarrow{CN},\\overrightarrow{CA},\\overrightarrow{MP} $',
                ]
            daz1= random.choice(dz1)
            sz1 = ['$\\overrightarrow{AP},\\overrightarrow{NC},\\overrightarrow{AC},\\overrightarrow{NA},\\overrightarrow{CN},\\overrightarrow{CA},\\overrightarrow{MP} $',
                '$\\overrightarrow{AN},\\overrightarrow{NP},\\overrightarrow{AC},\\overrightarrow{NA},\\overrightarrow{CN},\\overrightarrow{CA},\\overrightarrow{MP} $',
                '$\\overrightarrow{AN},\\overrightarrow{NC},\\overrightarrow{AB},\\overrightarrow{NA},\\overrightarrow{CN},\\overrightarrow{CA},\\overrightarrow{MP} $',
                '$\\overrightarrow{AN},\\overrightarrow{NC},\\overrightarrow{AC},\\overrightarrow{NM},\\overrightarrow{CN},\\overrightarrow{CA},\\overrightarrow{MP} $',
                '$\\overrightarrow{AN},\\overrightarrow{NC},\\overrightarrow{AC},\\overrightarrow{NA},\\overrightarrow{CM},\\overrightarrow{CA},\\overrightarrow{MP} $',
                '$\\overrightarrow{AN},\\overrightarrow{NC},\\overrightarrow{AC},\\overrightarrow{NA},\\overrightarrow{CN},\\overrightarrow{CP},\\overrightarrow{MP} $',
                '$\\overrightarrow{AN},\\overrightarrow{NC},\\overrightarrow{AC},\\overrightarrow{NA},\\overrightarrow{CN},\\overrightarrow{CA},\\overrightarrow{MB} $',
                ]
            das1z1 = random.choice(sz1)
            sz1.remove(das1z1)
            das2z1 = random.choice(sz1)
            sz1.remove(das2z1)
            das3z1 = random.choice(sz1)

            dz2 = ['$\\overrightarrow{AM},\\overrightarrow{MB},\\overrightarrow{AB},\\overrightarrow{MA},\\overrightarrow{BM},\\overrightarrow{BA},\\overrightarrow{PN} $',
                ]
            daz2= random.choice(dz2)
            sz2 = ['$\\overrightarrow{AC},\\overrightarrow{MB},\\overrightarrow{AB},\\overrightarrow{MA},\\overrightarrow{BM},\\overrightarrow{BA},\\overrightarrow{PN} $',
                '$\\overrightarrow{AM},\\overrightarrow{MP},\\overrightarrow{AB},\\overrightarrow{MA},\\overrightarrow{BM},\\overrightarrow{BA},\\overrightarrow{PN} $',
                '$\\overrightarrow{AM},\\overrightarrow{MB},\\overrightarrow{AN},\\overrightarrow{MA},\\overrightarrow{BM},\\overrightarrow{BA},\\overrightarrow{PN} $',
                '$\\overrightarrow{AM},\\overrightarrow{MB},\\overrightarrow{AB},\\overrightarrow{MN},\\overrightarrow{BM},\\overrightarrow{BA},\\overrightarrow{PN} $',
                '$\\overrightarrow{AM},\\overrightarrow{MB},\\overrightarrow{AB},\\overrightarrow{MA},\\overrightarrow{BP},\\overrightarrow{BA},\\overrightarrow{PN} $',
                '$\\overrightarrow{AM},\\overrightarrow{MB},\\overrightarrow{AB},\\overrightarrow{MA},\\overrightarrow{BM},\\overrightarrow{BN},\\overrightarrow{PN} $',
                '$\\overrightarrow{AM},\\overrightarrow{MB},\\overrightarrow{AB},\\overrightarrow{MA},\\overrightarrow{BM},\\overrightarrow{BA},\\overrightarrow{PM} $',
                ]
            das1z2 = random.choice(sz2)
            sz2.remove(das1z2)
            das2z2 = random.choice(sz2)
            sz2.remove(das2z2)
            das3z2 = random.choice(sz2)

            lisdang=['3']
            dang=random.choice(lisdang)
            if dang=='3':
                # Câu hỏi
                noidungcauhoi='''Cho tam giác $ABC$, các điểm $M, N, P$ lần lượt là trung điểm của $AB, AC$ và $BC$. Các vectơ phân biệt khác $\\overrightarrow{0}$ cùng phương với vectơ $\\overrightarrow{NP}$ là \n'''
                # Các đáp án
                da_d = ('\\True ' +str(daz2))
                da_s1 = str(das1z2)
                da_s2 = str(das2z2) 
                da_s3 = str(das3z2) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.9]    \n'
                                '\\draw (0,0) node[below left]{$A$};    \n'
                                '\\draw (2,4) node[above ]{$B$};    \n'
                                '\\draw (6,0) node[above right]{$C$};    \n'
                                '\\draw (1,2) node[above left]{$M$};   \n'
                                '\\draw (3,0) node[below ]{$N$};    \n'
                                '\\draw (4,2) node[above right]{$P$};    \n'
                                '\\coordinate (A) at (0,0);     \n'
                                '\\coordinate (B) at (2,4);      \n'
                                '\\coordinate (C) at (6,0);     \n'
                                '\\coordinate (M) at (1,2);     \n'
                                '\\coordinate (N) at (3,0);     \n'
                                '\\coordinate (P) at (4,2);    \n'
                                '\\draw[] (A)--(B)--(C)--(A);      \n'
                                '\\draw[] (N)--(M);     \n'
                                '\\draw[] (P)--(M);   \n'
                                '\\draw[] (P)--(N);   \n'
                            '\\end{tikzpicture}   \n'
                        '\\end{center} \n'
                            'Các vectơ phân biệt với vectơ $\\overrightarrow{MN}$ là \\\\ \n'
                            '$\\overrightarrow{AM},\\overrightarrow{MB},\\overrightarrow{AB},\\overrightarrow{MA},\\overrightarrow{BM},\\overrightarrow{BA},\\overrightarrow{PN} $.'
                        )
            if dang=='2':
                # Câu hỏi
                noidungcauhoi='''Cho tam giác $ABC$, các điểm $M, N, P$ lần lượt là trung điểm của $AB, AC$ và $BC$. Các vectơ phân biệt khác $\\overrightarrow{0}$ cùng phương với vectơ $\\overrightarrow{MP}$ là \n'''
                # Các đáp án
                da_d = ('\\True ' +str(daz1))
                da_s1 = str(das1z1)
                da_s2 = str(das2z1) 
                da_s3 = str(das3z1) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.9]    \n'
                                '\\draw (0,0) node[below left]{$A$};    \n'
                                '\\draw (2,4) node[above ]{$B$};    \n'
                                '\\draw (6,0) node[above right]{$C$};    \n'
                                '\\draw (1,2) node[above left]{$M$};   \n'
                                '\\draw (3,0) node[below ]{$N$};    \n'
                                '\\draw (4,2) node[above right]{$P$};    \n'
                                '\\coordinate (A) at (0,0);     \n'
                                '\\coordinate (B) at (2,4);      \n'
                                '\\coordinate (C) at (6,0);     \n'
                                '\\coordinate (M) at (1,2);     \n'
                                '\\coordinate (N) at (3,0);     \n'
                                '\\coordinate (P) at (4,2);    \n'
                                '\\draw[] (A)--(B)--(C)--(A);      \n'
                                '\\draw[] (N)--(M);     \n'
                                '\\draw[] (P)--(M);   \n'
                                '\\draw[] (P)--(N);   \n'
                            '\\end{tikzpicture}   \n'
                        '\\end{center} \n'
                            'Các vectơ phân biệt cùng phương với vectơ $\\overrightarrow{MN}$ là \\\\ \n'
                            '$\\overrightarrow{AN},\\overrightarrow{NC},\\overrightarrow{AC},\\overrightarrow{NA},\\overrightarrow{CN},\\overrightarrow{CA},\\overrightarrow{MP} $.'
                        )
            if dang=='1':
                # Câu hỏi
                noidungcauhoi='''Cho tam giác $ABC$, các điểm $M, N, P$ lần lượt là trung điểm của $AB, AC$ và $BC$. Các vectơ phân biệt khác $\\overrightarrow{0}$ cùng phương với vectơ $\\overrightarrow{MN}$ là \n'''
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
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.9]    \n'
                                '\\draw (0,0) node[below left]{$A$};    \n'
                                '\\draw (2,4) node[above ]{$B$};    \n'
                                '\\draw (6,0) node[above right]{$C$};    \n'
                                '\\draw (1,2) node[above left]{$M$};   \n'
                                '\\draw (3,0) node[below ]{$N$};    \n'
                                '\\draw (4,2) node[above right]{$P$};    \n'
                                '\\coordinate (A) at (0,0);     \n'
                                '\\coordinate (B) at (2,4);      \n'
                                '\\coordinate (C) at (6,0);     \n'
                                '\\coordinate (M) at (1,2);     \n'
                                '\\coordinate (N) at (3,0);     \n'
                                '\\coordinate (P) at (4,2);    \n'
                                '\\draw[] (A)--(B)--(C)--(A);      \n'
                                '\\draw[] (N)--(M);     \n'
                                '\\draw[] (P)--(M);   \n'
                                '\\draw[] (P)--(N);   \n'
                            '\\end{tikzpicture}   \n'
                        '\\end{center} \n'
                            'Các vectơ phân biệt cùng phương với vectơ $\\overrightarrow{MN}$ là \\\\ \n'
                            '$\\overrightarrow{BP},\\overrightarrow{PC},\\overrightarrow{BC},\\overrightarrow{NM},\\overrightarrow{PB},\\overrightarrow{CP},\\overrightarrow{CB} $.'
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

