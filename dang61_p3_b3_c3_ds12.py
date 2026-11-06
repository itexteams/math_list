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


def bt_dang61_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tọa độ A(-a, -b) và B(a, -b). 
                # b phải đủ lớn so với a để đỉnh O luôn nằm trên tâm I
                a = randint(2, 4)
                # Tăng giới hạn trên lên 10 để đảm bảo (a * 2) luôn <= 10
                b = randint(a * 2, 10) 

                # Tính các thông số hình học và hệ số parabol
                # Phương trình (P1) ban đầu: y = k*x^2
                k_sym = Rational(-b, a**2)
                p_sym = Rational(b, a**2) # Lấy trị tuyệt đối để dùng cho hệ trục mới

                t36 = math.tan(math.radians(36))
                t54 = math.tan(math.radians(54))
                t18 = math.tan(math.radians(18))

                p = b / (a**2)
                d = b - a / t36

                # Hoành độ giao điểm
                xm = (-t54 + math.sqrt(t54**2 + 4 * p * d)) / (2 * p)
                xn = (-t18 + math.sqrt(t18**2 + 4 * p * d)) / (2 * p)

                # Tính tích phân
                int1 = 0.5 * (t54 - t18) * (xm**2)
                def F(X):
                    return d * X - (p / 3) * X**3 - (t18 / 2) * X**2
                int2 = F(xn) - F(xm)

                S_gach = int1 + int2
                S_total = 10 * S_gach

                # Xử lý làm tròn số đến 2 chữ số thập phân cho đáp án cuối cùng
                kq_dec = Decimal(S_total).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_dec).replace('.', ',')

                # Chuỗi hiển thị các số trung gian
                d_str = str(round(d, 4)).replace('.', ',')
                xm_str = str(round(xm, 4)).replace('.', ',')
                xn_str = str(round(xn, 4)).replace('.', ',')
                S_gach_str = str(round(S_gach, 4)).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq_str)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên quanh giá trị đúng
                wrong_offsets = [0.11, -0.12, 0.25, -0.21, 0.45, -0.32, 1.1, -1.5]
                random.shuffle(wrong_offsets)
                s = []
                for offset in wrong_offsets[:5]:
                    val = Decimal(S_total + offset).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    s.append('$%s$' % (str(val).replace('.', ',')))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\scalebox{0.6}{  \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                                \draw  [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  (331.06,106.47) -- (290.9,231.1) -- (159.96,231.42) -- (119.19,106.98) -- (224.94,29.76) -- cycle ;
                                \draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1]    (224.94,29.76) .. controls (167.6,189.4) and (185.1,226.4) .. (331.06,106.47) ;
                                \draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1]    (331.06,106.47) .. controls (224.6,102.4) and (90.1,98.9) .. (290.9,231.1) ;
                                \draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1]    (159.96,231.42) .. controls (196.6,84.4) and (243.6,30.4) .. (290.9,231.1) ;
                                \draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1]    (119.19,106.98) .. controls (272.1,92.4) and (335.1,120.4) .. (159.96,231.42) ;
                                \draw [color={rgb, 255:red, 65; green, 117; blue, 5 }  ,draw opacity=1 ][line width=1]    (119.19,106.98) .. controls (190.1,160.4) and (322.6,263.9) .. (224.94,29.76) ;
                                \draw  [draw opacity=0][fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ] (222.51,139.45) .. controls (222.51,137.95) and (223.72,136.75) .. (225.21,136.75) .. controls (226.7,136.75) and (227.91,137.95) .. (227.91,139.45) .. controls (227.91,140.94) and (226.7,142.15) .. (225.21,142.15) .. controls (223.72,142.15) and (222.51,140.94) .. (222.51,139.45) -- cycle ;
                                \draw (144,231) node [anchor=north west][inner sep=0.75pt]    {$A$};
                                \draw (290.9,231.1) node [anchor=north west][inner sep=0.75pt]    {$B$};
                                \draw (332.5,91) node [anchor=north west][inner sep=0.75pt]    {$C$};
                                \draw (217.5,11) node [anchor=north west][inner sep=0.75pt]    {$D$};
                                \draw (100.5,93) node [anchor=north west][inner sep=0.75pt]    {$E$};
                                \draw (142,166) node [anchor=north west][inner sep=0.75pt]    {$( P_{1})$};
                                \draw (228.5,206) node [anchor=north west][inner sep=0.75pt]    {$( P_{2})$};
                                \draw (284,139) node [anchor=north west][inner sep=0.75pt]    {$( P_{3})$};
                                \draw (239,57) node [anchor=north west][inner sep=0.75pt]    {$( P_{4})$};
                                \draw (148.5,82) node [anchor=north west][inner sep=0.75pt]    {$( P_{5})$};
                                \draw (210,125) node [anchor=north west][inner sep=0.75pt]    {$I$};
                            \end{tikzpicture} }'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Trong mặt phẳng với hệ tọa độ $Oxy$, cho ngũ giác đều $ABCDE$ có tâm $I$, $A(-%s; -%s)$, $B(%s; -%s)$ và năm parabol $(P_1), (P_2), (P_3), (P_4), (P_5)$ giống nhau như hình dưới. Biết $(P_1)$ có đỉnh là gốc tọa độ $O$, hỏi diện tích hình phẳng giới hạn bởi năm parabol đã cho bằng bao nhiêu? (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng phần chục).}{%s}'''
                                 % (latex(a), latex(b), latex(a), latex(b), hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải bám sát ảnh
                loigiai = ('''\\begin{center} \\scalebox{0.8}{ 
                    \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                        \\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (246.08,135.6) -- (258.08,154.8) -- (225.21,166.15) -- cycle ;
                        \\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]  (331.06,131.47) -- (290.9,256.1) -- (159.96,256.42) -- (119.19,131.98) -- (224.94,54.76) -- cycle ;
                        \\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (224.94,54.76) .. controls (167.6,214.4) and (185.1,251.4) .. (331.06,131.47) ;
                        \\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (331.06,131.47) .. controls (224.6,127.4) and (90.1,123.9) .. (290.9,256.1) ;
                        \\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (159.96,256.42) .. controls (196.6,109.4) and (243.6,55.4) .. (290.9,256.1) ;
                        \\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (119.19,131.98) .. controls (272.1,117.4) and (335.1,145.4) .. (159.96,256.42) ;
                        \\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (119.19,131.98) .. controls (190.1,185.4) and (322.6,288.9) .. (224.94,54.76) ;
                        \\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (101.5,166) -- (363.8,167.87) ;
                        \\draw [shift={(367.8,167.9)}, rotate = 180.41] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                        \\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (225.3,276.4) -- (225.3,29.9) ;
                        \\draw [shift={(225.3,25.9)}, rotate = 90] [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=1 ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                        \\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (225.21,166.15) -- (277.28,92.4) ;
                        \\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]    (225.21,166.15) -- (331.06,131.47) ;
                        \\draw (144,256) node [anchor=north west][inner sep=0.75pt]    {$A$};
                        \\draw (290.9,256.1) node [anchor=north west][inner sep=0.75pt]    {$B$};
                        \\draw (332.5,116) node [anchor=north west][inner sep=0.75pt]    {$C$};
                        \\draw (203,35) node [anchor=north west][inner sep=0.75pt]    {$D$};
                        \\draw (102,116.5) node [anchor=north west][inner sep=0.75pt]    {$E$};
                        \\draw (140.5,188) node [anchor=north west][inner sep=0.75pt]    {$( P_{1})$};
                        \\draw (228.5,231) node [anchor=north west][inner sep=0.75pt]    {$( P_{2})$};
                        \\draw (280,172) node [anchor=north west][inner sep=0.75pt]    {$( P_{3})$};
                        \\draw (239,82) node [anchor=north west][inner sep=0.75pt]    {$( P_{4})$};
                        \\draw (148.5,104.5) node [anchor=north west][inner sep=0.75pt]    {$( P_{5})$};
                        \\draw (210.5,144.5) node [anchor=north west][inner sep=0.75pt]    {$I$};
                        \\draw (347.7,175) node [anchor=north west][inner sep=0.75pt]    {$x$};
                        \\draw (230.9,25) node [anchor=north west][inner sep=0.75pt]    {$y$};
                        \\draw (204.5,259) node [anchor=north west][inner sep=0.75pt]    {$K$};
                        \\draw (207.6,109) node [anchor=north west][inner sep=0.75pt]    {$O$};
                        \\draw (228.8,108.4) node [anchor=north west][inner sep=0.75pt]    {$M$};
                        \\draw (266.8,149) node [anchor=north west][inner sep=0.75pt]    {$N$};
                        \\draw (274.2,70.24) node [anchor=north west][inner sep=0.75pt]    {$H$};
                    \\end{tikzpicture} }
                \\end{center}
                Ta có $AB = %s$, góc chắn một cạnh của ngũ giác đều là $\\widehat{DIC} = \\frac{360^\\circ}{5} = 72^\\circ$. \\\\
                Gọi $K$ là trung điểm $AB$. Khoảng cách từ tâm $I$ đến $AB$ là $IK = \\frac{AB/2}{\\tan 36^\\circ} = \\frac{%s}{\\tan 36^\\circ}$. \\\\
                Parabol $(P_1)$ có đỉnh là gốc $O(0;0)$, đi qua $A(-%s; -%s)$ và $B(%s; -%s)$ nên phương trình $(P_1)$ là $y = %s x^2$. Chiều cao $OK = %s$. \\\\
                Ta có $OI = OK - IK = %s - \\frac{%s}{\\tan 36^\\circ}$. \\\\
                Do $y_I < 0$ nên tọa độ điểm $I$ là $I\\left(0; \\frac{%s}{\\tan 36^\\circ} - %s\\right)$. \\\\
                Coi $I$ là gốc tọa độ mới (trục hoành $Ix // AB$), phương trình $(P_1)$ trở thành: $Y = %s - \\frac{%s}{\\tan 36^\\circ} - %s X^2$. \\\\
                Đặt $d = %s - \\frac{%s}{\\tan 36^\\circ} \\approx %s$, ta được $(P_1): Y = d - %s X^2$. \\\\
                Gọi $H$ là trung điểm $DC$. Lại có $\\widehat{HIx} = 90^\\circ - 36^\\circ = 54^\\circ \\Rightarrow$ phương trình đường thẳng $IH$ là $Y = X \\tan 54^\\circ$. \\\\
                Gọi $M$ là giao điểm của $(P_1)$ và tia $IH$ (với $X > 0$). Hoành độ $X_M$ thỏa mãn: \\\\
                $d - %s X^2 = X \\tan 54^\\circ \\Rightarrow X_M \\approx %s$. \\\\
                Tương tự, đường thẳng $IC$ có phương trình $Y = X \\tan 18^\\circ$. Gọi $N$ là giao điểm của $(P_1)$ và tia $IC$ (với $X > 0$), hoành độ $X_N$ thỏa mãn: \\\\
                $d - %s X^2 = X \\tan 18^\\circ \\Rightarrow X_N \\approx %s$. \\\\
                Do tính đối xứng, diện tích hình phẳng cần tìm bằng $10$ lần diện tích một phần nhỏ (tô màu). Diện tích phần gạch chéo là: \\\\
                $S_{mau} = \\int_{0}^{X_M} \\left( X \\tan 54^\\circ - X \\tan 18^\\circ \\right) \\mathrm{d}X + \\int_{X_M}^{X_N} \\left( d - %s X^2 - X \\tan 18^\\circ \\right) \\mathrm{d}X \\approx %s$. \\\\
                Vậy diện tích hình phẳng cần tìm là $S = 10 \\cdot S_{mau} \\approx %s$.'''
                % (
                    latex(2*a), latex(a),
                    latex(a), latex(b), latex(a), latex(b), latex(k_sym), latex(b),
                    latex(b), latex(a),
                    latex(a), latex(b),
                    latex(b), latex(a), latex(p_sym),
                    latex(b), latex(a), d_str, latex(p_sym),
                    latex(p_sym), xm_str,
                    latex(p_sym), xn_str,
                    latex(p_sym), S_gach_str,
                    kq_str
                ))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

