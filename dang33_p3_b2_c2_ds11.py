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


def bt_dang33_p3_b2_c2_ds11(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng phân số chứa pi chuẩn LaTeX
            def format_pi(r):
                if r == 0: return "0"
                if r == 1: return "\\pi"
                if r == -1: return "-\\pi"
                if r.q == 1: return f"{r.p}\\pi"
                if r.p == 1: return f"\\frac{{\\pi}}{{{r.q}}}"
                if r.p == -1: return f"-\\frac{{\\pi}}{{{r.q}}}"
                if r.p > 0: return f"\\frac{{{r.p}\\pi}}{{{r.q}}}"
                return f"-\\frac{{{-r.p}\\pi}}{{{r.q}}}"

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random thời điểm ban đầu (kim giờ chỉ số T1)
                T1 = random.randint(1, 5)
                # Random thời điểm gặp nhau cuối cùng trước T2 giờ
                T2 = T1 + random.randint(3, 7)
                if T2 > 12:
                    T2 = 12

                # Tính toán các giá trị bằng SymPy để giữ độ chính xác tuyệt đối
                # Khoảng cách góc ban đầu (mang dấu âm do quay theo chiều kim đồng hồ)
                r_gap_neg = Rational(-T1, 6)
                s_gap_neg = format_pi(r_gap_neg)

                # Góc alpha kim giờ quay được ở lần gặp đầu
                r_alpha = Rational(-T1, 66)
                s_alpha = format_pi(r_alpha)

                # Góc v1 kim phút quay được ở lần gặp đầu
                r_v1 = r_gap_neg + r_alpha
                s_v1 = format_pi(r_v1)

                # Góc giới hạn trước khi đến T2 giờ
                r_limit = Rational(-(T2 - T1), 6)
                s_limit = format_pi(r_limit)

                # Giải bất phương trình: u_n > limit <=> 12(n-1) < 11(T2-T1) - T1
                rhs_val = 11 * (T2 - T1) - T1
                frac_n = Rational(rhs_val, 12)

                # Xử lý chuỗi in ra cho bất phương trình
                if frac_n.q == 1:
                    str_ineq_left = "(n-1)"
                    str_ineq_right = f"{frac_n.p}"
                    str_ineq_n = f"{frac_n.p + 1}"
                else:
                    str_ineq_left = f"{frac_n.q}(n-1)"
                    str_ineq_right = f"{frac_n.p}"
                    str_ineq_n = f"\\frac{{{frac_n.p + frac_n.q}}}{{{frac_n.q}}}"

                # Số lần gặp nhau tối đa
                n_max = (rhs_val - 1) // 12 + 1

                # Công sai d' của kim phút
                r_d_prime = Rational(-24, 11)

                # Góc v_n tại lần gặp cuối
                r_vn = r_v1 + (n_max - 1) * r_d_prime
                s_vn = format_pi(r_vn)

                # Đưa về giá trị xấp xỉ và làm tròn
                approx_val = float(r_vn * math.pi)
                round_val = round(approx_val)
                abs_round_val = abs(round_val)

                # Các đáp án trắc nghiệm (lấy giá trị tuyệt đối như mẫu)
                da = abs_round_val

                # Tạo các phương án nhiễu sai khác nhau
                s_options = [da + 1, da - 1, da + 2, da - 2, da + 3, da - 3]
                random.shuffle(s_options)

                das1 = s_options[0]
                das2 = s_options[1]
                das3 = s_options[2]

                # Nội dung câu hỏi có kèm vẽ đồng hồ bằng TikZ tương ứng với thời gian T1
                noidungcauhoi = (
                    '\\immini{Trên đồng hồ, tại thời điểm buổi sáng đang xét, kim giờ chỉ số $%s$, kim phút chỉ số $12$. '
                    'Đến khi kim phút và kim giờ gặp nhau lần cuối cùng trước $%s$ giờ thì kim phút quay được '
                    'một góc lượng giác bằng bao nhiêu radian? (Kết quả làm tròn đến hàng đơn vị).}'
                    '{\\begin{tikzpicture}[line width=1pt]\n'
                    '\\draw[fill=blue!60!black] (0,0) circle (2.2);\n'
                    '\\draw[fill=cyan!30] (0,0) circle (1.9);\n'
                    '\\foreach \\x in {1,2,...,12} {\n'
                    '    \\node[font=\\sffamily\\bfseries, text=blue!80!black] at (90-\\x*30:1.4) {\\x};\n'
                    '}\n'
                    '\\fill[blue!80!black] (0,0) circle (0.1);\n'
                    '\\draw[->, >=stealth, line width=1.5pt, blue!80!black] (0,0) -- (90:1.1);\n'
                    '\\draw[->, >=stealth, line width=2.5pt, blue!80!black] (0,0) -- (90-%s*30:0.7);\n'
                    '\\end{tikzpicture}}' % (T1, T2, T1)
                )

                # Các đáp án được định dạng chuẩn
                da_d = ('\\True $%s$' % da)
                da_s1 = str('$%s$' % das1)
                da_s2 = str('$%s$' % das2) 
                da_s3 = str('$%s$' % das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = (
                    'Xét lần đầu tiên kim giờ và kim phút gặp nhau, khi đó gọi $\\alpha$ là góc lượng giác mà kim giờ đi được, '
                    'khi đó kim phút quay được một góc bằng $%s+\\alpha$. Vì kim phút quay nhanh gấp $12$ lần kim giờ nên ta có: '
                    '$%s+\\alpha=12\\alpha \\Leftrightarrow \\alpha=%s$.\\\\\n'
                    'Xét lần thứ hai kim giờ và kim phút gặp nhau, gọi $\\beta$ là góc lượng giác mà kim giờ đi được, khi đó '
                    'kim phút quay được một góc bằng $-2\\pi+\\beta$. Vì kim phút quay nhanh gấp $12$ lần kim giờ nên ta có '
                    '$-2\\pi+\\beta=12\\beta \\Leftrightarrow \\beta=-\\frac{2\\pi}{11}$.\\\\\n'
                    'Kể tại thời điểm đang xét đến các lần gặp nhau thì kim giờ tạo thành các góc lập thành cấp số cộng $(u_n)$ '
                    'với $u_1=%s$ và công sai $d=-\\frac{2\\pi}{11}$.\\\\\n'
                    'Các góc của kim phút cũng lập thành cấp số cộng $(v_n)$ với $v_1=%s+\\left(%s\\right)=%s$ và công sai '
                    '$d\'=-2\\pi+\\left(-\\frac{2\\pi}{11}\\right)=-\\frac{24\\pi}{11}$. Theo giả thiết, lần gặp nhau của hai kim '
                    'lần cuối cùng trước $%s$h nên ta có $u_n > %s \\Leftrightarrow %s+(n-1)\\left(-\\frac{2\\pi}{11}\\right) > %s '
                    '\\Leftrightarrow %s < %s \\Leftrightarrow n < %s$.\\\\\n'
                    'Khi đó lần gặp nhau cuối cùng trước $%s$h là lần thứ $%s$, lúc đó kim phút quay được một góc lượng giác '
                    'bằng $v_{%s}=v_1+(%s-1).d\'=%s+%s.\\left(-\\frac{24\\pi}{11}\\right)=%s \\approx %s$ nên quay được góc lượng '
                    'giác bằng $%s$ radian.' % (
                        s_gap_neg, s_gap_neg, s_alpha,
                        s_alpha,
                        s_gap_neg, s_alpha, s_v1,
                        T2, s_limit, s_alpha, s_limit, str_ineq_left, str_ineq_right, str_ineq_n,
                        T2, n_max,
                        n_max, n_max, s_v1, n_max - 1, s_vn, round_val, abs_round_val
                    )
                )
                dapan='\\shortans[0]{$%s$}\n'%(abs_round_val)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content 

