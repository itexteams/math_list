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


def bt_dang17_p1_b2_c2_hh10(self):
            #Khai báo biến
            a = randint(10,90)
            b = Rational(a,3)
            c = Rational(a*2,3)
            lis=['1','3']
            dang=random.choice(lis)
            if dang=='1':
                #Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Chất điểm $A$ chịu tác động của ba lực $\\overrightarrow{F}_{1},\\text{ }\\overrightarrow{F}_{2},\\text{ }\\overrightarrow{F}_{3}$ '''
                            '''như hình vẽ bên và ở trạng thái cân bằng (tức là $\\overrightarrow{F}_{1}+\\overrightarrow{F}_{2}+\\overrightarrow{F}_{3}=\\overrightarrow{0}$ ).'''
                            ''' Biết $\\overrightarrow{F}_{1}$ có độ lớn là $%s$ N. Độ lớn của các lực $\\overrightarrow{F}_{2},\\text{ }\\overrightarrow{F}_{3}$ là '''
                            %(latex(a)))
                # Các đáp án
                da_d = '\\True $\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\sqrt{2}\\text{ N}$' %(latex(a),latex(a))
                da_s1 = '$\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\sqrt{3}\\text{ N}$' %(latex(a),latex(a))
                da_s2 = '$\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\sqrt{2}\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\text{ N}$' %(latex(a),latex(a))
                da_s3 = '$\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\sqrt{3}\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\text{ N}$' %(latex(a),latex(a))

                hinhve=(
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
                '\\clip(6.6,-6.7) rectangle (13.9,0.3);\n'
                '\\draw [shift={(10,-3)}] (0,0) -- (0:0.4) arc (0:135:0.4) -- cycle;\n'
                '\\draw [->] (10,-3) -- (13,-3);\n'
                '\\draw [->] (10,-3) -- (10,-6);\n'
                '\\draw [->] (10,-3) -- (7,0.);\n'
                '\\draw (9.4,-2.9) node[anchor=north west] {A};\n'
                '\\begin{scriptsize}\n'
                    '\\draw [fill=black] (10.,-3) circle (2.5pt);\n'
                    '\\draw[color=black] (10.6,-2.6) node {${135}^{0}$};\n'
                    '\\draw[color=black] (10.5,-5.5) node {$\\overrightarrow{{F}_{1}}$};\n'
                    '\\draw[color=black] (12.6,-2.6) node {$\\overrightarrow{{F}_{2}}$};\n'
                    '\\draw[color=black] (7.8,-0.3) node {$\\overrightarrow{{F}_{3}}$};\n'
                '\\end{scriptsize}\n'
            '\\end{tikzpicture}' )
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có theo hình vẽ: $\\overrightarrow{{F}_{1}}+\\overrightarrow{{F}_{2}}=\\overrightarrow{{F}_{4}}$. \\\\ \n'
                    '$\\overrightarrow{{F}_{1}}+\\overrightarrow{{F}_{2}}+\\overrightarrow{{F}_{3}}=\\vec{0}'
                    '\\Leftrightarrow \\overrightarrow{{F}_{4}}=-\\overrightarrow{{F}_{3}}\\'
                    'Rightarrow \\left| -\\overrightarrow{{F}_{3}}\\right|=\\left| \\overrightarrow{{F}_{4}}\\right|$.\\\\ \n'
                    'Khi đó: $\\left|\\overrightarrow{{{F}_{2}}}\\right|=\\dfrac{\\left|\\overrightarrow{{{F}_{1}}} \\right|}{\\tan 45{}^\\circ} =%s;'
                    '\\left|\\overrightarrow{{{F}_{4}}} \\right|=\\dfrac{\\left|\\overrightarrow{{{F}_{1}}}\\right|}{\\text{sin4}5{}^\\circ }'
                    '=%s\\sqrt{2}$;\\\\ \n'
                    'Vậy $\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\sqrt{2}\\text{ N}$.'
                    %(latex(a),latex(a),latex(a),latex(a)))
                hinhlg=('\\begin{center}\n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
                    '\\clip(-3.9,-4.34) rectangle (5.54,3.74);\n'
                    '\\draw [shift={(0,0)}] (0,0) -- (0.:0.7) arc (0.:135:0.7) -- cycle;\n'
                    '\\draw [shift={(0,0)}] (0,0) -- (-45:0.6) arc (-45:0:0.6) -- cycle;\n'
                    '\\draw [->] (0,0) -- (-3,3);\n'
                    '\\draw [->] (0,0) -- (3,-3);\n'
                    '\\draw [->] (0,0) -- (0,-3);\n'
                    '\\draw [->] (0,0) -- (3,0);\n'
                    '\\draw (3,0)-- (3,-3.);\n'
                    '\\draw (0,-3)-- (3,-3);\n'
                    '\\draw (-0.56,-0.06) node[anchor=north west] {$A$};\n'
                    '\\draw[color=black] (0.5,-2.6) node {$\\overrightarrow{{F}_{1}}$};\n'
                    '\\draw[color=black] (2.6,0.6) node {$\\overrightarrow{{F}_{2}}$};\n'
                    '\\draw[color=black] (-2,2.6) node {$\\overrightarrow{{F}_{3}}$};\n'
                    '\\draw[color=black] (2.6,-2.2) node {$\\overrightarrow{{F}_{4}}$};\n'
                    '\\begin{scriptsize}\n'
                '\\draw [fill=black] (0,0) circle (1.5pt);\n'
                '\\draw[color=black] (0.7,0.7) node {$135^{0}$};\n'
                '\\draw[color=black] (0.9,-0.3) node {$45^{0}$};\n'
                '\\end{scriptsize}\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
                    )
            if dang=='2':
                #Nội dung câu hỏi
                noidungcauhoi = ('''{Chất điểm $A$ chịu tác động của ba lực $\\overrightarrow{F}_{1},\\text{ }\\overrightarrow{F}_{2},\\text{ }\\overrightarrow{F}_{3}$ '''
                            '''như hình vẽ và ở trạng thái cân bằng (tức là $\\overrightarrow{F}_{1}+\\overrightarrow{F}_{2}+\\overrightarrow{F}_{3}=\\overrightarrow{0}$ ).'''
                            ''' Biết $\\overrightarrow{F}_{1}$ có độ lớn là $%s$ N. Độ lớn của các lực $\\overrightarrow{F}_{2},\\text{ }\\overrightarrow{F}_{3}$ là '''

                            %(latex(a)))
                # Các đáp án
                da_d = '\\True $\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\sqrt{3}\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\text{ N}$' %(latex(a),latex(2*a))
                da_s1 = '$\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\sqrt{3}\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\sqrt{2}\\text{ N}$' %(latex(a),latex(2*a))
                da_s2 = '$\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\sqrt{2}\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\sqrt{2}\\text{ N}$' %(latex(a),latex(2*a))
                da_s3 = '$\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\sqrt{3}\\text{ N}$' %(latex(a),latex(2*a))
                hinhve=(
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
                    '\\clip(-6.52,-3.82) rectangle (6.46,3.8);\n'
                    '\\draw [shift={(0.,0.)}] (0,0) -- (0.:0.6) arc (0.:150.:0.6) -- cycle;\n'
                    '\\draw [->] (0.,0.) -- (0.,-3.);\n'
                    '\\draw [->] (0.,0.) -- (5.28,-0.02);\n'
                    '\\draw [->] (0.,0.) -- (-5.196152422706632,3.);\n'
                    '\\draw (-0.84,0.24) node[anchor=north west] {$A$};\n'
                    '\\draw[color=black] (0.5,-2.3) node {$\\overrightarrow{{F}_{1}}$};\n'
                    '\\draw[color=black] (5,-0.5) node {$\\overrightarrow{{F}_{2}}$};\n'
                    '\\draw[color=black] (-4,2.8) node {$\\overrightarrow{{F}_{3}}$};\n'
                    '\\begin{scriptsize}\n'
                        '\\draw [fill=black] (0.,0.) circle (2.5pt);\n'
                        '\\draw[color=black] (0.8,0.53) node {$150^0$};\n'
                    '\\end{scriptsize}\n'
                '\\end{tikzpicture}' )
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có theo hình vẽ: $\\overrightarrow{{F}_{1}}+\\overrightarrow{{F}_{2}}=\\overrightarrow{{F}_{4}}$. \\\\ \n'
                    '$\\overrightarrow{{F}_{1}}+\\overrightarrow{{F}_{2}}+\\overrightarrow{{F}_{3}}=\\vec{0}'
                    '\\Leftrightarrow \\overrightarrow{{F}_{4}}=-\\overrightarrow{{F}_{3}}\\'
                    'Rightarrow \\left| -\\overrightarrow{{F}_{3}}\\right|=\\left| \\overrightarrow{{F}_{4}}\\right|$.\\\\ \n'
                    'Khi đó: $\\left|\\overrightarrow{{{F}_{2}}}\\right|=\\dfrac{\\left|\\overrightarrow{{{F}_{1}}} \\right|}{\\tan 30{}^\\circ} =%s\\sqrt{3};'
                    '\\left|\\overrightarrow{{{F}_{4}}} \\right|=\\dfrac{\\left|\\overrightarrow{{{F}_{1}}}\\right|}{\\text{sin3}0{}^\\circ }'
                    '=%s$;\\\\ \n'
                    'Vậy $\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\sqrt{3}\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\text{ N}$.'
                    %(latex(a),latex(2*a),latex(a),latex(2*a)))
                hinhlg=('\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
                '\\clip(-5.7,-3.9) rectangle (6.24,3.46);\n'
                '\\draw [shift={(0.,0.)}] (0,0) -- (0.:0.6) arc (0.:150.:0.6) -- cycle;\n'
                '\\draw [shift={(0.,0.)}] (0,0) -- (-29.98163936884933:0.6) arc (-29.98163936884933:0.018360631150660233:0.6) -- cycle;\n'
                '\\draw [->] (0.,0.) -- (0.,-3.);\n'
                '\\draw [->] (0.,0.) -- (5.28,-0.02);\n'
                '\\draw [->] (0.,0.) -- (-5.196152422706632,3.);\n'
                '\\draw (-0.84,0.24) node[anchor=north west] {$A$};\n'
                '\\draw[color=black] (0.6,-2.5) node {$\\overrightarrow{{F}_{1}}$};\n'
                '\\draw[color=black] (4.8,-0.5) node {$\\overrightarrow{{F}_{2}}$};\n'
                '\\draw[color=black] (-4,2.7) node {$\\overrightarrow{{F}_{3}}$};\n'
                '\\draw[color=black] (4.8,-2.3) node {$\\overrightarrow{{F}_{4}}$};\n'
                '\\draw (0.,-3.)-- (5.2,-3.);\n'
                '\\draw (5.2,-3.)-- (5.260000286956397,-0.019924243511198474);\n'
                '\\draw [->] (0.,0.) -- (5.2,-3.);\n'
                '\\begin{scriptsize}\n'
                    '\\draw [fill=black] (0.,0.) circle (2.5pt);\n'
                    '\\draw[color=black] (0.8,0.53) node {$150^0$};\n'
                    '\\draw[color=black] (1.,-0.19) node {$30^0$};\n'
                '\\end{scriptsize}\n'
            '\\end{tikzpicture}'
                    )
            if dang=='3':
                #Nội dung câu hỏi
                noidungcauhoi = ('\\immini{Chất điểm $A$ chịu tác động của ba lực $\\overrightarrow{F}_{1},\\text{ }\\overrightarrow{F}_{2},\\text{ }\\overrightarrow{F}_{3}$ '''
                            '''như hình vẽ và ở trạng thái cân bằng (tức là $\\overrightarrow{F}_{1}+\\overrightarrow{F}_{2}+\\overrightarrow{F}_{3}=\\overrightarrow{0}$ ).'''
                            ''' Biết $\\overrightarrow{F}_{1}$ có độ lớn là $%s$ N. Độ lớn của các lực $\\overrightarrow{F}_{2},\\text{ }\\overrightarrow{F}_{3}$ là '''
                            %(latex(a)))
                # Các đáp án
                da_d = '\\True $\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\sqrt{3}\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\sqrt{3}\\text{ N}$' %(latex(b),latex(c))
                da_s1 = '$\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\text{ N}$' %(latex(b),latex(c))
                da_s2 = '$\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\sqrt{3}\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\text{ N}$' %(latex(b),latex(c))
                da_s3 = '$\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\sqrt{3}\\text{ N}$' %(latex(b),latex(c))
                hinhve=(
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
                '\\clip(0.8,-1) rectangle (7.1,7);\n'
                '\\draw [shift={(4,3)}] (0,0) -- (0:0.55) arc (0:120:0.55) -- cycle;\n'
                '\\draw [->] (4,3) -- (2,6.5);\n'
                '\\draw [->] (4,3) -- (6,3);\n'
                '\\draw [->] (4,3) -- (4,-0.6);\n'
                '\\draw (3.2,3.4) node[anchor=north west] {$A$};\n'
                '\\draw[color=black] (4.5,-0.3) node {$\\overrightarrow{{F}_{1}}$};\n'
                '\\draw[color=black] (6,2.6) node {$\\overrightarrow{{F}_{2}}$};\n'
                '\\draw[color=black] (2.6,6) node {$\\overrightarrow{{F}_{3}}$};\n'
                '\\begin{scriptsize}\n'
                    '\\draw [fill=black] (4,3) circle (2.5pt);\n'
                    '\\draw[color=black] (4.6,3.6) node {$120^0$};\n'
                    '\\draw [fill=black] (4,3) circle (2.5pt);\n'
                '\\end{scriptsize}\n'
            '\\end{tikzpicture}' )
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có theo hình vẽ: $\\overrightarrow{{F}_{1}}+\\overrightarrow{{F}_{2}}=\\overrightarrow{{F}_{4}}$. \\\\ \n'
                    '$\\overrightarrow{{F}_{1}}+\\overrightarrow{{F}_{2}}+\\overrightarrow{{F}_{3}}=\\vec{0}'
                    '\\Leftrightarrow \\overrightarrow{{F}_{4}}=-\\overrightarrow{{F}_{3}}\\'
                    'Rightarrow \\left| -\\overrightarrow{{F}_{3}}\\right|=\\left| \\overrightarrow{{F}_{4}}\\right|$.\\\\ \n'
                    'Khi đó: $\\left|\\overrightarrow{{{F}_{2}}}\\right|=\\dfrac{\\left|\\overrightarrow{{{F}_{1}}} \\right|}{\\tan 60{}^\\circ}=%s\\sqrt{3};'
                    '\\left|\\overrightarrow{{{F}_{4}}} \\right|=\\dfrac{\\left|\\overrightarrow{{{F}_{1}}}\\right|}{\\text{sin6}0{}^\\circ }'
                    '=%s\\sqrt{3}$;\\\\ \n'
                    'Vậy $\\left|\\overrightarrow{{{F}_{2}}}\\right|=%s\\sqrt{3}\\text{ N},\\text{ }\\left| \\overrightarrow{{{F}_{3}}}\\right|=%s\\sqrt{3}\\text{ N}$.'
                    %(latex(b),latex(c),latex(b),latex(c)))
                hinhlg=('\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
                    '\\clip(0.5,-1.3) rectangle (7.6,7.2);\n'
                    '\\draw [shift={(4,3)}] (0,0) -- (0:0.43) arc (0:120:0.432) -- cycle;\n'
                    '\\draw [shift={(4.,3)}] (0,0) -- (-60:0.35) arc (-60:0:0.36) -- cycle;\n'
                '\\draw [->] (4,3) -- (2,6.5);\n'
                '\\draw [->] (4,3) -- (6,3);\n'
                '\\draw [->] (4,3) -- (4,-0.4);\n'
                '\\draw (3.2,3.5) node[anchor=north west] {$A$};\n'
                '\\draw[color=black] (4.3,0) node {$\\overrightarrow{{F}_{1}}$};\n'
                '\\draw[color=black] (5.5,2.5) node {$\\overrightarrow{{F}_{2}}$};\n'
                '\\draw[color=black] (2.7,6) node {$\\overrightarrow{{F}_{3}}$};\n'
                '\\draw[color=black] (5.3,0) node {$\\overrightarrow{{F}_{4}}$};\n'
                '\\draw [->] (4,3) -- (6,-0.4);\n'
                '\\draw (4,-0.4)-- (6,-0.44);\n'
                '\\draw (6,-0.4)-- (6,3);\n'
                '\\begin{scriptsize}\n'
                    '\\draw[color=black] (4.5,3.5) node {$120^0$};\n'
                    '\\draw [fill=black] (4,3) circle (2.5pt);\n'
                    '\\draw[color=black] (4.7,2.8) node {$60^0$};\n'
                    '\\end{scriptsize}\n'
                    '\\end{tikzpicture}'
                    )
            # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n}{'+hinhve+'}'
                '\\loigiai{'
                '\\begin{center}'
                +hinhlg+
                '\\end{center}'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('++','+').replace('+-','-').replace('\\frac','\\dfrac')
            return content

