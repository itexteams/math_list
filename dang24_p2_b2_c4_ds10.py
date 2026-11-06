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


def bt_dang24_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # BƯỚC 1: RANDOM CÁC THÔNG SỐ CỦA BÀI TOÁN
            # Hàm số có dạng f(x) = ax^2 + (m-k)x + c
            # Để giống bài mẫu f(x) = -2x^2 + (m-1)x - 2
            a_val = -2 
            c_val = -2
            k_val = randint(1, 5) # Ngẫu nhiên hằng số trong (m-k)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số: $f(x) = %sx^2 + (m - %s)x %s$.''' 
                             % (latex(a_val), latex(k_val), latex(c_val)))

            ########################################################################
            # Nhận biết (Câu a): Đồ thị nằm hoàn toàn dưới trục hoành
            ########################################################################
            # Điều kiện: a < 0 (luôn đúng với a=-2) và Delta < 0
            # Delta = (m-k)^2 - 4ac = (m-k)^2 - 16 < 0 => |m-k| < 4 => k-4 < m < k+4
            m_min = k_val - 4
            m_max = k_val + 4

            nb_da_1_d = '\\True Đồ thị hàm số $y=f(x)$ nằm hoàn toàn phía dưới trục hoành khi $%s < m < %s$' % (latex(m_min), latex(m_max))
            nb_da_1_s = 'Đồ thị hàm số $y=f(x)$ nằm hoàn toàn phía dưới trục hoành khi $m < %s$' % (latex(m_min))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Đồ thị hàm số $y=f(x)$ nằm hoàn toàn phía dưới trục hoành $\\Leftrightarrow %sx^2 + (m-%s)x %s < 0, \\forall x \\in \\mathbb{R}$. \\\\
            $\\Leftrightarrow \\begin{cases} a = %s < 0 \\\\ \\Delta = (m-%s)^2 - 16 < 0 \\end{cases} \\Leftrightarrow (m-%s)^2 < 16 \\Leftrightarrow %s < m < %s$.'''
                            % (latex(a_val), latex(k_val), latex(c_val), latex(a_val), latex(k_val), latex(k_val), latex(m_min), latex(m_max)))

            list_nb_1 = [nb_da_1]
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu (Câu b): Tương giao và khoảng cách nghiệm
            ########################################################################
            # Phương trình: ax^2 + (m-k)x + c = x - 1 => -2x^2 + (m-k-1)x - 1 = 0
            # 2x^2 - (m - (k+1))x + 1 = 0. Giả sử k=1, phương trình là 2x^2 - (m-2)x + 1 = 0
            # Giống đề bài: (x1+x2)^2 - 2x1x2 = 4
            k_plus_1 = k_val + 1
            # Giải: ((m-k_plus_1)/2)^2 - 2(1/2) = 4 => (m-k_plus_1)^2 / 4 = 5 => (m-k_plus_1)^2 = 20
            # m^2 - 2(k+1)m + (k+1)^2 - 20 = 0. Tổng các giá trị m là 2(k+1)
            tong_m = 2 * k_plus_1

            th_da_1_d = '\\True Tổng các giá trị thực của tham số $m$ để đường thẳng $y=x-1$ cắt đồ thị tại hai điểm phân biệt có hoành độ $x_1, x_2$ thỏa mãn $x_1^2 + x_2^2 = 4$ là $%s$' % (latex(tong_m))
            th_da_1_s = 'Tổng các giá trị thực của tham số $m$ thỏa mãn yêu cầu là $%s$' % (latex(k_plus_1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Phương trình hoành độ giao điểm: $%sx^2 + (m-%s)x %s = x - 1 \\Leftrightarrow 2x^2 - (m - %s)x + 1 = 0$. \\\\
            Yêu cầu bài toán $\\Leftrightarrow \\begin{cases} \\Delta = (m-%s)^2 - 8 > 0 \\\\ (x_1+x_2)^2 - 2x_1x_2 = 4 \\end{cases} \\Leftrightarrow \\begin{cases} (m-%s)^2 > 8 \\\\ \\frac{(m-%s)^2}{4} - 2 \\cdot \\frac{1}{2} = 4 \\end{cases}$ \\\\
            $\\Leftrightarrow (m-%s)^2 = 20$ (thỏa mãn $\\Delta > 0$). \\\\
            Phương trình: $m^2 - %sm + %s = 0$. Tổng các giá trị $m$ là $%s$.'''
                            % (latex(a_val), latex(k_val), latex(c_val), latex(k_plus_1), latex(k_plus_1), latex(k_plus_1), latex(k_plus_1), latex(k_plus_1), latex(2*k_plus_1), latex(k_plus_1**2 - 20), latex(tong_m)))

            list_th_1 = [th_da_1]
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng (Câu c): Tính đơn điệu
            ########################################################################
            # Hoành độ đỉnh x_I = -(m-k)/(2a) = (m-k)/4
            # Hàm số nghịch biến trên (1; +inf) <=> x_I <= 1 => (m-k)/4 <= 1 => m <= k+4
            m_limit_c = k_val + 4

            vd_da_1_d = '\\True Hàm số nghịch biến trên khoảng $(1; +\\infty)$ khi $m \\leq %s$' % (latex(m_limit_c))
            vd_da_1_s = '\\True Hàm số nghịch biến trên khoảng $(1; +\\infty)$ khi $m \\geq %s$' % (latex(m_limit_c))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Hoành độ đỉnh của parabol là $x_I = \\frac{m-%s}{4}$. \\\\
            Vì $a = %s < 0$ nên hàm số nghịch biến trên khoảng $(x_I; +\\infty)$. \\\\
            Để hàm số nghịch biến trên $(1; +\\infty)$ thì $x_I \\leq 1 \\Leftrightarrow \\frac{m-%s}{4} \\leq 1 \\Leftrightarrow m \\leq %s$.'''
                            % (latex(k_val), latex(a_val), latex(k_val), latex(m_limit_c)))

            list_vd_1 = [vd_da_1]
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao (Câu d): Hàm chứa trị tuyệt đối
            ########################################################################
            # y = |f(x)| đồng biến trên (2; +inf)
            # TH: f(x) nghịch biến trên (2; +inf) và f(x) <= 0 trên (2; +inf)
            # 1. x_I <= 2 => (m-k)/4 <= 2 => m <= k+8
            # 2. f(2) <= 0 => a(2)^2 + (m-k)2 + c <= 0 => -8 + 2m - 2k - 2 <= 0 => 2m <= 2k + 10 => m <= k+5
            # Kết hợp: m <= k+5
            m_limit_d = k_val + 5

            vdc_da_1_d = '\\True Hàm số $y=|f(x)|$ đồng biến trên khoảng $(2; +\\infty)$ khi $m \\in (-\\infty; %s]$' % (latex(m_limit_d))
            vdc_da_1_s = 'Hàm số $y=|f(x)|$ đồng biến trên khoảng $(2; +\\infty)$ khi $m \\in [%s; +\\infty)$' % (latex(m_limit_d))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Cách vẽ đồ thị $y=|f(x)|$: Giữ phần trên trục hoành, lấy đối xứng phần dưới qua trục hoành và xóa phần dưới cũ. \\\\
            Vì đồ thị $y=f(x)$ là parabol hướng bề lõm xuống dưới nên để $y=|f(x)|$ đồng biến trên $(2; +\\infty)$ thì: \\\\
            $\\Leftrightarrow$ Hàm số $y=f(x)$ nghịch biến trên $(2; +\\infty)$ và $f(x) \\leq 0, \\forall x \\in (2; +\\infty)$. \\\\
            $\\Leftrightarrow \\begin{cases} f(2) \\leq 0 \\\\ \\frac{m-%s}{4} \\leq 2 \\end{cases} \\Leftrightarrow \\begin{cases} %s(2)^2 + (m-%s)2 %s \\leq 0 \\\\ m - %s \\leq 8 \\end{cases} \\Leftrightarrow m \\leq %s$.'''
                             % (latex(k_val), latex(a_val), latex(k_val), latex(c_val), latex(k_val), latex(m_limit_d)))

            list_vdc_1 = [vdc_da_1]
            list_vdc_2 = [loigiai_vdc_1]

            ########################################################################
            # KIỂM TRA ĐIỀU KIỆN ĐÁP ÁN ĐÚNG (1-3 câu đúng)
            ########################################################################
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

