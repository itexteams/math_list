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


def bt_dang77_p3_b3_c3_ds12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # B3: Random hóa bài toán
        x1 = random.choice([-10, -8, -6])
        x2 = random.choice([20, 16, 12])
        y1 = random.choice([2, 3, 4])
        d = random.choice([2, 3, 4]) # Chênh lệch tung độ tại x=0
        y2 = y1 + d
        R = random.choice([25, 30, 35])

        # Tính hệ số k của hàm hiệu f(x) - g(x) = k(x - x1)(x - x2)
        # Tại x = 0: f(0) - g(0) = d => k * (-x1) * (-x2) = d => k = d / (x1 * x2)
        k = Rational(d, x1 * x2)

        # Tính diện tích 1 dải sóng màu trắng (Tích phân)
        # S1 = tích phân từ x1 đến x2 của k*(x - x1)*(x - x2) dx = -k * (x2 - x1)^3 / 6
        S1 = -k * Rational((x2 - x1)**3, 6)

        # Diện tích 4 dải sóng màu trắng
        S4 = 4 * S1

        # Diện tích hình tròn và diện tích màu xanh
        S_exact = pi * R**2 - S4
        S_val = float(N(S_exact))

        # Làm tròn đến hàng đơn vị bằng Decimal và ROUND_HALF_UP
        kq_dec = Decimal(str(S_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        kq = str(kq_dec)

        # B4: Điều chỉnh các phương án sai không trùng đáp án đúng
        da = '$%s$' % kq
        offset_list = [-120, -80, -40, 40, 80, 120, 160]
        s_list = []
        for off in offset_list:
            val_wrong = Decimal(str(S_val + off)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
            s_list.append('$%s$' % str(val_wrong))

        # Lọc đáp án trùng với đáp án đúng
        s_filtered = list(set([ans for ans in s_list if ans != da]))

        das1 = random.choice(s_filtered)
        s_filtered.remove(das1)
        das2 = random.choice(s_filtered)
        s_filtered.remove(das2)
        das3 = random.choice(s_filtered)

        # Các đáp án trắc nghiệm
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Hỗ trợ định dạng dấu cho lời giải
        sign_x1 = f"+ {-x1}"
        sign_x2 = f"- {x2}"

        # Nội dung câu hỏi (đã bỏ phần hình vẽ và câu dẫn tham chiếu hình)
        noidungcauhoi = ('''Một biểu trưng (logo) có dạng hình tròn với bán kính $R = %s$ cm có nền màu xanh. Ở chính giữa logo có $4$ hình dải sóng màu trắng giống hệt nhau. Mỗi dải sóng màu trắng được giới hạn bởi hai đường cong là đồ thị của hai hàm số $y = f(x)$ và $y = g(x)$. Trên hệ trục tọa độ $Oxy$, hai đồ thị cắt nhau tại hai điểm có hoành độ $x = %s$ và $x = %s$, đồng thời cắt trục tung tại các điểm có tung độ lần lượt là $y = %s$ và $y = %s$. Diện tích phần nền màu xanh của logo bằng bao nhiêu? (đơn vị: cm$^2$, làm tròn đến hàng đơn vị).
                         \\begin{center}
                         	\\tikzset{every picture/.style={line width=0.75pt}}       
                         	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                            \\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (330.32,140.72) .. controls (358.72,105.52) and (403.1,128.72) .. (425.12,134.72) .. controls (459.12,143.12) and (484.32,152.72) .. (522.72,127.92) .. controls (486.32,160.72) and (455.92,156.32) .. (427.38,146.32) .. controls (395.64,139.12) and (370.72,111.92) .. (330.32,140.72) -- cycle ;
                            	\\draw [line width=1]    (308.32,174.32) .. controls (339.92,103.12) and (381.12,118.72) .. (435.92,137.92) .. controls (490.72,157.12) and (535.6,129.97) .. (556.72,87.92) ;
                            	\\draw [line width=1]    (302.32,171.12) .. controls (345.52,107.92) and (376.72,127.12) .. (429.52,147.12) .. controls (482.32,167.12) and (524.72,142.32) .. (556.32,82.72) ;
                            	\\draw [line width=1]    (301.52,154.16) -- (553.92,154.51) ;
                            	\\draw [shift={(557.92,154.52)}, rotate = 180.08] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                            	\\draw [line width=1]    (397.52,178.32) -- (397.14,81.12) ;
                            	\\draw [shift={(397.12,77.12)}, rotate = 89.77] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (6.43,-3.09) -- (0,0) -- (6.43,3.09) -- (4.27,0) -- cycle    ;
                            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (329.92,145.16) -- (329.52,155.12) ;
                            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (523.92,131.56) -- (523.92,155.12) ;
                            	\\draw  [draw opacity=0][fill={rgb, 255:red, 19; green, 159; blue, 128 }  ,fill opacity=1 ] (42.6,134.73) .. controls (42.6,78.58) and (88.12,33.07) .. (144.27,33.07) .. controls (200.42,33.07) and (245.93,78.58) .. (245.93,134.73) .. controls (245.93,190.88) and (200.42,236.4) .. (144.27,236.4) .. controls (88.12,236.4) and (42.6,190.88) .. (42.6,134.73) -- cycle ;
                            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (90.44,105.41) .. controls (105.51,86.73) and (129.06,99.04) .. (140.75,102.23) .. controls (158.79,106.68) and (172.16,111.78) .. (192.53,98.62) .. controls (173.22,116.02) and (157.09,113.69) .. (141.95,108.38) .. controls (125.1,104.56) and (111.88,90.13) .. (90.44,105.41) -- cycle ;
                            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (90.44,123.99) .. controls (105.51,105.31) and (129.06,117.62) .. (140.75,120.81) .. controls (158.79,125.26) and (172.16,130.36) .. (192.53,117.2) .. controls (173.22,134.6) and (157.09,132.27) .. (141.95,126.96) .. controls (125.1,123.14) and (111.88,108.71) .. (90.44,123.99) -- cycle ;
                            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (89.65,143.73) .. controls (104.72,125.05) and (128.27,137.36) .. (139.96,140.54) .. controls (158,145) and (171.37,150.09) .. (191.74,136.93) .. controls (172.43,154.34) and (156.3,152) .. (141.16,146.7) .. controls (124.31,142.88) and (111.09,128.44) .. (89.65,143.73) -- cycle ;
                            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (90.44,162.67) .. controls (105.51,143.99) and (129.06,156.3) .. (140.75,159.49) .. controls (158.79,163.95) and (172.16,169.04) .. (192.53,155.88) .. controls (173.22,173.28) and (157.09,170.95) .. (141.95,165.64) .. controls (125.1,161.82) and (111.88,147.39) .. (90.44,162.67) -- cycle ;
                         		\\draw (382.32,154.36) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$O$};
                         		\\draw (314.32,156.36) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$};
                         		\\draw (454.32,156.36) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$};
                         		\\draw (515.92,154.36) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$};
                         		\\draw (387.12,137.56) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$};
                         		\\draw (396.72,110.36) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$%s$};
                         		\\draw (381.92,75.56) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$y$};
                         		\\draw (546.32,137.96) node [anchor=north west][inner sep=0.75pt]  [font=\\scriptsize]  {$x$};
                         	\\end{tikzpicture}
                         \\end{center}'''
                         % (latex(R),
                            latex(x1),
                            latex(x2),
                            latex(y2),
                            latex(y1),
                            latex(x1),latex(-x1),latex(x2),latex(y1),latex(y2)
                            ))

        # Lời giải chi tiết
        loigiai = ('''Gọi hai hàm số giới hạn một dải sóng màu trắng là $y = f(x)$ và $y = g(x)$ (với $f(x) \\ge g(x)$ trên đoạn $[%s; %s]$). \\\\
    Vì hai đồ thị cắt nhau tại $x = %s$ và $x = %s$ nên hàm hiệu $f(x) - g(x) = k(x %s)(x %s)$ (với $k < 0$). \\\\
    Tại $x = 0$, hai đồ thị cắt trục tung tại các điểm có tung độ $y = %s$ và $y = %s$, suy ra: \\\\
    $f(0) - g(0) = %s - %s = %s \\Leftrightarrow k(0 %s)(0 %s) = %s \\Leftrightarrow k = %s$. \\\\
    Do đó, $f(x) - g(x) = %s(x %s)(x %s)$. \\\\
    Diện tích của $1$ dải sóng màu trắng là: \\\\
    $S_1 = \\int_{%s}^{%s} (f(x) - g(x)) \\text{d}x = \\int_{%s}^{%s} \\left[%s(x %s)(x %s)\\right] \\text{d}x = %s \\text{ (cm}^2\\text{)}$. \\\\
    Diện tích của $4$ dải sóng màu trắng là: \\\\
    $S_4 = 4 \\cdot S_1 = 4 \\cdot %s = %s \\text{ (cm}^2\\text{)}$. \\\\
    Diện tích của logo hình tròn bán kính $R = %s$ cm là: \\\\
    $S_{\\text{tròn}} = \\pi R^2 = \\pi \\cdot %s^2 = %s\\pi \\approx %s \\text{ (cm}^2\\text{)}$. \\\\
    Diện tích phần nền màu xanh của logo là: \\\\
    $S_{\\text{xanh}} = S_{\\text{tròn}} - S_4 = %s\\pi - %s \\approx %s \\text{ (cm}^2\\text{)}$. \\\\
    Làm tròn đến hàng đơn vị ta được kết quả là $%s$.'''
                   % (latex(x1), latex(x2),
                      latex(x1), latex(x2), sign_x1, sign_x2,
                      latex(y2), latex(y1),
                      latex(y2), latex(y1), latex(d), sign_x1, sign_x2, latex(d), latex(k),
                      latex(k), sign_x1, sign_x2,
                      latex(x1), latex(x2), latex(x1), latex(x2), latex(k), sign_x1, sign_x2, latex(S1),
                      latex(S1), latex(S4),
                      latex(R), latex(R), latex(R**2), str(Decimal(str(float(N(pi * R**2)))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)),
                      latex(R**2), latex(S4), kq,
                      kq
                      ))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
               '\\loigiai{\n' + str(loigiai) + '\n}\n'
               '\\end{ex}\n\\end{minipage} \n\n')
    return content

