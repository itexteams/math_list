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


def bt_dang35_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo các danh sách để chọn dạng
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1: KHỞI TẠO CÁC BIẾN RANDOM ---
                tong_hop = 48 # Tổng số hộp trong 1 thùng
                lay_ra = 10   # Số hộp lấy ra
                so_gia_can_tim = 2 # Số hộp giả cần có trong 10 hộp

                # Số hộp sữa giả trong loại I và loại II
                f1 = random.randint(5, 7) # Loại I có 5 đến 7 hộp giả
                f2 = random.randint(3, 4) # Loại II có 3 đến 4 hộp giả
                if f1 <= f2: f1 = f2 + 1

                # Tỷ lệ số thùng loại I gấp k lần loại II
                k_ti_le = random.choice([1.5, 2, 2.5, 3])

                # --- BƯỚC 2: TÍNH TOÁN XÁC SUẤT ---
                # 1. Xác suất chọn được thùng loại I và II
                # P(A) = k / (k + 1)
                pa_tu = sp.Rational(str(k_ti_le))
                pa_mau = pa_tu + 1
                prob_A = pa_tu / pa_mau
                prob_NotA = 1 - prob_A

                # 2. Xác suất lấy đúng 2 hộp giả trong từng loại thùng
                # P(B|A) = (C(f1, 2) * C(tong-f1, 10-2)) / C(tong, 10)
                def tinh_prob_cond(f_count, total, sample, target):
                    tu = sp.binomial(f_count, target) * sp.binomial(total - f_count, sample - target)
                    mau = sp.binomial(total, sample)
                    return tu, mau, sp.Rational(tu, mau)

                tu1, mau1, p_B_A = tinh_prob_cond(f1, tong_hop, lay_ra, so_gia_can_tim)
                tu2, mau2, p_B_NotA = tinh_prob_cond(f2, tong_hop, lay_ra, so_gia_can_tim)

                # 3. Xác suất toàn phần
                prob_B = prob_A * p_B_A + prob_NotA * p_B_NotA

                # Làm tròn kết quả đến hàng phần trăm
                kq_float = float(prob_B.evalf())
                kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # --- BƯỚC 3: TẠO CÁC ĐÁP ÁN SAI ---
                distractors = set()
                while len(distractors) < 3:
                    sai = kq_decimal + Decimal(str(random.choice([-0.05, -0.03, -0.02, 0.02, 0.03, 0.05])))
                    if sai > 0 and sai != kq_decimal:
                        distractors.add(str(sai).replace('.', ','))

                list_dist = list(distractors)

                # --- BƯỚC 4: NỘI DUNG CÂU HỎI VÀ LỜI GIẢI ---
                noidungcauhoi = ('''Một cơ sở sản xuất sữa giả mua các thùng sữa thật giống nhau ($%s$ hộp / thùng), rồi thay thế một số hộp sữa thật thành các hộp sữa giả nhằm thu lợi bất chính. Trong quá trình sản xuất, cơ sở phân ra làm hai loại: Loại I để lẫn mỗi thùng $%s$ hộp sữa giả và loại II để lẫn mỗi thùng $%s$ hộp sữa giả. Biết rằng số thùng sữa loại I gấp $%s$ lần số thùng sữa loại II. Chọn ngẫu nhiên một thùng sữa từ cơ sở sản xuất và từ thùng đó lấy ngẫu nhiên $%s$ hộp. Xác suất để trong $%s$ hộp lấy ra có đúng $%s$ hộp sữa giả bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'''
                                 %(latex(tong_hop), latex(f1), latex(f2), latex(k_ti_le).replace('.', ','), 
                                   latex(lay_ra), latex(lay_ra), latex(so_gia_can_tim)))

                # Chuẩn bị ký hiệu latex cho xác suất chọn thùng
                # Ví dụ: 1,5x / (1,5x + x) = 3/5
                pa_tu_latex = latex(pa_tu).replace('.', ',')
                pa_mau_latex = latex(pa_mau).replace('.', ',')

                loigiai = ('''Gọi biến cố $A$ là biến cố chọn được "Thùng sữa loại I".\\\\
                             Biến cố $\\overline{A}$ là biến cố chọn được "Thùng sữa loại II".\\\\
                             Nếu số thùng sữa loại II là $x$ thùng ($x \\in \\mathbb{N}$) thì số thùng sữa loại I là $%s x$ thùng.\\\\
                             Khi đó: $P(A) = \\frac{%s x}{%s x + x} = %s$; $P(\\overline{A}) = 1 - P(A) = %s$.\\\\
                             Gọi biến cố $B$ là biến cố chọn được "$%s$ hộp lấy ra có đúng $%s$ hộp sữa giả".\\\\
                             $P(B|A) = \\frac{C_{%s}^{%s} \\cdot C_{%s}^{%s}}{C_{%s}^{%s}}$; $P(B|\\overline{A}) = \\frac{C_{%s}^{%s} \\cdot C_{%s}^{%s}}{C_{%s}^{%s}}$.\\\\
                             Xác suất cần tìm là:\\\\
                             $P(B) = P(A) \\cdot P(B|A) + P(\\overline{A}) \\cdot P(B|\\overline{A}) = %s \\cdot \\frac{C_{%s}^{%s} \\cdot C_{%s}^{%s}}{C_{%s}^{%s}} + %s \\cdot \\frac{C_{%s}^{%s} \\cdot C_{%s}^{%s}}{C_{%s}^{%s}} \\approx %s$.'''
                           %(pa_tu_latex, pa_tu_latex, pa_tu_latex, latex(prob_A), latex(prob_NotA),
                             latex(lay_ra), latex(so_gia_can_tim),
                             latex(f1), latex(so_gia_can_tim), latex(tong_hop - f1), latex(lay_ra - so_gia_can_tim), latex(tong_hop), latex(lay_ra),
                             latex(f2), latex(so_gia_can_tim), latex(tong_hop - f2), latex(lay_ra - so_gia_can_tim), latex(tong_hop), latex(lay_ra),
                             latex(prob_A), latex(f1), latex(so_gia_can_tim), latex(tong_hop - f1), latex(lay_ra - so_gia_can_tim), latex(tong_hop), latex(lay_ra),
                             latex(prob_NotA), latex(f2), latex(so_gia_can_tim), latex(tong_hop - f2), latex(lay_ra - so_gia_can_tim), latex(tong_hop), latex(lay_ra),
                             kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

                # Đưa các đáp án vào danh sách
                da_d = '\\True $' + kq_str + '$'
                da_s1 = '$' + list_dist[0] + '$'
                da_s2 = '$' + list_dist[1] + '$'
                da_s3 = '$' + list_dist[2] + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

