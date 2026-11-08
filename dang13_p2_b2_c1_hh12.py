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


def bt_dang13_p2_b2_c1_hh12(self):
    # Random toạ độ các đỉnh A, B, C không thẳng hàng
    # Để trọng tâm G có toạ độ nguyên đẹp, ta chọn tổng toạ độ chia hết cho 3
    while True:
        xa, ya, za = (
            random.randint(-4, 4),
            random.randint(-4, 4),
            random.randint(-4, 4),
        )
        xb, yb, zb = (
            random.randint(-4, 4),
            random.randint(-4, 4),
            random.randint(-4, 4),
        )
    
        # Chọn toạ độ C sao cho xA+xB+xC, yA+yB+yC, zA+zB+zC chia hết cho 3
        # và yC != 0 để mệnh đề hình chiếu lên Oxz có ý nghĩa
        cand_xc = [c for c in range(-5, 6) if (xa + xb + c) % 3 == 0]
        cand_yc = [c for c in range(-5, 6) if (ya + yb + c) % 3 == 0 and c != 0]
        cand_zc = [c for c in range(-5, 6) if (za + zb + c) % 3 == 0]
    
        if not cand_xc or not cand_yc or not cand_zc:
            continue
    
        xc = random.choice(cand_xc)
        yc = random.choice(cand_yc)
        zc = random.choice(cand_zc)
    
        # Vectơ AB và AC
        ab_x, ab_y, ab_z = xb - xa, yb - ya, zb - za
        ac_x, ac_y, ac_z = xc - xa, yc - ya, zc - za
    
        # Tích có hướng [AB, AC] để kiểm tra ba điểm không thẳng hàng
        cp_x = ab_y * ac_z - ab_z * ac_y
        cp_y = ab_z * ac_x - ab_x * ac_z
        cp_z = ab_x * ac_y - ab_y * ac_x
    
        if (
            (cp_x != 0 or cp_y != 0 or cp_z != 0)
            and (xa, ya, za) != (xb, yb, zb)
            and (xa, ya, za) != (xc, yc, zc)
            and (xb, yb, zb) != (xc, yc, zc)
        ):
            break
    
    # 1. Toạ độ trọng tâm G của tam giác ABC
    xg = (xa + xb + xc) // 3
    yg = (ya + yb + yc) // 3
    zg = (za + zb + zc) // 3
    
    # 2. Tích vô hướng AB . AC
    dot_val = ab_x * ac_x + ab_y * ac_y + ab_z * ac_z
    
    # 3. Hình chiếu vuông góc của C lên mặt phẳng Oxz là C_h(xC; 0; zC)
    hc_x = xc
    hc_y = 0
    hc_z = zc
    
    # 4. Tứ giác ABDC là hình bình hành
    # Chú ý thứ tự đỉnh ABDC là hình bình hành <=> vecto AB = vecto CD
    # <=> (xB - xA; yB - ya; zB - zA) = (xD - xC; yD - yC; zD - zC)
    # <=> D = C + B - A
    xd = xb + xc - xa
    yd = yb + yc - ya
    zd = zb + zc - za
    
    # Toạ độ sai phổ biến (ví dụ nhầm sang hình bình hành ABCD: vecto AB = vecto DC => D = C + A - B)
    xd_s = xc + xa - xb
    yd_s = yc + ya - yb
    zd_s = zc + za - zb
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian với hệ trục tọa độ $Oxyz$, cho tam giác $ABC$ với $A(%s;%s;%s)$, $B(%s;%s;%s)$, $C(%s;%s;%s)$."""
        % (xa, ya, za, xb, yb, zb, xc, yc, zc)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Phát biểu a: Tọa độ trọng tâm G
    nb_da_1_d = "\\True Tọa độ trọng tâm $G$ của tam giác là $(%s;%s;%s)$" % (
        xg,
        yg,
        zg,
    )
    nb_da_1_s = "Tọa độ trọng tâm $G$ của tam giác là $(%s;%s;%s)$" % (
        xg + 1,
        yg,
        zg,
    )
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ trọng tâm $G$ của tam giác $ABC$ được tính theo công thức: \\\\ $\\begin{cases} x_G = \\frac{x_A + x_B + x_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ y_G = \\frac{y_A + y_B + y_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\\\ z_G = \\frac{z_A + z_B + z_C}{3} = \\frac{%s + (%s) + (%s)}{3} = %s \\end{cases}$ \\\\ Vậy tọa độ trọng tâm là $G(%s;%s;%s)$."""
        % (
            xa,
            xb,
            xc,
            xg,
            ya,
            yb,
            yc,
            yg,
            za,
            zb,
            zc,
            zg,
            xg,
            yg,
            zg,
        )
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Phát biểu b: Tích vô hướng AB . AC
    th_da_1_d = "\\True $\\vec{AB} \\cdot \\vec{AC} = %s$" % (dot_val)
    th_da_1_s = "$\\vec{AB} \\cdot \\vec{AC} = %s$" % (-dot_val if dot_val != 0 else 5)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Ta có $\\vec{AB} = (x_B - x_A; y_B - y_A; z_B - z_A) = (%s;%s;%s)$ \\\\ và $\\vec{AC} = (x_C - x_A; y_C - y_A; z_C - z_A) = (%s;%s;%s)$. \\\\ Suy ra: \\\\ $\\vec{AB} \\cdot \\vec{AC} = (%s) \\cdot (%s) + (%s) \\cdot (%s) + (%s) \\cdot (%s) = %s$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            ac_x,
            ac_y,
            ac_z,
            ab_x,
            ac_x,
            ab_y,
            ac_y,
            ab_z,
            ac_z,
            dot_val,
        )
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Phát biểu c: Hình chiếu vuông góc của C trên mặt phẳng Oxz
    vd_da_1_d = (
        "\\True Hình chiếu vuông góc của $C$ trên mặt phẳng $Oxz$ là điểm $(%s;0;%s)$"
        % (hc_x, hc_z)
    )
    vd_da_1_s = (
        "Hình chiếu vuông góc của $C$ trên mặt phẳng $Oxz$ là điểm $(%s;%s;0)$"
        % (hc_x, yc)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Hình chiếu vuông góc của điểm $C(%s;%s;%s)$ lên mặt phẳng toạ độ $Oxz$ giữ nguyên hoành độ và cao độ, tung độ bằng $0$. \\\\ Do đó hình chiếu vuông góc của $C$ trên mặt phẳng $Oxz$ là điểm $(%s;0;%s)$."""
        % (xc, yc, zc, hc_x, hc_z)
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Phát biểu d: Tứ giác ABDC là hình bình hành
    vdc_da_1_d = (
        "\\True Nếu $ABDC$ là hình bình hành thì tọa độ điểm $D$ là $(%s;%s;%s)$"
        % (xd, yd, zd)
    )
    vdc_da_1_s = (
        "Nếu $ABDC$ là hình bình hành thì tọa độ điểm $D$ là $(%s;%s;%s)$"
        % (xd_s, yd_s, zd_s)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Gọi tọa độ điểm $D$ là $D(x_D; y_D; z_D)$. \\\\ Vì $ABDC$ là hình bình hành nên ta có $\\vec{AB} = \\vec{CD}$. \\\\ Mà $\\vec{AB} = (%s;%s;%s)$ và $\\vec{CD} = (x_D - (%s); y_D - (%s); z_D - (%s))$. \\\\ Do đó ta có hệ phương trình: \\\\ $\\begin{cases} x_D - (%s) = %s \\\\ y_D - (%s) = %s \\\\ z_D - (%s) = %s \\end{cases} \\Leftrightarrow \\begin{cases} x_D = %s + (%s) = %s \\\\ y_D = %s + (%s) = %s \\\\ z_D = %s + (%s) = %s \\end{cases}$ \\\\ Vậy tọa độ điểm $D$ là $(%s;%s;%s)$."""
        % (
            ab_x,
            ab_y,
            ab_z,
            xc,
            yc,
            zc,
            xc,
            ab_x,
            yc,
            ab_y,
            zc,
            ab_z,
            xc,
            ab_x,
            xd,
            yc,
            ab_y,
            yd,
            zc,
            ab_z,
            zd,
            xd,
            yd,
            zd,
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
    