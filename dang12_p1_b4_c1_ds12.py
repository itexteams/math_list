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


def bt_dang12_p1_b4_c1_ds12(self):
            # Khai báo biến

            lisdang=['1','2','3','4','5','6','7','8','21','22','23','24','25','26','27']
            dang=random.choice(lisdang)
            if dang=='27':
                x1=randint(1,4)
                x2=randint(5,9)
                y1=randint(-20,-1)
                y2=randint(1,20)

                d = [
                    '$1$',
                    ]
                da= random.choice(d)
                s = [
                    '$0$',
                    '$2$',
                    '$3$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,-,0,+,0,-,} \n'
                                    '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Trong các số $a, b$ và $c$ có bao nhiêu số dương?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $(%s;+\\infty)$ nên $a<0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        'Suy ra $a<0, b>0, c<0$.\\\\ \n'
                        'Vậy trong các số $a, b$ và $c$ có $1$ số dương. \\\\ \n'
                        %(latex(x2),latex(x1),latex(x2))
                        )
            if dang=='26':
                x1=randint(1,4)
                x2=randint(5,9)
                y1=randint(-20,-1)
                y2=randint(1,20)

                d = [
                    '$a<0, b>0, c<0$',
                    ]
                da= random.choice(d)
                s = [
                    '$a<0, b<0, c<0$',
                    '$a<0, b<0, c=0$',
                    '$a<0, b>0, c>0$',
                    '$a<0, b=0, c>0$',
                    '$a>0, b<0, c>0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,-,0,+,0,-,} \n'
                                    '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Khẳng định nào dưới đây đúng?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $(%s;+\\infty)$ nên $a<0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b>0, c<0$.'
                        %(latex(x2),latex(x1),latex(x2))
                        )
            if dang=='25':
                x1=randint(1,4)
                x2=randint(5,9)
                y1=randint(1,9)
                y2=randint(10,20)

                d = [
                    '$2$',
                    ]
                da= random.choice(d)
                s = [
                    '$0$',
                    '$1$',
                    '$3$',
                    '$4$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,-,0,+,0,-,} \n'
                                    '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Trong các số $a, b, c$ và $d$ có bao nhiêu số âm?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $(%s;+\\infty)$ nên $a<0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_2 <0, y_{\\text{CT}}>0$ và hàm số nghịch biến trên khoảng $(-\\infty;%s)$ nên $d>0$. \\\\ \n'
                        'Suy ra $a<0, b>0, c<0, d>0$.\\\\ \n'
                        'Vậy trong các số $a, b, c$ và $d$ có $2$ âm. \\\\ \n'
                        %(latex(x2),latex(x1),latex(x2),latex(x1))
                        )
            if dang=='24':
                x1=randint(1,4)
                x2=randint(5,9)
                y1=randint(1,9)
                y2=randint(10,20)

                d = [
                    '$a<0, b>0, c<0, d>0$',
                    ]
                da= random.choice(d)
                s = [
                    '$a<0, b<0, c>0, d=0$',
                    '$a<0, b<0, c>0, d<0$',
                    '$a<0, b<0, c=0, d>0$',
                    '$a<0, b<0, c<0, d>0$',
                    '$a<0, b=0, c>0, d>0$',
                    '$a<0, b>0, c>0, d>0$',
                    '$a>0, b<0, c>0, d>0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,-,0,+,0,-,} \n'
                                    '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Khẳng định nào dưới đây đúng?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $(%s;+\\infty)$ nên $a<0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_2 <0, y_{\\text{CT}}>0$ và hàm số nghịch biến trên khoảng $(-\\infty;%s)$ nên $d>0$. \\\\ \n'
                        'Vậy $a<0, b>0, c<0, d>0$.'
                        %(latex(x2),latex(x1),latex(x2),latex(x1))
                        )
            if dang=='23':
                x1=randint(-9,-5)
                x2=randint(-4,-1)
                y1=randint(-20,-1)
                y2=randint(1,20)

                d = [
                    '$a<0, b<0, c<0$',
                    ]
                da= random.choice(d)
                s = [
                    '$a<0, b>0, c<0$',
                    '$a<0, b>0, c=0$',
                    '$a<0, b<0, c>0$',
                    '$a<0, b=0, c>0$',
                    '$a>0, b>0, c>0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,-,0,+,0,-,} \n'
                                    '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Khẳng định nào dưới đây đúng?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $(%s;+\\infty)$ nên $a<0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b<0, c<0$.'
                        %(latex(x2),latex(x1),latex(x2))
                        )
            if dang=='22':
                x1=randint(-9,-5)
                x2=randint(-4,-1)
                y1=randint(-20,-10)
                y2=randint(-9,-1)

                d = [
                    '$4$',
                    ]
                da= random.choice(d)
                s = [
                    '$0$',
                    '$1$',
                    '$3$',
                    '$2$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,-,0,+,0,-,} \n'
                                    '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Trong các số $a, b, c$ và $d$ có bao nhiêu số âm?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $(%s;+\\infty)$ nên $a<0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_2 <0, y_{\\text{CĐ}}<0$ và hàm số nghịch biến trên khoảng $(%s;+\\infty)$ nên $d<0$. \\\\ \n'
                        'Suy ra $a<0, b<0, c<0, d<0$. \\\\ \n'
                        'Vậy trong các số $a, b, c$ và $d$ có $4$ số âm. \\\\ \n'
                        %(latex(x2),latex(x1),latex(x2),latex(x2))
                        )
            if dang=='21':
                x1=randint(-9,-5)
                x2=randint(-4,-1)
                y1=randint(-20,-10)
                y2=randint(-9,-1)

                d = [
                    '$a<0, b<0, c<0, d<0$',
                    ]
                da= random.choice(d)
                s = [
                    '$a<0, b>0, c>0, d=0$',
                    '$a<0, b>0, c>0, d>0$',
                    '$a<0, b>0, c=0, d<0$',
                    '$a<0, b>0, c<0, d<0$',
                    '$a<0, b=0, c>0, d<0$',
                    '$a<0, b<0, c>0, d<0$',
                    '$a>0, b>0, c>0, d<0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,-,0,+,0,-,} \n'
                                    '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Khẳng định nào dưới đây đúng?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số nghịch biến trên khoảng $(%s;+\\infty)$ nên $a<0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_2 <0, y_{\\text{CĐ}}<0$ và hàm số nghịch biến trên khoảng $(%s;+\\infty)$ nên $d<0$. \\\\ \n'
                        'Vậy $a<0, b<0, c<0, d<0$.'
                        %(latex(x2),latex(x1),latex(x2),latex(x2))
                        )
            if dang=='8':
                x1=randint(1,4)
                x2=randint(5,9)
                y1=randint(1,20)
                y2=randint(-20,-1)

                d = [
                    '$a>0, b<0, c>0$',
                    ]
                da= random.choice(d)
                s = [
                    '$a>0, b<0, c<0$',
                    '$a>0, b>0, c>0$',
                    '$a>0, b<0, c=0$',
                    '$a>0, b=0, c>0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,+,0,-,0,+,} \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Khẳng định nào dưới đây đúng?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $a>0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a>0, b<0, c>0$.'
                        %(latex(x2),latex(x1),latex(x2))
                        )
            if dang=='7':
                x1=randint(1,4)
                x2=randint(5,9)
                y1=randint(-9,-1)
                y2=randint(-20,-10)

                d = [
                    '$2$',
                    ]
                da= random.choice(d)
                s = [
                    '$0$',
                    '$1$',
                    '$3$',
                    '$4$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,+,0,-,0,+,} \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Trong các số $a, b, c$ và $d$ có bao nhiêu số dương?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $a>0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 >0, y_{\\text{CĐ}}<0$ và hàm số đồng biến trên khoảng $(-\\infty;%s)$ nên $d<0$. \\\\ \n'
                        'Suy ra $a>0, b<0, c>0, d<0$.\\\\ \n'
                        'Vậy trong các số $a, b, c$ và $d$ có $2$ số dương. \\\\ \n'
                        %(latex(x2),latex(x1),latex(x2),latex(x1))
                        )
            if dang=='6':
                x1=randint(1,4)
                x2=randint(5,9)
                y1=randint(-9,-1)
                y2=randint(-20,-10)

                d = [
                    '$a>0, b<0, c>0, d<0$',
                    ]
                da= random.choice(d)
                s = [
                    '$a>0, b<0, c>0, d>0$',
                    '$a>0, b<0, c<0, d<0$',
                    '$a>0, b>0, c>0, d<0$',
                    '$a<0, b<0, c>0, d<0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,+,0,-,0,+,} \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Khẳng định nào dưới đây đúng?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $a>0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 >0, y_{\\text{CĐ}}<0$ và hàm số đồng biến trên khoảng $(-\\infty;%s)$ nên $d<0$. \\\\ \n'
                        'Vậy $a>0, b<0, c>0, d<0$.'
                        %(latex(x2),latex(x1),latex(x2),latex(x1))
                        )
            if dang=='5':
                x1=randint(-9,-5)
                x2=randint(-4,-1)
                y1=randint(-9,-1)
                y2=randint(-20,-10)

                d = [
                    '$a>0, b>0, c>0$',
                    ]
                da= random.choice(d)
                s = [
                    '$a>0, b>0, c<0$',
                    '$a>0, b<0, c>0$',
                    '$a<0, b>0, c>0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,+,0,-,0,+,} \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Khẳng định nào dưới đây đúng?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $a>0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a>0, b>0, c>0$.'
                        %(latex(x2),latex(x1),latex(x2))
                        )
            if dang=='4':
                x1=randint(-9,-5)
                x2=randint(-4,-1)
                y1=randint(1,20)
                y2=randint(-20,-1)

                d = [
                    '$3$',
                    ]
                da= random.choice(d)
                s = [
                    '$1$',
                    '$2$',
                    '$0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,+,0,-,0,+,} \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Trong các số $a, b$ và $c$ có bao nhiêu số dương?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $a>0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Suy ra $a>0, b>0, c>0$. \\\\ \n'
                        'Vậy trong các số $a, b$ và $c$ có $3$ số dương. \\\\ \n'
                        %(latex(x2),latex(x1),latex(x2))
                        )
            if dang=='3':
                x1=randint(-9,-5)
                x2=randint(-4,-1)
                y1=randint(1,20)
                y2=randint(-20,-1)

                d = [
                    '$a>0, b>0, c>0$',
                    ]
                da= random.choice(d)
                s = [
                    '$a>0, b>0, c<0$',
                    '$a>0, b<0, c>0$',
                    '$a<0, b>0, c>0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,+,0,-,0,+,} \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Khẳng định nào dưới đây đúng?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $a>0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a>0, b>0, c>0$.'
                        %(latex(x2),latex(x1),latex(x2))
                        )
            if dang=='2':
                x1=randint(-9,-5)
                x2=randint(-4,-1)
                y1=randint(10,20)
                y2=randint(1,9)

                d = [
                    '$4$',
                    ]
                da= random.choice(d)
                s = [
                    '$1$',
                    '$2$',
                    '$3$',
                    '$0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,+,0,-,0,+,} \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Trong các số $a, b, c$ và $d$ có bao nhiêu số dương?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $a>0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_2 <0, y_{\\text{CT}}>0$ và hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $d>0$. \\\\ \n'
                        'Suy ra $a>0, b>0, c>0, d>0$. \\\\ \n'
                        'Vậy trong các số $a, b, c$ và $d$ có $4$ số dương. \\\\ \n'
                        %(latex(x2),latex(x1),latex(x2),latex(x2))
                        )

            if dang=='1':
                x1=randint(-9,-5)
                x2=randint(-4,-1)
                y1=randint(10,20)
                y2=randint(1,9)

                d = [
                    '$a>0, b>0, c>0, d>0$',
                    ]
                da= random.choice(d)
                s = [
                    '$a>0, b>0, c>0, d<0$',
                    '$a>0, b>0, c<0, d>0$',
                    '$a>0, b<0, c>0, d>0$',
                    '$a>0, b<0, c<0, d>0$',
                    '$a>0, b<0, c>0, d<0$',
                    '$a>0, b>0, c<0, d<0$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có bảng biến thiên như sau  \n'
                                '\\begin{center} \n'
                                    '\\begin{tikzpicture} \n'
                                    '\\tkzTabInit[espcl=2.5,lgt=1.5] \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                    '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                    '\\tkzTabLine{,+,0,-,0,+,} \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Khẳng định nào dưới đây đúng?  \n'
                                %(latex(x1),latex(x2),latex(y1),latex(y2))
                            ) 

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
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $a>0$. \\\\ \n'
                        'Gọi $x_1=%s, x_2=%s$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_2 <0, y_{\\text{CT}}>0$ và hàm số đồng biến trên khoảng $(%s;+\\infty)$ nên $d>0$. \\\\ \n'
                        'Vậy $a>0, b>0, c>0, d>0$.'
                        %(latex(x2),latex(x1),latex(x2),latex(x2))
                        )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

