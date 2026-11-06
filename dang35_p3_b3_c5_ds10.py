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


def bt_dang35_p3_b3_c5_ds10(self):
            # Chọn n cụ thể trong khoảng [4, 7] để C(2n, n) < 9999
            n = random.randint(4, 7)
            m = 2 * n

            # Tính giá trị số nguyên của tổng S = C(2n, n)
            kq_val = math.comb(m, n)

            # Câu hỏi
            noidungcauhoi = (r"Tổng $S = \left(C_{%d}^0\right)^2 + \left(C_{%d}^1\right)^2 + \left(C_{%d}^2\right)^2 + \dots + \left(C_{%d}^{%d}\right)^2$ bằng bao nhiêu?"
                             % (n, n, n, n, n))

            # Đáp án đúng dạng số nguyên
            da_dung = r"\True $%d$" % kq_val

            # Tạo các phương án nhiễu (số nguyên)
            s_set = set()
            while len(s_set) < 3:
                # Các sai lầm: tính C(2n, n-1), tính 2^m, hoặc sai lệch đơn vị
                sai_1 = math.comb(m, n - 1)
                sai_2 = 2**m
                offset = random.choice([1, -1, 10, 100, 2, -2])

                nhieu = random.choice([sai_1, sai_2, kq_val + offset])
                if nhieu != kq_val and 0 < nhieu < 20000:
                    s_set.add(r"$%d$" % nhieu)

            list_ans = [da_dung] + list(s_set)
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết
            loigiai = (r"Ta có công thức tính tổng bình phương các hệ số nhị thức: \\ "
                       r"$\sum_{k=0}^{n} \left(C_n^k\right)^2 = C_{2n}^n$. \\ "
                       r"Áp dụng với $n = %d$, ta có: \\ "
                       r"$S = \left(C_{%d}^0\right)^2 + \left(C_{%d}^1\right)^2 + \dots + \left(C_{%d}^{%d}\right)^2 = C_{%d}^{%d}$. \\ "
                       r"Giá trị của tổng là: $C_{%d}^{%d} = %d$."
                       % (n, n, n, n, n, m, n, m, n, kq_val))

            # Đáp án ngắn (Điền số nguyên cụ thể)
            dapan = r"\shortans[0]{$%d$}" % kq_val

            # Xuất nội dung
            content = (r"\begin{minipage}{\textwidth} " + "\n"
                       r"\begin{ex}" + "\n" + noidungcauhoi + dapan +
                       r"\loigiai{" + loigiai + r"}" + "\n"
                       r"\end{ex}" + "\n" + r"\end{minipage}" + "\n\n")

            return content

