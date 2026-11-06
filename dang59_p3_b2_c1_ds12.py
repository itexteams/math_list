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


def bt_dang59_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân sang dấu phẩy
            def fmt(num):
                s = str(num)
                if s.endswith('.0'): 
                    s = s[:-2]
                return s.replace('.', ',')

            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Các bộ thông số đảm bảo nghiệm luôn đẹp (nguyên) 
                # (L, V, p, m, x_ans, y_ans)
                # L: chiều dài, V: thể tích, p: % chi phí in, m: tỷ lệ chi phí phốt pho
                bocauhoi = [
                    (5, 15, 10, 3, 3, 1),
                    (8, 16, 25, 2, 2, 1),
                    (2, 6, 50, 3, 3, 1),
                    (16, 32, 12.5, 2, 2, 1)
                ]

                cau_hinh = random.choice(bocauhoi)
                L, V, p, m, x_ans, y_ans = cau_hinh

                K = V / L # xy = K
                k1_cost = 1 + p / 100
                k2_cost = m

                # Tính các hệ số diện tích và chi phí
                # Khay trong
                S1_x_coeff = L
                S1_y_coeff = 2 * L
                S1_const = 2 * K

                # Mặt lớn vỏ ngoài (in logo)
                SL_area = 2 * L
                TL_coeff = k1_cost * SL_area

                # Mặt bên vỏ ngoài (phốt pho)
                SB_area = 2 * L
                TB_coeff = k2_cost * SB_area

                # Tổng chi phí T
                T_x_coeff = S1_x_coeff + TL_coeff
                T_y_coeff = S1_y_coeff + TB_coeff

                # Hệ số hàm f(x)
                fx_x = T_x_coeff
                fx_1x = T_y_coeff * K
                fx_2x = 4 * (K**2)
                fx_const = S1_const

                # Đạo hàm f'(x)
                f_prime_const = fx_x
                f_prime_1x2 = fx_1x
                f_prime_1x3 = 2 * fx_2x

                # Các đáp án trắc nghiệm nhiễu
                x_ans_float = float(x_ans)
                s_vals = [x_ans_float + 1, x_ans_float + 2, x_ans_float + 0.5, x_ans_float + 1.5]
                if x_ans_float - 1 > 0: s_vals.append(x_ans_float - 1)
                if x_ans_float - 0.5 > 0: s_vals.append(x_ans_float - 0.5)

                du = ['$%s$' % fmt(x_ans)]
                da = random.choice(du)

                s = list(set(['$%s$' % fmt(v) for v in s_vals]))
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Code vẽ hình bằng TikZ (Mô tả khay trong và vỏ bao ngoài)
                tikz_img = '''\\begin{center}
            \\begin{tikzpicture}[>=stealth, line width=1pt]
            \\def\\y{0.8} \\def\\x{2.4} \\def\\L{4}
            \\draw[fill=gray!20] (0,\\y) -- (\\y,\\y) -- (\\y,0) -- (\\y+\\x,0) -- (\\y+\\x,\\y) -- (\\y+\\x+\\y,\\y) -- (\\y+\\x+\\y,\\y+\\L) -- (\\y+\\x,\\y+\\L) -- (\\y+\\x,\\y+\\L+\\y) -- (\\y,\\y+\\L+\\y) -- (\\y,\\y+\\L) -- (0,\\y+\\L) -- cycle;
            \\draw[dashed] (\\y,\\y) -- (\\y+\\x,\\y) -- (\\y+\\x,\\y+\\L) -- (\\y,\\y+\\L) -- cycle;
            \\draw[dashed] (0,\\y) -- (\\y+\\x+\\y,\\y);
            \\draw[dashed] (0,\\y+\\L) -- (\\y+\\x+\\y,\\y+\\L);
            \\draw[dashed] (\\y,0) -- (\\y,\\y+\\L+\\y);
            \\draw[dashed] (\\y+\\x,0) -- (\\y+\\x,\\y+\\L+\\y);
            \\node[left] at (0, \\y/2 + \\L/2) {$y$};
            \\node[below] at (\\y/2, 0) {$y$};
            \\node[below] at (\\y+\\x/2, 0) {$x$};
            \\node[right] at (\\y+\\x+\\y, \\y+\\L/2) {$%s cm$};
            \\begin{scope}[xshift=6.5cm, yshift=\\y cm]
            \\draw[fill=brown!70] (0,0) rectangle (\\y,\\L);
            \\draw[fill=white] (\\y,0) rectangle (\\y+\\x,\\L);
            \\draw[fill=brown!70] (\\y+\\x,0) rectangle (\\y+\\x+\\y,\\L);
            \\draw[fill=white] (\\y+\\x+\\y,0) rectangle (\\y+\\x+\\y+\\x,\\L);
            \\node[below] at (\\y/2, 0) {$y$};
            \\node[below] at (\\y+\\x/2, 0) {$x$};
            \\node[right] at (\\y+\\x+\\y+\\x, \\L/2) {$%s cm$};
            \\end{scope}
            \\end{tikzpicture}
            \\end{center}''' % (fmt(L), fmt(L))

                # Câu hỏi
                noidungcauhoi = (
                    'Công ty Diêm Thống Nhất cần thiết kế một mẫu hộp diêm kỷ niệm có chiều dài cố định là $%s$ cm '
                    'và thể tích chứa là $%s$ cm$^3$. Gọi chiều rộng hộp là $x$ (cm) và chiều cao là $y$ (cm). '
                    'Cấu tạo hộp diêm tham khảo hình vẽ. Khay nắp được gấp từ một tấm bìa cứng. '
                    'Tấm bìa này bị cắt bỏ 4 hình vuông cạnh $y$ ở các góc. Vỏ bao ngoài là một tấm bìa cuộn lại '
                    'thành hình hộp rỗng hai đầu, gồm 2 mặt lớn (in logo Thống Nhất) và 2 mặt bên (phủ hóa chất '
                    'ma sát để đánh lửa). Để tối ưu hóa chi phí sản xuất hàng loạt, bộ phận thiết kế đưa ra định '
                    'mức giá thành tính trên cùng một đơn vị diện tích như sau: chi phí vật liệu làm bìa khay nắp '
                    'trong là $C$ (VNĐ/cm$^2$). Phần bìa mặt lớn của vỏ ngoài yêu cầu in màu logo chất lượng cao '
                    'nên chi phí tốn kém hơn bìa khay trong $%s\\%%$. Phần bìa mặt bên của vỏ ngoài (quét photpho đỏ) '
                    'là tốn kém nhất, có chi phí gấp $%s$ lần bìa khay trong. '
                    'Tìm giá trị của $x$ để tổng chi phí vật liệu cho mỗi hộp diêm là thấp nhất?' % (fmt(L), fmt(V), fmt(p), fmt(m))
                )
                noidungcauhoi += tikz_img

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Bảng biến thiên TikZ
                bbt_tikz = '''\\begin{center}
            \\begin{tikzpicture}[>=stealth, line width=1pt]
            \\draw (0,2) -- (8,2);
            \\draw (0,1) -- (8,1);
            \\draw (0,-1) -- (8,-1);
            \\draw (0,3) -- (8,3);
            \\draw (0,-1) -- (0,3);
            \\draw (8,-1) -- (8,3);
            \\draw (1.5,-1) -- (1.5,3);
            \\node at (0.75, 2.5) {$x$};
            \\node at (0.75, 1.5) {$f'(x)$};
            \\node at (0.75, 0) {$f(x)$};
            \\node at (2, 2.5) {$0$};
            \\node at (4.75, 2.5) {$%s$};
            \\node at (7.5, 2.5) {$+\\infty$};
            \\node at (3.375, 1.5) {$-$};
            \\node at (4.75, 1.5) {$0$};
            \\node at (6.125, 1.5) {$+$};
            \\node at (2, 0.5) {$+\\infty$};
            \\node at (7.5, 0.5) {$+\\infty$};
            \\node at (4.75, -0.5) {$f(%s)$};
            \\draw[->] (2.3, 0.3) -- (4.4, -0.4);
            \\draw[->] (5.1, -0.4) -- (7.2, 0.3);
            \\end{tikzpicture}
            \\end{center}''' % (fmt(x_ans), fmt(x_ans))

                # Nội dung lời giải
                loigiai = (
                    'Thể tích: $V = %sxy = %s \\Rightarrow xy = %s \\Rightarrow y = \\frac{%s}{x}$.\\\\ \n'
                    'Khay nắp trong được gấp từ một tấm bìa hình chữ nhật có kích thước $(x + 2y) \\cdot (%s + 2y)$ sau khi cắt bỏ 4 hình vuông cạnh $y$ ở góc.\\\\ \n'
                    'Diện tích tấm bìa khay là: $S_1 = (x + 2y)(%s + 2y) = %sx + 2xy + %sy + 4y^2 = %sx + %sy + 4y^2 + %s$.\\\\ \n'
                    'Chi phí khay: $T_1 = C \\cdot S_1 = C(%sx + %sy + 4y^2 + %s)$.\\\\ \n'
                    'Vỏ bao ngoài bao gồm 2 mặt lớn và 2 mặt bên, mỗi mặt có chiều dài là $%s$ cm.\\\\ \n'
                    'Hai mặt lớn in logo có diện tích $S_L = 2 \\cdot %s \\cdot x = %sx$; chi phí đơn vị là $%s C$ nên chi phí tổng cho hai mặt lớn là $T_L = %s Cx$.\\\\ \n'
                    'Hai mặt bên quét phốt pho có diện tích $S_B = 2 \\cdot %s \\cdot y = %sy$; chi phí đơn vị là $%s C$ nên chi phí tổng cho hai mặt bên là $T_B = %s Cy$.\\\\ \n'
                    'Tổng chi phí vật liệu $T$ là:\\\\ \n'
                    '$T = T_1 + T_L + T_B = C(%sx + %sy + 4y^2 + %s + %sx + %sy) = C(%sx + %sy + 4y^2 + %s)$.\\\\ \n'
                    'Thay $y = \\frac{%s}{x}$ vào biểu thức, xét hàm số $f(x)$ với $x>0$:\\\\ \n'
                    '$f(x) = %sx + %s\\left(\\frac{%s}{x}\\right) + 4\\left(\\frac{%s}{x}\\right)^2 + %s = %sx + \\frac{%s}{x} + \\frac{%s}{x^2} + %s$.\\\\ \n'
                    'Đạo hàm: $f\'(x) = %s - \\frac{%s}{x^2} - \\frac{%s}{x^3} = \\frac{%sx^3 - %sx - %s}{x^3}$.\\\\ \n'
                    'Giải phương trình $f\'(x) = 0 \\Leftrightarrow %sx^3 - %sx - %s = 0 \\Leftrightarrow x = %s$.\\\\ \n'
                    'Bảng biến thiên: \n'
                    '%s \n'
                    'Từ bảng biến thiên, ta thấy hàm số đạt giá trị nhỏ nhất tại $x = %s$.\\\\ \n'
                    'Vậy giá trị của $x = %s$ thì tổng chi phí vật liệu là thấp nhất.'
                ) % (
                    fmt(L), fmt(V), fmt(K), fmt(K),
                    fmt(L),
                    fmt(L), fmt(S1_x_coeff), fmt(S1_y_coeff), fmt(S1_x_coeff), fmt(S1_y_coeff), fmt(S1_const),
                    fmt(S1_x_coeff), fmt(S1_y_coeff), fmt(S1_const),
                    fmt(L),
                    fmt(L), fmt(SL_area), fmt(k1_cost), fmt(TL_coeff),
                    fmt(L), fmt(SB_area), fmt(k2_cost), fmt(TB_coeff),
                    fmt(S1_x_coeff), fmt(S1_y_coeff), fmt(S1_const), fmt(TL_coeff), fmt(TB_coeff), fmt(T_x_coeff), fmt(T_y_coeff), fmt(S1_const),
                    fmt(K),
                    fmt(T_x_coeff), fmt(T_y_coeff), fmt(K), fmt(K), fmt(S1_const), fmt(fx_x), fmt(fx_1x), fmt(fx_2x), fmt(fx_const),
                    fmt(f_prime_const), fmt(f_prime_1x2), fmt(f_prime_1x3), fmt(f_prime_const), fmt(f_prime_1x2), fmt(f_prime_1x3),
                    fmt(f_prime_const), fmt(f_prime_1x2), fmt(f_prime_1x3), fmt(x_ans),
                    bbt_tikz,
                    fmt(x_ans),
                    fmt(x_ans)
                )
                dapan='\\shortans[0]{$%s$}\n'%(fmt(x_ans))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

