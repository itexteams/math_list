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


def bt_dang5_p3_b2_c4_ds11(self):
            # Khai báo biến
            # --- KHỞI TẠO BIẾN ---
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Random tham số
                # Chọn a để giới hạn lim_phai = 1/a là số hữu tỉ đẹp
                m=symbols('m')
                a = random.randint(1, 3) 
                coeff = random.choice([2, 4, 6]) # Hệ số của m

                # 2. Thiết lập biểu thức toán học
                # Nhánh phải: 1/(x-a) - 3a^2/(x^3 - a^3)
                tu_so_2 = 3 * (a**2)
                mau_so_2 = a**3

                f_phai = 1/(x - a) - tu_so_2/(x**3 - a**3)
                lim_phai = limit(f_phai, x, a, dir='+') # Kết quả sẽ là 1/a

                # Nhánh trái: x + m^2/2 - coeff*m
                # Giới hạn trái: a + m^2/2 - coeff*m
                lim_trai_bieu_thuc = a + (m**2 / 2) - coeff * m

                # 3. Giải phương trình tìm m
                phuong_trinh = lim_trai_bieu_thuc - lim_phai
                tap_nghiem = solve(phuong_trinh, m)

                # 4. Tính tổng các giá trị m
                tong_m = sum(tap_nghiem)
                tong_m_latex = latex(tong_m)

                # --- TẠO NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (r'''Cho hàm số $f(x) = \begin{cases} \dfrac{1}{x-%s} - \dfrac{%s}{x^3-%s} & \text{khi } x > %s \\ x + \dfrac{m^2}{2} - %sm & \text{khi } x \le %s \end{cases}$. Tổng các giá trị của tham số $m$ để hàm số có giới hạn tại $x = %s$ bằng bao nhiêu?'''
                                % (latex(a), latex(tu_so_2), latex(mau_so_2), latex(a), latex(coeff), latex(a), latex(a)))

                # --- TẠO ĐÁP ÁN ---
                da_dung = r'$S = %s$' % tong_m_latex

                # Tạo các đáp án nhiễu
                da_sai1 = r'$S = %s$' % latex(tong_m + random.choice([1, 2]))
                da_sai2 = r'$S = %s$' % latex(tong_m - random.choice([1, 2]))
                da_sai3 = r'$S = %s$' % latex(-tong_m)

                if tong_m == 0:
                    da_sai3 = r'$S = 1$'

                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(da_sai1), str(da_sai2), str(da_sai3)]
                random.shuffle(list_1)

                # --- TẠO LỜI GIẢI CHI TIẾT ---
                da_thuc_tu = simplify(x**2 + a*x + a**2 - tu_so_2)
                da_thuc_rut_gon = simplify(da_thuc_tu / (x - a))

                # Chuẩn bị chuỗi liệt kê nghiệm m
                nghiem_list = [latex(sol) for sol in tap_nghiem]
                if len(tap_nghiem) > 1:
                    dong_nghiem = r"\Leftrightarrow \hoac{ " + r" \\ ".join(["m=" + n for n in nghiem_list]) + r" }."
                    buoc_tong = r"Tổng các giá trị của $m$ là: $S = %s = %s$." % (" + ".join(nghiem_list), tong_m_latex)
                elif len(tap_nghiem) == 1:
                    dong_nghiem = r"\Leftrightarrow m = " + nghiem_list[0]
                    buoc_tong = r"Hàm số chỉ có một giá trị $m$ thỏa mãn nên tổng $S = %s$." % nghiem_list[0]
                else:
                    dong_nghiem = r"\text{Vô nghiệm}"
                    buoc_tong = r"Không có giá trị $m$ nào thỏa mãn."

                loigiai = (r'''Ta có: \\
                            $\bullet$ $\displaystyle \lim_{x \to %s^+} f(x) = \lim_{x \to %s^+} \left( \frac{1}{x-%s} - \frac{%s}{x^3-%s} \right) = \lim_{x \to %s^+} \frac{x^2+%sx+%s-%s}{(x-%s)(x^2+%sx+%s)}$ \\
                            $= \displaystyle \lim_{x \to %s^+} \frac{%s}{(x-%s)(x^2+%sx+%s)} = \lim_{x \to %s^+} \frac{%s}{x^2+%sx+%s} = %s$. \\
                            $\bullet$ $\displaystyle \lim_{x \to %s^-} f(x) = \lim_{x \to %s^-} \left( x + \frac{m^2}{2} - %sm \right) = \frac{m^2}{2} - %sm + %s$. \\
                            Hàm số có giới hạn tại $x = %s$ khi và chỉ khi $\displaystyle \lim_{x \to %s^+} f(x) = \lim_{x \to %s^-} f(x)$ \\
                            $\Leftrightarrow \frac{m^2}{2} - %sm + %s = %s \Leftrightarrow %s = 0$ \\
                            $%s$. \\
                            %s'''
                            % (latex(a), latex(a), latex(a), latex(tu_so_2), latex(mau_so_2), 
                               latex(a), latex(a), latex(a**2), latex(tu_so_2), latex(a), latex(a), latex(a**2),
                               latex(a), latex(da_thuc_tu), latex(a), latex(a), latex(a**2),
                               latex(a), latex(da_thuc_rut_gon), latex(a), latex(a**2), latex(lim_phai),
                               latex(a), latex(a), latex(coeff), latex(coeff), latex(a),
                               latex(a), latex(a), latex(a),
                               latex(coeff), latex(a), latex(lim_phai), latex(simplify(2*phuong_trinh)),
                               dong_nghiem, buoc_tong))

            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(tong_m_latex))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

