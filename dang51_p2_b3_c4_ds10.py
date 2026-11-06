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


def bt_dang51_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # ==============================================================================
            # HÀM TẠO BẢNG XÉT DẤU ĐƠN GIẢN (2 DÒNG - DÙNG CHO CÂU HỎI)
            # ==============================================================================
            def tao_bang_don_gian(k, den_roots, is_correct=True):
                roots = sorted([k] + den_roots)
                p1, p2, p3 = roots[0], roots[1], roots[2]

                # Tính dấu f(x)
                test_pts = [p1 - 0.5, (p1 + p2)/2, (p2 + p3)/2, p3 + 0.5]
                fx_s, fx_l = [], []

                for tp in test_pts:
                    val = (tp - k) / ((tp - den_roots[0]) * (tp - den_roots[1]))
                    sign = "+" if val > 0 else "-"
                    if not is_correct: sign = "+" if sign == "-" else "-"
                    fx_s.append(sign)

                for p in roots:
                    fx_l.append("||" if p in den_roots else "0")

                tikz = (
                    "\\begin{tikzpicture}\n"
                    "\\tkzTabInit[lgt=1.2,espcl=2.0]{$x$/1, $f(x)$/1}{$-\\infty$, $%s$, $%s$, $%s$, $+\\infty$}\n"
                    "\\tkzTabLine{ , %s, %s, %s, %s, %s, %s, %s, }\n"
                    "\\end{tikzpicture}"
                    % (latex(p1), latex(p2), latex(p3), 
                       fx_s[0], fx_l[0], fx_s[1], fx_l[1], fx_s[2], fx_l[2], fx_s[3])
                )
                return tikz

            # ==============================================================================
            # HÀM TẠO BẢNG XÉT DẤU CHI TIẾT (4 DÒNG - DÙNG CHO LỜI GIẢI)
            # ==============================================================================
            def tao_bang_chi_tiet(k, den_roots):
                roots = sorted([k] + den_roots)
                p1, p2, p3 = roots[0], roots[1], roots[2]
                ts_lbl = latex(x - k)
                ms_lbl = latex(expand((x - den_roots[0]) * (x - den_roots[1])))

                test_pts = [p1 - 0.5, (p1 + p2)/2, (p2 + p3)/2, p3 + 0.5]
                ts_s, ms_s, fx_s = [], [], []
                ts_l, ms_l, fx_l = [], [], []

                for tp in test_pts:
                    v_ts = tp - k
                    v_ms = (tp - den_roots[0]) * (tp - den_roots[1])
                    ts_s.append("+" if v_ts > 0 else "-")
                    ms_s.append("+" if v_ms > 0 else "-")
                    fx_s.append("+" if (v_ts * v_ms) > 0 else "-")

                for p in roots:
                    ts_l.append("0" if p == k else "|")
                    ms_l.append("0" if p in den_roots else "|")
                    fx_l.append("||" if p in den_roots else "0")

                tikz = (
                    "\\begin{tikzpicture}\n"
                    "\\tkzTabInit[lgt=2.5,espcl=2.0]{$x$/1, $%s$/1, $%s$/1, $f(x)$/1}{$-\\infty$, $%s$, $%s$, $%s$, $+\\infty$}\n"
                    "\\tkzTabLine{ , %s, %s, %s, %s, %s, %s, %s, }\n"
                    "\\tkzTabLine{ , %s, %s, %s, %s, %s, %s, %s, }\n"
                    "\\tkzTabLine{ , %s, %s, %s, %s, %s, %s, %s, }\n"
                    "\\end{tikzpicture}"
                    % (ts_lbl, ms_lbl, latex(p1), latex(p2), latex(p3),
                       ts_s[0], ts_l[0], ts_s[1], ts_l[1], ts_s[2], ts_l[2], ts_s[3],
                       ms_s[0], ms_l[0], ms_s[1], ms_l[1], ms_s[2], ms_l[2], ms_s[3],
                       fx_s[0], fx_l[0], fx_s[1], fx_l[1], fx_s[2], fx_l[2], fx_s[3])
                )
                return tikz

            # ==============================================================================
            # VÒNG LẶP RANDOM ĐỀ BÀI
            # ==============================================================================
            while True:
                k = randint(-5, 5)
                while True:
                    x1, x2 = randint(-7, 7), randint(-7, 7)
                    if x1 != x2 and x1 != k and x2 != k: break

                tu_so, mau_so = x - k, expand((x - x1) * (x - x2))
                noidungcauhoi = "Cho biểu thức $f(x) = \\dfrac{%s}{%s}$." % (latex(tu_so), latex(mau_so))
                pts = sorted([k, x1, x2])
                p1, p2, p3 = pts[0], pts[1], pts[2]

                # a) Nhận biết
                nb_da_1_d = "\\True $f(x)=0 \\Leftrightarrow x=%s$" % latex(k)
                nb_da_1_s = "$f(x)=0 \\Leftrightarrow \\left[ \\begin{aligned} x &= %s \\\\ x &= %s \\end{aligned} \\right.$" % (latex(x1), latex(x2))
                nb_da_1 = random.choice([nb_da_1_d, nb_da_1_s])
                loigiai_nb_1 = "Ta có $f(x)=0 \\Leftrightarrow %s = 0 \\Leftrightarrow x = %s$." % (latex(tu_so), latex(k))

                # b) Thông hiểu (Câu hỏi dùng bảng đơn giản, Lời giải dùng bảng chi tiết)
                th_da_1_d = "\\True Bảng xét dấu của biểu thức là: \\\\ %s" % tao_bang_don_gian(k, [x1, x2], True)
                th_da_1_s = "Bảng xét dấu của biểu thức là: \\\\ %s" % tao_bang_don_gian(k, [x1, x2], False)
                th_da_1 = random.choice([th_da_1_d, th_da_1_s])
                loigiai_th_1 = "Ta có bảng xét dấu chi tiết của biểu thức: \\\\ %s" % tao_bang_chi_tiet(k, [x1, x2])

                # c) & d) Vận dụng
                s_neg = "$x \\in (-\\infty; %s) \\cup (%s; %s)$" % (latex(p1), latex(p2), latex(p3))
                s_pos = "$x \\in (%s; %s) \\cup (%s; +\\infty)$" % (latex(p1), latex(p2), latex(p3))

                vd_da_1_d = "\\True với %s thì $f(x) < 0$" % s_neg
                vd_da_1_s = "với %s thì $f(x) < 0$" % s_pos
                vd_da_1 = random.choice([vd_da_1_d, vd_da_1_s])
                loigiai_vd_1 = "Từ bảng xét dấu, $f(x) < 0$ khi %s." % s_neg

                vdc_da_1_d = "\\True $f(x) > 0$ khi %s" % s_pos
                vdc_da_1_s = "$f(x) > 0$ khi %s" % s_neg
                vdc_da_1 = random.choice([vdc_da_1_d, vdc_da_1_s])
                loigiai_vdc_1 = "Từ bảng xét dấu, $f(x) > 0$ khi %s." % s_pos

                if 1 <= sum('\\True' in a for a in [nb_da_1, th_da_1, vd_da_1, vdc_da_1]) <= 3: break

            # Chuẩn bị dữ liệu cho mẫu xuất
            shuffled_answers_nb, shuffled_solutions_nb = [nb_da_1], [loigiai_nb_1]
            shuffled_answers_th, shuffled_solutions_th = [th_da_1], [loigiai_th_1]
            shuffled_answers_vd, shuffled_solutions_vd = [vd_da_1], [loigiai_vd_1]
            shuffled_answers_vdc, shuffled_solutions_vdc = [vdc_da_1], [loigiai_vdc_1]

            # ==============================================================================
            # XUẤT CÂU HỎI (ĐÚNG MẪU CUỐI CỦA BẠN)
            # ==============================================================================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers_nb[0]) + '}\n'
                '{' + str(shuffled_answers_th[0]) + '}\n'
                '{' + str(shuffled_answers_vd[0]) + '}\n'
                '{' + str(shuffled_answers_vdc[0]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

