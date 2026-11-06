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


def bt_dang17_p3_b1_c1_ds10(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Năm hiện tại theo hệ thống là 2026
        current_year = 2026

        # Random hình thức số lượng nghiệm phân biệt của phương trình bậc ba (3 hoặc 4 phần tử nếu mở rộng lên bậc cao, ở đây dùng 3 hoặc 4 nghiệm nguyên)
        # Để giữ nguyên tính chất của bài toán gốc (phương trình bậc 3 có 3 nghiệm phân biệt):
        # Chọn 3 nghiệm nguyên ngẫu nhiên phân biệt trong khoảng từ -3 đến 5
        roots = random.sample(range(-3, 6), 3)
        roots.sort()

        x = symbols('x')
        # Lập phương trình bậc ba từ các nghiệm phân biệt: (x - r1)(x - r2)(x - r3) = 0
        poly = expand((x - roots[0]) * (x - roots[1]) * (x - roots[2]))
        poly_latex = latex(poly)

        # Tập hợp S chứa 3 phần tử nghiệm phân biệt
        # Số tập con có 2 phần tử của tập S có 3 phần tử luôn là C_3^2 = 3
        n_val = 3

        # Tính giá trị T = current_year * n_val
        kq_num = current_year * n_val
        da = '$%s$' % latex(kq_num)

        # Tạo các phương án sai xung quanh đáp án đúng (không trùng kq_num)
        s_candi = [current_year * 1, current_year * 2, current_year * 4, current_year * 6, kq_num - 2026, kq_num + 2026]
        s_candi = [v for v in s_candi if v != kq_num and v > 0]

        s = []
        for val in random.sample(s_candi, 3):
            s.append('$%s$' % latex(val))

        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Tạo chuỗi hiển thị danh sách các nghiệm và các tập con 2 phần tử
        roots_str = "; ".join(str(r) for r in roots)

        subsets_list = []
        subsets_list.append("\\{%s; %s\\}" % (roots[0], roots[1]))
        subsets_list.append("\\{%s; %s\\}" % (roots[0], roots[2]))
        subsets_list.append("\\{%s; %s\\}" % (roots[1], roots[2]))
        subsets_str = ", ".join(subsets_list)

        # Câu hỏi
        noidungcauhoi = ('''Xét mệnh đề chứa biến $P(x)$: "$%s = 0$". Gọi $S$ là tập hợp các giá trị của biến $x$ để $P(x)$ là mệnh đề đúng. Giả sử $n$ là số tập con có hai phần tử của $S$. Giá trị $T = %sn$ bằng bao nhiêu?'''
                            % (poly_latex, latex(current_year)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Tạo chuỗi lời giải chi tiết từng bước
        loigiai = ('''Ta giải phương trình tìm các giá trị của biến $x$ để mệnh đề $P(x)$ đúng: \\\\
    $%s = 0 \\Leftrightarrow \\hoac{& x = %s \\\\& x = %s \\\\& x = %s }$. \\\\
    Vậy tập hợp tất cả các nghiệm là $S = \\{%s\\}$. \\\\
    Số tập con có hai phần tử của tập hợp $S$ gồm các cặp giá trị là: $%s$. \\\\
    Suy ra số lượng tập con thỏa mãn là $n = %s$. \\\\
    Vậy giá trị của biểu thức $T$ cần tìm là: \\\\
    $T = %s \\cdot n = %s \\cdot %s = %s$.'''
                    % (poly_latex, latex(roots[0]), latex(roots[1]), latex(roots[2]), roots_str, subsets_str, latex(n_val), latex(current_year), latex(current_year), latex(n_val), latex(kq_num)))
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_num))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
    return content

