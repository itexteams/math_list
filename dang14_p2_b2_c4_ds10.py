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


def bt_dang14_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Hàm bổ trợ để chuyển dấu . thành dấu , trong chuỗi số/latex
            def v_commas(val):
                return str(val).replace('.', ',')

            def l_commas(expr):
                return latex(expr).replace('.', ',')

            # Khai báo biến
            x = symbols('x')

            v0_val = random.choice([8, 10, 12])
            alpha_deg = random.choice([30, 45])
            y0_val = random.choice([0.5, 0.6, 0.8])
            d_luoi = 5
            h_luoi = 1.524

            # Chuyển sang radian để tính toán
            alpha_rad = (alpha_deg * pi / 180)

            # Tính toán các hệ số cho phương trình: y = ax^2 + bx + c
            # g = 9.8
            mau_so = 2 * (v0_val**2) * (cos(alpha_rad)**2)
            he_so_a = -9.8 / mau_so
            he_so_b = tan(alpha_rad)
            he_so_c = y0_val

            # Phương trình quỹ đạo
            pt_quydao = he_so_a * x**2 + he_so_b * x + he_so_c

            delta = he_so_b**2 - 4 * he_so_a * he_so_c
            x_xa = (-he_so_b - math.sqrt(delta)) / (2 * he_so_a)
            x_xa_val = round(float(x_xa), 2)

            # --- Nội dung câu hỏi ---
            # Lưu ý: Các tham số trong TikZ cần giữ dấu chấm để code LaTeX chạy được, 
            # nhưng text hiển thị cho học sinh sẽ dùng dấu phẩy.
            noidungcauhoi = ('''Trong môn cầu lông, khi phát cầu, người chơi cần đánh cầu qua khỏi lưới sang sân đối phương. Trong mặt phẳng $Oxy$, chọn điểm phát cầu có tọa độ $(0; y_0)$, phương trình quỹ đạo của cầu là $y = \\frac{-9,8x^2}{2v_0^2 \\cos^2 \\alpha} + (\\tan \\alpha)x + y_0$. Giả sử góc phát cầu là $%s^\\circ$, vận tốc ban đầu là $%s$ m/s và khoảng cách phát cầu đến mặt đất là $%s$ m. \\\\
                             \\begin{center} \\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
                             \\draw[->] (-1,0) -- (10,0) node[below] {$x$};
                             \\draw[->] (0,-1) -- (0,4) node[left] {$y$};
                             \\draw[dashed] (0,%s) node[left]{$%s$} -- (0.5,%s);
                             \\draw[shift={(%s,0)}] (0,0) node[below]{%s} -- (0,%s) node[above]{Lưới};
                             \\draw[domain=0:%s, color=blue, thick] plot (\\x, {%s*(\\x)^2 + %s*\\x + %s});
                             \\filldraw[red] (%s,0) circle (1.5pt) node[below]{Chạm đất};
                             \\end{tikzpicture} \\end{center}''' 
                             % (v_commas(alpha_deg), v_commas(v0_val), v_commas(y0_val), y0_val, v_commas(y0_val), y0_val, d_luoi, d_luoi, h_luoi, x_xa_val, float(he_so_a), float(he_so_b), float(he_so_c), x_xa_val ))

            ########################################################################
            # a) Nhận biết: Phương trình quỹ đạo
            ########################################################################
            pt_hien_thi = pt_quydao.evalf(3)
            nb_da_1_d = '\\True Phương trình quỹ đạo của quả cầu là $y = %s$' % l_commas(pt_hien_thi)
            nb_da_1_s = 'Phương trình quỹ đạo của quả cầu là $y = %s$' % l_commas(pt_hien_thi + 0.5*x)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Với $v_0 = %s$ m/s, $\\alpha = %s^\\circ$, $y_0 = %s$ m, ta có phương trình: \\\\ $y = \\frac{-9,8x^2}{2 \\cdot %s^2 \\cdot \\cos^2 %s^\\circ} + \\tan %s^\\circ \\cdot x + %s = %s$.''' 
                            % (v_commas(v0_val), v_commas(alpha_deg), v_commas(y0_val), v_commas(v0_val), v_commas(alpha_deg), v_commas(alpha_deg), v_commas(y0_val), l_commas(pt_hien_thi)))

            ########################################################################
            # b) Thông hiểu: Tầm bay cao (Đỉnh Parabol)
            ########################################################################
            x_dinh = -he_so_b / (2 * he_so_a)
            y_max = pt_quydao.subs(x, x_dinh)
            y_max_val = round(float(y_max), 2)

            th_da_1_d = '\\True Tầm bay cao của quả cầu là $%s$ m' % v_commas(y_max_val)
            th_da_1_s = 'Tầm bay cao của quả cầu là $%s$ m' % v_commas(round(y_max_val + 1, 2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Quả cầu đạt vị trí cao nhất tại đỉnh của Parabol. Tọa độ đỉnh $x = -\\frac{b}{2a} \\approx %s$. Khi đó $y_{max} \\approx %s$ m. Vậy tầm bay cao là %s m.''' 
                            % (v_commas(round(float(x_dinh), 2)), v_commas(y_max_val), v_commas(y_max_val)))

            ########################################################################
            # c) Vận dụng: Tầm bay xa (y = 0)
            ########################################################################
            delta = he_so_b**2 - 4 * he_so_a * he_so_c
            x_xa = (-he_so_b - math.sqrt(delta)) / (2 * he_so_a)
            x_xa_val = round(float(x_xa), 2)

            vd_da_1_d = '\\True Tầm bay xa của quả cầu là $%s$ m' % v_commas(x_xa_val)
            vd_da_1_s = 'Tầm bay xa của quả cầu là $%s$ m' % v_commas(round(x_xa_val - 2, 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Quả cầu chạm đất khi $y=0$. Giải phương trình $%s = 0$ ta được $x \\approx %s$ m (loại nghiệm âm). Vậy tầm bay xa là %s m.''' 
                            % (l_commas(pt_hien_thi), v_commas(x_xa_val), v_commas(x_xa_val)))

            ########################################################################
            # d) Vận dụng cao: Kiểm tra qua lưới
            ########################################################################
            y_tai_luoi = pt_quydao.subs(x, d_luoi)
            y_tai_luoi_val = round(float(y_tai_luoi), 3)
            is_good = y_tai_luoi_val > h_luoi

            check_str = "tốt" if is_good else "không tốt"
            vdc_da_1_d = '\\True Nếu vị trí phát cách lưới %s m thì đây là một đợt phát cầu %s' % (v_commas(d_luoi), check_str)
            vdc_da_1_s = 'Nếu vị trí phát cách lưới %s m thì đây là một đợt phát cầu %s' % (v_commas(d_luoi), "tốt" if not is_good else "không tốt")
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Tại vị trí lưới $x = %s$, độ cao quả cầu là: $y = %s$. \\\\ So sánh với chiều cao lưới %s m: Ta thấy %s %s %s. Do đó đây là một đợt phát cầu %s.''' 
                             % (v_commas(d_luoi), v_commas(y_tai_luoi_val), v_commas(h_luoi), v_commas(y_tai_luoi_val), ">" if is_good else "<", v_commas(h_luoi), check_str))

            # --- XỬ LÝ ĐÁP ÁN ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    break

            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

