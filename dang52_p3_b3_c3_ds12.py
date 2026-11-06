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


def bt_dang52_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Hệ số k dùng để random kích thước nhưng vẫn giữ nguyên hình dáng tương đồng
                k = random.choice([1, 2])

                OA = 4 * k
                OB = 10 * k
                OC_coeff = 10 * k

                # Toạ độ các điểm A, B
                xA = 2 * k
                yA = 2 * k
                xB = 5 * k
                yB = 5 * k

                # Tâm I của cung tròn
                xI_coeff = 17 * k
                yI = -3 * k

                # Bán kính R
                R_coeff = 14 * k
                R2_coeff = 196 * (k**2)

                # Hệ số diện tích
                coeff_arcsin = 784 * (k**2)
                coeff_sqrt3 = 156 * (k**2)

                val_arcsin = math.asin(13/14)
                val_sqrt3 = math.sqrt(3)

                exact_area = coeff_arcsin * val_arcsin - coeff_sqrt3 * val_sqrt3
                exact_area_dec = Decimal(str(exact_area)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq = str(exact_area_dec).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án nhiễu sai khác nhau
                s = []
                offsets = [10, -10, 20, -20, 30, -30]
                for off in offsets:
                    fake_val = exact_area + off * (k**2)
                    fake_dec = Decimal(str(fake_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    s.append('$%s$' % str(fake_dec).replace('.', ','))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Hình vẽ TikZ (Được cố định tỷ lệ vẽ để luôn hiển thị đẹp và chuẩn khung hình)
                hinhve = r'''\scalebox{0.8}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [line width=1]  (68.14,145.89) .. controls (68.14,77.14) and (123.88,21.41) .. (192.62,21.41) .. controls (261.37,21.41) and (317.11,77.14) .. (317.11,145.89) .. controls (317.11,214.64) and (261.37,270.37) .. (192.62,270.37) .. controls (123.88,270.37) and (68.14,214.64) .. (68.14,145.89) -- cycle ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (84.82,207.68) .. controls (142.61,225.18) and (178.26,204.5) .. (191.78,145.65) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (193.71,146.13) .. controls (153.36,187.71) and (153.52,229.12) .. (194.21,270.38) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (84.24,83.44) .. controls (100.34,140.58) and (136.74,160.34) .. (193.43,142.7) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (194.56,21.66) .. controls (150.28,62.72) and (150,104.08) .. (193.72,145.74) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (300,83.73) .. controls (242.53,68.85) and (207.12,90.34) .. (193.79,148.19) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (300.83,208.71) .. controls (286.68,151.05) and (250.98,130.06) .. (193.72,145.74) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (193.43,142.7) .. controls (208.35,198.69) and (243.97,219.83) .. (300.26,206.13) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (192.62,270.37) .. controls (233.5,229.32) and (233.86,187.9) .. (193.71,146.13) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (192.45,145.63) .. controls (136.2,131.75) and (100.52,152.77) .. (85.41,208.71) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (191.78,145.65) .. controls (176.22,89.84) and (140.38,69.1) .. (84.24,83.44) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (193.71,146.13) .. controls (234.08,104.58) and (233.93,63.17) .. (193.28,21.89) ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (193.72,145.74) .. controls (249.92,159.82) and (285.67,138.92) .. (300.98,83.04) ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (131.55,148.19) .. controls (131.55,113.81) and (159.41,85.95) .. (193.79,85.95) .. controls (228.16,85.95) and (256.03,113.81) .. (256.03,148.19) .. controls (256.03,182.56) and (228.16,210.43) .. (193.79,210.43) .. controls (159.41,210.43) and (131.55,182.56) .. (131.55,148.19) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (163.86,148.19) .. controls (163.86,131.66) and (177.26,118.26) .. (193.79,118.26) .. controls (210.31,118.26) and (223.71,131.66) .. (223.71,148.19) .. controls (223.71,164.72) and (210.31,178.12) .. (193.79,178.12) .. controls (177.26,178.12) and (163.86,164.72) .. (163.86,148.19) -- cycle ;
            	\draw  [line width=1]  (62.5,145.63) .. controls (62.5,73.86) and (120.68,15.68) .. (192.45,15.68) .. controls (264.22,15.68) and (322.4,73.86) .. (322.4,145.63) .. controls (322.4,217.4) and (264.22,275.58) .. (192.45,275.58) .. controls (120.68,275.58) and (62.5,217.4) .. (62.5,145.63) -- cycle ;
            	\draw [line width=1]    (193.79,148.19) -- (300,83.73) ;
            	\draw [line width=1]    (194.76,147.49) -- (224.14,93.05) ;
            	\draw (179.33,144.07) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (194.67,102) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (207.33,72) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (304.67,62.73) node [anchor=north west][inner sep=0.75pt]    {$C$};	
            \end{tikzpicture} }'''

                # Câu hỏi
                noidungcauhoi = (r'''\immini{Tại trung tâm phường Pleiku, người ta quy hoạch một vòng xuyến ngã 6 với điểm nhấn là một vòng xuyến giao thông gồm 6 cánh hoa giống hệt nhau, được sắp xếp đối xứng qua tâm vòng xuyến $O$.\\
            Để đảm bảo tính thẩm mỹ và độ chính xác cao khi thi công, các kiến trúc sư thiết kế hình dạng của mỗi cánh hoa dựa trên các cung tròn. Xét một cánh hoa bất kỳ:\\
            + Mỗi bên biên của cánh hoa là một cung tròn được xác định duy nhất bằng cách đi qua ba điểm mốc kỹ thuật ký hiệu là $A, B, C$.\\
            + Điểm $C$ là đỉnh xa nhất của cánh hoa, nằm trên trục đối xứng của cánh hoa đó và cách tâm $O$ một khoảng $%s\sqrt{3}$ mét.}{%s}
            + Hai điểm $A$ và $B$ nằm trên biên cánh hoa sao cho các tia $OA$ và $OB$ cùng tạo với trục đối xứng của cánh hoa một góc $30^\circ$.\\
            + Qua đo đạc thực tế, khoảng cách từ tâm $O$ đến điểm $A$ là $%s$ mét và đến điểm $B$ là $%s$ mét.\\
            Diện tích (đơn vị: $\text{m}^2$) toàn bộ cánh hoa nói trên (gồm 6 cánh hoa) bằng bao nhiêu? (Kết quả làm tròn đến chữ số hàng đơn vị).'''% (OC_coeff, hinhve, OA, OB))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tính toán các biến phụ cho phần Tích phân
                lim1 = 4 * k
                abs_yI = abs(yI)

                # Nội dung lời giải theo Tích phân
                loigiai = ('''Chọn hệ trục tọa độ $Oxy$ sao cho $O$ là tâm vòng xuyến, tia $Ox$ chứa trục đối xứng của một cánh hoa.\\\\
            Điểm $C$ nằm trên $Ox$ và $OC = %s\\sqrt{3}$ nên $C\\left(%s\\sqrt{3}; 0\\right)$.\\\\
            Các tia $OA, OB$ tạo với $Ox$ góc $30^\\circ$ và $OA = %s, OB = %s$ nên $A\\left(%s\\sqrt{3}; %s\\right)$ và $B\\left(%s\\sqrt{3}; %s\\right)$.\\\\
            Gọi phương trình đường tròn $\\left(T\\right)$ đi qua $A, B, C$ là $x^2 + y^2 - 2ax - 2by + d = 0$.\\\\
            Thay tọa độ $A, B, C$ vào phương trình $\\left(T\\right)$, ta tìm được tâm $I\\left(\\frac{%s\\sqrt{3}}{3}; %s\\right)$ và bán kính $R = \\frac{%s\\sqrt{3}}{3}$.\\\\
            Phương trình đường tròn $\\left(T\\right)$ là: $\\left(x - \\frac{%s\\sqrt{3}}{3}\\right)^2 + \\left(y + %s\\right)^2 = \\frac{%s}{3}$.\\\\
            Phần biên phía trên trục $Ox$ ($y \\ge 0$) của cánh hoa có phương trình là:\\\\ $y = -%s + \\sqrt{\\frac{%s}{3} - \\left(x - \\frac{%s\\sqrt{3}}{3}\\right)^2}$.\\\\
            Hoành độ giao điểm của cung tròn này với trục $Ox$ là nghiệm của phương trình $y = 0$, giải ra ta được $x_1 = \\frac{%s\\sqrt{3}}{3}$ và $x_2 = %s\\sqrt{3}$.\\\\
            Diện tích của toàn bộ 6 cánh hoa (bằng 12 lần diện tích nửa cánh hoa phía trên $Ox$) được tính bằng ứng dụng tích phân:\\\\
            $S = 12 \\int\\limits_{\\frac{%s\\sqrt{3}}{3}}^{%s\\sqrt{3}} \\left( -%s + \\sqrt{\\frac{%s}{3} - \\left(x - \\frac{%s\\sqrt{3}}{3}\\right)^2} \\right) \\mathrm{d}x \\approx %s \\left(\\text{m}^2\\right)$.'''
                           % (OC_coeff, OC_coeff,
                              OA, OB, xA, yA, xB, yB,
                              xI_coeff, yI, R_coeff,
                              xI_coeff, abs_yI, R2_coeff,
                              abs_yI, R2_coeff, xI_coeff,
                              lim1, OC_coeff,
                              lim1, OC_coeff, abs_yI, R2_coeff, xI_coeff, kq))

                dapan = '\\shortans[0]{$%s$}\n' % (kq)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}   \\end{minipage} \n\n')
            return content  

