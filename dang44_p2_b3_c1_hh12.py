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


def bt_dang44_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    while True:
        xa_val = random.choice([2, 4, 6])
    
        # Chọn a = b nguyên dương[cite: 23]
        a_val = random.choice([2, 3, 4, 5, 6])
        b_val = a_val
    
        # Kiểm tra tam giác OAB không suy biến
        if a_val == xa_val and b_val == 0:
            continue
    
        ab_sq = (a_val - xa_val) ** 2 + b_val**2
        str_ab_len = latex(sp.sqrt(ab_sq))
    
        # Chọn c nguyên dương sao cho V_OABC nguyên đẹp[cite: 23]
        c_candidates = [k for k in range(1, 10) if (xa_val * b_val * k) % 12 == 0]
        if not c_candidates:
            continue
        c_val = random.choice(c_candidates)
    
        v_oabc = (xa_val * b_val * c_val) // 12
        if v_oabc > 0:
            break
    
    # 1. Khoảng cách từ A đến gốc tọa độ O: OA = xa_val[cite: 23]
    oa_val = xa_val
    oa_val_s = oa_val + random.choice([-1, 1])
    
    # 2. Tứ diện OABC có là tứ diện vuông không?
    # Vì góc AOB = 45 độ != 90 độ nên OA không vuông góc OB, do đó OABC KHÔNG PHẢI là tứ diện vuông[cite: 23]
    
    # 3. Giá trị biểu thức c^2 * (a^2 + b^2)[cite: 23]
    val_c2_ab = (c_val**2) * (a_val**2 + b_val**2)
    val_c2_ab_s = val_c2_ab + random.choice([-20, -10, 10, 20])
    
    # 4. Giá trị biểu thức T = a + b + c là số tự nhiên lẻ hay chẵn[cite: 23]
    val_t = a_val + b_val + c_val
    is_t_odd = val_t % 2 != 0
    
    # Nội dung câu hỏi[cite: 23]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(%s;0;0), B(a;b;0), C(0;0;c)$ với $(a,b,c > 0)$ thỏa mãn độ dài đoạn $AB = %s$, góc $\\widehat{AOB} = 45^\\circ$ và thể tích khối tứ diện $OABC$ bằng $%s$."""
        % (xa_val, str_ab_len, v_oabc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Phát biểu a: Điểm A cách gốc tọa độ một khoảng bằng oa_val[cite: 23]
    nb_da_1_d = "\\True Điểm $A$ cách gốc tọa độ một khoảng bằng $%s$" % (oa_val)
    nb_da_1_s = "Điểm $A$ cách gốc tọa độ một khoảng bằng $%s$" % (oa_val_s)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ gốc tọa độ là $O(0;0;0)$. \\\\ Khoảng cách từ điểm $A(%s;0;0)$ đến gốc tọa độ $O$ là: \\\\ $OA = \\sqrt{(%s - 0)^2 + (0 - 0)^2 + (0 - 0)^2} = %s$."""
        % (xa_val, xa_val, oa_val)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Phát biểu b: Tứ diện OABC là tứ diện vuông[cite: 23]
    th_da_1_d = "\\True Tứ diện $OABC$ không phải là tứ diện vuông"
    th_da_1_s = "Tứ diện $OABC$ là tứ diện vuông"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Theo giả thiết, góc $\\widehat{AOB} = 45^\\circ \\neq 90^\\circ$ nên hai cạnh $OA$ và $OB$ không vuông góc với nhau. \\\\ Do đó, tại đỉnh $O$ không có ba cạnh đôi một vuông góc ($OA, OB, OC$ không đôi một vuông góc), suy ra tứ diện $OABC$ không phải là tứ diện vuông tại $O$. \\\\ Tương tự, các đỉnh còn lại cũng không thể có ba cạnh đôi một vuông góc. \\\\ Vậy phát biểu khẳng định tứ diện $OABC$ là tứ diện vuông là sai."""
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Phát biểu c: c^2 (a^2 + b^2) = val_c2_ab[cite: 23]
    vd_da_1_d = "\\True $c^2(a^2 + b^2) = %s$" % (val_c2_ab)
    vd_da_1_s = "$c^2(a^2 + b^2) = %s$" % (val_c2_ab_s)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có $\\vec{OA} = (%s;0;0)$ và $\\vec{OB} = (a;b;0)$ (với $a, b > 0$). \\\\ $\\cos\\widehat{AOB} = \\frac{\\vec{OA} \\cdot \\vec{OB}}{|\\vec{OA}| \\cdot |\\vec{OB}|} = \\frac{%s a}{%s \\sqrt{a^2 + b^2}} = \\frac{a}{\\sqrt{a^2 + b^2}}$. \\\\ Do $\\widehat{AOB} = 45^\\circ$ nên: \\\\ $\\frac{a}{\\sqrt{a^2 + b^2}} = \\cos 45^\\circ = \\frac{\\sqrt{2}}{2} \\Leftrightarrow 2a^2 = a^2 + b^2 \\Leftrightarrow a = b$ (do $a, b > 0$). \\\\ Mặt khác: \\\\ $AB^2 = (a - %s)^2 + b^2 + 0^2 = (a - %s)^2 + a^2 = 2a^2 - %sa + %s$. \\\\ Theo đề bài $AB = %s \\Rightarrow AB^2 = %s$, do đó: \\\\ $2a^2 - %sa + %s = %s \\Leftrightarrow 2a^2 - %sa + (%s) = 0 \\Leftrightarrow a = %s$ (do $a > 0$). \\\\ Suy ra $b = %s$. \\\\ Tam giác $OAB$ nằm trong mặt phẳng $(Oxy)$ có diện tích là: \\\\ $S_{OAB} = \\frac{1}{2} OA \\cdot b = \\frac{1}{2} \\cdot %s \\cdot %s = %s$. \\\\ Điểm $C(0;0;c) \\in Oz \\Rightarrow OC \\perp (Oxy)$ và $OC = c$ (do $c > 0$). \\\\ Thể tích tứ diện $OABC$ là: \\\\ $V_{OABC} = \\frac{1}{3} S_{OAB} \\cdot OC = \\frac{1}{3} \\cdot %s \\cdot c = %s \\Leftrightarrow c = %s$. \\\\ Khi đó: $c^2(a^2 + b^2) = %s^2 \\cdot (%s^2 + %s^2) = %s \\cdot %s = %s$."""
        % (
            xa_val,
            xa_val,
            xa_val,
            xa_val,
            xa_val,
            2 * xa_val,
            xa_val**2,
            str_ab_len,
            ab_sq,
            2 * xa_val,
            xa_val**2,
            ab_sq,
            2 * xa_val,
            xa_val**2 - ab_sq,
            a_val,
            b_val,
            xa_val,
            b_val,
            (xa_val * b_val) // 2,
            (xa_val * b_val) // 2,
            v_oabc,
            c_val,
            c_val,
            a_val,
            b_val,
            c_val**2,
            a_val**2 + b_val**2,
            val_c2_ab,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Phát biểu d: Giá trị biểu thức T = a + b + c là một số tự nhiên lẻ/chẵn[cite: 23]
    if is_t_odd:
        vdc_da_1_d = (
            "\\True Giá trị biểu thức $T = a + b + c$ là một số tự nhiên lẻ"
        )
        vdc_da_1_s = (
            "Giá trị biểu thức $T = a + b + c$ là một số tự nhiên chẵn"
        )
    else:
        vdc_da_1_d = (
            "\\True Giá trị biểu thức $T = a + b + c$ là một số tự nhiên chẵn"
        )
        vdc_da_1_s = (
            "Giá trị biểu thức $T = a + b + c$ là một số tự nhiên lẻ"
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Từ kết quả tìm được ở các câu trên, ta có tọa độ các tham số: \\\\ $a = %s$, $b = %s$, $c = %s$. \\\\ Khi đó giá trị của biểu thức $T$ là: \\\\ $T = a + b + c = %s + %s + %s = %s$. \\\\ Vì $%s$ là một số tự nhiên %s nên phát biểu là %s."""
        % (
            a_val,
            b_val,
            c_val,
            a_val,
            b_val,
            c_val,
            val_t,
            val_t,
            "lẻ" if is_t_odd else "chẵn",
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
    