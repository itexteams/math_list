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


def bt_dang28_p3_b2_c4_ds10(self):
            # Khai báo biến
            # --- BƯỚC 1: KHAI BÁO BIẾN ---
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Dùng vòng lặp để ép kết quả x_optimal < 9999
                while True:
                    # Giảm giá bán ban đầu xuống mức thấp (ví dụ: 6k - 9k)
                    p0 = random.randint(6, 9) * 1000 
                    # So luong ban dau
                    q0 = random.randint(30, 50)
                    # Muc giam gia moi don vi
                    dp = 500 # Giảm bước nhảy giá để x_optimal không bị đẩy đi quá xa
                    # So luong tang them tuong ung
                    dq = random.randint(5, 15)
                    # Gia nhap (phải nhỏ hơn p0)
                    c = random.randint(3, 5) * 1000

                    # --- TINH TOAN LOGIC ĐỂ KIỂM TRA ---
                    he_so_x = Rational(dq, dp)
                    hang_so_q = q0 + he_so_x * p0
                    b = hang_so_q + c * he_so_x

                    # Gia ban toi uu
                    x_optimal = int(b / (2 * he_so_x))

                    # Chỉ thoát vòng lặp nếu x_optimal nhỏ hơn 9999 và hợp lệ
                    if x_optimal < 9999 and x_optimal > c:
                        break

                # --- BƯỚC 2: CÁC TÍNH TOÁN CÒN LẠI ---
                # Loi nhuan cuc dai
                max_profit = int((x_optimal - c) * (hang_so_q - he_so_x * x_optimal))

                # --- BƯỚC 3: ĐIỀU CHỈNH ĐÁP ÁN ---
                da = f"{x_optimal} đồng"

                # Tao cac phuong an sai khong trung voi dap an dung
                s = set()
                while len(s) < 3:
                    # Sai số nhỏ hơn vì giá trị tổng đã nhỏ
                    sai = x_optimal + random.choice([-1000, -500, 500, 1000])
                    if sai != x_optimal and sai > c:
                        s.add(f"{sai} đồng")

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # --- BƯỚC 4: VIẾT LẠI NỘI DUNG ---
                noidungcauhoi = (f"Một cửa hàng bán bưởi Đoan Hùng với giá mỗi quả là {p0} đồng. "
                                f"Với giá này mỗi ngày bán được {q0} quả. Cửa hàng ước tính nếu "
                                f"giảm mỗi quả {dp} đồng thì số bưởi bán tăng thêm được {dq} quả. "
                                f"Giá bán bằng bao nhiêu để cửa hàng thu được lợi nhuận cao nhất, "
                                f"biết giá nhập mỗi quả là {c} đồng?")

                # Đáp án đúng
                da_d = f"\\True {da}"

                # Tron dap an
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (f"Gọi $x$ là giá bán thực tế của mỗi quả bưởi ($x$: đồng, ${c} \\le x \\le {p0}$). \\\\\n"
                        f"Tương ứng với giá bán là $x$ thì số quả bán được là: \\\\\n"
                        f"${q0} + \\frac{{{dq}}}{{{dp}}}({p0} - x) = -{latex(he_so_x)}x + {latex(hang_so_q)}$. \\\\\n"
                        f"Gọi $f(x)$ là hàm lợi nhuận thu được, ta có: \\\\\n"
                        f"$f(x) = (-{latex(he_so_x)}x + {latex(hang_so_q)})(x - {c}) = -{latex(he_so_x)}x^2 + {latex(b)}x - {latex(c * hang_so_q)}$. \\\\\n"
                        f"Lợi nhuận thu được lớn nhất khi hàm $f(x)$ đạt giá trị lớn nhất tại đỉnh Parabol. \\\\\n"
                        f"Ta có: $x = \\frac{{-b}}{{2a}} = {x_optimal}$. \\\\\n"
                        f"$\\Rightarrow \\max f(x) = f({x_optimal}) = {max_profit}$. \\\\\n"
                        f"Vậy với giá bán ${x_optimal}$ đồng mỗi quả bưởi thì cửa hàng thu được lợi nhuận lớn nhất.")

                # Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(x_optimal))

                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                        '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                        '\\loigiai{'+str(loigiai)+'}\n'
                        '\\end{ex}\n \\end{minipage} \n\n')
            return content

