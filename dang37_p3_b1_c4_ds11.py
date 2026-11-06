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


def bt_dang37_p3_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- CẤU HÌNH DỮ LIỆU ---
                # 1. Giữ nguyên độ cao h = 55.8m
                h_val = Rational(558, 10) # Dùng phân số để tính toán chính xác
                h_str = "55,8" # Chuỗi hiển thị cố định

                # 2. Random tỉ lệ nảy (Công bội q = 1/mau_so)
                # Chọn các mẫu số sao cho bài toán ra số tương đối đẹp
                list_mau_so = [2, 3, 4, 5, 8, 9, 20] 
                mau_so = random.choice(list_mau_so)
                cong_boi = Rational(1, mau_so)

                q_str = latex(cong_boi) # Hiển thị phân số (ví dụ: \frac{1}{5})

                # --- TÍNH TOÁN KẾT QUẢ ---
                # Tổng quãng đường S = h + 2*h*q + 2*h*q^2 + ...
                # S = h + [2hq / (1-q)]
                # Phần chuỗi phụ (tổng quãng đường nảy lên và rơi xuống sau lần 1)
                tu_so_u1 = 2 * h_val * cong_boi
                mau_so_cong_boi = 1 - cong_boi
                tong_chuoi_phu = tu_so_u1 / mau_so_cong_boi

                # Kết quả cuối cùng
                kq_val = h_val + tong_chuoi_phu

                # Xử lý hiển thị số liệu (Làm tròn 1 hoặc 2 chữ số thập phân nếu cần, thay chấm bằng phẩy)
                # Hàm convert float sang string chuẩn format đề bài
                def format_num(val):
                    return str(round(float(val), 2)).replace('.',',').rstrip('0').rstrip(',')

                tong_chuoi_phu_str = format_num(tong_chuoi_phu)
                kq_str = format_num(kq_val)

                # --- TẠO ĐÁP ÁN NHIỄU (Distractors) ---
                kq_float = float(kq_val)

                # Đáp án đúng
                da = '$%s$'%(kq_str)

                # Sai 1: Cộng nhầm giá trị xấp xỉ
                s1 = kq_float + random.randint(1, 5) + 0.5
                # Sai 2: Trừ nhầm
                s2 = kq_float - random.randint(1, 5) - 0.2
                # Sai 3: Sai công thức (Ví dụ quên nhân 2 cho quãng đường nảy)
                # S_sai = h / (1-q)
                s3 = float(h_val / (1 - cong_boi))

                list_s = [s1, s2, s3]
                ds_tex = []
                for x in list_s:
                     ds_tex.append('$%s$'%(format_num(x)))

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = ('''Từ độ cao $%s$m của tháp nghiêng Pisa nước Italia người ta thả một quả bóng cao su chạm xuống đất. Giả sử mỗi lần chạm đất quả bóng lại nảy lên độ cao bằng $%s$ độ cao mà quả bóng đạt trước đó. Tổng độ dài (đơn vị: m) hành trình của quả bóng được thả từ lúc ban đầu cho đến khi nó nằm yên trên mặt đất bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                  %(h_str, q_str))

                # --- NỘI DUNG LỜI GIẢI ---
                # Tạo chuỗi biểu thức d2, d3... dynamic theo mẫu số random
                d2_str = "%s + 2.\\frac{%s}{%s}" % (h_str, h_str, mau_so)
                d3_str = "%s + 2.\\frac{%s}{%s} + 2.\\frac{%s}{%s^2}" % (h_str, h_str, mau_so, h_str, mau_so)
                dn_str = "55,8 + 2.\\frac{55,8}{%s} + 2.\\frac{55,8}{%s^2} + ... + 2.\\frac{55,8}{%s^{n-1}}" % (mau_so, mau_so, mau_so)

                # Biểu thức tổng quát S
                sum_series_str = "2.\\frac{55,8}{%s} + 2.\\frac{55,8}{%s^2} + ... + 2.\\frac{55,8}{%s^{n-1}} + ..." % (mau_so, mau_so, mau_so)

                # Biểu thức u1
                u1_display = "2.\\frac{55,8}{%s}" % (mau_so)

                # Biểu thức tính tổng chuỗi phụ
                calc_sum_display = "\\frac{%s}{1 - \\frac{1}{%s}}" % (u1_display, mau_so)

                loigiai=('''Theo đề, mỗi lần chạm đất quả bóng lại nảy lên độ cao bằng $%s$ độ cao mà quả bóng đạt trước đó và sau đó lại rơi xuống từ độ cao thứ hai. Do đó độ dài hành trình của quả bóng được thả từ lúc ban đầu cho đến:\\\\
                Thời điểm chạm đất lần thứ nhất là $d_1 = 55,8$m.\\\\
                Thời điểm chạm đất lần thứ 2 là $d_2 = %s$.\\\\
                Thời điểm chạm đất lần thứ 3 là $d_3 = %s$.\\\\
                Thời điểm chạm đất lần thứ 4 là $d_4 = %s + 2.\\frac{55,8}{%s} + 2.\\frac{55,8}{%s^2} + 2.\\frac{55,8}{%s^3}$.\\\\
                ..........................................\\\\
                Thời điểm chạm đất lần thứ $n, (n>1)$ là $d_n = %s$.\\\\
                Do đó độ dài hành trình của quả bóng được thả từ lúc ban đầu cho đến khi nó nằm yên trên mặt đất là\\\\
                $d = 55,8 + %s$ (m).\\\\
                Vì $%s$ là một cấp số nhân lùi vô hạn, công bội $q = %s$. \\\\
                Nên ta có: $%s = %s = %s$.\\\\
                Vậy $d = 55,8 + %s = %s$m.'''
                         %(q_str, 
                           d2_str, 
                           d3_str, 
                           h_str, mau_so, mau_so, mau_so, # Cho d4
                           dn_str, 
                           sum_series_str, 
                           u1_display, # "Vì 2.55,8/mau..."
                           q_str,
                           sum_series_str, calc_sum_display, tong_chuoi_phu_str,
                           tong_chuoi_phu_str, kq_str
                          ))

                # --- XÁO TRỘN ĐÁP ÁN ---
                list_1 = ['\\True ' + da, ds_tex[0], ds_tex[1], ds_tex[2]]
                random.shuffle(list_1)

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_str))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

