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


def bt_dang26_p4_b3_c5_ds11(self):
            # Khai báo biến
            # Khai báo biến danh sách dạng (ở đây có 1 dạng bài lãi kép)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- BƯỚC 1 & 3: NGHIÊN CỨU ĐỀ BÀI VÀ RANDOM DỮ LIỆU ---
                # Số tiền gốc ban đầu (triệu đồng)
                M_val = random.randint(30, 100) 
                M = M_val * 10**6

                # Kỳ hạn (tháng)
                ky_han = 3 
                so_ky_han_trong_nam = 12 // ky_han # Thường là 4 kỳ/năm

                # Đợt 1
                r1_annual = random.choice([7.2, 7.6, 8.0, 8.4, 8.8]) # Lãi suất năm %
                r1_term = r1_annual / so_ky_han_trong_nam # Lãi suất mỗi kỳ hạn %
                n1 = random.randint(2, 4) # Số kỳ hạn gửi đợt 1

                # Đợt 2
                r2_annual = random.choice([10.0, 10.4, 11.2, 12.0, 12.8]) # Lãi suất năm % đợt sau
                r2_term = r2_annual / so_ky_han_trong_nam # Lãi suất mỗi kỳ hạn %
                t2_months = 12 # Gửi thêm 12 tháng
                n2 = t2_months // ky_han # Số kỳ hạn đợt 2

                # --- BƯỚC 2: TÍNH TOÁN KẾT QUẢ CHÍNH XÁC ---
                # Tính số tiền sau đợt 1
                P3_val = M * (1 + r1_term/100)**n1

                # Tính số tiền cuối cùng sau đợt 2
                P_final = P3_val * (1 + r2_term/100)**n2

                # Làm tròn đến hàng đơn vị
                kq_num = int(Decimal(P_final).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                kq = "{:,}".format(kq_num).replace(',', '.') # Định dạng phân cách nghìn kiểu VN

                # --- BƯỚC 4: TẠO CÁC PHƯƠNG ÁN SAI (KHÔNG TRÙNG ĐÁP ÁN ĐÚNG) ---
                du = [f"{kq} đồng"]
                da = du[0]

                s = []
                while len(s) < 3:
                    # Tạo sai số bằng cách cộng/trừ một lượng tiền ngẫu nhiên hoặc tính sai công thức
                    sai_so = random.choice([100000, 200000, -100000, 50000, -50000, 150000])
                    fake_val = kq_num + sai_so
                    fake_str = "{:,} đồng".format(fake_val).replace(',', '.')
                    if fake_str not in s and fake_str != da:
                        s.append(fake_str)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # --- NỘI DUNG CÂU HỎI ---
                noidungcauhoi = (f"Ông An gửi tiết kiệm {M_val} triệu đồng vào ngân hàng với kỳ hạn {ky_han} tháng, "
                                 f"lãi suất {r1_annual}ptr một năm theo hình thức lãi kép. Ông gửi được đúng {n1} kỳ hạn "
                                 f"thì ngân hàng thay đổi lãi suất, ông gửi tiếp {t2_months} tháng nữa với kỳ hạn như cũ "
                                 f"và lãi suất trong thời gian này là {r2_annual}ptr một năm thì ông rút tiền về. "
                                 f"Số tiền ông An nhận được cả gốc lẫn lãi là: (làm tròn đến chữ số hàng đơn vị)")

                # --- NỘI DUNG LỜI GIẢI ---
                loigiai = (f"Đợt I, ông An gửi số tiền $P_0 = {M_val}$ triệu, lãi suất {r1_annual}ptr một năm tức là "
                           f"{r1_term}ptr mỗi kỳ hạn. Số tiền cả gốc và lãi ông thu được sau {n1} kỳ hạn là: "
                           f"$P_{n1} = {M} \\cdot (1 + {r1_term/100})^{n1}$. \\\\\n"
                           f"Đợt II, do ông không rút ra nên số tiền $P_{n1}$ được xem là số tiền gửi ban đầu của đợt II, "
                           f"lãi suất đợt II là {r2_term}ptr mỗi kỳ hạn. Ông gửi tiếp {t2_months} tháng bằng {n2} kỳ hạn "
                           f"nên số tiền thu được cuối cùng là: \\\\\n"
                           f"$P = P_{n1} \\cdot (1 + {r2_term/100})^{n2} = {M} \\cdot (1.0{int(r1_term*10) if r1_term*10 == int(r1_term*10) else r1_term})^{n1} "
                           f"\\cdot (1.0{int(r2_term)})^ {n2} \\approx {kq}$ đồng.")

                # Đưa các đáp án vào danh sách chọn ngẫu nhiên
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('ptr', '\\%')
            return content

