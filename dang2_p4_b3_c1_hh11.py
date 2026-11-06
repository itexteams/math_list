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


def bt_dang2_p4_b3_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(1,10)
                b=randint(2,9)
                h1=b**2*a**2/(b+1)**2 
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình chóp tứ giác đều $S$zz$ABCD$ có cạnh đáy bằng $%s$$zz$ $M$ là điểm trên $SA$ sao cho $\\dfrac{SM}{SA} = \\dfrac{%s}{%s}$$zz$ Một mặt phẳng $(\\alpha)$ đi qua $M$ song song với $AB$ và $CD$, cắt hình chóp theo một tứ giác$zz$ Tính diện tích của tứ giác đó$zz$  \n'
                                %(latex(a),latex(b),latex(b+1)
                                ))

                # Nội dung lời giải
                loigiai = (

                            '\\begin{center}  \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\clip(-0$zz$538002232100764,-0$zz$5542600506082738) rectangle (6$zz$625555193639811,5$zz$664440541050772); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0$zz$,0$zz$)-- (2$zz$,1$zz$); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,1$zz$)-- (6$zz$,1$zz$); \n'
                            '\\draw (6$zz$,1$zz$)-- (4$zz$,0$zz$); \n'
                            '\\draw (4$zz$,0$zz$)-- (0$zz$,0$zz$); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,1$zz$)-- (3$zz$,5$zz$); \n'
                            '\\draw (3$zz$,5$zz$)-- (0$zz$,0$zz$); \n'
                            '\\draw (3$zz$,5$zz$)-- (4$zz$,0$zz$); \n'
                            '\\draw (3$zz$,5$zz$)-- (6$zz$,1$zz$); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2$zz$3350616505558994,2$zz$3402466022235986)-- (1$zz$005184951667699,1$zz$6753082527794985); \n'
                            '\\draw (1$zz$005184951667699,1$zz$6753082527794985)-- (3$zz$6649383494441006,1$zz$6753082527794985); \n'
                            '\\draw (3$zz$6649383494441006,1$zz$6753082527794985)-- (4$zz$994815048332301,2$zz$3402466022235986); \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (4$zz$994815048332301,2$zz$3402466022235986)-- (2$zz$3350616505558994,2$zz$3402466022235986); \n'
                            '\\draw (1$zz$4,1$zz$5) node[anchor=north west] {A}; \n'
                            '\\draw (-0$zz$4,-0$zz$014341859704542612) node[anchor=north west] {B}; \n'
                            '\\draw (3$zz$8,-0$zz$12039721863206122) node[anchor=north west] {C}; \n'
                            '\\draw (6$zz$08563700273608,1$zz$2) node[anchor=north west] {D}; \n'
                            '\\draw (1$zz$7,2$zz$8) node[anchor=north west] {M}; \n'
                            '\\draw (0$zz$4,2) node[anchor=north west] {N}; \n'
                            '\\draw (3$zz$55,2$zz$3) node[anchor=north west] {P}; \n'
                            '\\draw (4$zz$9,2$zz$8) node[anchor=north west] {Q}; \n'
                            '\\draw (2$zz$76,5$zz$6) node[anchor=north west] {S}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'        

                        'Ta có $\\heva{& AB // (\\alpha) \\\\& CD // (\\alpha)}$$zz$ \\\\ \n'
                        'Giả sử $(\\alpha)$ cắt các mặt bên $(SAB), (SBC), (SCD), (SDA)$ lần lượt tại các điểm $N, P, Q, D$$zz$ \\\\ \n'
                        'Với $N \\in SB, P \\in SC, Q \\in SD$ suy ra $(\\alpha) = (MNPQ)$$zz$ \\\\ \n'
                        'Ta có $\\heva{& (MNPQ) \\cap (SAB) = MN \\\\& AB // (MNPQ)} \\Rightarrow \\dfrac{MN}{AB} = \\dfrac{SM}{SA} = \\dfrac{%s}{%s}$$zz$ \\\\ \n'
                        'Tương tự, ta có được $\\dfrac{NP}{BC} = \\dfrac{PQ}{CD} = \\dfrac{QM}{DA} = \\dfrac{%s}{%s}$ và $MNPQ$ là hình vuông$zz$ \\\\ \n'
                        'Suy ra $S_{MNPQ} = \\left(\\dfrac{%s}{%s} \\right)^2 S_{ABCD} = \\dfrac{%s}{%s} S_{ABCD} = \\dfrac{%s}{%s} \\cdot %s \\cdot %s = \\dfrac{%s}{%s}$$zz$'
                        %(latex(b),latex(b+1),latex(b),latex(b+1),
                            latex(b),latex(b+1),latex(b**2),latex((b+1)**2),latex(b**2),latex((b+1)**2),latex(a),latex(a),latex(b*a*a),latex((b+1)**2)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content                                                       

