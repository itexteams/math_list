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


def bt_dang10_p3_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số sao cho cos(alpha) = 1/2 để góc ở tâm luôn đẹp (pi/3)
                # R_val và r_val là các số nguyên, d_val = 2*(R_val + r_val)
                R_val = random.randint(20, 40)
                r_val = random.randint(10, R_val - 5)
                d_val = 2 * (R_val + r_val)

                R = sp.Integer(R_val)
                r = sp.Integer(r_val)
                d = sp.Integer(d_val)
                sum_Rr = R + r

                # Tính toán chiều dài đoạn thẳng AB
                AB_sq = d**2 - sum_Rr**2
                AB = sp.simplify(sp.sqrt(AB_sq))
                AB_2 = sp.simplify(2 * AB)

                # Tính các thành phần cung
                # Góc alpha = pi/3, nên góc ôm mỗi ròng rọc là 4*pi/3
                phi = 4 * sp.pi / 3
                L_R = sp.simplify(R * phi)
                L_r = sp.simplify(r * phi)

                # Tổng chiều dài chính xác
                L_exact = sp.simplify(L_R + L_r + AB_2)

                # Làm tròn đến hàng đơn vị
                L_approx = L_exact.evalf()
                L_rounded = int(Decimal(str(L_approx)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                # Các đáp án trắc nghiệm nhiễu
                da = '$%s$' % (L_rounded)

                s = [
                    '$%s$' % (L_rounded + random.randint(1, 3)),
                    '$%s$' % (L_rounded - random.randint(1, 3)),
                    '$%s$' % (L_rounded + random.randint(4, 6)),
                    '$%s$' % (L_rounded - random.randint(4, 6)),
                    '$%s$' % (L_rounded + random.randint(7, 9))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\tikzset {_vjz47kqfg/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { -37.5 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_94oruazmw}{150bp}{rgb(0bp)=(0.64,0.51,0.31);
            			rgb(37.5bp)=(0.64,0.51,0.31);
            			rgb(50bp)=(0.91,0.82,0.74);
            			rgb(62.5bp)=(0.64,0.54,0.38);
            			rgb(100bp)=(0.64,0.54,0.38)}
            		\tikzset {_ld37u11uv/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { -37.5 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_3mw2zuxcr}{150bp}{rgb(0bp)=(0.43,0.33,0.17);
            			rgb(37.5bp)=(0.43,0.33,0.17);
            			rgb(50bp)=(0.91,0.82,0.74);
            			rgb(62.5bp)=(0.34,0.26,0.13);
            			rgb(100bp)=(0.34,0.26,0.13)}
            		\tikzset {_11w6ta0fq/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { -37.5 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_809pvhd1w}{150bp}{rgb(0bp)=(0.64,0.51,0.31);
            			rgb(37.5bp)=(0.64,0.51,0.31);
            			rgb(50bp)=(0.91,0.82,0.74);
            			rgb(62.5bp)=(0.64,0.54,0.38);
            			rgb(100bp)=(0.64,0.54,0.38)}
            		\tikzset {_df0dg5gmp/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { -37.5 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_93wtyiq23}{150bp}{rgb(0bp)=(0.64,0.51,0.31);
            			rgb(37.5bp)=(0.64,0.51,0.31);
            			rgb(50bp)=(0.91,0.82,0.74);
            			rgb(62.5bp)=(0.64,0.54,0.38);
            			rgb(100bp)=(0.64,0.54,0.38)}
            		\tikzset {_3dbbylg1k/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { -37.5 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_zhztnq9pm}{150bp}{rgb(0bp)=(0.43,0.33,0.17);
            			rgb(37.5bp)=(0.43,0.33,0.17);
            			rgb(50bp)=(0.91,0.82,0.74);
            			rgb(62.5bp)=(0.34,0.26,0.13);
            			rgb(100bp)=(0.34,0.26,0.13)}
            		\tikzset {_ihl6ax85b/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { -37.5 bp }  }  \pgftransformrotate{0 }  \pgftransformscale{2 }  }}}
            		\pgfdeclarehorizontalshading{_4rbf6vmjm}{150bp}{rgb(0bp)=(0.64,0.51,0.31);
            			rgb(37.5bp)=(0.64,0.51,0.31);
            			rgb(50bp)=(0.91,0.82,0.74);
            			rgb(62.5bp)=(0.64,0.54,0.38);
            			rgb(100bp)=(0.64,0.54,0.38)}
            		\tikzset{every picture/.style={line width=0.75pt}} 
            		\draw [color={rgb, 255:red, 21; green, 63; blue, 112 }  ,draw opacity=1 ][line width=3.75]    (147.63,210.85) -- (427.1,96.59) ;
            		\draw [color={rgb, 255:red, 21; green, 63; blue, 112 }  ,draw opacity=1 ][line width=3.75]    (147.63,67.42) -- (416.57,178.08) ;
            		\draw  [draw opacity=0][line width=3.75]  (147.63,210.85) .. controls (139.49,213.84) and (130.7,215.47) .. (121.53,215.47) .. controls (79.56,215.47) and (45.53,181.29) .. (45.53,139.13) .. controls (45.53,96.98) and (79.56,62.8) .. (121.53,62.8) .. controls (130.7,62.8) and (139.49,64.43) .. (147.63,67.42) -- (121.53,139.13) -- cycle ; \draw  [color={rgb, 255:red, 20; green, 61; blue, 110 }  ,draw opacity=1 ][line width=3.75]  (147.63,210.85) .. controls (139.49,213.84) and (130.7,215.47) .. (121.53,215.47) .. controls (79.56,215.47) and (45.53,181.29) .. (45.53,139.13) .. controls (45.53,96.98) and (79.56,62.8) .. (121.53,62.8) .. controls (130.7,62.8) and (139.49,64.43) .. (147.63,67.42) ;  
            		\draw  [draw opacity=0][line width=3.75]  (427.1,96.59) .. controls (431.44,95.21) and (436.07,94.47) .. (440.87,94.47) .. controls (465.9,94.47) and (486.2,114.76) .. (486.2,139.8) .. controls (486.2,164.84) and (465.9,185.13) .. (440.87,185.13) .. controls (431.93,185.13) and (423.59,182.55) .. (416.57,178.08) -- (440.87,139.8) -- cycle ; \draw  [color={rgb, 255:red, 22; green, 61; blue, 106 }  ,draw opacity=1 ][line width=3.75]  (427.1,96.59) .. controls (431.44,95.21) and (436.07,94.47) .. (440.87,94.47) .. controls (465.9,94.47) and (486.2,114.76) .. (486.2,139.8) .. controls (486.2,164.84) and (465.9,185.13) .. (440.87,185.13) .. controls (431.93,185.13) and (423.59,182.55) .. (416.57,178.08) ;  
            		\path  [shading=_94oruazmw,_vjz47kqfg] (46.2,138.8) .. controls (46.2,96.83) and (80.23,62.8) .. (122.2,62.8) .. controls (164.17,62.8) and (198.2,96.83) .. (198.2,138.8) .. controls (198.2,180.77) and (164.17,214.8) .. (122.2,214.8) .. controls (80.23,214.8) and (46.2,180.77) .. (46.2,138.8) -- cycle ; 
            		\draw  [color={rgb, 255:red, 132; green, 92; blue, 55 }  ,draw opacity=1 ] (46.2,138.8) .. controls (46.2,96.83) and (80.23,62.8) .. (122.2,62.8) .. controls (164.17,62.8) and (198.2,96.83) .. (198.2,138.8) .. controls (198.2,180.77) and (164.17,214.8) .. (122.2,214.8) .. controls (80.23,214.8) and (46.2,180.77) .. (46.2,138.8) -- cycle ; 
            		\path  [shading=_3mw2zuxcr,_ld37u11uv] (63.53,138.8) .. controls (63.53,106.4) and (89.8,80.13) .. (122.2,80.13) .. controls (154.6,80.13) and (180.87,106.4) .. (180.87,138.8) .. controls (180.87,171.2) and (154.6,197.47) .. (122.2,197.47) .. controls (89.8,197.47) and (63.53,171.2) .. (63.53,138.8) -- cycle ; 
            		\draw  [color={rgb, 255:red, 157; green, 121; blue, 92 }  ,draw opacity=1 ] (63.53,138.8) .. controls (63.53,106.4) and (89.8,80.13) .. (122.2,80.13) .. controls (154.6,80.13) and (180.87,106.4) .. (180.87,138.8) .. controls (180.87,171.2) and (154.6,197.47) .. (122.2,197.47) .. controls (89.8,197.47) and (63.53,171.2) .. (63.53,138.8) -- cycle ; 
            		\path  [shading=_809pvhd1w,_11w6ta0fq] (67.87,138.97) .. controls (67.87,108.31) and (92.71,83.47) .. (123.37,83.47) .. controls (154.02,83.47) and (178.87,108.31) .. (178.87,138.97) .. controls (178.87,169.62) and (154.02,194.47) .. (123.37,194.47) .. controls (92.71,194.47) and (67.87,169.62) .. (67.87,138.97) -- cycle ; 
            		\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.33 ][line width=1.5]  (67.87,138.97) .. controls (67.87,108.31) and (92.71,83.47) .. (123.37,83.47) .. controls (154.02,83.47) and (178.87,108.31) .. (178.87,138.97) .. controls (178.87,169.62) and (154.02,194.47) .. (123.37,194.47) .. controls (92.71,194.47) and (67.87,169.62) .. (67.87,138.97) -- cycle ; 
            		\path  [shading=_93wtyiq23,_df0dg5gmp] (396.87,139.8) .. controls (396.87,114.76) and (417.16,94.47) .. (442.2,94.47) .. controls (467.24,94.47) and (487.53,114.76) .. (487.53,139.8) .. controls (487.53,164.84) and (467.24,185.13) .. (442.2,185.13) .. controls (417.16,185.13) and (396.87,164.84) .. (396.87,139.8) -- cycle ; 
            		\draw  [color={rgb, 255:red, 132; green, 92; blue, 55 }  ,draw opacity=1 ] (396.87,139.8) .. controls (396.87,114.76) and (417.16,94.47) .. (442.2,94.47) .. controls (467.24,94.47) and (487.53,114.76) .. (487.53,139.8) .. controls (487.53,164.84) and (467.24,185.13) .. (442.2,185.13) .. controls (417.16,185.13) and (396.87,164.84) .. (396.87,139.8) -- cycle ; 
            		\path  [shading=_zhztnq9pm,_3dbbylg1k] (407.21,139.8) .. controls (407.21,120.47) and (422.87,104.81) .. (442.2,104.81) .. controls (461.53,104.81) and (477.19,120.47) .. (477.19,139.8) .. controls (477.19,159.13) and (461.53,174.79) .. (442.2,174.79) .. controls (422.87,174.79) and (407.21,159.13) .. (407.21,139.8) -- cycle ; 
            		\draw  [color={rgb, 255:red, 157; green, 121; blue, 92 }  ,draw opacity=1 ] (407.21,139.8) .. controls (407.21,120.47) and (422.87,104.81) .. (442.2,104.81) .. controls (461.53,104.81) and (477.19,120.47) .. (477.19,139.8) .. controls (477.19,159.13) and (461.53,174.79) .. (442.2,174.79) .. controls (422.87,174.79) and (407.21,159.13) .. (407.21,139.8) -- cycle ; 
            		\path  [shading=_4rbf6vmjm,_ihl6ax85b] (409.79,139.9) .. controls (409.79,121.62) and (424.61,106.79) .. (442.9,106.79) .. controls (461.18,106.79) and (476,121.62) .. (476,139.9) .. controls (476,158.18) and (461.18,173) .. (442.9,173) .. controls (424.61,173) and (409.79,158.18) .. (409.79,139.9) -- cycle ; 
            		\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.33 ][line width=1.5]  (409.79,139.9) .. controls (409.79,121.62) and (424.61,106.79) .. (442.9,106.79) .. controls (461.18,106.79) and (476,121.62) .. (476,139.9) .. controls (476,158.18) and (461.18,173) .. (442.9,173) .. controls (424.61,173) and (409.79,158.18) .. (409.79,139.9) -- cycle ; 
            		\draw  [dash pattern={on 4.5pt off 4.5pt}]  (123.37,138.97) -- (441.53,139.13) ;
            		\draw    (123.37,138.97) -- (147.63,67.42) ;
            		\draw    (147.63,210.85) -- (123.37,138.97) ;
            		\draw    (441.53,139.13) -- (430.53,95.47) ;
            		\draw    (432.53,182.8) -- (441.53,139.13) ;
            		\draw    (287.37,153.72) .. controls (279.87,147.6) and (277.87,133.6) .. (285.33,126.33) ;
            		\draw (94,125) node [anchor=north west][inner sep=0.75pt]    {$O_{1}$};
            		\draw (113.33,87.67) node [anchor=north west][inner sep=0.75pt]    {$R$};
            		\draw (442,127.67) node [anchor=north west][inner sep=0.75pt]    {$O_{2}$};
            		\draw (442.2,104.81) node [anchor=north west][inner sep=0.75pt]    {$r$};
            		\draw (264,122) node [anchor=north west][inner sep=0.75pt]    {$\theta $};
            	\end{tikzpicture}
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Một dây curoa mỏng dài $L$ bao quanh hai ròng rọc có bán kính lần lượt là ròng rọc lớn $R$ và ròng rọc nhỏ $r$, vắt chéo nhau tạo thành hình số 8. Giả sử bán kính $R = %s$ cm, bán kính $r = %s$ cm. Biết khoảng cách giữa tâm của hai ròng rọc là $%s$ cm. Tổng chiều dài $L$ của dây curoa bằng bao nhiêu? (Kết quả làm tròn đến hàng đơn vị của cm). %s'''
                                 % (R_val, r_val, d_val, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Khối mã TikZ vẽ hình minh họa

                hinhve1='''\\begin{center}
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                			\\tikzset {_rx4kls2sy/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { -37.5 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                		\\pgfdeclarehorizontalshading{_e1s6yx822}{150bp}{rgb(0bp)=(0.64,0.51,0.31);
                			rgb(37.5bp)=(0.64,0.51,0.31);
                			rgb(50bp)=(0.91,0.82,0.74);
                			rgb(62.5bp)=(0.64,0.54,0.38);
                			rgb(100bp)=(0.64,0.54,0.38)}
                		\\tikzset {_2nvk3ua8r/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { -37.5 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                		\\pgfdeclarehorizontalshading{_v1y7fq01f}{150bp}{rgb(0bp)=(0.43,0.33,0.17);
                			rgb(37.5bp)=(0.43,0.33,0.17);
                			rgb(50bp)=(0.91,0.82,0.74);
                			rgb(62.5bp)=(0.34,0.26,0.13);
                			rgb(100bp)=(0.34,0.26,0.13)}
                		\\tikzset {_hqi1hdrcx/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { -37.5 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                		\\pgfdeclarehorizontalshading{_ylzp0pz7j}{150bp}{rgb(0bp)=(0.64,0.51,0.31);
                			rgb(37.5bp)=(0.64,0.51,0.31);
                			rgb(50bp)=(0.91,0.82,0.74);
                			rgb(62.5bp)=(0.64,0.54,0.38);
                			rgb(100bp)=(0.64,0.54,0.38)}
                		\\tikzset {_0eghhx6sj/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { -37.5 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                		\\pgfdeclarehorizontalshading{_p9wzlzvd9}{150bp}{rgb(0bp)=(0.64,0.51,0.31);
                			rgb(37.5bp)=(0.64,0.51,0.31);
                			rgb(50bp)=(0.91,0.82,0.74);
                			rgb(62.5bp)=(0.64,0.54,0.38);
                			rgb(100bp)=(0.64,0.54,0.38)}
                		\\tikzset {_bk86a8guf/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { -37.5 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                		\\pgfdeclarehorizontalshading{_k0o96shq9}{150bp}{rgb(0bp)=(0.43,0.33,0.17);
                			rgb(37.5bp)=(0.43,0.33,0.17);
                			rgb(50bp)=(0.91,0.82,0.74);
                			rgb(62.5bp)=(0.34,0.26,0.13);
                			rgb(100bp)=(0.34,0.26,0.13)}
                		\\tikzset {_r5v6uxz2x/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { -37.5 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                		\\pgfdeclarehorizontalshading{_f60jen8nf}{150bp}{rgb(0bp)=(0.64,0.51,0.31);
                			rgb(37.5bp)=(0.64,0.51,0.31);
                			rgb(50bp)=(0.91,0.82,0.74);
                			rgb(62.5bp)=(0.64,0.54,0.38);
                			rgb(100bp)=(0.64,0.54,0.38)}
                		\\tikzset{every picture/.style={line width=0.75pt}}  
                		\\draw [color={rgb, 255:red, 21; green, 63; blue, 112 }  ,draw opacity=1 ][line width=3.75]    (147.63,210.85) -- (427.1,96.59) ;
                		\\draw [color={rgb, 255:red, 21; green, 63; blue, 112 }  ,draw opacity=1 ][line width=3.75]    (147.63,67.42) -- (416.57,178.08) ;
                		\\draw  [draw opacity=0][line width=3.75]  (147.63,210.85) .. controls (139.49,213.84) and (130.7,215.47) .. (121.53,215.47) .. controls (79.56,215.47) and (45.53,181.29) .. (45.53,139.13) .. controls (45.53,96.98) and (79.56,62.8) .. (121.53,62.8) .. controls (130.7,62.8) and (139.49,64.43) .. (147.63,67.42) -- (121.53,139.13) -- cycle ; \\draw  [color={rgb, 255:red, 20; green, 61; blue, 110 }  ,draw opacity=1 ][line width=3.75]  (147.63,210.85) .. controls (139.49,213.84) and (130.7,215.47) .. (121.53,215.47) .. controls (79.56,215.47) and (45.53,181.29) .. (45.53,139.13) .. controls (45.53,96.98) and (79.56,62.8) .. (121.53,62.8) .. controls (130.7,62.8) and (139.49,64.43) .. (147.63,67.42) ;  
                		\\draw  [draw opacity=0][line width=3.75]  (427.1,96.59) .. controls (431.44,95.21) and (436.07,94.47) .. (440.87,94.47) .. controls (465.9,94.47) and (486.2,114.76) .. (486.2,139.8) .. controls (486.2,164.84) and (465.9,185.13) .. (440.87,185.13) .. controls (431.93,185.13) and (423.59,182.55) .. (416.57,178.08) -- (440.87,139.8) -- cycle ; \\draw  [color={rgb, 255:red, 22; green, 61; blue, 106 }  ,draw opacity=1 ][line width=3.75]  (427.1,96.59) .. controls (431.44,95.21) and (436.07,94.47) .. (440.87,94.47) .. controls (465.9,94.47) and (486.2,114.76) .. (486.2,139.8) .. controls (486.2,164.84) and (465.9,185.13) .. (440.87,185.13) .. controls (431.93,185.13) and (423.59,182.55) .. (416.57,178.08) ;  
                		\\path  [shading=_e1s6yx822,_rx4kls2sy] (46.2,138.8) .. controls (46.2,96.83) and (80.23,62.8) .. (122.2,62.8) .. controls (164.17,62.8) and (198.2,96.83) .. (198.2,138.8) .. controls (198.2,180.77) and (164.17,214.8) .. (122.2,214.8) .. controls (80.23,214.8) and (46.2,180.77) .. (46.2,138.8) -- cycle ; 
                		\\draw  [color={rgb, 255:red, 132; green, 92; blue, 55 }  ,draw opacity=1 ] (46.2,138.8) .. controls (46.2,96.83) and (80.23,62.8) .. (122.2,62.8) .. controls (164.17,62.8) and (198.2,96.83) .. (198.2,138.8) .. controls (198.2,180.77) and (164.17,214.8) .. (122.2,214.8) .. controls (80.23,214.8) and (46.2,180.77) .. (46.2,138.8) -- cycle ; 
                		\\path  [shading=_v1y7fq01f,_2nvk3ua8r] (63.53,138.8) .. controls (63.53,106.4) and (89.8,80.13) .. (122.2,80.13) .. controls (154.6,80.13) and (180.87,106.4) .. (180.87,138.8) .. controls (180.87,171.2) and (154.6,197.47) .. (122.2,197.47) .. controls (89.8,197.47) and (63.53,171.2) .. (63.53,138.8) -- cycle ; 
                		\\draw  [color={rgb, 255:red, 157; green, 121; blue, 92 }  ,draw opacity=1 ] (63.53,138.8) .. controls (63.53,106.4) and (89.8,80.13) .. (122.2,80.13) .. controls (154.6,80.13) and (180.87,106.4) .. (180.87,138.8) .. controls (180.87,171.2) and (154.6,197.47) .. (122.2,197.47) .. controls (89.8,197.47) and (63.53,171.2) .. (63.53,138.8) -- cycle ; 
                		\\path  [shading=_ylzp0pz7j,_hqi1hdrcx] (67.87,138.97) .. controls (67.87,108.31) and (92.71,83.47) .. (123.37,83.47) .. controls (154.02,83.47) and (178.87,108.31) .. (178.87,138.97) .. controls (178.87,169.62) and (154.02,194.47) .. (123.37,194.47) .. controls (92.71,194.47) and (67.87,169.62) .. (67.87,138.97) -- cycle ; 
                		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.33 ][line width=1.5]  (67.87,138.97) .. controls (67.87,108.31) and (92.71,83.47) .. (123.37,83.47) .. controls (154.02,83.47) and (178.87,108.31) .. (178.87,138.97) .. controls (178.87,169.62) and (154.02,194.47) .. (123.37,194.47) .. controls (92.71,194.47) and (67.87,169.62) .. (67.87,138.97) -- cycle ; 
                		\\path  [shading=_p9wzlzvd9,_0eghhx6sj] (396.87,139.8) .. controls (396.87,114.76) and (417.16,94.47) .. (442.2,94.47) .. controls (467.24,94.47) and (487.53,114.76) .. (487.53,139.8) .. controls (487.53,164.84) and (467.24,185.13) .. (442.2,185.13) .. controls (417.16,185.13) and (396.87,164.84) .. (396.87,139.8) -- cycle ; 
                		\\draw  [color={rgb, 255:red, 132; green, 92; blue, 55 }  ,draw opacity=1 ] (396.87,139.8) .. controls (396.87,114.76) and (417.16,94.47) .. (442.2,94.47) .. controls (467.24,94.47) and (487.53,114.76) .. (487.53,139.8) .. controls (487.53,164.84) and (467.24,185.13) .. (442.2,185.13) .. controls (417.16,185.13) and (396.87,164.84) .. (396.87,139.8) -- cycle ; 
                		\\path  [shading=_k0o96shq9,_bk86a8guf] (407.21,139.8) .. controls (407.21,120.47) and (422.87,104.81) .. (442.2,104.81) .. controls (461.53,104.81) and (477.19,120.47) .. (477.19,139.8) .. controls (477.19,159.13) and (461.53,174.79) .. (442.2,174.79) .. controls (422.87,174.79) and (407.21,159.13) .. (407.21,139.8) -- cycle ; 
                		\\draw  [color={rgb, 255:red, 157; green, 121; blue, 92 }  ,draw opacity=1 ] (407.21,139.8) .. controls (407.21,120.47) and (422.87,104.81) .. (442.2,104.81) .. controls (461.53,104.81) and (477.19,120.47) .. (477.19,139.8) .. controls (477.19,159.13) and (461.53,174.79) .. (442.2,174.79) .. controls (422.87,174.79) and (407.21,159.13) .. (407.21,139.8) -- cycle ; 
                		\\path  [shading=_f60jen8nf,_r5v6uxz2x] (409.79,139.9) .. controls (409.79,121.62) and (424.61,106.79) .. (442.9,106.79) .. controls (461.18,106.79) and (476,121.62) .. (476,139.9) .. controls (476,158.18) and (461.18,173) .. (442.9,173) .. controls (424.61,173) and (409.79,158.18) .. (409.79,139.9) -- cycle ; 
                		\\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.33 ][line width=1.5]  (409.79,139.9) .. controls (409.79,121.62) and (424.61,106.79) .. (442.9,106.79) .. controls (461.18,106.79) and (476,121.62) .. (476,139.9) .. controls (476,158.18) and (461.18,173) .. (442.9,173) .. controls (424.61,173) and (409.79,158.18) .. (409.79,139.9) -- cycle ; 
                		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (123.37,138.97) -- (441.53,139.13) ;
                		\\draw    (123.37,138.97) -- (165.87,26.93) ;
                		\\draw    (147.63,210.85) -- (123.37,138.97) ;
                		\\draw    (441.53,139.13) -- (430.53,95.47) ;
                		\\draw    (424.53,182.27) -- (441.53,139.13) ;
                		\\draw    (287.37,153.72) .. controls (279.87,147.6) and (277.87,133.6) .. (285.33,126.33) ;
                		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (165.87,26.93) -- (442.9,139.9) ;
                		\\draw    (136.7,139.05) .. controls (140.53,132.27) and (137.87,124.27) .. (131.2,121.6) ;
                		\\draw (94,125) node [anchor=north west][inner sep=0.75pt]    {$O_{1}$};
                		\\draw (113.33,87.67) node [anchor=north west][inner sep=0.75pt]    {$R$};
                		\\draw (442,127.67) node [anchor=north west][inner sep=0.75pt]    {$O_{2}$};
                		\\draw (442.2,104.81) node [anchor=north west][inner sep=0.75pt]    {$r$};
                		\\draw (264,122) node [anchor=north west][inner sep=0.75pt]    {$\\theta $};
                		\\draw (142.67,10.67) node [anchor=north west][inner sep=0.75pt]    {$H$};
                		\\draw (132,40.67) node [anchor=north west][inner sep=0.75pt]    {$A$};
                		\\draw (143.33,213) node [anchor=north west][inner sep=0.75pt]    {$A'$};
                		\\draw (412,184.67) node [anchor=north west][inner sep=0.75pt]    {$B$};
                		\\draw (418.67,70.33) node [anchor=north west][inner sep=0.75pt]    {$B'$};
                		\\draw (138.67,104) node [anchor=north west][inner sep=0.75pt]    {$\\alpha $};
                	\\end{tikzpicture}
                \\end{center}'''
                # Nội dung lời giải
                loigiai = ('''Từ tâm $O_2$, kẻ đường thẳng song song với đoạn $AB$. Kéo dài bán kính $O_1A$ cắt đường thẳng vừa kẻ tại $H$\\\\
            %s
            Xét tứ giác $ABO_2H$ có ba góc vuông nên $ABO_2H$ là hình chữ nhật\\\\
            Khi đó: $AH = O_2B = r = %s$ cm và $O_2H = AB$\\\\
            Xét $\\Delta O_1HO_2$ vuông tại $H$ có $O_1H = O_1A + AH = R + r = %s + %s = %s$ cm và $O_1O_2 = d = %s$ cm\\\\
            Áp dụng định lý Pytago trong $\\Delta O_1HO_2$: $O_2H = \\sqrt{O_1O_2^2 - O_1H^2} = \\sqrt{%s^2 - %s^2} = %s$ cm\\\\
            Vì $AB = O_2H$ nên chiều dài một đoạn dây thẳng là $%s$ cm\\\\
            Do có 2 đoạn chéo nhau, tổng chiều dài phần dây thẳng là $%s$ cm và đặt $\\alpha = \\widehat{HO_1O_2}$\\\\
            Xét tam giác vuông $O_1HO_2$, ta có: $\\cos(\\alpha) = \\frac{O_1H}{O_1O_2} = \\frac{%s}{%s} = \\frac{1}{2} \\Rightarrow \\alpha = 60^\\circ = \\frac{\\pi}{3}$ rad (góc này là cung nhỏ) nên góc ở tâm $\\widehat{AO_1A'} = 2\\alpha = 120^\\circ = \\frac{2\\pi}{3}$ rad\\\\
            Vậy góc của phần cung mà dây ôm vào ròng rọc lớn là: $\\varphi_1 = 2\\pi - \\frac{2\\pi}{3} = \\frac{4\\pi}{3}$ rad\\\\
            Mặt khác $O_1A \\perp AB$ và $O_2B \\perp AB$ nên $O_1A // O_2B$\\\\
            Đường thẳng $O_1O_2$ cắt hai đường thẳng song song này tạo ra các góc so le trong bằng nhau\\\\
            Do đó góc hợp bởi bán kính ròng rọc nhỏ và đường nối tâm cũng bằng $\\alpha = 60^\\circ$\\\\
            Tương tự suy ra góc ôm dây trên ròng rọc nhỏ cũng là: $\\varphi_2 = 2\\pi - \\frac{2\\pi}{3} = \\frac{4\\pi}{3}$ rad\\\\
            Chiều dài cung trên ròng rọc lớn: $L_R = R.\\varphi_1 = %s.\\frac{4\\pi}{3} = %s$ cm\\\\
            Chiều dài cung trên ròng rọc nhỏ: $L_r = r.\\varphi_2 = %s.\\frac{4\\pi}{3} = %s$ cm\\\\
            Tổng chiều dài dây curoa $L$ là: $L = L_R + L_r + 2.AB = %s \\approx %s$ cm.'''
                         % ( hinhve1,
                            r_val, 
                            R_val, r_val, sum_Rr, 
                            d_val, 
                            d_val, sum_Rr, latex(AB), 
                            latex(AB), 
                            latex(AB_2), 
                            sum_Rr, d_val, 
                            R_val, latex(L_R), 
                            r_val, latex(L_r), 
                            latex(L_exact), L_rounded))
                dapan='\\shortans[0]{$%s$}\n'%(L_rounded)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{\n' + str(loigiai) + '\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

