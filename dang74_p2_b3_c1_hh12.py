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


def bt_dang74_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A và B, và hằng số k sao cho |MA + MB| = 2*R_val
    # Đảm bảo:
    # 1. xA + xB = 0 để trung điểm I có hoành độ bằng 0 (xI = 0)
    # 2. yA = yB để I có tung độ đẹp, zA và zB có tổng chẵn
    # 3. Khi M(m; 0; 0) thuộc Ox: MI^2 = (m - 0)^2 + yI^2 + zI^2 = R_val^2
    #    => m^2 = R_val^2 - yI^2 - zI^2 > 0 để tồn tại m > 0
    while True:
        k_x = random.choice([2, 3, 4])
        xa = -k_x
        xb = k_x
    
        ya = random.randint(1, 3)
        yb = ya
    
        za = random.choice([3, 5])
        zb = random.choice([1, 3])
    
        xi = 0
        yi = ya
        zi = (za + zb) // 2
    
        # Chọn bán kính R_val sao cho R_val^2 > yi^2 + zi^2
        min_r_sq = yi**2 + zi**2
        # Chọn R_val nguyên
        r_val = int(math.isqrt(min_r_sq)) + random.choice([1, 2])
        k_len = 2 * r_val  # |MA + MB| = k_len
    
        m_sq = r_val**2 - min_r_sq
        if m_sq > 0:
            m_val = math.sqrt(m_sq)
            # So sánh OM với căn bậc hai của một số nguyên bound_comp
            bound_comp = m_sq - 1
            if bound_comp > 0:
                break
    
    # 1. Khẳng định a: Điểm A cách xa mặt phẳng (Oyz) hơn so với điểm B (hoặc bằng nhau)
    dist_a_oyz = abs(xa)
    dist_b_oyz = abs(xb)
    
    # 2. Khẳng định b: Điểm I có hoành độ bằng 0
    xi_true = 0
    xi_false = xi_true + random.choice([1, 2])
    
    # 3. Khẳng định c: Độ dài đoạn thẳng MI không đổi (luôn đúng do |MA + MB| = 2MI = const)
    
    # 4. Khẳng định d: Nếu M có hoành độ dương thuộc trục Ox thì OM > sqrt(bound_comp)
    str_bound_comp = latex(sp.sqrt(bound_comp))
    is_om_gt = m_val > math.sqrt(bound_comp)
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A(%s;%s;%s), B(%s;%s;%s)$. Điểm $I$ là trung điểm của đoạn thẳng $AB$ và điểm $M$ bất kỳ thỏa mãn $\\left|\\vec{MA} + \\vec{MB}\\right| = %s$."""
        % (xa, ya, za, xb, yb, zb, k_len)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Điểm A cách xa mặt phẳng (Oyz) hơn so với điểm B
    nb_da_1_d = (
        "\\True Điểm $A$ và điểm $B$ có khoảng cách đến mặt phẳng $(Oyz)$ bằng nhau"
    )
    nb_da_1_s = (
        "Điểm $A$ cách xa mặt phẳng $(Oyz)$ hơn so với điểm $B$"
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng tọa độ $(Oyz)$ có phương trình là $x = 0$. \\\\ Khoảng cách từ điểm $A(%s;%s;%s)$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(A, (Oyz)) = |x_A| = |%s| = %s$. \\\\ Khoảng cách từ điểm $B(%s;%s;%s)$ đến mặt phẳng $(Oyz)$ là: \\\\ $d(B, (Oyz)) = |x_B| = |%s| = %s$. \\\\ Do đó $d(A, (Oyz)) = d(B, (Oyz)) = %s$. \\\\ Khẳng định điểm $A$ cách xa mặt phẳng $(Oyz)$ hơn so với điểm $B$ là sai."""
        % (
            xa,
            ya,
            za,
            xa,
            dist_a_oyz,
            xb,
            yb,
            zb,
            xb,
            dist_b_oyz,
            dist_a_oyz,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Điểm I có hoành độ bằng 0
    th_da_1_d = "\\True Điểm $I$ có hoành độ bằng $%s$" % (xi_true)
    th_da_1_s = "Điểm $I$ có hoành độ bằng $%s$" % (xi_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $I$ là trung điểm của đoạn thẳng $AB$ nên tọa độ của điểm $I$ là: \\\\ $\\begin{cases} x_I = \\frac{x_A + x_B}{2} = \\frac{%s + (%s)}{2} = 0 \\\\ y_I = \\frac{y_A + y_B}{2} = \\frac{%s + (%s)}{2} = %s \\\\ z_I = \\frac{z_A + z_B}{2} = \\frac{%s + (%s)}{2} = %s \\end{cases} \\Rightarrow I(0;%s;%s)$. \\\\ Suy ra điểm $I$ có hoành độ bằng $0$. \\\\ Do đó khẳng định là %s."""
        % (
            xa,
            xb,
            ya,
            yb,
            yi,
            za,
            zb,
            zi,
            yi,
            zi,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Độ dài đoạn thẳng MI không đổi
    vd_da_1_d = "\\True Độ dài đoạn thẳng $MI$ không đổi"
    vd_da_1_s = "Độ dài đoạn thẳng $MI$ luôn thay đổi theo vị trí của $M$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $I$ là trung điểm của đoạn thẳng $AB$ nên với mọi điểm $M$, ta có hệ thức vectơ: \\\\ $\\vec{MA} + \\vec{MB} = 2\\vec{MI}$. \\\\ Theo giả thiết đề bài: \\\\ $\\left|\\vec{MA} + \\vec{MB}\\right| = %s \\Leftrightarrow \\left|2\\vec{MI}\\right| = %s \\Leftrightarrow 2MI = %s \\Leftrightarrow MI = %s$. \\\\ Do điểm $I$ cố định và $MI = %s$ không đổi nên tập hợp các điểm $M$ là mặt cầu tâm $I(0;%s;%s)$, bán kính $R = %s$. \\\\ Do đó độ dài đoạn thẳng $MI$ không đổi. Khẳng định là %s."""
        % (
            k_len,
            k_len,
            k_len,
            r_val,
            r_val,
            yi,
            zi,
            r_val,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Nếu M có hoành độ dương thuộc trục Ox thì OM > sqrt(bound_comp)
    if is_om_gt:
        vdc_da_1_d = (
            "\\True Nếu $M$ có hoành độ dương thuộc trục $Ox$ thì $OM > %s$"
            % (str_bound_comp)
        )
        vdc_da_1_s = (
            "Nếu $M$ có hoành độ dương thuộc trục $Ox$ thì $OM < %s$"
            % (str_bound_comp)
        )
    else:
        vdc_da_1_d = (
            "\\True Nếu $M$ có hoành độ dương thuộc trục $Ox$ thì $OM < %s$"
            % (str_bound_comp)
        )
        vdc_da_1_s = (
            "Nếu $M$ có hoành độ dương thuộc trục $Ox$ thì $OM > %s$"
            % (str_bound_comp)
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_m_exact = latex(sp.sqrt(m_sq))
    
    loigiai_vdc_1 = (
        """Vì điểm $M$ thuộc trục hoành $Ox$ nên tọa độ của điểm $M$ có dạng $M(m;0;0)$ với điều kiện $m > 0$. \\\\ Theo kết quả ở câu c, ta có $MI = %s$. \\\\ Kết hợp tọa độ điểm $I(0;%s;%s)$, ta có phương trình: \\\\ $MI = \\sqrt{(m - 0)^2 + (0 - %s)^2 + (0 - %s)^2} = %s$ \\\\ $\\Leftrightarrow \\sqrt{m^2 + %s + %s} = %s \\Leftrightarrow m^2 + %s = %s \\Leftrightarrow m^2 = %s$. \\\\ Vì $m > 0$ nên $m = %s$. \\\\ Suy ra tọa độ điểm $M$ là $M(%s;0;0)$, khi đó độ dài đoạn thẳng $OM$ là: \\\\ $OM = \\sqrt{m^2 + 0^2 + 0^2} = %s = \\sqrt{%s}$. \\\\ Vì $\\sqrt{%s} %s %s$ nên khẳng định là %s."""
        % (
            r_val,
            yi,
            zi,
            yi,
            zi,
            r_val,
            yi**2,
            zi**2,
            r_val,
            min_r_sq,
            r_val**2,
            m_sq,
            str_m_exact,
            str_m_exact,
            str_m_exact,
            m_sq,
            m_sq,
            ">" if is_om_gt else "<",
            str_bound_comp,
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
    