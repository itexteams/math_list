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


def bt_dang59_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Lựa chọn các cặp (Bán kính R, khoảng cách a = AH = BK) 
                # sao cho 2*a*R là số chính phương để cận tích phân luôn là số nguyên
                pairs = [(9, 2), (8, 4), (18, 4), (16, 2), (25, 8), (25, 2)]
                R_val, a_val = random.choice(pairs)
                AB_val = 2 * R_val

                # Tọa độ các điểm và thông số
                x_K = R_val - a_val
                y_K_sq = 2 * a_val * R_val - a_val**2
                r_sq = 2 * a_val * R_val
                r_val = int(math.sqrt(r_sq))

                # Cận dưới của tích phân phần 1
                lower_lim = R_val - r_val

                # Tính các tích phân (Thể tích) - để dạng phân số chính xác
                V1_expr = integrate(r_sq - (x - R_val)**2, (x, lower_lim, x_K))
                V2_expr = integrate(R_val**2 - x**2, (x, x_K, R_val))

                # Thể tích khối cầu lớn
                V_sphere = Rational(4, 3) * R_val**3

                # Tổng thể tích vật trang trí
                V_total = V_sphere - 2 * (V1_expr + V2_expr)

                # Tính ra số thập phân và làm tròn đến hàng đơn vị
                V_num = float(V_total * pi.evalf())
                while V_num>9999:
                    pairs = [(9, 2), (8, 4), (18, 4), (16, 2), (25, 8), (25, 2)]
                    R_val, a_val = random.choice(pairs)
                    AB_val = 2 * R_val

                    # Tọa độ các điểm và thông số
                    x_K = R_val - a_val
                    y_K_sq = 2 * a_val * R_val - a_val**2
                    r_sq = 2 * a_val * R_val
                    r_val = int(math.sqrt(r_sq))

                    # Cận dưới của tích phân phần 1
                    lower_lim = R_val - r_val

                    # Tính các tích phân (Thể tích) - để dạng phân số chính xác
                    V1_expr = integrate(r_sq - (x - R_val)**2, (x, lower_lim, x_K))
                    V2_expr = integrate(R_val**2 - x**2, (x, x_K, R_val))

                    # Thể tích khối cầu lớn
                    V_sphere = Rational(4, 3) * R_val**3

                    # Tổng thể tích vật trang trí
                    V_total = V_sphere - 2 * (V1_expr + V2_expr)

                    # Tính ra số thập phân và làm tròn đến hàng đơn vị
                    V_num = float(V_total * pi.evalf())
                kq_int = round(V_num)

                kq = str(kq_int)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Tạo các phương án sai ngẫu nhiên
                s = set()
                while len(s) < 3:
                    offset = random.choice([-20, -15, -10, -5, -2, -1, 1, 2, 5, 10, 15, 20])
                    wrong_ans = kq_int + offset
                    if wrong_ans > 0 and wrong_ans != kq_int:
                        s.add('$%s$' % str(wrong_ans))

                s_list = list(s)
                das1 = s_list[0]
                das2 = s_list[1]
                das3 = s_list[2]
                hinhve=r'''\scalebox{0.8}{  \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ][line width=1]  (91.27,128.3) .. controls (91.27,73.57) and (135.64,29.2) .. (190.37,29.2) .. controls (245.1,29.2) and (289.47,73.57) .. (289.47,128.3) .. controls (289.47,183.03) and (245.1,227.4) .. (190.37,227.4) .. controls (135.64,227.4) and (91.27,183.03) .. (91.27,128.3) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (133,204.8) -- (133,48.13) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (250,204.8) -- (250,48.13) ;
            	\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]    (133,48.13) .. controls (189.07,78.13) and (191.77,164.73) .. (133.7,209.4) ;
            	\draw [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]    (251.6,50.4) .. controls (197.37,80.27) and (195.44,161.92) .. (251.6,206.4) ;
            	\draw [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]    (133,48.13) .. controls (62.9,101.65) and (96.43,191.4) .. (133.7,209.4) ;
            	\draw [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]    (252.1,50.4) .. controls (299.17,86.67) and (307.1,170.65) .. (251.6,206.4) ;
            	\draw [line width=1]    (191,127.67) -- (289.47,127.67) ;
            	\draw [line width=1]    (92.53,127.67) -- (191,127.67) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (133,48.13) -- (133.9,207.4) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (252.1,50.4) -- (251.35,204.65) ;
            	\draw  [line width=1]  (91.27,128.3) .. controls (91.27,73.57) and (135.64,29.2) .. (190.37,29.2) .. controls (245.1,29.2) and (289.47,73.57) .. (289.47,128.3) .. controls (289.47,183.03) and (245.1,227.4) .. (190.37,227.4) .. controls (135.64,227.4) and (91.27,183.03) .. (91.27,128.3) -- cycle ;
            	\draw (73,116.5) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (291,114.5) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (113.5,129) node [anchor=north west][inner sep=0.75pt]    {$H$};
            	\draw (250,129) node [anchor=north west][inner sep=0.75pt]    {$K$};
            \end{tikzpicture} }'''
                # Câu hỏi
                noidungcauhoi = (r'''\immini{Một vật trang trí có dạng một khối tròn xoay được tạo thành khi quay miền $\left(H\right)$ (phần màu xám trong hình vẽ) quanh trục $AB$. Miền $\left(H \right)$ được giới hạn bởi đường tròn đường kính $AB$ và các cung tròn tâm $A, B$ có cùng bán kính. Biết $AB=%s$ cm, $AH = BK = %s$ cm. Thể tích vật trang trí đó bằng bao nhiêu $\text{cm}^3$? (không làm tròn kết quả các phép tính trung gian, chỉ làm tròn kết quả cuối cùng đến hàng đơn vị).}{%s}'''
                                 % (AB_val, a_val,hinhve))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Chọn hệ trục tọa độ $Oxy$ với gốc $O$ là trung điểm của đoạn thẳng $AB$, trục $Ox$ trùng với đường thẳng $AB$. \\\\
                Ta có $A\\left(-%s; 0\\right)$ và $B\\left(%s; 0\\right)$. Phương trình đường tròn đường kính $AB$ là $x^2 + y^2 = %s$. \\\\
                Do $AH = BK = %s$ nên $H\\left(-%s; 0\\right)$ và $K\\left(%s; 0\\right)$. \\\\
                Đường thẳng $x = %s$ cắt đường tròn lớn tại điểm có tung độ $y$ thỏa mãn $y^2 = %s - %s^2 = %s$. \\\\
                Cung tròn tâm $B\\left(%s; 0\\right)$ đi qua điểm này nên có bán kính $R'$ thỏa mãn $R'^2 = \\left(%s - %s\\right)^2 + %s = %s + %s = %s \\Rightarrow R' = %s$. \\\\
                Phương trình đường tròn tâm $B$ là $\\left(x-%s\\right)^2 + y^2 = %s \\Rightarrow y^2 = %s - \\left(x-%s\\right)^2$. \\\\
                Thể tích vật thể tạo thành bằng thể tích khối cầu đường kính $AB$ trừ đi hai lần thể tích phần màu trắng (phần bị khoét) ở hai bên. \\\\
                Xét phần màu trắng bên phải trục $Oy$, thể tích của nó gồm hai phần: \\\\
                Phần 1 $\\left(V_1\\right)$: Quay hình phẳng giới hạn bởi đường tròn tâm $B$ và trục $Ox$, từ $x = %s$ đến $x = %s$ quanh $Ox$: \\\\
                $V_1 = \\pi \\int\\limits_{%s}^{%s} \\left[ %s - \\left(x-%s\\right)^2 \\right] \\mathrm{d}x = %s\\pi$. \\\\
                Phần 2 $\\left(V_2\\right)$: Quay hình phẳng giới hạn bởi đường tròn lớn và trục $Ox$, từ $x=%s$ đến $x=%s$ quanh $Ox$: \\\\
                $V_2 = \\pi \\int\\limits_{%s}^{%s} \\left( %s - x^2 \\right) \\mathrm{d}x = %s\\pi$. \\\\
                Thể tích khối cầu là $V_{c\\text{ầu}} = \\frac{4}{3} \\pi \\cdot %s^3 = %s\\pi$. \\\\
                Thể tích vật trang trí là $V = V_{c\\text{ầu}} - 2\\left(V_1 + V_2\\right) = %s\\pi - 2\\left(%s\\pi + %s\\pi\\right) = %s\\pi \\approx %s$ cm$^3$.'''
                % (R_val, R_val, R_val**2,
                   a_val, x_K, x_K,
                   x_K, R_val**2, x_K, y_K_sq,
                   R_val, R_val, x_K, y_K_sq, a_val**2, y_K_sq, r_sq, r_val,
                   R_val, r_sq, r_sq, R_val,
                   lower_lim, x_K,
                   lower_lim, x_K, r_sq, R_val, latex(V1_expr).replace('(', '\\left(').replace(')', '\\right)'),
                   x_K, R_val,
                   x_K, R_val, R_val**2, latex(V2_expr).replace('(', '\\left(').replace(')', '\\right)'),
                   R_val, latex(V_sphere).replace('(', '\\left(').replace(')', '\\right)'),
                   latex(V_sphere).replace('(', '\\left(').replace(')', '\\right)'), latex(V1_expr).replace('(', '\\left(').replace(')', '\\right)'), latex(V2_expr).replace('(', '\\left(').replace(')', '\\right)'), latex(V_total).replace('(', '\\left(').replace(')', '\\right)'), kq_int))
                dapan='\\shortans[0]{$%s$}\n'%(kq_int)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

