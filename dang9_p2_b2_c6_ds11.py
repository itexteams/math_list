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


def bt_dang9_p2_b2_c6_ds11(self):
            # Khai báo biến
            # Hàm hỗ trợ chuyển đổi số thập phân sang định dạng dấu phẩy Việt Nam
            def vn_format(value):
                return str(float(value)).replace('.', ',')

            # --- Bước 1: Khởi tạo giá trị ngẫu nhiên ---
            # P(A) và P(B) là các số thập phân đẹp (0,1; 0,2; ...; 0,5)
            pa_val = Rational(random.randint(2, 5), 10)
            pb_val = Rational(random.randint(1, 4), 10)

            # Chuyển sang chuỗi để hiển thị
            pa = vn_format(pa_val)
            pb = vn_format(pb_val)

            # Nội dung câu hỏi gốc
            noidungcauhoi = ('''Cho các biến cố $A, B,C,D$ và $P(A)=%s$ và $P(B)=%s$.''' % (pa, pb))

            ########################################################################
            # (a) Nhận biết: P(A \cup B) khi A, B xung khắc
            ########################################################################
            p_aub_dung = pa_val + pb_val
            p_aub_sai = pa_val + pb_val + Rational(1, 10) if pa_val + pb_val <= Rational(8, 10) else pa_val + pb_val - Rational(1, 10)

            nb_da_1_d = '\\True Nếu $A, B$ là hai biến cố xung khắc thì $P\\left( A \\cup B \\right) = %s$' % vn_format(p_aub_dung)
            nb_da_1_s = 'Nếu $A, B$ là hai biến cố xung khắc thì $P\\left( A \\cup B \\right) = %s$' % vn_format(p_aub_sai)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Nếu $A, B$ là hai biến cố xung khắc thì $P\\left( A \\cup B \\right) = P(A) + P(B) = %s + %s = %s$.''' 
                            % (pa, pb, vn_format(p_aub_dung)))

            ########################################################################
            # (b) Thông hiểu: Tính P(C) khi biết P(A \cup C)
            ########################################################################
            # Chọn P(A \cup C) sao cho lớn hơn P(A)
            p_auc_val = pa_val + Rational(random.randint(1, 3), 10)
            if p_auc_val > 1: p_auc_val = Rational(9, 10)
            pc_val = p_auc_val - pa_val

            th_da_1_d = '\\True Nếu $A, C$ xung khắc và $P\\left( A \\cup C \\right) = %s$ thì $P(C) = %s$' % (vn_format(p_auc_val), vn_format(pc_val))
            th_da_1_s = 'Nếu $A, C$ xung khắc và $P\\left( A \\cup C \\right) = %s$ thì $P(C) = %s$' % (vn_format(p_auc_val), vn_format(pc_val + Rational(1, 10)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Vì $A, C$ xung khắc nên $P\\left( A \\cup C \\right) = P(A) + P(C) \\\\ \\Rightarrow P(C) = P\\left( A \\cup C \\right) - P(A) = %s - %s = %s$.'''
                            % (vn_format(p_auc_val), pa, vn_format(pc_val)))

            ########################################################################
            # (c) Vận dụng: P(\bar{A} \cup B) khi \bar{A}, B xung khắc
            ########################################################################
            p_notA_val = 1 - pa_val
            p_notA_ub_dung = p_notA_val + pb_val
            p_notA_ub_sai = p_notA_val + pb_val - Rational(2, 10)

            vd_da_1_d = '\\True Nếu $\\bar{A}, B$ là hai biến cố xung khắc thì $P\\left( \\bar{A} \\cup B \\right) = %s$' % vn_format(p_notA_ub_dung)
            vd_da_1_s = 'Nếu $\\bar{A}, B$ là hai biến cố xung khắc thì $P\\left( \\bar{A} \\cup B \\right) = %s$' % vn_format(p_notA_ub_sai)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Ta có $P(\\bar{A}) = 1 - P(A) = 1 - %s = %s$. \\\\
                            Vì $\\bar{A}, B$ xung khắc nên $P\\left( \\bar{A} \\cup B \\right) = P(\\bar{A}) + P(B) = %s + %s = %s$.'''
                            % (pa, vn_format(p_notA_val), vn_format(p_notA_val), pb, vn_format(p_notA_ub_dung)))

            ########################################################################
            # (d) Vận dụng cao: Tính P(D) khi biết P(A \cup \bar{D})
            ########################################################################
            # Chọn P(A \cup \bar{D}) sao cho lớn hơn P(A)
            p_au_notD_val = pa_val + Rational(random.randint(1, 4), 10)
            if p_au_notD_val > 1: p_au_notD_val = Rational(8, 10)
            p_notD_val = p_au_notD_val - pa_val
            pd_dung = 1 - p_notD_val
            pd_sai = pd_dung + Rational(1, 10) if pd_dung <= Rational(8, 10) else pd_dung - Rational(1, 10)

            vdc_da_1_d = '\\True Nếu $A, \\bar{D}$ xung khắc và $P\\left( A \\cup \\bar{D} \\right) = %s$ thì $P(D) = %s$' % (vn_format(p_au_notD_val), vn_format(pd_dung))
            vdc_da_1_s = 'Nếu $A, \\bar{D}$ xung khắc và $P\\left( A \\cup \\bar{D} \\right) = %s$ thì $P(D) = %s$' % (vn_format(p_au_notD_val), vn_format(pd_sai))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Vì $A, \\bar{D}$ xung khắc nên $P\\left( A \\cup \\bar{D} \\right) = P(A) + P(\\bar{D}) \\\\ \\Rightarrow P(\\bar{D}) = P\\left( A \\cup \\bar{D} \\right) - P(A) = %s - %s = %s$. \\\\
                            Khi đó $P(D) = 1 - P(\\bar{D}) = 1 - %s = %s$.'''
                            % (vn_format(p_au_notD_val), pa, vn_format(p_notD_val), vn_format(p_notD_val), vn_format(pd_dung)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lời giải tương ứng
            loigiai_nb = loigiai_nb_1
            loigiai_th = loigiai_th_1
            loigiai_vd = loigiai_vd_1
            loigiai_vdc = loigiai_vdc_1

            # Xuất câu hỏi theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(loigiai_nb)+'\n'
                '\\item '+str(loigiai_th)+'\n'
                '\\item '+str(loigiai_vd)+'\n'
                '\\item '+str(loigiai_vdc)+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

