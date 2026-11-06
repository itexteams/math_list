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


def bt_dang41_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy
            def format_decimal(value):
                return str(value).replace('.', ',')

            # --- Bước 3: Suy nghĩ tìm cách random bài toán ---
            # Random số lượng thùng hàng loại I và II (bội số của 10 để tính toán đẹp)
            N1 = random.randint(40, 60) * 10  # Ví dụ: 480
            N2 = random.randint(40, 60) * 10  # Ví dụ: 520
            tong_quat = N1 + N2

            # Random tỷ lệ kiểm định (số nguyên %)
            p1_pct = random.randint(75, 90)   # Ví dụ: 80%
            p2_pct = random.randint(75, 90)   # Ví dụ: 85%

            # Tính toán các giá trị trong bảng
            da_kd_I = int(N1 * p1_pct / 100)
            chua_kd_I = N1 - da_kd_I
            da_kd_II = int(N2 * p2_pct / 100)
            chua_kd_II = N2 - da_kd_II

            tong_da_kd = da_kd_I + da_kd_II
            tong_chua_kd = chua_kd_I + chua_kd_II

            # Các xác suất cơ bản (để tính toán)
            prob_A = N1 / tong_quat
            prob_B_bar = tong_chua_kd / tong_quat
            prob_notA_and_B = da_kd_II / tong_quat

            # Xác suất có điều kiện cho câu a
            p_A_given_Bbar = chua_kd_I / tong_chua_kd
            p_notA_given_Bbar = chua_kd_II / tong_chua_kd

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một kho hàng có $%s$ thùng hàng loại I và $%s$ thùng hàng loại II, tất cả với bề ngoài giống hệt nhau. Trong số các thùng hàng đó, có $%s\\%%$ thùng hàng loại I và $%s\\%%$ thùng hàng loại II đã được kiểm định. Chọn ngẫu nhiên một thùng hàng trong kho.''' 
                             % (N1, N2, p1_pct, p2_pct))

            # --- NHẬN BIẾT (Câu b trong ảnh - Xác suất loại I) ---
            val_b = format_decimal(round(prob_A * 100, 2))
            nb_da_1_d = '\\True Xác suất chọn được thùng hàng loại I bằng $%s\\%%$' % val_b
            nb_da_1_s = 'Xác suất chọn được thùng hàng loại I bằng $%s\\%%$' % format_decimal(round(prob_A * 100 + 5, 1))
            list_nb = [nb_da_1_d, nb_da_1_s]

            loigiai_nb = ('''Xác suất chọn được thùng hàng loại I là: $P(A) = \\frac{%s}{%s + %s} = %s\\%%$.''' 
                          % (N1, N1, N2, val_b))

            # --- THÔNG HIỂU (Câu c trong ảnh - Loại II và đã kiểm định) ---
            val_c = format_decimal(round(prob_notA_and_B * 100, 2))
            th_da_1_d = '\\True Xác suất chọn được thùng hàng loại II và đã được kiểm định bằng $%s\\%%$' % val_c
            th_da_1_s = 'Xác suất chọn được thùng hàng loại II và đã được kiểm định bằng $%s\\%%$' % format_decimal(round(prob_notA_and_B * 100 - 4, 1))
            list_th = [th_da_1_d, th_da_1_s]

            loigiai_th = ('''Xác suất chọn được thùng hàng loại II và đã được kiểm định là: $P(\\overline{A}B) = \\frac{n(\\overline{A}B)}{n(\\Omega)} = \\frac{%s}{%s} = %s\\%%$.''' 
                          % (da_kd_II, tong_quat, val_c))

            # --- VẬN DỤNG (Câu d trong ảnh - Chưa kiểm định) ---
            val_d = format_decimal(round(prob_B_bar * 100, 2))
            vd_da_1_d = '\\True Xác suất chọn được thùng hàng chưa kiểm định bằng $%s\\%%$' % val_d
            vd_da_1_s = 'Xác suất chọn được thùng hàng chưa kiểm định bằng $%s\\%%$' % format_decimal(round(prob_B_bar * 100 + 2.5, 1))
            list_vd = [vd_da_1_d, vd_da_1_s]

            loigiai_vd = ('''Xác suất chọn được thùng hàng chưa kiểm định là: \\\\
            Cách 1: $P(\\overline{B}) = \\frac{n(\\overline{B})}{n(\\Omega)} = \\frac{%s}{%s} = %s\\%%$. \\\\
            Cách 2: $P(\\overline{B}) = P(A).P(\\overline{B}|A) + P(\\overline{A}).P(\\overline{B}|\\overline{A}) = %s.%s + %s.%s = %s\\%%$.''' 
                          % (tong_chua_kd, tong_quat, val_d, 
                             format_decimal(round(prob_A, 2)), format_decimal(round(chua_kd_I/N1, 2)),
                             format_decimal(round(N2/tong_quat, 2)), format_decimal(round(chua_kd_II/N2, 2)),
                             val_d))

            # --- VẬN DỤNG CAO (Câu a trong ảnh - So sánh xác suất có điều kiện) ---
            so_sanh = "thấp hơn" if p_A_given_Bbar < p_notA_given_Bbar else "cao hơn"
            so_sanh_nguoc = "cao hơn" if p_A_given_Bbar < p_notA_given_Bbar else "thấp hơn"

            vdc_da_1_d = '\\True Giả sử thùng hàng được lấy ra là thùng hàng chưa được kiểm định, xác suất thùng hàng đó là thùng loại I %s xác suất thùng hàng đó là thùng loại II' % so_sanh
            vdc_da_1_s = 'Giả sử thùng hàng được lấy ra là thùng hàng chưa được kiểm định, xác suất thùng hàng đó là thùng loại I %s xác suất thùng hàng đó là thùng loại II' % so_sanh_nguoc
            list_vdc = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc = ('''Giả sử thùng hàng được lấy ra là thùng hàng chưa được kiểm định, xác suất thùng hàng đó là thùng loại I là: $P(A|\\overline{B}) = \\frac{n(A\\overline{B})}{n(\\overline{B})} = \\frac{%s}{%s} \\approx %s\\%%$. \\\\
            Giả sử thùng hàng được lấy ra là thùng hàng chưa được kiểm định, xác suất thùng hàng đó là thùng loại II là: $P(\\overline{A}|\\overline{B}) = \\frac{n(\\overline{A}\\overline{B})}{n(\\overline{B})} = \\frac{%s}{%s} \\approx %s\\%%$. \\\\
            Nhận xét: $P(A|\\overline{B}) %s P(\\overline{A}|\\overline{B})$.''' 
                           % (chua_kd_I, tong_chua_kd, format_decimal(round(p_A_given_Bbar*100, 1)),
                              chua_kd_II, tong_chua_kd, format_decimal(round(p_notA_given_Bbar*100, 1)),
                              ">" if p_A_given_Bbar > p_notA_given_Bbar else "<"))

            # --- Logic chọn đáp án đúng/sai ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                da_nb = random.choice(list_nb)
                da_th = random.choice(list_th)
                da_vd = random.choice(list_vd)
                da_vdc = random.choice(list_vdc)
                if 1 <= count_true_answers([da_nb, da_th, da_vd, da_vdc]) <= 3:
                    break

            # --- Xuất nội dung ---
            table_latex = ('''\\begin{center}
            \\begin{tabular}{|c|c|c|c|}
            \\hline
             & Loại I ($A$) & Loại II ($\\overline{A}$) & Tổng \\\\
            \\hline
            Đã kiểm định ($B$) & %s & %s & %s \\\\
            \\hline
            Chưa kiểm định ($\\overline{B}$) & %s & %s & %s \\\\
            \\hline
            Tổng & %s & %s & %s \\\\
            \\hline
            \\end{tabular}
            \\end{center}''' % (da_kd_I, da_kd_II, tong_da_kd, chua_kd_I, chua_kd_II, tong_chua_kd, N1, N2, tong_quat))

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(da_vdc) + '}\n'
                '{' + str(da_nb) + '}\n'
                '{' + str(da_th) + '}\n'
                '{' + str(da_vd) + '}\n'
                '\\loigiai{ \n'
                'Gọi biến cố $A$: "Thùng hàng chọn được là loại I". Suy ra $\\overline{A}$: "Thùng hàng chọn được là loại II".\\\\ \n'
                'Biến cố $B$: "Thùng hàng chọn đã được kiểm định". Suy ra $\\overline{B}$: "Thùng hàng chọn chưa được kiểm định".\\\\ \n'
                'Ta có bảng sau: \n' + table_latex + '\n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_vdc) + '\n'
                '\\item ' + str(loigiai_nb) + '\n'
                '\\item ' + str(loigiai_th) + '\n'
                '\\item ' + str(loigiai_vd) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

