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


def bt_dang41_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # --- Hàm bổ trợ để làm sạch số và định dạng phân số ---
            def clean_num(val):
                # Nếu là đối tượng Rational của SymPy (phân số)
                if isinstance(val, sp.Rational):
                    if val.q == 1: # Nếu mẫu số bằng 1 thì trả về số nguyên
                        return str(val.p)
                    return r"\dfrac{" + str(val.p) + "}{" + str(val.q) + "}"

                # Nếu là số thực (float/int)
                try:
                    f_val = float(val)
                    if f_val.is_integer():
                        return str(int(f_val))
                    return str(f_val).replace('.', ',')
                except:
                    return str(val).replace('.', ',')

            # --- Bước 3: Random bài toán ---
            list_AB = [4, 6, 8, 10]
            list_cost = [10, 15, 20, 25]

            AB_val = random.choice(list_AB)
            cost_val = random.choice(list_cost)
            AD_val = AB_val // 2

            # Sử dụng Rational để giữ định dạng phân số
            R = Rational(AB_val, 2) 
            r = Rational(AD_val, 2) 

            x = symbols('x')
            f_line_sq = Rational(1, 3) * x**2 
            f_big_circle_sq = 2*R*x - x**2
            f_small_circle_sq = 2*r*x - x**2

            # Hoành độ giao điểm (Dạng phân số)
            x_inter_big = Rational(3, 2) * R
            x_inter_small = Rational(3, 2) * r

            # --- Tính toán Thể tích ---
            def to_dfrac_pi(coeff):
                p = sp.numer(coeff)
                q = sp.denom(coeff)
                if q == 1:
                    return str(p) + r"\pi"
                return r"\dfrac{" + str(p) + "}{" + str(q) + r"}\pi"

            V1_total_coeff = integrate(f_line_sq, (x, 0, x_inter_big)) + integrate(f_big_circle_sq, (x, x_inter_big, AB_val))
            V2_total_coeff = integrate(f_line_sq, (x, 0, x_inter_small)) + integrate(f_small_circle_sq, (x, x_inter_small, AD_val))
            V_res_coeff = V1_total_coeff - V2_total_coeff

            V1_latex = to_dfrac_pi(V1_total_coeff)
            V2_latex = to_dfrac_pi(V2_total_coeff)
            V_res_latex = to_dfrac_pi(V_res_coeff)

            # Tính tiền
            total_cost_val = float(V_res_coeff.evalf() * sp.pi.evalf()) * cost_val
            final_ans = int(Decimal(total_cost_val).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

            # --- Phương án trắc nghiệm ---
            da_dung = str(final_ans)
            s_wrong = set()
            while len(s_wrong) < 3:
                sai = final_ans + random.choice([-20, -10, 10, 20, 30, -15, 15])
                if sai > 0 and str(sai) != da_dung:
                    s_wrong.add(str(sai))

            list_options = [da_dung] + list(s_wrong)
            random.shuffle(list_options)

            list_1 = []
            for item in list_options:
                if item == da_dung:
                    list_1.append(r'\True ' + item)
                else:
                    list_1.append(item)

            # --- TikZ ---
            sc = 6.0 / AB_val 
            tikz_code = "\\begin{tikzpicture}[scale=" + str(sc) + ", line cap=round, line join=round, line width=1pt]\n" \
                "    \\fill[yellow] (0,0) -- ({" + str(float(x_inter_big)) + "}, {" + str(float(x_inter_big*sqrt(3)/3)) + "}) \n" \
                "        arc[start angle=60, end angle=0, radius=" + str(float(R)) + "] -- (" + str(AD_val) + ",0)\n" \
                "        arc[start angle=0, end angle=60, radius=" + str(float(r)) + "] -- cycle;\n" \
                "    \\draw (0,0) arc[start angle=180, end angle=0, radius=" + str(float(R)) + "];\n" \
                "    \\draw (0,0) arc[start angle=180, end angle=0, radius=" + str(float(r)) + "];\n" \
                "    \\draw (0,0) -- (" + str(AB_val) + ",0);\n" \
                "    \\draw (0,0) -- ({" + str(float(x_inter_big)+0.5) + "}, {" + str(float((x_inter_big+0.5)*sqrt(3)/3)) + "});\n" \
                "    \\node[below left] at (0,0) {$A$};\n" \
                "    \\node[below right] at (" + str(AB_val) + ",0) {$B$};\n" \
                "    \\node[below] at (" + str(AD_val) + ",0) {$D$};\n" \
                "    \\node[above right] at ({" + str(float(x_inter_big)) + "}, {" + str(float(x_inter_big*sqrt(3)/3)) + "}) {$C$};\n" \
                "    \\node at ({" + str(float(R)*1.1) + "}, {" + str(float(R)*0.4) + "}) {$(H)$};\n" \
                "    \\draw (0.6,0) arc [start angle=0, end angle=30, radius=0.6];\n" \
                "    \\node at (0.9,0.25) {\\small $30^\\circ$};\n" \
                "\\end{tikzpicture}"

            # --- Nội dung câu hỏi và lời giải ---
            noidungcauhoi = (
                "Trên mặt phẳng vẽ hai nửa đường tròn đường kính $AB, AD$, với $AB = 2AD = " + str(AB_val) + "$ cm như hình vẽ. "
                "Cho biết $\\widehat{BAC} = 30^\\circ$. Hình phẳng $(H)$ là phần tô đậm nằm giữa hai nửa đường tròn, đường thẳng $AB, AC$. "
                "Một kỹ sư cần chế tạo chi tiết máy bằng thép có dạng tròn xoay khi xoay hình phẳng $(H)$ quanh trục $AB$. "
                "Biết chi phí sản xuất là " + str(cost_val) + " nghìn đồng/cm$^3$. "
                "Giá tiền sản xuất một chi tiết máy là bao nhiêu nghìn đồng? (Kết quả làm tròn đến hàng đơn vị)."
                "\n\\begin{center}\n" + tikz_code + "\n\\end{center}"
            )

            loigiai = (
                "Chọn hệ trục tọa độ $Oxy$ sao cho gốc tọa độ $O$ trùng với điểm $A$, tia $Ox$ trùng với tia $AB$. "
                "Khi đó ta có tọa độ các điểm: $A(0;0), D(" + str(AD_val) + ";0)$ và $B(" + str(AB_val) + ";0)$. \\\\ "
                "Phương trình của hai nửa đường tròn nằm phía trên trục hoành: \\\\ "
                "Nửa đường tròn lớn đường kính $AB$ (tâm $(" + clean_num(R) + ";0)$, bán kính $R = " + clean_num(R) + "$): $y = \\sqrt{" + clean_num(2*R) + "x - x^2}$ với $x \\in \\left[ 0;" + str(AB_val) + " \\right]$. \\\\ "
                "Nửa đường tròn nhỏ đường kính $AD$ (tâm $\\left(" + clean_num(r) + ";0\\right)$, bán kính $r = " + clean_num(r) + "$): $y = \\sqrt{" + clean_num(2*r) + "x - x^2}$ với $x \\in \\left[ 0;" + str(AD_val) + " \\right]$. \\\\ "
                "Đường thẳng $AC$ đi qua gốc tọa độ $O$ và tạo với tia $Ox$ một góc $30^\\circ$ nên có hệ số góc $k = \\tan\\left( 30^\\circ \\right) = \\frac{\\sqrt{3}}{3}$. "
                "Phương trình $AC: y = \\frac{\\sqrt{3}}{3}x$. \\\\ "
                "Hoành độ giao điểm của $AC$ với đường tròn lớn là $x = " + clean_num(x_inter_big) + "$, với đường tròn nhỏ là $x = " + clean_num(x_inter_small) + "$. \\\\ "
                "Thể tích khối lớn $V_1$ (quay phần giới hạn bởi $AC$, nửa đường tròn lớn và trục $Ox$): \\\\ "
                "$V_1 = \\pi \\int_{0}^{" + clean_num(x_inter_big) + "} \\left( \\frac{\\sqrt{3}}{3}x \\right)^2 dx + \\pi \\int_{" + clean_num(x_inter_big) + "}^{" + str(AB_val) + "} \\left( " + clean_num(2*R) + "x - x^2 \\right) dx = " + V1_latex + "$. \\\\ "
                "Thể tích khối nhỏ $V_2$ (quay phần giới hạn bởi $AC$, nửa đường tròn nhỏ và trục $Ox$): \\\\ "
                "$V_2 = \\pi \\int_{0}^{" + clean_num(x_inter_small) + "} \\left( \\frac{\\sqrt{3}}{3}x \\right)^2 dx + \\pi \\int_{" + clean_num(x_inter_small) + "}^{" + str(AD_val) + "} \\left( " + clean_num(2*r) + "x - x^2 \\right) dx = " + V2_latex + "$. \\\\ "
                "Thể tích chi tiết máy là: $V = V_1 - V_2 = " + V_res_latex + " \\text{ (cm}^3\\text{)}$. \\\\ "
                "Giá tiền để sản xuất một chi tiết máy là: $T = V \\cdot " + str(cost_val) + " \\approx " + clean_num(round(total_cost_val, 2)) + "$ nghìn đồng. "
                "Làm tròn đến hàng đơn vị ta được " + da_dung + " nghìn đồng."
            )
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(da_dung))
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

