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


def bt_dang12_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m = symbols('m')

            # B1: Khởi tạo tham số ngẫu nhiên
            # f(x) = x^2 - 2(m + k)x + c
            k_val = random.randint(1, 3) 
            c_val = random.randint(-5, -1)
            x_start = random.randint(4, 6) # Ngẫu nhiên đầu khoảng đồng biến để m_max thay đổi
            x_end = 2024

            # Nội dung câu hỏi
            noidungcauhoi = ("Cho hàm số $f(x) = x^2 - 2(m + %s)x %s$ với $m$ là tham số." 
                             % (latex(k_val), latex(c_val)))

            ########################################################################
            # Nhận biết
            ########################################################################
            m_0 = 0
            truc_dx_0 = m_0 + k_val
            nb_da_1_d = "\\True Với $m = %s$, hàm số đồng biến trên khoảng $(%s; +\\infty)$ và nghịch biến trên khoảng $(-\\infty; %s)$" % (m_0, truc_dx_0, truc_dx_0)
            nb_da_1_s = "Với $m = %s$, hàm số nghịch biến trên khoảng $(%s; +\\infty)$ và đồng biến trên khoảng $(-\\infty; %s)$" % (m_0, truc_dx_0, truc_dx_0)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ("Với $m = %s$, hàm số có dạng $f(x) = x^2 - %sx %s$. Trục đối xứng của đồ thị hàm số là $x = -\\frac{b}{2a} = %s$. Vì hệ số $a = 1 > 0$ nên hàm số đồng biến trên khoảng $(%s; +\\infty)$ và nghịch biến trên khoảng $(-\\infty; %s)$." 
                            % (m_0, 2*(m_0 + k_val), latex(c_val), truc_dx_0, truc_dx_0, truc_dx_0))

            ########################################################################
            # Thông hiểu
            ########################################################################
            x1, x2 = -5, -1
            th_da_1_d = "\\True Với $m = %s$, hàm số nghịch biến trên khoảng $(-\\infty; %s)$ nên $f(%s) > f(%s)$" % (m_0, truc_dx_0, x1, x2)
            th_da_1_s = "Với $m = %s$, hàm số nghịch biến trên khoảng $(-\\infty; %s)$ nên $f(%s) < f(%s)$" % (m_0, truc_dx_0, x1, x2)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ("Với $m = %s$, hàm số nghịch biến trên khoảng $(-\\infty; %s)$. Do $%s < %s < %s$ nên theo tính chất của hàm số nghịch biến ta có $f(%s) > f(%s)$." 
                            % (m_0, truc_dx_0, x1, x2, truc_dx_0, x1, x2))

            ########################################################################
            # Vận dụng
            ########################################################################
            c_da_1_d = "\\True Hàm số luôn nghịch biến trên khoảng $(-\\infty; m + %s)$ và đồng biến trên khoảng $(m + %s; +\\infty)$ với mọi $m \\in \\mathbb{R}$" % (k_val, k_val)
            c_da_1_s = "Hàm số luôn đồng biến trên khoảng $(-\\infty; m + %s)$ và nghịch biến trên khoảng $(m + %s; +\\infty)$ với mọi $m \\in \\mathbb{R}$" % (k_val, k_val)
            list_c_da_1 = [c_da_1_d, c_da_1_s]
            c_da_1 = random.choice(list_c_da_1)

            loigiai_c_1 = ("Hàm số đã cho có hệ số $a = 1 > 0$, hoành độ đỉnh là $x_I = -\\frac{b}{2a} = m + %s$. Do đó hàm số luôn nghịch biến trên khoảng $(-\\infty; m + %s)$ và đồng biến trên khoảng $(m + %s; +\\infty)$ với mọi $m \\in \\mathbb{R}$." 
                           % (k_val, k_val, k_val))

            ########################################################################
            # Vận dụng cao: Xử lý liệt kê chi tiết m
            ########################################################################
            m_max = x_start - k_val
            so_giatri = m_max if m_max > 0 else 0

            # Tạo chuỗi liệt kê chi tiết các giá trị của m: {1; 2; 3; 4}
            if so_giatri > 0:
                danh_sach_m = "; ".join(str(i) for i in range(1, m_max + 1))
                chuoi_tap_hop = "\\{" + danh_sach_m + "\\}"
                ket_luan_m = "Vì $m$ là số nguyên dương nên $m \\in %s$. Vậy có %s giá trị thỏa mãn." % (chuoi_tap_hop, so_giatri)
            else:
                ket_luan_m = "Vì $m$ là số nguyên dương nên không có giá trị $m$ nào thỏa mãn."

            vdc_da_1_d = "\\True Có %s giá trị nguyên dương của $m$ để hàm số đồng biến trên khoảng $(%s; %s)$" % (so_giatri, x_start, x_end)
            vdc_da_1_s = "Có %s giá trị nguyên dương của $m$ để hàm số đồng biến trên khoảng $(%s; %s)$" % (so_giatri + 1, x_start, x_end)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ("Hàm số đồng biến trên khoảng $(m + %s; +\\infty)$. Để hàm số đồng biến trên khoảng $(%s; %s)$ thì $(%s; %s) \\subset (m + %s; +\\infty) \\Leftrightarrow m + %s \\le %s \\Leftrightarrow m \\le %s$. %s" 
                             % (k_val, x_start, x_end, x_start, x_end, k_val, k_val, x_start, m_max, ket_luan_m))

            ########################################################################
            # Xử lý Logic và Xuất nội dung
            ########################################################################

            def count_true_answers(answers):
                return sum("\\True" in ans for ans in answers)

            while True:
                ans_a = random.choice(list_nb_da_1)
                ans_b = random.choice(list_th_da_1)
                ans_c = random.choice(list_c_da_1)
                ans_d = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([ans_a, ans_b, ans_c, ans_d]) <= 3:
                    list_ans = [ans_a, ans_b, ans_c, ans_d]
                    break

            list_sol = [loigiai_nb_1, loigiai_th_1, loigiai_c_1, loigiai_vdc_1]

            content = ("\\begin{minipage}{\\textwidth} \n"
                "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                "\\choiceTFn \n"
                "{" + str(list_ans[0]) + "}\n"
                "{" + str(list_ans[1]) + "}\n"
                "{" + str(list_ans[2]) + "}\n"
                "{" + str(list_ans[3]) + "}\n"
                "\\loigiai{ \n"
                "\\begin{enumEX}[a)]{1} \n"
                "\\item " + str(list_sol[0]) + "\n"
                "\\item " + str(list_sol[1]) + "\n"
                "\\item " + str(list_sol[2]) + "\n"
                "\\item " + str(list_sol[3]) + "\n"
                "\\end{enumEX}} \n"
                "\\end{ex}\n \\end{minipage} \n\n")
            return content

