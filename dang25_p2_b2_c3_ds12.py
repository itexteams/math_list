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


def bt_dang25_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')
            x = symbols('x')

            # --- BƯỚC 1: RANDOM THÔNG SỐ ---
            # Mô hình: C = k * (a + b * tích phân t^(1/4) từ 0 đến x)
            k = random.choice([4000, 5000, 6000]) 
            a = random.choice([20, 25, 30])
            b = random.choice([2, 3, 4])
            so_tien_ngan_sach = random.choice([10, 15, 20]) * 10**6 # triệu đồng
            so_nam_du_tinh = 10

            # Tính toán các giá trị cơ bản
            # Chi phí mua (x=0)
            chi_phi_mua = k * a

            # Biểu thức tích phân: 3 * tích phân t^(1/4) dt = 3 * (4/5 * t^(5/4))
            # C(x) = k * (a + b * (4/5) * x^(5/4))
            def calculate_C(val_x):
                # Tích phân từ 0 đến val_x của t^(1/4) là (4/5) * val_x^(5/4)
                tp = Rational(4, 5) * (val_x**(Rational(5, 4)))
                return k * (a + b * tp)

            # Tính giá trị cụ thể
            C_0 = chi_phi_mua
            C_1 = calculate_C(1)
            bao_tri_nam_dau = C_1 - C_0

            # Giải phương trình chi phí bảo trì = chi phí mua tại năm x
            # k * b * (4/5) * x^(5/4) = k * a  => x^(5/4) = (5*a)/(4*b)
            x_val_equal = (Rational(5 * a, 4 * b))**(Rational(4, 5))
            x_approx = round(float(x_val_equal), 2)

            # Tính cho câu VDC
            C_10 = calculate_C(so_nam_du_tinh)
            max_san_pham = int(so_tien_ngan_sach / float(C_10))

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            # Lưu ý dùng \text{d}t trong latex
            formula_latex = r'C = %s \left( %s + %s \int_{0}^{x} t^{\frac{1}{4}} \text{d}t \right)' % (k, a, b)
            noidungcauhoi = r'''Giả sử chi phí mua và bảo trì một thiết bị trong $x$ năm có thể được mô hình hóa theo công thức $%s$.''' % formula_latex

            # --- BƯỚC 3: CÁC MỨC ĐỘ ---

            # --- Nhận biết (Chi phí mua) ---
            nb_da_1_d = r'\True Chi phí mua 1 sản phẩm ban đầu là $%s$ đồng' % (f"{C_0:,}".replace(",", "."))
            nb_da_1_s = r'Chi phí mua 1 sản phẩm ban đầu là $%s$ đồng' % (f"{k*b:,}".replace(",", "."))
            list_nb = [nb_da_1_d, nb_da_1_s]
            nb_selected = random.choice(list_nb)
            loigiai_nb = r'''Chi phí mua ứng với $x=0$, khi đó $C = %s \cdot %s = %s$.''' % (k, a, f"{C_0:,}".replace(",", "."))

            # --- Thông hiểu (Bảo trì năm đầu) ---
            th_da_1_d = r'\True Chi phí bảo trì năm đầu tiên của sản phẩm là $%s$ đồng' % (f"{int(bao_tri_nam_dau):,}".replace(",", "."))
            th_da_1_s = r'Chi phí bảo trì năm đầu tiên của sản phẩm là $%s$ đồng' % (f"{int(C_1):,}".replace(",", "."))
            list_th = [th_da_1_d, th_da_1_s]
            th_selected = random.choice(list_th)
            loigiai_th = r'''Với $x=1$ ta có $C(1) = %s \left( %s + %s \int_{0}^{1} t^{\frac{1}{4}} \text{d}t \right) = %s$. \\
                Suy ra chi phí bảo trì năm đầu là $C(1) - C(0) = %s$.''' % (k, a, b, f"{int(C_1):,}".replace(",", "."), f"{int(bao_tri_nam_dau):,}".replace(",", "."))

            # --- Vận dụng (Thời điểm bảo trì bằng giá mua) ---
            vd_da_1_d = r'\True Số năm mà tiền bảo trì bằng tiền mua sản phẩm là khoảng $%s$ năm' % x_approx
            vd_da_1_s = r'Số năm mà tiền bảo trì bằng tiền mua sản phẩm là khoảng $%s$ năm' % round(x_approx + 2.1, 2)
            list_vd = [vd_da_1_d, vd_da_1_s]
            vd_selected = random.choice(list_vd)
            loigiai_vd = r'''Tiền bảo trì bằng tiền mua khi tổng chi phí $C = 2 \times %s = %s$. \\
                Ta có phương trình: $%s \left( %s + %s \cdot \frac{4}{5} x^{\frac{5}{4}} \right) = %s \Rightarrow x \approx %s$.''' % (f"{C_0:,}".replace(",", "."), f"{2*C_0:,}".replace(",", "."), k, a, b, f"{2*C_0:,}".replace(",", "."), x_approx)

            # --- Vận dụng cao (Ngân sách) ---
            vdc_da_1_d = r'\True Với %s triệu đồng, họ có thể mua và bảo trì tối đa %s sản phẩm trong 10 năm' % (int(so_tien_ngan_sach/10**6), max_san_pham)
            vdc_da_1_s = r'Với %s triệu đồng, họ có thể mua và bảo trì tối đa %s sản phẩm trong 10 năm' % (int(so_tien_ngan_sach/10**6), max_san_pham + 5)
            list_vdc = [vdc_da_1_d, vdc_da_1_s]
            vdc_selected = random.choice(list_vdc)
            loigiai_vdc = r'''Chi phí cho 1 sản phẩm trong 10 năm là $C(10) \approx %s$. \\
                Số sản phẩm tối đa là $\left\lfloor \frac{%s}{%s} \right\rfloor = %s$.''' % (f"{float(C_10):,.2f}".replace(",", "."), f"{so_tien_ngan_sach:,}".replace(",", "."), f"{float(C_10):,.2f}".replace(",", "."), max_san_pham)

            # --- XUẤT KẾT QUẢ ---
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + '\n'
                '\\choiceTFn \n'
                '{' + nb_selected + '}\n'
                '{' + th_selected + '}\n'
                '{' + vd_selected + '}\n'
                '{' + vdc_selected + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb + '\n'
                '\\item ' + loigiai_th + '\n'
                '\\item ' + loigiai_vd + '\n'
                '\\item ' + loigiai_vdc + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

