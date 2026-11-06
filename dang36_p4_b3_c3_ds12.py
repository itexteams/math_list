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


def bt_dang36_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # a_cm: Nửa độ dài trục lớn (40 cm -> 4 dm)
                # b_cm: Nửa độ dài trục bé (30 cm -> 3 dm)
                # R_cm: Bán kính đáy (60 cm -> 6 dm)

                # Random hóa thông số (đảm bảo đơn vị cm chia hết cho 10 để ra dm đẹp)
                a_cm = random.choice([30, 40, 50]) 
                b_cm = random.choice([20, 30])
                R_cm = random.choice([50, 60, 70])

                # Chuyển sang đơn vị dm để tính toán theo mẫu
                a = Rational(a_cm, 10)
                b = Rational(b_cm, 10)
                R = Rational(R_cm, 10)

                # Thiết lập phương trình elip (E): x^2/a^2 + y^2/b^2 = 1
                # Phương trình đường sinh sau khi tịnh tiến lên R đơn vị: y = R - (b/a)*sqrt(a^2 - x^2)
                expr = R - (b/a) * sqrt(a**2 - x**2)

                # Tính tích phân thể tích: V = pi * integral(y^2, -a, a)
                V_exact = pi * integrate(expr**2, (x, -a, a))
                V_float = float(V_exact.evalf())

                # Kết quả làm tròn đến hàng đơn vị
                kq_val = int(Decimal(V_float).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                kq = str(kq_val)

                # =====================================================
                # B4: Điều chỉnh phương án sai (không trùng đáp án đúng)
                # =====================================================
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo danh sách các phương án nhiễu xung quanh đáp án đúng
                s_vals = [kq_val + 10, kq_val - 10, kq_val + 25, kq_val - 25, kq_val + 50, kq_val - 50]
                s = []
                for v in s_vals:
                    if v != kq_val and v > 0:
                        s.append('$%s$' % v)

                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # =====================================================
                # B2: Viết lại nội dung câu hỏi và lời giải (sử dụng \text{d}x)
                # =====================================================

                noidungcauhoi = (r'''\immini{Cho chiếc trống như hình vẽ, có đường sinh là nửa elip được cắt bởi trục lớn với độ dài trục lớn bằng $%s$ cm, độ dài trục bé bằng $%s$ cm và đáy trống là hình tròn có bán kính bằng $%s$ cm. Tính thể tích $V$ của chiếc trống (đơn vị: dm$^3$, kết quả làm tròn đến hàng đơn vị).}
                                 {\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            			\draw   (66,44.33) .. controls (66,33.29) and (92.5,24.33) .. (125.2,24.33) .. controls (157.9,24.33) and (184.4,33.29) .. (184.4,44.33) .. controls (184.4,55.38) and (157.9,64.33) .. (125.2,64.33) .. controls (92.5,64.33) and (66,55.38) .. (66,44.33) -- cycle ;
            			\draw  [draw opacity=0] (186.77,163.11) .. controls (174.72,154.97) and (166,131.35) .. (166,103.47) .. controls (166,78.12) and (173.2,56.3) .. (183.56,46.42) -- (196,103.47) -- cycle ; \draw   (186.77,163.11) .. controls (174.72,154.97) and (166,131.35) .. (166,103.47) .. controls (166,78.12) and (173.2,56.3) .. (183.56,46.42) ;  
            			\draw  [draw opacity=0] (65.33,44.94) .. controls (77.53,52.91) and (86.24,76.84) .. (85.99,105.04) .. controls (85.76,132.39) and (77.17,155.57) .. (65.4,164.02) -- (56,104.78) -- cycle ; \draw   (65.33,44.94) .. controls (77.53,52.91) and (86.24,76.84) .. (85.99,105.04) .. controls (85.76,132.39) and (77.17,155.57) .. (65.4,164.02) ;  
            			\draw  [dash pattern={on 4.5pt off 4.5pt}]  (125.2,44.33) -- (126,164.33) ;
            			\draw    (126,44.33) -- (184.4,44.33) ;
            			\draw  [dash pattern={on 4.5pt off 4.5pt}]  (126,164.33) -- (186,164.33) ;
            			\draw  [draw opacity=0][dash pattern={on 4.5pt off 4.5pt}] (64.62,167.02) .. controls (69.55,152.81) and (95.42,141.72) .. (126.73,141.32) .. controls (157.79,140.93) and (183.76,151.2) .. (189.33,165.11) -- (127.11,171.32) -- cycle ; \draw  [dash pattern={on 4.5pt off 4.5pt}] (64.62,167.02) .. controls (69.55,152.81) and (95.42,141.72) .. (126.73,141.32) .. controls (157.79,140.93) and (183.76,151.2) .. (189.33,165.11) ;  
            			\draw  [draw opacity=0] (189.13,163.15) .. controls (188.92,179.5) and (160.91,192.49) .. (126.52,192.17) .. controls (93.85,191.87) and (67.16,179.67) .. (64.65,164.43) -- (126.79,162.53) -- cycle ; \draw   (189.13,163.15) .. controls (188.92,179.5) and (160.91,192.49) .. (126.52,192.17) .. controls (93.85,191.87) and (67.16,179.67) .. (64.65,164.43) ;  
            		\end{tikzpicture}}'''
                                 % (latex(2*a_cm), latex(2*b_cm), latex(R_cm)))

                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết theo tham số
                loigiai = (r'''\begin{center}
            				\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            					\draw   (56.48,172.96) .. controls (45.41,172.97) and (36.42,146.45) .. (36.4,113.73) .. controls (36.38,81.02) and (45.35,54.49) .. (56.42,54.49) .. controls (67.49,54.48) and (76.48,81) .. (76.5,113.71) .. controls (76.52,146.43) and (67.55,172.95) .. (56.48,172.96) -- cycle ;
            					\draw  [draw opacity=0] (175.47,52.07) .. controls (167.32,64.13) and (143.64,72.85) .. (115.71,72.87) .. controls (90.32,72.88) and (68.44,65.7) .. (58.53,55.34) -- (115.69,42.85) -- cycle ; \draw   (175.47,52.07) .. controls (167.32,64.13) and (143.64,72.85) .. (115.71,72.87) .. controls (90.32,72.88) and (68.44,65.7) .. (58.53,55.34) ;  
            					\draw  [draw opacity=0] (57.1,173.61) .. controls (65.1,161.41) and (89.07,152.69) .. (117.33,152.92) .. controls (144.73,153.15) and (167.96,161.72) .. (176.45,173.48) -- (117.08,182.94) -- cycle ; \draw   (57.1,173.61) .. controls (65.1,161.41) and (89.07,152.69) .. (117.33,152.92) .. controls (144.73,153.15) and (167.96,161.72) .. (176.45,173.48) ;  
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (56.45,113.72) -- (176.74,112.86) ;
            					\draw    (56.45,112.92) -- (56.42,54.49) ;
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (176.74,112.86) -- (176.71,52.82) ;
            					\draw  [draw opacity=0][dash pattern={on 4.5pt off 4.5pt}] (179.58,172.7) .. controls (165.27,168.04) and (154.07,142.79) .. (153.67,112.19) .. controls (153.28,81.83) and (163.64,56.46) .. (177.66,51.15) -- (183.75,111.8) -- cycle ; \draw  [dash pattern={on 4.5pt off 4.5pt}] (179.58,172.7) .. controls (165.27,168.04) and (154.07,142.79) .. (153.67,112.19) .. controls (153.28,81.83) and (163.64,56.46) .. (177.66,51.15) ;  
            					\draw  [draw opacity=0] (176.64,51.86) .. controls (193.66,52.06) and (207.22,79.17) .. (206.93,112.47) .. controls (206.65,144.21) and (193.89,170.12) .. (177.94,172.37) -- (176.07,112.2) -- cycle ; \draw   (176.64,51.86) .. controls (193.66,52.06) and (207.22,79.17) .. (206.93,112.47) .. controls (206.65,144.21) and (193.89,170.12) .. (177.94,172.37) ;  
            					\draw    (176.07,112.2) -- (248.4,112.78) ;
            					\draw [shift={(250.4,112.8)}, rotate = 180.47] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw  [dash pattern={on 4.5pt off 4.5pt}]  (120.4,114.13) -- (120.4,72.8) ;
            					\draw    (120.4,72.8) -- (119.76,28.13) ;
            					\draw [shift={(119.73,26.13)}, rotate = 89.18] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw (110.67,115) node [anchor=north west][inner sep=0.75pt]    {$O$};
            					\draw (228,115.33) node [anchor=north west][inner sep=0.75pt]    {$x$};
            					\draw (101.33,20.33) node [anchor=north west][inner sep=0.75pt]    {$y$};
            				\end{tikzpicture}
            			\end{center}
                        Đặt hệ trục tọa độ $Oxy$ (trục hoành là trục của chiếc trống, gốc tọa độ là trung điểm của đường cao chiếc trống, đơn vị: dm).\\
                             Gọi $(E)$ là elip có phương trình $\frac{x^2}{%s} + \frac{y^2}{%s} = 1$ thì ảnh của $(E)$ qua phép tịnh tiến theo vectơ $\vec{u}(0;%s)$ là elip $(E')$ có phương trình $\frac{x^2}{%s} + \frac{(y-%s)^2}{%s} = 1$.\\
                             Suy ra, phương trình của đường sinh là: $y = %s - \frac{%s}{%s}\sqrt{%s - x^2}$.\\
                             Do đó, thể tích của chiếc trống là: $V = \pi \int_{-%s}^{%s} \left( %s - \frac{%s}{%s}\sqrt{%s - x^2} \right)^2 \text{d}x \approx %s \text{ (dm}^3\text{)}$.'''
                           % (latex(a**2), latex(b**2), latex(R), latex(a**2), latex(R), latex(b**2),
                              latex(R), latex(b), latex(a), latex(a**2),
                              latex(a), latex(a), latex(R), latex(b), latex(a), latex(a**2), kq))

            # Xuất câu trắc nghiệm theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + 
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

