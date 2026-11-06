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


def bt_dang9_p2_b2_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # --- BƯỚC 1: RANDOM CÁC THÔNG SỐ BÀI TOÁN ---
            # Thể tích ban đầu (m3)
            V0 = random.choice([4000, 5000, 6000]) 
            # Tốc độ bơm (m3/phút)
            v = random.choice([5, 10, 15, 20])
            # Nồng độ muối biển (g/lít)
            S_in = random.choice([25, 30, 35])

            # Các tính toán trung gian
            # Đổi m3 sang lít để tính toán nồng độ g/l
            V0_lit = V0 * 1000
            v_lit = v * 1000

            # Khối lượng muối sau t phút (gam): m(t) = S_in * v_lit * t
            mass_salt_g = S_in * v_lit * t
            mass_salt_kg = (S_in * v_lit / 1000) * t # Đổi sang kg

            # Thể tích nước sau t phút (m3)
            volume_m3 = V0 + v * t
            volume_lit = V0_lit + v_lit * t

            # Nồng độ C(t) = Khối lượng muối (g) / Thể tích (lít)
            # C(t) = (S_in * v * 1000 * t) / (V0 * 1000 + v * 1000 * t) = (S_in * v * t) / (V0 + v * t)
            Ct_expr = (S_in * v * t) / (V0 + v * t)
            limit_Ct = limit(Ct_expr, t, oo)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r'''Nhà anh Bình có một hồ hình chữ nhật rộng $10$ hecta và có độ sâu trung bình $1,5$ m. Trong hồ có chứa $%s$ $m^3$ nước ngọt. Để nuôi tôm, anh Bình bơm nước biển có nồng độ muối là $%s$ gam/lít vào hồ với tốc độ $%s$ $m^3$/phút. Theo nghiên cứu, độ mặn thích hợp cho tôm thẻ chân trắng nằm trong khoảng từ $2 - 40 \text{\textperthousand}$. Tôm sống và phát triển tốt nhất với chỉ số từ $10 - 25 \text{\textperthousand}$.''' 
                             % (latex(V0), latex(S_in), latex(v)))

            # --- NHẬN BIẾT: Khối lượng muối ---
            nb_da_1_d = r'\True Sau $t$ phút, lượng muối bơm vào hồ là $%s t$ (kg)' % (latex(int(S_in * v)))
            nb_da_1_s = r'Sau $t$ phút, lượng muối bơm vào hồ là $%s t$ (kg)' % (latex(int(S_in * v * 10)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = (r'''Lượng muối bơm vào sau $t$ phút là: $%s \text{ (g/l)} \cdot %s \cdot 1000 \text{ (l/phút)} \cdot t = %s t \text{ (g)} = %s t \text{ (kg)}$.''' 
                            % (latex(S_in), latex(v), latex(S_in * v * 1000), latex(S_in * v)))

            # --- THÔNG HIỂU: Thể tích nước ---
            th_da_1_d = r'\True Thể tích nước trong hồ sau $t$ phút là $V(t) = %s + %s t$ ($m^3$)' % (latex(V0), latex(v))
            th_da_1_s = r'Thể tích nước trong hồ sau $t$ phút là $V(t) = %s + %s t$ (lít)' % (latex(V0), latex(v))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = (r'''Thể tích ban đầu là $%s$ $m^3$, mỗi phút bơm thêm $%s$ $m^3$. Vậy sau $t$ phút thể tích là $V(t) = %s + %s t$ ($m^3$).''' 
                            % (latex(V0), latex(v), latex(V0), latex(v)))

            # --- VẬN DỤNG: Công thức nồng độ ---
            # Rút gọn phân số nồng độ
            tu = S_in * v
            mau_const = V0
            mau_t = v
            # C(t) = (tu * t) / (mau_const + mau_t * t)
            vd_da_1_d = r'\True Nồng độ muối của nước trong hồ sau $t$ phút là $C(t) = \frac{%s t}{%s + %s t}$ (g/l)' % (latex(tu), latex(mau_const), latex(mau_t))
            vd_da_1_s = r'Nồng độ muối của nước trong hồ sau $t$ phút là $C(t) = \frac{%s}{%s + t}$ (g/l)' % (latex(S_in), latex(V0 // v))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = (r'''Nồng độ muối $C(t) = \frac{\text{Khối lượng muối (g)}}{\text{Thể tích (l)}} = \frac{%s \cdot %s \cdot 1000 \cdot t}{%s \cdot 1000 + %s \cdot 1000 \cdot t} = \frac{%s t}{%s + %s t}$ (g/l).''' 
                            %(latex(S_in), latex(v), latex(V0), latex(v), latex(tu), latex(mau_const), latex(mau_t)))

            # --- VẬN DỤNG CAO: Giới hạn và kết luận ---
            vdc_da_1_d = r'\True Khi $t \to +\infty$, nồng độ muối tiến dần đến $%s$ g/l, hồ luôn thích hợp để nuôi tôm' % (latex(limit_Ct))
            vdc_da_1_s = r'Nồng độ muối trong hồ sẽ tăng vô hạn theo thời gian bơm'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = (r'''Ta có $\lim_{t \to +\infty} C(t) = \lim_{t \to +\infty} \frac{%s t}{%s + %s t} = %s$. 
                            Vì $%s$ g/l (tương đương $%s \text{\textperthousand}$) nằm trong khoảng $2 - 40 \text{\textperthousand}$ nên hồ luôn thích hợp để nuôi tôm.''' 
                             % (latex(tu), latex(mau_const), latex(mau_t), latex(limit_Ct), latex(limit_Ct), latex(limit_Ct)))

            # --- LOGIC XÁO TRỘN VÀ KIỂM TRA ĐÁP ÁN (GIỮ NGUYÊN THEO MẪU) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất kết quả theo định dạng LaTeX (minipage/ex)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + ans_nb + '}\n'
                '{' + ans_th + '}\n'
                '{' + ans_vd + '}\n'
                '{' + ans_vdc + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

