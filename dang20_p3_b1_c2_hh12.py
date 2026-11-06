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


def bt_dang20_p3_b1_c2_hh12(self):
            # Khai báo biến
            # Vòng lặp random để đảm bảo số liệu hợp lệ (Delta > 0 và kết quả khoảng cách có nghĩa)
            while True:
                k = random.randint(8, 15)
                m = k + random.randint(0, 2)
                n = m + random.randint(0, 2)
                p = n + random.randint(0, 2)

                Q = m**2 + n**2 + p**2
                S = m + n + p
                A_coeff = Q - k**2
                S2 = 2 * S

                delta_prime = S**2 - 3 * A_coeff

                if delta_prime > 0:
                    h_val = (S - math.sqrt(delta_prime)) / 3
                    if 0 < h_val < min(m, n, p):
                        break

            # Xử lý các biểu thức toán học
            sqrt_delta_latex = latex(sp.sqrt(delta_prime))
            final_exact_latex = "\\frac{%s - %s}{3}" % (S, sqrt_delta_latex)

            # Tính toán kết quả số thập phân xấp xỉ
            kq_dec = Decimal(float(h_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kq = str(kq_dec).replace('.', ',')

            # Tạo danh sách các đáp án sai
            w_pool = [
                h_val + random.uniform(0.1, 0.5),
                abs(h_val - random.uniform(0.1, 0.5)),
                h_val + random.uniform(0.6, 1.2),
                abs(h_val - random.uniform(0.6, 1.2)),
                (S + math.sqrt(delta_prime)) / 3
            ]

            s_opts = []
            for w in w_pool:
                w_dec = Decimal(float(w)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                w_str = str(w_dec).replace('.', ',')
                if w_str != kq and w_str not in s_opts:
                    s_opts.append(w_str)

            random.shuffle(s_opts)
            das1 = s_opts[0]
            das2 = s_opts[1]
            das3 = s_opts[2]
            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_on54dsw7v/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { -4 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_6x8tmqzlz}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.97,0.91,0.11);
            		rgb(0bp)=(0.97,0.91,0.11);
            		rgb(25bp)=(0.31,0.89,0.76);
            		rgb(400bp)=(0.31,0.89,0.76)}
            	\tikzset {_pb9bu15g3/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { -0.5 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_0fq3omo2j}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.97,0.91,0.11);
            		rgb(0bp)=(0.97,0.91,0.11);
            		rgb(25bp)=(0.31,0.82,0.89);
            		rgb(400bp)=(0.31,0.82,0.89)}
            	\tikzset {_o40u2wuq2/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_etdhnkwhd}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(0.97,0.91,0.11);
            		rgb(0bp)=(0.97,0.91,0.11);
            		rgb(25bp)=(0.31,0.89,0.76);
            		rgb(400bp)=(0.31,0.89,0.76)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\draw  [fill={rgb, 255:red, 91; green, 9; blue, 64 }  ,fill opacity=1 ] (125.6,61.9) -- (164.6,52.9) -- (189.6,62.9) -- (153.12,70.56) -- cycle ;
            	\draw  [fill={rgb, 255:red, 78; green, 9; blue, 91 }  ,fill opacity=1 ] (125.12,56.56) -- (164.32,46.56) -- (164.6,52.9) -- (125.6,61.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 52; green, 2; blue, 62 }  ,fill opacity=1 ] (164.32,46.56) -- (189.52,56.96) -- (189.6,62.9) -- (164.6,52.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 91; green, 9; blue, 65 }  ,fill opacity=1 ] (154.8,63) -- (159.12,63) -- (159.12,103) -- (154.8,103) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 35; blue, 89 }  ,fill opacity=1 ] (95.12,187.36) -- (158.72,172.16) -- (158.32,93.76) -- (95.12,116.96) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 83; blue, 35 }  ,fill opacity=1 ] (158.72,172.16) -- (215.12,188.96) -- (214.72,118.16) -- (158.32,93.76) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 35; blue, 104 }  ,fill opacity=1 ] (154.32,203.36) -- (215.12,188.96) -- (158.72,172.16) -- (95.12,187.36) -- cycle ;
            	\draw [color={rgb, 255:red, 164; green, 14; blue, 89 }  ,draw opacity=1 ]   (164.6,52.9) -- (125.6,61.9) ;
            	\draw [color={rgb, 255:red, 164; green, 14; blue, 89 }  ,draw opacity=1 ]   (189.6,62.9) -- (164.6,52.9) ;
            	\path  [shading=_6x8tmqzlz,_on54dsw7v] (99.52,181.76) -- (154.72,168.16) -- (154.32,100.16) -- (99.52,119.76) -- cycle ; 
            	\draw   (99.52,181.76) -- (154.72,168.16) -- (154.32,100.16) -- (99.52,119.76) -- cycle ;
            	\path  [shading=_0fq3omo2j,_pb9bu15g3] (163.52,168.96) -- (211.92,183.36) -- (211.52,120.56) -- (162.72,100.16) -- cycle ; 
            	\draw   (163.52,168.96) -- (211.92,183.36) -- (211.52,120.56) -- (162.72,100.16) -- cycle ; 
            	\path  [shading=_etdhnkwhd,_o40u2wuq2] (154.4,200.96) -- (205.6,188.96) -- (158.8,176.16) -- (105.2,188.16) -- cycle ; 
            	\draw   (154.4,200.96) -- (205.6,188.96) -- (158.8,176.16) -- (105.2,188.16) -- cycle ; 
            	\draw  [fill={rgb, 255:red, 245; green, 35; blue, 126 }  ,fill opacity=1 ] (100,140.16) -- (154.4,122.56) -- (154.32,117.76) -- (99.2,136.56) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 83; blue, 35 }  ,fill opacity=1 ] (163.6,123.36) -- (212,141.76) -- (212.4,138.16) -- (163.52,118.56) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (126.45,138.91) -- (130.64,146.91) -- (140.08,146.03) -- (133.23,154.75) -- (134.81,164.28) -- (126.37,161.66) -- (117.91,168.43) -- (119.56,158.1) -- (112.75,152.75) -- (122.2,148.98) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ,even odd rule] (110.8,154.08) .. controls (112.75,144.02) and (121.32,135.86) .. (129.93,135.86) .. controls (138.55,135.86) and (143.95,144.02) .. (142,154.08) .. controls (140.05,164.14) and (131.48,172.3) .. (122.87,172.3) .. controls (114.25,172.3) and (108.85,164.14) .. (110.8,154.08)(108.4,154.08) .. controls (110.61,142.69) and (120.46,133.46) .. (130.4,133.46) .. controls (140.34,133.46) and (146.61,142.69) .. (144.4,154.08) .. controls (142.19,165.47) and (132.34,174.7) .. (122.4,174.7) .. controls (112.46,174.7) and (106.19,165.47) .. (108.4,154.08) ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (188.18,138.72) -- (192.28,148.64) -- (201.17,150.84) -- (194.85,157.85) -- (196.51,168.54) -- (188.51,162.96) -- (180.65,167.36) -- (182.02,156.9) -- (175.5,148.93) -- (184.34,148.05) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ,even odd rule] (172.8,154.88) .. controls (171.02,144.82) and (176.57,136.66) .. (185.18,136.66) .. controls (193.8,136.66) and (202.22,144.82) .. (204,154.88) .. controls (205.78,164.94) and (200.23,173.1) .. (191.62,173.1) .. controls (183,173.1) and (174.58,164.94) .. (172.8,154.88)(170.4,154.88) .. controls (168.39,143.49) and (174.82,134.26) .. (184.76,134.26) .. controls (194.7,134.26) and (204.39,143.49) .. (206.4,154.88) .. controls (208.41,166.27) and (201.98,175.5) .. (192.04,175.5) .. controls (182.1,175.5) and (172.41,166.27) .. (170.4,154.88) ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (103.2,145.78) .. controls (103.42,144.22) and (104.5,142.96) .. (105.6,142.96) .. controls (106.7,142.96) and (107.42,144.22) .. (107.2,145.78) .. controls (106.98,147.34) and (105.9,148.6) .. (104.8,148.6) .. controls (103.7,148.6) and (102.98,147.34) .. (103.2,145.78) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (146,131.78) .. controls (146.22,130.22) and (147.3,128.96) .. (148.4,128.96) .. controls (149.5,128.96) and (150.22,130.22) .. (150,131.78) .. controls (149.78,133.34) and (148.7,134.6) .. (147.6,134.6) .. controls (146.5,134.6) and (145.78,133.34) .. (146,131.78) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (166.4,133.78) .. controls (166.4,132.22) and (167.3,130.96) .. (168.4,130.96) .. controls (169.5,130.96) and (170.4,132.22) .. (170.4,133.78) .. controls (170.4,135.34) and (169.5,136.6) .. (168.4,136.6) .. controls (167.3,136.6) and (166.4,135.34) .. (166.4,133.78) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (205.6,146.98) .. controls (205.6,145.42) and (206.5,144.16) .. (207.6,144.16) .. controls (208.7,144.16) and (209.6,145.42) .. (209.6,146.98) .. controls (209.6,148.54) and (208.7,149.8) .. (207.6,149.8) .. controls (206.5,149.8) and (205.6,148.54) .. (205.6,146.98) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (103.6,173.78) .. controls (103.82,172.22) and (104.9,170.96) .. (106,170.96) .. controls (107.1,170.96) and (107.82,172.22) .. (107.6,173.78) .. controls (107.38,175.34) and (106.3,176.6) .. (105.2,176.6) .. controls (104.1,176.6) and (103.38,175.34) .. (103.6,173.78) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (147.2,162.98) .. controls (147.42,161.42) and (148.5,160.16) .. (149.6,160.16) .. controls (150.7,160.16) and (151.42,161.42) .. (151.2,162.98) .. controls (150.98,164.54) and (149.9,165.8) .. (148.8,165.8) .. controls (147.7,165.8) and (146.98,164.54) .. (147.2,162.98) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (166.4,163.78) .. controls (166.4,162.22) and (167.3,160.96) .. (168.4,160.96) .. controls (169.5,160.96) and (170.4,162.22) .. (170.4,163.78) .. controls (170.4,165.34) and (169.5,166.6) .. (168.4,166.6) .. controls (167.3,166.6) and (166.4,165.34) .. (166.4,163.78) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ] (205.6,176.18) .. controls (205.6,174.62) and (206.5,173.36) .. (207.6,173.36) .. controls (208.7,173.36) and (209.6,174.62) .. (209.6,176.18) .. controls (209.6,177.74) and (208.7,179) .. (207.6,179) .. controls (206.5,179) and (205.6,177.74) .. (205.6,176.18) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (104.44,121.46) -- (148.42,105.53) -- (148.3,116.74) -- (104.32,132.67) -- cycle(146.93,107.75) -- (105.9,122.6) -- (105.82,130.45) -- (146.84,115.59) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (205.94,120.67) -- (206.29,131.01) -- (168.17,116.95) -- (167.82,106.61) -- cycle(204.66,128.88) -- (204.42,121.64) -- (169.44,108.74) -- (169.69,115.98) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ,even odd rule] (127.88,189.16) .. controls (127.88,185.89) and (140.65,183.24) .. (156.4,183.24) .. controls (172.15,183.24) and (184.92,185.89) .. (184.92,189.16) .. controls (184.92,192.43) and (172.15,195.08) .. (156.4,195.08) .. controls (140.65,195.08) and (127.88,192.43) .. (127.88,189.16)(126.4,189.16) .. controls (126.4,185.07) and (139.83,181.76) .. (156.4,181.76) .. controls (172.97,181.76) and (186.4,185.07) .. (186.4,189.16) .. controls (186.4,193.25) and (172.97,196.56) .. (156.4,196.56) .. controls (139.83,196.56) and (126.4,193.25) .. (126.4,189.16) ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (142,189.36) .. controls (142,188.03) and (148.45,186.96) .. (156.4,186.96) .. controls (164.35,186.96) and (170.8,188.03) .. (170.8,189.36) .. controls (170.8,190.69) and (164.35,191.76) .. (156.4,191.76) .. controls (148.45,191.76) and (142,190.69) .. (142,189.36) -- cycle ;
            \end{tikzpicture}'''
            # Câu hỏi
            noidungcauhoi = (r'''\immini{Trong không gian với hệ trục tọa độ $Oxyz$, người ta treo một quả lồng đèn có dạng một hình lập phương $ABCD.A'B'C'D'$ cạnh bằng $%s$ cm sao cho điểm $A$ gần mặt đất nhất (xem hình vẽ). Biết rằng các đỉnh $B, D, A'$ kề điểm $A$ lần lượt cách mặt đất $%s$ cm; $%s$ cm và $%s$ cm. Hỏi đỉnh $A$ cách mặt đất bao nhiêu centimet? (Kết quả làm tròn đến hàng phần trăm).}{%s}''' % (k, m, n, p, hinhve))

            # Các đáp án
            da_d = ('\\True $%s$' % kq)
            da_s1 = '$%s$' % das1
            da_s2 = '$%s$' % das2
            da_s3 = '$%s$' % das3

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải bám sát y hệt ảnh
            loigiai = ('''\\textbf{Nhận xét ban đầu:} Ta thấy bốn đỉnh $B,D,A'$ và $A$ tạo thành một tam diện vuông bên trong hình lập phương $ABCD.A'B'C'D'$ nên ta có thể chọn hệ trục tọa độ $Oxyz$ với điểm $A$ trùng với gốc tọa độ và các trục $Ox,Oy,Oz$ lần lượt trùng với các cạnh $OB,OD,OA'$ như hình vẽ dưới đây
            \\begin{center}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\draw (-2,-1) -- (4,-1) -- (5,0) -- (-1,0) -- cycle;
                \\node at (-2,-0.5) {$P$};
                \\coordinate (A) at (1,2);
                \\coordinate (B) at (-0.5,3.5);
                \\coordinate (D) at (4,2.5);
                \\coordinate (A') at (1.5,5);
                \\coordinate (C) at ($(B)+(D)-(A)$);
                \\coordinate (B') at ($(B)+(A')-(A)$);
                \\coordinate (D') at ($(D)+(A')-(A)$);
                \\coordinate (C') at ($(C)+(A')-(A)$);
                \\draw[->, blue] (A) -- ($(A)!1.5!(B)$) node[left] {$x$};
                \\draw[->, blue] (A) -- ($(A)!1.5!(D)$) node[right] {$y$};
                \\draw[->, blue, dashed] (A) -- ($(A)!1.3!(A')$) node[right] {$z$};
                \\draw[dashed] (A) -- (A');
                \\draw[dashed] (A') -- (B');
                \\draw[dashed] (A') -- (D');
                \\draw (A) node[below] {$A \\equiv O$} -- (B) node[left] {$B$} -- (C) -- (D) node[below] {$D$} -- cycle;
                \\draw (B) -- (B');
                \\draw (C) -- (C');
                \\draw (D) -- (D');
                \\draw (B') -- (C') -- (D');
            	\\draw[dashed] (B') -- (D');
                \\draw (2.3,6) -- (2.3,8);
                \\draw[fill=blue!30] (1,8) rectangle (3.6, 8.2);
            \\end{tikzpicture}
            \\end{center}
            Suy ra các tọa độ: $A(0;0;0),B(%s;0;0),D(0;%s;0),A'(0;0;%s)$ \\\\
            Khi đó ta gọi $(P): ax+by+cz+d=0$ và chọn $d=%s$, ta có: $(P): ax+by+cz+%s=0$ \\\\
            Từ đây lần lượt có được như sau: (với $a,b,c \\in \\mathbb{R}^*$). \\\\
            $d(B;(P)) = \\frac{|%sa+%s|}{\\sqrt{a^2+b^2+c^2}} = %s;\\\\ d(D;(P)) = \\frac{|%sb+%s|}{\\sqrt{a^2+b^2+c^2}} = %s; \\\\d(A';(P)) = \\frac{|%sc+%s|}{\\sqrt{a^2+b^2+c^2}} = %s$ \\\\
            Đặt $t = \\sqrt{a^2+b^2+c^2}$, khi ấy ta có dãy tỉ lệ thức sau:\\\\ $\\frac{a+1}{%s} = \\frac{b+1}{%s} = \\frac{c+1}{%s} = t \\Rightarrow \\begin{cases} a = %st-1 \\\\ b = %st-1 \\\\ c = %st-1 \\end{cases}$ \\\\
            Suy ra $t = \\sqrt{a^2+b^2+c^2} = \\sqrt{(%st-1)^2 + (%st-1)^2 + (%st-1)^2} = \\sqrt{%st^2 - %st + 3}$ \\\\
            Khi ấy ta có phương trình: $d(B;(P)) = \\frac{|%sa+%s|}{\\sqrt{a^2+b^2+c^2}} = \\frac{|%st|}{\\sqrt{%st^2 - %st + 3}} = %s$ \\\\
            $\\Leftrightarrow %st^2 - %st + 3 = 0 \\Leftrightarrow t = t_0 = \\frac{%s + %s}{%s}$. \\\\
            Vậy ta suy ra khoảng cần tìm là: $d(A;(P)) = \\left. \\frac{|%s|}{\\sqrt{%st^2 - %st + 3}} \\right|_{t=t_0} = %s \\approx %s \\text{ (cm)}$'''
            % (k, k, k,
               k, k,
               k, k, m, k, k, n, k, k, p,
               m, n, p, m, n, p,
               m, n, p, Q, S2,
               k, k, k*m, Q, S2, m,
               A_coeff, S2, S, sqrt_delta_latex, A_coeff,
               k, Q, S2, final_exact_latex, kq)
            )
            dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

