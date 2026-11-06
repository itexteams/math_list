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


def bt_dang33_p2_b1_c3_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ: Đổi dấu chấm thành dấu phẩy cho số thập phân và biểu thức LaTeX
            def fix_num(val):
                # Lấy chuỗi latex hoặc string
                s = latex(val) if not isinstance(val, str) else val
                # Thay thế dấu chấm bằng dấu phẩy
                return s.replace('.', ',')

            # ==============================================================================
            # BƯỚC 1, 2, 3: THIẾT LẬP VÀ RANDOM HÓA BÀI TOÁN
            # ==============================================================================

            # Khai báo biến thời gian
            t = symbols('t')

            # --- Random số liệu đầu vào ---
            # Chọn vận tốc ban đầu v0 (m/s)
            v0 = random.choice([10, 12, 15, 16, 18, 20, 22, 24, 25, 30]) 

            # Chọn gia tốc hãm a (m/s^2)
            accel_candidates = [a for a in [2, 3, 4, 5, 6, 8, 10] if v0 % a == 0]
            if not accel_candidates: accel_candidates = [2, 5]
            accel = random.choice(accel_candidates)

            # Tính toán vận tốc km/h
            v0_kmh = v0 * 3.6
            # Xử lý hiển thị km/h (nếu tròn thì bỏ .0, nếu lẻ thì thay . bằng ,)
            if v0_kmh.is_integer():
                v0_kmh_str = str(int(v0_kmh))
            else:
                v0_kmh_str = fix_num(round(v0_kmh, 1))

            # Thời gian phản ứng (giây) - đảm bảo định dạng phẩy
            t_react_val = random.choice([0.5, 0.75, 1, 1.25, 1.5])
            t_react = fix_num(t_react_val)

            # Biểu thức vận tốc: v(t) = -at + v0
            vt_expr = -accel * t + v0

            # Biểu thức quãng đường s(t)
            st_expr = sp.integrate(vt_expr, t) 

            # --- Tính toán thông số ---
            time_stop = sp.solve(vt_expr, t)[0] # Thời gian dừng
            dist_braking = st_expr.subs(t, time_stop) # Quãng đường phanh
            dist_react = v0 * t_react_val # Quãng đường phản ứng
            dist_total_needed = dist_braking + dist_react # Tổng quãng đường cần để dừng

            # Khoảng cách chướng ngại vật
            delta = random.choice([-10, -5, -2, 2, 5, 10, 15]) 
            dist_obstacle_val = float(dist_total_needed) + delta
            # Xử lý hiển thị khoảng cách (nếu là số nguyên thì in nguyên, float thì in phẩy)
            if dist_obstacle_val.is_integer():
                dist_obstacle = str(int(dist_obstacle_val))
            else:
                dist_obstacle = fix_num(round(dist_obstacle_val, 1))

            is_collision = dist_total_needed >= dist_obstacle_val

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (
                '''Một xe ô tô đang chạy với tốc độ $%s$ km/h (tương đương $%s$ m/s) thì người lái xe bất ngờ phát hiện chướng ngại vật 
                trên đường cách đó $%s m$. Người lái xe phản ứng mất $%s$ giây, sau đó đạp phanh khẩn cấp. Kể từ thời điểm 
                này, ô tô chuyển động chậm dần đều với tốc độ $v(t) = %s$ (m/s), trong đó $t$ là thời gian tính bằng 
                giây kể từ lúc đạp phanh. Gọi $s(t)$ là quãng đường xe ô tô đi được trong $t$ (giây) kể từ lúc đạp phanh.''' 
                % (v0_kmh_str, fix_num(v0), dist_obstacle, t_react, fix_num(vt_expr))
            )

            # ==============================================================================
            # NHẬN BIẾT (NB)
            # ==============================================================================
            # Lưu ý: Đã bỏ dấu chấm (.) ở cuối câu
            nb_da_1_d = '\\True Quãng đường $s(t)$ mà xe ô tô đi được trong thời gian $t$ (giây) là một nguyên hàm của hàm số $v(t)$'
            nb_da_1_s = 'Đạo hàm của quãng đường $s(t)$ là một nguyên hàm của hàm số $v(t)$'

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Do $s'(t) = v(t)$ nên quãng đường $s(t)$ mà xe ô tô đi được trong thời gian $t$ (giây) là một nguyên hàm của hàm số $v(t)$.''')
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            # ==============================================================================
            # THÔNG HIỂU (TH)
            # ==============================================================================
            # Lưu ý: Đã bỏ dấu chấm (.) ở cuối câu
            th_da_1_d = '\\True $s(t) = %s$' % fix_num(st_expr)

            st_expr_wrong_1 = sp.integrate(-accel*t - v0, t)
            st_expr_wrong_2 = sp.integrate(accel*t + v0, t)
            th_da_1_s = random.choice(['$s(t) = %s$' % fix_num(st_expr_wrong_1), '$s(t) = %s$' % fix_num(st_expr_wrong_2)])

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta có $\\displaystyle \\int v(t) \\text{d}t = \\int (%s) \\text{d}t = %s + C$. 
            Vì $s(0)=0$ nên $C=0$. Suy ra $s(t) = %s$.''' % (fix_num(vt_expr), fix_num(st_expr), fix_num(st_expr)))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            # ==============================================================================
            # VẬN DỤNG (VD)
            # ==============================================================================
            # Lưu ý: Đã bỏ dấu chấm (.) ở cuối câu
            vd_da_1_d = '\\True Thời gian kể từ lúc đạp phanh đến khi xe ô tô dừng hẳn là $%s$ giây' % fix_num(time_stop)

            time_wrong = time_stop + random.choice([1, 2, 5])
            vd_da_1_s = 'Thời gian kể từ lúc đạp phanh đến khi xe ô tô dừng hẳn là $%s$ giây' % fix_num(time_wrong)

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Xe dừng hẳn khi $v(t)=0 \\Leftrightarrow %s = 0 \\Leftrightarrow t = %s$. 
            Vậy thời gian kể từ lúc đạp phanh đến khi xe ô tô dừng hẳn là $%s$ giây.''' 
            % (fix_num(vt_expr), fix_num(time_stop), fix_num(time_stop)))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            # ==============================================================================
            # VẬN DỤNG CAO (VDC)
            # ==============================================================================
            # Lưu ý: Đã bỏ dấu chấm (.) ở cuối câu
            if not is_collision:
                vdc_da_1_d = '\\True Xe ô tô đó không va vào chướng ngại vật ở trên đường'
                vdc_da_1_s = 'Xe ô tô đó sẽ va chạm với chướng ngại vật'
                conclusion_text = "không va chạm"
                compare_sign = "<"
            else:
                vdc_da_1_d = '\\True Xe ô tô đó sẽ va chạm với chướng ngại vật ở trên đường'
                vdc_da_1_s = 'Xe ô tô đó dừng lại trước khi va vào chướng ngại vật'
                conclusion_text = "va chạm"
                compare_sign = "\\ge"

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Quãng đường xe đi được trong thời gian phản ứng ($%s$ giây) là: $s_1 = v_0 \\cdot t = %s \\cdot %s = %s$ (m).
            Quãng đường xe đi được từ lúc đạp phanh đến khi dừng hẳn ($t=%s$) là: $s_2 = s(%s) = %s$ (m).
            Tổng quãng đường xe đi được kể từ lúc phát hiện chướng ngại vật là: $S = s_1 + s_2 = %s + %s = %s$ (m).
            Vì $%s %s %s$ nên xe ô tô %s với chướng ngại vật.''' 
            % (t_react, fix_num(v0), t_react, fix_num(dist_react),
               fix_num(time_stop), fix_num(time_stop), fix_num(dist_braking),
               fix_num(dist_react), fix_num(dist_braking), fix_num(dist_total_needed),
               fix_num(dist_total_needed), compare_sign, dist_obstacle, conclusion_text))

            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # ==============================================================================
            # LOGIC RANDOM
            # ==============================================================================
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            shuffled_answers_nb = [nb_da_1]
            shuffled_answers_th = [th_da_1]
            shuffled_answers_vd = [vd_da_1]
            shuffled_answers_vdc = [vdc_da_1]

            # ==============================================================================
            # XUẤT NỘI DUNG
            # ==============================================================================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage}'
                '\n\n')
            return content

