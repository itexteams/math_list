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


def bt_dang15_p3_b3_c6_ds11(self):
            # Khai báo biến
            # Các bộ (r1, r2, r3) tính theo % (ví dụ 5 = 0,05)
            cac_bo_so = [
                (5, 4, 3),    # k = 3, N = 49997, a=9, b=9, c=9, S = 9*9-9 = 72
                (2, 5, 6),    # k = 3, N = 49997, a=9, b=9, c=9, S = 9*9-9 = 72
                (5, 4, 13),   # k = 13, N = 49987, a=9, b=9, c=8, S = 9*9-8 = 73
                (2, 10, 13),  # k = 13, N = 49987, a=9, b=9, c=8, S = 9*9-8 = 73
                (5, 12, 11),  # k = 33, N = 49967, a=9, b=9, c=6, S = 9*9-6 = 75
                (2, 10, 33),  # k = 33, N = 49967, a=9, b=9, c=6, S = 9*9-6 = 75
                (5, 4, 23),   # k = 23, N = 49977, a=9, b=9, c=7, S = 9*9-7 = 74
            ]

            r_pick = list(random.choice(cac_bo_so))
            random.shuffle(r_pick)
            r1, r2, r3 = r_pick

            # Chuyển sang định dạng chuỗi thập phân dấu phẩy
            p1_s = f"{r1/100:.2f}".replace('.', ',')
            p2_s = f"{r2/100:.2f}".replace('.', ',')
            p3_s = f"{r3/100:.2f}".replace('.', ',')

            # Tính toán các giá trị
            k = (r1 * r2 * r3) // 20
            num_p = 50000 - k
            a = (num_p // 1000) % 10
            b = (num_p // 100) % 10
            c = (num_p // 10) % 10
            S_val = a * b - c

            # Bước 4: Tạo các phương án nhiễu
            da_dung = f"${S_val}$"
            cac_phuong_an_sai = set()
            while len(cac_phuong_an_sai) < 3:
                nhieu = S_val + random.choice([-2, -1, 1, 2, 5, 10, -5, -10])
                if nhieu != S_val and nhieu > 0:
                    cac_phuong_an_sai.add(f"${nhieu}$")

            list_sai = list(cac_phuong_an_sai)

            # Nội dung câu hỏi
            noidungcauhoi = (
                "Trong phòng học của An có ba bóng đèn và xác suất hỏng của chúng lần lượt bằng "
                f"${p1_s}; {p2_s}; {p3_s}$. Chỉ cần có một bóng đèn sáng thì An vẫn có thể làm bài tập được. "
                "Xác suất để An có thể làm bài tập có dạng $\\frac{\\overline{4abc7}}{50000} \\left( a; b; c \\in \\mathbb{N} \\right)$, "
                "biết tình trạng (sáng hoặc bị hỏng) của mỗi bóng đèn không ảnh hưởng đến tình trạng các bóng còn lại. "
                "Giá trị $S = a \\cdot b - c$ bằng bao nhiêu?"
            )

            # Nội dung lời giải chi tiết
            loigiai = (
                f"Gọi $A_i \\left( 1 \\le i \\le 3, i \\in \\mathbb{{N}} \\right)$ là biến cố: \"Bóng đèn thứ $i$ sáng bình thường\".\\\\ "
                "An không thể làm bài tập nếu cả ba bóng đèn đều bị hỏng, khi đó xác suất là:\\\\ "
                f"$P\\left( \\bar{{A}}_1 \\bar{{A}}_2 \\bar{{A}}_3 \\right) = P\\left( \\bar{{A}}_1 \\right) \\cdot P\\left( \\bar{{A}}_2 \\right) \\cdot P\\left( \\bar{{A}}_3 \\right) = {p1_s} \\cdot {p2_s} \\cdot {p3_s} = \\frac{{{k}}}{{50000}}$.\\\\ "
                "Gọi $P$ là xác suất để An có thể làm bài tập, ta có:\\\\ "
                f"$P = 1 - P\\left( \\bar{{A}}_1 \\bar{{A}}_2 \\bar{{A}}_3 \\right) = 1 - \\frac{{{k}}}{{50000}} = \\frac{{{num_p}}}{{50000}}$.\\\\ "
                f"Khi đó, đối chiếu với dạng $\\frac{{\\overline{{4abc7}}}}{{50000}}$ ta có: "
                f"$\\begin{{cases}} a = {a} \\\\ b = {b} \\\\ c = {c} \\end{{cases}} \\Rightarrow S = a \\cdot b - c = {a} \\cdot {b} - {c} = {S_val}$."
            )
            dapan=' \\shortans[0]{$%s$} '%(S_val) 
            # Sắp xếp đáp án
            da_d = '\\True ' + da_dung
            list_ans = [da_d, list_sai[0], list_sai[1], list_sai[2]]
            random.shuffle(list_ans)

            # Xuất nội dung theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

