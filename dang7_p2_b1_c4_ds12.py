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


def bt_dang7_p2_b1_c4_ds12(self):
            # Khai báo biến
            # --- HÀM HỖ TRỢ CHUYỂN DẤU CHẤM THÀNH DẤU PHẨY ---
            def vn_num(val):
                """Chuyển số thành chuỗi LaTeX và thay dấu chấm bằng dấu phẩy"""
                return str(latex(float(val))).replace('.', ',')

            # --- BƯỚC 1 & 2: KHỞI TẠO VÀ RANDOM DỮ LIỆU ---
            while True:
                p1_val = random.choice([0.6, 0.7, 0.5, 0.8])
                p2_val = random.choice([0.5, 0.4, 0.6])
                p12_val = random.choice([0.3, 0.4, 0.35])

                if p12_val < p1_val and p12_val < p2_val and (p1_val + p2_val - p12_val) <= 1:
                    break

            pA = Rational(str(p1_val))
            pB = Rational(str(p2_val))
            pAB = Rational(str(p12_val))

            pA_bar = 1 - pA
            p_AgB = pAB / pB  
            p_BgA = pAB / pA  

            p_notAB = (1 - p_AgB) * pB 
            p_AnotB = (1 - p_BgA) * pA 
            p_exactly_one = p_notAB + p_AnotB
            p_BgnotA = (pB - pAB) / pA_bar

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Một công ty truyền thông đấu thầu hai dự án. Khả năng thắng thầu của dự án thứ nhất là %s "
                "và dự án thứ hai là %s. Khả năng thắng thầu cả hai dự án là %s. "
                "Gọi $A, B$ lần lượt là biến cố thắng thầu dự án thứ nhất và dự án thứ hai."
                % (vn_num(pA), vn_num(pB), vn_num(pAB))
            )

            ########################################################################
            # NHẬN BIẾT
            ########################################################################
            is_independent = (pA * pB == pAB)
            if not is_independent:
                nb_da_1_d = "\\True $A$ và $B$ không là hai biến cố độc lập"
                nb_da_1_s = "$A$ và $B$ là hai biến cố độc lập"
            else:
                nb_da_1_d = "\\True $A$ và $B$ là hai biến cố độc lập"
                nb_da_1_s = "$A$ và $B$ không là hai biến cố độc lập"

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (
                "Ta có $P(A).P(B) = %s . %s = %s$. Vì $P(A \\cap B) = %s %s P(A).P(B)$ "
                "nên hai biến cố $A, B$ %s độc lập."
                % (vn_num(pA), vn_num(pB), vn_num(pA*pB), 
                   vn_num(pAB), "=" if is_independent else "\\neq", 
                   "là" if is_independent else "không")
            )

            ########################################################################
            # THÔNG HIỂU
            ########################################################################
            th_da_1_d = "\\True Xác suất công ty thắng thầu đúng một dự án là %s" % (vn_num(p_exactly_one))
            th_da_1_s = "Xác suất công ty thắng thầu đúng một dự án là %s" % (vn_num(p_exactly_one + Rational(1, 10)))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (
                "Gọi $C$ là biến cố công ty thắng thầu đúng một dự án suy ra $C = \\bar{A}B \\cup A\\bar{B}$. \\\\ "
                "+) $P(\\bar{A}B) = P(\\bar{A}|B).P(B) = [1 - P(A|B)].P(B) = [1 - %s].%s = %s$. \\\\ "
                "+) $P(A\\bar{B}) = P(\\bar{B}|A).P(A) = [1 - P(B|A)].P(A) = [1 - %s].%s = %s$. \\\\ "
                "Vì hai biến cố $\\bar{A}B$ và $A\\bar{B}$ xung khắc nên $P(C) = P(\\bar{A}B) + P(A\\bar{B}) = %s$."
                % (latex(p_AgB), vn_num(pB), vn_num(p_notAB), 
                   latex(p_BgA), vn_num(pA), vn_num(p_AnotB), 
                   vn_num(p_exactly_one))
            )

            ########################################################################
            # VẬN DỤNG
            ########################################################################
            vd_da_1_d = "\\True Biết công ty thắng thầu dự án thứ nhất, xác suất thắng thầu dự án thứ hai là $%s$" % (latex(p_BgA))
            vd_da_1_s = "Biết công ty thắng thầu dự án thứ nhất, xác suất thắng thầu dự án thứ hai là $%s$" % (latex(p_AgB))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (
                "Xác suất công ty thắng thầu dự án thứ hai, biết đã thắng thầu dự án thứ nhất là: \\\\ "
                "$P(B|A) = \\frac{P(A \\cap B)}{P(A)} = \\frac{%s}{%s} = %s$."
                % (vn_num(pAB), vn_num(pA), latex(p_BgA))
            )

            ########################################################################
            # VẬN DỤNG CAO (ĐÃ SỬA SANG DẠNG PHÂN SỐ RATIONAL)
            ########################################################################
            # Sử dụng latex(p_BgnotA) để nhận được \frac{a}{b} thay vì dùng vn_num()
            vdc_da_1_d = "\\True Biết công ty không thắng thầu dự án thứ nhất, xác suất thắng thầu dự án thứ hai là $%s$" % (latex(p_BgnotA))
            vdc_da_1_s = "Biết công ty không thắng thầu dự án thứ nhất, xác suất thắng thầu dự án thứ hai là $%s$" % (latex(p_BgnotA + Rational(1, 12)))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (
                "Xác suất công ty thắng thầu dự án thứ hai, biết không thắng thầu dự án thứ nhất là: \\\\ "
                "$P(B|\\bar{A}) = \\frac{P(B \\cap \\bar{A})}{P(\\bar{A})} = \\frac{P(B) - P(A \\cap B)}{1 - P(A)} = \\frac{%s - %s}{1 - %s} = %s$."
                % (vn_num(pB), vn_num(pAB), vn_num(pA), latex(p_BgnotA))
            )

            # --- XỬ LÝ ĐÁP ÁN VÀ XUẤT NỘI DUNG ---
            def count_true_answers(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shf_ans = [d1, d2, d3, d4]
                    shf_sol = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            content = (
                "\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\choiceTFn \n"
                "{" + str(shf_ans[0]) + "}\n"
                "{" + str(shf_ans[1]) + "}\n"
                "{" + str(shf_ans[2]) + "}\n"
                "{" + str(shf_ans[3]) + "}\n"
                "\\loigiai{ \n"
                "\\begin{enumEX}[a)]{1} \n"
                "\\item " + str(shf_sol[0]) + "\n"
                "\\item " + str(shf_sol[1]) + "\n"
                "\\item " + str(shf_sol[2]) + "\n"
                "\\item " + str(shf_sol[3]) + "\n"
                "\\end{enumEX}} \n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content

