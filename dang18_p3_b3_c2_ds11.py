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


def bt_dang18_p3_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random các thông số của bài toán
                a_val = random.choice([4, 6, 8, 10, 12]) # Kích thước bức vách hình vuông (m)
                n_val = random.choice([4, 5, 6, 7])      # Số lượng mảng màu
                labor_val = random.choice([8, 10, 12, 15, 20]) # Tiền công thiết kế và thi công (triệu đồng)
                mat_rate_val = random.choice([200, 250, 300, 350, 400, 500]) # Chi phí vật tư keo epoxy (nghìn đồng/m2)

                # Chuỗi hiển thị đề bài
                labor_str = str(labor_val) + ".000.000"
                mat_rate_str = str(mat_rate_val) + ".000"

                # Tính toán
                # Công thức tổng diện tích: S = 2 * a^2 * (1 - pi/4) * (1 - (1/2)^n)
                q_ratio = 1 - (0.5)**n_val
                S_area = 2 * (a_val**2) * (1 - math.pi/4) * q_ratio

                mat_cost_m = float(mat_rate_val) / 1000 # Đổi đơn vị sang triệu đồng
                mat_cost_total = S_area * mat_cost_m    # Tổng chi phí vật liệu
                total_cost = labor_val + mat_cost_total # Tổng chi phí (Tiền công + Vật tư)

                # Làm tròn đến hàng phần mười
                kq_decimal = Decimal(float(total_cost)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq_decimal).replace('.', ',')
                kq_float = float(kq_decimal)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq)]
                da = random.choice(du)

                # Tạo các phương án sai lệch xung quanh đáp án đúng
                s = ['$%s$'%(str(Decimal(float(kq_float + 1.2)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq_float + 2.5)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq_float + 0.8)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq_float - 1.1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq_float - 2.3)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.',',')),
                     '$%s$'%(str(Decimal(float(kq_float - 0.7)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)).replace('.',','))]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 255; green, 0; blue, 29 }  ,fill opacity=1 ][line width=1]  (127.9,22) -- (327.5,22) -- (327.5,221.6) -- (127.9,221.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (128.21,22.3) .. controls (238.14,22.47) and (327.2,111.63) .. (327.2,221.6) -- (127.9,221.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=1 ][line width=1]  (128.21,81.6) -- (268.51,81.6) -- (268.51,221.9) -- (128.21,221.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (128.43,81.6) .. controls (205.82,81.72) and (268.51,144.49) .. (268.51,221.9) -- (128.21,221.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ][line width=1]  (128.21,123.4) -- (226.71,123.4) -- (226.71,221.9) -- (128.21,221.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (128.06,122.79) .. controls (182.56,122.87) and (226.71,167.08) .. (226.71,221.6) .. controls (226.71,221.6) and (226.71,221.6) .. (226.71,221.6) -- (127.9,221.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ][line width=1]  (128.21,152.4) -- (197.71,152.4) -- (197.71,221.9) -- (128.21,221.9) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (128.01,151.79) .. controls (166.52,151.85) and (197.71,183.08) .. (197.71,221.6) .. controls (197.71,221.6) and (197.71,221.6) .. (197.71,221.6) -- (127.9,221.6) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ][line width=1]  (128.01,172.4) -- (176.9,172.4) -- (176.9,221.29) -- (128.01,221.29) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (128.09,171.83) .. controls (155.36,171.88) and (177.46,194) .. (177.46,221.29) -- (128.01,221.29) -- cycle ;
            	\draw [line width=1]    (128.01,221.29) -- (327.5,22) ;
            	\draw (106.5,10) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (109,214.5) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (328.5,213.5) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (328.5,9) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\draw (105,68.5) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\draw (258,53) node [anchor=north west][inner sep=0.75pt]    {$N$};
            	\draw (261,225) node [anchor=north west][inner sep=0.75pt]    {$E$};
            \end{tikzpicture}'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Thư viện trường học muốn thuê bác Bình thiết kế một bức vách gỗ trang trí hình vuông kích thước $%s$ m theo phong cách hình học. Bác Bình đề xuất ý tưởng: coi bức vách ban đầu là hình vuông $ABCD$, vẽ $\frac{1}{4}$ đường tròn tâm $B$, bán kính $AB$ và phủ lớp keo epoxy màu cho phần giữa cung tròn với hình vuông $ABCD$. Từ giao điểm $N$ của đường chéo $BD$ và cung tròn, dựng hình vuông $BMNE$ và tiếp tục vẽ $\frac{1}{4}$ đường tròn tâm $B$, bán kính $BM$ rồi phủ keo cho phần giữa cung tròn mới và hình vuông $BMNE$ (hình vẽ). Quá trình này lặp lại cho đến khi phủ keo được $%s$ mảng màu.
            Ngoài tiền công thiết kế và thi công là $%s$ đồng, thư viện phải trả chi phí vật tư keo epoxy là $%s$ đồng/$1\text{m}^2$. Tổng số tiền thư viện phải trả cho bác Bình (gồm tiền công và vật tư) theo đơn vị triệu đồng bằng bao nhiêu? (làm tròn kết quả đến hàng phần mười).}{%s}'''
                                 %(latex(a_val), latex(n_val), labor_str, mat_rate_str, hinhve))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Xử lý chuỗi tính toán phân số cho lời giải
                tu_so = 2**n_val - 1
                mau_so = 2**(n_val - 1)
                frac_val = Rational(a_val**2 * tu_so, mau_so)
                if frac_val.q == 1:
                    S_exact_str_simp = f"{frac_val.p} \\left(1 - \\frac{{\\pi}}{{4}}\\right)"
                else:
                    S_exact_str_simp = f"\\frac{{{frac_val.p}}}{{{frac_val.q}}} \\left(1 - \\frac{{\\pi}}{{4}}\\right)"

                mat_cost_m_str = str(mat_cost_m).replace('.', ',')
                mat_cost_total_str = str(Decimal(float(mat_cost_total)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).replace('.', ',').rstrip('0').rstrip(',')
                total_cost_str = str(Decimal(float(total_cost)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)).replace('.', ',').rstrip('0').rstrip(',')
                if total_cost_str == "": total_cost_str = "0"

                # Nội dung lời giải
                loigiai=('''Diện tích mảng màu thứ nhất là $S_1 = S_{ABCD} - S_{\\text{quạt}} = %s^2 - \\frac{1}{4}\\pi \\cdot %s^2 = %s \\left(1 - \\frac{\\pi}{4}\\right) \\text{ (m}^2\\text{)}$.\\\\
            Đường chéo của hình vuông thứ nhất là $BD = %s\\sqrt{2}$. Vì $N$ nằm trên cung tròn tâm $B$ bán kính $AB$ nên $BN = AB = %s$.\\\\
            Hình vuông thứ hai $BMNE$ có đường chéo $BN = %s$, do đó cạnh của nó là $BM = \\frac{BN}{\\sqrt{2}} = \\frac{%s}{\\sqrt{2}}$.\\\\
            Diện tích mảng màu thứ hai là $S_2 = \\left(\\frac{%s}{\\sqrt{2}}\\right)^2 \\left(1 - \\frac{\\pi}{4}\\right) = \\frac{1}{2} \\cdot %s \\left(1 - \\frac{\\pi}{4}\\right) = \\frac{1}{2}S_1$.\\\\
            Tương tự, diện tích các mảng màu tiếp theo lập thành một cấp số nhân có số hạng đầu $S_1 = %s \\left(1 - \\frac{\\pi}{4}\\right)$ và công bội $q = \\frac{1}{2}$.\\\\
            Tổng diện tích của $%s$ mảng màu là:\\\\
            $S = S_1 \\cdot \\frac{1 - q^{%s}}{1 - q} = %s \\left(1 - \\frac{\\pi}{4}\\right) \\cdot \\frac{1 - \\left(\\frac{1}{2}\\right)^{%s}}{1 - \\frac{1}{2}} = %s$ (m$^2$).\\\\
            Tiền vật tư keo epoxy là: $%s \\cdot %s \\approx %s$ (triệu đồng).\\\\
            Tổng số tiền thư viện phải trả là: $%s + %s = %s$ (triệu đồng) $\\approx %s$ (triệu đồng).'''
                         %( latex(a_val), latex(a_val), latex(a_val**2),
                            latex(a_val), latex(a_val),
                            latex(a_val), latex(a_val),
                            latex(a_val), latex(a_val**2),
                            latex(a_val**2),
                            latex(n_val),
                            latex(n_val), latex(a_val**2), latex(n_val), S_exact_str_simp,
                            mat_cost_m_str, S_exact_str_simp, mat_cost_total_str,
                            latex(labor_val), mat_cost_total_str, total_cost_str, kq
                          ))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')   
            return content 

