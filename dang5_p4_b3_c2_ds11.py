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


def bt_dang5_p4_b3_c2_ds11(self):
            # Khai báo biến
            # --- HÀM HỖ TRỢ ĐỊNH DẠNG SỐ MŨ ĐÃ CHỈNH SỬA ---
            def format_exponent(s):
                """Thay thế ký hiệu khoa học 'e' bằng định dạng LaTeX và loại bỏ số 0 đứng đầu trong số mũ (ví dụ: e+07 -> \\cdot 10^{7})."""
                # Bước 1: Thay thế 'e+' và 'e-' bằng định dạng LaTeX
                s = s.replace('e+', '\\cdot 10^{').replace('e-', '\\cdot 10^{-')

                # Bước 2: Thêm '}' để đóng số mũ
                s_closed = s + '}'

                # Bước 3: Tìm và loại bỏ số '0' đứng đầu trong số mũ
                # Tìm vị trí của dấu '{' đầu tiên
                start_brace = s_closed.find('{')
                if start_brace != -1:
                    # Lấy phần số mũ bên trong ngoặc
                    exponent_part = s_closed[start_brace + 1 : -1]

                    # Kiểm tra nếu số mũ bắt đầu bằng '0' và có độ dài > 1 (ví dụ: '07')
                    if len(exponent_part) > 1 and exponent_part.startswith('0'):
                        # Loại bỏ số '0' đứng đầu
                        new_exponent_part = exponent_part.lstrip('0')
                        # Lắp lại chuỗi LaTeX
                        s_closed = s_closed[:start_brace + 1] + new_exponent_part + '}'

                return s_closed

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Thời gian phân bào (phút)
                tg_phan_bao_phut = random.choice([15, 20, 25, 30])
                # 2. Thời gian cần tính (giờ)
                tg_hoi_gio = random.choice([6, 8, 10, 12, 16])
                # 3. Số vi khuẩn ban đầu
                so_vk_ban_dau = random.choice([1, 2, 4, 5])

                # --- TÍNH TOÁN KẾT QUẢ CHÍNH XÁC ---
                tg_hoi_phut = tg_hoi_gio * 60
                so_lan_phan_bao = tg_hoi_phut / tg_phan_bao_phut

                # Kiểm tra đảm bảo số lần phân bào là số nguyên để tránh số mũ không nguyên
                if so_lan_phan_bao != int(so_lan_phan_bao):
                    # Nếu không nguyên, thay đổi tg_hoi_gio để đảm bảo chia hết
                    # Tìm các giá trị tg_hoi_gio * 60 chia hết cho tg_phan_bao_phut
                    possible_tg = [t for t in [6, 8, 10, 12, 16, 20, 24] if (t * 60) % tg_phan_bao_phut == 0]
                    if not possible_tg:
                         # Nếu không tìm thấy, chọn một giá trị lớn hơn có thể chia hết
                         tg_hoi_gio = (tg_phan_bao_phut * random.choice([1, 2, 3])) // 60
                         if tg_hoi_gio < 1: tg_hoi_gio = 1
                    else:
                         tg_hoi_gio = random.choice(possible_tg)

                    tg_hoi_phut = tg_hoi_gio * 60
                    so_lan_phan_bao = tg_hoi_phut / tg_phan_bao_phut

                so_lan_phan_bao = int(so_lan_phan_bao) # Đảm bảo là số nguyên
                kq_exact = so_vk_ban_dau * (2**so_lan_phan_bao)

                # Giới hạn số vi khuẩn ở 2 chữ số có nghĩa cho việc làm tròn và tạo đáp án sai
                if kq_exact >= 1e6:
                    # Làm tròn kết quả về 2 chữ số có nghĩa (Decimal('1e' + str(len(str(int(kq_exact))) - 2)))
                    precision = len(str(int(kq_exact))) - 2
                    if precision < 0: precision = 0
                    kq_tron = float(Decimal(kq_exact).quantize(Decimal('1e' + str(precision)), rounding=ROUND_HALF_UP))
                else:
                    kq_tron = kq_exact # Giữ nguyên nếu số nhỏ

                # Định dạng kết quả đúng cho LaTeX, làm tròn về 2 chữ số có nghĩa
                kq_str_latex = format_exponent("{:.2e}".format(kq_tron))
                da = '$%s$'%(kq_str_latex)

                # --- TẠO CÁC ĐÁP ÁN SAI (Dựa trên kết quả làm tròn) ---
                s = []
                # Các đáp án sai được tạo bằng cách nhân với các hệ số gần 1
                he_so_sai = [0.8, 0.9, 1.1, 1.2, 1.5, 2.0, 0.75, 1.25]
                random.shuffle(he_so_sai)

                for hs in he_so_sai:
                    sai_tron = kq_tron * hs
                    # Tránh trùng với đáp án đúng (sai khác tối thiểu 10%) và tránh trùng với đáp án sai đã có
                    if abs(sai_tron - kq_tron) / kq_tron > 0.1:
                        sai_str_latex = format_exponent("{:.2e}".format(sai_tron))
                        if sai_str_latex not in s:
                            s.append('$%s$'%(sai_str_latex))
                            if len(s) >= 3:
                                break

                # Nếu không đủ 3 đáp án sai, thêm một đáp án sai cơ bản (ví dụ: sai mũ)
                while len(s) < 3:
                    sai_tron = kq_tron / 2
                    sai_str_latex = format_exponent("{:.2e}".format(sai_tron))
                    if sai_str_latex not in s:
                         s.append('$%s$'%(sai_str_latex))
                    elif len(s) < 3: # Nếu vẫn trùng, thay đổi một chút
                         sai_tron = kq_tron / 4
                         sai_str_latex = format_exponent("{:.2e}".format(sai_tron))
                         if sai_str_latex not in s:
                            s.append('$%s$'%(sai_str_latex))
                    if len(s) < 3:
                         # Thêm một lỗi tính toán khác (ví dụ: quên nhân số vi khuẩn ban đầu)
                         sai_tron = (2**(so_lan_phan_bao - 1)) if so_lan_phan_bao > 0 else 1
                         sai_str_latex = format_exponent("{:.2e}".format(sai_tron))
                         if sai_str_latex not in s:
                             s.append('$%s$'%(sai_str_latex))

                # Chọn 3 đáp án sai đầu tiên
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
                noidungcauhoi = ('''Một loại vi khuẩn sinh sản thông qua quá trình phân đôi. Vi khuẩn phân chia làm đôi cứ sau $%s$ phút. Giả sử ban đầu có $%s$ vi khuẩn xâm nhập vào cơ thể. Tính số vi khuẩn có trong cơ thể sau $%s$ giờ. (Giả sử nguồn dinh dưỡng vô hạn và tốc độ phân bào được duy trì).'''
                                 %(latex(tg_phan_bao_phut), latex(so_vk_ban_dau), latex(tg_hoi_gio)
                                 ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai=('''Tổng thời gian là $%s$ giờ, tương đương $%s \\cdot 60 = %s$ phút. \\\\
                Thời gian phân bào là $%s$ phút/lần. \\\\
                Số lần phân bào trong $%s$ giờ là:
                $\\qquad N = \\frac{%s}{%s} = %s$ (lần). \\\\
                Số lượng vi khuẩn ban đầu là $%s$. \\\\
                Số lượng vi khuẩn sau $%s$ giờ là:
                $\\qquad S = \\text{Số ban đầu} \\cdot 2^N = %s \\cdot 2^{%s} = %s$ (con). \\\\
                Làm tròn ta được kết quả: $%s$ (con).'''
                         %(latex(tg_hoi_gio), latex(tg_hoi_gio), latex(tg_hoi_phut),
                           latex(tg_phan_bao_phut),
                           latex(tg_hoi_gio), latex(tg_hoi_phut), latex(tg_phan_bao_phut), latex(so_lan_phan_bao),
                           latex(so_vk_ban_dau),
                           latex(tg_hoi_gio), latex(so_vk_ban_dau), latex(so_lan_phan_bao), kq_exact,
                           da.replace('$', '')
                         ))


                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n'+ str(noidungcauhoi)+
                           '\\loigiai{'+str(loigiai)+'}\n'
                           '\\end{ex}\n \\end{minipage} \n\n')
            return content 

