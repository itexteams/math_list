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


def bt_dang15_p3_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo các ký hiệu
            x, y = symbols('x y')

            # B1 & B3: Nghiên cứu đề bài và thiết lập random
            def generate_problem():
                while True:
                    # Tạo tọa độ A, B sao cho trung điểm E là số nguyên
                    xA = random.randint(-5, 2)
                    yA = random.randint(-2, 5)

                    # Để trung điểm là số nguyên, khoảng cách x và y giữa A và B phải là số chẵn
                    u_ab = random.choice([2, 4, 6]) 
                    v_ab = random.choice([2, 4])
                    xB, yB = xA + u_ab, yA + v_ab

                    xC = random.randint(xB + 1, xB + 6)
                    yC = random.randint(yA - 3, yA + 1)

                    # Kiểm tra không thẳng hàng
                    if (xB - xA) * (yC - yA) == (yB - yA) * (xC - xA):
                        continue

                    A = Point(xA, yA)
                    B = Point(xB, yB)
                    C = Point(xC, yC)
                    E = (A + B) / 2

                    # Gán giá trị xE, yE để tránh NameError
                    xE_val, yE_val = E.x, E.y

                    vec_AB = B - A 
                    u, v = vec_AB[0], vec_AB[1]

                    # Đường trung trực d của AB: u(x - xE) + v(y - yE) = 0
                    d_eq = Eq(u*(x - xE_val) + v*(y - yE_val), 0)

                    # Đường thẳng CD: v(x - xC) - u(y - yC) = 0 (pháp tuyến vuông với AB)
                    cd_eq = Eq(v*(x - C.x) - u*(y - C.y), 0)

                    # Giao điểm F của d và CD
                    sol = solve([d_eq, cd_eq], (x, y))
                    if not sol: continue
                    xF_val, yF_val = sol[x], sol[y]

                    # D đối xứng C qua d => F là trung điểm CD
                    xD_val = 2*xF_val - C.x
                    yD_val = 2*yF_val - C.y

                    # Kiểm tra điều kiện hình thang cân (vectơ DC và AB cùng hướng)
                    if (xC - xD_val) * u < 0: 
                        continue

                    # Chỉ lấy kết quả tọa độ nguyên cho đẹp
                    if xD_val.is_Integer and yD_val.is_Integer and xF_val.is_Integer and yF_val.is_Integer:
                        return xA, yA, xB, yB, xC, yC, xE_val, yE_val, u, v, xF_val, yF_val, xD_val, yD_val

            # Thực thi hàm để lấy dữ liệu
            xA, yA, xB, yB, xC, yC, xE, yE, u, v, xF, yF, xD, yD = generate_problem()

            # Rút gọn phương trình đường thẳng
            def simplify_line_eq(a, b, const_val):
                common = gcd(gcd(a, b), const_val)
                a, b, const_val = a//common, b//common, const_val//common
                if a < 0 or (a == 0 and b < 0):
                    a, b, const_val = -a, -b, -const_val
                return a, b, const_val

            # Phương trình d
            a1, b1, c1 = simplify_line_eq(u, v, u*xE + v*yE)
            line_d_str = str(Poly(a1*x + b1*y - c1, x, y).as_expr()) + " = 0"

            # Phương trình CD
            a2, b2, c2 = simplify_line_eq(v, -u, v*xC - u*yC)
            line_cd_str = str(Poly(a2*x + b2*y - c2, x, y).as_expr()) + " = 0"

            # B4: Điều chỉnh phương án sai
            kq = int(yD)
            s = {str(kq + 1), str(kq + 2), str(kq - 1), str(kq - 2), str(int(xD)), str(int(yF))}
            wrong_options = random.sample(list(s - {str(kq)}), 3)

            # Câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(%s;%s), B(%s;%s), C(%s;%s)$. Tung độ điểm $D$ để tứ giác $ABCD$ là hình thang cân với hai đáy $AB, CD$ bằng bao nhiêu?'''
                             %(latex(xA), latex(yA), latex(xB), latex(yB), latex(xC), latex(yC)))

            # Các đáp án
            da_d = '\\True $' + str(kq) + '$'
            da_s1 = '$' + str(wrong_options[0]) + '$'
            da_s2 = '$' + str(wrong_options[1]) + '$'
            da_s3 = '$' + str(wrong_options[2]) + '$'

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Hình vẽ TikZ
            tikz_code = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.6, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                \\coordinate (A) at (0,2);
                \\coordinate (B) at (2.5,2);
                \\coordinate (C) at (4,0);
                \\coordinate (D) at (-1.5,0);
                \\coordinate (E) at (1.25,2);
                \\coordinate (F) at (1.25,0);
                \\draw[thick] (A) node[above left]{$A$} -- (B) node[above right]{$B$} -- (C) node[below right]{$C$} -- (D) node[below left]{$D$} -- cycle;
                \\draw (E) node[above left]{$E$} -- (F) node[below left]{$F$};
                \\draw (1.25,2.8) -- (1.25,-0.8) node[right]{$d$};
            \\end{tikzpicture}
            \\end{center}''')

            # Nội dung lời giải
            loigiai = (tikz_code + '''Ta có: $\\overrightarrow{AB} = (%s; %s)$.\\\\
            Gọi $E$ là trung điểm của đoạn thẳng $AB$, ta tính được tọa độ $E(%s; %s)$.\\\\
            Đường trung trực $d$ của cạnh $AB$ đi qua $E$ và vuông góc với $AB$ nên có phương trình là: $%s$.\\\\
            Đường thẳng $CD$ đi qua điểm $C$ và song song với đường thẳng $AB$ nên có phương trình là: $%s$.\\\\
            Giao điểm $F$ của hai đường thẳng $CD$ và đường trung trực $d$ có tọa độ là $F(%s; %s)$.\\\\
            Vì tứ giác $ABCD$ là hình thang cân với hai đáy $AB, CD$ nên $D$ đối xứng với $C$ qua đường thẳng $d$. Khi đó $F$ là trung điểm của đoạn thẳng $CD$.\\\\
            Áp dụng công thức tọa độ trung điểm, ta có tọa độ điểm $D$:\\\\
            $\\begin{cases} x_D = 2x_F - x_C = 2 \\cdot (%s) - (%s) = %s \\\\ y_D = 2y_F - y_C = 2 \\cdot (%s) - (%s) = %s \\end{cases}$ $\\Rightarrow D(%s; %s)$.\\\\
            Thử lại, ta thấy $\\overrightarrow{DC} = (%s; %s)$ và $\\overrightarrow{AB} = (%s; %s)$ cùng hướng nên $D$ thỏa mãn.\\\\
            Vậy tung độ của điểm $D$ là $%s$.'''
                       %(latex(u), latex(v), latex(xE), latex(yE), 
                         line_d_str, line_cd_str, latex(xF), latex(yF),
                         latex(xF), latex(xC), latex(xD), latex(yF), latex(yC), latex(yD),
                         latex(xD), latex(yD), latex(xC-xD), latex(yC-yD), latex(u), latex(v), latex(yD)))
            dapan='\\shortans[0]{$%s$}\n'%(latex(yD))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

