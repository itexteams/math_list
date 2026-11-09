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


def bt_dang27_p2_b2_c1_hh12(self):
    # Hàm biểu diễn vectơ theo hệ ba vectơ đơn vị i, j, k
    def format_ijk(c1, c2, c3):
        res = ""
        # Thành phần i
        if c1 == 1:
            res += "\\vec{i}"
        elif c1 == -1:
            res += "-\\vec{i}"
        elif c1 != 0:
            res += "%s\\vec{i}" % c1
    
        # Thành phần j
        if c2 == 1:
            res += "+\\vec{j}" if res else "\\vec{j}"
        elif c2 == -1:
            res += "-\\vec{j}"
        elif c2 > 0:
            res += "+%s\\vec{j}" % c2 if res else "%s\\vec{j}" % c2
        elif c2 < 0:
            res += "%s\\vec{j}" % c2
    
        # Thành phần k
        if c3 == 1:
            res += "+\\vec{k}" if res else "\\vec{k}"
        elif c3 == -1:
            res += "-\\vec{k}"
        elif c3 > 0:
            res += "+%s\\vec{k}" % c3 if res else "%s\\vec{k}" % c3
        elif c3 < 0:
            res += "%s\\vec{k}" % c3
    
        if not res:
            return "\\vec{0}"
        return res
    
    
    # Sinh ngẫu nhiên dữ liệu cho hai điểm A và B
    while True:
        xa = random.randint(-4, 4)
        ya = random.randint(-4, 4)
        za = random.randint(-4, 4)
    
        xb = random.randint(-4, 4)
        yb = 0  # Chọn tung độ bằng 0 như bài gốc để tạo bẫy vectơ OB
        zb = random.randint(-4, 4)
    
        # Đảm bảo O, A, B không thẳng hàng và khác nhau
        cp_x = ya * zb - za * yb
        cp_y = za * xb - xa * zb
        cp_z = xa * yb - ya * xb
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (0, 0, 0)
            and (xb, yb, zb) != (0, 0, 0)
        ):
            break
    
    # 1. Toạ độ của vectơ OA chính là toạ độ của điểm A[cite: 23]
    oa_x = xa
    oa_y = ya
    oa_z = za
    
    oa_x_s = -xa if xa != 0 else 1
    oa_y_s = ya
    oa_z_s = za
    
    # 2. Biểu diễn vectơ OB theo các vectơ đơn vị i, j, k[cite: 23]
    str_ob_true = format_ijk(xb, yb, zb)
    # Dạng sai: thêm thành phần j (ví dụ yb = 0 nhưng biểu diễn có + j)[cite: 23]
    str_ob_false = format_ijk(xb, 1, zb)
    
    # 3. Toạ độ của vectơ BA[cite: 23]
    ba_x = xa - xb
    ba_y = ya - yb
    ba_z = za - zb
    
    # Vectơ BA sai (nhầm sang vectơ AB)[cite: 23]
    ba_x_s = -ba_x
    ba_y_s = -ba_y
    ba_z_s = -ba_z
    
    # 4. Tứ giác OABC là hình bình hành <=> vecto OA = vecto CB <=> C = B - OA = B - A[cite: 23]
    # Hoặc vecto OC = vecto BA => C = BA = (ba_x; ba_y; ba_z)[cite: 23]
    # Chú ý: Ở đề gốc khẳng định C(ba_x; ba_y; ba_z), tức là C = BA[cite: 23].
    # Nhưng nếu OABC là hình bình hành thì vecto OC = vecto AB (chứ không phải BA)[cite: 23]
    # => vecto OA = vecto CB <=> B - C = A - O <=> C = B - A = -BA = (-ba_x; -ba_y; -ba_z)[cite: 23]
    xc_true = xb - xa
    yc_true = yb - ya
    zc_true = zb - za
    
    # Tọa độ khẳng định trong đề gốc (nhầm OABC có OC = BA):
    xc_claim = ba_x
    yc_claim = ba_y
    zc_claim = ba_z
    
    # Nội dung câu hỏi[cite: 23]
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho hai điểm $A(%s;%s;%s)$, $B(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Tọa độ của vectơ OA[cite: 23]
    nb_da_1_d = "\\True Tọa độ của vectơ $\\vec{OA}$ là $\\vec{OA} = (%s;%s;%s)$" % (
        oa_x,
        oa_y,
        oa_z,
    )
    nb_da_1_s = "Tọa độ của vectơ $\\vec{OA}$ là $\\vec{OA} = (%s;%s;%s)$" % (
        oa_x_s,
        oa_y_s,
        oa_z_s,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Theo định nghĩa tọa độ của vectơ, ta có $\\vec{OA} = (x_A - x_O; y_A - y_O; z_A - z_O) = (%s - 0; %s - 0; %s - 0) = (%s;%s;%s)$."""
        % (xa, ya, za, oa_x, oa_y, oa_z)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Biểu diễn vectơ OB theo i, j, k[cite: 23]
    th_da_1_d = "\\True Ta có $\\vec{OB} = %s$" % (str_ob_true)
    th_da_1_s = "Ta có $\\vec{OB} = %s$" % (str_ob_false)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Tọa độ điểm $B$ là $B(%s;%s;%s)$, suy ra $\\vec{OB} = (%s;%s;%s)$. \\\\ Do đó ta có biểu diễn theo các vectơ đơn vị là: $\\vec{OB} = %s$."""
        % (xb, yb, zb, xb, yb, zb, str_ob_true)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Tọa độ của vectơ BA[cite: 23]
    vd_da_1_d = "\\True Tọa độ của vectơ $\\vec{BA}$ là $\\vec{BA} = (%s;%s;%s)$" % (
        ba_x,
        ba_y,
        ba_z,
    )
    vd_da_1_s = "Tọa độ của vectơ $\\vec{BA}$ là $\\vec{BA} = (%s;%s;%s)$" % (
        ba_x_s,
        ba_y_s,
        ba_z_s,
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có tọa độ của vectơ $\\vec{BA}$ là: \\\\ $\\vec{BA} = (x_A - x_B; y_A - y_B; z_A - z_B) = (%s - (%s); %s - (%s); %s - (%s)) = (%s;%s;%s)$."""
        % (xa, xb, ya, yb, za, zb, ba_x, ba_y, ba_z)
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tọa độ điểm C để tứ giác OABC là hình bình hành[cite: 23]
    vdc_da_1_d = (
        "\\True Tọa độ điểm $C$ để tứ giác $OABC$ là hình bình hành là $C(%s;%s;%s)$"
        % (xc_true, yc_true, zc_true)
    )
    vdc_da_1_s = (
        "Tọa độ điểm $C$ để tứ giác $OABC$ là hình bình hành là $C(%s;%s;%s)$"
        % (xc_claim, yc_claim, zc_claim)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi tọa độ điểm $C$ là $C(x_C; y_C; z_C)$. \\\\ Tứ giác $OABC$ là hình bình hành khi và chỉ khi: \\\\ $\\vec{OC} = \\vec{AB} \\Leftrightarrow (x_C; y_C; z_C) = (x_B - x_A; y_B - y_A; z_B - z_A)$ \\\\ $\\Leftrightarrow \\begin{cases} x_C = %s - (%s) = %s \\\\ y_C = %s - (%s) = %s \\\\ z_C = %s - (%s) = %s \\end{cases} \\Rightarrow C(%s;%s;%s)$."""
        % (
            xb,
            xa,
            xc_true,
            yb,
            ya,
            yc_true,
            zb,
            za,
            zc_true,
            xc_true,
            yc_true,
            zc_true,
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
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    