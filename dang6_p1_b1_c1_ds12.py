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


def bt_dang6_p1_b1_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='1':
                #Khai báo biến
                x=symbols('x')
                a=randint(-1,1)
                b=randint(-1,1)
                hs=(x+a)**3-3*(x+a)**2+(2+b)
                x1=-a
                x2=2-a
                y1=(x1+a)**3-3*(x1+a)**2+(2+b)
                y2=(x2+a)**3-3*(x2+a)**2+(2+b)
                #Các đáp án trắc nghiệm
                du = ['$(%s;%s)$'%(latex(x1),latex(x2)),
                      ]
                da= random.choice(du)
                s = ['$(-\\infty;%s)$'%(latex(x1)),
                     '$(%s;+\\infty)$'%(latex(x2)),
                     '$(-\\infty;%s)$'%(latex(x2)),
                     '$(%s;+\\infty)$'%(latex(x1)),
                     '$(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                if a==0:
                    noidungcauhoi = ('''\\immini{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số nghịch biến trên khoảng nào dưới đây?}{
                             		\\scalebox{0.7}{ 
                                    \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]
                                 		\\tikzset{every node/.style={scale=0.9}}
                                 		\\draw[->] (%s,0)--(%s,0) node[below left] {$x$};
                                 		\\draw[->] (0,%s)--(0,%s) node[below left] {$y$};
                                 		\\draw (0,0) node [below left] {$O$};
                                 		\\foreach \\x/\\nx in {%s/%s}
                                 		\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$};
                                 		\\foreach \\y/\\ny in {%s/%s,%s/%s}
                                 		\\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {$\\ny$};
                                 		\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);
                                 		\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);
                                 		\\begin{scope}
                                 			\\clip (%s,%s) rectangle (%s,%s);
                                 			\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{1*((\\x+%s)^3)+-3*((\\x+%s)^2)+0*(\\x)+2+%s});
                                 		\\end{scope}
                                 	\\end{tikzpicture}}}'''                 
                                     %(latex(x1-2),latex(x2+2),
                                       latex(y2-1),latex(y1+1),
                                       latex(x2),latex(x2),
                                       latex(y1),latex(y1),latex(y2),latex(y2),
                                       latex(x2),latex(x2),latex(y2),latex(y2),
                                       latex(x1),latex(x1),latex(y1),latex(y1),
                                       latex(x1-2),latex(y2-1),latex(x2+2),latex(y1+1),
                                       latex(a),latex(a),latex(b)
                                         ))  
                else:
                    # Nội dung câu hỏi
                    noidungcauhoi = ('''\\immini{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số nghịch biến trên khoảng nào dưới đây?}{
                             		\\scalebox{0.7}{ 
                                    \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]
                                 		\\tikzset{every node/.style={scale=0.9}}
                                 		\\draw[->] (%s,0)--(%s,0) node[below left] {$x$};
                                 		\\draw[->] (0,%s)--(0,%s) node[below left] {$y$};
                                 		\\draw (0,0) node [below left] {$O$};
                                 		\\foreach \\x/\\nx in {%s/%s,%s/%s}
                                 		\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$};
                                 		\\foreach \\y/\\ny in {%s/%s,%s/%s}
                                 		\\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {$\\ny$};
                                 		\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);
                                 		\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);
                                 		\\begin{scope}
                                 			\\clip (%s,%s) rectangle (%s,%s);
                                 			\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{1*((\\x+%s)^3)+-3*((\\x+%s)^2)+0*(\\x)+2+%s});
                                 		\\end{scope}
                                 	\\end{tikzpicture}}}'''                 
                                     %(latex(x1-2),latex(x2+2),
                                       latex(y2-1),latex(y1+1),
                                       latex(x1),latex(x1),latex(x2),latex(x2),
                                       latex(y1),latex(y1),latex(y2),latex(y2),
                                       latex(x2),latex(x2),latex(y2),latex(y2),
                                       latex(x1),latex(x1),latex(y1),latex(y1),
                                       latex(x1-2),latex(y2-1),latex(x2+2),latex(y1+1),
                                       latex(a),latex(a),latex(b)
                                         ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Từ đồ thị ta thấy hàm số nghịch biến trên khoảng $(%s;%s)$.'''

                         %(latex(x1),latex(x2)
                         ))

            if dang=='2':
                #Khai báo biến
                x=symbols('x')
                a=randint(-1,1)
                b=randint(-1,1)
                hs=(x+a)**3-3*(x+a)**2+(2+b)
                x1=-a
                x2=2-a
                y1=(x1+a)**3-3*(x1+a)**2+(2+b)
                y2=(x2+a)**3-3*(x2+a)**2+(2+b)
                #Các đáp án trắc nghiệm
                du = ['$(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2)),
                      ]
                da= random.choice(du)
                s = [
                     '$(-\\infty;%s)$'%(latex(x2)),
                     '$(%s;+\\infty)$'%(latex(x1)),
                     '$(%s;%s)$'%(latex(x1),latex(x2)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                if a==0:
                    noidungcauhoi = ('''\\immini{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số đồng biến trên khoảng nào dưới đây?}{
                             		\\scalebox{0.7}{ 
                                    \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]
                                 		\\tikzset{every node/.style={scale=0.9}}
                                 		\\draw[->] (%s,0)--(%s,0) node[below left] {$x$};
                                 		\\draw[->] (0,%s)--(0,%s) node[below left] {$y$};
                                 		\\draw (0,0) node [below left] {$O$};
                                 		\\foreach \\x/\\nx in {%s/%s}
                                 		\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$};
                                 		\\foreach \\y/\\ny in {%s/%s,%s/%s}
                                 		\\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {$\\ny$};
                                 		\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);
                                 		\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);
                                 		\\begin{scope}
                                 			\\clip (%s,%s) rectangle (%s,%s);
                                 			\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{1*((\\x+%s)^3)+-3*((\\x+%s)^2)+0*(\\x)+2+%s});
                                 		\\end{scope}
                                 	\\end{tikzpicture}}}'''                 
                                     %(latex(x1-2),latex(x2+2),
                                       latex(y2-1),latex(y1+1),
                                       latex(x2),latex(x2),
                                       latex(y1),latex(y1),latex(y2),latex(y2),
                                       latex(x2),latex(x2),latex(y2),latex(y2),
                                       latex(x1),latex(x1),latex(y1),latex(y1),
                                       latex(x1-2),latex(y2-1),latex(x2+2),latex(y1+1),
                                       latex(a),latex(a),latex(b)
                                         ))  
                else:
                    # Nội dung câu hỏi
                    noidungcauhoi = ('''\\immini{Cho hàm số $y=f(x)$ có đồ thị như hình vẽ bên. Hàm số đồng biến trên khoảng nào dưới đây?}{
                             		\\scalebox{0.7}{ 
                                    \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]
                                 		\\tikzset{every node/.style={scale=0.9}}
                                 		\\draw[->] (%s,0)--(%s,0) node[below left] {$x$};
                                 		\\draw[->] (0,%s)--(0,%s) node[below left] {$y$};
                                 		\\draw (0,0) node [below left] {$O$};
                                 		\\foreach \\x/\\nx in {%s/%s,%s/%s}
                                 		\\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$};
                                 		\\foreach \\y/\\ny in {%s/%s,%s/%s}
                                 		\\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {$\\ny$};
                                 		\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);
                                 		\\draw[dashed,thin](%s,0)--(%s,%s)--(0,%s);
                                 		\\begin{scope}
                                 			\\clip (%s,%s) rectangle (%s,%s);
                                 			\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{1*((\\x+%s)^3)+-3*((\\x+%s)^2)+0*(\\x)+2+%s});
                                 		\\end{scope}
                                 	\\end{tikzpicture}}}'''                 
                                     %(latex(x1-2),latex(x2+2),
                                       latex(y2-1),latex(y1+1),
                                       latex(x1),latex(x1),latex(x2),latex(x2),
                                       latex(y1),latex(y1),latex(y2),latex(y2),
                                       latex(x2),latex(x2),latex(y2),latex(y2),
                                       latex(x1),latex(x1),latex(y1),latex(y1),
                                       latex(x1-2),latex(y2-1),latex(x2+2),latex(y1+1),
                                       latex(a),latex(a),latex(b)
                                         ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Từ đồ thị ta thấy hàm số nghịch biến trên khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$.'''          
                         %(latex(x1),latex(x2)
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

