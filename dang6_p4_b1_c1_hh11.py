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


def bt_dang6_p4_b1_c1_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':

                # Các đỉnh và điểm theo thứ tự trong đề bài
                A, B, C, D = 'A', 'B', 'C', 'D'
                M, N = 'M', 'N'

                # Các tam giác và mặt phẳng:
                T1 = (A, B, D) # Tam giác ABD (M thuộc)
                T2 = (A, C, D) # Tam giác ACD (N thuộc)
                MP1 = (A, M, N) # Mặt phẳng AMN
                MP2 = (B, C, D) # Mặt phẳng BCD
                MP3 = (D, M, N) # Mặt phẳng DMN
                MP4 = (A, B, C) # Mặt phẳng ABC

                # Các giao điểm:
                # a) (AMN) giao (BCD) -> Tìm E, F
                E_diem = 'E'
                E_tinh = f"{A}{M} \\cap {B}{D}" # E = AM giao BD
                F_diem = 'F'
                F_tinh = f"{A}{N} \\cap {C}{D}" # F = AN giao CD
                GT_a = f"{E_diem}{F_diem}"

                # b) (DMN) giao (ABC) -> Tìm G, H
                G_diem = 'G'
                G_tinh = f"{D}{M} \\cap {A}{B}" # G = DM giao AB
                H_diem = 'H'
                H_tinh = f"{D}{N} \\cap {A}{C}" # H = DN giao AC
                GT_b = f"{G_diem}{H_diem}"
                # Nội dung câu hỏi
                noidungcauhoi =  ('''Cho tứ diện $ABCD$. $M$ là một điểm bên trong $\\triangle ABD$, $N$ là điểm bên trong của $\\triangle ACD$. Tìm giao tuyến của các cặp mặt phẳng:\\\\
                a) $(AMN)$ và $(BCD)$.\\\\
                b) $(DMN)$ và $(ABC)$.'''
                                  )

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                           \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,scale=0.8]
            	\\clip(-1.6474916610143997,-2.910511697076057) rectangle (7.471796744413204,4.849041856647621);
            	\\draw (0.,0.)-- (2.,4.);
            	\\draw (2.,4.)-- (6.,0.);
            	\\draw [dash pattern=on 1pt off 1pt] (6.,0.)-- (0.,0.);
            	\\draw (0.,0.)-- (2.,-2.);
            	\\draw (2.,-2.)-- (6.,0.);
            	\\draw (2.,-2.)-- (2.,4.);
            	\\draw [dash pattern=on 1pt off 1pt] (0.9780418901572401,1.9560837803144802)-- (4.136675782570697,1.8633242174293028);
            	\\draw [dash pattern=on 1pt off 1pt] (4.560267858235837,-0.7198660708820819)-- (0.7977145223784878,-0.7977145223784878);
            	\\draw (2.,-2.)-- (0.9780418901572401,1.9560837803144802);
            	\\draw (0.7977145223784878,-0.7977145223784878)-- (2.,4.);
            	\\draw (2.,4.)-- (4.560267858235837,-0.7198660708820819);
            	\\draw (2.,-2.)-- (4.136675782570697,1.8633242174293028);
            	\\draw (1.7065209731885957,4.7) node[anchor=north west] {$A$};
            	\\draw (-0.75,0.3) node[anchor=north west] {$B$};
            	\\draw (6,0.3) node[anchor=north west] {$C$};
            	\\draw (1.5,-2) node[anchor=north west] {$D$};
            	\\draw (4.552899262755463,-0.6) node[anchor=north west] {$F$};
            	\\draw (0.1,-0.6) node[anchor=north west] {$E$};
            	\\draw (4.117784110210209,2.5) node[anchor=north west] {$H$};
            	\\draw (0.3105265254392409,2.5) node[anchor=north west] {$G$};
            	\\draw (3.7,1.3862504343083162) node[anchor=north west] {$N$};
            	\\draw (0.42,1.2774716461720028) node[anchor=north west] {$M$};
            \\end{tikzpicture}
                           \\end{center}'''
                    f'''a) Giao tuyến của $(AMN)$ và $(BCD)$:\\\\
                    Trong mặt phẳng $(ABD)$, gọi ${E_diem} = {E_tinh}$.\\\\
                    Trong mặt phẳng $(ACD)$, gọi ${F_diem} = {F_tinh}$.\\\\
                    Ta có: ${E_diem} \\in AM \\subset (AMN)$ và ${E_diem} \\in BD \\subset (BCD)$. $\\Rightarrow {E_diem}$ là điểm chung thứ nhất.\\\\
                    Ta có: ${F_diem} \\in AN \\subset (AMN)$ và ${F_diem} \\in CD \\subset (BCD)$. $\\Rightarrow {F_diem}$ là điểm chung thứ hai.\\\\
                    Giao tuyến là đường thẳng ${{{GT_a}}}$.\\\\
                    b) Giao tuyến của $(DMN)$ và $(ABC)$:\\\\
                    Tương tự câu a):\\\\
                    Trong mặt phẳng $(ABD)$, gọi ${G_diem} = {G_tinh}$.\\\\
                    Trong mặt phẳng $(ACD)$, gọi ${H_diem} = {H_tinh}$.\\\\
                    Giao tuyến là đường thẳng ${{{GT_b}}}$.
                    ''')

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

