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


def bt_dang30_p3_b1_c4_ds11(self):
            # Khai báo biến
            # Điều kiện: a = k^3 để tạo dạng vô định khử được

            k = randint(2, 9)          # Hệ số của n bên ngoài (ví dụ: 1, 2, 3)
            a = k**3                   # Hệ số n^3 trong căn (ví dụ: k=2 -> a=8)
            b = randint(2, 9)          # Hệ số n^2 trong căn
            c = randint(2, 9)          # Hằng số trong căn
            d = randint(2, 10)         # Hằng số tự do bên ngoài

            # Tính toán kết quả chính xác (dùng Rational để giữ dạng phân số)
            # Giới hạn của phần căn - kn là: b / (3 * k^2)
            phan_so_gioi_han = Rational(b, 3 * k**2)
            ket_qua = d + phan_so_gioi_han
            h1=round(ket_qua,9)
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kq1=str(kqz).replace('.', ',')

            # --- TẠO CÁC ĐÁP ÁN NHIỄU (DISTRACTORS) ---
            # Phương án sai 1: Quên nhân 3 ở mẫu số công thức liên hợp
            sai_1 = d + Rational(b, k**2)
            # Phương án sai 2: Sai dấu hằng số d
            sai_2 = d - phan_so_gioi_han
            # Phương án sai 3: Quên cộng hằng số d
            sai_3 = phan_so_gioi_han

            # Gom đáp án vào list
            list_dap_an = [ket_qua, sai_1, sai_2, sai_3]
            # Đảm bảo các đáp án không trùng nhau (nếu trùng thì cộng thêm chút xíu)
            list_dap_an = sorted(list(set(list_dap_an)), key=list_dap_an.index)
            while len(list_dap_an) < 4:
                list_dap_an.append(list_dap_an[-1] + 1)

            # Format đáp án sang Latex
            str_da_dung = '$' + latex(ket_qua) + '$'
            str_sai_1 = '$' + latex(list_dap_an[1]) + '$'
            str_sai_2 = '$' + latex(list_dap_an[2]) + '$'
            str_sai_3 = '$' + latex(list_dap_an[3]) + '$'

            list_output = [str_da_dung, str_sai_1, str_sai_2, str_sai_3]
            random.shuffle(list_output) # Trộn ngẫu nhiên vị trí

            # --- XÂY DỰNG NỘI DUNG CÂU HỎI VÀ LỜI GIẢI (LATEX) ---

            # 1. Câu hỏi
            # Tạo chuỗi biểu thức đề bài: cbrt(an^3 + bn^2 + c) - kn + d
            bieu_thuc_de = f"\\sqrt[3]{{{a}n^3 + {b}n^2 + {c}}} - {k}n + {d}"
            noidungcauhoi = f"Giới hạn $L = \\lim_{{n \\to +\\infty}} \\left( {bieu_thuc_de} \\right)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)."

            # 2. Lời giải chi tiết
            # Bước 1: Tách d
            step1_inner = f"\\sqrt[3]{{{a}n^3 + {b}n^2 + {c}}} - {k}n"
            step1 = f"L = \\lim_{{n \\to +\\infty}} \\left( {bieu_thuc_de} \\right) = {d} + \\lim_{{n \\to +\\infty}} \\left( {step1_inner} \\right)"

            # Bước 2: Nhân liên hợp
            tu_so_lh = f"{b}n^2 + {c}" # (an^3 + bn^2 + c) - (kn)^3 = bn^2 + c
            mau_so_lh = f"\\sqrt[3]{{({a}n^3 + {b}n^2 + {c})^2}} + {k}n.\\sqrt[3]{{{a}n^3 + {b}n^2 + {c}}} + {k**2}n^2"
            step2 = f"= {d} + \\lim_{{n \\to +\\infty}} \\frac{{{tu_so_lh}}}{{{mau_so_lh}}}"

            # Bước 3: Chia n^2 (Rút gọn)
            tu_so_rut_gon = f"{b} + \\frac{{{c}}}{{n^2}}"
            # Xử lý hiển thị mẫu số rút gọn cho đẹp
            can_rut_gon = f"\\sqrt[3]{{{a} + \\frac{{{b}}}{{n}} + \\frac{{{c}}}{{n^3}}}}"
            mau_so_rut_gon = f"\\sqrt[3]{{({a} + \\frac{{{b}}}{{n}} + \\frac{{{c}}}{{n^3}})^2}} + {k}.{can_rut_gon} + {k**2}"
            step3 = f"= {d} + \\lim_{{n \\to +\\infty}} \\frac{{{tu_so_rut_gon}}}{{{mau_so_rut_gon}}}"

            # Bước 4: Thay số
            so_hang_mau = k**2 # Giá trị của từng số hạng ở mẫu: k^2
            mau_so_so = f"{so_hang_mau} + {k}.\\sqrt[3]{{{a}}} + {k**2}" # Hiển thị 4 + 2.cbrt(8) + 4
            mau_so_tong = 3 * k**2
            step4 = f"= {d} + \\frac{{{b}}}{{{mau_so_tong}}} = {d} + {latex(phan_so_gioi_han)} = {latex(ket_qua)} \\approx {str(kq1)}."

            # Ghép lời giải hoàn chỉnh
            loigiai = f"""Ta có:
            \\\\ ${step1}$
            \\\\ ${step2}$
            \\\\ ${step3}$
            \\\\ ${step4}$"""

            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(str(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

