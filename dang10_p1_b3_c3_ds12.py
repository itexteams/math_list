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


def bt_dang10_p1_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                k=randint(1,9)
                x1=-1*k
                x2=1*k
                x3=3*k


                du = ['$S=-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    ]
                da= random.choice(du)
                s = ['$S=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    '$S=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    '$S=-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{R}$. Gọi $S$ là diện tích hình phẳng giới hạn bởi đồ thị hàm số và trục hoành như hình vẽ. Mệnh đề nào sau đây là đúng? \n'
                                '}{'
                                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                    '\\clip(-2.3638463541899375,-1.9904580889334818) rectangle (5.604787343266249,2.2329177707182986);  \n'
                                    '\\draw[line width=0.8pt,fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=-1.5707963267948966:4.71238898038469] plot(\\x,{-1*cos((\\x)*180/pi)}) -- (4.71238898038469,0.) -- (-1.5707963267948966,0.) -- cycle;  \n'
                                    '\\draw[line width=1.pt,smooth,samples=100,domain=-2.3638463541899375:5.604787343266249] plot(\\x,{-1*cos(((\\x))*180/pi)});  \n'
                                    '\\draw [->,line width=1.pt] (-2.456813747326928,0.) -- (5.591506287103821,0.);  \n'
                                    '\\draw [->,line width=1.pt] (0.,-2.) -- (0.,2.);  \n'
                                    '\\draw (-0.5443416599374418,0.5) node[anchor=north west] {$O$};  \n'
                                    '\\draw (5.0337019282818884,0) node[anchor=north west] {$x$};  \n'
                                    '\\draw (-0.47793637912530684,2.153231433743737) node[anchor=north west] {$y$};  \n'
                                    '\\draw (-2.2575979048905217,0) node[anchor=north west] {$%s$};  \n'
                                    '\\draw (1.461097820589032,0) node[anchor=north west] {$%s$};  \n'
                                    '\\draw (4,0) node[anchor=north west] {$%s$};  \n'
                                    '\\end{tikzpicture}  \n'
                                '}'
                                %(
                                latex(x1),latex(x2),latex(x3)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x) \\right|\\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x) \\right|\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$.'
                        %(latex(x1),latex(x2),latex(x2),latex(x3),latex(x1),latex(x2),latex(x2),latex(x3)
                        ))

            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                k=randint(1,9)
                x1=-1*k
                x2=1*k
                x3=3*k


                du = ['$S=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    ]
                da= random.choice(du)
                s = ['$S=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    '$S=-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    '$S=-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{R}$. Gọi $S$ là diện tích hình phẳng giới hạn bởi đồ thị hàm số và trục hoành như hình vẽ. Mệnh đề nào sau đây là đúng? \n'
                                '}{'
                                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                    '\\clip(-2.3638463541899375,-1.9904580889334818) rectangle (5.604787343266249,2.2329177707182986);  \n'
                                    '\\draw[line width=0.8pt,fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=-1.5707963267948966:4.71238898038469] plot(\\x,{cos((\\x)*180/pi)}) -- (4.71238898038469,0.) -- (-1.5707963267948966,0.) -- cycle;  \n'
                                    '\\draw[line width=1.pt,smooth,samples=100,domain=-2.3638463541899375:5.604787343266249] plot(\\x,{cos(((\\x))*180/pi)});  \n'
                                    '\\draw [->,line width=1.pt] (-2.456813747326928,0.) -- (5.591506287103821,0.);  \n'
                                    '\\draw [->,line width=1.pt] (0.,-2.) -- (0.,2.);  \n'
                                    '\\draw (-0.5443416599374418,0) node[anchor=north west] {$O$};  \n'
                                    '\\draw (5.0337019282818884,0) node[anchor=north west] {$x$};  \n'
                                    '\\draw (-0.47793637912530684,2.153231433743737) node[anchor=north west] {$y$};  \n'
                                    '\\draw (-2.2575979048905217,0.5) node[anchor=north west] {$%s$};  \n'
                                    '\\draw (1.461097820589032,0.5) node[anchor=north west] {$%s$};  \n'
                                    '\\draw (4,0.5) node[anchor=north west] {$%s$};  \n'
                                    '\\end{tikzpicture}  \n'
                                '}'
                                %(
                                latex(x1),latex(x2),latex(x3)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x) \\right|\\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x) \\right|\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$.'
                        %(latex(x1),latex(x2),latex(x2),latex(x3),latex(x1),latex(x2),latex(x2),latex(x3)
                        ))
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                k=randint(1,9)
                x1=-1*k
                x2=1*k
                x3=2*k


                du = ['$S=-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    ]
                da= random.choice(du)
                s = ['$S=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    '$S=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    '$S=-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{R}$. Gọi $S$ là diện tích hình phẳng giới hạn bởi các đường $y=f(x), y=0, x=%s$ và $x=%s$ như hình vẽ. Mệnh đề nào sau đây là đúng? \n'
                                '}{'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-3,-3) rectangle (5.3,2); \n'
                                '\\draw[line width=0.8pt,fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=-1.0:2.0] plot(\\x,{-1*(\\x+1.0)*(\\x-1.0)*(\\x-2.0)}) -- (2.,0.) -- (-1.,0.) -- cycle; \n'
                                '\\draw[line width=1.pt,smooth,samples=100,domain=-2:3] plot(\\x,{-1*((\\x)+1.0)*((\\x)-1.0)*((\\x)-2.0)}); \n'
                                '\\draw [->,line width=1.pt] (-2.011700886161612,0.) -- (3.0666286460874312,0.); \n'
                                '\\draw [->,line width=1.pt] (0,-3) -- (0,2); \n'
                                '\\draw (-2,0.6231112653441612) node[anchor=north west] {$%s$}; \n'
                                '\\draw (-0.6,0.5) node[anchor=north west] {$O$}; \n'
                                '\\draw (0.6,0.6121665896281072) node[anchor=north west] {$%s$}; \n'
                                '\\draw (2,0) node[anchor=north west] {$%s$}; \n'
                                '\\draw (2.7054543474576502,0.5) node[anchor=north west] {$x$}; \n'
                                '\\draw (-0.5,2) node[anchor=north west] {$y$}; \n'
                                '\\end{tikzpicture} \n'
                                '}'
                                %(latex(x1),latex(x3),
                                latex(x1),latex(x2),latex(x3)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x) \\right|\\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x) \\right|\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$.'
                        %(latex(x1),latex(x2),latex(x2),latex(x3),latex(x1),latex(x2),latex(x2),latex(x3)
                        ))

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                k=randint(1,9)
                x1=-1*k
                x2=1*k
                x3=2*k


                du = ['$S=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    ]
                da= random.choice(du)
                s = ['$S=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    '$S=-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    '$S=-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$'%(latex(x1),latex(x2),latex(x2),latex(x3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hàm số $y=f(x)$ liên tục trên $\\mathbb{R}$. Gọi $S$ là diện tích hình phẳng giới hạn bởi các đường $y=f(x), y=0, x=%s$ và $x=%s$ như hình vẽ. Mệnh đề nào sau đây là đúng? \n'
                                '}{'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                                '\\clip(-2,-1.3) rectangle (3.5,3);  \n'
                                '\\draw[line width=0.8pt,fill=black,pattern=north east lines,pattern color=black, smooth,samples=50,domain=-1.0:2.0] plot(\\x,{(\\x+1.0)*(\\x-1.0)*(\\x-2.0)}) -- (2.,0.) -- (-1.,0.) -- cycle;  \n'
                                '\\draw[line width=1.pt,smooth,samples=100,domain=-2:3] plot(\\x,{((\\x)+1.0)*((\\x)-1.0)*((\\x)-2.0)});  \n'
                                '\\draw [->,line width=1.pt] (-2.011700886161612,0.) -- (3.0666286460874312,0.);  \n'
                                '\\draw [->,line width=1.pt] (-0.008825230123735038,-1.3250410121134477) -- (0.,3.);  \n'
                                '\\draw (-1.6833606146799929,0.6231112653441612) node[anchor=north west] {$%s$};  \n'
                                '\\draw (-0.6,0) node[anchor=north west] {$O$};  \n'
                                '\\draw (0.9324168814569066,0.6121665896281072) node[anchor=north west] {$%s$};  \n'
                                '\\draw (1.939327047333872,0) node[anchor=north west] {$%s$};  \n'
                                '\\draw (2.7054543474576502,0.5) node[anchor=north west] {$x$};  \n'
                                '\\draw (-0.5,3.195110058616847) node[anchor=north west] {$y$};  \n'
                                '\\end{tikzpicture}  \n'
                                '}'
                                %(latex(x1),latex(x3),
                                latex(x1),latex(x2),latex(x3)
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
                loigiai=('Ta có \\\\ \n'
                        '\\hspace*{1cm} $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x) \\right|\\text{d}x+\\displaystyle\\int\\limits_{%s}^{%s} \\left| f(x) \\right|\\text{d}x=\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x-\\displaystyle\\int\\limits_{%s}^{%s} f(x) \\text{d}x$.'
                        %(latex(x1),latex(x2),latex(x2),latex(x3),latex(x1),latex(x2),latex(x2),latex(x3)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

