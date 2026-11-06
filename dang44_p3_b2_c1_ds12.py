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


def bt_dang44_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các hằng số cho bài toán
                # Tiệm cận đứng x = m, tiệm cận ngang y = a
                m = random.randint(2, 6)
                a = random.randint(2, 6)
                # Hệ số k = ad - bc
                k = random.randint(15, 45) 
                b = k - a * m
                # Độ dài cạnh BD cố định
                L = random.randint(3, 8)

                # Định dạng hàm số để hiển thị đẹp
                if b > 0:
                    f_latex = "\\frac{%sx + %s}{x - %s}" % (a, b, m)
                elif b < 0:
                    f_latex = "\\frac{%sx - %s}{x - %s}" % (a, abs(b), m)
                else:
                    f_latex = "\\frac{%sx}{x - %s}" % (a, m)

                # Tính toán diện tích lớn nhất
                max_d = math.sqrt(2 * k)
                max_S = 0.5 * L * max_d

                # Xử lý kết quả làm tròn đến hàng phần mười và chuyển dấu chấm thành phẩy
                kq3 = Decimal(float(max_S)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                kq4 = round(max_S, 1)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên
                s_set = set()
                while len(s_set) < 6:
                    offset = random.choice([-3, -2, -1.5, -1, -0.5, 0.5, 1, 1.5, 2, 2.5, 3])
                    wrong_val = kq4 + offset
                    if wrong_val > 0 and wrong_val != kq4:
                        wrong_str = str(Decimal(float(wrong_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.', ',')
                        s_set.add('$%s$' % wrong_str)

                s = list(s_set)
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 165; green, 237; blue, 247 }  ,fill opacity=1 ][line width=1]  (61,32) -- (231.1,32) -- (231.1,202.1) -- (61,202.1) -- cycle ;
            	\draw  [fill={rgb, 255:red, 229; green, 230; blue, 160 }  ,fill opacity=1 ][line width=1]  (135,33) .. controls (170.6,32.4) and (197.1,32.4) .. (230.6,32.5) .. controls (230.6,67.4) and (230.6,105.9) .. (230.1,132.4) .. controls (226.6,130.4) and (160.1,127.9) .. (135,33) -- cycle ;
            	\draw  [line width=1]  (60.5,32.5) -- (230.6,32.5) -- (230.6,202.6) -- (60.5,202.6) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 0; blue, 33 }  ,draw opacity=1 ][line width=1]    (93,170.5) -- (152.6,79.4) ;
            	\draw [color={rgb, 255:red, 255; green, 0; blue, 33 }  ,draw opacity=1 ][line width=1]    (180.1,124.4) -- (152.6,79.4) ;
            	\draw [color={rgb, 255:red, 255; green, 0; blue, 33 }  ,draw opacity=1 ][line width=1]    (93,170.5) -- (180.1,124.4) ;
            	\draw (177.5,59) node [anchor=north west][inner sep=0.75pt]    {$(C)$};
            	\draw (75.5,166) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (135,69) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (174.5,129) node [anchor=north west][inner sep=0.75pt]    {$D$};
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Trong mặt phẳng $Oxy$ có đơn vị dài trên mỗi trục là mét, giữa một hồ nước có một mô đất mà bờ của nó lồi và là một phần đồ thị $(C)$ của hàm số $y = %s$. Người ta dùng một lưới quây thành một hình tam giác $ABD$ với $A(%s; %s)$, đường thẳng $BD$ là tiếp tuyến với $(C)$ tại tiếp điểm $B$, độ dài $BD = %s$. Diện tích lớn nhất mà lưới quây được bằng bao nhiêu mét vuông? (không làm tròn các phép tính trung gian, làm tròn kết quả cuối cùng đến hàng phần mười).}{%s}'''
                                 % (f_latex, m, a, L, hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải theo cách khảo sát hàm số
                loigiai = ('''Ta có $A(%s; %s)$ là giao điểm của hai đường tiệm cận của đồ thị $(C)$. \\\\
                         Đồ thị $(C)$ có phương trình $y = %s + \\frac{%s}{x - %s}$. \\\\
                         Gọi $B\\left(x_0; y_0\\right)$ với $y_0 = %s + \\frac{%s}{x_0 - %s}$ là tiếp điểm. \\\\
                         Phương trình tiếp tuyến $\\Delta$ tại $B$ của $(C)$ có dạng: \\\\
                         $y = \\frac{-%s}{(x_0 - %s)^2}(x - x_0) + y_0 \\Leftrightarrow %s(x - x_0) + (x_0 - %s)^2(y - y_0) = 0$. \\\\
                         Khoảng cách từ $A$ đến tiếp tuyến $\\Delta$ (chứa đường thẳng $BD$) là: \\\\
                         $d(A, BD) = \\frac{\\left| %s(%s - x_0) + (x_0 - %s)^2(%s - y_0) \\right|}{\\sqrt{%s^2 + (x_0 - %s)^4}}$. \\\\
                         Thay $y_0 = %s + \\frac{%s}{x_0 - %s}$ ta được khoảng cách: \\\\
                         $d(A, BD) = \\frac{%s |x_0 - %s|}{\\sqrt{%s^2 + (x_0 - %s)^4}}$. \\\\
                         Đặt $t = |x_0 - %s| > 0$. Xét hàm số $f(t) = \\frac{%s t}{\\sqrt{%s^2 + t^4}}$ trên khoảng $(0; +\\infty)$. \\\\
                         Ta có đạo hàm $f'(t) = \\frac{%s(%s^2 - t^4)}{(%s^2 + t^4)\\sqrt{%s^2 + t^4}}$. \\\\
                         $f'(t) = 0 \\Leftrightarrow t^4 = %s^2 \\Leftrightarrow t = \\sqrt{%s}$ (do $t > 0$). \\\\
                         Lập bảng biến thiên, ta thấy hàm số $f(t)$ đồng biến trên khoảng $(0; \\sqrt{%s})$ và nghịch biến trên khoảng $(\\sqrt{%s}; +\\infty)$. Do đó hàm số đạt giá trị lớn nhất tại $t = \\sqrt{%s}$. \\\\
                         Khi đó $\\max d(A, BD) = f(\\sqrt{%s}) = \\frac{%s \\sqrt{%s}}{\\sqrt{%s^2 + %s^2}} = \\sqrt{%s}$. \\\\
                         Diện tích tam giác $ABD$ là: \\\\
                         $S_{ABD} = \\frac{1}{2} \\cdot BD \\cdot d(A, BD) \\le \\frac{1}{2} \\cdot %s \\cdot \\sqrt{%s} \\approx %s \\left( \\text{m}^2 \\right)$. \\\\
                         Vậy diện tích lớn nhất mà lưới quây được là khoảng $%s \\text{ m}^2$.'''

                         % (m, a, 
                            a, k, m, 
                            a, k, m, 
                            k, m, k, m, 
                            k, m, m, a, k, m, 
                            a, k, m, 
                            2*k, m, k, m, 
                            m, 2*k, k, 
                            2*k, k, k, k, 
                            k, k, 
                            k, k, k, 
                            k, 2*k, k, k, k, 2*k, 
                            L, 2*k, kq, 
                            kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

