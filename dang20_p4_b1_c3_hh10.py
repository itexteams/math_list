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


def bt_dang20_p4_b1_c3_hh10(self):
            # Khai báo biến và chọn dạng (Trục Ox hoặc Trục Oy)
            # Khai báo các biến ký hiệu
            x, y = symbols('x y')

            # Bước 1: Random dữ liệu bài toán
            def generate_problem():
                while True:
                    # Random hệ số cho d1: a1x + b1y + c1 = 0
                    a1, b1 = random.randint(-3, 3), random.randint(-3, 3)
                    if a1 == 0 and b1 == 0: b1 = 1
                    c1 = random.randint(-10, 10)

                    # Random hệ số cho d2: a2x + b2y + c2 = 0
                    a2, b2 = random.randint(-3, 3), random.randint(-3, 3)
                    if a2 == 0 and b2 == 0: b2 = 1
                    c2 = random.randint(-10, 10)

                    # Đảm bảo d1 và d2 không song song
                    if a1*b2 - a2*b1 == 0: continue

                    # Random điểm M(xM, yM)
                    xM, yM = random.randint(-5, 5), random.randint(-5, 5)

                    # Kiểm tra xem M có nằm trên d1 hoặc d2 không (tránh trường hợp suy biến)
                    if a1*xM + b1*yM + c1 == 0 or a2*xM + b2*yM + c2 == 0: continue

                    # Bước 2: Giải toán bằng Sympy để lấy kết quả chuẩn
                    xA, yA, xB, yB = symbols('xA yA xB yB')

                    # Hệ phương trình:
                    # 1. A thuộc d1
                    # 2. B thuộc d2
                    # 3. M là trung điểm AB => xA + xB = 2*xM, yA + yB = 2*yM
                    eq1 = Eq(a1*xA + b1*yA + c1, 0)
                    eq2 = Eq(a2*xB + b2*yB + c2, 0)
                    eq3 = Eq(xA + xB, 2*xM)
                    eq4 = Eq(yA + yB, 2*yM)

                    sol = solve((eq1, eq2, eq3, eq4), (xA, yA, xB, yB))

                    if sol:
                        # Lấy tọa độ điểm A
                        val_xA = sol[xA]
                        val_yA = sol[yA]

                        # Viết phương trình Delta đi qua M(xM, yM) và A(xA, yA)
                        # Vectơ chỉ phương u = (xA - xM, yA - yM)
                        # Vectơ pháp tuyến n = (-(yA - yM), xA - xM)
                        dx = val_xA - xM
                        dy = val_yA - yM

                        if dx == 0 and dy == 0: continue # M trùng A

                        # Pháp tuyến n = (A, B) -> Ax + By + C = 0
                        A_coeff = -dy
                        B_coeff = dx
                        C_coeff = -(A_coeff*xM + B_coeff*yM)

                        # Tối giản phương trình đường thẳng
                        common = simplify(A_coeff).as_numer_denom()[0] # Lấy tử số nếu là phân số
                        # Đơn giản hóa các hệ số nguyên
                        import math
                        def get_gcd(a, b, c):
                            a, b, c = int(a), int(b), int(c)
                            return math.gcd(math.gcd(a, b), c)

                        # Chuyển về số nguyên để rút gọn
                        # Nhân với mẫu số chung nếu cần (Sympy đã lo phần phân số, ta lấy tử)
                        # Ở đây ta dùng hàm chuẩn hóa của đường thẳng
                        pt_delta = simplify(A_coeff*x + B_coeff*y + C_coeff)
                        # Trích xuất hệ số cuối cùng
                        final_coeffs = pt_delta.as_coefficients_dict()
                        h_a = final_coeffs.get(x, 0)
                        h_b = final_coeffs.get(y, 0)
                        h_c = final_coeffs.get(1, 0)

                        # Đảm bảo hệ số x dương cho đẹp
                        if h_a < 0 or (h_a == 0 and h_b < 0):
                            h_a, h_b, h_c = -h_a, -h_b, -h_c

                        res_string = latex(h_a*x + h_b*y + h_c) + " = 0"
                        return (a1, b1, c1, a2, b2, c2, xM, yM, val_xA, val_yA, res_string, h_a, h_b, h_c)

            # Chạy tạo dữ liệu
            a1, b1, c1, a2, b2, c2, xM, yM, v_xA, v_yA, dap_an_dung, ha, hb, hc = generate_problem()

            # Tạo các đáp án nhiễu
            du = ["$" + dap_an_dung + "$"]
            s = [
                "$" + latex(ha*x + hb*y + random.randint(-5, 5)) + " = 0$",
                "$" + latex(hb*x - ha*y + hc) + " = 0$",
                "$" + latex(ha*x - hb*y + random.randint(-10, 10)) + " = 0$",
                "$" + latex(ha*x + hb*y - hc) + " = 0$"
            ]
            random.shuffle(s)
            da_s1, da_s2, da_s3 = s[0], s[1], s[2]

            # Nội dung câu hỏi
            d1_str = latex(a1*x + b1*y + c1) + " = 0"
            d2_str = latex(a2*x + b2*y + c2) + " = 0"
            M_coords = "(" + str(xM) + ";" + str(yM) + ")"

            noidungcauhoi = ("Cho đường thẳng $d_1: %s$; $d_2: %s$ và điểm $M%s$. Lập phương trình đường thẳng $\\Delta$ đi qua điểm $M$, cắt $d_1$ và $d_2$ lần lượt tại $A$ và $B$ sao cho $M$ là trung điểm của đoạn $AB$."
                             %(d1_str, d2_str, M_coords))

            # Lời giải chi tiết
            # Biểu diễn y theo x cho d1 và d2 (phục vụ trình bày giống ảnh)
            def expr_y(a, b, c):
                if b != 0:
                    return latex(simplify((-a*x - c)/b))
                return "..."

            loigiai = ("Gọi $A(x_A; y_A) \\in d_1$. Suy ra phương trình liên hệ: $%s = 0$. \\\\"
                       "Gọi $B(x_B; y_B) \\in d_2$. Suy ra phương trình liên hệ: $%s = 0$. \\\\"
                       "Vì $M$ là trung điểm của $AB$ nên ta có hệ thức: \\\\"
                       "$\\begin{cases} x_A + x_B = 2x_M \\\\ y_A + y_B = 2y_M \\end{cases} \\Rightarrow \\begin{cases} x_A + x_B = %s \\\\ y_A + y_B = %s \\end{cases}$. \\\\"
                       "Thay tọa độ vào phương trình đường thẳng, ta giải hệ tìm được $A = (%s; %s)$. \\\\"
                       "Đường thẳng $\\Delta$ đi qua hai điểm $A$ và $M$. \\\\"
                       "Từ đó suy ra phương trình $\\Delta: %s$."
                       %(d1_str, d2_str, latex(2*xM), latex(2*yM), latex(v_xA), latex(v_yA), dap_an_dung))

            # Trộn đáp án
            da_d = "\\True " + du[0]
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

