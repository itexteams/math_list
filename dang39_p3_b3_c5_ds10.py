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


def bt_dang39_p3_b3_c5_ds10(self):
            while True:
                # Random các thông số cơ bản (giới hạn p nhỏ để kq < 9999)
                p = random.randint(5, 10)
                m = random.choice([2, 3, 5])
                n = random.choice([2, 3, 5])
                if m == n: n = 7

                a = 2 # Bậc căn bậc hai
                b = 3 # Bậc căn bậc ba

                integer_terms = []
                k_values = []

                # Tìm các số hạng nguyên
                for k in range(p + 1):
                    # Điều kiện: (p-k) chia hết cho 2 và k chia hết cho 3
                    if (p - k) % a == 0 and k % b == 0:
                        # T_k+1 = C(p,k) * m^((p-k)/2) * n^(k/3)
                        val = math.comb(p, k) * (m**((p - k) // a)) * (n**(k // b))
                        integer_terms.append(int(val))
                        k_values.append(k)

                # Nếu có số hạng nguyên, lấy số hạng lớn nhất và kiểm tra điều kiện < 9999
                if integer_terms:
                    kq_val = max(integer_terms)
                    if kq_val < 9999:
                        break

            # Câu hỏi
            bieu_thuc_latex = r"\left( \sqrt{%s} + \sqrt[3]{%s} \right)^{%s}" % (latex(m), latex(n), latex(p))
            noidungcauhoi = (r"Trong khai triển biểu thức $F = %s$, số hạng nguyên có giá trị lớn nhất bằng bao nhiêu?"
                             % bieu_thuc_latex)

            # Đáp án đúng
            da_d = r"\True $%d$" % kq_val

            # Tạo các phương án nhiễu
            s_set = set()
            # Thêm các số hạng nguyên khác (nếu có) vào danh sách nhiễu
            for v in integer_terms:
                if v != kq_val:
                    s_set.add(r"$%d$" % v)

            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, -10, 100, 2, 5])
                nhieu = kq_val + offset
                if nhieu > 0 and nhieu != kq_val:
                    s_set.add(r"$%d$" % nhieu)

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Lời giải chi tiết
            dieu_kien_k = (r"$\begin{cases} k \in \mathbb{N} \\ 0 \le k \le %d \\ (%d - k) \vdots 2 \\ k \vdots 3 \end{cases}$" 
                           % (p, p))

            loigiai_k = " hoặc ".join(["k = " + str(kv) for kv in k_values])

            chi_tiet_t = ""
            for i in range(len(k_values)):
                kv = k_values[i]
                val = integer_terms[i]
                chi_tiet_t += r"Với $k = %d \Rightarrow T_{%d} = C_{%d}^{%d} \cdot (\sqrt{%d})^{%d} \cdot (\sqrt[3]{%d})^{%d} = %d$.\\ " % (
                    kv, kv + 1, p, kv, m, p - kv, n, kv, val
                )

            loigiai = (r"Số hạng tổng quát trong khai triển là $T_{k+1} = C_{%d}^k (\sqrt{%d})^{%d-k} (\sqrt[3]{%d})^k$. \\ "
                       r"Để $T_{k+1}$ là một số nguyên thì %s. \\ "
                       r"Suy ra $%s$. \\ "
                       r"%s"
                       r"Vậy trong khai triển, số hạng nguyên có giá trị lớn nhất là $%d$."
                       % (p, m, p, n, dieu_kien_k, loigiai_k, chi_tiet_t, kq_val))

            # Đáp án ngắn (Số nguyên cụ thể)
            dapan = r"\shortans[0]{$%d$}" % kq_val

            # Xuất nội dung
            content = ("\\begin{minipage}{\\textwidth} " + "\n"
                       "\\begin{ex}" + "\n" + noidungcauhoi + dapan +
                       "\\loigiai{" + loigiai + "}" + "\n"
                       "\\end{ex}" + "\n" + "\\end{minipage}" + "\n\n")

            return content

