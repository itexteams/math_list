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


def bt_dang21_p4_b1_c1_hh10(self):
            # Khai báo biến
            # Khai báo biến: Chọn ngẫu nhiên hệ số a (có thể tùy chỉnh thêm các số lớn hơn)
            lisdang = [2, 3, 4, 5, 6, 7]
            a_val = random.choice(lisdang)

            # Các bước tính toán cho bài toán a*cos(alpha) - sin(alpha) = 1
            a2 = a_val**2
            a2_plus_1 = a2 + 1
            one_minus_a2 = 1 - a2
            a2_minus_1 = a2 - 1
            two_a = 2 * a_val

            # Tính giá trị các tỉ số lượng giác
            sin_a = Rational(a2_minus_1, a2_plus_1)
            cos_a = Rational(two_a, a2_plus_1)
            tan_a = Rational(a2_minus_1, two_a)

            # Các đáp án trắc nghiệm
            kq_latex = f"${latex(tan_a)}$"

            # Sinh các phương án nhiễu ngẫu nhiên
            s_distractors = [
                f"${latex(Rational(two_a, a2_minus_1))}$",
                f"${latex(Rational(a2_plus_1, two_a))}$",
                f"${latex(Rational(two_a, a2_plus_1))}$",
                f"${latex(Rational(a2_plus_1, a2_minus_1))}$",
                f"${latex(Rational(a2_minus_1, a2_plus_1))}$"
            ]

            # Đảm bảo đáp án nhiễu không trùng đáp án đúng
            if kq_latex in s_distractors:
                s_distractors.remove(kq_latex)

            das1 = random.choice(s_distractors)
            s_distractors.remove(das1)
            das2 = random.choice(s_distractors)
            s_distractors.remove(das2)
            das3 = random.choice(s_distractors)

            # Câu hỏi
            noidungcauhoi = f"Cho biết ${a_val}\\cos\\alpha - \\sin\\alpha = 1$, $0^\\circ < \\alpha < 90^\\circ$. Tính giá trị của $\\tan\\alpha$."

            # Các đáp án
            da_d = ('\\True ' + kq_latex)
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            # Đưa các đáp án vào danh sách và xáo trộn
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xử lý chuẩn hóa hiển thị dấu để không bị "+ -8" mà hiển thị thành "- 8"
            c_term = f"- {-one_minus_a2}" if one_minus_a2 < 0 else f"+ {one_minus_a2}"

            # Nội dung lời giải
            loigiai = (
                "Ta có\\\\\n"
                f"${a_val}\\cos\\alpha - \\sin\\alpha = 1 \\Leftrightarrow {a_val}\\cos\\alpha = \\sin\\alpha + 1 \\rightarrow {a2}\\cos^2\\alpha = (\\sin\\alpha + 1)^2$\\\\\n"
                f"$\\Leftrightarrow {a2}(1 - \\sin^2\\alpha) = \\sin^2\\alpha + 2\\sin\\alpha + 1 \\Leftrightarrow {a2_plus_1}\\sin^2\\alpha + 2\\sin\\alpha {c_term} = 0 \\Leftrightarrow \\left[ \\begin{{array}}{{l}} \\sin\\alpha = -1 \\\\ \\sin\\alpha = {latex(sin_a)} \\end{{array}} \\right.$\\\\\n"
                "$\\sin\\alpha = -1$: không thỏa mãn vì $0^\\circ < \\alpha < 90^\\circ$.\\\\\n"
                f"$\\sin\\alpha = {latex(sin_a)} \\Rightarrow \\cos\\alpha = {latex(cos_a)} \\Rightarrow \\tan\\alpha = \\frac{{\\sin\\alpha}}{{\\cos\\alpha}} = {latex(tan_a)}$."
            )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


