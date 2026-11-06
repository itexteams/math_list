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


def bt_dang10_p1_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                #Khai báo biến
                A=["A","B","C"]
                B=["B","C","A"]
                C=["C","A","B"]
                A1=["A'","B'","C'"]
                B1=["B'","C'","A'"]
                C1=["C'","A'","B'"]
                #Chọn ngẫu nhiên vị trí
                i = random.randint(0,2)
                A, B, C, A1, B1, C1 = A[i], B[i], C[i], A1[i], B1[i], C1[i]
                # Xuất ra mã TikZ
                tikz_code = f'''\\begin{{center}}
                \\scalebox{{0.7}}{{\\begin{{tikzpicture}}[scale=1, line join=round, line cap=round,>=stealth,thick]
                    \\coordinate ({A}) at (0,0)   node at ({A}) [left] {{${A}$}}; 
                    \\coordinate ({B}) at (2,-1) node at ({B}) [below] {{${B}$}}; 
                    \\coordinate ({C}) at (4,0)  node at ({C}) [below] {{${C}$}}; 
                    \\coordinate ({A1}) at (1,4)   node at ({A1}) [above] {{${A1}$}}; 
                    \\coordinate ({B1}) at (3,3)   node at ({B1}) [above] {{${B1}$}}; 
                    \\coordinate ({C1}) at (5,4)   node at ({C1}) [above] {{${C1}$}};
                    \\draw [dashed] ({A})--({C}); 
                    \\draw ({A})--({B})--({B1})--({A1})--({A}); 
                    \\draw ({B1})--({C1})--({C})--({B}) ({A1})--({C1})--({C}); 
                \\end{{tikzpicture}}}}
                \\end{{center}}'''

                kq = ['%s'%(f'$\\overrightarrow{{{B}{A}}} + \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{B}{C}}}$'),
                    '%s'%(f'$\\overrightarrow{{{A1}{C1}}} + \\overrightarrow{{{B}{A}}} = \\overrightarrow{{{B}{C}}}$'),
                    '%s'%(f'$\\overrightarrow{{{A}{A1}}} + \\overrightarrow{{{B1}{C1}}} = \\overrightarrow{{{B}{C1}}}$')
                    ]
                lg = ['%s'%(f'$\\overrightarrow{{{B}{A}}} + \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{B}{A}}} + \\overrightarrow{{{A}{C}}} = \\overrightarrow{{{B}{C}}}$.'),
                    '%s'%(f'$\\overrightarrow{{{A1}{C1}}} + \\overrightarrow{{{B}{A}}} = \\overrightarrow{{{A}{C}}} + \\overrightarrow{{{B}{A}}} =\\overrightarrow{{{B}{C}}}$.'),
                    '%s'%(f'$\\overrightarrow{{{A}{A1}}} + \\overrightarrow{{{B1}{C1}}} = \\overrightarrow{{{B}{B1}}} + \\overrightarrow{{{B1}{C1}}} =\\overrightarrow{{{B}{C1}}}$.')
                ]
                k = random.randint(0,2)
                da = kq[k]
                loigiai=lg[k]
                #Các đáp án trắc nghiệm
                s = ['%s'%(f'$\\overrightarrow{{{B}{A}}} + \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{C1}{B1}}}$'),
                    '%s'%(f'$\\overrightarrow{{{B}{A}}} + \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{A1}{A}}}$'),
                    '%s'%(f'$\\overrightarrow{{{B}{A}}} + \\overrightarrow{{{A1}{C1}}} = \\overrightarrow{{{B}{C1}}}$'),
                    '%s'%(f'$\\overrightarrow{{{A}{A1}}} + \\overrightarrow{{{B1}{C1}}} = \\overrightarrow{{{A}{C1}}}$'),
                    '%s'%(f'$\\overrightarrow{{{A1}{C1}}} + \\overrightarrow{{{B}{A}}} = \\overrightarrow{{{A1}{A}}}$')
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi=f"""Cho hình lăng trụ ${A}{B}{C}.{A1}{B1}{C1}$ (xem hình dưới). 
                {tikz_code}
                Phát biểu nào sau đây đúng?"""
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

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

