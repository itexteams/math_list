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


def bt_dang56_p2_b3_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Sinh ngẫu nhiên dữ liệu ba điểm A, B, C không thẳng hàng[cite: 20]:
    # Điểm E thỏa mãn: -2*EA + (3/2)*EB - (3/2)*EC = 0 <=> -4*EA + 3*EB - 3*EC = 0[cite: 20]
    # <=> -4(A - E) + 3(B - E) - 3(C - E) = 0 <=> -2*E - 4*A + 3*B - 3*C = 0 <=> 2*E = -4*A + 3*B - 3*C
    # <=> E = (-4*A + 3*(B - C)) / 2[cite: 20]
    # zA + zB + zC chia hết cho 3 để trọng tâm G có cao độ nguyên đẹp[cite: 20]
    while True:
        xa = random.randint(2, 5)
        ya = random.randint(1, 3)
        za = random.randint(3, 6)
    
        # Chọn điểm B và C sao cho 3*(B - C) có các thành phần chẵn để E nguyên đẹp[cite: 20]
        # => B - C chẵn, tức (xB - xC), (yB - yC), (zB - zC) là các số chẵn
        diff_x = 2 * random.randint(1, 3)
        diff_y = 2 * random.randint(-2, 1)
        diff_z = 2 * random.randint(0, 2)
    
        xc = random.randint(-2, 1)
        yc = random.randint(1, 3)
        zc = random.randint(0, 2)
    
        xb = xc + diff_x
        yb = yc + diff_y
        zb = zc + diff_z
    
        # Trọng tâm G: zG = (za + zb + zc) / 3[cite: 20]
        if (za + zb + zc) % 3 == 0:
            zg_val = (za + zb + zc) // 3
    
            # Tọa độ điểm E:[cite: 20]
            # xE = (-4*xa + 3*xb - 3*xc)/2 = -2*xa + 3*diff_x/2
            xe_val = -2 * xa + (3 * diff_x) // 2
            ye_val = -2 * ya + (3 * diff_y) // 2
            ze_val = -2 * za + (3 * diff_z) // 2
    
            oa_sq = xa**2 + ya**2 + za**2
    
            # Đảm bảo A, B, C không thẳng hàng
            ab_x, ab_y, ab_z = xb - xa, yb - ya, zb - za
            ac_x, ac_y, ac_z = xc - xa, yc - ya, zc - za
            cp_x = ab_y * ac_z - ab_z * ac_y
            cp_y = ab_z * ac_x - ab_x * ac_z
            cp_z = ab_x * ac_y - ab_y * ac_x
    
            if (cp_x != 0 or cp_y != 0 or cp_z != 0) and (xa, ya, za) != (xb, yb, zb):
                # Tính giá trị P = a - 2b + 4c khi M trùng E[cite: 20]
                val_p = xe_val - 2 * ye_val + 4 * ze_val
                break
    
    # 1. Khẳng định a: OA = sqrt(oa_sq)[cite: 20]
    str_oa_true = latex(sp.sqrt(oa_sq))
    str_oa_false = latex(sp.sqrt(oa_sq + random.choice([-2, -1, 1, 2])))
    if str_oa_false == str_oa_true:
        str_oa_false = "\\sqrt{42}"[cite: 20]
    
    # 2. Khẳng định b: Trọng tâm tam giác ABC có cao độ bằng zg_val[cite: 20]
    zg_false = zg_val + random.choice([-1, 1])
    
    # 3. Khẳng định c: Điểm E có tung độ bằng ye_val[cite: 20]
    ye_false = ye_val + random.choice([-2, -1, 1, 2])
    
    # 4. Khẳng định d: Điểm M thỏa mãn MA.MB + 2MB.MC - 5MC.MA lớn nhất thì P = a - 2b + 4c bằng val_p[cite: 20]
    val_p_false = val_p + random.choice([-3, -2, 2, 3])
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho các điểm $A(%s;%s;%s), B(%s;%s;%s), C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Độ dài đoạn OA[cite: 20]
    nb_da_1_d = "\\True $OA = %s$" % (str_oa_true)
    nb_da_1_s = "$OA = %s$" % (str_oa_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Khoảng cách từ gốc tọa độ $O(0;0;0)$ đến điểm $A(%s;%s;%s)$ là: \\\\ $OA = \\sqrt{x_A^2 + y_A^2 + z_A^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s} = %s$."""
        % (
            xa,
            ya,
            za,
            xa,
            ya,
            za,
            oa_sq,
            str_oa_true,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Trọng tâm tam giác ABC có cao độ bằng zg_val[cite: 20]
    th_da_1_d = (
        "\\True Trọng tâm tam giác $ABC$ có cao độ bằng $%s$" % (zg_val)
    )
    th_da_1_s = (
        "Trọng tâm tam giác $ABC$ có cao độ bằng $%s$" % (zg_false)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Gọi $G$ là trọng tâm của tam giác $ABC$. Cao độ của điểm $G$ là: \\\\ $z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = \\frac{%s}{3} = %s$. \\\\ Vì $%s %s %s$ nên khẳng định là %s."""
        % (
            za,
            zb,
            zc,
            za + zb + zc,
            zg_val,
            zg_val,
            "=" if "\\True" in th_da_1 else "\\neq",
            zg_val if "\\True" in th_da_1 else zg_false,
            "đúng" if "\\True" in th_da_1 else "sai",
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Gọi E là điểm thỏa mãn -2*EA + (3/2)*EB - (3/2)*EC = 0 thì E có tung độ bằng ye_val[cite: 20]
    vd_da_1_d = (
        "\\True Gọi $E$ là điểm thỏa mãn $-2\\vec{EA} + \\frac{3}{2}\\vec{EB} - \\frac{3}{2}\\vec{EC} = \\vec{0}$ thì $E$ có tung độ bằng $%s$"
        % (ye_val)
    )
    vd_da_1_s = (
        "Gọi $E$ là điểm thỏa mãn $-2\\vec{EA} + \\frac{3}{2}\\vec{EB} - \\frac{3}{2}\\vec{EC} = \\vec{0}$ thì $E$ có tung độ bằng $%s$"
        % (ye_false)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có hệ thức vectơ: \\\\ $-2\\vec{EA} + \\frac{3}{2}\\vec{EB} - \\frac{3}{2}\\vec{EC} = \\vec{0} \\Leftrightarrow -4\\vec{EA} + 3\\vec{EB} - 3\\vec{EC} = \\vec{0}$ \\\\ $\\Leftrightarrow -4(\\vec{OA} - \\vec{OE}) + 3(\\vec{OB} - \\vec{OE}) - 3(\\vec{OC} - \\vec{OE}) = \\vec{0}$ \\\\ $\\Leftrightarrow -2\\vec{OE} - 4\\vec{OA} + 3\\vec{OB} - 3\\vec{OC} = \\vec{0} \\Leftrightarrow \\vec{OE} = \\frac{-4\\vec{OA} + 3\\vec{OB} - 3\\vec{OC}}{2}$. \\\\ Khi đó tung độ của điểm $E$ là: \\\\ $y_E = \\frac{-4y_A + 3y_B - 3y_C}{2} = \\frac{-4 \\cdot (%s) + 3 \\cdot (%s) - 3 \\cdot (%s)}{2} = \\frac{%s}{2} = %s$. \\\\ Do đó khẳng định điểm $E$ có tung độ bằng $%s$ là %s."""
        % (
            ya,
            yb,
            yc,
            -4 * ya + 3 * yb - 3 * yc,
            ye_val,
            ye_val if "\\True" in vd_da_1 else ye_false,
            "đúng" if "\\True" in vd_da_1 else "sai",
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm M(a;b;c) thỏa mãn MA.MB + 2MB.MC - 5MC.MA lớn nhất thì P = a - 2b + 4c bằng val_p[cite: 20]
    vdc_da_1_d = (
        "\\True Điểm $M(a;b;c)$ thỏa mãn $\\vec{MA} \\cdot \\vec{MB} + 2\\vec{MB} \\cdot \\vec{MC} - 5\\vec{MC} \\cdot \\vec{MA}$ lớn nhất thì $P = a - 2b + 4c$ bằng $%s$"
        % (val_p)
    )
    vdc_da_1_s = (
        "Điểm $M(a;b;c)$ thỏa mãn $\\vec{MA} \\cdot \\vec{MB} + 2\\vec{MB} \\cdot \\vec{MC} - 5\\vec{MC} \\cdot \\vec{MA}$ lớn nhất thì $P = a - 2b + 4c$ bằng $%s$"
        % (val_p_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Xét biểu thức $T = \\vec{MA} \\cdot \\vec{MB} + 2\\vec{MB} \\cdot \\vec{MC} - 5\\vec{MC} \\cdot \\vec{MA}$. \\\\ Chèn điểm $E$ vào biểu thức $T$, ta có: \\\\ $\\vec{MA} \\cdot \\vec{MB} = (\\vec{ME} + \\vec{EA})(\\vec{ME} + \\vec{EB}) = ME^2 + \\vec{ME}(\\vec{EA} + \\vec{EB}) + \\vec{EA} \\cdot \\vec{EB}$. \\\\ $2\\vec{MB} \\cdot \\vec{MC} = 2(\\vec{ME} + \\vec{EB})(\\vec{ME} + \\vec{EC}) = 2ME^2 + \\vec{ME}(2\\vec{EB} + 2\\vec{EC}) + 2\\vec{EB} \\cdot \\vec{EC}$. \\\\ $-5\\vec{MC} \\cdot \\vec{MA} = -5(\\vec{ME} + \\vec{EC})(\\vec{ME} + \\vec{EA}) = -5ME^2 + \\vec{ME}(-5\\vec{EC} - 5\\vec{EA}) - 5\\vec{EC} \\cdot \\vec{EA}$. \\\\ Cộng từng vế các đẳng thức trên lại, ta được: \\\\ $T = (1 + 2 - 5)ME^2 + \\vec{ME} \\cdot (-4\\vec{EA} + 3\\vec{EB} - 3\\vec{EC}) + (\\vec{EA} \\cdot \\vec{EB} + 2\\vec{EB} \\cdot \\vec{EC} - 5\\vec{EC} \\cdot \\vec{EA})$ \\\\ $= -2ME^2 + 2\\vec{ME} \\cdot \\left(-2\\vec{EA} + \\frac{3}{2}\\vec{EB} - \\frac{3}{2}\\vec{EC}\\right) + k$ (với $k$ là hằng số). \\\\ Theo kết quả ở câu c, điểm $E$ thỏa mãn $-2\\vec{EA} + \\frac{3}{2}\\vec{EB} - \\frac{3}{2}\\vec{EC} = \\vec{0}$, do đó: \\\\ $T = -2ME^2 + k$. \\\\ Vì $ME^2 \\ge 0$ nên $T \\le k$. \\\\ Biểu thức $T$ đạt giá trị lớn nhất khi và chỉ khi $ME = 0 \\Leftrightarrow M \\equiv E$. \\\\ Tọa độ điểm $E$ là: \\\\ $\\begin{cases} x_E = \\frac{-4x_A + 3x_B - 3x_C}{2} = \\frac{-4 \\cdot (%s) + 3 \\cdot (%s) - 3 \\cdot (%s)}{2} = %s \\\\ y_E = \\frac{-4y_A + 3y_B - 3y_C}{2} = \\frac{-4 \\cdot (%s) + 3 \\cdot (%s) - 3 \\cdot (%s)}{2} = %s \\\\ z_E = \\frac{-4z_A + 3z_B - 3z_C}{2} = \\frac{-4 \\cdot (%s) + 3 \\cdot (%s) - 3 \\cdot (%s)}{2} = %s \\end{cases} \\Rightarrow E(%s;%s;%s)$. \\\\ Do đó $a = %s, b = %s, c = %s$. \\\\ Khi đó: $P = a - 2b + 4c = (%s) - 2 \\cdot (%s) + 4 \\cdot (%s) = %s$. \\\\ Do đó khẳng định là %s."""
        % (
            xa,
            xb,
            xc,
            xe_val,
            ya,
            yb,
            yc,
            ye_val,
            za,
            zb,
            zc,
            ze_val,
            xe_val,
            ye_val,
            ze_val,
            xe_val,
            ye_val,
            ze_val,
            xe_val,
            ye_val,
            ze_val,
            val_p,
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
    