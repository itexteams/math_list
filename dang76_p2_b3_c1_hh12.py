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


def bt_dang76_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A(a; 0; 0), B(0; a; 0), C(0; 0; a) với a nguyên dương[cite: 25]
    # Đảm bảo tứ diện OABC là tứ diện vuông cân tại O[cite: 25]
    while True:
        a_val = random.choice([2, 3, 4, 5, 6])
        xa, ya, za = a_val, 0, 0
        xb, yb, zb = 0, a_val, 0
        xc, yc, zc = 0, 0, a_val
    
        # OA = a_val[cite: 25]
        oa_val = a_val
    
        # Thể tích khối tứ diện vuông OABC: V = 1/6 * a^3[cite: 25]
        v_rat = Rational(a_val**3, 6)
        str_v_true = format_fraction_latex(v_rat.p, v_rat.q)
    
        # Điểm M thỏa mãn góc vuông nhìn AB, BC, CA[cite: 25]:
        # x^2 + y^2 + z^2 - ax - ay = 0
        # x^2 + y^2 + z^2 - ay - az = 0
        # x^2 + y^2 + z^2 - az - ax = 0
        # => ax = ay = az => x = y = z.
        # Thay vào: 3x^2 - 2ax = 0 <=> x = 0 (tức M trùng O) hoặc x = 2a/3 (M(2a/3; 2a/3; 2a/3))[cite: 25].
        # Cả hai điểm đều không trùng với A, B, C nên có chính xác 2 điểm M thỏa mãn[cite: 25].
        num_pts_m = 2
    
        # Giá trị sai cho thể tích[cite: 25]
        v_rat_false = Rational(a_val**3, 3)
        str_v_false = format_fraction_latex(v_rat_false.p, v_rat_false.q)
        if str_v_false == str_v_true:
            str_v_false = "\\frac{4}{3}"
    
        break
    
    # 1. Khẳng định a: OA = a_val[cite: 25]
    oa_false = a_val + random.choice([-1, 1])
    
    # 2. Khẳng định b: Tứ diện OABC là tứ diện vuông (luôn đúng do OA, OB, OC đôi một vuông góc)[cite: 25]
    
    # 3. Khẳng định c: V_{O.ABC} = str_v_true[cite: 25]
    
    # 4. Khẳng định d: Số lượng điểm M thỏa mãn góc AMB = BMC = CMA = 90 độ (đúng là 2 điểm)[cite: 25]
    num_pts_m_false = 3
    
    # Tọa độ điểm M thứ hai
    str_xm2 = format_fraction_latex(2 * a_val, 3)
    
    # Nội dung câu hỏi[cite: 25]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho ba điểm $A(%s;0;0), B(0;%s;0), C(0;0;%s)$."""
        % (a_val, a_val, a_val)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: OA = a_val[cite: 25]
    nb_da_1_d = "\\True $OA = %s$" % (oa_val)
    nb_da_1_s = "$OA = %s$" % (oa_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Khoảng cách từ gốc tọa độ $O(0;0;0)$ đến điểm $A(%s;0;0)$ là: \\\\ $OA = \\sqrt{x_A^2 + y_A^2 + z_A^2} = \\sqrt{(%s)^2 + 0^2 + 0^2} = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            a_val,
            a_val,
            oa_val,
            "đúng" if "\\True" in nb_da_1 else "sai",
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Tứ diện OABC là tứ diện vuông[cite: 25]
    th_da_1_d = "\\True Tứ diện $OABC$ là tứ diện vuông"
    th_da_1_s = "Tứ diện $OABC$ không phải là tứ diện vuông"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có điểm $A(%s;0;0) \\in Ox$, điểm $B(0;%s;0) \\in Oy$, điểm $C(0;0;%s) \\in Oz$. \\\\ Vì ba trục tọa độ $Ox, Oy, Oz$ đôi một vuông góc với nhau nên các đoạn thẳng $OA, OB, OC$ đôi một vuông góc tại gốc tọa độ $O$, tức là: \\\\ $OA \\perp OB, OB \\perp OC, OC \\perp OA$. \\\\ Theo định nghĩa, tứ diện có ba cạnh xuất phát từ một đỉnh đôi một vuông góc là một tứ diện vuông (vuông tại đỉnh $O$). \\\\ Do đó khẳng định là %s."""
        % (
            a_val,
            a_val,
            a_val,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Thể tích khối tứ diện OABC[cite: 25]
    vd_da_1_d = "\\True $V_{O.ABC} = %s$" % (str_v_true)
    vd_da_1_s = "$V_{O.ABC} = %s$" % (str_v_false)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì tứ diện $OABC$ là tứ diện vuông đỉnh $O$ nên thể tích khối tứ diện $OABC$ được tính theo công thức: \\\\ $V_{O.ABC} = \\frac{1}{6} OA \\cdot OB \\cdot OC$. \\\\ Ta có: $OA = %s, OB = %s, OC = %s$. \\\\ Khi đó: \\\\ $V_{O.ABC} = \\frac{1}{6} \\cdot %s \\cdot %s \\cdot %s = \\frac{%s}{6} = %s$. \\\\ Do đó mệnh đề là %s."""
        % (
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val**3,
            str_v_true,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Có tất cả 3 điểm M không trùng với A, B, C đồng thời thỏa mãn các góc vuông[cite: 25]
    vdc_da_1_d = (
        "\\True Có tất cả $2$ điểm $M$ không trùng với các điểm $A, B, C$ đồng thời thỏa mãn $\\widehat{AMB} = \\widehat{BMC} = \\widehat{CMA} = 90^\\circ$"
    )
    vdc_da_1_s = (
        "Có tất cả $%s$ điểm $M$ không trùng với các điểm $A, B, C$ đồng thời thỏa mãn $\\widehat{AMB} = \\widehat{BMC} = \\widehat{CMA} = 90^\\circ$"
        % (num_pts_m_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi tọa độ điểm $M$ là $M(x;y;z)$. \\\\ Điều kiện $\\widehat{AMB} = \\widehat{BMC} = \\widehat{CMA} = 90^\\circ$ tương đương với: \\\\ $\\begin{cases} \\vec{MA} \\cdot \\vec{MB} = 0 \\\\ \\vec{MB} \\cdot \\vec{MC} = 0 \\\\ \\vec{MC} \\cdot \\vec{MA} = 0 \\end{cases} \\Leftrightarrow \\begin{cases} (x - %s)x + y(y - %s) + z^2 = 0 \\\\ x^2 + (y - %s)y + z(z - %s) = 0 \\\\ (x - %s)x + y^2 + (z - %s)z = 0 \\end{cases}$ \\\\ $\\Leftrightarrow \\begin{cases} x^2 + y^2 + z^2 - %sx - %sy = 0 \\quad (1) \\\\ x^2 + y^2 + z^2 - %sy - %sz = 0 \\quad (2) \\\\ x^2 + y^2 + z^2 - %sz - %sx = 0 \\quad (3) \\end{cases}$. \\\\ Trừ vế với vế của (1) cho (2), và (2) cho (3), ta được: \\\\ $\\begin{cases} -%sx + %sz = 0 \\\\ -%sy + %sx = 0 \\end{cases} \\Leftrightarrow x = y = z$. \\\\ Thay $x = y = z$ vào phương trình (1), ta được: \\\\ $3x^2 - %sx - %sx = 0 \\Leftrightarrow 3x^2 - %sx = 0 \\Leftrightarrow x(3x - %s) = 0 \\Leftrightarrow \\left[\\begin{aligned} &x = 0 \\\\ &x = %s \\end{aligned}\\right.$. \\\\ $\\bullet$ Với $x = 0 \\Rightarrow y = 0, z = 0 \\Rightarrow M_1(0;0;0) \\equiv O$. \\\\ $\\bullet$ Với $x = %s \\Rightarrow y = %s, z = %s \\Rightarrow M_2\\left(%s;%s;%s\\right)$. \\\\ Cả hai điểm $M_1$ và $M_2$ đều không trùng với bất kỳ điểm nào trong ba điểm $A, B, C$. \\\\ Như vậy có tất cả đúng $2$ điểm $M$ thỏa mãn yêu cầu bài toán. \\\\ Do đó khẳng định có $%s$ điểm $M$ là %s."""
        % (
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            a_val,
            2 * a_val,
            2 * a_val,
            str_xm2,
            str_xm2,
            str_xm2,
            str_xm2,
            str_xm2,
            str_xm2,
            str_xm2,
            num_pts_m_false if "\\True" not in vdc_da_1 else 2,
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
    