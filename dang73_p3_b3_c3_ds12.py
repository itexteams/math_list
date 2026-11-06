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


def bt_dang73_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các cấu hình tạo bài toán ngẫu nhiên (chọn a, xA, xB sao cho hệ số góc đường thẳng AB luôn m=1 để hình vẽ TikZ giữ nguyên tính đối xứng)
                configs = [
                    {'a': sp.Rational(1, 1), 'xA': -1, 'xB': 2},
                    {'a': sp.Rational(1, 2), 'xA': -2, 'xB': 4},
                    #{'a': sp.Rational(1, 1), 'xA': -2, 'xB': 3}
                ]
                cfg = random.choice(configs)
                a_sym = cfg['a']
                xA = cfg['xA']
                xB = cfg['xB']

                yA = a_sym * xA**2
                yB = a_sym * xB**2

                # Hệ số góc m luôn bằng 1, tìm tung độ gốc n của đường thẳng AB
                m = 1
                n = yA - m * xA

                # Tính toán tích phân bằng Sympy
                x_sym = sp.Symbol('x')
                P_expr = a_sym * x_sym**2
                d_expr = x_sym + n

                S1_sym = sp.integrate(d_expr - P_expr, (x_sym, xA, xB))
                S_sym = 8 * S1_sym

                # Định dạng đáp án
                kq = sp.latex(S_sym)
                da = '$%s$' % kq

                # Định dạng các số hiển thị bằng dấu phẩy
                yA_str = str(float(yA)).rstrip('0').rstrip('.') if float(yA).is_integer() else str(float(yA)).replace('.', ',')
                yB_str = str(float(yB)).rstrip('0').rstrip('.') if float(yB).is_integer() else str(float(yB)).replace('.', ',')

                # Chuỗi LaTeX
                P_latex = sp.latex(P_expr)
                d_latex = sp.latex(d_expr)

                # Tạo các đáp án gây nhiễu
                s = ['$%s$' % sp.latex(S_sym + sp.Rational(10, 3)),
                     '$%s$' % sp.latex(S_sym - sp.Rational(10, 3)),
                     '$%s$' % sp.latex(4 * S1_sym), # Học sinh quên nhân 8 mà chỉ nhân 4
                     '$%s$' % sp.latex(S_sym + 12),
                     '$%s$' % sp.latex(S_sym - 12),
                     '$%s$' % sp.latex(S_sym + 6)]

                s_set = []
                for item in s:
                    if item != da and item not in s_set:
                        s_set.append(item)

                random.shuffle(s_set)
                das1 = s_set[0]
                das2 = s_set[1]
                das3 = s_set[2]

                # Giá trị phục vụ vẽ TikZ
                a_val = float(a_sym)
                n_val = float(n)
                xA_val = xA
                xB_val = xB
                yA_val = float(yA)
                yB_val = float(yB)

                ymax = yB_val + 1
                ymin = -1

                # Khởi tạo mã TikZ
                tikz_fig = ('''\\begin{center} \\scalebox{0.8}{ 
            \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (197.37,144.76) .. controls (165.3,281.27) and (133.23,273.45) .. (113.28,229.64) .. controls (72.99,210.87) and (61.25,176.84) .. (197.37,144.76) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (197.37,144.76) .. controls (229.45,8.25) and (261.52,16.07) .. (281.47,59.88) .. controls (321.76,78.66) and (333.49,112.69) .. (197.37,144.76) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (197.37,144.76) .. controls (60.86,112.69) and (68.69,80.61) .. (112.49,60.66) .. controls (131.27,20.37) and (165.3,8.64) .. (197.37,144.76) -- cycle ;
            	\\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (197.37,144.76) .. controls (333.89,176.84) and (326.06,208.91) .. (282.25,228.86) .. controls (263.48,269.15) and (229.45,280.88) .. (197.37,144.76) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (261.73,80.8) .. controls (228,109.05) and (229.73,112.13) .. (197.37,144.76) .. controls (225.73,118.13) and (225.33,115.72) .. (261.73,80.8) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (133.01,208.72) .. controls (166.75,180.47) and (165.01,177.39) .. (197.37,144.76) .. controls (169.01,171.39) and (169.42,173.8) .. (133.01,208.72) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (261.33,209.12) .. controls (233.08,175.38) and (230,177.12) .. (197.37,144.76) .. controls (224,173.12) and (226.42,172.71) .. (261.33,209.12) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.2 ] (133.41,80.4) .. controls (161.67,114.14) and (164.75,112.4) .. (197.37,144.76) .. controls (170.75,116.4) and (168.33,116.81) .. (133.41,80.4) -- cycle ;
            \\end{tikzpicture} \\hspace*{2cm}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,line width=1pt] 
            \\fill[green!30, opacity=0.8] plot[domain=%s:%s, samples=100] (\\x, %s*\\x*\\x) -- plot[domain=%s:%s, samples=100] (%s*\\x*\\x - %s, \\x + %s) -- cycle;
            \\draw[->] (%s, 0) -- (%s, 0) node[below] {$x$};
            \\draw[->] (0, %s) -- (0, %s) node[right] {$y$};
            \\node[below right] at (0,0) {$O$};
            \\draw[dashed] (%s, 0) node[below] {$%s$} -- (%s, %s) -- (0, %s) node[right] {$%s$};
            \\draw[dashed] (%s, 0) node[below] {$%s$} -- (%s, %s) -- (0, %s) node[left] {$%s$};
            \\draw[blue, thick, domain=%s:%s, samples=100] plot (\\x, %s*\\x*\\x);
            \\draw[blue, thick, domain=%s:%s, samples=100] plot (%s*\\x*\\x - %s, \\x + %s);
            \\draw[thick] (%s, %s) -- (%s, %s);
            \\fill (%s, %s) circle (2pt) node[left] {$A$};
            \\fill (%s, %s) circle (2pt) node[right] {$B$};
            \\node at (%s, %s) {$S_1$};
            \\end{tikzpicture}}
            \\end{center}''' % (xA_val, xB_val, a_val, xB_val, xA_val, a_val, n_val, n_val,
                xA_val - 1, xB_val + 1.5, ymin, ymax,
                xA_val, xA_val, xA_val, yA_val, yA_val, yA_str,
                xB_val, xB_val, xB_val, yB_val, yB_val, yB_str,
                xA_val, xB_val, a_val,
                xB_val, xA_val, a_val, n_val, n_val,
                xA_val - 0.5, yA_val - 0.5, xB_val + 0.5, yB_val + 0.5,
                xA_val, yA_val, xB_val, yB_val,
                (xA_val + xB_val)/2 + 0.2, (yA_val + yB_val)/2 - 0.5
                ))

                # Câu hỏi
                noidungcauhoi = ('''Bạn Khôi muốn dùng các đường cong parabol để vẽ một chiếc cỏ 4 lá may mắn như hình minh họa. Mỗi cánh lá là phần được giới hạn bởi hai phần parabol đối xứng nhau qua đường thẳng $AB$ và đặt trong hệ trục tọa độ $Oxy$. Diện tích một cánh lá là phần hình phẳng giới hạn bởi hai phần parabol đó. Diện tích của chiếc cỏ 4 lá bằng bao nhiêu? Biết rằng nó được cấu tạo bởi 4 cánh giống hệt nhau và parabol giới hạn cánh lá đi qua các điểm $A(%s; %s)$, gốc tọa độ $O(0;0)$ và điểm $B(%s; %s)$.\n%s''' % (xA, yA_str, xB, yB_str, tikz_fig))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa đáp án vào danh sách ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ('''Parabol $(P): y = ax^2 + bx + c$ đi qua các điểm $A(%s; %s)$, $O(0;0)$ và $B(%s; %s)$\\\\
            Suy ra $(P): y = %s$\\\\
            Phương trình đường thẳng $AB$ có dạng: $d = mx + n$ đi qua các điểm $A(%s; %s)$ và $B(%s; %s)$\\\\
            Suy ra $d = %s$\\\\
            Vậy diện tích một nửa cánh lá là $S_1 = \\int_{%s}^{%s} \\left[ %s - (%s) \\right] \\mathrm{d}x = %s$\\\\
            Diện tích của cỏ $4$ lá là: $S = 8 \\cdot S_1 = 8 \\cdot %s = %s$ (đvdt).''' % (
                    xA, yA_str, xB, yB_str,
                    P_latex,
                    xA, yA_str, xB, yB_str,
                    d_latex,
                    xA, xB, d_latex, P_latex, sp.latex(S1_sym),
                    sp.latex(S1_sym), kq
                ))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

