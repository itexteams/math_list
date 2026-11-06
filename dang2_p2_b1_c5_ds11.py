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


def bt_dang2_p2_b1_c5_ds11(self):
            # --- KHAI BÁO BIẾN ---
            a_sym = symbols('a')

            # Để tránh số ảo i khi a = -1, mẫu số PHẢI lẻ
            mau_le = [3, 5, 7, 9]

            # Tạo số mũ m = p/q (q lẻ)
            q = random.choice(mau_le)
            p = random.choice([x for x in range(1, 10) if x != q])
            m = Rational(p, q)

            # Tạo số mũ n = r/s (s lẻ)
            s = random.choice(mau_le)
            r = random.choice([x for x in range(1, 10) if x != s])
            n = Rational(r, s)

            A = a_sym**m
            B = a_sym**n

            # --- GIÁ TRỊ THỰC KHI a = 1 và a = -1 ---
            # a = 1
            val_A_1 = 1
            val_B_1 = 1

            # a = -1 (Vì mẫu số lẻ nên (-1)^(p/q) = (-1)^p)
            val_A_neg1 = 1 if p % 2 == 0 else -1
            val_B_neg1 = 1 if r % 2 == 0 else -1

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho $A=%s$ và $B=%s$.' % (latex(A), latex(B)))

            # ######################################################################## Nhận biết
            AB_expr = a_sym**(m + n)
            nb_da_1_d = '\\True $A \\cdot B=%s$' % (latex(AB_expr))
            nb_da_1_s = '$A \\cdot B=%s$' % (latex(a_sym**(m + n + Rational(1, 3))))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('Ta có: $A \\cdot B = %s \\cdot %s = %s^{%s+%s} = %s$.' 
                            % (latex(A), latex(B), latex(a_sym), latex(m), latex(n), latex(AB_expr)))

            # ######################################################################## Thông hiểu
            AcB_expr = a_sym**(m - n)
            th_da_1_d = '\\True $\\dfrac{A}{B}=%s$' % (latex(AcB_expr))
            th_da_1_s = '$\\dfrac{A}{B}=%s$' % (latex(a_sym**(m + n)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('Ta có: $\\dfrac{A}{B} = \\dfrac{%s}{%s} = %s^{%s-%s} = %s$.' 
                            % (latex(A), latex(B), latex(a_sym), latex(m), latex(n), latex(AcB_expr)))

            # ######################################################################## Vận dụng
            sum_val_1 = val_A_1 + val_B_1
            vd_da_1_d = '\\True $A+B=%s$ với $a=1$' % (latex(sum_val_1))
            vd_da_1_s = '$A+B=0$ với $a=1$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('Với $a=1$, ta có $A=1^{%s}=1$ và $B=1^{%s}=1$. Suy ra $A+B=2$.' 
                            % (latex(m), latex(n)))

            # ######################################################################## Vận dụng cao
            diff_val_neg1 = val_A_neg1 - val_B_neg1
            vdc_da_1_d = '\\True $A-B=%s$ với $a=-1$' % (latex(diff_val_neg1))
            vdc_da_1_s = '$A-B=%s$ với $a=-1$' % (latex(diff_val_neg1 + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('Với $a=-1$, ta có $A=(-1)^{%s}=%s$ và $B=(-1)^{%s}=%s$. '
                             'Do đó $A-B = %s - (%s) = %s$.' 
                            % (latex(m), latex(val_A_neg1), latex(n), latex(val_B_neg1), 
                               latex(val_A_neg1), latex(val_B_neg1), latex(diff_val_neg1)))

            # --- XỬ LÝ TRỘN ĐÁP ÁN ---
            shuffled_answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # Xuất nội dung - Đã thay toàn bộ \ thành \\ để không cần dùng tiền tố r
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

