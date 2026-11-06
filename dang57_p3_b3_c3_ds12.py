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


def bt_dang57_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các thông số bài toán
                # a là hệ số bậc 3, xb là hoành độ điểm B (đỉnh cánh hoa)
                a, xb = random.choice([(1, 2), (2, 2), (1, 3)])
                xa = 1
                # Tính tung độ điểm A sao cho A nằm trên đồ thị nhánh trên
                ya = a * xa * (xa - xb)**2 + xa

                # Tính hệ số b, c để hàm số y = f(x) tiếp xúc y = x tại x = xb và qua O(0,0)
                b = -2 * a * xb
                c = a * xb**2 + 1

                # Random số cánh hoa và bán kính nhụy
                N = random.choice([4, 5, 6, 8])
                R_choices = [(0.5, "0,5", Rational(1, 4)), (1.0, "1", Rational(1, 1)), (1.5, "1,5", Rational(9, 4))]
                R, R_str, R_sq = random.choice(R_choices)

                # Hàm số f(x)
                x = symbols('x')
                fx = a*x**3 + b*x**2 + c*x
                fx_latex = latex(fx)

                # Tính toán diện tích
                S_canh = Rational(a * xb**4, 6) # Diện tích 1 cánh
                S2_expr = Rational(a * xb**4, 12) # Diện tích nhánh trên
                S3_expr = 2 * S2_expr
                S_exact_expr = N * S_canh + R_sq * pi
                S_float = float(S_exact_expr.evalf())

                # Làm tròn đến hàng phần chục
                kq3 = Decimal(str(S_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                # Các đáp án trắc nghiệm nhiễu
                kq_val = float(kq3)
                wrong_candidates = [
                    round(kq_val + 0.1, 1),
                    round(kq_val - 0.1, 1),
                    round(kq_val + 1.0, 1),
                    round(kq_val - 1.0, 1),
                    round(kq_val + 2.0, 1),
                    round(kq_val - 2.0, 1),
                    round(kq_val + 0.2, 1),
                    round(kq_val - 0.2, 1),
                ]
                # Loại bỏ các đáp án trùng lặp với đáp án đúng
                wrong_candidates = list(set([w for w in wrong_candidates if abs(w - kq_val) > 0.01]))
                random.shuffle(wrong_candidates)

                du = ['$%s$' % (kq)]
                da = du[0]

                s = ['$%s$' % str(w).replace('.', ',') for w in wrong_candidates[:6]]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_ec1esj7m5/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_wbd4dhxj5}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.98,0.58,0.73);
            		rgb(400bp)=(0.98,0.58,0.73)}
            	\tikzset {_6uha1qo6t/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_cumy26qx2}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.95,0.38,0.62);
            		rgb(400bp)=(0.95,0.38,0.62)}
            	\tikzset {_7m9fdj1i3/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_kb9ot5t6p}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.98,0.58,0.73);
            		rgb(400bp)=(0.98,0.58,0.73)}
            	\tikzset {_7sr85usei/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_ol5u8xk6m}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.95,0.38,0.62);
            		rgb(400bp)=(0.95,0.38,0.62)}
            	\tikzset {_e5s7gljq2/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_6sri8i37c}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.98,0.58,0.73);
            		rgb(400bp)=(0.98,0.58,0.73)}
            	\tikzset {_pze6mpq38/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_hiuurmzl2}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.95,0.38,0.62);
            		rgb(400bp)=(0.95,0.38,0.62)}
            	\tikzset {_iwgjxrc6b/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_6lb5tp2xq}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.98,0.58,0.73);
            		rgb(400bp)=(0.98,0.58,0.73)}
            	\tikzset {_8ikm3z2jx/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_goy0jixdl}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.95,0.38,0.62);
            		rgb(400bp)=(0.95,0.38,0.62)}
            	\tikzset {_7ds2d3dgm/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_813w294wq}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.98,0.58,0.73);
            		rgb(400bp)=(0.98,0.58,0.73)}
            	\tikzset {_u026d9lrc/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_d4lg91t2t}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.95,0.38,0.62);
            		rgb(400bp)=(0.95,0.38,0.62)}
            	\tikzset {_tme77zkul/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformscale{1 }  }}}
            	\pgfdeclareradialshading{_hck9fb9dd}{\pgfpoint{0bp}{0bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(25bp)=(0.97,0.91,0.11);
            		rgb(400bp)=(0.97,0.91,0.11)}
            	\tikzset{every picture/.style={line width=0.75pt}} 
            	\draw    (55,151) -- (286.3,150.9) ;
            	\draw [shift={(289.3,150.9)}, rotate = 179.98] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (10.72,-5.15) -- (0,0) -- (10.72,5.15) -- (7.12,0) -- cycle    ;
            	\draw    (170.3,256.9) -- (170.79,45.9) ;
            	\draw [shift={(170.8,42.9)}, rotate = 90.13] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (10.72,-5.15) -- (0,0) -- (10.72,5.15) -- (7.12,0) -- cycle    ;
            	\path  [shading=_wbd4dhxj5,_ec1esj7m5] (169.88,149.9) .. controls (175.31,116.06) and (187.6,88.4) .. (197.13,82.9) .. controls (217.6,70.4) and (221.13,94.4) .. (248.13,80.4) .. controls (234.27,92.4) and (250.93,107.73) .. (247.13,118.9) .. controls (237.93,142.4) and (185.27,146.4) .. (169.88,149.9) -- cycle ; 
            	\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (169.88,149.9) .. controls (175.31,116.06) and (187.6,88.4) .. (197.13,82.9) .. controls (217.6,70.4) and (221.13,94.4) .. (248.13,80.4) .. controls (234.27,92.4) and (250.93,107.73) .. (247.13,118.9) .. controls (237.93,142.4) and (185.27,146.4) .. (169.88,149.9) -- cycle ;
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=0.22 ][shading=_cumy26qx2,_6uha1qo6t]   (248.13,80.4) -- (169.88,149.9) ;
            	\path  [shading=_kb9ot5t6p,_7m9fdj1i3] (167.33,153.6) .. controls (200.23,143.98) and (237.87,146.48) .. (246.93,152.73) .. controls (267.01,165.86) and (245.27,176.73) .. (267.15,195.18) .. controls (250.36,187.81) and (239.65,206.37) .. (227.93,207.73) .. controls (202.76,209.51) and (177.1,165.99) .. (167.33,153.6) -- cycle ; 
            	\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (167.33,153.6) .. controls (200.23,143.98) and (237.87,146.48) .. (246.93,152.73) .. controls (267.01,165.86) and (245.27,176.73) .. (267.15,195.18) .. controls (250.36,187.81) and (239.65,206.37) .. (227.93,207.73) .. controls (202.76,209.51) and (177.1,165.99) .. (167.33,153.6) -- cycle ; 
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=0.22 ][shading=_ol5u8xk6m,_7sr85usei]   (267.15,195.18) -- (170.79,154.32) ;
            	\path  [shading=_6sri8i37c,_e5s7gljq2] (169.99,151.46) .. controls (188.27,187.73) and (194.64,212.45) .. (189.93,222.4) .. controls (180.23,244.33) and (166.49,223.52) .. (152.27,250.4) .. controls (156.83,232.64) and (130.17,227.41) .. (126.93,216.07) .. controls (121.11,191.51) and (159.34,163.1) .. (169.99,151.46) -- cycle ;
            	\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (169.99,151.46) .. controls (188.27,187.73) and (194.64,212.45) .. (189.93,222.4) .. controls (180.23,244.33) and (166.49,223.52) .. (152.27,250.4) .. controls (156.83,232.64) and (130.17,227.41) .. (126.93,216.07) .. controls (121.11,191.51) and (159.34,163.1) .. (169.99,151.46) -- cycle ; 
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=0.22 ][shading=_hiuurmzl2,_pze6mpq38]   (152.27,250.4) -- (169.99,151.46) ;
            	\path  [shading=_6lb5tp2xq,_iwgjxrc6b] (169.65,150.93) .. controls (137.85,138.13) and (111.52,116.92) .. (108.27,106.4) .. controls (100.62,83.67) and (125.27,91.4) .. (120.27,62.4) .. controls (128.89,78.58) and (149.89,67.22) .. (159.93,73.4) .. controls (180.81,87.58) and (169.64,135.15) .. (169.65,150.93) -- cycle ; 
            	\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (169.65,150.93) .. controls (137.85,138.13) and (111.52,116.92) .. (108.27,106.4) .. controls (100.62,83.67) and (125.27,91.4) .. (120.27,62.4) .. controls (128.89,78.58) and (149.89,67.22) .. (159.93,73.4) .. controls (180.81,87.58) and (169.64,135.15) .. (169.65,150.93) -- cycle ; 
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=0.22 ][shading=_goy0jixdl,_8ikm3z2jx]   (120.27,62.4) -- (169.88,149.9) ;
            	\path  [shading=_813w294wq,_7ds2d3dgm] (169.65,150.93) .. controls (146.22,175.95) and (114.91,191.51) .. (103.93,190.73) .. controls (79.98,189.65) and (91.34,169.41) .. (61.13,165.91) .. controls (79.33,163.72) and (78.2,141.86) .. (87.6,134.73) .. controls (108.37,120.4) and (154.94,145.23) .. (169.65,150.93) -- cycle ; 
            	\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (169.65,150.93) .. controls (146.22,175.95) and (114.91,191.51) .. (103.93,190.73) .. controls (79.98,189.65) and (91.34,169.41) .. (61.13,165.91) .. controls (79.33,163.72) and (78.2,141.86) .. (87.6,134.73) .. controls (108.37,120.4) and (154.94,145.23) .. (169.65,150.93) -- cycle ; 
            	\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=0.22 ][shading=_d4lg91t2t,_u026d9lrc]   (61.13,165.91) -- (169.65,150.93) ;
            	\path  [shading=_hck9fb9dd,_tme77zkul] (150.85,149.9) .. controls (150.85,139.39) and (159.37,130.87) .. (169.88,130.87) .. controls (180.4,130.87) and (188.92,139.39) .. (188.92,149.9) .. controls (188.92,160.41) and (180.4,168.93) .. (169.88,168.93) .. controls (159.37,168.93) and (150.85,160.41) .. (150.85,149.9) -- cycle ; 
            	\draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ] (150.85,149.9) .. controls (150.85,139.39) and (159.37,130.87) .. (169.88,130.87) .. controls (180.4,130.87) and (188.92,139.39) .. (188.92,149.9) .. controls (188.92,160.41) and (180.4,168.93) .. (169.88,168.93) .. controls (159.37,168.93) and (150.85,160.41) .. (150.85,149.9) -- cycle ; 
            	\draw (159.33,141) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (194.67,49.67) node [anchor=north west][inner sep=0.75pt]    {$y=f( x)$};
            	\draw (274.67,129) node [anchor=north west][inner sep=0.75pt]    {$x$};
            	\draw (152,43) node [anchor=north west][inner sep=0.75pt]    {$y$};
            \end{tikzpicture}'''

                # Nội dung câu hỏi
                noidungcauhoi = (r'''\immini{Một nghệ nhân thiết kế một mô hình bông hoa $%s$ cánh trên hệ trục tọa độ $Oxy$, đơn vị trên mỗi trục là $1$ cm. Bông hoa có nhụy là một hình tròn tâm $O$ bán kính $%s$ cm. Các cánh hoa giống hệt nhau và được xếp đối xứng xoay quanh $O$. Xét cánh hoa ở góc phần tư thứ nhất, nó được tạo bởi hai nhánh đường cong đối xứng nhau qua đường phân giác $y = x$. Nhánh phía trên là một phần của đồ thị hàm số bậc ba $y = f\left( x \right) = %s$ đi qua gốc tọa độ $O\left( 0;0 \right)$, điểm $A\left( %s;%s \right)$ và tiếp xúc với đường thẳng $y = x$ tại điểm đỉnh cánh hoa $B\left( %s;%s \right)$. Diện tích bông hoa này bằng bao nhiêu? (làm tròn đến hàng phần chục của $\text{cm}^2$)}{%s}''' % (N, R_str, fx_latex, xa, ya, xb, xb, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Diện tích của nhụy hoa là $S_1 = \\pi R^2 = \\pi \\cdot \\left( %s \\right)^2 = %s \\left( \\text{cm}^2 \\right)$.\\\\
            Xét nhánh phía trên của cánh hoa ở góc phần tư thứ nhất, nó là đồ thị hàm số $y = f\\left( x \\right) = %s$.\\\\
            Phương trình hoành độ giao điểm của nhánh này với đường phân giác $y = x$ là:
            $$ %s = x \\Leftrightarrow %s = 0 \\Leftrightarrow \\left[\\begin{array}{l} x = 0 \\\\ x = %s \\end{array}\\right. $$
            Diện tích nhánh phía trên (phần nằm trên đường $y=x$) là:
            $$ S_2 = \\int_{0}^{%s} \\left( f\\left( x \\right) - x \\right) \\text{d}x = \\int_{0}^{%s} \\left( %s \\right) \\text{d}x = %s \\left( \\text{cm}^2 \\right). $$
            Diện tích một cánh hoa là $S_3 = 2S_2 = 2 \\cdot \\left( %s \\right) = %s \\left( \\text{cm}^2 \\right)$.\\\\
            Diện tích bông hoa bằng tổng diện tích nhụy hoa và diện tích %s cánh hoa:\\\\
            $$ S = S_1 + %s \\cdot S_3 = %s + %s \\cdot \\left( %s \\right) = %s \\approx %s \\left( \\text{cm}^2 \\right).$$
            ''' % (R_str, latex(R_sq * pi),
                   fx_latex,
                   fx_latex, latex(fx - x), xb,
                   xb, xb, latex(fx - x), latex(S2_expr),
                   latex(S2_expr), latex(S3_expr),
                   N,
                   N, latex(R_sq * pi), N, latex(S3_expr), latex(S_exact_expr), kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi) + dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

