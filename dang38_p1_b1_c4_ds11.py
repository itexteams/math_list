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


def bt_dang38_p1_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: SUY NGHĨ TÌM CÁCH RANDOM ---
                # Cấu trúc: [sqrt(a_sq*n^2 + b) + c*n] / [d*n - sqrt(e_sq*n^2 + f)]

                # 1. Chọn hệ số trong căn sao cho khai căn ra số đẹp (số chính phương)
                # Ví dụ: a_sq là bình phương của k1
                k1 = randint(2, 9) # Hệ số của n^2 trong căn ở Tử (sau khi khai căn)
                a_sq = k1**2       # Hệ số thực tế trong căn (VD: 2^2 = 4)

                k2 = randint(2, 9) # Hệ số của n^2 trong căn ở Mẫu (sau khi khai căn)
                e_sq = k2**2       # Hệ số thực tế trong căn (VD: 1^2 = 1)

                # 2. Các hằng số tự do (không ảnh hưởng giới hạn, chọn ngẫu nhiên)
                b = randint(2, 9)  # Hằng số trong căn tử
                f = randint(2, 9)  # Hằng số trong căn mẫu

                # 3. Các hệ số bậc 1 bên ngoài căn
                c = randint(2, 9)  # Hệ số của n ở Tử

                # Chọn d sao cho mẫu số khác 0 (d - k2 != 0) và mẫu dương cho đẹp
                d = randint(k2 + 1, k2 + 6) # Hệ số của n ở Mẫu

                # 4. Tính toán kết quả giới hạn
                # Lim = (k1 + c) / (d - k2)
                tu_so_lim = k1 + c
                mau_so_lim = d - k2
                ket_qua = Rational(tu_so_lim, mau_so_lim)

                # --- XỬ LÝ HIỂN THỊ LATEX ---
                n = Symbol('n')

                # Tạo biểu thức hiển thị cho đề bài
                # Tử: sqrt(a_sq*n^2 + b) + cn
                # Mẫu: dn - sqrt(e_sq*n^2 + f)
                # Lưu ý: Dùng latex() của sympy để tự động xử lý số 1n hay 4n

                str_tu = latex(sqrt(a_sq*n**2 + b) + c*n)
                # Sympy thường đưa n ra trước căn, ta chỉnh chuỗi thủ công một chút nếu cần hiển thị y hệt mẫu
                # Nhưng latex(sqrt(...)) mặc định khá ổn. Để giống hệt mẫu "căn + n", ta dựng chuỗi thủ công cho đẹp:
                str_tu_de = f"\\sqrt{{{a_sq}n^2 + {b}}} + {c if c>1 else ''}n"
                str_mau_de = f"{d if d>1 else ''}n - \\sqrt{{{e_sq}n^2 + {f}}}"

                noidungcauhoi = f"Giới hạn $I = \\lim_{{n \\to +\\infty}} \\frac{{{str_tu_de}}}{{{str_mau_de}}}$ bằng"

                # --- TẠO ĐÁP ÁN TRẮC NGHIỆM ---
                da = f"${latex(ket_qua)}$" # Đáp án đúng

                # Tạo đáp án nhiễu bằng cách cộng trừ thêm giá trị vào kết quả đúng
                list_nhieu = []
                while len(list_nhieu) < 3:
                    delta = randint(-3, 3)
                    if delta == 0: continue
                    fake_val = ket_qua + delta
                    fake_str = f"${latex(fake_val)}$"
                    if fake_str not in list_nhieu and fake_str != da:
                        list_nhieu.append(fake_str)

                da_d = '\\True ' + da
                da_s1 = list_nhieu[0]
                da_s2 = list_nhieu[1]
                da_s3 = list_nhieu[2]

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- NỘI DUNG LỜI GIẢI (B2: Viết lại y hệt lời giải) ---
                # Dựng latex cho bước chia n
                # Tử: sqrt(a_sq + b/n^2) + c
                step1_tu = f"\\sqrt{{{a_sq} + \\frac{{{b}}}{{n^2}}}} + {c}"
                # Mẫu: d - sqrt(e_sq + f/n^2)
                step1_mau = f"{d} - \\sqrt{{{e_sq} + \\frac{{{f}}}{{n^2}}}}"

                # Dựng latex cho bước thay số
                # = (k1 + c) / (d - k2)
                step2_tu = f"\\sqrt{{{a_sq}}} + {c}"
                step2_mau = f"{d} - \\sqrt{{{e_sq}}}"

                loigiai = (
                    f"Ta có $I = \\lim_{{n \\to +\\infty}} \\frac{{{str_tu_de}}}{{{str_mau_de}}} "
                    f"= \\lim_{{n \\to +\\infty}} \\frac{{{step1_tu}}}{{{step1_mau}}} "
                    f"= \\frac{{{step2_tu}}}{{{step2_mau}}} "
                    f"= \\frac{{{tu_so_lim}}}{{{mau_so_lim}}} = {latex(ket_qua)}.$"
                )

                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                    '\n\\choice \n'
                    '{'+str(list_1[1])+'}\n'
                    '{'+str(list_1[2])+'}\n'
                    '{'+str(list_1[3])+'}\n'
                    '{'+str(list_1[0])+'}\n'
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n')
            return content

