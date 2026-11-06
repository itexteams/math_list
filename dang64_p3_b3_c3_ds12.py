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


def bt_dang64_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random chi phí dát bạc (c1) và chi phí phủ sơn (c2)
                c1 = random.choice([8, 10, 12, 14, 15]) # triệu đồng/m2
                c2 = random.choice([2, 3, 4, 5])        # triệu đồng/m2

                # Tính toán diện tích (giữ nguyên tỷ lệ bài toán)
                # S_bac = 7/6
                # S_tron = 25*pi/16
                # S_son = S_tron - S_bac

                # Tính tổng tiền (kq_exact)
                kq_exact = c1 * Rational(7, 6) + c2 * (Rational(25, 16) * pi - Rational(7, 6))

                # Làm tròn đến hàng phần chục
                kq3 = Decimal(float(kq_exact)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                kq4 = round(float(kq_exact), 1)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các đáp án nhiễu (sai số hợp lý)
                s = [
                     '$%s$'%(str(round(kq4 + 1.2, 1)).replace('.', ',')),
                     '$%s$'%(str(round(kq4 + 2.5, 1)).replace('.', ',')),
                     '$%s$'%(str(round(kq4 + 3.1, 1)).replace('.', ',')),
                     '$%s$'%(str(round(kq4 - 1.2, 1)).replace('.', ',')),
                     '$%s$'%(str(round(kq4 - 2.5, 1)).replace('.', ',')),
                     '$%s$'%(str(round(kq4 - 3.1, 1)).replace('.', ',')),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\scalebox{0.7}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (154.03,164.03) .. controls (154.03,106.52) and (200.66,59.9) .. (258.17,59.9) .. controls (315.68,59.9) and (362.3,106.52) .. (362.3,164.03) .. controls (362.3,221.54) and (315.68,268.17) .. (258.17,268.17) .. controls (200.66,268.17) and (154.03,221.54) .. (154.03,164.03) -- cycle ;
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (173.18,104.66) .. controls (199.96,143.34) and (238.76,200.25) .. (258.17,226.13) .. controls (280.8,191.2) and (306.03,151.1) .. (341.6,101.94) .. controls (322.2,183.44) and (296.97,266.87) .. (258.17,268.17) .. controls (216.77,264.93) and (199.96,195.08) .. (173.18,104.66) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (258.17,226.13) -- (258.17,268.17) ;
            	\draw (152.95,88) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (343.69,83.31) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (251.05,272) node [anchor=north west][inner sep=0.75pt]    {$I$};
            	\draw (253.29,199) node [anchor=north west][inner sep=0.75pt]    {$J$};
            	\draw (189.1,90) node [anchor=north west][inner sep=0.75pt]  [font=\huge] [align=left] {VINFAST};
            \end{tikzpicture} }'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Lô gô gắn tại các Showroom của hãng ô tô VINFAST là một hình tròn. Phần tô đậm (nằm giữa parabol đỉnh $I$ và đường gấp khúc $AJB$) được dát bạc với chi phí $%s$ triệu đồng/$\text{m}^2$. Phần còn lại của hình tròn được phủ sơn với chi phí $%s$ triệu đồng/$\text{m}^2$. Biết $AB = 2\text{m}$, $IA = IB = \sqrt{5}\text{m}$ và $JA = JB = \frac{\sqrt{13}}{2}\text{m}$. Tính tổng số tiền (đơn vị: triệu đồng) để dát bạc và phủ sơn toàn bộ lô gô nói trên (Kết quả làm tròn đến hàng phần chục).}{%s}'''
                                 %(latex(c1), latex(c2),hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Giá trị chi tiết chưa làm tròn để show trong lời giải
                kq_detail = str(round(float(kq_exact), 4)).replace('.', ',')

                # Nội dung lời giải
                loigiai = ('''\\begin{center} \\scalebox{0.7}{
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (154.03,164.03) .. controls (154.03,106.52) and (200.66,59.9) .. (258.17,59.9) .. controls (315.68,59.9) and (362.3,106.52) .. (362.3,164.03) .. controls (362.3,221.54) and (315.68,268.17) .. (258.17,268.17) .. controls (200.66,268.17) and (154.03,221.54) .. (154.03,164.03) -- cycle ;
            		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (173.18,104.66) .. controls (199.96,143.34) and (238.76,200.25) .. (258.17,226.13) .. controls (280.8,191.2) and (306.03,151.1) .. (341.6,101.94) .. controls (322.2,183.44) and (296.97,266.87) .. (258.17,268.17) .. controls (216.77,264.93) and (199.96,195.08) .. (173.18,104.66) -- cycle ;
            		\\draw [line width=1]    (123.6,103.5) -- (400.8,101.43) ;
            		\\draw [shift={(404.8,101.4)}, rotate = 179.57] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            		\\draw [line width=1]    (258.17,286.13) -- (258.17,33.9) ;
            		\\draw [shift={(258.17,29.9)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            		\\draw (155.95,79.6) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\\draw (339.69,78.31) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\\draw (244.05,271) node [anchor=north west][inner sep=0.75pt]    {$I$};
            		\\draw (243.79,224) node [anchor=north west][inner sep=0.75pt]    {$J$};
            		\\draw (239,105) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\\draw (385.1,109) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\\draw (238.1,33) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\\end{tikzpicture} }
            \\end{center}
            Gọi $O$ là trung điểm của đoạn thẳng $AB$. Chọn hệ trục tọa độ $Oxy$ với gốc tọa độ tại $O$, trục $Ox$ chứa đoạn thẳng $AB$, và trục $Oy$ là đường trung trực của $AB$ hướng lên trên.\\\\
                         Vì $AB = 2\\text{m}$ nên $OA = OB = 1\\text{m}$. Suy ra tọa độ các điểm đầu mút là: $A(-1; 0), \\quad B(1; 0)$.\\\\
                         Điểm $I$ nằm trên trục tung phía dưới trục hoành nên $I(0; y_I)$ với $y_I < 0$. Xét tam giác $IOA$ vuông tại $O$, áp dụng định lý Pytago:\\\\
                         $OI = \\sqrt{IA^2 - OA^2} = \\sqrt{(\\sqrt{5})^2 - 1^2} = 2 \\Rightarrow I(0; -2)$.\\\\
                         Tương tự, điểm $J$ cũng nằm trên trục tung dưới trục hoành nên $J(0; y_J)$ với $y_J < 0$. Xét tam giác $JOA$ vuông tại $O$:\\\\
                         $OJ = \\sqrt{JA^2 - OA^2} = \\sqrt{\\left(\\frac{\\sqrt{13}}{2}\\right)^2 - 1^2} = \\sqrt{\\frac{13}{4} - 1} = \\frac{3}{2} = 1{,}5 \\Rightarrow J(0; -1{,}5)$.\\\\
                         Parabol có đỉnh $I(0; -2)$ nên dạng tổng quát là $y = ax^2 - 2$. Vì $(P)$ đi qua $B(1; 0)$, ta có:\\\\
                         $0 = a(1)^2 - 2 \\Rightarrow a = 2 \\Rightarrow (P): y = 2x^2 - 2$.\\\\
                         Đường thẳng đi qua $J(0; -1{,}5)$ và $B(1; 0)$ có hệ số góc $k = \\frac{0 - (-1{,}5)}{1 - 0} = 1{,}5$. Phương trình của đoạn thẳng này ứng với $x \\ge 0$ là: $y = 1{,}5x - 1{,}5$.\\\\
                         Đường tròn đi qua 3 điểm $A, B, I$. Do tính đối xứng, tâm đường tròn là $K(0; m)$ nằm trên trục $Oy$. Gọi $R$ là bán kính đường tròn, ta có phương trình hệ thức khoảng cách:\\\\
                         $KB^2 = KI^2 \\Leftrightarrow 1^2 + (0 - m)^2 = 0^2 + (-2 - m)^2 \\Leftrightarrow m^2 + 1 = m^2 + 4m + 4 \\Rightarrow 4m = -3 \\Rightarrow m = -0{,}75$.\\\\
                         Bình phương bán kính là: $R^2 = m^2 + 1 = (-0{,}75)^2 + 1 = \\frac{25}{16}$.\\\\
                         Diện tích toàn bộ hình tròn lô gô là: $S_{\\text{tròn}} = \\pi R^2 = \\frac{25\\pi}{16} \\text{ (m}^2\\text{)}$.\\\\
                         Là phần giới hạn bởi Parabol $(P)$ và đường gấp khúc $AJB$. Sử dụng tính đối xứng qua trục $Oy$, ta tính trên miền $x \\in [0;1]$ rồi nhân đôi:\\\\
                         $S_{\\text{bạc}} = 2 \\int_{0}^{1} \\left[ (1{,}5x - 1{,}5) - (2x^2 - 2) \\right] \\text{d}x = 2 \\int_{0}^{1} (-2x^2 + 1{,}5x + 0{,}5) \\text{d}x = \\frac{7}{6} \\text{ (m}^2\\text{)}$.\\\\
                         Diện tích phần phủ sơn ($S_{\\text{sơn}}$):\\\\
                         $S_{\\text{sơn}} = S_{\\text{tròn}} - S_{\\text{bạc}} = \\frac{25\\pi}{16} - \\frac{7}{6} \\text{ (m}^2\\text{)}$.\\\\
                         Tổng chi phí $T$ (triệu đồng) được tính theo công thức:\\\\
                         $T = %s \\times S_{\\text{bạc}} + %s \\times S_{\\text{sơn}} = %s \\left(\\frac{7}{6}\\right) + %s \\left(\\frac{25\\pi}{16} - \\frac{7}{6}\\right) \\approx %s \\text{ (triệu đồng)}$.\\\\
                         Làm tròn kết quả đến hàng phần chục theo yêu cầu đề bài, ta được số tiền là: $%s$ triệu đồng.'''
                         %(latex(c1), latex(c2), latex(c1), latex(c2), kq_detail, kq)
                         )
                dapan='\\shortans[0]{$%s$}\n'%(kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

