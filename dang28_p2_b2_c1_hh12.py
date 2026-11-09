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


def bt_dang28_p2_b2_c1_hh12(self):
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
    
    
    # Sinh ngẫu nhiên dữ liệu cho điểm A và khoảng cách OB
    while True:
        xa = random.choice([-4, -3, -2, 2, 3, 4])
        ya = random.choice([-4, -3, -2, 2, 3, 4])
        za = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
    
        ob_len = random.randint(2, 5)
    
        if xa != 0 and ya != 0 and za != 0:
            break
    
    # 1. Vectơ OA = (xa; ya; za) biểu diễn theo i, j, k
    str_oa_true = format_ijk(xa, ya, za)
    str_oa_false = format_ijk(xa, -ya, za)
    
    # 2. Điểm B nằm trên trục Oy sao cho OB = ob_len
    # Vì B thuộc Oy nên B(0; yB; 0) với |yB| = ob_len => B(0; ob_len; 0) hoặc B(0; -ob_len; 0)
    # Mệnh đề đề bài đưa ra dạng B(ob_len; 0; 0) (sai do nằm trên Ox)
    xb_s = ob_len
    yb_s = 0
    zb_s = 0
    
    # 3. Điểm M đối xứng với A(xa; ya; za) qua trục Ox:
    # Giữ nguyên x, đổi dấu y và z => M(xa; -ya; -za)
    xm_true = xa
    ym_true = -ya
    zm_true = -za
    
    xm_false = -xa
    ym_false = ya
    zm_false = za
    
    # 4. Điểm N đối xứng với A(xa; ya; za) qua mặt phẳng (Oxy):
    # Giữ nguyên x, y, đổi dấu z => N(xa; ya; -za)
    xn_true = xa
    yn_true = ya
    zn_true = -za
    
    # Dạng khẳng định sai trong đề gốc (đổi dấu x, y, giữ nguyên z):
    xn_false = -xa
    yn_false = -ya
    zn_false = za
    
    # Nội dung câu hỏi
    noidungcauhoi = (
        """Trong không gian $Oxyz$, cho điểm $A(%s;%s;%s)$, $B$ nằm trên trục $Oy$ sao cho $OB = %s$."""
        % (xa, ya, za, ob_len)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Vectơ OA biểu diễn theo các vectơ đơn vị
    nb_da_1_d = "\\True $\\vec{OA} = %s$" % (str_oa_true)
    nb_da_1_s = "$\\vec{OA} = %s$" % (str_oa_false)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Tọa độ điểm $A$ là $A(%s;%s;%s)$, suy ra $\\vec{OA} = (%s;%s;%s)$. \\\\ Do đó ta có $\\vec{OA} = %s$."""
        % (xa, ya, za, xa, ya, za, str_oa_true)
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Tọa độ điểm B
    th_da_1_d = (
        "\\True Tọa độ điểm $B$ là $B(0;%s;0)$ hoặc $B(0;%s;0)$"
        % (ob_len, -ob_len)
    )
    th_da_1_s = "Tọa độ điểm $B(%s;%s;%s)$" % (xb_s, yb_s, zb_s)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì điểm $B$ nằm trên trục $Oy$ nên tọa độ của điểm $B$ có dạng $B(0; y_B; 0)$. \\\\ Ta có $OB = |y_B| = %s \\Leftrightarrow y_B = \\pm %s$. \\\\ Do đó tọa độ điểm $B$ là $B(0;%s;0)$ hoặc $B(0;%s;0)$."""
        % (ob_len, ob_len, ob_len, -ob_len)
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Điểm M đối xứng với A qua trục Ox
    vd_da_1_d = (
        "\\True Điểm $M(%s;%s;%s)$ đối xứng với $A$ qua trục $Ox$"
        % (xm_true, ym_true, zm_true)
    )
    vd_da_1_s = (
        "Điểm $M(%s;%s;%s)$ đối xứng với $A$ qua trục $Ox$"
        % (xm_false, ym_false, zm_false)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Điểm $M$ đối xứng với $A(%s;%s;%s)$ qua trục $Ox$ sẽ giữ nguyên hoành độ và đổi dấu tung độ, cao độ. \\\\ Do đó tọa độ điểm $M$ là $M(%s;%s;%s)$."""
        % (xa, ya, za, xm_true, ym_true, zm_true)
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Tọa độ điểm N đối xứng với A qua mặt phẳng tọa độ (Oxy)
    vdc_da_1_d = (
        "\\True Tọa độ điểm $N(%s;%s;%s)$ đối xứng với $A$ qua mặt phẳng tọa độ $(Oxy)$"
        % (xn_true, yn_true, zn_true)
    )
    vdc_da_1_s = (
        "Tọa độ điểm $N(%s;%s;%s)$ đối xứng với $A$ qua mặt phẳng tọa độ $(Oxy)$"
        % (xn_false, yn_false, zn_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Điểm $N$ đối xứng với $A(%s;%s;%s)$ qua mặt phẳng tọa độ $(Oxy)$ sẽ giữ nguyên hoành độ, tung độ và đổi dấu cao độ. \\\\ Do đó tọa độ điểm $N$ đối xứng với $A$ qua $(Oxy)$ là $N(%s;%s;%s)$."""
        % (xa, ya, za, xn_true, yn_true, zn_true)
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
    