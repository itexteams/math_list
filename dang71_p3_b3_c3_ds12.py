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


def bt_dang71_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Các cặp (m, n) tương ứng với nửa đường chéo lớn và nửa đường chéo nhỏ (m > n)
                # được chọn lọc để cạnh hình thoi c = sqrt(m^2 + n^2) luôn là số nguyên.
                pairs = [(40, 30), (60, 45), (80, 60), (120, 50), (150, 80)]
                m, n = random.choice(pairs)

                # Tính toán các thông số cơ bản
                c = int(math.sqrt(m**2 + n**2))
                S = 2 * m * n
                S_half = S // 2
                d1 = 2 * m
                d2 = 2 * n

                # Các phân số và biểu thức cho phương trình
                frac_n_m = sp.Rational(n, m)
                frac_n2_m2 = sp.Rational(n**2, m**2)
                coeff_x = sp.Rational(2 * n**2, m)
                n2 = n**2

                # Định dạng latex cho hệ số của x để tránh lỗi hiển thị khi nó là phân số
                coeff_x_latex = latex(coeff_x)
                if '\\frac' in coeff_x_latex:
                    coeff_x_str = '\\left(' + coeff_x_latex + '\\right)'
                else:
                    coeff_x_str = coeff_x_latex

                # Tính toán cho bất đẳng thức Cosi và đồng nhất hệ số
                g = math.gcd(n**2, m**2)
                coeff_a2 = n**2 // g
                coeff_b2 = m**2 // g
                val_rhs = (m**2 * n**2) // g

                coeff_ab = 2 * int(math.sqrt(coeff_a2 * coeff_b2))
                max_ab = val_rhs // coeff_ab

                # Các thông số của elip
                a2 = m**2 // 2
                b2 = n**2 // 2
                a_val = sp.sqrt(a2)

                # Tính thể tích (đơn vị dm^3)
                coeff_V_dm3 = sp.Rational(m * n**2, 3000)
                V_exact = coeff_V_dm3 * sp.pi * sp.sqrt(2)
                while V_exact>99.9:
                    pairs = [(40, 30), (60, 45), (80, 60), (120, 50), (150, 80)]
                    m, n = random.choice(pairs)

                    # Tính toán các thông số cơ bản
                    c = int(math.sqrt(m**2 + n**2))
                    S = 2 * m * n
                    S_half = S // 2
                    d1 = 2 * m
                    d2 = 2 * n

                    # Các phân số và biểu thức cho phương trình
                    frac_n_m = sp.Rational(n, m)
                    frac_n2_m2 = sp.Rational(n**2, m**2)
                    coeff_x = sp.Rational(2 * n**2, m)
                    n2 = n**2

                    # Định dạng latex cho hệ số của x để tránh lỗi hiển thị khi nó là phân số
                    coeff_x_latex = latex(coeff_x)
                    if '\\frac' in coeff_x_latex:
                        coeff_x_str = '\\left(' + coeff_x_latex + '\\right)'
                    else:
                        coeff_x_str = coeff_x_latex

                    # Tính toán cho bất đẳng thức Cosi và đồng nhất hệ số
                    g = math.gcd(n**2, m**2)
                    coeff_a2 = n**2 // g
                    coeff_b2 = m**2 // g
                    val_rhs = (m**2 * n**2) // g

                    coeff_ab = 2 * int(math.sqrt(coeff_a2 * coeff_b2))
                    max_ab = val_rhs // coeff_ab

                    # Các thông số của elip
                    a2 = m**2 // 2
                    b2 = n**2 // 2
                    a_val = sp.sqrt(a2)

                    # Tính thể tích (đơn vị dm^3)
                    coeff_V_dm3 = sp.Rational(m * n**2, 3000)
                    V_exact = coeff_V_dm3 * sp.pi * sp.sqrt(2)        
                V_approx = float(V_exact)

                # Làm tròn 1 chữ số thập phân
                kq_decimal = Decimal(str(V_approx)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_decimal).replace('.', ',')
                kq4 = float(kq_decimal)

                # Các đáp án trắc nghiệm sai (distractors)
                deltas = [1.2, 2.5, 3.1, -1.3, -2.4, -3.2, 4.5, -4.5]
                random.shuffle(deltas)
                s = []
                for d in deltas:
                    val = round(kq4 + d, 1)
                    if val > 0:
                        s.append('$%s$' % str(val).replace('.', ','))

                da = '$%s$' % kq
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung câu hỏi (Đã bỏ hình vẽ và chữ "xem hình vẽ")
                noidungcauhoi = ('''Một chiếc lồng đèn gồm chiếc lồng bên ngoài được thiết kế có dạng hai hình nón giống hệt nhau lại chụm lại, bên trong là một lòng giấy màu cam để thắp đèn. Thiết diện cắt dọc của lồng đèn này đi qua đỉnh của hai nón và tâm của đáy chung là một hình thoi và lòng giấy màu cam bên trong là một hình elip.
                                 \\begin{center}
                                 	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                 			\\tikzset {_1ednc7uep/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformscale{1 }  }}}
                                 		\\pgfdeclareradialshading{_bd3in32px}{\\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
                                 			rgb(0bp)=(1,1,1);
                                 			rgb(25bp)=(0.96,0.65,0.14);
                                 			rgb(400bp)=(0.96,0.65,0.14)}
                                 		\\tikzset{every picture/.style={line width=0.75pt}} 
                                 		\\path  [shading=_bd3in32px,_1ednc7uep] (89.85,146.65) .. controls (89.85,99.87) and (115.15,61.95) .. (146.35,61.95) .. controls (177.55,61.95) and (202.85,99.87) .. (202.85,146.65) .. controls (202.85,193.43) and (177.55,231.35) .. (146.35,231.35) .. controls (115.15,231.35) and (89.85,193.43) .. (89.85,146.65) -- cycle ;  
                                 		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (89.85,146.65) .. controls (89.85,99.87) and (115.15,61.95) .. (146.35,61.95) .. controls (177.55,61.95) and (202.85,99.87) .. (202.85,146.65) .. controls (202.85,193.43) and (177.55,231.35) .. (146.35,231.35) .. controls (115.15,231.35) and (89.85,193.43) .. (89.85,146.65) -- cycle ; 
                                 		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (146.1,25.4) -- (226.6,144.5) -- (66.5,144.5) -- cycle ;
                                 		\\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (146.6,267.9) -- (66.5,144.5) -- (226.6,144.5) -- cycle ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.1,25.4) -- (146.6,267.9) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.1,25.4) -- (187.1,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (187.1,144.4) -- (146.6,267.9) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.1,25.4) -- (103.6,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (103.6,144.4) -- (146.6,267.9) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.1,25.4) -- (86.1,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (86.1,144.4) -- (146.6,267.9) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.1,25.4) -- (125.1,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (125.1,144.4) -- (146.6,267.9) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.1,25.4) -- (164.6,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (164.6,144.4) -- (146.6,267.9) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (206.6,143.4) -- (146.6,267.9) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (206.6,143.4) -- (146.1,25.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (216.6,144.4) -- (146.1,25.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (196.6,144.4) -- (146.1,25.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (175.1,144.9) -- (146.1,25.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (155.1,144.4) -- (146.1,25.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (135.6,144.4) -- (146.1,25.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (113.6,144.9) -- (146.1,25.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (95.6,144.4) -- (146.1,25.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (76.6,144.4) -- (146.1,25.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.6,267.9) -- (216.6,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.6,267.9) -- (196.6,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.6,267.9) -- (175.1,144.9) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.6,267.9) -- (155.1,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.6,267.9) -- (135.6,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.6,267.9) -- (113.6,144.9) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.6,267.9) -- (95.6,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (146.6,267.9) -- (76.6,144.4) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (95.5,101) -- (199.1,101) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (94,189) -- (197.6,189) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (108,82.5) -- (185.1,82.5) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (107.7,208.9) -- (184.6,210) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (120.5,63) -- (172.1,63) ;
                                 		\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ]   (121,227) -- (172.6,227) ;
                                 		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (413.05,87.95) .. controls (459.83,87.95) and (497.75,113.25) .. (497.75,144.45) .. controls (497.75,175.65) and (459.83,200.95) .. (413.05,200.95) .. controls (366.27,200.95) and (328.35,175.65) .. (328.35,144.45) .. controls (328.35,113.25) and (366.27,87.95) .. (413.05,87.95) -- cycle ;
                                 		\\draw  [line width=1]  (415.2,64.6) -- (534.3,144.2) -- (415.2,224.7) -- (291.8,144.7) -- cycle ;
                                 	\\end{tikzpicture}
                                 \\end{center}
                                 Biết hình thoi này có cạnh bằng $%s$ cm và có diện tích là $%s$ cm$^2$. Người ta muốn thiết kế phần lòng giấy màu cam sao cho diện tích hình elip là lớn nhất (lòng giấy màu cam là khối tròn xoay khi quay hình elip quanh trục lớn của nó). Khi đó, phần lòng giấy màu cam ấy có thể tích bằng bao nhiêu deximet khối? (làm tròn kết quả đến hàng phần chục).''' % (c, S))

                # Nội dung lời giải (Đã bỏ hình vẽ và thêm mô tả hệ trục tọa độ)
                loigiai = ('''\\begin{center}
                	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                		\\draw [line width=1]    (113.2,142.03) -- (371.87,142.03) ;
                		\\draw [shift={(375.87,142.03)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                		\\draw [line width=1]    (220.53,168.8) -- (220.53,40.13) ;
                		\\draw [shift={(220.53,36.13)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                		\\draw  [draw opacity=0][line width=1]  (134,142.13) .. controls (134,141.94) and (134,141.74) .. (134,141.54) .. controls (134,110.2) and (171.85,84.8) .. (218.54,84.8) .. controls (265.23,84.8) and (303.08,110.2) .. (303.08,141.54) .. controls (303.08,141.96) and (303.08,142.38) .. (303.06,142.8) -- (218.54,141.54) -- cycle ; \\draw  [line width=1]  (134,142.13) .. controls (134,141.94) and (134,141.74) .. (134,141.54) .. controls (134,110.2) and (171.85,84.8) .. (218.54,84.8) .. controls (265.23,84.8) and (303.08,110.2) .. (303.08,141.54) .. controls (303.08,141.96) and (303.08,142.38) .. (303.06,142.8) ;  
                		\\draw [line width=1]    (220.53,61.93) -- (339.63,141.53) ;
                		\\draw (198.67,142.33) node [anchor=north west][inner sep=0.75pt]    {$O$};
                		\\draw (356.67,155) node [anchor=north west][inner sep=0.75pt]    {$x$};
                		\\draw (201.33,32.67) node [anchor=north west][inner sep=0.75pt]    {$y$};
                	\\end{tikzpicture}
                \\end{center}
                Gọi $d_1, d_2$ lần lượt là đường chéo lớn và đường chéo nhỏ của hình thoi ($0 < d_2 < d_1$), khi đó ta có hệ phương trình sau: $\\left(\\frac{d_1}{2}\\right)^2 + \\left(\\frac{d_2}{2}\\right)^2 = %s^2; \\frac{d_1}{2} \\cdot \\frac{d_2}{2} = %s \\Leftrightarrow \\begin{cases} d_1 = %s \\\\ d_2 = %s \\end{cases}$.\\\\
            Chọn hệ trục tọa độ sao cho tâm hình thoi trùng với gốc tọa độ $O$, hai đường chéo nằm trên hai trục tọa độ. Do tính đối xứng, ta chỉ cần tìm diện tích lớn nhất của $\\frac{1}{4}$ hình elip ở góc phần tư thứ nhất.\\\\
            Xét phương trình cạnh hình thoi ở góc phần tư thứ nhất là $y = -%s x + %s, 0 \\le x \\le %s$ và phương trình elip ở góc phần tư thứ nhất là $y = \\sqrt{b^2\\left(1 - \\frac{x^2}{a^2}\\right)}, 0 \\le x \\le a$.\\\\
            Khi đó ta có đánh giá sau: $\\sqrt{b^2\\left(1 - \\frac{x^2}{a^2}\\right)} \\le -%s x + %s \\Leftrightarrow b^2\\left(1 - \\frac{x^2}{a^2}\\right) \\le \\left(%s - %s x\\right)^2$\\\\
            Bất phương trình tương đương với: $\\left(%s + \\frac{b^2}{a^2}\\right)x^2 - %s x + %s - b^2 \\ge 0 \\quad (*)$\\\\
            $(*)$ luôn đúng khi và chỉ khi $\\Delta = %s^2 - 4\\left(%s + \\frac{b^2}{a^2}\\right)(%s - b^2) \\le 0 \\Leftrightarrow %s \\ge %s a^2 + %s b^2$\\\\
            Theo bất đẳng thức Cosi ta có: $%s \\ge %s a^2 + %s b^2 \\ge %s ab \\Leftrightarrow ab \\le %s \\Rightarrow S_{(E)} \\le %s \\pi$\\\\
            Dấu bằng xảy ra khi và chỉ khi $\\begin{cases} %s a^2 = %s b^2 \\\\ %s a^2 + %s b^2 = %s \\end{cases} \\Leftrightarrow \\begin{cases} a^2 = %s \\\\ b^2 = %s \\end{cases} \\Rightarrow (E): y = \\sqrt{%s\\left(1 - \\frac{x^2}{%s}\\right)}$\\\\
            Vậy thể tích cần tìm là $V = \\pi \\int_{-%s}^{%s} \\left( \\sqrt{%s\\left(1 - \\frac{x^2}{%s}\\right)} \\right)^2 \\text{d}x \\approx %s \\text{ (dm}^3)$''' % (
                    c, S_half, d1, d2, 
                    latex(frac_n_m), n, m, 
                    latex(frac_n_m), n, n, latex(frac_n_m), 
                    latex(frac_n2_m2), latex(coeff_x), n2, 
                    coeff_x_str, latex(frac_n2_m2), n2, val_rhs, coeff_a2, coeff_b2, 
                    val_rhs, coeff_a2, coeff_b2, coeff_ab, max_ab, max_ab, 
                    coeff_a2, coeff_b2, coeff_a2, coeff_b2, val_rhs, a2, b2, 
                    b2, a2, 
                    latex(a_val), latex(a_val), b2, a2, kq
                ))
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

