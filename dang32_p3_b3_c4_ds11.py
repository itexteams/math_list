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


def bt_dang32_p3_b3_c4_ds11(self):

        while True:  # LẶP ĐẾN KHI SINH ĐƯỢC BÀI HỢP LỆ
            # ----------------------
            # RANDOM THAM SỐ
            # ----------------------
            b = random.randint(3, 5)
            c = random.randint(11, 15)
            d = random.randint(2, 5)
            v_muc_tieu = random.randint(9, 11)

            # ----------------------
            # LIÊN TỤC TẠI t = 5
            # ----------------------
            v_tai_5 = -25 + 5*b + c
            a_val = Rational(v_tai_5 + d, 5)

            # ----------------------
            # GIẢI PT GIAI ĐOẠN 1
            # ----------------------
            pt1 = -t**2 + b*t + c - v_muc_tieu
            roots1 = solve(pt1, t)

            t1_val = None
            for r in roots1:
                r_float = float(r.evalf())
                if 0 <= r_float <= 5:
                    t1_val = r
                    break

            if t1_val is None:
                continue  # random lại bài

            # ----------------------
            # GIAI ĐOẠN 2
            # ----------------------
            t2_val = Rational(v_muc_tieu + d, a_val)

            if float(t2_val.evalf()) <= 5 or float(t2_val.evalf()) > 10:
                continue

            break  # bài hợp lệ

        # ======================
        # TÍNH KẾT QUẢ
        # ======================
        tong_t = t1_val + t2_val
        kq_float = float(tong_t.evalf())
        kq_str = str(
            Decimal(str(kq_float)).quantize(
                Decimal('0.1'), rounding=ROUND_HALF_UP
            )
        ).replace('.', ',')

        da_dung = f"${kq_str}$"

        # ======================
        # ĐÁP ÁN NHIỄU
        # ======================
        s = []
        while len(s) < 3:
            sai = Decimal(
                str(kq_float + random.choice([-1.2, -0.8, 0.5, 1.5, 2.1]))
            ).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            sai_str = f"${str(sai).replace('.', ',')}$"
            if sai_str != da_dung and sai_str not in s:
                s.append(sai_str)

        # ======================
        # NỘI DUNG CÂU HỎI
        # ======================
        noidungcauhoi = (
            f"Hàm số $v(t)=\\begin{{cases}}"
            f"-t^2+{b}t+{c} & 0\\le t\\le5 \\\\ "
            f"{latex(a_val)}t-{d} & 5<t\\le10"
            f"\\end{{cases}}$ mô tả vận tốc (m/s) của một vật. "
            f"Trong 10 giây đầu, vật đạt vận tốc ${v_muc_tieu}$ m/s "
            f"tại hai thời điểm $t_1,t_2$. Tính $t_1+t_2$ "
            f"(làm tròn đến hàng phần mười)."
        )

        # ======================
        # LỜI GIẢI
        # ======================
        loigiai = (
            f"Hàm số liên tục tại $t=5$ nên $5a-{d}={v_tai_5}$ "
            f"$\\Rightarrow a={latex(a_val)}$.\\\\ "
            f"Giải $v(t)={v_muc_tieu}$ ta được "
            f"$t_1={latex(t1_val)},\\ t_2={latex(t2_val)}$.\\\\ "
            f"Suy ra $t_1+t_2\\approx {kq_str}$."
        )

        # ======================
        # XUẤT LATEX
        # ======================
        dapan = f'\\shortans[0]{{${kq_str}$}}\n'
        content = (
            '\\begin{minipage}{\\textwidth}\n'
            '\\begin{ex}\n'
            + noidungcauhoi + '\n'
            + dapan +
            '\\loigiai{' + loigiai + '}\n'
            '\\end{ex}\n'
            '\\end{minipage}\n\n')

        self.content_textedit.append(content)


