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


def bt_dang50_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    
    # Sinh ngẫu nhiên dữ liệu hai điểm A, B sao cho:
    # 1. zA, zB cùng tính chẵn lẻ để trung điểm I có cao độ nguyên đẹp
    # 2. Tam giác OAB cân tại B (OB = AB) để đường trung tuyến kẻ từ B vuông góc cạnh OA
    #    hoặc không cân để tạo ra câu hỏi đa dạng
    # 3. xA + xB + yA + yB là số chẵn để a + b là số nguyên
    while True:
        xa = random.randint(1, 3)
        ya = random.randint(1, 3)
        za = random.choice([1, 2, 3])
    
        xb = random.randint(1, 4)
        yb = random.randint(-3, 0)
        # zB cùng tính chẵn lẻ với zA và khác 0
        zb = za + random.choice([-4, -2, 2, 4])
        if zb == 0:
            zb = za + 2
    
        oa_sq = xa**2 + ya**2 + za**2
        ob_sq = xb**2 + yb**2 + zb**2
        ab_sq = (xb - xa) ** 2 + (yb - ya) ** 2 + (zb - za) ** 2
    
        # Đảm bảo ba điểm O, A, B không thẳng hàng
        cp_x = ya * zb - za * yb
        cp_y = za * xb - xa * zb
        cp_z = xa * yb - ya * xb
    
        # a + b = (xA + xB + yA + yB) / 2
        sum_xy = xa + xb + ya + yb
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and sum_xy % 2 == 0
        ):
            break
    
    # 1. Khoảng cách từ B đến mặt phẳng (Oxy): d(B, (Oxy)) = |zB|[cite: 25]
    dist_b_oxy = abs(zb)
    dist_b_oxy_s = dist_b_oxy + random.choice([-1, 1])
    
    # 2. Cao độ của trung điểm I của đoạn thẳng AB[cite: 25]
    zi_val = (za + zb) // 2
    zi_val_s = zi_val + random.choice([-1, 1])
    
    # 3. Tam giác OAB có một đường trung tuyến vuông góc với cạnh tương ứng:[cite: 25]
    # Điều này tương đương với tam giác OAB là tam giác cân tại một trong các đỉnh O, A, hoặc B[cite: 25]
    is_isosceles = (oa_sq == ob_sq) or (oa_sq == ab_sq) or (ob_sq == ab_sq)
    if oa_sq == ob_sq:
        c_vertex = "O"
        c_edge = "AB"
    elif oa_sq == ab_sq:
        c_vertex = "A"
        c_edge = "OB"
    else:
        c_vertex = "B"
        c_edge = "OA"
    
    # 4. Điểm M(a;b;0) thuộc (Oxy) để MA^2 + MB^2 đạt GTNN:[cite: 25]
    # MA^2 + MB^2 = 2MI^2 + AB^2/2 min khi M là hình chiếu của trung điểm I lên (Oxy)[cite: 25]
    # M(xI; yI; 0) => a = (xA + xB)/2, b = (yA + yB)/2[cite: 25]
    # a + b = (xA + xB + yA + yB) / 2[cite: 25]
    sum_ab_val = sum_xy // 2
    is_sum_ab_prime = is_prime(sum_ab_val)
    
    # Nội dung câu hỏi[cite: 25]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho hai điểm $A(%s;%s;%s), B(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm B cách mặt phẳng (Oxy) một khoảng bằng dist_b_oxy[cite: 25]
    nb_da_1_d = "\\True Điểm $B$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$" % (
        dist_b_oxy
    )
    nb_da_1_s = "Điểm $B$ cách mặt phẳng $(Oxy)$ một khoảng bằng $%s$" % (
        dist_b_oxy_s
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Mặt phẳng tọa độ $(Oxy)$ có phương trình là $z = 0$. \\\\ Khoảng cách từ điểm $B(%s;%s;%s)$ đến mặt phẳng $(Oxy)$ là: \\\\ $d(B, (Oxy)) = |z_B| = |%s| = %s$."""
        % (
            xb,
            yb,
            zb,
            zb,
            dist_b_oxy,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Hai điểm A, B đối xứng qua điểm có cao độ bằng zi_val[cite: 25]
    th_da_1_d = (
        "\\True Hai điểm $A(%s;%s;%s), B(%s;%s;%s)$ đối xứng qua điểm có cao độ bằng $%s$"
        % (xa, ya, za, xb, yb, zb, zi_val)
    )
    th_da_1_s = (
        "Hai điểm $A(%s;%s;%s), B(%s;%s;%s)$ đối xứng qua điểm có cao độ bằng $%s$"
        % (xa, ya, za, xb, yb, zb, zi_val_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Hai điểm $A$ và $B$ đối xứng nhau qua trung điểm $I$ của đoạn thẳng $AB$. \\\\ Cao độ của trung điểm $I$ là: \\\\ $z_I = \\frac{z_A + z_B}{2} = \\frac{%s + (%s)}{2} = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            za,
            zb,
            zi_val,
            zi_val,
            "=" if "\\True" in th_da_1 else "\\neq",
            zi_val if "\\True" in th_da_1 else zi_val_s,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Tam giác OAB có một đường trung tuyến vuông góc với cạnh tương ứng[cite: 25]
    if is_isosceles:
        vd_da_1_d = (
            "\\True Tam giác $OAB$ có một đường trung tuyến vuông góc với cạnh tương ứng"
        )
        vd_da_1_s = (
            "Tam giác $OAB$ không có đường trung tuyến nào vuông góc với cạnh tương ứng"
        )
    else:
        vd_da_1_d = (
            "\\True Tam giác $OAB$ không có đường trung tuyến nào vuông góc với cạnh tương ứng"
        )
        vd_da_1_s = (
            "Tam giác $OAB$ có một đường trung tuyến vuông góc với cạnh tương ứng"
        )
    
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Độ dài các cạnh của tam giác $OAB$ là: \\\\ $OA = \\sqrt{x_A^2 + y_A^2 + z_A^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $OB = \\sqrt{x_B^2 + y_B^2 + z_B^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s}$. \\\\ $AB = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2} = \\sqrt{(%s - (%s))^2 + (%s - (%s))^2 + (%s - (%s))^2} = \\sqrt{%s}$. \\\\ Trong một tam giác, đường trung tuyến vuông góc với cạnh tương ứng khi và chỉ khi tam giác đó cân tại đỉnh xuất phát của đường trung tuyến. \\\\ %s \\\\ Do đó mệnh đề là %s."""
        % (
            xa,
            ya,
            za,
            oa_sq,
            xb,
            yb,
            zb,
            ob_sq,
            xb,
            xa,
            yb,
            ya,
            zb,
            za,
            ab_sq,
            (
                "Nhận thấy tam giác $OAB$ cân tại đỉnh $%s$ (vì hai cạnh bằng nhau), do đó đường trung tuyến kẻ từ đỉnh $%s$ vuông góc với cạnh tương ứng $%s$."
                % (c_vertex, c_vertex, c_edge)
            )
            if is_isosceles
            else "Nhận thấy ba cạnh $OA, OB, AB$ đôi một khác nhau nên tam giác $OAB$ không cân tại bất kỳ đỉnh nào, do đó không có đường trung tuyến nào vuông góc với cạnh tương ứng.",
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm M(a;b;0) sao cho MA^2 + MB^2 nhỏ nhất thì a + b là một số nguyên tố[cite: 25]
    if is_sum_ab_prime:
        vdc_da_1_d = (
            "\\True Xét điểm $M(a;b;0)$ sao cho $MA^2 + MB^2$ nhỏ nhất thì giá trị của $a + b$ là một số nguyên tố"
        )
        vdc_da_1_s = (
            "Xét điểm $M(a;b;0)$ sao cho $MA^2 + MB^2$ nhỏ nhất thì giá trị của $a + b$ không phải là số nguyên tố"
        )
    else:
        vdc_da_1_d = (
            "\\True Xét điểm $M(a;b;0)$ sao cho $MA^2 + MB^2$ nhỏ nhất thì giá trị của $a + b$ không phải là số nguyên tố"
        )
        vdc_da_1_s = (
            "Xét điểm $M(a;b;0)$ sao cho $MA^2 + MB^2$ nhỏ nhất thì giá trị của $a + b$ là một số nguyên tố"
        )
    
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    str_a = format_fraction_latex(xa + xb, 2)
    str_b = format_fraction_latex(ya + yb, 2)
    
    loigiai_vdc_1 = (
        """Gọi $I$ là trung điểm của đoạn thẳng $AB$. Khi đó: \\\\ $I\\left(\\frac{x_A + x_B}{2}; \\frac{y_A + y_B}{2}; \\frac{z_A + z_B}{2}\\right) = I\\left(%s; %s; %s\\right)$. \\\\ Với mọi điểm $M$, áp dụng công thức đường trung tuyến ta có: \\\\ $MA^2 + MB^2 = 2MI^2 + \\frac{AB^2}{2}$. \\\\ Do $AB$ không đổi nên $MA^2 + MB^2$ đạt giá trị nhỏ nhất khi và chỉ khi đoạn thẳng $MI$ ngắn nhất. \\\\ Vì $M(a;b;0) \\in (Oxy)$ nên $MI$ ngắn nhất khi $M$ là hình chiếu vuông góc của điểm $I$ lên mặt phẳng $(Oxy)$. \\\\ Suy ra tọa độ của điểm $M$ là: \\\\ $M\\left(%s; %s; 0\\right) \\Rightarrow a = %s, b = %s$. \\\\ Khi đó: $a + b = %s + %s = %s$. \\\\ Vì $%s$ %s số nguyên tố nên khẳng định là %s."""
        % (
            str_a,
            str_b,
            zi_val,
            str_a,
            str_b,
            str_a,
            str_b,
            str_a,
            str_b,
            sum_ab_val,
            sum_ab_val,
            "là một" if is_sum_ab_prime else "không phải là",
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
    