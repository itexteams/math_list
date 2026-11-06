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


def bt_dang46_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random các giá trị: Bán kính R, Chiều cao h, Khoảng cách d (đảm bảo d < R)
                R = random.randint(4, 10)
                h = random.randint(5, 12)
                d = random.randint(2, R - 1)

                # Tính toán kết quả chính xác bằng công thức nguyên hàm của thể tích
                term1 = (R**3) * math.acos(d / R)
                term2 = 2 * R * d * math.sqrt(R**2 - d**2)
                term3 = (d**3) * math.log((R + math.sqrt(R**2 - d**2)) / d)
                V_exact = (h / (3 * R)) * (term1 - term2 + term3)
                while V_exact>99.9:
                    R = random.randint(4, 10)
                    h = random.randint(5, 12)
                    d = random.randint(2, R - 1)

                    # Tính toán kết quả chính xác bằng công thức nguyên hàm của thể tích
                    term1 = (R**3) * math.acos(d / R)
                    term2 = 2 * R * d * math.sqrt(R**2 - d**2)
                    term3 = (d**3) * math.log((R + math.sqrt(R**2 - d**2)) / d)
                    V_exact = (h / (3 * R)) * (term1 - term2 + term3)        

                # Làm tròn kết quả cuối cùng đến hàng phần chục
                kq_dec = Decimal(float(V_exact)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',')
                kq_float = float(kq_dec)

                # Kết quả xấp xỉ 3 chữ số thập phân để hiển thị trong lời giải tích phân
                V_approx_str = "{:.3f}".format(V_exact).replace('.', ',')

                # Khởi tạo các đáp án nhiễu (sai), đảm bảo không trùng nhau
                sai1 = round(kq_float + random.choice([1.2, 2.4, 3.1, 0.8]), 1)
                sai2 = round(kq_float - random.choice([1.1, 2.3, 3.5, 0.9]), 1)
                sai3 = round(kq_float + random.choice([-0.5, 0.5, -1.5, 1.5]), 1)

                while sai3 == sai1 or sai3 == sai2 or sai3 == kq_float or sai3 <= 0:
                    sai3 = round(kq_float + random.uniform(-4, 4), 1)

                # Các đáp án trắc nghiệm
                da = '$%s$' % kq_str
                s = [
                    '$%s$' % str(Decimal(float(sai1)).quantize(Decimal('0.1'))).replace('.', ','),
                    '$%s$' % str(Decimal(float(sai2)).quantize(Decimal('0.1'))).replace('.', ','),
                    '$%s$' % str(Decimal(float(sai3)).quantize(Decimal('0.1'))).replace('.', ','),
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                hinhve=r'''\begin{center} \scalebox{0.8}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (342.55,99.16) .. controls (347.03,68.76) and (365.23,46) .. (387,46) .. controls (401.25,46) and (413.96,55.74) .. (422.31,70.99) -- cycle ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][line width=1]  (272.5,77.4) -- (422.31,70.99) -- (342.55,99.16) -- (242.5,86.4) -- (242.5,86.4) -- cycle ;
            	\draw [line width=1]    (123.6,118.9) -- (376.7,180.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (123.6,118.9) -- (386.1,114.45) ;
            	\draw [line width=1]    (422.31,70.99) -- (342.55,99.16) ;
            	\draw [line width=1]    (242.5,86.4) -- (342.55,99.16) ;
            	\draw  [draw opacity=0][fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (378.2,46.9) -- (386.1,71.4) -- (266.53,79.47) -- cycle ;
            	\draw [line width=1]    (375.2,47.9) -- (123.6,118.9) ;
            	\draw  [line width=1]  (340.6,114.45) .. controls (340.6,76.92) and (360.97,46.5) .. (386.1,46.5) .. controls (411.23,46.5) and (431.6,76.92) .. (431.6,114.45) .. controls (431.6,151.98) and (411.23,182.4) .. (386.1,182.4) .. controls (360.97,182.4) and (340.6,151.98) .. (340.6,114.45) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (276.15,77.2) -- (418.65,71.2) ;
            	\draw [line width=1]    (386.1,46.5) -- (386.1,182.4) ;
            	\draw (106.67,111) node [anchor=north west][inner sep=0.75pt]    {$S$};
            	\draw (378.67,30) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (386.67,103.67) node [anchor=north west][inner sep=0.75pt]    {$O$};
            \end{tikzpicture} }\end{center}'''
                # Câu hỏi
                noidungcauhoi = (r'''Cho hình nón có bán kính đáy $OA=%s$ cm và chiều cao $SO=%s$ cm. Cắt hình nón đã cho bởi một mặt phẳng song song với trục $SO$ và cách trục $SO$ một khoảng bằng $%s$ cm ta được hai phần. %s Thể tích phần không chứa đỉnh $S$ bằng bao nhiêu cm$^3$?
            (làm tròn kết quả đến hàng phần chục).''' 
                                 % (R, h, d, hinhve))

                # Các đáp án và xáo trộn
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Cấu hình các biến cho lời giải
                x_min_val = sp.Rational(d * h, R)
                r_coef = sp.Rational(R, h)

                # Nội dung lời giải bám sát ảnh chụp
                loigiai = ('''Đặt trục $SO$ làm trục $Ox$, đỉnh $S$ tại gốc, tâm đáy $O$ tại $x=%s$.\\\\
            Bán kính đáy là $%s$, nên ở vị trí cách đỉnh một đoạn $x$, bán kính tiết diện tròn là \\\\
            $r\\left(x\\right) = \\frac{%s}{%s}x = %s x$.\\\\
            Mặt phẳng cắt song song với trục $SO$ và cách trục $SO$ một khoảng $d=%s$ cm.\\\\
            Phần \\textbf{không chứa đỉnh} $S$ là phần "mảnh" gần mặt bên hình nón.\\\\
            Thiết diện thu được là một hình viên phân. Diện tích thiết diện $S\\left(x\\right)$ bằng diện tích hình quạt trừ đi diện tích tam giác:\\\\
            - Cung tròn bị cắt căng một góc ở tâm $2\\alpha$ với $\\cos\\alpha = \\frac{d}{r} = \\frac{%s}{r}$.\\\\ Diện tích hình quạt là $S_{\\text{quạt}} = \\frac{1}{2}r^2\\left(2\\alpha\\right) = r^2\\arccos\\left(\\frac{%s}{r}\\right)$.\\\\
            - Tam giác tạo bởi hai bán kính và dây cung có chiều cao $d=%s$ và độ dài đáy $2\\sqrt{r^2 - d^2} = 2\\sqrt{r^2 - %s^2}$. Diện tích tam giác là $S_{\\text{tam giác}} = \\frac{1}{2} \\cdot %s \\cdot 2\\sqrt{r^2 - %s^2} = %s\\sqrt{r^2 - %s^2}$.\\\\
            - Suy ra diện tích viên phân: $S\\left(x\\right) = S_{\\text{quạt}} - S_{\\text{tam giác}} = r^2 \\arccos\\left(\\frac{%s}{r}\\right) - %s\\sqrt{r^2 - %s^2}$.\\\\
            Tính theo phương pháp tích phân, thể tích phần này là \\\\
            $V = \\int_{%s}^{%s} S\\left(x\\right) \\, dx = \\int_{%s}^{%s} \\left[ r^2 \\arccos\\left(\\frac{%s}{r}\\right) - %s\\sqrt{r^2 - %s^2} \\right] \\, dx \\approx %s$.\\\\
            Làm tròn đến hàng phần chục ta được thể tích cần tìm là $%s$ cm$^3$''' % (
                    h, 
                    R, 
                    R, h, latex(r_coef), 
                    d,
                    d, d,
                    d, d, d, d, d, d,
                    d, d, d,
                    latex(x_min_val), h, latex(x_min_val), h, d, d, d, 
                    V_approx_str,
                    kq_str
                ))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq_str))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

