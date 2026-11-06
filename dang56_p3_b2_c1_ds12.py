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


def bt_dang56_p3_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random kịch bản để tạo ra các mức hoa hồng khác nhau
                case_type = random.choice([1, 2, 3])
                K_val = random.choice([10, 20, 30, 40, 50])

                # Hàm format số thập phân dùng dấu phẩy
                def fmt(num):
                    if num == int(num):
                        return str(int(num))
                    return str(num).replace('.', ',')

                def fmt_c(num):
                    return "" if num == 1 else fmt(num)

                if case_type == 1:
                    # Kịch bản 1: S(x) ~ căn bậc 2, C(x) ~ bậc 2 => Đáp án r = 25%
                    ans_r = 25
                    a_val = random.choice([0.5, 1, 2, 2.5])
                    b_val = int(400 * a_val * K_val)

                    C_str = f"{fmt_c(a_val)}x^2"
                    S_str = f"{fmt_c(b_val)}\\sqrt{{x}}"
                    I_str = f"\\frac{{r}}{{100}} \\cdot {fmt_c(b_val)}\\sqrt{{x}} - {fmt_c(a_val)}x^2 = {fmt_c(b_val/100)} r \\sqrt{{x}} - {fmt_c(a_val)}x^2"
                    I_prime_str = f"I'(x) = \\frac{{{fmt(b_val/200)} r}}{{\\sqrt{{x}}}} - {fmt_c(2*a_val)}x = 0 \\Rightarrow x(r) = \\sqrt[3]{{({K_val} r)^2}}"
                    L_str = f"(1 - r\\%) \\cdot {fmt_c(b_val)} \\sqrt[3]{{({K_val} r)^2}}"

                elif case_type == 2:
                    # Kịch bản 2: S(x) ~ căn bậc 2, C(x) ~ bậc 1 => Đáp án r = 50%
                    ans_r = 50
                    a_val = random.choice([1, 2, 3, 4, 5])
                    b_val = int(200 * a_val * K_val)

                    C_str = f"{fmt_c(a_val)}x"
                    S_str = f"{fmt_c(b_val)}\\sqrt{{x}}"
                    I_str = f"\\frac{{r}}{{100}} \\cdot {fmt_c(b_val)}\\sqrt{{x}} - {fmt_c(a_val)}x = {fmt_c(b_val/100)} r \\sqrt{{x}} - {fmt_c(a_val)}x"
                    I_prime_str = f"I'(x) = \\frac{{{fmt(b_val/200)} r}}{{\\sqrt{{x}}}} - {fmt(a_val)} = 0 \\Rightarrow x(r) = ({K_val} r)^2"
                    L_str = f"(1 - r\\%) \\cdot {fmt_c(b_val)} \\cdot ({K_val} r)"

                else:
                    # Kịch bản 3: S(x) ~ bậc 1, C(x) ~ bậc 2 => Đáp án r = 50%
                    ans_r = 50
                    a_val = random.choice([0.5, 1, 2, 3])
                    b_val = int(200 * a_val * K_val)

                    C_str = f"{fmt_c(a_val)}x^2"
                    S_str = f"{fmt_c(b_val)}x"
                    I_str = f"\\frac{{r}}{{100}} \\cdot {fmt_c(b_val)}x - {fmt_c(a_val)}x^2 = {fmt_c(b_val/100)} r x - {fmt_c(a_val)}x^2"
                    I_prime_str = f"I'(x) = {fmt(b_val/100)} r - {fmt_c(2*a_val)}x = 0 \\Rightarrow x(r) = {K_val} r"
                    L_str = f"(1 - r\\%) \\cdot {fmt_c(b_val)} \\cdot ({K_val} r)"

                # Câu hỏi
                noidungcauhoi = ('''Một công ty công nghệ muốn thiết kế chính sách hoa hồng cho đội ngũ kinh doanh chủ lực của mình. Công ty sẽ đưa ra một mức hoa hồng là $r$ (tính bằng $\\%%$) trên tổng doanh thu mà đội ngũ kinh doanh mang về. Sau khi phân tích dữ liệu kinh doanh và chi phí hoạt động trong nhiều quý người ta nhận thấy rằng để tạo ra doanh thu thì đội ngũ bán hàng phải chi trả các chi phí hoạt động như đi lại, gặp gỡ,... Nếu đội kinh doanh tiếp cận $x$ khách hàng tiềm năng thì tổng chi phí hoạt động là $C(x) = %s$ (triệu đồng) và doanh thu dự kiến mang về từ $x$ khách hàng tiềm năng này là $S(x) = %s$ (triệu đồng). Đội ngũ kinh doanh được trao quyền tự chủ để tự quyết định số lượng khách hàng cần tiếp cận mỗi tháng sao cho thu nhập của cả đội là lớn nhất. Để tối đa hóa lợi nhuận thì công ty cần đặt ra mức hoa hồng là bao nhiêu?''' 
                                 % (C_str, S_str))

                # Lời giải chứa code TikZ bảng biến thiên
                loigiai = ('''Gọi $r$ là mức hoa hồng ($\\%%$) công ty đưa ra. Thu nhập của đội ngũ kinh doanh là hiệu số giữa tiền hoa hồng nhận được và chi phí hoạt động:
                $$I(x) = %s \\ (x>0)$$
                Giá trị $x$ làm cho $I(x)_{\\max}$ là: $%s$ \\\\
                Công ty hưởng phần: $(1 - r\\%%) \\cdot S(x)$ \\\\
                Thay $x = x(r)$ vào $\\Rightarrow L(r) = %s$ \\\\
                Dùng $\\frac{\\mathrm{d}}{\\mathrm{d}r} \\left[ L(r) \\right] = 0 \\Rightarrow r = %s$ \\\\
                Bảng biến thiên:
                \\begin{center}
                \\begin{tikzpicture}[line width=1pt]
                \\draw (0,0) rectangle (8,3);
                \\draw (0,2) -- (8,2);
                \\draw (0,2.5) -- (8,2.5);
                \\draw (1,0) -- (1,3);
                \\node at (0.5, 2.75) {$r$};
                \\node at (1.5, 2.75) {$0$};
                \\node at (4.5, 2.75) {$%s$};
                \\node at (7.5, 2.75) {$100$};
                \\node at (0.5, 2.25) {$L'(r)$};
                \\node at (2.75, 2.25) {$+$};
                \\node at (4.5, 2.25) {$0$};
                \\node at (6.25, 2.25) {$-$};
                \\node at (0.5, 1) {$L(r)$};
                \\draw[->, >=stealth, line width=1pt] (1.5, 0.2) -- (4.0, 1.7);
                \\node at (4.5, 1.8) {$L(r_{\\max})$};
                \\draw[->, >=stealth, line width=1pt] (5.0, 1.7) -- (7.5, 0.2);
                \\end{tikzpicture}
                \\end{center}
                Để tối đa hóa lợi nhuận thì công ty cần đặt ra mức hoa hồng là $%s\\%%$.''' 
                           % (I_str, I_prime_str, L_str, ans_r, ans_r, ans_r))
                dapan='\\shortans[0]{$%s$}\n'%(ans_r)

                # Các đáp án
                da = f'${ans_r}\\%%$'
                all_possible = [15, 20, 25, 30, 35, 40, 45, 50, 60]
                if ans_r in all_possible:
                    all_possible.remove(ans_r)

                wrong_choices = random.sample(all_possible, 3)

                da_d = ('\\True ' + str(da))
                da_s1 = '$%s\\%%$' % wrong_choices[0]
                da_s2 = '$%s\\%%$' % wrong_choices[1] 
                da_s3 = '$%s\\%%$' % wrong_choices[2] 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

