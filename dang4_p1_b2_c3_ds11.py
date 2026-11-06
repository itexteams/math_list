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


def bt_dang4_p1_b2_c3_ds11(self):
    # 1. Khai báo và chọn dạng
    lisdang = ['1', '2', '3', '4']
    dang = random.choice(lisdang)

    # Thời gian (phút), ví dụ bắt đầu từ 35, 40, 45, 50...
    lisv = [35, 40, 45, 50, 55]
    v = random.choice(lisv)

    # Độ rộng mỗi khoảng thời gian (phút)
    lisk = [5, 10]
    k = random.choice(lisk)

    # 2. Vòng lặp tạo mẫu số liệu thỏa mãn tính chất chẵn/lẻ của dạng
    while True:
        hs = [randint(5, 30) for _ in range(5)]
        tong = sum(hs)
        tong1 = (tong - 1) // 2 if tong % 2 != 0 else tong // 2

        if dang == '4' and (tong % 2 == 0 and tong1 % 2 != 0):
            break
        elif dang == '3' and (tong % 2 == 0 and tong1 % 2 == 0):
            break
        elif dang == '2' and (tong % 2 != 0 and tong1 % 2 != 0):
            break
        elif dang == '1' and (tong % 2 != 0 and tong1 % 2 == 0):
            break

    n = tong
    hs1, hs2, hs3, hs4, hs5 = hs
    frequencies = hs
    intervals = [(v + i * k, v + (i + 1) * k) for i in range(5)]

    # 3. Tính tần số tích lũy để tìm chính xác nhóm chứa trung vị
    cum_freq = []
    curr = 0
    for f in frequencies:
        curr += f
        cum_freq.append(curr)

    # Vị trí xác định nhóm theo SGK Toán 11:
    target_pos = (n + 1) / 2 if n % 2 != 0 else n / 2

    q2_idx = 0
    for i, cf in enumerate(cum_freq):
        if cf >= target_pos:
            q2_idx = i
            break

    Q2_interval = intervals[q2_idx]
    Q2_interval_frequency = frequencies[q2_idx]
    total_freq_before_Q2 = cum_freq[q2_idx - 1] if q2_idx > 0 else 0

    L = Q2_interval[0]
    h = Q2_interval[1] - Q2_interval[0]

    # Công thức trung vị của mẫu số liệu ghép nhóm:
    kqQ2 = L + Rational(Rational(n, 2) - total_freq_before_Q2, Q2_interval_frequency) * h

    # 4. Tạo các phương án trắc nghiệm
    da = '$M_e=%s$' % (latex(kqQ2))
    s = [
        '$M_e=%s$' % (latex(kqQ2 + 1)),
        '$M_e=%s$' % (latex(kqQ2 + 2)),
        '$M_e=%s$' % (latex(kqQ2 + 3)),
        '$M_e=%s$' % (latex(kqQ2 - 1)),
        '$M_e=%s$' % (latex(kqQ2 - 2)),
        '$M_e=%s$' % (latex(kqQ2 - 3)),
    ]
    sai = random.sample(s, 3)

    da_d = '\\True ' + str(da)
    list_1 = [da_d, sai[0], sai[1], sai[2]]
    random.shuffle(list_1)

    # 5. Nội dung câu hỏi (Thời gian làm bài kiểm tra)
    noidungcauhoi = (
        'Thời gian hoàn thành bài kiểm tra (tính bằng phút) của các bạn học sinh lớp 11B được cho trong bảng sau:\n'
        '\\begin{center}\n'
        '\\begin{tabular}{|c|c|c|c|c|c|}\n'
        '\\hline\n'
        'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\\n'
        '\\hline\n'
        'Số học sinh & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\\n'
        '\\hline\n'
        '\\end{tabular}\n'
        '\\end{center}\n'
        'Trung vị của mẫu số liệu ghép nhóm trên là'
        % (
            latex(intervals[0][0]), latex(intervals[0][1]),
            latex(intervals[1][0]), latex(intervals[1][1]),
            latex(intervals[2][0]), latex(intervals[2][1]),
            latex(intervals[3][0]), latex(intervals[3][1]),
            latex(intervals[4][0]), latex(intervals[4][1]),
            latex(hs1), latex(hs2), latex(hs3), latex(hs4), latex(hs5),
        )
    )

    # 6. Nội dung lời giải theo từng trường hợp chẵn / lẻ
    if n % 2 == 0:
        pos1 = n // 2
        pos2 = pos1 + 1
        loigiai_vitri = (
            'Vì cỡ mẫu $n=%s$ là số chẵn nên trung vị của mẫu số liệu gốc là '
            '$\\dfrac{x_{%d} + x_{%d}}{2}$. Do cả hai giá trị $x_{%d}$ và $x_{%d}$ đều thuộc nhóm $[%s; %s)$ '
            'nên nhóm chứa trung vị là $[%s; %s)$.\\\\\n'
            % (
                latex(n), pos1, pos2, pos1, pos2,
                latex(Q2_interval[0]), latex(Q2_interval[1]),
                latex(Q2_interval[0]), latex(Q2_interval[1]),
            )
        )
    else:
        pos = (n + 1) // 2
        loigiai_vitri = (
            'Vì cỡ mẫu $n=%s$ là số lẻ nên trung vị của mẫu số liệu gốc là $x_{%d}$. '
            'Do $x_{%d}$ thuộc nhóm $[%s; %s)$ nên nhóm chứa trung vị là $[%s; %s)$.\\\\\n'
            % (
                latex(n), pos, pos,
                latex(Q2_interval[0]), latex(Q2_interval[1]),
                latex(Q2_interval[0]), latex(Q2_interval[1]),
            )
        )

    loigiai = (
        'Cỡ mẫu $n=%s$. Giả sử dãy số liệu gốc gồm thời gian làm bài của $%s$ học sinh được xếp theo thứ tự không giảm là $x_1, x_2, \\dots, x_{%s}$.\\\\\n'
        '%s'
        '\\hspace*{0.5cm} Do đó, trung vị của mẫu số liệu ghép nhóm là:\\\\\n'
        '\\hspace*{0.5cm} $M_e = %s + \\dfrac{\\frac{%s}{2} - %s}{%s} \\cdot %s = %s$.'
        % (
            latex(n), latex(n), latex(n),
            loigiai_vitri,
            latex(L), latex(n), latex(total_freq_before_Q2),
            latex(Q2_interval_frequency), latex(h), latex(kqQ2),
        )
    )

    # 7. Xuất đề trắc nghiệm
    content = (
        '\\begin{minipage}{\\textwidth}\n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choice\n'
        '{' + str(list_1[0]) + '}\n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n\\end{minipage}\n\n').replace('\\frac', '\\dfrac').replace('.0', '')

    return content

