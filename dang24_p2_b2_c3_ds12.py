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


def bt_dang24_p2_b2_c3_ds12(self):
                # --- KHAI BÁO BIẾN NGẪU NHIÊN ---
                t = symbols('t')
                val_k = randint(2, 5) * 2           # Hệ số k trong v(t) = kt
                val_t1 = randint(3, 5)              # Thời điểm t1
                val_t2 = val_t1 + randint(4, 6)     # Thời điểm t2 (bắt đầu phanh)
                val_a_phanh = -randint(2, 5)        # Gia tốc phanh a < 0

                # Tính toán các đại lượng vật lý
                val_v_t2 = val_k * val_t2           # Vận tốc tại t2
                val_s_t1 = integrate(val_k * t, (t, 0, val_t1)) # Quãng đường t1 giây đầu
                val_s_t1_t2 = integrate(val_k * t, (t, val_t1, val_t2)) # Quãng đường từ t1 đến t2

                # Thời điểm dừng hẳn: a_phanh*(t - t2) + v_t2 = 0
                val_t_dung = val_t2 - Rational(val_v_t2, val_a_phanh)
                v_phanh_expr = val_a_phanh * (t - val_t2) + val_v_t2

                val_s_phanh = integrate(v_phanh_expr, (t, val_t2, val_t_dung))
                val_s_truoc_phanh = integrate(val_k * t, (t, 0, val_t2))
                val_s_tong = val_s_truoc_phanh + val_s_phanh

                # Nội dung câu hỏi
                noidungcauhoi = (r"Một ô tô đang chuyển động với vận tốc $v(t) = %st$ (m/s). Từ thời điểm $t = %s$ (s), người lái xe phanh gấp với gia tốc $a = %s$ (m/s$^2$)." 
                                % (latex(val_k), latex(val_t2), latex(val_a_phanh)))

                ########################################################################
                # Nhận biết ############################################################
                nb_da_1_d = r'\True Quãng đường ô tô đi được trong $%s$ giây đầu tiên là $%s$ m' % (latex(val_t1), latex(val_s_t1))
                nb_da_1_s = r'Quãng đường ô tô đi được trong $%s$ giây đầu tiên là $%s$ m' % (latex(val_t1), latex(val_s_t1 + 5))
                list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
                nb_da_1 = random.choice(list_nb_da_1)
                list_nb_1 = [nb_da_1]

                loigiai_nb_1 = (r"Quãng đường ô tô đi được trong $%s$ giây đầu là $s = \int_{0}^{%s} %st \text{d}t = %s$ (m)." 
                                % (latex(val_t1), latex(val_t1), latex(val_k), latex(val_s_t1)))
                list_nb_2 = [loigiai_nb_1]

                # Xáo trộn Nhận biết
                combined_nb = list(zip(list_nb_1, list_nb_2))
                random.shuffle(combined_nb)
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ########################################################################
                # Thông hiểu ###########################################################
                th_da_1_d = r'\True Vận tốc của ô tô tại thời điểm bắt đầu phanh là $%s$ m/s' % (latex(val_v_t2))
                th_da_1_s = r'Vận tốc của ô tô tại thời điểm bắt đầu phanh là $%s$ m/s' % (latex(val_v_t2 + 10))
                list_th_da_1 = [th_da_1_d, th_da_1_s]
                th_da_1 = random.choice(list_th_da_1)
                list_th_1 = [th_da_1]

                loigiai_th_1 = (r"Tại thời điểm $t = %s$ (s), vận tốc ô tô là $v(%s) = %s \cdot %s = %s$ (m/s)." 
                                % (latex(val_t2), latex(val_t2), latex(val_k), latex(val_t2), latex(val_v_t2)))
                list_th_2 = [loigiai_th_1]

                # Xáo trộn Thông hiểu
                combined_th = list(zip(list_th_1, list_th_2))
                random.shuffle(combined_th)
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ########################################################################
                # Vận dụng #############################################################
                vd_da_1_d = r'\True Quãng đường ô tô đi được từ giây thứ $%s$ đến giây thứ $%s$ là $%s$ m' % (latex(val_t1), latex(val_t2), latex(val_s_t1_t2))
                vd_da_1_s = r'Quãng đường ô tô đi được từ giây thứ $%s$ đến giây thứ $%s$ là $%s$ m' % (latex(val_t1), latex(val_t2), latex(val_s_t1_t2 - 10))
                list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
                vd_da_1 = random.choice(list_vd_da_1)
                list_vd_1 = [vd_da_1]

                loigiai_vd_1 = (r"Quãng đường ô tô đi từ giây $%s$ đến $%s$ là $s = \int_{%s}^{%s} %st \text{d}t = %s$ (m)." 
                                % (latex(val_t1), latex(val_t2), latex(val_t1), latex(val_t2), latex(val_k), latex(val_s_t1_t2)))
                list_vd_2 = [loigiai_vd_1]

                # Xáo trộn Vận dụng
                combined_vd = list(zip(list_vd_1, list_vd_2))
                random.shuffle(combined_vd)
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ########################################################################
                # Vận dụng cao #########################################################
                vdc_da_1_d = r'\True Tổng quãng đường ô tô đi được đến khi dừng hẳn là $%s$ m' % (latex(val_s_tong))
                vdc_da_1_s = r'Tổng quãng đường ô tô đi được đến khi dừng hẳn là $%s$ m' % (latex(val_s_tong + 20))
                list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
                vdc_da_1 = random.choice(list_vdc_da_1)
                list_vdc_1 = [vdc_da_1]

                loigiai_vdc_1 = (r"Giai đoạn đầu: $s_1 = \int_{0}^{%s} %st \text{d}t = %s$. Giai đoạn phanh: $v_{phanh}(t) = %s(t-%s) + %s$. Ô tô dừng khi $v_{phanh}=0 \Rightarrow t = %s$. Khi đó $s_2 = \int_{%s}^{%s} v_{phanh}(t) \text{d}t = %s$. Tổng quãng đường $s = s_1 + s_2 = %s$ (m)." 
                                % (latex(val_t2), latex(val_k), latex(val_s_truoc_phanh), latex(val_a_phanh), latex(val_t2), latex(val_v_t2), latex(val_t_dung), latex(val_t2), latex(val_t_dung), latex(val_s_phanh), latex(val_s_tong)))
                list_vdc_2 = [loigiai_vdc_1]

                # Xáo trộn Vận dụng cao
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))
                random.shuffle(combined_vdc)
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

                # --- KIỂM TRA SỐ LƯỢNG ĐÁP ÁN ĐÚNG (1-3) ---
                def count_true_answers(answers):
                    return sum('\\True' in ans for ans in answers)

                while True:
                    nb_sel = random.choice(list_nb_da_1)
                    th_sel = random.choice(list_th_da_1)
                    vd_sel = random.choice(list_vd_da_1)
                    vdc_sel = random.choice(list_vdc_da_1)
                    if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                        shuffled_answers_nb = [nb_sel]
                        shuffled_answers_th = [th_sel]
                        shuffled_answers_vd = [vd_sel]
                        shuffled_answers_vdc = [vdc_sel]
                        break

                # --- XUẤT NỘI DUNG ---
                content = ('\\begin{minipage}{\\textwidth} \n'
                        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                        '\\choiceTFn \n'
                        '{' + str(shuffled_answers_nb[0]) + '}\n'
                        '{' + str(shuffled_answers_th[0]) + '}\n'
                        '{' + str(shuffled_answers_vd[0]) + '}\n'
                        '{' + str(shuffled_answers_vdc[0]) + '}\n'
                        '\\loigiai{ \n'
                        '\\begin{enumEX}[a)]{1} \n'
                        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                        '\\end{enumEX}} \n'
                        '\\end{ex}\n \\end{minipage} \n\n').replace('+ -', '-').replace('- -', '+')

                return content

