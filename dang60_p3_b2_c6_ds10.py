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


def bt_dang60_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Random tổng số bóng trên bàn (từ 9 đến 13 bóng)
            N = random.randint(9, 13)
            N_reg = N - 3 # Số bóng thường

            # Random 3 con số trên quả bóng mục tiêu
            targets = random.sample(range(1, N + 1), 3)
            targets.sort()
            target_str = f"{targets[0]}, {targets[1]} \\, \\text{{và}} \\, {targets[2]}"

            # Tính toán các trường hợp thỏa mãn (x + y <= 3 và x > y)
            # Trường hợp 1: x = 1, y = 0
            w1_x = math.comb(3, 1) * math.comb(N_reg, 2)
            c1_y = math.comb(N_reg - 2, 3)
            n1 = w1_x * c1_y

            # Trường hợp 2: x = 2, y = 0
            w2_x = math.comb(3, 2) * math.comb(N_reg, 1)
            c2_y = math.comb(N_reg - 1, 3)
            n2 = w2_x * c2_y

            # Trường hợp 3: x = 2, y = 1
            w3_x = math.comb(3, 2) * math.comb(N_reg, 1)
            w3_y = math.comb(1, 1) * math.comb(N_reg - 1, 2)
            n3 = w3_x * w3_y

            # Trường hợp 4: x = 3, y = 0
            n4 = math.comb(N_reg, 3)
            c4_y = n4

            # Tính không gian mẫu và biến cố
            n_omega = n1 + n2 + n3 + n4
            n_A = n1 + n2 + n4

            # Tính xác suất
            prob_frac = Rational(n_A, n_omega)
            num = prob_frac.p
            den = prob_frac.q

            prob_val = n_A / n_omega
            prob_round = round(prob_val, 2)
            prob_round_str = str(prob_round).replace('.', ',')

            # Xử lý các đáp án trắc nghiệm
            du = ['$%s$' % prob_round_str]
            da = du[0]

            # Tạo các đáp án nhiễu (sai số ngẫu nhiên xung quanh kết quả đúng)
            s_pool = set()
            while len(s_pool) < 3:
                false_prob = round(prob_val + random.choice([-0.15, -0.12, -0.08, -0.04, 0.04, 0.08, 0.12, 0.15]), 2)
                if 0 < false_prob < 1 and false_prob != prob_round:
                    s_pool.add(str(false_prob).replace('.', ','))

            s_list = list(s_pool)
            random.shuffle(s_list)

            das1 = '$%s$' % s_list[0]
            das2 = '$%s$' % s_list[1]
            das3 = '$%s$' % s_list[2]

            # Trộn ngẫu nhiên 4 đáp án
            da_d = ('\\True ' + str(da))
            list_1 = [da_d, str(das1), str(das2), str(das3)]
            random.shuffle(list_1)
            hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_egcp79jvt/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -128.7 bp }  }  \pgftransformscale{1.32 }  }}}
            	\pgfdeclareradialshading{_jhrqxfcb8}{\pgfpoint{-72bp}{104bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(16.659600394112722bp)=(0.97,0.91,0.11);
            		rgb(24.873880658830917bp)=(0,0,0);
            		rgb(400bp)=(0,0,0)}
            	\tikzset {_suhfpjfpm/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -128.7 bp }  }  \pgftransformscale{1.32 }  }}}
            	\pgfdeclareradialshading{_3318nqh1p}{\pgfpoint{-72bp}{104bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(16.73102787562779bp)=(0.96,0.58,0.14);
            		rgb(24.873880658830917bp)=(0,0,0);
            		rgb(400bp)=(0,0,0)}
            	\tikzset {_doc458qr9/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{89.1 bp } { -128.7 bp }  }  \pgftransformscale{1.32 }  }}}
            	\pgfdeclareradialshading{_f9u47eqj5}{\pgfpoint{-72bp}{104bp}}{rgb(0bp)=(1,1,1);
            		rgb(0bp)=(1,1,1);
            		rgb(16.73102787562779bp)=(0,0,0);
            		rgb(24.873880658830917bp)=(0,0,0);
            		rgb(400bp)=(0,0,0)}
            	\tikzset{every picture/.style={line width=0.75pt}}    
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=0.43 ] (217.2,129.5) .. controls (217.2,118.45) and (234.26,109.5) .. (255.3,109.5) .. controls (276.34,109.5) and (293.4,118.45) .. (293.4,129.5) .. controls (293.4,140.55) and (276.34,149.5) .. (255.3,149.5) .. controls (234.26,149.5) and (217.2,140.55) .. (217.2,129.5) -- cycle ;
            	\path  [shading=_jhrqxfcb8,_egcp79jvt] (199.48,98.74) .. controls (199.48,73.13) and (220.25,52.36) .. (245.86,52.36) .. controls (271.47,52.36) and (292.24,73.13) .. (292.24,98.74) .. controls (292.24,124.35) and (271.47,145.12) .. (245.86,145.12) .. controls (220.25,145.12) and (199.48,124.35) .. (199.48,98.74) -- cycle ; 
            	\draw   (199.48,98.74) .. controls (199.48,73.13) and (220.25,52.36) .. (245.86,52.36) .. controls (271.47,52.36) and (292.24,73.13) .. (292.24,98.74) .. controls (292.24,124.35) and (271.47,145.12) .. (245.86,145.12) .. controls (220.25,145.12) and (199.48,124.35) .. (199.48,98.74) -- cycle ; 
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (210,93.5) .. controls (210,79.69) and (221.19,68.5) .. (235,68.5) .. controls (248.81,68.5) and (260,79.69) .. (260,93.5) .. controls (260,107.31) and (248.81,118.5) .. (235,118.5) .. controls (221.19,118.5) and (210,107.31) .. (210,93.5) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=0.43 ] (341.22,158.14) .. controls (341.22,145.21) and (361.18,134.73) .. (385.81,134.73) .. controls (410.44,134.73) and (430.4,145.21) .. (430.4,158.14) .. controls (430.4,171.07) and (410.44,181.55) .. (385.81,181.55) .. controls (361.18,181.55) and (341.22,171.07) .. (341.22,158.14) -- cycle ;
            	\path  [shading=_3318nqh1p,_suhfpjfpm] (320.48,122.14) .. controls (320.48,92.16) and (344.78,67.86) .. (374.76,67.86) .. controls (404.74,67.86) and (429.04,92.16) .. (429.04,122.14) .. controls (429.04,152.12) and (404.74,176.42) .. (374.76,176.42) .. controls (344.78,176.42) and (320.48,152.12) .. (320.48,122.14) -- cycle ; 
            	\draw   (320.48,122.14) .. controls (320.48,92.16) and (344.78,67.86) .. (374.76,67.86) .. controls (404.74,67.86) and (429.04,92.16) .. (429.04,122.14) .. controls (429.04,152.12) and (404.74,176.42) .. (374.76,176.42) .. controls (344.78,176.42) and (320.48,152.12) .. (320.48,122.14) -- cycle ; 
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (357.37,106.06) .. controls (357.37,89.9) and (370.47,76.8) .. (386.63,76.8) .. controls (402.79,76.8) and (415.89,89.9) .. (415.89,106.06) .. controls (415.89,122.22) and (402.79,135.32) .. (386.63,135.32) .. controls (370.47,135.32) and (357.37,122.22) .. (357.37,106.06) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=0.43 ] (250.09,205.41) .. controls (250.09,190.87) and (272.55,179.08) .. (300.25,179.08) .. controls (327.95,179.08) and (350.4,190.87) .. (350.4,205.41) .. controls (350.4,219.95) and (327.95,231.73) .. (300.25,231.73) .. controls (272.55,231.73) and (250.09,219.95) .. (250.09,205.41) -- cycle ;
            	\path  [shading=_f9u47eqj5,_doc458qr9] (226.77,164.91) .. controls (226.77,131.19) and (254.1,103.86) .. (287.82,103.86) .. controls (321.54,103.86) and (348.87,131.19) .. (348.87,164.91) .. controls (348.87,198.63) and (321.54,225.97) .. (287.82,225.97) .. controls (254.1,225.97) and (226.77,198.63) .. (226.77,164.91) -- cycle ; 
            	\draw   (226.77,164.91) .. controls (226.77,131.19) and (254.1,103.86) .. (287.82,103.86) .. controls (321.54,103.86) and (348.87,131.19) .. (348.87,164.91) .. controls (348.87,198.63) and (321.54,225.97) .. (287.82,225.97) .. controls (254.1,225.97) and (226.77,198.63) .. (226.77,164.91) -- cycle ; 
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (253.59,156.16) .. controls (253.59,137.98) and (268.33,123.25) .. (286.5,123.25) .. controls (304.68,123.25) and (319.41,137.98) .. (319.41,156.16) .. controls (319.41,174.34) and (304.68,189.07) .. (286.5,189.07) .. controls (268.33,189.07) and (253.59,174.34) .. (253.59,156.16) -- cycle ;
            	\draw (226,79) node [anchor=north west][inner sep=0.75pt]  [font=\Huge] [align=left] {3};
            	\draw (374,88) node [anchor=north west][inner sep=0.75pt]  [font=\fontsize{3em}{3.6em}\selectfont,rotate=-357.39] [align=left] {6};
            	\draw (272,133) node [anchor=north west][inner sep=0.75pt]  [font=\fontsize{3.67em}{4.4em}\selectfont,rotate=-0.81] [align=left] {8};
            \end{tikzpicture}'''
            # Câu hỏi
            noidungcauhoi = (r'''\immini{Trong bộ môn billiards $%s$ bóng (các bóng được đánh số từ $1$ đến $%s$) có $3$ quả bóng mục tiêu là $%s$. Cơ thủ X chọn ngẫu nhiên $3$ quả, sau đó cơ thủ Y chọn ngẫu nhiên $3$ quả từ các quả còn lại. Biết rằng sau khi chọn, cơ thủ X đang có lợi thế hơn cơ thủ Y (tức là số bóng mục tiêu của X nhiều hơn của Y). Hãy tính xác suất để cơ thủ Y không giữ bất kỳ quả bóng mục tiêu nào (Kết quả làm tròn đến hàng phần trăm).}{%s}''' 
            % (N, N, target_str, hinhve))

            # Nội dung lời giải
            loigiai = ('''Gọi $x; y$ lần lượt là số bóng mà cơ thủ X và Y chọn được.\\\\
            Tổng số bóng mục tiêu tối đa là $3$ bóng nên ta có $x + y \\le 3$.\\\\
            Do cơ thủ X đang có lợi thế hơn cơ thủ Y nên số bóng mục tiêu của X nhiều hơn của Y.\\\\
            Khi đó ta có điều kiện $\\begin{cases} x + y \\le 3 \\\\\\\\ x > y \\end{cases}$ nên ta có thể liệt kê các trường hợp thỏa mãn:\\\\
            Trường hợp 1: $x = 1; y = 0$\\\\
            Cơ thủ X chọn: $1$ bóng mục tiêu trong $3$ bóng và $2$ bóng thường trong $%s$ bóng có số cách chọn là $C_3^1 \\cdot C_{%s}^2 = %s$ cách.\\\\
            Cơ thủ Y chọn: $3$ bóng thường trong $%s$ bóng có $C_{%s}^3 = %s$ cách chọn.\\\\
            Vậy có tổng cộng $n_1 = %s \\cdot %s = %s$ (cách).\\\\
            Trường hợp 2: $x = 2; y = 0$\\\\
            Cơ thủ X chọn: $2$ bóng mục tiêu trong $3$ bóng và $1$ bóng thường trong $%s$ bóng có số cách chọn là $C_3^2 \\cdot C_{%s}^1 = %s$ cách.\\\\
            Cơ thủ Y chọn: $3$ bóng thường trong $%s$ bóng có $C_{%s}^3 = %s$ cách chọn.\\\\
            Vậy có tổng cộng $n_2 = %s \\cdot %s = %s$ (cách).\\\\
            Trường hợp 3: $x = 2; y = 1$\\\\
            Cơ thủ X chọn: $2$ bóng mục tiêu trong $3$ bóng và $1$ bóng thường trong $%s$ bóng có số cách chọn là $C_3^2 \\cdot C_{%s}^1 = %s$ cách.\\\\
            Cơ thủ Y chọn: $1$ bóng mục tiêu trong $1$ bóng còn lại và $2$ bóng thường trong $%s$ bóng có số cách chọn là $C_1^1 \\cdot C_{%s}^2 = %s$ cách.\\\\
            Vậy có tổng cộng $n_3 = %s \\cdot %s = %s$ (cách).\\\\
            Trường hợp 4: $x = 3; y = 0$\\\\
            Cơ thủ X chọn: $3$ bóng mục tiêu trong $3$ bóng có số cách chọn là $1$ cách.\\\\
            Cơ thủ Y chọn: $3$ bóng thường trong $%s$ bóng có số cách chọn là $C_{%s}^3 = %s$ cách.\\\\
            Vậy có tổng cộng $n_4 = %s$ (cách).\\\\
            Vậy tổng số trường hợp thỏa mãn X lợi thế hơn Y là: $n(\\Omega) = %s + %s + %s + %s = %s$ cách.\\\\
            Theo yêu cầu bài toán, cơ thủ Y không giữ bất kỳ quả bóng mục tiêu nào tức $y = 0$.\\\\
            Khi đó $n(A) = %s + %s + %s = %s$ cách.\\\\
            Vậy xác suất cần tìm là: $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{%s}{%s} = \\frac{%s}{%s} \\approx %s$.''' 
            % (
                N_reg, N_reg, w1_x, 
                N_reg - 2, N_reg - 2, c1_y, 
                w1_x, c1_y, n1,

                N_reg, N_reg, w2_x, 
                N_reg - 1, N_reg - 1, c2_y, 
                w2_x, c2_y, n2,

                N_reg, N_reg, w3_x, 
                N_reg - 1, N_reg - 1, w3_y, 
                w3_x, w3_y, n3,

                N_reg, N_reg, c4_y, 
                n4,

                n1, n2, n3, n4, n_omega,

                n1, n2, n4, n_A,

                n_A, n_omega, num, den, prob_round_str
            ))
            dapan='\\shortans[0]{$%s$}\n'%(prob_round_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

