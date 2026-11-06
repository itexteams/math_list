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


def bt_dang74_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random bán kính R
                R = random.randint(2, 5)
                R2 = R * R

                # Cấu trúc vector: (a_str, b_str, a2b2_str, vX_str, vX_val, c_str, c_val, k_val)
                # k = 1 + (vX / c)^2. Chọn các số sao cho k là số chính phương để phương trình Elip đẹp.
                vec_options = [
                    ("1", "\\sqrt{2}", "1^2 + (\\sqrt{2})^2", "\\sqrt{3}", math.sqrt(3), "-1", -1, 4),
                    ("2", "2", "2^2 + 2^2", "2\\sqrt{2}", math.sqrt(8), "-1", -1, 9),
                    ("\\sqrt{6}", "3", "(\\sqrt{6})^2 + 3^2", "\\sqrt{15}", math.sqrt(15), "-1", -1, 16)
                ]

                vec = random.choice(vec_options)
                a_str, b_str, a2b2_str, vX_str, vX_val, c_str, c_val, k_val = vec

                sqrt_k = int(math.sqrt(k_val))
                kR2 = k_val * R2
                sqrt_k_times_R = sqrt_k * R

                # Tính diện tích tích phân: S = 2 * (1/4*pi*R^2 + 1/4*pi*sqrt(k)*R^2) = 1/2 * pi * R^2 * (1 + sqrt(k))
                S_float = 0.5 * math.pi * R2 * (1 + sqrt_k)
                kq_val = Decimal(S_float).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_val).replace('.', ',')

                # Các đáp án trắc nghiệm gây nhiễu
                kq_float = float(kq_val)
                s_vals = [
                    kq_float + 1, kq_float + 2, kq_float + 3,
                    kq_float - 1, kq_float - 2, kq_float - 3,
                    kq_float + 0.5, kq_float - 0.5
                ]

                du = ['$%s$' % (kq_str)]
                da = random.choice(du)

                s = ['$%s$' % (str(Decimal(v).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')) for v in s_vals]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Hình vẽ TikZ
                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\tikzset {_zwbfoczwe/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{75.9 bp } { -122.1 bp }  }  \pgftransformscale{1.32 }  }}}
            		\pgfdeclareradialshading{_sfgknv5zc}{\pgfpoint{-72bp}{104bp}}{rgb(0bp)=(1,1,1);
            			rgb(0bp)=(1,1,1);
            			rgb(16.55357905796596bp)=(0.49,0.83,0.13);
            			rgb(25bp)=(0.25,0.46,0.02);
            			rgb(400bp)=(0.25,0.46,0.02)}
            		\tikzset {_oivkcok4d/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            		\pgfdeclareradialshading{_l4acbm0jr}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            			rgb(0bp)=(1,1,1);
            			rgb(25bp)=(0.97,0.91,0.11);
            			rgb(400bp)=(0.97,0.91,0.11)}
            		\tikzset{every picture/.style={line width=0.75pt}}  
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.36 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (407.8,158.9) -- (319.8,248.4) -- (73.8,180.4) -- (195.8,102.4) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.31 ] (272.3,160.4) .. controls (259.8,152.4) and (214.8,153.9) .. (234.8,183.9) .. controls (347.8,207.5) and (333.8,169) .. (272.3,160.4) -- cycle ;
            		\path  [shading=_sfgknv5zc,_zwbfoczwe] (249.3,130.4) .. controls (267.3,129.9) and (287.3,144.9) .. (284.3,171.9) .. controls (275.3,184.4) and (233.8,193.4) .. (215.5,171) .. controls (212.8,141.9) and (232.3,132.4) .. (249.3,130.4) -- cycle ; 
            		\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.3 ] (249.3,130.4) .. controls (267.3,129.9) and (287.3,144.9) .. (284.3,171.9) .. controls (275.3,184.4) and (233.8,193.4) .. (215.5,171) .. controls (212.8,141.9) and (232.3,132.4) .. (249.3,130.4) -- cycle ; 
            		\draw    (284.3,171.9) -- (366.82,182.52) ;
            		\draw [shift={(369.8,182.9)}, rotate = 187.33] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw    (232.6,181.5) -- (200.93,207.11) ;
            		\draw [shift={(198.6,209)}, rotate = 321.03] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw    (247.8,128.9) -- (246.36,57.4) ;
            		\draw [shift={(246.3,54.4)}, rotate = 88.85] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (248.8,166.9) -- (284.3,171.9) ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (248.8,166.9) -- (232.6,181.5) ;
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (248.8,166.9) -- (247.8,128.9) ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.23 ] (73.5,50.5) .. controls (73.5,36.69) and (84.69,25.5) .. (98.5,25.5) .. controls (112.31,25.5) and (123.5,36.69) .. (123.5,50.5) .. controls (123.5,64.31) and (112.31,75.5) .. (98.5,75.5) .. controls (84.69,75.5) and (73.5,64.31) .. (73.5,50.5) -- cycle ;
            		\draw  [draw opacity=0][shading=_l4acbm0jr,_oivkcok4d] (82.5,50.5) .. controls (82.5,41.66) and (89.66,34.5) .. (98.5,34.5) .. controls (107.34,34.5) and (114.5,41.66) .. (114.5,50.5) .. controls (114.5,59.34) and (107.34,66.5) .. (98.5,66.5) .. controls (89.66,66.5) and (82.5,59.34) .. (82.5,50.5) -- cycle ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (111,60) -- (220.85,137.27) ;
            		\draw [shift={(223.3,139)}, rotate = 215.13] [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (106.5,64) -- (217.34,141.78) ;
            		\draw [shift={(219.8,143.5)}, rotate = 215.06] [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (114,55.5) -- (224.84,133.28) ;
            		\draw [shift={(227.3,135)}, rotate = 215.06] [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (98.5,66.5) -- (213.35,147.27) ;
            		\draw [shift={(215.8,149)}, rotate = 215.12] [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (114.5,49) -- (231.84,131.28) ;
            		\draw [shift={(234.3,133)}, rotate = 215.04] [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (90.5,67.5) -- (213.15,154.27) ;
            		\draw [shift={(215.6,156)}, rotate = 215.28] [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw [color={rgb, 255:red, 248; green, 231; blue, 28 }  ,draw opacity=1 ]   (115,42.5) -- (238.14,128.29) ;
            		\draw [shift={(240.6,130)}, rotate = 214.86] [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (5.36,-2.57) -- (0,0) -- (5.36,2.57) -- (3.56,0) -- cycle    ;
            		\draw (185.7,186.5) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\draw (356.7,155) node [anchor=north west][inner sep=0.75pt]    {$y$};
            		\draw (230.7,47.5) node [anchor=north west][inner sep=0.75pt]    {$z$};
            		\draw (165.7,66) node [anchor=north west][inner sep=0.75pt]  [font=\tiny,color={rgb, 255:red, 248; green, 231; blue, 28 }  ,opacity=1 ] [align=left] {Chùm tia sáng};
            	\end{tikzpicture}
            \end{center}'''

                noidungcauhoi = (r'''Trong không gian hệ tọa độ $Oxyz$, có một khối bán cầu tâm $O(0;0;0)$, bán kính $R = %s$ và đáy bán cầu trùng với mặt phẳng $Oxy$ (phần $z \ge 0$). Một chùm tia sáng mặt trời chiếu tới khối bán cầu, các tia sáng song song với vectơ $\vec{v}=(%s; %s; %s)$. Biết rằng khối bán cầu không cho ánh sáng xuyên qua. Diện tích bóng của bán cầu trên mặt phẳng $Oxy$ bằng bao nhiêu? (Kết quả làm tròn đến hàng phần chục). %s'''
                                 % (R, a_str, b_str, c_str, hinhve))


                # Random vị trí đáp án đúng
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải bám sát 100% hình ảnh
                loigiai = ('''\\begin{center}
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                		\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.23 ][line width=1]  (136.41,56.9) .. controls (234.7,56.99) and (314.32,92.31) .. (314.32,135.86) .. controls (314.32,179.46) and (234.5,214.81) .. (136.04,214.81) .. controls (135.86,214.81) and (135.68,214.81) .. (135.49,214.81) -- (136.04,135.86) -- cycle ; \\draw  [line width=1]  (136.41,56.9) .. controls (234.7,56.99) and (314.32,92.31) .. (314.32,135.86) .. controls (314.32,179.46) and (234.5,214.81) .. (136.04,214.81) .. controls (135.86,214.81) and (135.68,214.81) .. (135.49,214.81) ;  
                		\\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (135.35,214.81) .. controls (91.99,214.61) and (56.91,179.34) .. (56.91,135.86) .. controls (56.91,92.25) and (92.19,56.9) .. (135.72,56.9) .. controls (135.91,56.9) and (136.09,56.91) .. (136.27,56.91) -- (135.72,135.86) -- cycle ; \\draw  [line width=1]  (135.35,214.81) .. controls (91.99,214.61) and (56.91,179.34) .. (56.91,135.86) .. controls (56.91,92.25) and (92.19,56.9) .. (135.72,56.9) .. controls (135.91,56.9) and (136.09,56.91) .. (136.27,56.91) ;  
                		\\draw  [draw opacity=0][fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (136.04,56.9) .. controls (179.4,57.11) and (214.49,92.38) .. (214.49,135.86) .. controls (214.49,179.46) and (179.2,214.81) .. (135.67,214.81) .. controls (135.49,214.81) and (135.3,214.81) .. (135.12,214.81) -- (135.67,135.86) -- cycle ; \\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (136.04,56.9) .. controls (179.4,57.11) and (214.49,92.38) .. (214.49,135.86) .. controls (214.49,179.46) and (179.2,214.81) .. (135.67,214.81) .. controls (135.49,214.81) and (135.3,214.81) .. (135.12,214.81) ;  
                		\\draw [line width=1]    (23.22,135.86) -- (353.8,135.86) ;
                		\\draw [shift={(357.8,135.86)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                		\\draw [line width=1]    (135.86,234.49) -- (135.86,29.32) ;
                		\\draw [shift={(135.86,25.32)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (136.04,135.86) -- (155.65,93.49) ;
                		\\draw [shift={(157.33,89.86)}, rotate = 114.83] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (136.04,135.86) -- (210.08,135.64) ;
                		\\draw [shift={(214.08,135.63)}, rotate = 179.83] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (8.75,-4.2) -- (0,0) -- (8.75,4.2) -- (5.81,0) -- cycle    ;
                		\\draw [color={rgb, 255:red, 128; green, 128; blue, 128 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (62.12,230.38) -- (215.45,33.1) ;
                		\\draw  [line width=1]  (457.07,108.93) -- (623.2,108.93) -- (552,182.67) -- (385.87,182.67) -- cycle ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (407.2,145.8) -- (599.2,145.8) ;
                		\\draw [shift={(603.2,145.8)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (553.2,90.93) -- (456.49,202.58) ;
                		\\draw [shift={(453.87,205.6)}, rotate = 310.9] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (504.53,145.8) -- (504.53,53.6) ;
                		\\draw [shift={(504.53,49.6)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                		\\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=0.45 ][line width=1]  (452.53,145.8) .. controls (452.53,134.75) and (476.11,125.8) .. (505.2,125.8) .. controls (534.29,125.8) and (557.87,134.75) .. (557.87,145.8) .. controls (557.87,156.85) and (534.29,165.8) .. (505.2,165.8) .. controls (476.11,165.8) and (452.53,156.85) .. (452.53,145.8) -- cycle ;
                		\\draw  [draw opacity=0][fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=0.44 ][line width=1]  (452.53,145.8) .. controls (452.5,144.91) and (452.48,144.02) .. (452.48,143.13) .. controls (452.48,111.09) and (476.06,85.13) .. (505.14,85.13) .. controls (534.23,85.13) and (557.81,111.09) .. (557.81,143.13) .. controls (557.81,143.58) and (557.81,144.03) .. (557.8,144.49) -- (505.14,143.13) -- cycle ; \\draw  [line width=1]  (452.53,145.8) .. controls (452.5,144.91) and (452.48,144.02) .. (452.48,143.13) .. controls (452.48,111.09) and (476.06,85.13) .. (505.14,85.13) .. controls (534.23,85.13) and (557.81,111.09) .. (557.81,143.13) .. controls (557.81,143.58) and (557.81,144.03) .. (557.8,144.49) ;  
                		\\draw  [draw opacity=0][line width=1]  (557.85,146.26) .. controls (557.21,157.09) and (533.88,165.8) .. (505.2,165.8) .. controls (476.53,165.8) and (453.22,157.1) .. (452.55,146.28) -- (505.2,145.8) -- cycle ; \\draw  [line width=1]  (557.85,146.26) .. controls (557.21,157.09) and (533.88,165.8) .. (505.2,165.8) .. controls (476.53,165.8) and (453.22,157.1) .. (452.55,146.28) ;  
                		\\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (452.55,146.28) .. controls (453.19,135.44) and (476.52,126.74) .. (505.2,126.74) .. controls (533.87,126.74) and (557.18,135.43) .. (557.85,146.26) -- (505.2,146.74) -- cycle ; \\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (452.55,146.28) .. controls (453.19,135.44) and (476.52,126.74) .. (505.2,126.74) .. controls (533.87,126.74) and (557.18,135.43) .. (557.85,146.26) ;  
                		\\draw (442.67,195) node [anchor=north west][inner sep=0.75pt]    {$x$};
                		\\draw (586.67,149) node [anchor=north west][inner sep=0.75pt]    {$y$};
                		\\draw (486,42.67) node [anchor=north west][inner sep=0.75pt]    {$z$};
                		\\draw (404,156.33) node [anchor=north west][inner sep=0.75pt]    {$( Oxy)$};
                		\\draw (118.35,116.39) node [anchor=north west][inner sep=0.75pt]    {$O$};
                		\\draw (344.13,144) node [anchor=north west][inner sep=0.75pt]    {$u$};
                		\\draw (118.48,16.15) node [anchor=north west][inner sep=0.75pt]    {$v$};
                		\\draw (140.24,75.74) node [anchor=north west][inner sep=0.75pt]    {$z$};
                		\\draw (188.84,108.81) node [anchor=north west][inner sep=0.75pt]    {$\\overrightarrow{v'}$};
                		\\draw (218.78,204.73) node [anchor=north west][inner sep=0.75pt]    {$( Oxy)$};
                		\\draw (50.28,222) node [anchor=north west][inner sep=0.75pt]    {$x$};
                	\\end{tikzpicture}
                \\end{center}'''
                    'Hình chiếu vuông góc của $\\vec{v}$ lên mặt phẳng đáy $(Oxy)$ là $\\vec{v}_{xy} = (%s; %s; 0)$.\\\\ \n'
                    'Độ dài $|\\vec{v}_{xy}| = \\sqrt{%s} = %s$\\\\ \n'
                    'Ta thực hiện phép xoay trục: Giữ nguyên trục $Oz$, ta xoay hệ trục $Oxy$ quanh $O$ thành hệ trục $OXYZ$ sao cho trục $OX$ mới trùng với hướng của $\\vec{v}_{xy}$.\\\\ \n'
                    'Trong hệ tọa độ $OXYZ$ mới:\\\\ \n'
                    'Khối bán cầu là khối tròn xoay quanh $Oz$ nên phương trình không đổi: $X^2 + Y^2 + Z^2 \\le %s$\\\\ \n'
                    'Vectơ chỉ phương của tia sáng lúc này chỉ còn thành phần trên trục $OX$ và $OZ$ tọa độ mới của nó là: $\\vec{v}\'_{xy} = (|\\vec{v}_{xy}|; 0; v_z) = (%s; 0; %s)$\\\\ \n'
                    'Bóng của chính mặt đáy bán cầu: Do đáy bán cầu đã nằm sẵn trên mặt đất, bóng của nó chính là hình tròn tâm $O$, bán kính $R = %s$ có phương trình $(C): X^2 + Y^2 \\le %s$\\\\ \n'
                    'Bóng của phần mặt cong bán cầu: Gọi $M(X_0; Y_0; Z_0)$ là điểm tiếp xúc thì vectơ pháp tuyến tại điểm $M$ là $\\vec{n} = (X_0; Y_0; Z_0)$\\\\ \n'
                    'Điều kiện tiếp xúc (tia sáng vuông góc với pháp tuyến): $\\vec{n} \\cdot \\vec{v}\'_{xy} = 0 \\Leftrightarrow %s X_0 - Z_0 = 0 \\Rightarrow Z_0 = %s X_0$\\\\ \n'
                    'Thay $Z_0$ vào phương trình mặt cầu, ta được phương trình đường cong tiếp xúc:\\\\ \n'
                    '$X_0^2 + Y_0^2 + Z_0^2 = %s \\Leftrightarrow %s X_0^2 + Y_0^2 = %s$\\\\ \n'
                    'Một tia sáng đi qua $M$ có phương trình tham số: $\\begin{cases} X = X_0 + %s t \\\\ Y = Y_0 \\\\ Z = Z_0 - t \\end{cases}$ và tia sáng qua $M$ chạm đất khi \\\\ \n'
                    '$Z = 0 \\Rightarrow t = Z_0 = %s X_0$\\\\ \n'
                    'Tọa độ điểm bóng trên mặt đất là: $\\begin{cases} X = X_0 + (%s X_0)%s = %s X_0 \\Rightarrow X_0 = \\frac{X}{%s} \\\\ Y = Y_0 \\end{cases}$\\\\ \n'
                    'Thế vào phương trình trên, ta được đường viền của bóng cong là một nửa Elip \\\\ \n'
                    '$(E): \\frac{X^2}{%s} + \\frac{Y^2}{%s} = 1 \\ (X \\ge 0)$\\\\ \n'
                    'Bóng trên mặt đất là sự hợp nhất của hình tròn $(C)$ và nửa Elip $(E)$. Do nửa Elip bao trùm hoàn toàn nửa phải của hình tròn, nên hình phẳng tạo thành bóng được giới hạn bởi:\\\\ \n'
                    'Nửa trái là đường tròn $X^2 + Y^2 = %s \\Rightarrow Y = \\pm \\sqrt{%s - X^2}$ (với $X \\in [-%s; 0]$)\\\\ \n'
                    'Nửa phải là Elip $\\frac{X^2}{%s} + \\frac{Y^2}{%s} = 1 \\Rightarrow Y = \\pm \\frac{1}{%s} \\sqrt{%s - X^2}$\\\\ \n'
                    'Gọi $S$ là diện tích toàn bộ bóng. Do tính đối xứng qua trục $OX$, ta tính phần diện tích phía trên trục $OX$ rồi nhân đôi\\\\ \n'
                    'Vậy diện tích bóng cần tìm là: $S = 2 \\cdot \\left( \\int_{-%s}^{0} \\sqrt{%s - X^2} \\text{d}X + \\int_{0}^{%s} \\frac{1}{%s} \\sqrt{%s - X^2} \\text{d}X \\right) \\approx %s$.'
                ) % (a_str, b_str, 
                     a2b2_str, vX_str, 
                     R2, 
                     vX_str, c_str, 
                     R, R2, 
                     vX_str, vX_str, 
                     R2, k_val, R2, 
                     vX_str, 
                     vX_str, 
                     vX_str, vX_str, k_val, k_val, 
                     kR2, R2, 
                     R2, R2, R, 
                     kR2, R2, sqrt_k, kR2, 
                     R, R2, sqrt_k_times_R, sqrt_k, kR2, kq_str)
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

