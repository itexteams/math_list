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


def bt_dang21_p2_b2_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # --- BƯỚC 3: SUY NGHĨ TÌM CÁCH RANDOM BÀI TOÁN ---
            # Để bài toán số đẹp, ta chọn t1 (thời gian dừng) là một số hữu tỉ đẹp (0.5, 0.4, 0.25, ...)
            # Chọn v0 là vận tốc ban đầu (ví dụ: 10, 12, 14, 16, 18, 20)
            v0_val = random.choice([12, 16, 18, 20, 24])
            # Chọn t1_val là thời gian dừng hẳn (ví dụ 0.5 hoặc 0.4 hoặc 0.8)
            t1_val = random.choice([Rational(1, 2), Rational(2, 5), Rational(3, 4)]) 
            # Hệ số k trong v(t) = v0 - k*t. Khi dừng hẳn v(t1) = 0 => k = v0 / t1
            k_val = v0_val / t1_val
            vt = v0_val - k_val * t
            # Gia tốc a = v'(t)
            a_val = -k_val

            # Chọn một mốc thời gian t2 để tính quãng đường ở câu b (t2 < t1)
            t2_val = Rational(3, 10) if t1_val > Rational(3, 10) else t1_val / 2

            # Tính toán các giá trị quãng đường
            # s2: quãng đường sau t2 giây
            s2_val = integrate(vt, (t, 0, t2_val))
            # s_total: quãng đường đến khi dừng hẳn
            s_total = integrate(vt, (t, 0, t1_val))

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Một ô tô đang chạy với vận tốc $%s(\text{m/s})$ thì người lái hãm phanh. Sau khi hãm phanh ô tô chuyển động chậm dần đều với vận tốc $v(t)=%s(\text{m/s})$, trong đó $t$ là khoảng thời gian được tính bằng giây kể từ lúc ô tô bắt đầu hãm phanh.''' 
                             % (latex(v0_val), latex(vt)))

            ########################################################################
            # Nhận biết ############################################
            # Câu a: Thời gian dừng hẳn
            nb_da_1_d = r'\True Lúc hãm phanh đến khi dừng hẳn thì ô tô chuyển động trong $%s$ giây' % (latex(float(t1_val)))
            nb_da_1_s = r'Lúc hãm phanh đến khi dừng hẳn thì ô tô chuyển động trong $%s$ giây' % (latex(float(t1_val + 1)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Lúc ô tô dừng hẳn thì $v(t_1)=0 \Leftrightarrow %s = 0 \Leftrightarrow t_1 = %s$ giây.''' 
                            % (latex(vt), latex(float(t1_val))))

            ########################################################################
            # Thông hiểu ############################################
            # Câu b: Quãng đường sau t2 giây
            th_da_1_d = r'\True Quãng đường xe đi được sau $%s$ giây kể từ lúc hãm phanh là $%s$ m' % (latex(float(t2_val)), latex(float(s2_val)))
            th_da_1_s = r'Quãng đường xe đi được sau $%s$ giây kể từ lúc hãm phanh là $%s$ m' % (latex(float(t2_val)), latex(float(s2_val + 2)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''Quãng đường xe đi được sau $%s$ giây là: 
                            $s = \int\limits_{0}^{%s} \left(%s\right) \text{d}t = %s$ m.''' 
                            % (latex(float(t2_val)), latex(float(t2_val)), latex(vt), latex(float(s2_val))))

            ########################################################################
            # Vận dụng ############################################
            # Câu c: Tổng quãng đường dừng hẳn
            vd_da_1_d = r'\True Quãng đường kể từ lúc hãm phanh đến khi xe dừng hẳn là $%s$ m' % (latex(float(s_total)))
            vd_da_1_s = r'Quãng đường kể từ lúc hãm phanh đến khi xe dừng hẳn là $%s$ m' % (latex(float(s_total - 1)))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Với $t_1 = %s$ giây thì quãng đường kể từ lúc hãm phanh đến khi dừng hẳn là: 
                            $s_1 = \int\limits_{0}^{%s} \left(%s\right) \text{d}t = %s$ m.''' 
                            % (latex(float(t1_val)), latex(float(t1_val)), latex(vt), latex(float(s_total))))

            ########################################################################
            # Vận dụng cao ############################################
            # Câu d: Gia tốc
            vdc_da_1_d = r'\True Gia tốc tức thời của chuyển động này là $a = %s (\text{m/s}^2)$' % (latex(a_val))
            vdc_da_1_s = r'Gia tốc tức thời của chuyển động này là $a = %s (\text{m/s}^2)$' % (latex(abs(a_val)))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Gia tốc tức thời là đạo hàm của vận tốc: $a = v'(t) = \left(%s\right)' = %s (\text{m/s}^2)$.''' 
                             % (latex(vt), latex(a_val)))

            # --- LOGIC XỬ LÝ ĐÁP ÁN ĐÚNG/SAI (Giữ nguyên mẫu của bạn) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            # Xuất nội dung theo mẫu LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

