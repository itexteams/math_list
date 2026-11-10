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


def bt_dang68_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai vectơ u và v[cite: 21]:
    # u = (0; u2; u3)
    # v = (m - m0; k2*m; u3)
    # Khi đó:
    # 1. u = v <=> m = m0[cite: 21]
    # 2. |u| = |v| <=> m = m0 hoặc m = m2 = - (k2^2 - 1)*m0 / (k2^2 + 1)[cite: 21]
    # 3. u vuông góc v <=> u.v = 0 <=> k2*u2*m + u3^2 = 0 <=> m = - u3^2 / (k2*u2)[cite: 21]
    while True:
        m0 = random.choice([1, 2])
        k2 = random.choice([2, 3])
        u2 = k2 * m0
        u3 = random.choice([2, 3, 4, 5])
    
        len_u_sq = u2**2 + u3**2
    
        # Nghiệm thứ hai của phương trình |u| = |v|: m2 = - (k2^2 - 1)*m0 / (k2^2 + 1)[cite: 21]
        m2_rat = Rational(-(k2**2 - 1) * m0, k2**2 + 1)
    
        # Nghiệm của phương trình u vuông góc v: m_perp = - u3^2 / (k2 * u2)[cite: 21]
        m_perp_rat = Rational(-(u3**2), k2 * u2)
    
        if len_u_sq > 0:
            break
    
    # 1. Khẳng định a: |u| = sqrt(len_u_sq)[cite: 21]
    str_len_u_true = latex(sp.sqrt(len_u_sq))
    str_len_u_false = latex(sp.sqrt(len_u_sq + random.choice([-2, -1, 1, 2])))
    if str_len_u_false == str_len_u_true:
        str_len_u_false = "\\sqrt{13}"[cite: 21]
    
    # 2. Khẳng định b: u = v <=> m = m0[cite: 21]
    m0_false = m0 + random.choice([-1, 1])
    if m0_false == 0:
        m0_false = m0 + 2
    
    # 3. Khẳng định c: |u| = |v| <=> m = m2_rat (Mệnh đề sai vì phương trình có hai nghiệm m = m0 hoặc m = m2)[cite: 21]
    str_m2 = format_fraction_latex(m2_rat.p, m2_rat.q)
    
    # 4. Khẳng định d: u vuông góc v <=> m = - u3^2 / (k2 * u2)[cite: 21]
    # Tạo phương án sai bằng cách bỏ dấu trừ (như đề gốc)[cite: 21]
    str_m_perp_true = format_fraction_latex(m_perp_rat.p, m_perp_rat.q)
    str_m_perp_false = format_fraction_latex(-m_perp_rat.p, m_perp_rat.q)
    
    # Chuỗi hiển thị cho vectơ v[cite: 21]
    str_v1 = "m - %s" % (m0) if m0 > 0 else "m + %s" % (-m0)
    str_v2 = "%sm" % (k2)
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho hai véc tơ $\\vec{u} = (0;%s;%s)$ và $\\vec{v} = (%s;%s;%s)$."""
        % (u2, u3, str_v1, str_v2, u3)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: |u| = ...[cite: 21]
    nb_da_1_d = "\\True $|\\vec{u}| = %s$" % (str_len_u_true)
    nb_da_1_s = "$|\\vec{u}| = %s$" % (str_len_u_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Độ dài của vectơ $\\vec{u}$ được tính theo công thức: \\\\ $|\\vec{u}| = \\sqrt{0^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
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
    # Mệnh đề b: u = v <=> m = m0[cite: 21]
    th_da_1_d = "\\True $\\vec{u} = \\vec{v} \\Leftrightarrow m = %s$" % (m0)
    th_da_1_s = "$\\vec{u} = \\vec{v} \\Leftrightarrow m = %s$" % (m0_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Hai vectơ $\\vec{u}$ và $\\vec{v}$ bằng nhau khi và chỉ khi các tọa độ tương ứng bằng nhau: \\\\ $\\vec{u} = \\vec{v} \\Leftrightarrow \\begin{cases} m - %s = 0 \\\\ %sm = %s \\\\ %s = %s \\end{cases} \\Leftrightarrow \\begin{cases} m = %s \\\\ m = %s \\end{cases} \\Leftrightarrow m = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            m0,
            k2,
            u2,
            u3,
            u3,
            m0,
            m0,
            m0,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: |u| = |v| <=> m = m2_rat hoặc m = m0[cite: 21]
    vd_da_1_d = (
        "\\True $|\\vec{u}| = |\\vec{v}| \\Leftrightarrow \\left[\\begin{aligned} &m = %s \\\\ &m = %s \\end{aligned}\\right."
        % (m0, str_m2)
    )
    vd_da_1_s = (
        "$|\\vec{u}| = |\\vec{v}| \\Leftrightarrow m = %s$" % (str_m2)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    quad_a = k2**2 + 1
    quad_b = -2 * m0
    quad_c = m0**2 - u2**2
    
    loigiai_vd_1 = (
        """Ta có: \\\\ $|\\vec{u}| = \\sqrt{%s}$. \\\\ $|\\vec{v}| = \\sqrt{(m - %s)^2 + (%sm)^2 + (%s)^2} = \\sqrt{m^2 - %sm + %s + %sm^2 + %s} = \\sqrt{%sm^2 - %sm + %s}$. \\\\ Khi đó: \\\\ $|\\vec{u}| = |\\vec{v}| \\Leftrightarrow |\\vec{u}|^2 = |\\vec{v}|^2 \\Leftrightarrow %sm^2 - %sm + %s = %s$ \\\\ $\\Leftrightarrow %sm^2 - %sm + (%s) = 0 \\Leftrightarrow (m - %s)(%sm %s) = 0$ \\\\ $\\Leftrightarrow \\left[\\begin{aligned} &m = %s \\\\ &m = %s \\end{aligned}\\right.$. \\\\ Vì phương trình có hai nghiệm phân biệt nên khẳng định chỉ có một nghiệm $m = %s$ là sai. \\\\ Do đó mệnh đề là %s."""
        % (
            len_u_sq,
            m0,
            k2,
            u3,
            2 * m0,
            m0**2,
            k2**2,
            u3**2,
            quad_a,
            2 * m0,
            m0**2 + u3**2,
            quad_a,
            2 * m0,
            m0**2 + u3**2,
            len_u_sq,
            quad_a,
            2 * m0,
            quad_c,
            m0,
            quad_a,
            "+ %s" % (-m2_rat.p) if -m2_rat.p > 0 else "- %s" % (m2_rat.p),
            m0,
            str_m2,
            str_m2,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: u vuông góc v <=> m = str_m_perp_true[cite: 21]
    vdc_da_1_d = (
        "\\True $\\vec{u} \\perp \\vec{v} \\Leftrightarrow m = %s$"
        % (str_m_perp_true)
    )
    vdc_da_1_s = (
        "$\\vec{u} \\perp \\vec{v} \\Leftrightarrow m = %s$" % (str_m_perp_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Hai vectơ $\\vec{u}$ và $\\vec{v}$ vuông góc với nhau khi và chỉ khi tích vô hướng của chúng bằng $0$: \\\\ $\\vec{u} \\perp \\vec{v} \\Leftrightarrow \\vec{u} \\cdot \\vec{v} = 0$ \\\\ $\\Leftrightarrow 0 \\cdot (m - %s) + (%s) \\cdot (%sm) + (%s) \\cdot (%s) = 0$ \\\\ $\\Leftrightarrow %sm + %s = 0 \\Leftrightarrow %sm = -%s \\Leftrightarrow m = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            m0,
            u2,
            k2,
            u3,
            u3,
            k2 * u2,
            u3**2,
            k2 * u2,
            u3**2,
            str_m_perp_true,
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
    