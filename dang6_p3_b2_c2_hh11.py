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


def bt_dang6_p3_b2_c2_hh11(self):
            # Khai báo biến
            # Bước 1: Khởi tạo giá trị ngẫu nhiên cho a
            val_a = random.randint(1, 9)

            # Bước 2: Tính toán các thông số hình học
            side = 2 * val_a
            sa_val_exact = Rational(val_a, 2) * sqrt(3)
            am_val_exact = val_a * sqrt(3)

            # Tính diện tích chính xác (phân số)
            dien_tich_exact = Rational(3 * val_a**2, 4)

            # Bước 3: Làm tròn kết quả đến hàng phần chục
            # Chuyển sang float rồi dùng Decimal để làm tròn chuẩn
            dt_float = float(dien_tich_exact)
            kq_decimal = Decimal(str(dt_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            da_dung_str = str(kq_decimal).replace('.', ',')

            # Tạo các phương án trắc nghiệm sai (làm tròn tương tự)
            def generate_distractor(offset):
                val = dt_float + offset
                if val <= 0: val = dt_float * 0.5 # Tránh số âm
                res = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                return '$%s$' % str(res).replace('.', ',')

            s = [
                generate_distractor(1.2),
                generate_distractor(-0.8),
                generate_distractor(2.5),
                generate_distractor(-1.5),
                generate_distractor(0.5),
                generate_distractor(-0.3)
            ]

            random.shuffle(s)
            # Lấy 3 đáp án sai không trùng đáp án đúng
            list_wrong = []
            for item in s:
                if item != '$%s$' % da_dung_str and len(list_wrong) < 3:
                    list_wrong.append(item)

            # Bước 4: Nội dung câu hỏi và TikZ
            noidungcauhoi = (
                'Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $%s$, $SA \\perp (ABC)$, $SA = \\frac{%s\\sqrt{3}}{2}$. '
                'Gọi $(P)$ là mặt phẳng đi qua $A$ và vuông góc với $BC$. Thiết diện của hình chóp $S.ABC$ được cắt bởi $(P)$ có diện tích bằng bao nhiêu? (làm tròn đến hàng phần chục).'
                % (latex(2 * val_a), latex(val_a))
            )

            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1, line width=1pt, >=stealth]\n'
                '  \\coordinate (A) at (0,0);\n'
                '  \\coordinate (B) at (-1.5,-1.5);\n'
                '  \\coordinate (C) at (3,-1.5);\n'
                '  \\coordinate (S) at (0,3.5);\n'
                '  \\coordinate (M) at (0.75,-1.5);\n'
                '  \\draw[dashed] (S)--(A) (A)--(B) (A)--(C) (A)--(M);\n'
                '  \\draw (S)--(B)--(C)--cycle;\n'
                '  \\draw (S)--(M);\n'
                '  \\draw (0.2,0) -- (0.2,0.2) -- (0,0.2);\n'
                '  \\node[above] at (S) {$S$};\n'
                '  \\node[left] at (A) {$A$};\n'
                '  \\node[left] at (B) {$B$};\n'
                '  \\node[right] at (C) {$C$};\n'
                '  \\node[below] at (M) {$M$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            # Bước 5: Nội dung lời giải chi tiết
            loigiai = (
                'Gọi $M$ là trung điểm của $BC$. Vì tam giác $ABC$ đều cạnh $%s$ nên đường cao $AM = \\frac{%s \\cdot \\sqrt{3}}{2} = %s\\sqrt{3}$. \\\\'
                'Ta có $SA \\perp (ABC) \\implies SA \\perp BC$. \\\\'
                'Vì $BC \\perp AM$ và $BC \\perp SA$ nên $BC \\perp \\left( SAM \\right)$. \\\\'
                'Do đó, mặt phẳng $(P)$ đi qua $A$ và vuông góc với $BC$ chính là mặt phẳng $\\left( SAM \\right)$. \\\\'
                'Thiết diện của hình chóp cắt bởi mặt phẳng $(P)$ là tam giác $SAM$ vuông tại $A$ (do $SA \\perp AM$). \\\\'
                'Diện tích thiết diện là: \\\\'
                '$S_{\\triangle SAM} = \\frac{1}{2} \\cdot SA \\cdot AM = \\frac{1}{2} \\cdot \\frac{%s\\sqrt{3}}{2} \\cdot %s\\sqrt{3} = \\frac{3 \\cdot %s^2}{4} = %s \\approx %s$.'
                % (latex(2 * val_a), latex(2 * val_a), latex(val_a), latex(val_a), latex(val_a), latex(val_a), 
                   str(latex(dien_tich_exact)).replace('.', ','), da_dung_str)
            )
            dapan='\\shortans[0]{$%s$}\n'%(da_dung_str)
            # Bước 6: Xuất content
            list_ans = ['\\True $%s$' % da_dung_str, list_wrong[0], list_wrong[1], list_wrong[2]]
            random.shuffle(list_ans)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + str(tikz_code) + str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

