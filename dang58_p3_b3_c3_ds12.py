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


def bt_dang58_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # Các hàm phụ trợ để xử lý định dạng LaTeX chuẩn chỉ
            def fmt(expr):
                # Định dạng biểu thức sympy sang latex và thay thế () thành \left( \right)
                return str(latex(expr)).replace('(', '\\left(').replace(')', '\\right)')

            def fmt_sq(expr):
                # Bọc thêm ngoặc cho các phân số nếu cần bình phương
                s = fmt(expr)
                if '\\frac' in s:
                    return f"\\left({s}\\right)"
                return s

            def format_pi(val):
                # Xử lý đẹp các hệ số đi với pi
                if val == 0:
                    return "0"
                if val == 1:
                    return "\\pi"
                if val == -1:
                    return "-\\pi"
                if isinstance(val, Rational):
                    if val.q == 1:
                        return f"{val.p}\\pi"
                    else:
                        if val.p == 1:
                            return f"\\frac{{\\pi}}{{{val.q}}}"
                        elif val.p == -1:
                            return f"-\\frac{{\\pi}}{{{val.q}}}"
                        else:
                            sign = "-" if val.p < 0 else ""
                            return f"{sign}\\frac{{{abs(val.p)}\\pi}}{{{val.q}}}"
                else:
                    return f"{val}\\pi"

            # ----------------- TẠO DỮ LIỆU NGẪU NHIÊN -----------------
            # Giữ AM = BE = h (để bài toán cân xứng giống mẫu gốc)
            h = random.choice([1, 2])
            d = h
            L = 2 * h + random.choice([1, 2, 3]) # Chiều dài AB luôn thỏa mãn để hình vẽ hợp lý
            C_val = random.choice([100, 120, 150, 180, 200]) # Chi phí (nghìn đồng)

            # ----------------- TÍNH TOÁN -----------------
            # Tọa độ các điểm chính: A(0; 0), B(L; 0), M(0; h), E(L-d; 0)
            x_I = Rational(L - d, 2)
            R_sq = x_I**2 + h**2
            R = sqrt(R_sq)

            x_N = L - d
            y_N = h

            # Đạo hàm của f(x) tại x_N
            f_prime_N = Rational(-(x_N - x_I), h)

            # Phương trình Parabol g(x): g'(x_N) = -a*d  => f'(x_N) = -a*d => a = -f_prime_N / d
            a_val = -f_prime_N / d
            g_expr = a_val * (x - x_N) * (x - L) + h
            g_expr_exp = expand(g_expr)

            # Tích phân thể tích V1
            f_sq_expr = R_sq - (x - x_I)**2
            V1_pi = integrate(f_sq_expr, (x, 0, x_N))

            # Tích phân thể tích V2
            V2_pi = integrate(g_expr**2, (x, x_N, L))

            # Tổng thể tích và chi phí
            V_pi = V1_pi + V2_pi
            cost_exact = float(V_pi * math.pi) * C_val
            cost = math.floor(cost_exact + 0.5) # Làm tròn số chuẩn xác
            while cost>9999:
                h = random.choice([1, 2])
                d = h
                L = 2 * h + random.choice([1, 2, 3]) # Chiều dài AB luôn thỏa mãn để hình vẽ hợp lý
                C_val = random.choice([100, 120, 150, 180, 200]) # Chi phí (nghìn đồng)

                # ----------------- TÍNH TOÁN -----------------
                # Tọa độ các điểm chính: A(0; 0), B(L; 0), M(0; h), E(L-d; 0)
                x_I = Rational(L - d, 2)
                R_sq = x_I**2 + h**2
                R = sqrt(R_sq)

                x_N = L - d
                y_N = h

                # Đạo hàm của f(x) tại x_N
                f_prime_N = Rational(-(x_N - x_I), h)

                # Phương trình Parabol g(x): g'(x_N) = -a*d  => f'(x_N) = -a*d => a = -f_prime_N / d
                a_val = -f_prime_N / d
                g_expr = a_val * (x - x_N) * (x - L) + h
                g_expr_exp = expand(g_expr)

                # Tích phân thể tích V1
                f_sq_expr = R_sq - (x - x_I)**2
                V1_pi = integrate(f_sq_expr, (x, 0, x_N))

                # Tích phân thể tích V2
                V2_pi = integrate(g_expr**2, (x, x_N, L))

                # Tổng thể tích và chi phí
                V_pi = V1_pi + V2_pi
                cost_exact = float(V_pi * math.pi) * C_val
                cost = math.floor(cost_exact + 0.5) # Làm tròn số chuẩn xác

            # ----------------- XỬ LÝ ĐÁP ÁN -----------------
            # Các đáp án trắc nghiệm
            da_str = str(cost).replace('.', ',')
            du = [f'${da_str}$']
            da = random.choice(du)

            offsets = [random.randint(1, 9), random.randint(10, 50), random.randint(51, 100),
                       -random.randint(1, 9), -random.randint(10, 50), -random.randint(51, 100)]
            random.shuffle(offsets)

            s = [
                f'${str(cost + offsets[0]).replace(".", ",")}$',
                f'${str(cost + offsets[1]).replace(".", ",")}$',
                f'${str(cost + offsets[2]).replace(".", ",")}$',
                f'${str(cost + offsets[3]).replace(".", ",")}$',
            ]

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            # ----------------- NỘI DUNG CÂU HỎI -----------------
            hinhve=r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw  [draw opacity=0][fill={rgb, 255:red, 219; green, 229; blue, 240 }  ,fill opacity=1 ][line width=1]  (273.2,112.2) .. controls (276,107) and (307.2,72.6) .. (271.33,36.67) .. controls (295.2,36.6) and (289.6,36.6) .. (305.98,36.67) .. controls (306.4,82.6) and (305.6,151) .. (305.98,201.87) .. controls (292,201.4) and (292.77,200.95) .. (272.08,201.8) .. controls (222.88,177.4) and (236,149.4) .. (273.2,112.2) -- cycle ;
            		\draw  [line width=1]  (201.2,36.67) -- (305.98,36.67) -- (305.98,201.87) -- (201.2,201.87) -- cycle ;
            		\draw [line width=1]    (271.33,36.67) .. controls (290.33,53.86) and (297.87,87.8) .. (268.57,116.95) .. controls (239.28,146.09) and (220.75,177.8) .. (272.08,201.8) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (271.33,36.67) -- (272.08,201.8) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (305.68,113.8) -- (271.28,113.8) ;
            		\draw  [color={rgb, 255:red, 86; green, 111; blue, 127 }  ,draw opacity=1 ][fill={rgb, 255:red, 73; green, 125; blue, 159 }  ,fill opacity=1 ] (432.4,203.2) .. controls (432.4,198.51) and (449.3,194.7) .. (470.15,194.7) .. controls (491,194.7) and (507.9,198.51) .. (507.9,203.2) .. controls (507.9,207.89) and (491,211.7) .. (470.15,211.7) .. controls (449.3,211.7) and (432.4,207.89) .. (432.4,203.2) -- cycle ;
            		\draw  [color={rgb, 255:red, 86; green, 111; blue, 127 }  ,draw opacity=1 ][fill={rgb, 255:red, 73; green, 125; blue, 159 }  ,fill opacity=1 ] (437.68,203.2) .. controls (437.68,200.66) and (452.37,198.6) .. (470.48,198.6) .. controls (488.59,198.6) and (503.28,200.66) .. (503.28,203.2) .. controls (503.28,205.74) and (488.59,207.8) .. (470.48,207.8) .. controls (452.37,207.8) and (437.68,205.74) .. (437.68,203.2) -- cycle ;
            		\draw  [color={rgb, 255:red, 88; green, 115; blue, 132 }  ,draw opacity=1 ][fill={rgb, 255:red, 124; green, 153; blue, 172 }  ,fill opacity=0.3 ] (434,38) .. controls (432.3,29.2) and (509.04,30.68) .. (503.3,38.2) .. controls (493.07,48.43) and (475.3,81.2) .. (505.3,114.7) .. controls (528.3,136.7) and (555.8,175.7) .. (506.8,200.7) .. controls (491.04,209.08) and (456.64,210.28) .. (431.3,202.2) .. controls (377.44,173.88) and (415.04,133.48) .. (433.2,114.27) .. controls (452.3,92.2) and (459.66,67.68) .. (434,38) -- cycle ;
            		\draw  [color={rgb, 255:red, 88; green, 115; blue, 132 }  ,draw opacity=1 ] (434,38) .. controls (434,34.64) and (449.51,31.92) .. (468.65,31.92) .. controls (487.79,31.92) and (503.3,34.64) .. (503.3,38) .. controls (503.3,41.36) and (487.79,44.08) .. (468.65,44.08) .. controls (449.51,44.08) and (434,41.36) .. (434,38) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.45 ] (440.24,38.28) .. controls (438.54,29.48) and (501.98,30.76) .. (496.24,38.28) .. controls (486.01,48.51) and (471.44,81.18) .. (501.44,114.68) .. controls (524.44,136.68) and (555.8,175.7) .. (506.8,200.7) .. controls (491.04,209.08) and (456.64,210.28) .. (431.3,202.2) .. controls (377.44,173.88) and (419.28,135.09) .. (437.44,115.88) .. controls (456.54,93.81) and (465.9,67.96) .. (440.24,38.28) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.25 ] (469.4,89.87) .. controls (483.07,138.87) and (517.44,141.88) .. (509.44,177.88) .. controls (495.44,206.68) and (453.44,211.52) .. (433.44,181.52) .. controls (428.73,133.53) and (457.4,139.53) .. (469.4,89.87) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 79; green, 113; blue, 152 }  ,fill opacity=0.54 ] (436.44,41.08) .. controls (455.64,54.28) and (465.64,93.48) .. (431.24,118.28) .. controls (453.24,97.48) and (461.24,65.08) .. (436.44,41.08) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 79; green, 113; blue, 152 }  ,fill opacity=0.45 ] (499.29,42.14) .. controls (483.42,55.74) and (475.97,95.14) .. (505.62,119.2) .. controls (486.53,98.87) and (478.97,66.65) .. (499.29,42.14) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 79; green, 113; blue, 152 }  ,fill opacity=1 ] (460.64,205.88) .. controls (444.99,210.76) and (406.24,196.68) .. (404.24,167.48) .. controls (409.13,190.49) and (433.84,207.08) .. (460.64,205.88) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 79; green, 113; blue, 152 }  ,fill opacity=1 ] (532.08,160.99) .. controls (538.24,180.28) and (509.44,211.31) .. (480.68,205.88) .. controls (504.19,206.95) and (536.64,183.48) .. (532.08,160.99) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 79; green, 113; blue, 152 }  ,fill opacity=1 ] (502.24,199.88) .. controls (492.64,210.68) and (444.64,210.28) .. (429.44,197.88) .. controls (452.24,207.88) and (477.84,205.48) .. (502.24,199.88) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.29 ] (445.44,38.68) .. controls (441.21,36.2) and (447.65,36.46) .. (454.99,34.49) .. controls (469.44,78.28) and (466.24,107.48) .. (450.24,124.28) .. controls (411.44,167.08) and (447.04,191.88) .. (449.04,193.88) .. controls (444.38,195.52) and (443.84,195.08) .. (439.44,198.28) .. controls (422.99,197.35) and (391.44,160.28) .. (443.84,117.08) .. controls (447.04,112.68) and (473.44,88.28) .. (445.44,38.68) -- cycle ;
            		\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.29 ] (494.19,39.08) .. controls (498.68,36.6) and (491.84,36.86) .. (484.04,34.89) .. controls (468.69,78.68) and (472.09,107.88) .. (489.09,124.68) .. controls (530.31,167.48) and (492.49,192.28) .. (490.36,194.28) .. controls (495.31,195.92) and (495.89,195.48) .. (500.56,198.68) .. controls (518.04,197.75) and (551.56,160.68) .. (495.89,117.48) .. controls (492.49,113.08) and (464.44,88.68) .. (494.19,39.08) -- cycle ;
            		\draw [color={rgb, 255:red, 84; green, 112; blue, 146 }  ,draw opacity=1 ]   (434,38) .. controls (443.04,44.28) and (484.64,49.48) .. (503.3,38.2) ;
            		\draw [color={rgb, 255:red, 84; green, 112; blue, 146 }  ,draw opacity=1 ]   (434,38) .. controls (437.84,45.88) and (491.04,51.08) .. (503.3,38.2) ;
            		\draw [color={rgb, 255:red, 84; green, 112; blue, 146 }  ,draw opacity=0.34 ]   (423.04,128.68) .. controls (411.04,140.28) and (399.84,161.08) .. (407.7,181) ;
            		\draw [color={rgb, 255:red, 84; green, 112; blue, 146 }  ,draw opacity=0.25 ]   (530.8,175.6) .. controls (539.04,157.08) and (519.44,128.28) .. (507.84,119.48) ;
            		\draw [color={rgb, 255:red, 84; green, 112; blue, 146 }  ,draw opacity=0.33 ]   (445.73,35.87) .. controls (456.73,33.53) and (477.04,31.48) .. (499.44,37.48) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.66 ]   (429.67,201) .. controls (438.71,207.28) and (488.14,211.98) .. (506.8,200.7) ;
            		\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=0.42 ]   (439.4,201.2) .. controls (443.4,197.87) and (483.4,193.87) .. (500.73,200.87) ;
            		\draw (308.88,101.07) node [anchor=north west][inner sep=0.75pt]    {$E$};
            		\draw (260.88,19) node [anchor=north west][inner sep=0.75pt]    {$P$};
            		\draw (250.21,99) node [anchor=north west][inner sep=0.75pt]    {$N$};
            		\draw (259.55,205) node [anchor=north west][inner sep=0.75pt]    {$M$};
            		\draw (181.55,199.73) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (185,19) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (306.88,19) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (305.98,201.87) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\end{tikzpicture}
            \end{center}'''
            noidungcauhoi = (
                'Một người thợ gốm sứ muốn thiết kế một cái bình hoa bằng cách quay hình $\\left(H\\right)$ (phần tô màu trong hình vẽ) quanh trục $AB$. '
                'Hình phẳng $\\left(H\\right)$ nằm trong hình chữ nhật $ABCD$, giới hạn bởi các đoạn thẳng $AM, BP$ ($M, P$ là hai điểm lần lượt thuộc các cạnh $AD, BC, MP // CD$), '
                "cung tròn $MN$ (có tâm là trung điểm của đoạn thẳng $AE$) và cung parabol $NP$. Biết $AB = %s$ dm, $AM = BE = %s$ dm. Tiếp tuyến của cung tròn và cung parabol tại điểm $N$ là trùng nhau."
                r'''%s'''
                'Biết chi phí trung bình để sản xuất là $%s.000$ đồng trên mỗi $\\text{dm}^3$. Hỏi chi phí sản xuất một chiếc bình hoa là bao nhiêu nghìn đồng? (làm tròn đến hàng đơn vị).' 
                % (L, h,hinhve, C_val)
            )

            # ----------------- TRỘN ĐÁP ÁN -----------------
            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2) 
            da_s3 = str(das3) 

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # ----------------- CHUẨN BỊ CHUỖI LỜI GIẢI -----------------
            x_I_str = fmt(x_I)
            R_sq_str = fmt(R_sq)
            R_str = fmt(R)
            f_prime_N_str = fmt(f_prime_N)
            a_val_str = fmt(a_val)
            g_expr_str = fmt(g_expr_exp)
            g_prime_str = f"-{d}a" if d != 1 else "-a"

            loigiai = (
                '- Chọn hệ tọa độ sao cho $A \\equiv O\\left(0 ; 0\\right)$, tia $AB$ là trục $Ox$, tia $AD$ là trục $Oy$. \\\\ '
                'Khi đó $A\\left(0 ; 0\\right), B\\left(%s ; 0\\right), M\\left(0 ; %s\\right), E\\left(%s ; 0\\right)$. \\\\ '
                'Tâm $I$ của cung tròn là trung điểm của $AE \\Rightarrow I\\left(%s ; 0\\right)$. \\\\ '
                'Bán kính $R = IM = \\sqrt{x_I^2 + y_M^2} = \\sqrt{%s^2 + %s^2} = %s$. \\\\ '
                '- Phương trình đường tròn $\\left(C\\right)$ tâm $I\\left(%s ; 0\\right)$ bán kính $R = %s$ là $\\left(x - %s\\right)^2 + y^2 = %s \\Rightarrow y^2 = %s - \\left(x - %s\\right)^2$. \\\\ '
                'Gọi $y = f\\left(x\\right)$ là hàm số của cung tròn $MN$, khi đó: \\\\ '
                '$f^2\\left(x\\right) = %s - \\left(x - %s\\right)^2 \\Rightarrow f\\left(x\\right) = \\sqrt{%s - \\left(x - %s\\right)^2}$. \\\\ '
                'Thể tích khi quay hình phẳng giới hạn bởi $y = f\\left(x\\right), y=0, x=0, x=%s$ bằng: \\\\ '
                '$V_1 = \\pi \\int_{0}^{%s} f^2\\left(x\\right) dx = \\pi \\int_{0}^{%s} \\left( %s - \\left(x - %s\\right)^2 \\right) dx = %s \\text{ (dm}^3\\text{)}$. \\\\ '
                '- Gọi $y = g\\left(x\\right)$ là hàm số cung parabol đi qua $N\\left(%s ; %s\\right)$ và $P\\left(%s ; %s\\right)$. \\\\ '
                'Khi đó ta có: $g\\left(x\\right) - %s = a\\left(x - %s\\right)\\left(x - %s\\right)$ hay $g\\left(x\\right) = a\\left(x - %s\\right)\\left(x - %s\\right) + %s$. \\\\ '
                'Tiếp tuyến của cung tròn và cung parabol tại điểm $N\\left(%s ; %s\\right)$ là trùng nhau nên \\\\ '
                '$f\'\\left(%s\\right) = g\'\\left(%s\\right) \\Leftrightarrow %s = %s \\Leftrightarrow a = %s$. \\\\ '
                'Do đó, $g\\left(x\\right) = %s$. \\\\ '
                'Thể tích khi quay hình phẳng giới hạn bởi $y = g\\left(x\\right), y=0, x=%s, x=%s$ bằng: \\\\ '
                '$V_2 = \\pi \\int_{%s}^{%s} g^2\\left(x\\right) dx = \\pi \\int_{%s}^{%s} \\left( %s \\right)^2 dx = %s \\text{ (dm}^3\\text{)}$. \\\\ '
                'Thể tích của bình hoa đó bằng: \\\\ '
                '$V = V_1 + V_2 = %s + %s = %s \\text{ (dm}^3\\text{)}$. \\\\ '
                '- Chi phí sản xuất một chiếc bình hoa là $ %s \\cdot %s \\approx %s$ nghìn đồng.'
            ) % (
                L, h, x_N,
                x_I_str,
                fmt_sq(x_I), fmt_sq(h), R_str,
                x_I_str, R_str, x_I_str, R_sq_str, R_sq_str, x_I_str,
                R_sq_str, x_I_str, R_sq_str, x_I_str,
                x_N,
                x_N, x_N, R_sq_str, x_I_str, format_pi(V1_pi),
                x_N, h, L, h,
                h, x_N, L, x_N, L, h,
                x_N, h,
                x_N, x_N, f_prime_N_str, g_prime_str, a_val_str,
                g_expr_str,
                x_N, L,
                x_N, L, x_N, L, g_expr_str, format_pi(V2_pi),
                format_pi(V1_pi), format_pi(V2_pi), format_pi(V_pi),
                format_pi(V_pi), C_val, str(cost).replace('.', ',')
            )
            dapan='\\shortans[0]{$%s$}\n'%(str(cost).replace('.', ','))

            # ----------------- XUẤT CÂU TRẮC NGHIỆM -----------------
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{\n' + str(loigiai) + '\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

