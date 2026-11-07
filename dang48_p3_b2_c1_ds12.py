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


def bt_dang48_p3_b2_c1_ds12(self):
                # Khai báo biến
                lisdang = ['1']
                dang = random.choice(lisdang)

                if dang == '1':
                    # Danh sách các cặp (L, W) đã lọc đảm bảo L > 2W và V_max <= 9999
                    valid_pairs = [
                        (60, 20),   # V_max ≈ 1155
                        (90, 20),   # V_max ≈ 1893
                        (90, 30),   # V_max ≈ 3897
                        (90, 40),   # V_max ≈ 6338
                        (120, 20),  # V_max ≈ 2638
                        (120, 30),  # V_max ≈ 5556
                        (120, 40),  # V_max ≈ 9238
                        (150, 20),  # V_max ≈ 3385
                        (150, 30)   # V_max ≈ 7227
                    ]
                    L_val, W_val = random.choice(valid_pairs)

                    # Tính toán các đại lượng toán học bằng sympy
                    x = symbols('x')
                    # Thể tích V(x) = ((L - 3x)/2) * (W - 2x) * x
                    V = (L_val - 3*x)/2 * (W_val - 2*x) * x
                    V_exp = expand(V)

                    V_prime = diff(V_exp, x)
                    roots = solve(V_prime, x)

                    dk1 = W_val // 2
                    dk2 = L_val // 3
                    dk_min = min(dk1, dk2)

                    # Hàm xử lý định dạng số (đổi chấm thành phẩy, bỏ đuôi .0)
                    def format_num(num):
                        num_float = float(num)
                        if num_float == int(num_float):
                            return str(int(num_float))
                        return str(num_float).replace('.', ',')

                    valid_roots = []
                    for r in roots:
                        if r.is_real and 0 < r.evalf() < dk_min:
                            valid_roots.append(r)

                    best_x = valid_roots[0]
                    max_V = V_exp.subs(x, best_x).evalf()
                    kq_int = int(Decimal(str(max_V)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

                    max_V_float = float(max_V)
                    max_V_dec3 = f"{max_V_float:.3f}".replace('.', ',')

                    # Chuỗi toán học LaTeX
                    V_str = latex(V_exp)
                    V_prime_str = latex(V_prime)

                    root_latex_list = []
                    for r in roots:
                        r_str = latex(r)
                        if 0 < r.evalf() < dk_min:
                            root_latex_list.append('x = %s \\in (0; %s)' % (r_str, format_num(dk_min)))
                        else:
                            root_latex_list.append('x = %s \\notin (0; %s)' % (r_str, format_num(dk_min)))

                    if len(root_latex_list) == 2:
                        roots_cases = '\\left[ \\begin{array}{l} %s \\\\ %s \\end{array} \\right.' % (root_latex_list[0], root_latex_list[1])
                    else:
                        roots_cases = root_latex_list[0]

                    max_V_latex = latex(best_x)

                    # Tạo các đáp án trắc nghiệm
                    da = str(kq_int)
                    wrong_offsets = [1, -1, 2, -2, 5, -5, 10, -10]
                    s_list = []
                    for offset in wrong_offsets:
                        w_val = kq_int + offset
                        if w_val > 0 and w_val != kq_int:
                            s_list.append(str(w_val))
                    s_list = list(set(s_list))
                    random.shuffle(s_list)
                    das1 = s_list[0]
                    das2 = s_list[1]
                    das3 = s_list[2]

                    # TikZ vẽ hộp 3D
                    tikz_3d = (
                        '\\begin{tikzpicture}[scale=0.7, line join=round, line cap=round, line width=1pt]\n'
                        '    \\coordinate (O) at (0,0);\n'
                        '    \\coordinate (L) at (-4.5, 1.5);\n'
                        '    \\coordinate (R) at (2.5, 0.8);\n'
                        '    \\coordinate (B) at (-2.0, 2.3);\n'
                        '    \\def\\h{0.5}\n'
                        '    \\coordinate (Ot) at (0, \\h);\n'
                        '    \\coordinate (Lt) at (-4.5, 1.5+\\h);\n'
                        '    \\coordinate (Rt) at (2.5, 0.8+\\h);\n'
                        '    \\coordinate (Bt) at (-2.0, 2.3+\\h);\n'
                        '    \\draw[dashed] (B) -- (L);\n'
                        '    \\draw[dashed] (B) -- (R);\n'
                        '    \\draw[dashed] (B) -- (Bt);\n'
                        '    \\draw (Lt) -- (Bt) -- (Rt);\n'
                        '    \\draw[fill=white] (O) -- (L) -- (Lt) -- (Ot) -- cycle;\n'
                        '    \\draw[fill=orange!30] (O) -- (R) -- (Rt) -- (Ot) -- cycle;\n'
                        '    \\coordinate (Lid1) at (-2.5, 6.0);\n'
                        '    \\coordinate (Lid2) at (0.0, 6.8);\n'
                        '    \\draw[fill=white] (Lt) -- (Bt) -- (Lid2) -- (Lid1) -- cycle;\n'
                        '    \\coordinate (Lip1) at (-2.8, 5.2);\n'
                        '    \\coordinate (Lip2) at (-0.3, 6.0);\n'
                        '    \\draw[fill=blue!20] (Lid1) -- (Lid2) -- (Lip2) -- (Lip1) -- cycle;\n'
                        '    \\node[below left] at (-2.25, 0.75) {$\\frac{%s - 3x}{2}$};\n'
                        '    \\node[below right] at (1.25, 0.4) {$%s - 2x$};\n'
                        '    \\node[right] at (2.5, 0.4+\\h/2) {$x$};\n'
                        '    \\node[left] at (-2.65, 5.6) {$x$};\n'
                        '\\end{tikzpicture}'
                    ) % (L_val, W_val)

                    # TikZ vẽ thiết kế phẳng 2D
                    tikz_2d = (
                        '\\begin{tikzpicture}[scale=0.08, line join=round, line cap=round, line width=1pt]\n'
                        '    \\def\\W{30}\n'
                        '    \\def\\L{90}\n'
                        '    \\def\\x{6}\n'
                        '    \\def\\y{36}\n'
                        '    \\draw (0,0) rectangle (\\L, \\W);\n'
                        '    \\draw[<->] (0, \\W+4) -- (\\L, \\W+4) node[midway, fill=white] {$%s$};\n'
                        '    \\draw[<->] (\\L+4, 0) -- (\\L+4, \\W) node[midway, fill=white] {$%s$};\n'
                        '    \\fill[pattern=north east lines] (0, \\W-\\x) rectangle (\\x, \\W);\n'
                        '    \\fill[pattern=north east lines] (0, 0) rectangle (\\x, \\x);\n'
                        '    \\fill[pattern=north east lines] (\\x+\\y, \\W-\\x) rectangle (\\L, \\W);\n'
                        '    \\fill[pattern=north east lines] (\\x+\\y, 0) rectangle (\\L, \\x);\n'
                        '    \\fill[orange!30] (\\x+\\y, \\x) rectangle (\\x+\\y+\\x, \\W-\\x);\n'
                        '    \\fill[blue!20] (\\L-\\x, \\x) rectangle (\\L, \\W-\\x);\n'
                        '    \\draw[dashed] (\\x, 0) -- (\\x, \\W);\n'
                        '    \\draw[dashed] (\\x+\\y, 0) -- (\\x+\\y, \\W);\n'
                        '    \\draw[dashed] (\\x+\\y+\\x, 0) -- (\\x+\\y+\\x, \\W);\n'
                        '    \\draw[dashed] (\\L-\\x, 0) -- (\\L-\\x, \\W);\n'
                        '    \\draw[dashed] (0, \\x) -- (\\L, \\x);\n'
                        '    \\draw[dashed] (0, \\W-\\x) -- (\\L, \\W-\\x);\n'
                        '    \\draw (0,0) rectangle (\\L, \\W);\n'
                        '    \\draw (0, \\W-\\x) rectangle (\\x, \\W);\n'
                        '    \\draw (0, 0) rectangle (\\x, \\x);\n'
                        '    \\draw (\\x+\\y, \\W-\\x) rectangle (\\L, \\W);\n'
                        '    \\draw (\\x+\\y, 0) rectangle (\\L, \\x);\n'
                        '    \\node at (\\x/2, \\W-\\x/2) {$x$};\n'
                        '    \\node[below] at (\\x/2, 0) {$x$};\n'
                        '    \\node[below] at (\\x+\\y+\\x/2, \\x) {$x$};\n'
                        '    \\node[below] at (\\L-\\x/2, \\x) {$x$};\n'
                        '    \\draw[<->] (\\x, \\W/2) -- (\\x+\\y, \\W/2) node[midway, fill=white] {$//$};\n'
                        '    \\draw[<->] (\\x+\\y+\\x, \\W/2) -- (\\L-\\x, \\W/2) node[midway, fill=white] {$//$};\n'
                        '\\end{tikzpicture}'
                    ) % (L_val, W_val)

                    # Nội dung câu hỏi
                    noidungcauhoi = ('''Bạn Nam có dùng một miếng bìa hình chữ nhật có kích thước chiều dài bằng $%s$ cm và chiều rộng bằng $%s$ cm để gấp thành một chiếc hộp có nắp như hình vẽ. Bạn Nam tiến hành thao tác cắt bỏ hai hình vuông cạnh bằng $x$ (cm) và cắt bỏ hai hình chữ nhật là các phần gạch chéo như hình vẽ. Sau đó gấp theo các đường nét đứt. Hỏi thể tích lớn nhất của chiếc hộp là bao nhiêu centimet khối? (Kết quả làm tròn đến hàng đơn vị).
\\begin{center}
%s
\\hspace{1cm}
%s
\\end{center}'''
                                     % (L_val, W_val, tikz_3d, tikz_2d))

                    # Các đáp án
                    da_d = ('\\True ' + str(da))
                    da_s1 = str(das1)
                    da_s2 = str(das2)
                    da_s3 = str(das3)

                    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                    list_1 = [da_d, da_s1, da_s2, da_s3]
                    random.shuffle(list_1)

                    # Nội dung lời giải
                    loigiai = ('''Điều kiện xác định: $\\begin{cases} x > 0 \\\\ %s - 2x > 0 \\\\ \\frac{%s - 3x}{2} > 0 \\end{cases} \\Leftrightarrow \\begin{cases} x > 0 \\\\ x < %s \\\\ x < %s \\end{cases} \\Leftrightarrow 0 < x < %s$. \\\\
Thể tích của khối hộp là: $V(x) = S_d \\cdot h = \\left( \\frac{%s - 3x}{2} \\right) (%s - 2x) x = %s$. \\\\
Đạo hàm: $V'(x) = %s = 0 \\Leftrightarrow %s$. \\\\
Vậy thể tích lớn nhất của chiếc hộp là: $V\\left(%s\\right) = %s... \\approx %s$ (cm$^3$).'''
                               % (W_val, L_val,
                                  format_num(dk1), format_num(dk2), format_num(dk_min),
                                  L_val, W_val, V_str,
                                  V_prime_str, roots_cases,
                                  max_V_latex, max_V_dec3, kq_int))
                    dapan = '\\shortans[0]{$%s$}\n' % (kq_int)

                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                           '\\begin{ex}\n' + str(noidungcauhoi) + dapan +
                           '\\loigiai{\n' + str(loigiai) + '\n}\n'
                           '\\end{ex}\n\\end{minipage} \n\n')
                return content