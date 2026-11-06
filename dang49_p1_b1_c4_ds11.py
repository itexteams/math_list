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


def bt_dang49_p1_b1_c4_ds11(self):
            # Khai báo biến
            # 1. Random số liệu đầu vào
            u1 = randint(2, 9)          # Số hạng đầu u1 (ví dụ: 3)
            mau_so = randint(2, 6)      # Mẫu số của công bội (ví dụ: 5)
            dau = choice([-1, 1])       # Dấu của công bội (âm hoặc dương)

            # Thiết lập công bội q và biểu thức truy hồi
            q = Rational(dau, mau_so)   # q = +/- 1/mau_so

            if dau == -1:
                # Nếu q âm: u_{n+1} = - u_n / mau
                cong_thuc_truy_hoi = "u_{n+1} = -\\frac{u_n}{%s}" % mau_so
                q_display = "-\\frac{1}{%s}" % mau_so
            else:
                # Nếu q dương: u_{n+1} = u_n / mau
                cong_thuc_truy_hoi = "u_{n+1} = \\frac{u_n}{%s}" % mau_so
                q_display = "\\frac{1}{%s}" % mau_so

            # 2. Tính toán kết quả (Đáp án đúng và Nhiễu)
            kq_val = Rational(u1, 1 - q)  # Đáp án đúng: S = u1 / (1-q)

            # Tạo tập hợp đáp án để tránh trùng lặp
            answers = set()
            answers.add(kq_val)

            # Nhiễu 1: Sai dấu công thức (S = u1 / (1+q))
            ans_wrong1 = Rational(u1, 1 + q)
            if ans_wrong1 not in answers: answers.add(ans_wrong1)

            # Nhiễu 2: Nghịch đảo kết quả (1/S)
            if kq_val != 0:
                ans_wrong2 = Rational(1, kq_val)
                if ans_wrong2 not in answers: answers.add(ans_wrong2)

            # Nhiễu 3: Sai lầm cộng đơn giản (u1 + q)
            ans_wrong3 = Rational(u1 * mau_so + dau, mau_so) # u1 + q
            if ans_wrong3 not in answers: answers.add(ans_wrong3)

            # Nếu vẫn chưa đủ 4 đáp án (do trùng lặp), random thêm
            while len(answers) < 4:
                r = Rational(randint(1, 20), randint(2, 10))
                answers.add(r)

            # Chuyển set thành list để xử lý hiển thị
            list_ans_val = list(answers)

            # 3. Chuẩn bị xuất dữ liệu
            # Tạo danh sách chuỗi đáp án có thẻ \True cho đáp án đúng
            final_options_str = []

            for val in list_ans_val:
                val_latex = '$%s$.' % latex(val)
                if val == kq_val:
                    final_options_str.append('\\True ' + val_latex) # Đánh dấu đáp án đúng
                else:
                    final_options_str.append(val_latex)

            # Trộn ngẫu nhiên vị trí các đáp án A, B, C, D
            random.shuffle(final_options_str)

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (
                "Cho dãy số $(u_n), n \\in \\mathbb{N}^*$, thỏa mãn điều kiện "
                "$\\begin{cases} u_1 = %s \\\\ %s \\end{cases}$. "
                "Gọi $S = u_1 + u_2 + u_3 + \\dots + u_n$ là tổng $n$ số hạng đầu tiên của dãy số đã cho. "
                "Khi đó $\\lim S_n$ bằng" 
                % (u1, cong_thuc_truy_hoi)
            )

            # --- NỘI DUNG LỜI GIẢI ---
            mau_so_chung = 1 - q
            loigiai = (
                "Ta có $\\frac{u_{n+1}}{u_n} = %s$. \\\\\n"
                "Do đó dãy $(u_n), n \\in \\mathbb{N}^*$ là một cấp số nhân lùi vô hạn có "
                "$u_1 = %s, q = %s$. \\\\\n"
                "Suy ra $\\lim_{n \\to +\\infty} S_n = \\frac{u_1}{1-q} = \\frac{%s}{1 - \\left(%s\\right)} = \\frac{%s}{%s} = %s$."
                % (
                    q_display,      # q biểu diễn
                    u1, q_display,  # u1, q
                    u1, q_display,  # u1, q trong công thức
                    u1, latex(mau_so_chung), # tử, mẫu sau quy đồng
                    latex(kq_val)   # Kết quả cuối cùng
                )
            )

            # --- XUẤT RA CONTENT ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{'+str(final_options_str[0])+'}\n'
                       '{'+str(final_options_str[1])+'}\n'
                       '{'+str(final_options_str[2])+'}\n'
                       '{'+str(final_options_str[3])+'}\n'
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

