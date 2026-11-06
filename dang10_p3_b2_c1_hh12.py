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


def bt_dang10_p3_b2_c1_hh12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # 1. Random các hướng và khoảng cách
        # Ox hướng Nam (+), Bắc (-)
        dir_x_list = [("phía nam", 1), ("phía bắc", -1)]
        # Oy hướng Đông (+), Tây (-)
        dir_y_list = [("phía đông", 1), ("phía tây", -1)]

        dx_str, dx_sign = random.choice(dir_x_list)
        dy_str, dy_sign = random.choice(dir_y_list)

        # Khoảng cách x, y
        v_x = random.randint(1, 5)
        v_y = random.randint(1, 5)

        # Để số liệu thực tế, random chiều cao c có thể là số thập phân
        v_z = random.choice([0.5, 1, 1.5, 2, 2.5, 3])

        # 2. Xác định tọa độ a, b, c
        a = v_x * dx_sign
        b = v_y * dy_sign
        c = v_z

        # 3. Random hệ số m, n, p cho biểu thức T = m*a + n*b + p*c
        m = random.randint(-3, 3)
        while m == 0: m = random.randint(-3, 3)

        n = random.randint(-3, 3)
        while n == 0: n = random.randint(-3, 3)

        # Nếu c là số thập phân (có đuôi .5), đảm bảo p là số chẵn để kết quả T là số nguyên
        if isinstance(c, float) and c % 1 != 0:
            p = random.choice([-4, -2, 2, 4])
        else:
            p = random.randint(-3, 3)
            while p == 0: p = random.randint(-3, 3)

        kq = m*a + n*b + p*c
        if kq == int(kq):
            kq = int(kq) # Loại bỏ đuôi .0 nếu có

        # --- CÁC HÀM XỬ LÝ CHUỖI ĐỂ TRÁNH DẤU + - LỘN XỘN ---
        def fmt_term(coeff, var, is_first=False):
            if coeff == 0: return ""
            abs_c = abs(coeff)
            c_str = "" if abs_c == 1 else str(abs_c)
            if is_first:
                return f"-{c_str}{var}" if coeff < 0 else f"{c_str}{var}"
            else:
                return f" - {c_str}{var}" if coeff < 0 else f" + {c_str}{var}"

        # Tạo chuỗi biểu thức (ví dụ: a - 2b + 4c)
        expr_str = fmt_term(m, 'a', True) + fmt_term(n, 'b', False) + fmt_term(p, 'c', False)

        def fmt_sub(coeff, val):
            # Format giá trị (đổi dấu chấm thành phẩy cho số thập phân, đóng ngoặc nếu âm)
            val_str = str(val).replace('.', ',')
            if val < 0: val_str = f"({val_str})"

            if coeff == 1: return val_str
            if coeff == -1: return f"-{val_str}"
            return f"{coeff}\\cdot {val_str}"

        # Tạo chuỗi phép thế
        sub_str = f"{fmt_sub(m, a)} + {fmt_sub(n, b)} + {fmt_sub(p, c)}"
        # Dọn dẹp dấu triệt để
        sub_str = sub_str.replace("+ -", "- ").replace("- -", "+ ").replace("+ (-", "- (").replace("- (-", "+ (")

        # Format lại số thập phân sang dấu phẩy cho tiếng Việt
        z_str_comma = str(v_z).replace('.', ',')
        c_str_comma = str(c).replace('.', ',')

        # 4. Tạo nội dung đề bài và lời giải
        noidungcauhoi = (f"Một chiếc khinh khí cầu bay lên từ điểm xuất phát ${v_x}$ km về {dx_str} và ${v_y}$ km về {dy_str}, "
                         f"đồng thời cách mặt đất ${z_str_comma}$ km. Chọn hệ trục $Oxyz$ với gốc $O$ đặt tại điểm xuất phát của hai khinh khí cầu, "
                         f"mặt phẳng $(Oxy)$ trùng với mặt đất với tia $Ox$ hướng về phía nam, tia $Oy$ hướng về phía đông và tia $Oz$ hướng thẳng đứng lên trời "
                         f"(đơn vị đo lấy theo kilomet).\\\\\n"
                         f"Với hệ tọa độ đã chọn, tọa độ khinh khí cầu đã cho là $(a;b;c)$, giá trị $T = {expr_str}$ bằng bao nhiêu?")

        loigiai = (f"Theo giả thiết, hệ trục $Oxyz$ có:\\\\\n"
                   f"$-$ Tia $Ox$ hướng về phía nam. Khinh khí cầu cách gốc $O$ một khoảng ${v_x}$ km về {dx_str} nên hoành độ $a = {a}$. \\\\\n"
                   f"$-$ Tia $Oy$ hướng về phía đông. Khinh khí cầu cách gốc $O$ một khoảng ${v_y}$ km về {dy_str} nên tung độ $b = {b}$. \\\\\n"
                   f"$-$ Tia $Oz$ hướng thẳng đứng lên trời. Khinh khí cầu cách mặt đất ${z_str_comma}$ km nên cao độ $c = {c_str_comma}$. \\\\\n"
                   f"Suy ra tọa độ của khinh khí cầu là $(a;b;c) = ({a}; {b}; {c_str_comma})$. \\\\\n"
                   f"Thay vào biểu thức ta có: $T = {sub_str} = {kq}$.")

        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
    return content

