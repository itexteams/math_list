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


def bt_dang22_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # --- BƯỚC 3: TẠO GIÁ TRỊ NGẪU NHIÊN ĐỂ KẾT QUẢ LUÔN NGUYÊN ---
            # Chọn a1 là số chẵn để S1 = (1/2)*a1*t1^2 luôn nguyên
            a1 = random.choice([2, 4, 6]) 
            t1 = random.randint(5, 15)

            # Vận tốc tại thời điểm bắt đầu phanh
            v_tai_t1 = a1 * t1

            # Tìm các ước số của v_tai_t1 để chọn a2 sao cho thời gian phanh là số nguyên
            # Ta chọn ước số trong khoảng từ 2 đến 10 để bài toán thực tế
            uoc_so = [i for i in range(2, 11) if v_tai_t1 % i == 0]
            if not uoc_so: # Phòng trường hợp hiếm không có ước trong khoảng 2-10
                a2_tri_tuyet_doi = 2 
                # Nếu không có ước, ta ép a1*t1 phải chia hết cho 2 (đã thỏa do a1 chẵn)
            else:
                a2_tri_tuyet_doi = random.choice(uoc_so)

            a2 = -a2_tri_tuyet_doi # Gia tốc phanh phải âm

            # --- TÍNH TOÁN CÁC GIÁ TRỊ ---
            v1_func = a1 * t
            s1_val = int(integrate(v1_func, (t, 0, t1)))

            v2_func = v_tai_t1 + a2 * (t - t1)
            v2_expanded = expand(v2_func)

            # Thời điểm dừng hẳn v2(t) = 0
            thoi_gian_phanh = int(v_tai_t1 / a2_tri_tuyet_doi)
            t_stop = t1 + thoi_gian_phanh

            # Quãng đường phanh S2 = 1/2 * v_tai_t1 * thoi_gian_phanh
            s2_val = int(integrate(v2_func, (t, t1, t_stop)))
            s_total = s1_val + s2_val

            # --- NỘI DUNG CÂU HỎI ---
            noidungcauhoi = (r'''Một ô tô bắt đầu chuyển động nhanh dần đều với vận tốc $v_1(t) = %st \,(\text{m/s})$, trong đó thời gian $t$ tính bằng giây. Sau khi chuyển động được $%s$ giây thì ô tô gặp chướng ngại vật và người tài xế phanh gấp, ô tô tiếp tục chuyển động chậm dần đều với vận tốc $v_2(t)$ và gia tốc là $a = %s \,(\text{m/s}^2)$ cho đến khi dừng hẳn.''' 
                            % (latex(a1), latex(t1), latex(a2)))

            ########################################################################
            # a) Nhận biết
            ########################################################################
            da_a_d = r'\True Quãng đường ô tô đi được từ lúc bắt đầu đến khi phanh gấp là $%s\text{ m}$' % latex(s1_val)
            da_a_s = r'Quãng đường ô tô đi được từ lúc bắt đầu đến khi phanh gấp là $%s\text{ m}$' % latex(s1_val + random.randint(5, 15))
            list_da_a = [da_a_d, da_a_s]

            loigiai_a = (r'''Ta có quãng đường giai đoạn 1: $S_1 = \int\limits_{0}^{%s} v_1(t) \text{d}t = \int\limits_{0}^{%s} %st \text{d}t = %st^2 \Big|_{0}^{%s} = %s$.'''
                        % (latex(t1), latex(t1), latex(a1), latex(sp.Rational(a1, 2)), latex(t1), latex(s1_val)))

            ########################################################################
            # b) Thông hiểu
            ########################################################################
            da_b_d = r'\True Vận tốc của ô tô tại thời điểm người lái xe bắt đầu phanh là $%s\text{ m/s}$' % latex(v_tai_t1)
            da_b_s = r'Vận tốc của ô tô tại thời điểm người lái xe bắt đầu phanh là $%s\text{ m/s}$' % latex(v_tai_t1 + 2)
            list_da_b = [da_b_d, da_b_s]

            loigiai_b = (r'''Vận tốc tại thời điểm $t = %s$ là: $v_1(%s) = %s \cdot %s = %s \,(\text{m/s})$.'''
                        % (latex(t1), latex(t1), latex(a1), latex(t1), latex(v_tai_t1)))

            ########################################################################
            # c) Vận dụng
            ########################################################################
            da_c_d = r'\True Thời gian từ lúc ô tô giảm tốc độ cho đến khi dừng hẳn là $%s$ giây' % latex(thoi_gian_phanh)
            da_c_s = r'Thời gian từ lúc ô tô giảm tốc độ cho đến khi dừng hẳn là $%s$ giây' % latex(thoi_gian_phanh + 2)
            list_da_c = [da_c_d, da_c_s]

            loigiai_c = (r'''Vận tốc giai đoạn phanh: $v_2(t) = %s %s(t - %s) = %s$. \\ Ô tô dừng hẳn khi $v_2(t) = 0 \Leftrightarrow t = %s$. \\ Thời gian phanh là: $%s - %s = %s$ (giây).'''
                        % (latex(v_tai_t1), latex(a2), latex(t1), latex(v2_expanded), latex(t_stop), latex(t_stop), latex(t1), latex(thoi_gian_phanh)))

            ########################################################################
            # d) Vận dụng cao
            ########################################################################
            da_d_d = r'\True Tổng quãng đường ô tô đi được từ lúc bắt đầu đến khi dừng hẳn là $%s\text{ m}$' % latex(s_total)
            da_d_s = r'Tổng quãng đường ô tô đi được từ lúc bắt đầu đến khi dừng hẳn là $%s\text{ m}$' % latex(s_total - 10)
            list_da_d = [da_d_d, da_d_s]

            loigiai_d = (r'''Quãng đường giai đoạn phanh: $S_2 = \int\limits_{%s}^{%s} (%s) \text{d}t = %s$. \\ Vậy tổng quãng đường là $S = S_1 + S_2 = %s + %s = %s \,(\text{m})$.'''
                        % (latex(t1), latex(t_stop), latex(v2_expanded), latex(s2_val), latex(s1_val), latex(s2_val), latex(s_total)))

            # --- ĐẢM BẢO SỐ CÂU ĐÚNG TỪ 1 ĐẾN 3 ---
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                d_a = random.choice(list_da_a)
                d_b = random.choice(list_da_b)
                d_c = random.choice(list_da_c)
                d_d = random.choice(list_da_d)
                if 1 <= count_true([d_a, d_b, d_c, d_d]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + d_a + '}\n'
                '{' + d_b + '}\n'
                '{' + d_c + '}\n'
                '{' + d_d + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_a + '\n'
                '\\item ' + loigiai_b + '\n'
                '\\item ' + loigiai_c + '\n'
                '\\item ' + loigiai_d + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

