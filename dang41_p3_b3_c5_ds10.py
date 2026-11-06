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


def bt_dang41_p3_b3_c5_ds10(self):
            while True:
                # Random các thông số với dải số nhỏ để kiểm soát kết quả < 9999
                p = random.randint(4, 8)  # Số mũ khai triển nhỏ lại
                n = random.randint(1, 3)  # Số mũ x1
                m = random.randint(1, 2)  # Số mũ x2

                # Chọn k ngẫu nhiên trước
                k_target = random.randint(0, p)

                # Hệ số a và b nhỏ (ưu tiên các số -2, -1, 1, 2, 3)
                a = random.choice([1, 2, 3])
                b = random.choice([-2, -1, 1, 2])

                # Tính hệ số: C(p, k) * a^(p-k) * b^k
                he_so_dung = math.comb(p, k_target) * (a**(p - k_target)) * (b**k_target)

                # Khống chế kết quả: -999 < he_so_dung < 9999
                if -999 < he_so_dung < 9999:
                    break

            # Tính số mũ T của x cần tìm: T = n*(p-k) - m*k
            T = n * (p - k_target) - m * k_target

            # Định dạng hiển thị biểu thức
            dau_b = "+" if b > 0 else "-"
            tri_tuyet_b = abs(b)

            # Xử lý hiển thị hệ số a (nếu a=1 thì không hiện số 1)
            a_str = latex(a) if a != 1 else ""

            # Xử lý hiển thị tử số b (nếu b=1 thì hiện 1)
            b_tex = latex(tri_tuyet_b)

            bieu_thuc = r"\left(%s x^{%s} %s \dfrac{%s}{x^{%s}}\right)^{%s}" % (
                a_str, latex(n), dau_b, b_tex, latex(m), latex(p)
            )

            # Câu hỏi
            noidungcauhoi = (r"Hệ số của số hạng chứa $x^{%s}$ trong khai triển của biểu thức $%s$ bằng bao nhiêu?"
                             % (latex(T), bieu_thuc))

            # Đáp án đúng dạng số nguyên
            da_d = r"\True $%d$" % he_so_dung

            # Tạo các phương án nhiễu
            s_set = set()
            while len(s_set) < 3:
                offset = random.choice([1, -1, 10, -10, 2, -2, 5])
                nhieu = he_so_dung + offset
                if nhieu != he_so_dung:
                    s_set.add(r"$%d$" % nhieu)

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            loigiai = (r"Số hạng tổng quát trong khai triển là:\\ "
                       r"$T_{k+1} = C_{%s}^k \cdot \left(%s x^{%s}\right)^{%s-k} \cdot \left(\dfrac{%s}{x^{%s}}\right)^k$\\ "
                       r"$= C_{%s}^k \cdot (%s)^{%s-k} \cdot (%s)^k \cdot x^{%s(%s-k)} \cdot x^{-%sk}$\\ "
                       r"$= C_{%s}^k \cdot (%s)^{%s-k} \cdot (%s)^k \cdot x^{%s - %sk}$.\\ "
                       r"Số hạng chứa $x^{%s}$ ứng với: $%s - %sk = %s \Leftrightarrow k = %s$.\\ "
                       r"Vậy hệ số cần tìm là: $C_{%s}^{%s} \cdot (%s)^{%s} \cdot (%s)^{%s} = %d$."
                       % (latex(p), a_str, latex(n), latex(p), b, latex(m),
                          latex(p), latex(a), latex(p), latex(b), latex(n), latex(p), latex(m),
                          latex(p), latex(a), latex(p), latex(b), latex(n*p), latex(n+m),
                          latex(T), latex(n*p), latex(n+m), latex(T), latex(k_target),
                          latex(p), latex(k_target), latex(a), latex(p-k_target), latex(b), latex(k_target), he_so_dung))

            # Đáp án ngắn (Ghi kết quả số nguyên vào ô dapan)
            dapan = r"\shortans[0]{$%d$}" % he_so_dung

            # Xuất nội dung và làm sạch chuỗi
            content = (r"\begin{minipage}{\textwidth}" + "\n"
                       r"\begin{ex}" + "\n" + noidungcauhoi + "\n" + dapan + "\n"
                       r"\loigiai{" + loigiai + r"}" + "\n"
                       r"\end{ex}" + "\n" + r"\end{minipage}" + "\n\n").replace('+-', '-').replace('--', '+').replace('x^{1}', 'x')

            return content

