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


def bt_dang50_p1_b3_c5_ds11(self):
            # Khai báo biến
            # H0: Giá nhà ban đầu (từ 800 triệu đến 2 tỷ, bước nhảy 100 triệu)
            H0 = random.randrange(800, 2100, 100) * 10**6 
            # r_salary: Phần trăm tăng lương mỗi 2 năm (từ 5% đến 15%)
            r_salary_pct = random.choice([5, 8, 10, 12, 15])
            r_salary = r_salary_pct / 100
            # r_house: Phần trăm tăng giá nhà mỗi 2 năm (từ 3% đến 7%)
            r_house_pct = random.choice([3, 4, 5, 6, 7])
            r_house = r_house_pct / 100
            # p_spend: Phần trăm chi tiêu hàng tháng (từ 30% đến 50%)
            p_spend_pct = random.choice([30, 35, 40, 45, 50])
            p_save = (100 - p_spend_pct) / 100
            # T: Tổng số năm (mặc định 10 năm như đề bài)
            T = 10
            n_periods = T // 2 # Số chu kỳ tăng (5 chu kỳ)

            # --- TÍNH TOÁN ĐÁP ÁN ĐÚNG ---

            # 1. Giá trị ngôi nhà sau 10 năm: P = H0 * (1 + r_house)^5
            house_final = H0 * (1 + r_house)**n_periods

            # 2. Tổng số tiền tích lũy sau 10 năm:
            # Mỗi giai đoạn 2 năm (24 tháng). 
            # Tổng = 24 * p_save * a * [1 + (1+r_s) + (1+r_s)^2 + (1+r_s)^3 + (1+r_s)^4]
            # Sử dụng công thức cấp số nhân: S = (q^n - 1) / (q - 1)
            q = 1 + r_salary
            sum_geo = (q**n_periods - 1) / (q - 1)
            factor_a = 24 * p_save * sum_geo

            # 3. Tính a: a = house_final / factor_a
            a_exact = house_final / factor_a

            # Làm tròn đến hàng nghìn đồng
            def round_to_thousand(n):
                return int(Decimal(n).quantize(Decimal('1000'), rounding=ROUND_HALF_UP))

            res_a = round_to_thousand(a_exact)

            # Định dạng hiển thị số tiền có dấu chấm phân cách hàng nghìn
            def format_money(n):
                return "{:,}".format(n).replace(",", ".")

            da_dung = f"{format_money(res_a)}"

            # --- BƯỚC 4: TẠO PHƯƠNG ÁN SAI KHÔNG TRÙNG ĐÁP ÁN ĐÚNG ---

            s = set()
            while len(s) < 3:
                # Tạo các phương án sai bằng cách lệch từ 500k đến 3 triệu
                offset = random.choice([-2000000, -1500000, -1000000, -500000, 500000, 1000000, 1500000, 2000000])
                sai = round_to_thousand(a_exact + offset)
                if sai != res_a and sai > 0:
                    s.add(f"${format_money(sai)}$")

            list_sai = list(s)
            da_d = f"\\True ${da_dung}$"
            list_1 = [da_d] + list_sai
            random.shuffle(list_1)

            # --- BƯỚC 2: VIẾT LẠI NỘI DUNG THEO MẪU ---

            noidungcauhoi = (f"Một sinh viên ra trường đi làm ngày 1/1/2026 với mức lương khởi điểm là $a$ đồng mỗi tháng "
                             f"và cứ sau 2 năm lại được tăng thêm ${r_salary_pct}\\%$ và chi tiêu hàng tháng của anh ta là "
                             f"${p_spend_pct}\\%$ lương. Anh ta dự định mua một căn hộ chung cư giá rẻ có giá trị tại thời điểm 1/1/2020 "
                             f"là ${format_money(H0)}$ đồng và cũng sau 2 năm thì giá trị căn hộ tăng thêm ${r_house_pct}\\%$. "
                             f"Với $a$ bằng bao nhiêu thì sau đúng 10 năm anh ta mua được căn hộ đó, biết rằng mức lương và "
                             f"mức tăng giá trị ngôi nhà là không đổi (kết quả quy tròn đến hàng nghìn đồng).")

            loigiai = (f"Áp dụng công thức $P = P_0(1+r)^n$.\\\\ "
                       f"Giá trị ngôi nhà sau 10 năm (5 chu kỳ 2 năm) là: $P = {format_money(H0)} \\cdot (1 + {r_house})^{5} \\approx {format_money(int(house_final))}$ đồng.\\\\ "
                       f"Số tiền sinh viên còn lại mỗi tháng sau chi tiêu là ${100-p_spend_pct}\\%$ lương $= {p_save}a$.\\\\ "
                       f"Tổng số tiền tích lũy sau 10 năm là:\\\\ "
                       f"$24 \\cdot {p_save}a [1 + {q} + {q}^2 + {q}^3 + {q}^4] = 24 \\cdot {p_save}a \\cdot \\frac{{1 - {q}^5}}{{1 - {q}}} \\approx {factor_a:.4f} \\cdot a$.\\\\ "
                       f"Để mua được nhà: ${factor_a:.4f} \\cdot a = {format_money(int(house_final))} \\Rightarrow a \\approx {da_dung}$ đồng.")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

