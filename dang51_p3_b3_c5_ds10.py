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


def bt_dang51_p3_b3_c5_ds10(self):
            while True:
                # Random n và b trong dải an toàn để hệ số không bùng nổ quá nhanh
                n = random.randint(5, 15)
                b = random.randint(1, 4)

                # Tìm chỉ số k sao cho a_k là lớn nhất
                # Công thức: a_{k}/a_{k-1} >= 1 <=> k <= b(n+1)/(b+1)
                k_max = int((b * (n + 1)) // (b + 1))

                # Tính hệ số lớn nhất: a_k = C_n^k * b^k
                he_so_max = math.comb(n, k_max) * (b**k_max)

                # Kiểm tra điều kiện kết quả < 9999
                if 0 < he_so_max < 9999:
                    break

            # Câu hỏi
            noidungcauhoi = (r"Hệ số có giá trị lớn nhất trong khai triển biểu thức $P(x) = (1 + %sx^2)^{%d}$ thành đa thức bằng bao nhiêu?"
                             % (latex(b) if b != 1 else "", n))

            # Đáp án đúng
            da_d = r"\True $%d$" % he_so_max

            # Tạo các phương án nhiễu
            s_set = set()
            while len(s_set) < 3:
                # Nhiễu bằng cách lấy các hệ số lân cận k_max-1 hoặc k_max+1
                k_sai = random.choice([k_max - 1, k_max + 1, k_max - 2])
                if 0 <= k_sai <= n:
                    val_sai = math.comb(n, k_sai) * (b**k_sai)
                    if val_sai != he_so_max:
                        s_set.add(r"$%d$" % val_sai)

                # Nếu vẫn thiếu phương án nhiễu, cộng trừ ngẫu nhiên
                if len(s_set) < 3:
                    offset = random.choice([10, 20, 50, 100, -10])
                    val_sai = he_so_max + offset
                    if val_sai > 0 and val_sai != he_so_max:
                        s_set.add(r"$%d$" % val_sai)

            list_ans = [da_d] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            limit_val = (b * (n + 1)) / (b + 1)
            loigiai = (r"Khai triển $P(x) = \sum_{k=0}^{%d} C_{%d}^k (%sx^2)^k = \sum_{k=0}^{%d} C_{%d}^k %s^k x^{2k}$. \\ "
                       r"Gọi $a_k = C_{%d}^k %s^k$ là hệ số của $x^{2k}$. \\ "
                       r"Để $a_k$ lớn nhất, ta xét tỷ số $\dfrac{a_{k+1}}{a_k} \ge 1 \Leftrightarrow \dfrac{C_{%d}^{k+1} %s^{k+1}}{C_{%d}^k %s^k} \ge 1$. \\ "
                       r"$\Leftrightarrow \dfrac{%d-k}{k+1} \cdot %d \ge 1 \Leftrightarrow %d(%d-k) \ge k+1 \Leftrightarrow k \le \dfrac{%d}{%d} \approx %.2f$. \\ "
                       r"Vì $k \in \mathbb{N}$ nên chỉ số $k$ ứng với hệ số lớn nhất là $k = %d$. \\ "
                       r"Vậy hệ số lớn nhất là $a_{%d} = C_{%d}^{%d} \cdot %s^{%d} = %d$."
                       % (n, n, b if b != 1 else "", n, n, b, 
                          n, b, n, b, n, b, 
                          n, b, b, n, b*n-1, b+1, limit_val,
                          k_max, k_max, n, k_max, b, k_max, he_so_max))

            # Đáp án ngắn (Số nguyên cụ thể)
            dapan = r"\shortans[0]{$%d$}" % he_so_max

            # Xuất nội dung
            content = (r"\begin{minipage}{\textwidth} " + "\n"
                       r"\begin{ex}" + "\n" + noidungcauhoi + dapan +
                       r"\loigiai{" + loigiai + r"}" + "\n"
                       r"\end{ex}" + "\n" + r"\end{minipage}" + "\n\n")

            return content

