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


def bt_dang64_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai vectơ u và v[cite: 23]
    # u = (u1; u2; u3), v = (v1; 0; m)[cite: 23]
    # |u| = sqrt(u1^2 + u2^2 + u3^2)[cite: 23]
    # |v| = sqrt(v1^2 + m^2) >= |v1|[cite: 23]
    # u . v = u1*v1 + u3*m[cite: 23]
    # (u, v) = 45 độ <=> cos(u, v) = sqrt(2)/2 <=> u . v / (|u| * |v|) = sqrt(2)/2[cite: 23]
    # <=> 2 * (u1*v1 + u3*m)^2 = |u|^2 * (v1^2 + m^2) với u . v > 0[cite: 23]
    while True:
        u1 = random.choice([1, 2])
        u2 = random.choice([1, 2])
        u3 = random.choice([-3, -2, -1, 2, 3])
    
        v1 = random.choice([1, 2])
    
        len_u_sq = u1**2 + u2**2 + u3**2
    
        # Phương trình tìm m khi góc = 45 độ[cite: 23]:
        # 2*(u1*v1 + u3*m)^2 = len_u_sq * (v1^2 + m^2)
        # 2*(u3^2 * m^2 + 2*u1*v1*u3*m + (u1*v1)^2) = len_u_sq * m^2 + len_u_sq * v1^2
        # (2*u3^2 - len_u_sq)*m^2 + (4*u1*v1*u3)*m + (2*(u1*v1)^2 - len_u_sq * v1^2) = 0
        A_m = 2 * (u3**2) - len_u_sq
        B_m = 4 * u1 * v1 * u3
        C_m = 2 * ((u1 * v1) ** 2) - len_u_sq * (v1**2)
    
        delta_m = B_m**2 - 4 * A_m * C_m
        if delta_m > 0 and A_m != 0:
            # Kiểm tra điều kiện có nghiệm m sao cho u.v = u1*v1 + u3*m > 0
            sqrt_d = math.sqrt(delta_m)
            m_sol1 = (-B_m + sqrt_d) / (2 * A_m)
            m_sol2 = (-B_m - sqrt_d) / (2 * A_m)
    
            valid_m = []
            for m_val in [m_sol1, m_sol2]:
                if u1 * v1 + u3 * m_val > 0:
                    valid_m.append(m_val)
    
            if len(valid_m) > 0:
                m_target = valid_m[0]
                # Chọn ngưỡng so sánh cho m ở mệnh đề d[cite: 23]
                # Ví dụ so sánh m với một phân số k_num / k_den
                bound_val_float = math.floor(m_target * 10) / 10.0
                break
    
    # 1. Khẳng định a: |u| = sqrt(len_u_sq)[cite: 23]
    str_len_u_true = latex(sp.sqrt(len_u_sq))
    str_len_u_false = latex(sp.sqrt(len_u_sq + random.choice([-2, -1, 1, 2])))
    if str_len_u_false == str_len_u_true:
        str_len_u_false = "\\sqrt{5}"
    
    # 2. Khẳng định b: |v| >= |v1|[cite: 23]
    bound_v = abs(v1)
    bound_v_false = bound_v + 1
    
    # 3. Khẳng định c: (u, v) = 45 độ <=> cos(u, v) = sqrt(2)/2 (luôn đúng theo định nghĩa)[cite: 23]
    
    # 4. Khẳng định d: Khi góc giữa u, v bằng 45 độ thì m < bound hoặc m > bound[cite: 23]
    # Tạo phân số so sánh dạng latex[cite: 23]
    bound_rat = Rational(int(round(bound_val_float * 10)), 10)
    str_bound_m = format_fraction_latex(bound_rat.p, bound_rat.q)
    is_m_lt_bound = m_target < float(bound_rat)
    
    # Nội dung câu hỏi[cite: 23]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho véctơ $\\vec{u} = (%s;%s;%s), \\vec{v} = (%s;0;m)$."""
        % (u1, u2, u3, v1)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: |u| = ...[cite: 23]
    nb_da_1_d = "\\True $|\\vec{u}| = %s$" % (str_len_u_true)
    nb_da_1_s = "$|\\vec{u}| = %s$" % (str_len_u_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Độ dài của vectơ $\\vec{u}$ được tính theo công thức: \\\\ $|\\vec{u}| = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
            u1,
            u2,
            u3,
            len_u_sq,
            str_len_u_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: |v| >= bound_v[cite: 23]
    th_da_1_d = "\\True $|\\vec{v}| \\ge %s$" % (bound_v)
    th_da_1_s = "$|\\vec{v}| \\ge %s$" % (bound_v_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Độ dài của vectơ $\\vec{v}$ là: \\\\ $|\\vec{v}| = \\sqrt{(%s)^2 + 0^2 + m^2} = \\sqrt{%s + m^2}$. \\\\ Vì $m^2 \\ge 0$ với mọi số thực $m$ nên: \\\\ $|\\vec{v}| = \\sqrt{%s + m^2} \\ge \\sqrt{%s} = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            v1,
            v1**2,
            v1**2,
            v1**2,
            bound_v,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: (u, v) = 45 độ <=> cos(u, v) = sqrt(2)/2[cite: 23]
    vd_da_1_d = (
        "\\True $(\\vec{u}, \\vec{v}) = 45^\\circ \\Leftrightarrow \\cos(\\vec{u}, \\vec{v}) = \\frac{\\sqrt{2}}{2}$"
    )
    vd_da_1_s = (
        "$(\\vec{u}, \\vec{v}) = 45^\\circ \\Leftrightarrow \\cos(\\vec{u}, \\vec{v}) = \\frac{1}{2}$"
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Góc giữa hai vectơ $\\vec{u}$ và $\\vec{v}$ thỏa mãn $0^\\circ \\le (\\vec{u}, \\vec{v}) \\le 180^\\circ$. \\\\ Do đó: \\\\ $(\\vec{u}, \\vec{v}) = 45^\\circ \\Leftrightarrow \\cos(\\vec{u}, \\vec{v}) = \\cos 45^\\circ = \\frac{\\sqrt{2}}{2}$. \\\\ Mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Khi góc giữa u, v bằng 45 độ thì m < str_bound_m[cite: 23]
    if is_m_lt_bound:
        vdc_da_1_d = (
            "\\True Khi góc giữa $\\vec{u}, \\vec{v}$ bằng $45^\\circ$ thì $m < %s$"
            % (str_bound_m)
        )
        vdc_da_1_s = (
            "Khi góc giữa $\\vec{u}, \\vec{v}$ bằng $45^\\circ$ thì $m > %s$"
            % (str_bound_m)
        )
    else:
        vdc_da_1_d = (
            "\\True Khi góc giữa $\\vec{u}, \\vec{v}$ bằng $45^\\circ$ thì $m > %s$"
            % (str_bound_m)
        )
        vdc_da_1_s = (
            "Khi góc giữa $\\vec{u}, \\vec{v}$ bằng $45^\\circ$ thì $m < %s$"
            % (str_bound_m)
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta có tích vô hướng của hai vectơ $\\vec{u}$ và $\\vec{v}$ là: \\\\ $\\vec{u} \\cdot \\vec{v} = (%s) \\cdot (%s) + (%s) \\cdot 0 + (%s) \\cdot m = %s + (%s)m$. \\\\ Khi $(\\vec{u}, \\vec{v}) = 45^\\circ$, ta có: \\\\ $\\cos(\\vec{u}, \\vec{v}) = \\frac{\\vec{u} \\cdot \\vec{v}}{|\\vec{u}| \\cdot |\\vec{v}|} = \\frac{\\sqrt{2}}{2}$ \\\\ $\\Leftrightarrow \\frac{%s + (%s)m}{\\sqrt{%s} \\cdot \\sqrt{%s + m^2}} = \\frac{\\sqrt{2}}{2} \\Leftrightarrow \\begin{cases} %s + (%s)m > 0 \\\\ 2\\left[%s + (%s)m\\right]^2 = %s(%s + m^2) \\end{cases}$ \\\\ $\\Leftrightarrow %s m^2 + (%s) m + (%s) = 0$. \\\\ Giải phương trình và kết hợp điều kiện $\\vec{u} \\cdot \\vec{v} > 0$, ta thu được giá trị $m \\approx %s$. \\\\ So sánh với $%s$, ta thấy $m %s %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            u1,
            v1,
            u2,
            u3,
            u1 * v1,
            u3,
            u1 * v1,
            u3,
            len_u_sq,
            v1**2,
            u1 * v1,
            u3,
            u1 * v1,
            u3,
            len_u_sq,
            v1**2,
            A_m,
            B_m,
            C_m,
            str(round(m_target, 2)).replace(".", ","),
            str_bound_m,
            "<" if is_m_lt_bound else ">",
            str_bound_m,
            "đúng" if "\\True" in vdc_da_1 else "sai",
        )
    )
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    
    def count_true_answers(answers):
        return sum("\\True" in ans for ans in answers)
    
    
    # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
    
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        "\\begin{minipage}{\\textwidth} \n"
        "\\begin{ex}\n"
        + str(noidungcauhoi)
        + "\n"
        "\\choiceTFn \n"
        "{" + str(shuffled_answers_nb[0]) + "}\n"
        "{" + str(shuffled_answers_th[0]) + "}\n"
        "{" + str(shuffled_answers_vd[0]) + "}\n"
        "{" + str(shuffled_answers_vdc[0]) + "}\n"
        "\\loigiai{ \n"
        "\\begin{enumEX}[a)]{1} \n"
        "\\item " + str(shuffled_solutions_nb[0]) + "\n"
        "\\item " + str(shuffled_solutions_th[0]) + "\n"
        "\\item " + str(shuffled_solutions_vd[0]) + "\n"
        "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
        "\\end{enumEX}} \n"
        "\\end{ex}\n \\end{minipage}\n\n" )
    return content
    