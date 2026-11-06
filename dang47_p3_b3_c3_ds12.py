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


def bt_dang47_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số của bài toán
                h0 = random.choice([20, 25, 30, 35, 40]) # Nửa chiều cao
                h = 2 * h0 # Chiều cao đôn

                r_min = random.choice([10, 12, 14, 15, 16]) # Bán kính eo nhỏ nhất
                d_min = 2 * r_min # Đường kính eo

                r_max = r_min + random.choice([4, 5, 6, 8, 10]) # Bán kính đáy/mặt
                d_max = 2 * r_max # Đường kính đáy/mặt

                d_copper = 8960 # Khối lượng riêng (cố định theo thực tế)
                price_k = random.choice([200, 220, 250, 280, 300]) # Giá đồng (nghìn VNĐ/kg)
                cost_m = random.choice([5, 8, 10, 12, 15]) # Chi phí gia công (triệu VNĐ)

                # Tính toán các hệ số của Parabol y = ax^2 + c
                tu_a = r_max - r_min
                mau_a = h0**2
                a = Rational(tu_a, mau_a)
                c = r_min

                # Tính tích phân thể tích (chưa nhân pi)
                fx = a * x**2 + c
                fx_sq = fx**2
                integral_val = integrate(fx_sq, (x, -h0, h0))

                # Tính tổng chi phí
                # Thể tích (m^3) = integral_val * pi * 10^-6
                # Chi phí vật liệu (triệu) = V(m^3) * 8960 * (price_k * 1000) / 1,000,000 = V(m^3) * 8960 * price_k * 10^-3
                cost_mat_mil = float(integral_val) * math.pi * 10**(-6) * d_copper * price_k * 10**(-3)
                total_cost = cost_mat_mil + cost_m

                # Làm tròn kết quả giống mẫu
                kq3 = Decimal(float(total_cost)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.',',')

                kq4 = round(total_cost, 1)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da= random.choice(du)

                # Sinh phương án nhiễu (sai lệch so với đáp án đúng)
                s = ['$%s$'%(str(Decimal(float(kq4 + random.choice([1.2, 2.3, 3.1]))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq4 + random.choice([4.5, 5.2, 6.7]))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq4 - random.choice([1.5, 2.1, 3.4]))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq4 - random.choice([4.2, 5.8, 6.1]))).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq4 * 1.05)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq4 * 0.95)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)).replace('.',','))
                    ]

                # Loại bỏ trùng lặp nếu có
                s = list(set(s))
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\tikzset {_u2knrdes8/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-194 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_s13w4a3d6}{150bp}{rgb(0bp)=(0,0,0);
            	rgb(39.373888288225444bp)=(0,0,0);
            	rgb(43.821427481515066bp)=(0.72,0.38,0.16);
            	rgb(47.30357033865792bp)=(0.91,0.76,0.62);
            	rgb(48.78348214285714bp)=(0.91,0.79,0.68);
            	rgb(56.75000054495675bp)=(0.72,0.38,0.16);
            	rgb(62.24999836512974bp)=(0.45,0.23,0.04);
            	rgb(100bp)=(0.45,0.23,0.04)}
            \tikzset {_snjbu4bey/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-147 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_u96nmdahi}{150bp}{rgb(0bp)=(0.55,0.34,0.16);
            	rgb(37.5bp)=(0.55,0.34,0.16);
            	rgb(50bp)=(0.92,0.71,0.51);
            	rgb(62.5bp)=(0.55,0.34,0.16);
            	rgb(100bp)=(0.55,0.34,0.16)}
            \tikzset {_r6thhgh57/.code = {\pgfsetadditionalshadetransform{ \pgftransformshift{\pgfpoint{0 bp } { 0 bp }  }  \pgftransformrotate{-167 }  \pgftransformscale{2 }  }}}
            \pgfdeclarehorizontalshading{_ld5nyomil}{150bp}{rgb(0bp)=(0,0,0);
            	rgb(37.785712650844026bp)=(0,0,0);
            	rgb(42.10602624075753bp)=(0.72,0.38,0.16);
            	rgb(46.17633819580078bp)=(0.93,0.84,0.76);
            	rgb(55.303570883614675bp)=(0.72,0.38,0.16);
            	rgb(62.5bp)=(0.34,0.18,0.02);
            	rgb(100bp)=(0.34,0.18,0.02)}
            \tikzset{every picture/.style={line width=0.75pt}} 
                \path  [shading=_s13w4a3d6,_u2knrdes8] (131.3,64.9) .. controls (163.8,57.4) and (270.3,51.9) .. (285.8,66.4) .. controls (276.8,87.9) and (256.18,115.39) .. (257.3,153.9) .. controls (258.26,186.75) and (277.59,220.09) .. (286.8,233.9) .. controls (287.8,271.4) and (140.8,272.4) .. (134.3,237.4) .. controls (149.8,211.4) and (165.18,189.44) .. (163.8,151.9) .. controls (162.29,110.86) and (140.3,84.4) .. (131.3,64.9) -- cycle ; 
            	\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.42 ] (131.3,64.9) .. controls (163.8,57.4) and (270.3,51.9) .. (285.8,66.4) .. controls (276.8,87.9) and (256.18,115.39) .. (257.3,153.9) .. controls (258.26,186.75) and (277.59,220.09) .. (286.8,233.9) .. controls (287.8,271.4) and (140.8,272.4) .. (134.3,237.4) .. controls (149.8,211.4) and (165.18,189.44) .. (163.8,151.9) .. controls (162.29,110.86) and (140.3,84.4) .. (131.3,64.9) -- cycle ; 
            	\path  [shading=_u96nmdahi,_snjbu4bey] (131.3,65.4) .. controls (131.3,54.91) and (165.89,46.4) .. (208.55,46.4) .. controls (251.21,46.4) and (285.8,54.91) .. (285.8,65.4) .. controls (285.8,75.89) and (251.21,84.4) .. (208.55,84.4) .. controls (165.89,84.4) and (131.3,75.89) .. (131.3,65.4) -- cycle ; 
            	\draw  [color={rgb, 255:red, 161; green, 84; blue, 15 }  ,draw opacity=1 ] (131.3,65.4) .. controls (131.3,54.91) and (165.89,46.4) .. (208.55,46.4) .. controls (251.21,46.4) and (285.8,54.91) .. (285.8,65.4) .. controls (285.8,75.89) and (251.21,84.4) .. (208.55,84.4) .. controls (165.89,84.4) and (131.3,75.89) .. (131.3,65.4) -- cycle ; 
            	\draw  [draw opacity=0][shading=_ld5nyomil,_r6thhgh57] (257.3,153.9) .. controls (258.26,186.75) and (277.59,220.09) .. (286.8,233.9) .. controls (287.8,271.4) and (140.8,272.4) .. (134.3,237.4) .. controls (149.8,211.4) and (165.18,189.44) .. (163.8,151.9) .. controls (184.6,190.4) and (257.1,171.4) .. (257.3,153.9) -- cycle ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.78 ]   (240.65,82.9) .. controls (250.9,81.4) and (255.15,81.15) .. (264.9,78.15) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.26 ][line width=6]    (149.2,107.2) .. controls (184.7,172.7) and (146.7,229.7) .. (130.7,246.2) ;
            	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.26 ][line width=6]    (283.7,82.2) .. controls (230.7,145.7) and (272.2,228.2) .. (290.2,246.2) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.18 ] (177.2,122.7) .. controls (198.2,195.7) and (188.2,251.7) .. (178.7,264.2) .. controls (198.7,294.2) and (174.2,289.7) .. (154.2,259.7) .. controls (189.2,197.7) and (181.7,180.7) .. (177.2,122.7) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.18 ] (230.7,127.2) .. controls (214.7,208.2) and (282.2,257.7) .. (272.7,270.2) .. controls (292.7,300.2) and (254.2,301.2) .. (234.2,271.2) .. controls (222.7,213.7) and (216.2,189.7) .. (230.7,127.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.52 ] (228.2,171.2) .. controls (235.7,251.2) and (265.7,251.2) .. (256.2,263.7) .. controls (247.2,270.7) and (269.7,272.2) .. (248.7,267.2) .. controls (236.2,230.2) and (228.2,230.2) .. (228.2,171.2) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.18 ] (186.2,177.2) .. controls (192.7,221.2) and (186.2,257.2) .. (176.7,269.7) .. controls (196.7,299.7) and (186.2,296.2) .. (166.2,266.2) .. controls (176.2,249.7) and (181.7,235.2) .. (186.2,177.2) -- cycle ;
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một nghệ nhân tại làng nghề đúc đồng, nhận chế tác các mẫu đôn trang trí cao cấp bằng đồng. Mỗi chiếc đôn có dạng khối tròn xoay đặc, cao $%s$ cm, với thiết kế mềm mại và cân đối quanh một trục thẳng đứng. Khi cắt chiếc đôn bởi một mặt phẳng bất kỳ đi qua trục đối xứng, ta thu được một thiết diện giới hạn bởi hai đường parabol đối xứng nhau qua trục này. Theo yêu cầu thiết kế: Mặt trên và mặt đáy của đôn đều là hình tròn có đường kính $%s$ cm; phần thân được bo thon đều về phía trung tâm, tại đó đường kính nhỏ nhất là $%s$ cm. Biết khối lượng riêng của đồng là $%s$ kg/m$^3$, giá đồng là $%s$ nghìn đồng/kg và chi phí gia công cho mỗi sản phẩm là $%s$ triệu đồng (lượng đồng hao hụt trong quá trình gia công được xem là không đáng kể). Tổng chi phí để hoàn thiện một chiếc đôn theo thiết kế trên là bao nhiêu triệu đồng? (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng đơn vị).}{%s}'''
                                 %(h, d_max, d_min, d_copper, price_k, cost_m,hinhve))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Chuẩn bị hiển thị phương trình
                str_a = latex(a)
                if a == 1:
                    str_a = ""

                # Nội dung lời giải
                loigiai= ('''Chọn hệ trục tọa độ $Oxy$ sao cho trục $Ox$ là trục đối xứng của chiếc đôn, gốc tọa độ $O$ nằm tại tâm của phần eo nhỏ nhất (như hình vẽ). 
                          \\begin{center}
                          	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                          		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  (182.09,230.79) .. controls (174.64,198.28) and (169.31,91.77) .. (183.83,76.29) .. controls (205.32,85.32) and (232.78,105.99) .. (271.29,104.93) .. controls (304.13,104.02) and (337.51,84.74) .. (351.33,75.55) .. controls (388.83,74.61) and (389.6,221.61) .. (354.59,228.06) .. controls (328.62,212.52) and (306.68,197.1) .. (269.14,198.42) .. controls (228.1,199.87) and (201.6,221.82) .. (182.09,230.79) -- cycle ;
                          		\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (182.58,230.79) .. controls (170.98,230.85) and (161.41,196.31) .. (161.2,153.64) .. controls (161,110.98) and (170.23,76.35) .. (181.83,76.29) .. controls (193.42,76.24) and (202.99,110.78) .. (203.2,153.44) .. controls (203.41,196.1) and (194.18,230.73) .. (182.58,230.79) -- cycle ;
                          		\\draw [line width=1]    (182.71,153.54) -- (127.2,154.13) ;
                          		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (381.2,149.47) -- (182.71,153.54) ;
                          		\\draw [line width=1]    (279.2,106.13) -- (278.57,38.13) ;
                          		\\draw [shift={(278.53,34.13)}, rotate = 89.47] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                          		\\draw [line width=1]    (279.2,242.13) -- (279.2,197.47) ;
                          		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (279.2,106.13) -- (279.2,197.47) ;
                          		\\draw [line width=1]    (381.2,149.47) -- (427.87,150.08) ;
                          		\\draw [shift={(431.87,150.13)}, rotate = 180.75] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
                          		\\draw [line width=1]    (181.71,153.54) -- (181.83,76.29) ;
                          		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (354.21,152.8) -- (354.33,75.55) ;
                          		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (182.83,76.29) -- (351.33,75.55) ;
                          		\\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (357.52,228.51) .. controls (357.31,228.53) and (357.09,228.54) .. (356.87,228.54) .. controls (343.43,228.54) and (332.53,194.63) .. (332.53,152.8) .. controls (332.53,110.98) and (343.43,77.07) .. (356.87,77.07) .. controls (357.09,77.07) and (357.31,77.08) .. (357.52,77.1) -- (356.87,152.8) -- cycle ; \\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (357.52,228.51) .. controls (357.31,228.53) and (357.09,228.54) .. (356.87,228.54) .. controls (343.43,228.54) and (332.53,194.63) .. (332.53,152.8) .. controls (332.53,110.98) and (343.43,77.07) .. (356.87,77.07) .. controls (357.09,77.07) and (357.31,77.08) .. (357.52,77.1) ;  
                          		\\draw (260,155) node [anchor=north west][inner sep=0.75pt]    {$O$};
                          		\\draw (409.33,159) node [anchor=north west][inner sep=0.75pt]    {$x$};
                          		\\draw (262,33) node [anchor=north west][inner sep=0.75pt]    {$y$};
                          		\\draw (264.67,84.33) node [anchor=north west][inner sep=0.75pt]    {$I$};
                          		\\draw (345.33,55) node [anchor=north west][inner sep=0.75pt]    {$A$};
                          	\\end{tikzpicture}
                          \\end{center}
            Mặt cắt của chiếc đôn là hình phẳng giới hạn bởi hai đường parabol. Ta xét đường parabol $\\left(P\\right)$ nằm phía trên trục $Ox$.\\\\
            Theo đề bài, $\\left(P\\right)$ có đỉnh $I\\left(0; %s\\right)$ và đi qua điểm $A\\left(%s; %s\\right)$ (do chiều cao đôn là $%s$ cm, đường kính đáy là $%s$ cm nên bán kính là $%s$ cm).\\\\
            Giả sử phương trình của $\\left(P\\right)$ có dạng $y = ax^2 + c$.\\\\
            Vì $\\left(P\\right)$ có đỉnh $I\\left(0; %s\\right)$ nên $c = %s$. Do đó $y = ax^2 + %s$.\\\\
            Mặt khác, $\\left(P\\right)$ đi qua $A\\left(%s; %s\\right)$ nên ta có:\\\\
            $ %s = a \\cdot %s^2 + %s \\Rightarrow a = %s$.\\\\
            Suy ra phương trình của $\\left(P\\right)$ là: $y = %s x^2 + %s$.\\\\
            Thể tích của chiếc đôn (là khối tròn xoay khi quay phần mặt cắt quanh trục $Ox$) được tính bằng công thức:\\\\
            $V = \\pi \\int_{-%s}^{%s} \\left(%s x^2 + %s\\right)^2 \\text{d}x = %s\\pi \\text{ } \\left(\\text{cm}^3\\right)$.\\\\
            Đổi đơn vị: $V = %s\\pi \\cdot 10^{-6} \\text{ } \\left(\\text{m}^3\\right)$.\\\\
            Khối lượng của chiếc đôn là:\\\\
            $m = D \\cdot V = %s \\cdot %s\\pi \\cdot 10^{-6} \\text{ } \\left(\\text{kg}\\right)$.\\\\
            Chi phí tiền đồng để đúc chiếc đôn là:\\\\
            $T_1 = m \\cdot %s \\cdot 10^{-3} = %s \\cdot %s\\pi \\cdot 10^{-6} \\cdot %s \\cdot 10^{-3} \\text{ } \\left(\\text{triệu đồng}\\right)$.\\\\
            Tổng chi phí để hoàn thiện chiếc đôn là (cộng thêm $%s$ triệu tiền công):\\\\
            $T = T_1 + %s = %s \\cdot %s\\pi \\cdot 10^{-6} \\cdot %s \\cdot 10^{-3} + %s \\approx %s \\text{ } \\left(\\text{triệu đồng}\\right)$.'''
                          %(c, h0, r_max, h, d_max, r_max, c, c, c, h0, r_max, r_max, h0, c, latex(a), str_a, c,
                            h0, h0, str_a, c, latex(integral_val), latex(integral_val),
                            d_copper, latex(integral_val),
                            price_k, d_copper, latex(integral_val), price_k, cost_m, cost_m,
                            d_copper, latex(integral_val), price_k, cost_m, kq))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

