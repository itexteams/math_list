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


def bt_dang22_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Sinh ngẫu nhiên giá trị hằng số để tạo bình phương đầy đủ đẹp (x + k)^2 = x^2 + 2kx + k^2
        # Chọn k ngẫu nhiên từ 1 đến 4, tương ứng hệ số của x là 2k (b_coeff)
        k = random.randint(1, 4)
        b_coeff = 2 * k
        k_square = k ** 2

        # Sinh ngẫu nhiên hằng số trừ đi của m (trong ảnh gốc là m - 2)
        # Ta chọn một giá trị ngẫu nhiên từ 1 đến 5
        sub_val = random.randint(1, 5)

        # Biến đổi: x^2 + b_coeff*x + m - sub_val = (x + k)^2 - k_square + m - sub_val
        # = (x + k)^2 + m - (k_square + sub_val)
        const_total = k_square + sub_val

        # Điều kiện để mệnh đề đúng với mọi x thuộc R là: m - const_total > 0 <=> m > const_total
        # Vì m thuộc Z nên giá trị nhỏ nhất của m là const_total + 1
        kq_num = const_total + 1
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai xung quanh đáp án đúng (không trùng với kq_num và luôn > 0)
        s_candi = [kq_num + 1, kq_num + 2, kq_num - 1, kq_num - 2, const_total]
        s_candi = list(set([v for v in s_candi if v != kq_num and v > 0]))

        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Câu hỏi
        noidungcauhoi = ('''Với $m \\in \\mathbb{Z}$ ta xét mệnh đề $P$: "$\\forall x \\in \\mathbb{R}, x^2 + %sx + m - %s > 0$". Giá trị nhỏ nhất của $m$ để $P$ là mệnh đề đúng bằng bao nhiêu?'''
                            % (latex(b_coeff), latex(sub_val)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo nội dung lời giải chi tiết từng bước
        loigiai = ('''Ta thực hiện biến đổi tam thức bậc hai bằng phương pháp thêm bớt để xuất hiện bình phương sai lệch: \\\\
    Ta có: $x^2 + %sx + m - %s = \\left(x + %s\\right)^2 - %s + m - %s = \\left(x + %s\\right)^2 + m - %s$. \\\\
    Mệnh đề $P$ là mệnh đề đúng khi và chỉ khi bất đẳng thức $x^2 + %sx + m - %s > 0$ nghiệm đúng với mọi số thực $x$. \\\\
    Vì $\\left(x + %s\\right)^2 \\ge 0$ với mọi $x \\in \\mathbb{R}$, nên biểu thức luôn dương khi và chỉ khi hằng số dư lớn hơn $0$: \\\\
    $m - %s > 0 \\Leftrightarrow m > %s$. \\\\
    Vì $m \\in \\mathbb{Z}$ và ta cần tìm giá trị nhỏ nhất của $m$, nên ta lấy số nguyên đầu tiên lớn hơn $%s$. \\\\
    Suy ra $m = %s$. \\\\
    Vậy $m = %s$ là số nguyên nhỏ nhất để mệnh đề $P$ đúng.'''
                    % (latex(b_coeff), latex(sub_val), latex(k), latex(k_square), latex(sub_val), latex(k), latex(const_total),
                        latex(b_coeff), latex(sub_val), latex(k), latex(const_total), latex(const_total), latex(const_total), latex(kq_num), latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

