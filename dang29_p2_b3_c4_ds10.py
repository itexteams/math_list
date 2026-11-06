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


def bt_dang29_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến sympy
            x = symbols('x')

            # --- BƯỚC 1: RANDOM CÁC THAM SỐ TOÁN HỌC ---
            # Chọn x1, x2 sao cho khoảng cách là số chẵn để đỉnh parabol là số nguyên
            x1 = randint(1, 3)
            khoang_cach = randint(1, 2) * 2  # 2 hoặc 4
            x2 = x1 + khoang_cach
            tong = x1 + x2
            tich = x1 * x2
            d = khoang_cach // 2 # Giá trị lớn nhất của t = sqrt((x-x1)(x2-x))

            # Hệ số của căn thức (k)
            k = 2 

            # Thiết lập hằng số V sao cho t^2 + kt + V >= m^2 có V là số chính phương
            # Điều này giúp việc tìm số giá trị nguyên của m (m^2 <= V) trở nên đẹp (2*sqrt(V) + 1)
            v_root = randint(3, 5) # Căn bậc hai của V (ví dụ 3, 4, 5)
            V = v_root**2
            # Tính hằng số C trong đề bài: -x^2 + (x1+x2)x + C = t^2 + V
            # Vì t^2 = -x^2 + (x1+x2)x - x1*x2 => -x^2 + (x1+x2)x = t^2 + x1*x2
            # Suy ra: (t^2 + x1*x2) + C = t^2 + V => C = V - x1*x2
            C = V - tich

            # --- BƯỚC 2: NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r'''Cho bất phương trình $%s\sqrt{(x-%s)(%s-x)} - x^2 + %sx - m^2 + %s \ge 0$. ''' 
                             % (latex(k), latex(x1), latex(x2), latex(tong), latex(C)))

            ########################################################################
            # a) Nhận biết: Điều kiện xác định
            ########################################################################
            nb_da_1_d = r'\True Điều kiện xác định của bất phương trình là $%s \le x \le %s$' % (latex(x1), latex(x2))
            nb_da_1_s = r'Điều kiện xác định của bất phương trình là $x \in (%s; %s)$' % (latex(x1), latex(x2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Điều kiện xác định của bất phương trình là biểu thức dưới dấu căn không âm: \\
            $(x-%s)(%s-x) \ge 0 \Leftrightarrow %s \le x \le %s$.''' % (latex(x1), latex(x2), latex(x1), latex(x2)))

            ########################################################################
            # b) Thông hiểu: Đặt ẩn phụ và tập giá trị t
            ########################################################################
            th_da_1_d = r'\True Đặt $t = \sqrt{(x-%s)(%s-x)}$, khi đó $t \in [0; %s]$' % (latex(x1), latex(x2), latex(d))
            th_da_1_s = r'Đặt $t = \sqrt{(x-%s)(%s-x)}$, khi đó $t \in [0; %s]$' % (latex(x1), latex(x2), latex(khoang_cach))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Đặt $t = \sqrt{(x-%s)(%s-x)} = \sqrt{-x^2 + %sx - %s}$. \\
            Xét hàm số $g(x) = -x^2 + %sx - %s$ trên đoạn $[%s; %s]$. \\
            Hàm số đạt giá trị lớn nhất tại đỉnh $x = \frac{%s+%s}{2} = %s$. \\
            Giá trị lớn nhất $g(%s) = %s$. Do đó $0 \le t \le \sqrt{%s} = %s$.''' 
                            % (latex(x1), latex(x2), latex(tong), latex(tich), latex(tong), latex(tich), 
                               latex(x1), latex(x2), latex(x1), latex(x2), latex((x1+x2)/2), 
                               latex((x1+x2)/2), latex(d**2), latex(d**2), latex(d)))

            ########################################################################
            # c) Vận dụng: Biến đổi bất phương trình
            ########################################################################
            vd_da_1_d = r'\True Bất phương trình đã cho tương đương với $t^2 + %st + %s \ge m^2$' % (latex(k), latex(V))
            vd_da_1_s = r'Bất phương trình đã cho tương đương with $t^2 + %st + %s \ge m^2$' % (latex(k), latex(V + randint(1,3)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Ta có $t^2 = -x^2 + %sx - %s \Rightarrow -x^2 + %sx = t^2 + %s$. \\
            Thay vào bất phương trình ta được: \\
            $%st + (t^2 + %s) - m^2 + %s \ge 0 \Leftrightarrow t^2 + %st + %s \ge m^2$.''' 
                            % (latex(tong), latex(tich), latex(tong), latex(tich), 
                               latex(k), latex(tich), latex(C), latex(k), latex(V)))

            ########################################################################
            # d) Vận dụng cao: Tìm số giá trị nguyên của m
            ########################################################################
            so_luong_m = 2 * v_root + 1
            vdc_da_1_d = r'\True Có %s giá trị nguyên của tham số $m$ để bất phương trình nghiệm đúng với mọi $x \in [%s; %s]$' % (latex(so_luong_m), latex(x1), latex(x2))
            vdc_da_1_s = r'Có %s giá trị nguyên của tham số $m$ để bất phương trình nghiệm đúng với mọi $x \in [%s; %s]$' % (latex(so_luong_m + 2), latex(x1), latex(x2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Để bất phương trình nghiệm đúng với mọi $x \in [%s; %s]$, tức là đúng với mọi $t \in [0; %s]$, thì: \\
            $m^2 \le \min_{t \in [0; %s]} (t^2 + %st + %s)$. \\
            Xét hàm số $f(t) = t^2 + %st + %s$ trên đoạn $[0; %s]$. \\
            Vì $a=1>0$ và đỉnh $t = -%s < 0$ nên hàm số đồng biến trên $[0; %s]$. \\
            Suy ra $\min f(t) = f(0) = %s$. \\
            Do đó $m^2 \le %s \Leftrightarrow -%s \le m \le %s$. \\
            Vì $m \in \mathbb{Z}$ nên $m \in \{-%s; \dots; %s\}$. Vậy có $%s$ giá trị nguyên.''' 
                             % (latex(x1), latex(x2), latex(d), latex(d), latex(k), latex(V), 
                                latex(k), latex(V), latex(d), latex(k//2), latex(d), 
                                latex(V), latex(V), latex(v_root), latex(v_root), 
                                latex(v_root), latex(v_root), latex(so_luong_m)))

            # --- BƯỚC 3: XỬ LÝ LỰA CHỌN ĐÚNG/SAI ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                current_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # --- BƯỚC 4: XUẤT NỘI DUNG (KHÔNG DÙNG TIỀN TỐ r TRONG PHẦN content) ---
            content = ('\\begin{minipage}{\\textwidth} \n' +
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n' +
                '{' + str(nb_sel) + '}\n' +
                '{' + str(th_sel) + '}\n' +
                '{' + str(vd_sel) + '}\n' +
                '{' + str(vdc_sel) + '}\n' +
                '\\loigiai{ \n' +
                '\\begin{enumEX}[a)]{1} \n' +
                '\\item ' + str(loigiai_nb_1) + '\n' +
                '\\item ' + str(loigiai_th_1) + '\n' +
                '\\item ' + str(loigiai_vd_1) + '\n' +
                '\\item ' + str(loigiai_vdc_1) + '\n' +
                '\\end{enumEX}} \n' +
                '\\end{ex}\n \\end{minipage} \n\n').replace('+ -','-')
            return content

