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


def bt_dang7_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # 1. Sinh ngẫu nhiên cho mệnh đề B: x^2 + ax - b = 0 hoặc tương tự sao cho luôn có nghiệm thực
        # Chọn nghiệm nguyên đẹp để tạo phương trình
        x1 = random.randint(1, 3)
        x2 = -random.randint(4, 6)
        b_coeff = x1 + x2
        c_coeff = x1 * x2
        # Phương trình: x^2 - b_coeff*x + c_coeff = 0 -> x^2 + b_val*x - c_val = 0
        b_val = -b_coeff
        c_val = -c_coeff

        # 2. Sinh ngẫu nhiên cho mệnh đề C: \sqrt{n} là số nguyên (chọn n không phải số chính phương)
        perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
        n_val = random.randint(20, 150)
        while n_val in perfect_squares:
            n_val = random.randint(20, 150)

        # 3. Sinh ngẫu nhiên cho mệnh đề D: x^4 + d1*x^2 + d2 = 0 vô nghiệm (chọn d1, d2 > 0)
        d1 = random.randint(2, 5)
        d2 = random.randint(2, 6)

        # Đánh giá tính đúng sai của các mệnh đề gốc:
        # A: "Tổng hai cạnh của một tam giác lớn hơn cạnh còn lại" -> Luôn ĐÚNG (bất đẳng thức tam giác) -> Phủ định SAI
        # B: "\exists x \in \mathbb{R} : x^2 + bx + c = 0" -> ĐÚNG (vì có nghiệm thực) -> Phủ định SAI
        # C: "\sqrt{n} là số nguyên" -> SAI (vì n không phải số chính phương) -> Phủ định ĐÚNG
        # D: "Phương trình x^4 + d1*x^2 + d2 = 0 có nghiệm" -> SAI (vì vế trái >= d2 > 0) -> Phủ định ĐÚNG

        # Số lượng mệnh đề phủ định ĐÚNG luôn là 2 (Mệnh đề phủ định của C và D)
        kq_num = 2
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai xung quanh đáp án đúng (từ 0 đến 4)
        s_candi = [0, 1, 3, 4]
        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Câu hỏi
        noidungcauhoi = ('''Cho các mệnh đề: \\\\
    $A$: "Tổng hai cạnh của một tam giác lớn hơn cạnh còn lại". \\\\
    $B$: "$\\exists x \\in \\mathbb{R} : x^2 + %sx %s = 0$". \\\\
    $C$: "$\\sqrt{%s}$ là số nguyên". \\\\
    $D$: "Phương trình: $x^4 + %sx^2 + %s = 0$ có nghiệm". \\\\
    Mệnh đề phủ định của các mệnh đề trên có bao nhiêu mệnh đề đúng?'''
                            % (latex(b_val), latex(c_coeff), latex(n_val), latex(d1), latex(d2)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải chi tiết
        loigiai = ('''Để tìm số mệnh đề phủ định đúng, ta xét tính đúng sai của các mệnh đề ban đầu. Một mệnh đề có phủ định đúng khi và chỉ khi bản thân mệnh đề đó là mệnh đề sai. \\\\
    - Xét mệnh đề $A$: "Tổng hai cạnh của một tam giác lớn hơn cạnh còn lại". Đây là một tính chất hình học luôn đúng (bất đẳng thức tam giác). Do đó mệnh đề $A$ đúng, suy ra mệnh đề phủ định $\\overline{A}$ là sai. \\\\
    - Xét mệnh đề $B$: "$\\exists x \\in \\mathbb{R} : x^2 + %sx %s = 0$". Phương trình bậc hai có $\\Delta = (%s)^2 - 4 \\cdot 1 \\cdot (%s) = %s > 0$ nên phương trình luôn có nghiệm thực. Do đó mệnh đề $B$ đúng, suy ra mệnh đề phủ định \\\\
    $\\overline{B}$: "$\\forall x \\in \\mathbb{R} : x^2 + %sx %s \\neq 0$" là sai. \\\\
    - Xét mệnh đề $C$: "$\\sqrt{%s}$ là số nguyên". Vì $%s$ không phải là số chính phương nên $\\sqrt{%s}$ là số vô tỉ. Do đó mệnh đề $C$ sai, suy ra mệnh đề phủ định $\\overline{C}$ là đúng. \\\\
    - Xét mệnh đề $D$: "Phương trình: $x^4 + %sx^2 + %s = 0$ có nghiệm". Ta có $x^2 \\ge 0$ với mọi $x \\in \\mathbb{R}$, suy ra $x^4 + %sx^2 + %s \\ge %s > 0$. Do đó phương trình vô nghiệm. Mệnh đề $D$ sai, suy ra mệnh đề phủ định $\\overline{D}$ là đúng. \\\\
    Kết luận: Có tất cả $%s$ mệnh đề phủ định đúng (gồm $\\overline{C}$ và $\\overline{D}$).'''
                    % (latex(b_val), latex(c_coeff), latex(b_val), latex(c_coeff), latex(b_val**2 - 4*c_coeff), 
                        latex(b_val), latex(c_coeff), latex(n_val), latex(n_val), latex(n_val), 
                        latex(d1), latex(d2), latex(d1), latex(d2), latex(d2), latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

