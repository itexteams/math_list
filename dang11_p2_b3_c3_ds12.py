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


def bt_dang11_p2_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            a_sym = symbols('a')

            # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM ---
            # Random hệ số k của hàm số k*sin(x)
            k = random.randint(2, 9)
            f = k * sin(x)

            # Random tỉ số diện tích ở câu d (m/n)
            # Chọn m, n sao cho 0 < m/n < 1 để a tồn tại trong (0, pi)
            list_ratios = [(1, 2), (2, 3), (1, 3), (3, 4), (2, 5), (3, 5), (4, 5)]
            m_val, n_val = random.choice(list_ratios)
            ratio = Rational(m_val, n_val)

            # Tính toán các giá trị cố định để làm lời giải
            nguyen_ham = -k * cos(x)
            S_tong = 2 * k # Tích phân từ 0 đến pi của k*sin(x)
            Sa_bieu_thuc = k * (1 - cos(a_sym))
            # Giá trị cos(a) ở câu d: k(1-cos(a)) = ratio * (2k) => 1-cos(a) = 2*ratio => cos(a) = 1 - 2*ratio
            cos_a_val = 1 - 2 * ratio

            # --- BƯỚC 2: VIẾT LẠI BÀI TOÁN THEO MẪU ---

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hàm số $y = f(x) = %s \sin x$. Hình phẳng $(H)$ giới hạn bởi đồ thị hàm số $y = f(x)$, trục $Ox$, trục $Oy$ và đường thẳng $x = \pi$. Hình phẳng $(H_a)$ giới hạn bởi đồ thị hàm số $y = f(x)$, trục $Ox$, trục $Oy$ và đường thẳng $x = a$ với $a \in (0; \pi)$.''' 
                             % (latex(k) if k != 1 else ""))

            ########################################################################
            # Nhận biết (Nguyên hàm)
            nb_da_1_d = r'\True Họ nguyên hàm của hàm số là $\int f(x) \text{d}x = %s \cos x + C$' % (latex(-k))
            nb_da_1_s = r'Họ nguyên hàm của hàm số là $\int f(x) \text{d}x = %s \cos x + C$' % (latex(k))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'Ta có $\int f(x) \text{d}x = \int %s \sin x \text{d}x = %s \cos x + C$.' % (latex(k), latex(-k))

            ########################################################################
            # Thông hiểu (Diện tích S)
            th_da_1_d = r'\True Diện tích hình phẳng $(H)$ là $S = %s$' % (latex(S_tong))
            th_da_1_s = r'Diện tích hình phẳng $(H)$ là $S = %s$' % (latex(k))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''$S = \int_{0}^{\pi} |f(x)| \text{d}x = \int_{0}^{\pi} |%s \sin x| \text{d}x = \left( %s \cos x \right) \Big|_{0}^{\pi} = %s(-1 - 1) = %s$.''' 
                            % (latex(k), latex(-k), latex(-k), latex(S_tong)))

            ########################################################################
            # Vận dụng (Diện tích Sa)
            vd_da_1_d = r'\True Diện tích hình phẳng $(H_a)$ là $S_a = %s - %s \cos a$' % (latex(k), latex(k))
            vd_da_1_s = r'\True Diện tích hình phẳng $(H_a)$ là $S_a = %s + %s \cos a$' % (latex(k), latex(k)) # Sai dấu
            # Lưu ý: Sửa lại logic chọn đáp án đúng/sai cho khớp
            list_vd_da_1 = [vd_da_1_d, r'Diện tích hình phẳng $(H_a)$ là $S_a = %s \cos a$' % (latex(k))]

            loigiai_vd_1 = (r'''$S_a = \int_{0}^{a} |%s \sin x| \text{d}x = \left( %s \cos x \right) \Big|_{0}^{a} = %s - %s \cos a$.''' 
                            % (latex(k), latex(-k), latex(k), latex(k)))

            ########################################################################
            # Vận dụng cao (Tìm cos a)
            vdc_da_1_d = r'\True Nếu $S_a = \frac{%s}{%s} S$ thì $\cos a = %s$' % (latex(m_val), latex(n_val), latex(cos_a_val))
            vdc_da_1_s = r'Nếu $S_a = \frac{%s}{%s} S$ thì $\cos a = %s$' % (latex(m_val), latex(n_val), latex(cos_a_val+1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Nếu diện tích $(H_a)$ bằng $\frac{%s}{%s}$ diện tích $(H)$ thì: \\
                             $S_a = \frac{%s}{%s} S \Leftrightarrow %s - %s \cos a = \frac{%s}{%s} \cdot %s \Leftrightarrow %s - %s \cos a = %s \Leftrightarrow \cos a = %s$.''' 
                             % (latex(m_val), latex(n_val), latex(m_val), latex(n_val), 
                                latex(k), latex(k), latex(m_val), latex(n_val), latex(S_tong),
                                latex(k), latex(k), latex(ratio * S_tong), latex(cos_a_val)))

            # --- PHẦN LOGIC TRỘN VÀ XUẤT KẾT QUẢ ---

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)

                answers = [nb_sel, th_sel, vd_sel, vdc_sel]
                if 1 <= count_true_answers(answers) <= 3:
                    break

            # Đóng gói để in
            shuffled_answers = [nb_sel, th_sel, vd_sel, vdc_sel]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers[0])+'}\n'
                '{'+str(shuffled_answers[1])+'}\n'
                '{'+str(shuffled_answers[2])+'}\n'
                '{'+str(shuffled_answers[3])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

