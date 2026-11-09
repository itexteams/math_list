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


def bt_dang38_p2_b2_c1_hh12(self):
    # Sinh ngẫu nhiên dữ liệu bốn điểm A, B, C, G[cite: 24]
    while True:
        xa = random.randint(-4, 4)
        ya = random.randint(-4, 4)
        za = random.randint(3, 8)
    
        xb = random.randint(2, 6)
        yb = random.randint(2, 6)
        zb = random.randint(1, 5)
    
        xc = random.randint(-5, -1)
        yc = random.randint(3, 8)
        zc = random.randint(6, 12)
    
        xg = random.randint(1, 4)
        yg = random.randint(2, 6)
        zg = random.randint(4, 8)
    
        # Đảm bảo không trùng điểm[cite: 24]
        if (
            len(
                {
                    (xa, ya, za),
                    (xb, yb, zb),
                    (xc, yc, zc),
                    (xg, yg, zg),
                }
            )
            == 4
        ):
            break
    
    # 1. Điểm B cách gốc tọa độ O một khoảng: OB = sqrt(xb^2 + yb^2 + zb^2)[cite: 24]
    ob_sq = xb**2 + yb**2 + zb**2
    # Chọn mốc so sánh hợp lý: ob_sq - 5 hoặc ob_sq + 5[cite: 24]
    bound_ob_sq = ob_sq - random.choice([3, 4, 5])
    ob_gt_bound = ob_sq > bound_ob_sq
    
    # 2. Điểm N đối xứng với B qua C => C là trung điểm của BN => N = 2C - B[cite: 24]
    xn = 2 * xc - xb
    yn = 2 * yc - yb
    zn = 2 * zc - zb
    
    zn_s = zn + random.choice([-3, -2, 2, 3])
    
    # 3. Điểm C' đối xứng với C qua mặt phẳng (Oxz):
    # Giữ nguyên hoành độ và cao độ, đổi dấu tung độ: C'(xc; -yc; zc)[cite: 24]
    # Cao độ của C' vẫn là zC[cite: 24]
    bound_zc = zc + random.choice([1, 2])
    zc_gt_bound = zc > bound_zc  # Luôn Sai[cite: 24]
    
    # 4. A là trọng tâm của tam giác KBG:
    # A = (K + B + G) / 3 => K = 3A - B - G[cite: 24]
    xk = 3 * xa - xb - xg
    yk = 3 * ya - yb - yg
    zk = 3 * za - zb - zg
    
    xk_s = xk + random.choice([-2, 2])
    yk_s = yk
    zk_s = zk
    
    # Nội dung câu hỏi[cite: 24]
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho bốn điểm $A(%s;%s;%s); B(%s;%s;%s); C(%s;%s;%s); G(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc, xg, yg, zg)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Điểm B cách gốc tọa độ một khoảng lớn hơn \sqrt{bound_ob_sq}[cite: 24]
    if ob_gt_bound:
        nb_da_1_d = (
            "\\True Điểm $B(%s;%s;%s)$ cách gốc tọa độ một khoảng lớn hơn $\\sqrt{%s}$"
            % (xb, yb, zb, bound_ob_sq)
        )
        nb_da_1_s = (
            "Điểm $B(%s;%s;%s)$ cách gốc tọa độ một khoảng nhỏ hơn $\\sqrt{%s}$"
            % (xb, yb, zb, bound_ob_sq)
        )
    else:
        nb_da_1_d = (
            "\\True Điểm $B(%s;%s;%s)$ cách gốc tọa độ một khoảng nhỏ hơn $\\sqrt{%s}$"
            % (xb, yb, zb, bound_ob_sq)
        )
        nb_da_1_s = (
            "Điểm $B(%s;%s;%s)$ cách gốc tọa độ một khoảng lớn hơn $\\sqrt{%s}$"
            % (xb, yb, zb, bound_ob_sq)
        )
    
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Khoảng cách từ điểm $B(%s;%s;%s)$ đến gốc tọa độ $O(0;0;0)$ là: \\\\ $OB = \\sqrt{(%s - 0)^2 + (%s - 0)^2 + (%s - 0)^2} = \\sqrt{%s^2 + %s^2 + %s^2} = \\sqrt{%s}$. \\\\ Vì $%s > %s$ nên $\\sqrt{%s} > \\sqrt{%s}$, do đó mệnh đề khẳng định khoảng cách lớn hơn $\\sqrt{%s}$ là đúng."""
        % (
            xb,
            yb,
            zb,
            xb,
            yb,
            zb,
            xb,
            yb,
            zb,
            ob_sq,
            ob_sq,
            bound_ob_sq,
            ob_sq,
            bound_ob_sq,
            bound_ob_sq,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Điểm N đối xứng với B qua C, khi đó N có cao độ bằng zn[cite: 24]
    th_da_1_d = (
        "\\True Điểm $N$ đối xứng với điểm $B$ qua $C$, khi đó $N$ có cao độ bằng $%s$"
        % (zn)
    )
    th_da_1_s = (
        "Điểm $N$ đối xứng với điểm $B$ qua $C$, khi đó $N$ có cao độ bằng $%s$"
        % (zn_s)
    )
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $N$ đối xứng với điểm $B$ qua điểm $C$ nên $C$ là trung điểm của đoạn thẳng $BN$. \\\\ Do đó ta có: \\\\ $\\begin{cases} x_C = \\frac{x_B + x_N}{2} \\\\ y_C = \\frac{y_B + y_N}{2} \\\\ z_C = \\frac{z_B + z_N}{2} \\end{cases} \\Leftrightarrow \\begin{cases} x_N = 2x_C - x_B = 2 \\cdot (%s) - (%s) = %s \\\\ y_N = 2y_C - y_B = 2 \\cdot (%s) - (%s) = %s \\\\ z_N = 2z_C - z_B = 2 \\cdot (%s) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $N$ là $N(%s;%s;%s)$. \\\\ Vậy điểm $N$ có cao độ bằng $%s$."""
        % (
            xc,
            xb,
            xn,
            yc,
            yb,
            yn,
            zc,
            zb,
            zn,
            xn,
            yn,
            zn,
            zn,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Điểm C' đối xứng với C qua mặt phẳng (Oxz) thì C' có cao độ lớn hơn bound_zc[cite: 24]
    vd_da_1_d = (
        "\\True Điểm $C'$ đối xứng với điểm $C$ qua mặt phẳng tọa độ $(Oxz)$ thì $C'$ có cao độ bằng $%s$, nhỏ hơn $%s$"
        % (zc, bound_zc)
    )
    vd_da_1_s = (
        "Điểm $C'$ đối xứng với điểm $C$ qua mặt phẳng tọa độ $(Oxz)$ thì $C'$ có cao độ lớn hơn $%s$"
        % (bound_zc)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Điểm $C'$ đối xứng với điểm $C(%s;%s;%s)$ qua mặt phẳng tọa độ $(Oxz)$ sẽ giữ nguyên hoành độ và cao độ, đổi dấu tung độ. \\\\ Do đó ta có tọa độ điểm $C'$ là $C'(%s;%s;%s)$. \\\\ Như vậy cao độ của điểm $C'$ là $z_{C'} = %s$. \\\\ Vì $%s < %s$ nên khẳng định cao độ lớn hơn $%s$ là sai."""
        % (
            xc,
            yc,
            zc,
            xc,
            -yc,
            zc,
            zc,
            zc,
            bound_zc,
            bound_zc,
        )
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Điểm K sao cho A là trọng tâm của tam giác KBG thì K(xk; yk; zk)[cite: 24]
    vdc_da_1_d = (
        "\\True Điểm $K$ sao cho $A$ là trọng tâm của tam giác $KBG$ thì $K(%s;%s;%s)$"
        % (xk, yk, zk)
    )
    vdc_da_1_s = (
        "Điểm $K$ sao cho $A$ là trọng tâm của tam giác $KBG$ thì $K(%s;%s;%s)$"
        % (xk_s, yk_s, zk_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì điểm $A$ là trọng tâm của tam giác $KBG$ nên tọa độ của điểm $A$ thỏa mãn: \\\\ $\\begin{cases} x_A = \\frac{x_K + x_B + x_G}{3} \\\\ y_A = \\frac{y_K + y_B + y_G}{3} \\\\ z_A = \\frac{z_K + z_B + z_G}{3} \\end{cases} \\Leftrightarrow \\begin{cases} x_K = 3x_A - x_B - x_G = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ y_K = 3y_A - y_B - y_G = 3 \\cdot (%s) - (%s) - (%s) = %s \\\\ z_K = 3z_A - z_B - z_G = 3 \\cdot (%s) - (%s) - (%s) = %s \\end{cases}$ \\\\ Suy ra tọa độ điểm $K$ là $K(%s;%s;%s)$."""
        % (
            xa,
            xb,
            xg,
            xk,
            ya,
            yb,
            yg,
            yk,
            za,
            zb,
            zg,
            zk,
            xk,
            yk,
            zk,
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
    