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


def bt_dang30_p1_b1_c1_ds12(self):
            # Khai báo biến
            x = symbols('x')

            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)

            if dang=='4':
                i=randint(1,9)
                a=-i
                b=-5*a
                gtln=-3*a
                gtnn=2*a
                d = ['Hàm số đồng biến trên các khoảng $(%s;0)$ và $(%s;%s)$'%(latex(a),latex(2*i),latex(4*i)),
                    'Hàm số nghịch biến trên các khoảng $(0;%s)$ và $(%s;%s)$'%(latex(2*i),latex(4*i),latex(5*i)),
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(2*i)), 
                    'Hàm số đạt cực đại tại điểm $x=0$',
                    'Hàm số đạt cực đại tại điểm $x=%s$'%(latex(4*i)), 
                    'Hàm số có giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(-2*i)), 
                    'Hàm số có một giá trị cực đại là $y_{\\text{CĐ}}=%s$'%(latex(i)), 
                    'Hàm số có một giá trị cực đại là $y_{\\text{CĐ}}=%s$'%(latex(3*i)), 
                    'Hàm số có $3$ cực trị',
                    ]
                da= random.choice(d)
                s = ['Hàm số nghịch biến trên các khoảng $(%s;0)$ và $(%s;%s)$'%(latex(a),latex(2*i),latex(4*i)),
                    'Hàm số đồng biến trên các khoảng $(0;%s)$ và $(%s;%s)$'%(latex(2*i),latex(4*i),latex(5*i)),
                    'Hàm số đạt cực đại tại điểm $x=%s$'%(latex(2*i)), 
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(4*i)), 
                    'Hàm số có giá trị cực đại là $y_{\\text{CĐ}}=%s$'%(latex(-2*i)), 
                    'Hàm số có một giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(3*i)), 
                    'Hàm số có $5$ cực trị',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Khẳng định nào sau đây là đúng?  \n'
                                %(latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-2.1,0)--(6.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-3.1)--(0,4.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-1,0) node [above] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (5,0) node [below] {$%s$}; \n'
                                '\\draw (0,-2) node [above left] {$%s$}; \n'
                                '\\draw (0,1) node [above left] {$%s$}; \n'
                                '\\draw (0,3) node [left] {$%s$}; \n'
                                '\\draw (4.1,0) node [below] {$%s$}; \n'
                                '\\draw[dashed,thin](-1,0)--(-1,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](1.9,0)--(1.9,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](4.15,0)--(4.15,3.1)--(0,3.1); \n'
                                '\\draw[dashed,thin](5,0)--(5,1)--(0,1); \n'
                                '\\begin{scope} \n'
                                    '\\clip (-2,-3) rectangle (6,4); \n'
                                    '\\draw[name path=f(x)] plot[smooth,tension=0.7] coordinates{(-1,-2) (0,1) (2,-2) (4,3) (5,1)}; \n'
                                '\\end{scope} \n'
                            '\\end{tikzpicture}} \n'
                            %(latex(a),
                            latex(-2*a),
                            latex(b),
                            latex(gtnn),
                            latex(-a),
                            latex(gtln),
                            latex(4*i)
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
                loigiai=(
                        'Từ đồ thị hàm số ta có \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên các khoảng $(%s;0)$ và $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $(0;%s)$ và $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CT}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=0$, giá trị cực tiểu là $y_{\\text{CĐ}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực tiểu là $y_{\\text{CĐ}}=%s$. \\\\ \n'
                        %(latex(a),latex(2*i),latex(4*i),
                        latex(2*i),latex(4*i),latex(5*i),
                        latex(2*i),latex(-2*i),
                        latex(i),
                        latex(4*i),latex(3*i),               
                        )
                            )

            if dang=='3':
                i=randint(1,9)
                a=-2*i
                b=4*i
                gtnn=-4*i
                gtln=i
                d = ['Hàm số nghịch biến trên các khoảng $(%s;0)$ và $(%s;%s)$'%(latex(a),latex(i),latex(2*i)),
                    'Hàm số đồng biến trên các khoảng $(0;%s)$ và $(%s;%s)$'%(latex(i),latex(2*i),latex(4*i)),
                    'Hàm số đạt cực đại tại điểm $x=%s$'%(latex(i)), 
                    'Hàm số đạt cực tiểu tại điểm $x=0$',
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(2*i)), 
                    'Hàm số có giá trị cực đại là $y_{\\text{CĐ}}=%s$'%(latex(-2*i)), 
                    'Hàm số có một giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(-3*i)), 
                    'Hàm số có một giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(-4*i)), 
                    'Hàm số có $3$ cực trị',
                    ]
                da= random.choice(d)
                s = ['Hàm số đồng biến trên các khoảng $(%s;0)$ và $(%s;%s)$'%(latex(a),latex(i),latex(2*i)),
                    'Hàm số nghịch biến trên các khoảng $(0;%s)$ và $(%s;%s)$'%(latex(i),latex(2*i),latex(4*i)),
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(i)), 
                    'Hàm số đạt cực đại tại điểm $x=%s$'%(latex(2*i)), 
                    'Hàm số có giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(-2*i)), 
                    'Hàm số có một giá trị cực đại là $y_{\\text{CD}}=%s$'%(latex(-3*i)), 
                    'Hàm số có $5$ cực trị',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Khẳng định nào sau đây là đúng?  \n'
                                %(latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below] {$%s$}; \n'
                                '\\draw (1,0) node [above] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (4,0) node [above] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,-3) node [below left] {$%s$}; \n'
                                '\\draw (0,-2) node [left] {$%s$}; \n'
                                '\\draw (0,1) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,1)--(0,1); \n'
                                '\\draw[dashed,thin](1,0)--(1,-2)--(0,-2); \n'
                                '\\draw[dashed,thin](2,0)--(2,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (5,2); \n'
                                '\\draw[samples=200,domain=-2:1,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-3}); \n'
                                '\\draw[samples=200,domain=1:2,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+-2*(\\x)}); \n'
                                '\\draw[samples=200,domain=2:4,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+2*(\\x)-8}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'
                            %(latex(a),
                            latex(i),
                            latex(2*i),
                            latex(b),
                            latex(gtnn),
                            latex(-3*i),
                            latex(-2*i),
                            latex(i)
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
                loigiai=(
                        'Từ đồ thị hàm số ta có \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $(%s;0)$ và $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên các khoảng $(0;%s)$ và $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=0$, giá trị cực tiểu là $y_{\\text{CT}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{\\text{CT}}=%s$. \\\\ \n'
                        %(latex(a),latex(i),latex(2*i),
                        latex(i),latex(2*i),latex(4*i),
                        latex(i),latex(-2*i),
                        latex(-3*i),
                        latex(2*i),latex(-4*i),               
                        )
                            )

            if dang=='2':
                i=randint(1,9)
                a=-2*i
                b=3*i
                gtnn=-4*i
                gtln=3*i
                d = ['Hàm số nghịch biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(a),latex(-i),latex(i),latex(2*i)),
                    'Hàm số đồng biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(-i),latex(i),latex(2*i),latex(3*i)),
                    'Hàm số đạt cực đại tại điểm $x=%s$'%(latex(i)), 
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(-i)), 
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(2*i)), 
                    'Hàm số có giá trị cực đại là $y_{\\text{CĐ}}=%s$'%(latex(i)), 
                    'Hàm số có một giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(-3*i)), 
                    'Hàm số có một giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(-4*i)), 
                    'Hàm số có $3$ cực trị',
                    ]
                da= random.choice(d)
                s = ['Hàm số đồng biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(a),latex(-i),latex(i),latex(2*i)),
                    'Hàm số nghịch biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(-i),latex(i),latex(2*i),latex(3*i)),
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(i)), 
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(i)),  
                    'Hàm số có giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(i)), 
                    'Hàm số có một giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(4*i)), 
                    'Hàm số có $5$ cực trị',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Khẳng định nào sau đây là đúng?  \n'
                                %(latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(4.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,4.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2.2,0) node [below] {$%s$}; \n'
                                '\\draw (-1,0) node [above] {$%s$}; \n'
                                '\\draw (1,0) node [below] {$%s$}; \n'
                                '\\draw (2,0) node [above] {$%s$}; \n'
                                '\\draw (3,0) node [below] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,-3) node [right] {$%s$}; \n'
                                '\\draw (0,1) node [left] {$%s$}; \n'
                                '\\draw (0,2) node [left] {$%s$}; \n'
                                '\\draw (0,3) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2.2,0)--(-2.2,3)--(0,3); \n'
                                '\\draw[dashed,thin](-1,0)--(-1,-3)--(0,-3); \n'
                                '\\draw[dashed,thin](1,0)--(1,1)--(0,1); \n'
                                '\\draw[dashed,thin](2.1,0)--(2.1,-4)--(0,-4); \n'
                                '\\draw[dashed,thin](3,0)--(3,2)--(0,2); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (4,4); \n'
                                '\\draw[samples=200,domain=-2.2:2.1,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+0*((\\x)^2)+3*(\\x)+-1}); \n'
                                '\\draw[samples=200,domain=2.1:2.95,smooth,variable=\\x] plot (\\x,{0*((\\x)^3)+0*((\\x)^2)+7*(\\x)+-18.7}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'
                            %(latex(a),
                            latex(-i),
                            latex(i),
                            latex(2*i),
                            latex(b),
                            latex(gtnn),
                            latex(-3*i),
                            latex(i),
                            latex(2*i),
                            latex(gtln)
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
                loigiai=(
                        'Từ đồ thị hàm số ta có \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $(%s;%s)$ và $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên các khoảng $(%s;%s)$ và $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{\\text{CT}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{\\text{CT}}=%s$. \\\\ \n'
                        %(latex(a),latex(-i),latex(i),latex(2*i),
                        latex(-i),latex(i),latex(2*i),latex(3*i),
                        latex(i),latex(i),
                        latex(-i),latex(-3*i),
                        latex(2*i),latex(-4*i),               
                        )
                            )
            if dang=='1':
                i=randint(1,9)
                a=-2*i
                b=6*i
                gtnn=-4*i
                gtln=6*i
                d = ['Hàm số nghịch biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(a),latex(-i),latex(i),latex(4*i)),
                    'Hàm số đồng biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(-i),latex(i),latex(4*i),latex(6*i)),
                    'Hàm số đạt cực đại tại điểm $x=%s$'%(latex(i)), 
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(-i)), 
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(4*i)), 
                    'Hàm số có giá trị cực đại là $y_{\\text{CĐ}}=%s$'%(latex(5*i)), 
                    'Hàm số có một giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(i)), 
                    'Hàm số có một giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(-4*i)), 
                    'Hàm số có $3$ cực trị',
                    ]
                da= random.choice(d)
                s = ['Hàm số đồng biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(a),latex(-i),latex(i),latex(4*i)),
                    'Hàm số nghịch biến trên các khoảng $(%s;%s)$ và $(%s;%s)$'%(latex(-i),latex(i),latex(4*i),latex(6*i)),
                    'Hàm số đạt cực tiểu tại điểm $x=%s$'%(latex(i)), 
                    'Hàm số đạt cực đại tại điểm $x=%s$'%(latex(-i)),  
                    'Hàm số có giá trị cực đại là $y_{\\text{CĐ}}=%s$'%(latex(6*i)), 
                    'Hàm số có một giá trị cực tiểu là $y_{\\text{CT}}=%s$'%(latex(4*i)), 
                    'Hàm số có $5$ cực trị',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ liên tục trên đoạn $[%s;%s]$ và có đồ thị như hình vẽ bên. Khẳng định nào sau đây là đúng?  \n'
                                %(latex(a),latex(b))
                                )
                hinhve = (      '\\scalebox{0.5}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(7.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,7.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw (-2,0) node [below] {$%s$}; \n'
                                '\\draw (-1,0) node [below] {$%s$}; \n'
                                '\\draw (1,0) node [below] {$%s$}; \n'
                                '\\draw (4,0) node [above] {$%s$}; \n'
                                '\\draw (6,0) node [below] {$%s$}; \n'
                                '\\draw (0,-4) node [left] {$%s$}; \n'
                                '\\draw (0,1) node [right] {$%s$}; \n'
                                '\\draw (0,2) node [above right] {$%s$}; \n'
                                '\\draw (0,5) node [left] {$%s$}; \n'
                                '\\draw (0,6) node [right] {$%s$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,6)--(0,6); \n'
                                '\\draw[dashed,thin](-1,0)--(-1,1)--(0,1); \n'
                                '\\draw[dashed,thin](1,0)--(1,5)--(0,5); \n'
                                '\\draw[dashed,thin](4,0)--(4,-4)--(0,-4); \n'
                                '\\draw[dashed,thin](6,0)--(6,2)--(0,2); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-5) rectangle (7,7); \n'
                                '\\draw[samples=200,domain=-1:4,smooth,variable=\\x] plot (\\x,{-1*(\\x)^2+2*(\\x)+4}); \n'
                                '\\draw[samples=200,domain=-2:-1,smooth,variable=\\x] plot (\\x,{0*(\\x)^2-5*(\\x)-4}); \n'
                                '\\draw[samples=200,domain=4:6,smooth,variable=\\x] plot (\\x,{0*(\\x)^2+3*(\\x)-16}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'
                            %(latex(a),
                            latex(-i),
                            latex(i),
                            latex(4*i),
                            latex(b),
                            latex(gtnn),
                            latex(i),
                            latex(2*i),
                            latex(5*i),
                            latex(gtln)
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
                loigiai=(
                        'Từ đồ thị hàm số ta có \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên các khoảng $(%s;%s)$ và $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên các khoảng $(%s;%s)$ và $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực đại tại điểm $x=%s$, giá trị cực đại là $y_{\\text{CĐ}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{\\text{CT}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số đạt cực tiểu tại điểm $x=%s$, giá trị cực tiểu là $y_{\\text{CT}}=%s$. \\\\ \n'
                        %(latex(a),latex(-i),latex(i),latex(4*i),
                        latex(-i),latex(i),latex(4*i),latex(6*i),
                        latex(i),latex(5*i),
                        latex(-i),latex(i),
                        latex(4*i),latex(-4*i),               
                        )
                            )


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n \\immini{'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n }{'+hinhve+ '} \n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

