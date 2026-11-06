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


def bt_dang11_p1_b2_c1_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12']
            dang=random.choice(lisdang)
            if dang=='1':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(%s;%s;0)$'%(latex(x1),latex(y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(-x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(-x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ nhất của mặt phẳng $(Oxy)$, khoảng cách từ $%s$ đến $Ox$ và $Oy$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ nhất của mặt phẳng tọa độ $(Oxy)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{-2} \\def\\xmax{%s}\n'
                            '\\def\\ymin{-2} \\def\\ymax{%s}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below right]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [right] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin,0)--(\\xmax+1,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin)--(0,\\ymax+1) node [left]{$y$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin,\\ymin) rectangle (\\xmax+1,\\ymax+1);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{i}+%s\\overrightarrow{j}$ suy ra $%s(%s;%s;0)$.'

                        %(d,latex(x1),latex(y1),latex(x1),latex(y1),d,latex(x1),latex(y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(x1),latex(y1),d,latex(x1),latex(y1)

                            ))
            if dang=='2':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(%s;%s;0)$'%(latex(-x1),latex(y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(-x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ hai của mặt phẳng $(Oxy)$, khoảng cách từ $%s$ đến $Ox$ và $Oy$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ hai của mặt phẳng tọa độ $(Oxy)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{%s} \\def\\xmax{2}\n'
                            '\\def\\ymin{-2} \\def\\ymax{%s}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below left]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [left] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin-1,0)--(\\xmax,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin)--(0,\\ymax+1) node [left]{$y$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin-1,\\ymin) rectangle (\\xmax,\\ymax+1);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{i}+%s\\overrightarrow{j}$ suy ra $%s(%s;%s;0)$.\n'

                        %(d,latex(-x1),latex(y1),latex(-x1),latex(y1),d,latex(-x1),latex(y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(-x1),latex(y1),d,latex(-x1),latex(y1)

                            ))
            if dang=='3':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(%s;%s;0)$'%(latex(-x1),latex(-y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(-x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ ba của mặt phẳng $(Oxy)$, khoảng cách từ $%s$ đến $Ox$ và $Oy$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ ba của mặt phẳng tọa độ $(Oxy)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{%s} \\def\\xmax{2}\n'
                            '\\def\\ymin{%s} \\def\\ymax{2}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below right]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [left] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin-1,0)--(\\xmax,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin-1)--(0,\\ymax) node [left]{$y$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin-1,\\ymin-1) rectangle (\\xmax,\\ymax);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{i}+%s\\overrightarrow{j}$ suy ra $%s(%s;%s;0)$.\n'

                        %(d,latex(-x1),latex(-y1),latex(-x1),latex(-y1),d,latex(-x1),latex(-y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(-x1),latex(-y1),d,latex(-x1),latex(-y1)

                            ))
            if dang=='4':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(%s;%s;0)$'%(latex(x1),latex(-y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(-x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(-x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ tư của mặt phẳng $(Oxy)$, khoảng cách từ $%s$ đến $Ox$ và $Oy$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ tứ của mặt phẳng tọa độ $(Oxy)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{-2} \\def\\xmax{%s}\n'
                            '\\def\\ymin{%s} \\def\\ymax{2}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below right]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [right] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin,0)--(\\xmax+1,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin-1)--(0,\\ymax) node [left]{$y$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin,\\ymin-1) rectangle (\\xmax+1,\\ymax);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{i}+%s\\overrightarrow{j}$ suy ra $%s(%s;%s;0)$.\n'

                        %(d,latex(x1),latex(-y1),latex(x1),latex(-y1),d,latex(x1),latex(-y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(x1),latex(-y1),d,latex(x1),latex(-y1)

                            ))
            if dang=='5':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(%s;0;%s)$'%(latex(x1),latex(y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(-x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(-x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ nhất của mặt phẳng $(Oxz)$, khoảng cách từ $%s$ đến $Ox$ và $Oz$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ nhất của mặt phẳng tọa độ $(Oxz)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{-2} \\def\\xmax{%s}\n'
                            '\\def\\ymin{-2} \\def\\ymax{%s}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below right]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [right] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin,0)--(\\xmax+1,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin)--(0,\\ymax+1) node [left]{$z$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin,\\ymin) rectangle (\\xmax+1,\\ymax+1);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{i}+%s\\overrightarrow{k}$ suy ra $%s(%s;0;%s)$.'

                        %(d,latex(x1),latex(y1),latex(x1),latex(y1),d,latex(x1),latex(y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(x1),latex(y1),d,latex(x1),latex(y1)

                            ))
            if dang=='6':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(%s;0;%s)$'%(latex(-x1),latex(y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(-x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ hai của mặt phẳng $(Oxz)$, khoảng cách từ $%s$ đến $Ox$ và $Oz$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ hai của mặt phẳng tọa độ $(Oxz)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{%s} \\def\\xmax{2}\n'
                            '\\def\\ymin{-2} \\def\\ymax{%s}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below left]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [left] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin-1,0)--(\\xmax,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin)--(0,\\ymax+1) node [left]{$z$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin-1,\\ymin) rectangle (\\xmax,\\ymax+1);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{i}+%s\\overrightarrow{k}$ suy ra $%s(%s;0;%s)$.\n'

                        %(d,latex(-x1),latex(y1),latex(-x1),latex(y1),d,latex(-x1),latex(y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(-x1),latex(y1),d,latex(-x1),latex(y1)

                            ))
            if dang=='7':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(%s;0;%s)$'%(latex(-x1),latex(-y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(-x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ ba của mặt phẳng $(Oxz)$, khoảng cách từ $%s$ đến $Ox$ và $Oz$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ ba của mặt phẳng tọa độ $(Oxz)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{%s} \\def\\xmax{2}\n'
                            '\\def\\ymin{%s} \\def\\ymax{2}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below right]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [left] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin-1,0)--(\\xmax,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin-1)--(0,\\ymax) node [left]{$z$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin-1,\\ymin-1) rectangle (\\xmax,\\ymax);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{i}+%s\\overrightarrow{k}$ suy ra $%s(%s;0;%s)$.\n'

                        %(d,latex(-x1),latex(-y1),latex(-x1),latex(-y1),d,latex(-x1),latex(-y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(-x1),latex(-y1),d,latex(-x1),latex(-y1)

                            ))
            if dang=='8':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(%s;0;%s)$'%(latex(x1),latex(-y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(-x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(-x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ tư của mặt phẳng $(Oxz)$, khoảng cách từ $%s$ đến $Ox$ và $Oz$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ tứ của mặt phẳng tọa độ $(Oxz)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{-2} \\def\\xmax{%s}\n'
                            '\\def\\ymin{%s} \\def\\ymax{2}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below right]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [right] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin,0)--(\\xmax+1,0) node [below]{$x$};\n'
                            '\\draw[->] (0,\\ymin-1)--(0,\\ymax) node [left]{$z$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin,\\ymin-1) rectangle (\\xmax+1,\\ymax);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{i}+%s\\overrightarrow{k}$ suy ra $%s(%s;0;%s)$.\n'

                        %(d,latex(x1),latex(-y1),latex(x1),latex(-y1),d,latex(x1),latex(-y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(x1),latex(-y1),d,latex(x1),latex(-y1)

                            ))
            if dang=='9':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(0;%s;%s)$'%(latex(x1),latex(y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(-x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(-x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ nhất của mặt phẳng $(Oyz)$, khoảng cách từ $%s$ đến $Oy$ và $Oz$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ nhất của mặt phẳng tọa độ $(Oyz)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{-2} \\def\\xmax{%s}\n'
                            '\\def\\ymin{-2} \\def\\ymax{%s}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below right]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [right] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin,0)--(\\xmax+1,0) node [below]{$y$};\n'
                            '\\draw[->] (0,\\ymin)--(0,\\ymax+1) node [left]{$z$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin,\\ymin) rectangle (\\xmax+1,\\ymax+1);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{j}+%s\\overrightarrow{k}$ suy ra $%s(0;%s;%s)$.'

                        %(d,latex(x1),latex(y1),latex(x1),latex(y1),d,latex(x1),latex(y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(x1),latex(y1),d,latex(x1),latex(y1)

                            ))
            if dang=='10':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(0;%s;%s)$'%(latex(-x1),latex(y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(-x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ hai của mặt phẳng $(Oyz)$, khoảng cách từ $%s$ đến $Oy$ và $Oz$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ hai của mặt phẳng tọa độ $(Oyz)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{%s} \\def\\xmax{2}\n'
                            '\\def\\ymin{-2} \\def\\ymax{%s}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below left]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [left] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin-1,0)--(\\xmax,0) node [below]{$y$};\n'
                            '\\draw[->] (0,\\ymin)--(0,\\ymax+1) node [left]{$z$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin-1,\\ymin) rectangle (\\xmax,\\ymax+1);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{j}+%s\\overrightarrow{k}$ suy ra $%s(0;%s;%s)$.'

                        %(d,latex(-x1),latex(y1),latex(-x1),latex(y1),d,latex(-x1),latex(y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(-x1),latex(y1),d,latex(-x1),latex(y1)

                            ))
            if dang=='11':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(0;%s;%s)$'%(latex(-x1),latex(-y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(-x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ ba của mặt phẳng $(Oyz)$, khoảng cách từ $%s$ đến $Oy$ và $Oz$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ ba của mặt phẳng tọa độ $(Oyz)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{%s} \\def\\xmax{2}\n'
                            '\\def\\ymin{%s} \\def\\ymax{2}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below right]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [left] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin-1,0)--(\\xmax,0) node [below]{$y$};\n'
                            '\\draw[->] (0,\\ymin-1)--(0,\\ymax) node [left]{$z$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin-1,\\ymin-1) rectangle (\\xmax,\\ymax);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{j}+%s\\overrightarrow{k}$ suy ra $%s(0;%s;%s)$.'

                        %(d,latex(-x1),latex(-y1),latex(-x1),latex(-y1),d,latex(-x1),latex(-y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(-x1),latex(-y1),d,latex(-x1),latex(-y1)

                            ))
            if dang=='12':
                x1 = randint(1,10)
                y1 = randint(1,10)
                lis = ['A','B','C','D','E','F','G','H','I','K']
                d = random.choice(lis)
                du = ['$(0;%s;%s)$'%(latex(x1),latex(-y1))]

                da= random.choice(du)
                s = [ '$(%s;%s;0)$'%(latex(-x1),latex(y1)),
                    '$(%s;%s;0)$'%(latex(-x1),latex(-y1)),
                    '$(%s;%s;0)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(y1)),
                    '$(0;%s;%s)$'%(latex(-x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(y1)),
                    '$(%s;0;%s)$'%(latex(x1),latex(-y1)),
                    '$(%s;0;%s)$'%(latex(-x1),latex(-y1)),

                            ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = '''Trong không gian $Oxyz$, cho điểm $%s$ nằm trong góc phần tư thứ tư của mặt phẳng $(Oyz)$, khoảng cách từ $%s$ đến $Oy$ và $Oz$ lần lượt là $%s$ và $%s$. Toạ độ của điểm $%s$ là \n''' %(d,d,latex(y1),latex(x1),d)    
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Vì điểm $%s$ nằm trong góc phần tư thứ tứ của mặt phẳng tọa độ $(Oyz)$ ta có hình vẽ \\\\ \n'
                            '\\begin{center}\n'
                            '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
                            '\\def\\xmin{-2} \\def\\xmax{%s}\n'
                            '\\def\\ymin{%s} \\def\\ymax{2}\n'
                            '\\path \n'
                            '(%s,%s) coordinate (%s)\n'
                            '(%s,0) coordinate (L)\n'
                            '(0,%s) coordinate (M)\n'
                            '($(%s)!0.5!(M)$) node[above]{$%s$}\n'
                            '($(%s)!0.5!(L)$) node[below right]{$%s$};\n'
                            '\\draw (%s)--(L);\n'
                            '\\draw (%s)--(M);\n'
                            '\\draw [fill=black](%s)circle(1.5pt) node [right] {$%s$};\n'
                            '\\draw[color=gray!50,dashed] (\\xmin,\\ymin) grid (\\xmax,\\ymax);\n'
                            '\\draw[->] (\\xmin,0)--(\\xmax+1,0) node [below]{$y$};\n'
                            '\\draw[->] (0,\\ymin-1)--(0,\\ymax) node [left]{$z$};\n'
                            '\\node at (0,0) [below left]{$O$};\n'
                            '\\clip (\\xmin,\\ymin-1) rectangle (\\xmax+1,\\ymax);\n'
                        '\\end{tikzpicture}\n'
                        '\\end{center}\n'
                        'Dễ thấy $\\overrightarrow{O%s}=%s\\overrightarrow{j}+%s\\overrightarrow{k}$ suy ra $%s(0;%s;%s)$.'

                        %(d,latex(x1),latex(-y1),latex(x1),latex(-y1),d,latex(x1),latex(-y1),d,latex(x1),d,latex(y1),d,d,d,d,d,latex(x1),latex(-y1),d,latex(x1),latex(-y1)

                            ))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-')
            return content

