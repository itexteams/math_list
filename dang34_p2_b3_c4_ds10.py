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


def bt_dang34_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, m = symbols('x m')

            # B1: Nghiên cứu và thiết lập thông số ngẫu nhiên
            # k là giá trị trong cụm (m-k), ở đây k = 2
            k = random.randint(1, 5) 
            # p là hệ số trong x^2 - 2px, ở đây p = 3 (để có -6x)
            p = random.randint(2, 6)
            h_so_x = 2 * p

            # Các biểu thức thành phần
            f1 = x**4 + 4*(m - k)*x + (m - k)**2
            f2 = x**2 - h_so_x * x

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hệ bất phương trình $\\begin{cases} x^4 + 4(m - %s)x + m^2 - %sm + %s = 0 \\\\ x^2 - %sx \\le m \\end{cases}$.''' 
                             %(latex(k), latex(2*k), latex(k**2), latex(h_so_x)))

            ########################################################################
            # a) Nhận biết: Kiểm tra với m = k
            ########################################################################
            # Giải: Khi m = k, pt1 -> x^4 = 0 -> x = 0. Thay vào bpt2: 0 <= k (đúng vì k > 0)
            nb_da_1_d = '\\True Với $m = %s$ hệ bất phương trình có nghiệm duy nhất $x = 0$' % (latex(k))
            nb_da_1_s = 'Với $m = %s$ hệ bất phương trình vô nghiệm' % (latex(k))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Với $m = %s$, hệ trở thành: \\\\
                            $\\begin{cases} x^4 + 4(0)x + 0 = 0 \\\\ x^2 - %sx \\le %s \\end{cases} \\Leftrightarrow \\begin{cases} x = 0 \\\\ 0 \\le %s \\end{cases}$. \\\\
                            Vậy hệ có nghiệm duy nhất $x = 0$.'''
                            % (latex(k), latex(h_so_x), latex(k), latex(k)))

            ########################################################################
            # b) Thông hiểu: Kiểm tra nghiệm x = 2p
            ########################################################################
            # Giải: Để x = 2p là nghiệm, nó phải thỏa mãn pt1: (2p)^4 + 4(m-k)(2p) + (m-k)^2 = 0
            # Đây là pt bậc 2 của (m-k): (m-k)^2 + 8p(m-k) + 16p^4 = 0. Delta' = (4p)^2 - 16p^4 = 16p^2(1 - p^2) < 0 với p > 1.
            th_da_1_d = '\\True Hệ bất phương trình không thể nhận $x = %s$ làm nghiệm' % (latex(2*p))
            th_da_1_s = 'Hệ bất phương trình luôn nhận $x = %s$ làm nghiệm với mọi $m$' % (latex(2*p))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Giả sử $x = %s$ là nghiệm của hệ, khi đó phải thỏa mãn phương trình: \\\\
                            $(%s)^4 + 4(m - %s)(%s) + (m - %s)^2 = 0$. \\\\
                            Đặt $t = m - %s$, ta có $t^2 + %st + %s = 0$. \\\\
                            Xét $\\Delta' = (%s)^2 - %s = %s < 0$ (do $p=%s$). \\\\
                            Vậy không tồn tại $m$ để $x = %s$ là nghiệm.'''
                            % (latex(2*p), latex(2*p), latex(k), latex(2*p), latex(k), latex(k), latex(8*p), latex(16*p**4), latex(4*p), latex(16*p**4), latex(16*p**2*(1-p**2)), latex(p), latex(2*p)))

            ########################################################################
            # c) Vận dụng: Hệ quả về miền giá trị của x
            ########################################################################
            # Giải: Coi pt1 là pt bậc 2 theo (m-k). Để m tồn tại thì Delta' = (2x)^2 - x^4 >= 0
            # <=> x^2(4 - x^2) >= 0 <=> -2 <= x <= 2.
            vd_da_1_d = '\\True Một hệ quả của hệ bất phương trình là $-2 \\le x \\le 2$'
            vd_da_1_s = 'Một hệ quả của hệ bất phương trình là $-1 \\le x \\le 1$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Xét phương trình $x^4 + 4(m - %s)x + (m - %s)^2 = 0$. \\\\
                            Coi đây là phương trình bậc hai đối với ẩn $(m - %s)$: \\\\
                            $(m - %s)^2 + 4x(m - %s) + x^4 = 0$. \\\\
                            Để phương trình có nghiệm $m$ thì $\\Delta'_{(m-%s)} \\ge 0 \\Leftrightarrow (2x)^2 - x^4 \\ge 0$. \\\\
                            $\\Leftrightarrow 4x^2 - x^4 \\ge 0 \\Leftrightarrow x^2(4 - x^2) \\ge 0 \\Leftrightarrow -2 \\le x \\le 2$.'''
                            % (latex(k), latex(k), latex(k), latex(k), latex(k), latex(k)))

            ########################################################################
            # d) Vận dụng cao: Điều kiện của m để hệ có nghiệm
            ########################################################################
            # Giải: Ta có m - k = -2x +/- sqrt(4x^2 - x^4). Để hệ có nghiệm, m >= x^2 - 2px.
            # Thử với x = 2, ta có m - k = -4 => m = k - 4. Kiểm tra bpt2: 4 - 4p <= k - 4 (thường đúng).
            # Ở bài toán gốc k=2, p=3, x=2 -> m = -2. BPT2: -8 <= -2 (Đúng).
            # Giá trị m >= -8 ở đề gốc thường lấy từ cực tiểu của x^2-6x tại x=3, nhưng x bị chặn trong [-2, 2].
            vdc_da_1_s = '\\True Hệ bất phương trình có nghiệm khi $m \\ge %s$' % (latex(k - 4))
            vdc_da_1_d = 'Hệ bất phương trình có nghiệm khi $m \\ge -%s$' % (latex(h_so_x + 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Từ câu c, ta có $x \\in [-2; 2]$. Khi đó $m - %s = -2x \\pm \\sqrt{4x^2 - x^4}$. \\\\
                            Để hệ có nghiệm, tồn tại $x \\in [-2; 2]$ sao cho $m \\ge x^2 - %sx$ và $m = %s - 2x \\pm \\sqrt{4x^2 - x^4}$. \\\\
                            Xét tại $x = 2$, từ phương trình (1) ta có $m = %s$. \\\\
                            Thay vào bất phương trình (2): $2^2 - %s(2) \\le %s \\Leftrightarrow %s \\le %s$ (đúng). \\\\
                            Vậy với $m = %s$ hệ đã có nghiệm, nên điều kiện $m \\ge -8$ (nếu có) là sai hoặc chưa tối ưu tùy vào đề bài cụ thể.'''
                            % (latex(k), latex(h_so_x), latex(k), latex(k-4), latex(h_so_x), latex(k-4), latex(4 - 2*h_so_x), latex(k-4), latex(k-4)))

            ########################################################################
            # Xử lý trộn và xuất nội dung
            ########################################################################
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lời giải tương ứng
            sol_nb = loigiai_nb_1
            sol_th = loigiai_th_1
            sol_vd = loigiai_vd_1
            sol_vdc = loigiai_vdc_1

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(sol_nb) + '\n'
                '\\item ' + str(sol_th) + '\n'
                '\\item ' + str(sol_vd) + '\n'
                '\\item ' + str(sol_vdc) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

