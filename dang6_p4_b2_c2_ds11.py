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


def bt_dang6_p4_b2_c2_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lis=[50000, 55000, 60000, 65000, 70000, 75000, 80000]
                u1=1
                lis1=[2000,3000,5000,1000]
                d=2
                n=randint(10,40)
                un=u1+(n-1)*d
                sn=n*u1+Rational(n*(n-1)*d,2)
                h1=sn

                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Tại một Hội chợ, một công ty sữa muốn xếp $%s$ hộp sữa theo số lượng $1, 3, 5, ...$ từ trên xuống dưới như hình minh họa. \\\\ \n'
                                '\\begin{center} \n'
                                    '\\definecolor{zzttqq}{rgb}{0.6,0.2,0.} \n'
                                    '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                        '\\clip(-0.3651518370173674,-0.27767239587513737) rectangle (5.385927685649263,3.3996602040197277); \n'
                                        '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (0.,0.7130245145988209) -- (5.,0.6878373050104999) -- (5.,0.3100291611856849) -- (0.,0.3100291611856849) -- cycle; \n'
                                        '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (1.,1.6869299520138994) -- (4.,1.6785342154844591) -- (4.,1.2839345986007635) -- (1.,1.3007260716596443) -- cycle; \n'
                                        '\\fill[line width=1.pt,color=zzttqq,fill=zzttqq,fill opacity=0.1] (2.,2.7028140720761797) -- (3.,2.7028140720761797) -- (3.,2.3250059282513647) -- (2.,2.3166101917219244) -- cycle; \n'
                                        '\\draw [line width=1.pt] (0.,0.)-- (0.,1.); \n'
                                        '\\draw [line width=1.pt] (0.,1.)-- (1.,1.); \n'
                                        '\\draw [line width=1.pt] (1.,1.)-- (1.,0.); \n'
                                        '\\draw [line width=1.pt] (1.,0.)-- (0.,0.); \n'
                                        '\\draw [line width=1.pt] (1.,1.)-- (5.,1.); \n'
                                        '\\draw [line width=1.pt] (1.,0.)-- (5.,0.); \n'
                                        '\\draw [line width=1.pt] (5.,1.)-- (5.,0.); \n'
                                        '\\draw [line width=1.pt] (2.,1.)-- (2.,0.); \n'
                                        '\\draw [line width=1.pt] (3.,1.)-- (3.,0.); \n'
                                        '\\draw [line width=1.pt] (4.,1.)-- (4.,0.); \n'
                                        '\\draw [line width=1.pt] (1.,2.)-- (4.,2.); \n'
                                        '\\draw [line width=1.pt] (4.,2.)-- (4.,1.); \n'
                                        '\\draw [line width=1.pt] (1.,2.)-- (1.,1.); \n'
                                        '\\draw [line width=1.pt] (2.,1.)-- (2.,2.); \n'
                                        '\\draw [line width=1.pt] (3.,1.)-- (3.,2.); \n'
                                        '\\draw [line width=1.pt] (2.,2.)-- (2.,3.); \n'
                                        '\\draw [line width=1.pt] (2.,3.)-- (3.,3.); \n'
                                        '\\draw [line width=1.pt] (3.,3.)-- (3.,2.); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (0.,0.7130245145988209)-- (5.,0.6878373050104999); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (5.,0.6878373050104999)-- (5.,0.3100291611856849); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (5.,0.3100291611856849)-- (0.,0.3100291611856849); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (0.,0.3100291611856849)-- (0.,0.7130245145988209); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (1.,1.6869299520138994)-- (4.,1.6785342154844591); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (4.,1.6785342154844591)-- (4.,1.2839345986007635); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (4.,1.2839345986007635)-- (1.,1.3007260716596443); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (1.,1.3007260716596443)-- (1.,1.6869299520138994); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (2.,2.7028140720761797)-- (3.,2.7028140720761797); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (3.,2.7028140720761797)-- (3.,2.3250059282513647); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (3.,2.3250059282513647)-- (2.,2.3166101917219244); \n'
                                        '\\draw [line width=1.pt,color=zzttqq] (2.,2.3166101917219244)-- (2.,2.7028140720761797); \n'
                                        '\\draw (0,0.8) node[anchor=north west] {Sữa}; \n'
                                        '\\draw (1,0.8) node[anchor=north west] {Sữa}; \n'
                                        '\\draw (2,0.8) node[anchor=north west] {Sữa}; \n'
                                        '\\draw (3,0.8) node[anchor=north west] {Sữa}; \n'
                                        '\\draw (4,0.8) node[anchor=north west] {Sữa}; \n'
                                        '\\draw (1,1.8) node[anchor=north west] {Sữa}; \n'
                                        '\\draw (2,1.8) node[anchor=north west] {Sữa}; \n'
                                        '\\draw (3,1.8) node[anchor=north west] {Sữa}; \n'
                                        '\\draw (2,2.8) node[anchor=north west] {Sữa}; \n'
                                    '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Tính số hộp sữa xếp ở hàng dưới cùng.'
                                %(latex(sn)
                                ))

                # Nội dung lời giải
                loigiai = ('Gọi $u_1, u_2, ..., u_n$ lần lượt là số hộp sữa hàng thứ nhất, hàng thứ hai,.... Các giá trị này lập thành một cấp số cộng với số hạng đầu $u_1=1$ và công sai $d=2$. \\\\ \n'
                        'Khi đó, tổng số hộp sữa là \\\\ \n'
                        '\\hspace*{1cm} $S=%s \\Leftrightarrow n u_1+\\dfrac{n(n-1)}{2}d=%s \\Leftrightarrow n+\\dfrac{n(n-1)}{2} \\cdot 2=%s \\Leftrightarrow n^2=%s \\Rightarrow n=%s$.\\\\ \n'
                        'Suy ra $u_{%s}=u_1+(%s-1)d=%s+(%s-1) \\cdot %s=%s$.\\\\ \n'
                        'Vậy số hộp sữa hàng cuối cùng là $%s$ hộp.'

                        %(latex(sn),latex(sn),latex(sn),latex(sn),latex(n),
                            latex(n),latex(n),latex(u1),latex(n),latex(d),latex(un),
                            latex(un)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.0','')
            return content 

