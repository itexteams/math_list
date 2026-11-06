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


def bt_dang45_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random kích thước tấm nhôm ban đầu (A) và giữ nguyên đoạn cắt (X=1)
                A = random.choice([8, 9, 10, 11, 12, 13, 14, 15])
                X = 1

                # Tính toán các hệ số cho phương trình tối ưu thể tích
                S = A - X
                B = A - 2 * X

                C1 = A + 2
                C2 = A**2 - 2*A
                delta = 21*A**2 - 36*A + 4

                # Giá trị y tối ưu cho thể tích lớn nhất
                y = (C1 + math.sqrt(delta)) / 10

                # Tính chiều cao và thể tích max
                h = math.sqrt(S - y)
                V_max = (1/3) * h * (B**2 + B*y + y**2)

                # Làm tròn thể tích đến hàng đơn vị
                V_dec = Decimal(float(V_max)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq_exact = int(V_dec)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq_exact)]
                da = random.choice(du)

                # Tập hợp các đáp án nhiễu
                s = ['$%s$' % (kq_exact + 1),
                     '$%s$' % (kq_exact + 2),
                     '$%s$' % (kq_exact + 3),
                     '$%s$' % (kq_exact - 1),
                     '$%s$' % (kq_exact - 2),
                     '$%s$' % (kq_exact - 3)]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Chuyển đổi các biến sang chuỗi để format LaTeX
                S_str = str(S)
                A_str = str(A)
                B_str = str(B)
                B2_str = str(B**2)
                C1_str = str(C1)
                C2_str = str(C2)
                delta_str = str(delta)
                V_round_str = str(kq_exact)
                hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw  [line width=1]  (131.31,61.92) -- (287.39,61.92) -- (287.39,218) -- (131.31,218) -- cycle ;
            		\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (165.21,95.82) -- (253.49,95.82) -- (253.49,184.1) -- (165.21,184.1) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1]  (266.78,62.45) -- (287.39,61.92) -- (286.73,81.06) -- (253.49,95.82) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1]  (130.51,82.39) -- (131.31,61.92) -- (149.79,61.79) -- (165.21,95.82) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1]  (287.48,197.17) -- (287.39,218) -- (267.09,217.11) -- (253.49,184.1) -- cycle ;
            		\draw  [fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=1 ][line width=1]  (131.49,197.62) -- (131.31,218) -- (150.54,216.67) -- (165.21,184.1) -- cycle ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (131.31,61.92) -- (287.39,218) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (287.39,61.92) -- (131.31,218) ;
            		\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (481.67,145.32) -- (468.82,196.73) -- (359.8,186.54) -- (321.69,130.25) -- cycle ;
            		\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (573.41,130.25) -- (532.64,186.98) -- (468.82,196.73) -- (481.67,145.32) -- cycle ;
            		\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (481.67,145.32) -- (573.41,130.25) -- (413.43,114.3) -- (321.69,130.25) -- cycle ;
            		\draw [line width=1]    (413.43,114.3) -- (415.64,138.67) ;
            		\draw (112.23,48) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (115.35,213.36) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (287.39,218) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (285.46,48) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (108,69.52) node [anchor=north west][inner sep=0.75pt]    {$M$};
            		\draw (163.14,76) node [anchor=north west][inner sep=0.75pt]    {$N$};
            		\draw (141.92,44) node [anchor=north west][inner sep=0.75pt]    {$P$};
            		\draw (238,186) node [anchor=north west][inner sep=0.75pt]    {$Q$};
            	\end{tikzpicture}
            \end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Từ một tấm nhôm hình vuông có cạnh bằng $%s$ dm, người ta cắt bỏ bốn tứ giác bằng nhau (cùng bằng tứ giác $AMNP$) ở bốn góc tấm nhôm đó, biết $AM=AP=%s$ dm và điểm $N$ thuộc đường chéo $AC$. Với phần còn lại của tấm nhôm sau khi đã bỏ đi 4 tứ giác nói trên, người ta đã gập các đoạn $MN$ trùng với $PN$ rồi dán kỹ bằng keo, làm tương tự cho 3 cặp đoạn còn lại, người ta thu được chậu nước hình chóp cụt tứ giác đều. %s Bỏ qua độ dày tấm nhôm, sức chứa lớn nhất của chậu nước hình chóp cụt tứ giác đều này là bao nhiêu lít? (làm tròn kết quả đến hàng đơn vị).'''
                % (A_str, str(X), hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $x$ (dm) là độ dài cạnh đáy nhỏ của chóp cụt tứ giác đều ($0 < x < %s$). \\\\
                Đáy lớn của chóp cụt là phần còn lại của cạnh tấm nhôm sau khi cắt bỏ 2 góc, có độ dài là $B = %s - 2 \\cdot 1 = %s$ (dm). \\\\
                Đường cao của mặt bên chóp cụt là khoảng cách từ mép đáy lớn đến nếp gấp đáy nhỏ, tức là $l = \\frac{%s - x}{2}$. \\\\
                Chiều cao của chóp cụt là $h = \\sqrt{l^2 - \\left(\\frac{%s - x}{2}\\right)^2} = \\sqrt{\\left(\\frac{%s - x}{2}\\right)^2 - \\left(\\frac{%s - x}{2}\\right)^2} = \\sqrt{%s - x}$. \\\\
                Thể tích khối chóp cụt là $V(x) = \\frac{1}{3} \\sqrt{%s - x} (%s^2 + %s x + x^2) = \\frac{1}{3} \\sqrt{%s - x} (x^2 + %s x + %s)$. \\\\
                Để $x$ lớn nhất thì $f(x) = (%s - x)(x^2 + %s x + %s)^2$ phải đạt giá trị lớn nhất. \\\\
                Ta có $f'(x) = -(x^2 + %s x + %s)^2 + 2(%s - x)(x^2 + %s x + %s)(2x + %s) = (x^2 + %s x + %s)(-5x^2 + %s x + %s)$. \\\\
                $f'(x) = 0 \\Leftrightarrow -5x^2 + %s x + %s = 0 \\Rightarrow x = \\frac{%s + \\sqrt{%s}}{10}$. \\\\
                Với $x = \\frac{%s + \\sqrt{%s}}{10}$, ta tính được $V_{\\max} \\approx %s$ (lít).'''
                % (S_str, A_str, B_str, A_str, B_str, A_str, B_str, S_str, S_str, B_str, B_str, S_str, B_str, B2_str, S_str, B_str, B2_str, B_str, B2_str, S_str, B_str, B2_str, B_str, B_str, B2_str, C1_str, C2_str, C1_str, C2_str, C1_str, delta_str, C1_str, delta_str, V_round_str))
                dapan='\\shortans[0]{$%s$}\n'%(V_round_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

