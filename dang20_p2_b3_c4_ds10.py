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


def bt_dang20_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Chi phí mặt song song bờ sông (60.000đ -> 60)
            cp1 = random.choice([40, 50, 60, 80]) 
            # Chi phí 3 mặt vuông góc bờ sông (50.000đ -> 50)
            cp2 = random.choice([30, 40, 50, 70]) 
            # Tổng số tiền ông Tư bỏ ra (15 triệu -> 15000 ngàn đồng)
            tong_tien = random.choice([12000, 15000, 18000, 20000])
            # Diện tích tối thiểu
            S_min = random.choice([3000, 4000, 4500])

            # Tính toán các hệ số cho biểu thức
            # Phương trình hàng rào: cp1 * x + 3 * cp2 * y = tong_tien
            # Ví dụ: 60x + 150y = 15000 <=> 2x + 5y = 500 (sau khi chia bớt)

            x, y = symbols('x y')
            hsc_x = cp1
            hsc_y = 3 * cp2

            # Rút gọn phương trình đường thẳng nếu có thể
            common = math.gcd(math.gcd(hsc_x, hsc_y), tong_tien)
            hsc_x_rg = hsc_x // common
            hsc_y_rg = hsc_y // common
            tong_tien_rg = tong_tien // common

            # Biểu diễn y theo x: y = (tong_tien - cp1*x) / (3*cp2)
            y_expr = (tong_tien - cp1*x) / (3*cp2)
            # Tổng diện tích S = x * y
            S_expr = x * y_expr

            # Đạo hàm để tìm cực đại
            S_prime = S_expr.diff(x)
            x_max = solve(S_prime, x)[0]
            S_max_val = S_expr.subs(x, x_max)

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'''Ông Tư có khu đất trống dọc bờ sông. Dịp này ông bỏ ra %s triệu đồng làm hàng rào hình chữ E để phân làm hai mảnh vườn hình chữ nhật bằng nhau. Đối với mặt hàng rào song song bờ sông thì chi phí nguyên vật liệu là %s.000 đồng một mét, còn đối với ba mặt hàng rào song song nhau (vuông góc bờ sông) thì chi phí nguyên vật liệu là %s.000 đồng một mét. Ta đặt kích thước các hàng rào như hình vẽ (với $x, y > 0$ và có đơn vị m). Biết rằng tổng diện tích hai mảnh vườn tối thiểu bằng $%s m^2$.''' 
                             % (latex(tong_tien//1000), latex(cp1), latex(cp2), latex(S_min)))

            # --- NHẬN BIẾT ---
            nb_da_1_d = r'\True Mối liên hệ giữa x và y là $%sx + %sy = %s$' % (latex(hsc_x_rg), latex(hsc_y_rg), latex(tong_tien_rg))
            nb_da_1_s = r'Mối liên hệ giữa x và y là $%sx + %sy = %s$' % (latex(hsc_y_rg), latex(hsc_x_rg), latex(tong_tien_rg))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = r'''Tổng chi phí làm hàng rào là: $%s.000x + 3 \cdot %s.000y = %s.000.000$. \\ Rút gọn ta được phương trình: $%sx + %sy = %s$.''' % (latex(cp1), latex(cp2), latex(tong_tien//1000), latex(hsc_x_rg), latex(hsc_y_rg), latex(tong_tien_rg))

            # --- THÔNG HIỂU ---
            th_da_1_d = r'\True Diện tích hai mảnh vườn tính theo x là $S = \frac{1}{%s}(-%sx^2 + %sx)$' % (latex(3*cp2), latex(cp1), latex(tong_tien))
            th_da_1_s = r'Diện tích hai mảnh vườn tính theo x là $S = \frac{1}{%s}(-%sx^2 + %sx)$' % (latex(cp2), latex(cp1), latex(tong_tien))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = r'''Từ phương trình hàng rào, ta có $y = \frac{%s - %sx}{%s}$. \\ Khi đó diện tích $S = x \cdot y = x \cdot \frac{%s - %sx}{%s} = \frac{1}{%s}(-%sx^2 + %sx)$.''' % (latex(tong_tien), latex(cp1), latex(3*cp2), latex(tong_tien), latex(cp1), latex(3*cp2), latex(3*cp2), latex(cp1), latex(tong_tien))

            # --- VẬN DỤNG ---
            # Kiểm tra x_max có thỏa mãn diện tích tối thiểu không để đặt câu hỏi đúng/sai
            x_c_lim = solve(S_expr - S_min, x)
            x_min_val = float(min(x_c_lim))
            x_max_val_bound = float(max(x_c_lim))

            vd_da_1_d = r'\True Chiều dài tối đa của hàng rào song song bờ sông để diện tích không dưới $%s m^2$ là khoảng $%s m$' % (latex(S_min), latex(round(x_max_val_bound, 1)))
            vd_da_1_s = r'Chiều dài tối đa của hàng rào song song bờ sông là $%s m$' % (latex(tong_tien_rg))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = r'''Để diện tích $S \geq %s$, ta giải bất phương trình $\frac{1}{%s}(-%sx^2 + %sx) \geq %s$. \\ Giải ra ta được $x$ nằm trong đoạn giới hạn, giá trị tối đa x xấp xỉ $%s m$.''' % (latex(S_min), latex(3*cp2), latex(cp1), latex(tong_tien), latex(S_min), latex(round(x_max_val_bound,1)))

            # --- VẬN DỤNG CAO ---
            vdc_da_1_d = r'\True Tổng diện tích hai mảnh vườn không vượt quá $%s m^2$' % (latex(round(float(S_max_val), 1)))
            vdc_da_1_s = r'Tổng diện tích hai mảnh vườn không vượt quá $%s m^2$' % (latex(round(float(S_max_val) + 500, 1)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = r'''Xét hàm $S(x) = \frac{1}{%s}(-%sx^2 + %sx)$. Đạo hàm $S'(x) = \frac{1}{%s}(-%sx + %s)$. $S'(x) = 0 \Leftrightarrow x = %s$. \\ Khi đó diện tích cực đại là $S = %s m^2$.''' % (latex(3*cp2), latex(2*cp1), latex(tong_tien), latex(3*cp2), latex(2*cp1), latex(tong_tien), latex(x_max), latex(round(float(S_max_val),1)))

            # --- Tổng hợp và Xuất bản ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_list = [random.choice(list_nb_da_1), random.choice(list_th_da_1), random.choice(list_vd_da_1), random.choice(list_vdc_da_1)]
                if 1 <= count_true_answers(ans_list) <= 3:
                    shuffled_answers = ans_list
                    break

            list_sol = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(list_sol[0]) + '\n'
                '\\item ' + str(list_sol[1]) + '\n'
                '\\item ' + str(list_sol[2]) + '\n'
                '\\item ' + str(list_sol[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

