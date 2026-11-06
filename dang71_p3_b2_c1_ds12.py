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


def bt_dang71_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random các tham số đề bài
        p0 = random.choice([140, 150, 160, 180, 200])
        k1_val = random.choice([0.02, 0.03, 0.04])
        C0 = random.choice([15000, 20000, 25000, 30000])
        c1_val = random.choice([20, 25, 30, 35])
        X0 = 1000
        t0 = random.choice([8, 10, 12, 15])
        k2_val = random.choice([0.03, 0.04, 0.05])

        k1_str = str(k1_val).replace('.', ',')
        k2_str = str(k2_val).replace('.', ',')

        # Tính toán các hệ số thuế khi x > X0: Tax(x) = t0*X0 + t0*(x - X0) + k2_val*(x - X0)^2
        a_tax = k2_val
        b_tax = t0 - 2 * k2_val * X0  # Luôn âm
        c_tax = k2_val * (X0**2)

        a_tax_str = str(a_tax).replace('.', ',')
        b_tax_abs_str = str(abs(b_tax)).replace('.', ',')
        c_tax_str = str(int(c_tax))

        # C_tong(x) = C(x) + Tax(x)
        a_cost = a_tax
        b_cost = c1_val + b_tax  # Luôn âm
        c_cost = C0 + c_tax

        a_cost_str = str(a_cost).replace('.', ',')
        b_cost_abs_str = str(abs(b_cost)).replace('.', ',')
        c_cost_str = str(int(c_cost))

        # P(x) = R(x) - C_tong(x) = -A*x^2 + B*x - C_const
        A = k1_val + k2_val
        B = p0 - b_cost
        C_const = c_cost

        A_str = str(round(A, 4)).replace('.', ',')
        two_A_str = str(round(2 * A, 4)).replace('.', ',')
        B_str = str(int(B))
        C_const_str = str(int(C_const))

        x_star = B / (2 * A)
        P_max_nghin = (B**2) / (4 * A) - C_const
        P_max_trieu = P_max_nghin / 1000.0

        # Làm tròn đến hàng phần chục
        kq3 = Decimal(str(P_max_trieu)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq = str(kq3).replace('.', ',')
        kq4 = float(kq3)

        # Các đáp án trắc nghiệm
        du = ['$%s$' % (kq)]
        da = random.choice(du)

        s_opts = []
        deltas = [1.2, 2.5, 3.8, -1.5, -2.4, -3.6, 4.2, -4.5, 5.1, -5.3]
        random.shuffle(deltas)
        for d in deltas:
            val = round(kq4 + d, 1)
            if val > 0:
                val_str = str(Decimal(str(val)).quantize(Decimal('0.1'))).replace('.', ',')
                if val_str != kq and val_str not in s_opts:
                    s_opts.append(val_str)

        das1 = '$%s$' % s_opts[0]
        das2 = '$%s$' % s_opts[1]
        das3 = '$%s$' % s_opts[2]

        # Câu hỏi
        noidungcauhoi = ('''\\immini{Công ty năng lượng GreenPower dự định sản xuất một lô pin Lithium thế hệ mới. Bộ phận kinh doanh xác lập được hàm cầu của thị trường như sau: Nếu sản xuất $x$ (viên pin) thì đơn giá bán ra của mỗi viên pin sẽ là $p(x) = %s - %sx$ (nghìn đồng). Chi phí sản xuất cơ bản (chưa tính thuế) bao gồm chi phí cố định và biến đổi là $C(x) = %s + %sx$ (nghìn đồng). Tuy nhiên, do quy định khắt khe về xử lý chất thải độc hại nên nhà nước áp dụng chính sách thuế môi trường đặc biệt dựa trên sản lượng xả thải như sau:}
                         {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                         	\\tikzset {_ru7mb5xp8/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_71d5bds8n}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_bublo5ujd/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_x9i59fpzi}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_esuvujxg1/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_lti365ocx}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_ij9m527ur/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_c84bduk20}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_5m4y52j6l/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_olszgkaeg}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_jqyrdl5aq/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_sn7ym0ypb}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_noa4yow1t/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_elhct0hch}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_fmpruk0o5/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_yultwde1w}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_82a5lkwul/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_niiz9izbr}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_tsm9ugts0/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_6m7qisr1j}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_wrmprk3gy/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_cxz681nva}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_gi5l2vlkg/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_cg7slar9v}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_dzdohorjm/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_2uiis3xxz}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_crh6ph8p7/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_sqphevlct}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_bazfqrf52/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_m0vs45ehq}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_9g9mn097d/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_n4uq1kici}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_idc4jv8k6/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_kmb57h341}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_log1aq3hm/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_1gze1me5h}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_z13g3htd9/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_y4hmlupkd}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_38gyg57mf/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_eb83rsfge}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_5q9ou7os9/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_1a6ng5n5g}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_busm1hady/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_w6j4oj3h2}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_olz7bju8s/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_2qmoehqxy}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset {_0thz05okw/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
                         	\\pgfdeclarehorizontalshading{_ta6qrdh7q}{150bp}{rgb(0bp)=(0.09,0.94,0.37);
                         		rgb(37.5bp)=(0.09,0.94,0.37);
                         		rgb(55.96428462437221bp)=(0.03,0.55,0.2);
                         		rgb(62.5bp)=(0.09,0.94,0.37);
                         		rgb(100bp)=(0.09,0.94,0.37)}
                         	\\tikzset{every picture/.style={line width=0.75pt}}     
                         	\\path  [shading=_71d5bds8n,_ru7mb5xp8] (54.17,56.47) -- (54.17,118.88) .. controls (54.17,122.02) and (48.65,124.57) .. (41.84,124.57) .. controls (35.02,124.57) and (29.5,122.02) .. (29.5,118.88) -- (29.5,56.47) .. controls (29.5,53.33) and (35.02,50.78) .. (41.84,50.78) .. controls (48.65,50.78) and (54.17,53.33) .. (54.17,56.47) .. controls (54.17,59.61) and (48.65,62.15) .. (41.84,62.15) .. controls (35.02,62.15) and (29.5,59.61) .. (29.5,56.47) ; 
                         	\\draw   (54.17,56.47) -- (54.17,118.88) .. controls (54.17,122.02) and (48.65,124.57) .. (41.84,124.57) .. controls (35.02,124.57) and (29.5,122.02) .. (29.5,118.88) -- (29.5,56.47) .. controls (29.5,53.33) and (35.02,50.78) .. (41.84,50.78) .. controls (48.65,50.78) and (54.17,53.33) .. (54.17,56.47) .. controls (54.17,59.61) and (48.65,62.15) .. (41.84,62.15) .. controls (35.02,62.15) and (29.5,59.61) .. (29.5,56.47) ; 
                         	\\path  [shading=_x9i59fpzi,_bublo5ujd] (54.17,41.82) -- (54.17,56.47) .. controls (54.17,59.61) and (48.65,62.15) .. (41.84,62.15) .. controls (35.02,62.15) and (29.5,59.61) .. (29.5,56.47) -- (29.5,41.82) .. controls (29.5,38.68) and (35.02,36.13) .. (41.84,36.13) .. controls (48.65,36.13) and (54.17,38.68) .. (54.17,41.82) .. controls (54.17,44.96) and (48.65,47.5) .. (41.84,47.5) .. controls (35.02,47.5) and (29.5,44.96) .. (29.5,41.82) ; 
                         	\\draw   (54.17,41.82) -- (54.17,56.47) .. controls (54.17,59.61) and (48.65,62.15) .. (41.84,62.15) .. controls (35.02,62.15) and (29.5,59.61) .. (29.5,56.47) -- (29.5,41.82) .. controls (29.5,38.68) and (35.02,36.13) .. (41.84,36.13) .. controls (48.65,36.13) and (54.17,38.68) .. (54.17,41.82) .. controls (54.17,44.96) and (48.65,47.5) .. (41.84,47.5) .. controls (35.02,47.5) and (29.5,44.96) .. (29.5,41.82) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (35.1,41.82) .. controls (35.1,40.1) and (38.11,38.71) .. (41.84,38.71) .. controls (45.56,38.71) and (48.58,40.1) .. (48.58,41.82) .. controls (48.58,43.53) and (45.56,44.92) .. (41.84,44.92) .. controls (38.11,44.92) and (35.1,43.53) .. (35.1,41.82) -- cycle ;
                         	\\path  [shading=_lti365ocx,_esuvujxg1] (79.84,56.8) -- (79.84,119.22) .. controls (79.84,122.35) and (74.32,124.9) .. (67.5,124.9) .. controls (60.69,124.9) and (55.17,122.35) .. (55.17,119.22) -- (55.17,56.8) .. controls (55.17,53.66) and (60.69,51.12) .. (67.5,51.12) .. controls (74.32,51.12) and (79.84,53.66) .. (79.84,56.8) .. controls (79.84,59.94) and (74.32,62.49) .. (67.5,62.49) .. controls (60.69,62.49) and (55.17,59.94) .. (55.17,56.8) ; 
                         	\\draw   (79.84,56.8) -- (79.84,119.22) .. controls (79.84,122.35) and (74.32,124.9) .. (67.5,124.9) .. controls (60.69,124.9) and (55.17,122.35) .. (55.17,119.22) -- (55.17,56.8) .. controls (55.17,53.66) and (60.69,51.12) .. (67.5,51.12) .. controls (74.32,51.12) and (79.84,53.66) .. (79.84,56.8) .. controls (79.84,59.94) and (74.32,62.49) .. (67.5,62.49) .. controls (60.69,62.49) and (55.17,59.94) .. (55.17,56.8) ; 
                         	\\path  [shading=_c84bduk20,_ij9m527ur] (79.84,42.15) -- (79.84,56.8) .. controls (79.84,59.94) and (74.32,62.49) .. (67.5,62.49) .. controls (60.69,62.49) and (55.17,59.94) .. (55.17,56.8) -- (55.17,42.15) .. controls (55.17,39.01) and (60.69,36.47) .. (67.5,36.47) .. controls (74.32,36.47) and (79.84,39.01) .. (79.84,42.15) .. controls (79.84,45.29) and (74.32,47.84) .. (67.5,47.84) .. controls (60.69,47.84) and (55.17,45.29) .. (55.17,42.15) ; 
                         	\\draw   (79.84,42.15) -- (79.84,56.8) .. controls (79.84,59.94) and (74.32,62.49) .. (67.5,62.49) .. controls (60.69,62.49) and (55.17,59.94) .. (55.17,56.8) -- (55.17,42.15) .. controls (55.17,39.01) and (60.69,36.47) .. (67.5,36.47) .. controls (74.32,36.47) and (79.84,39.01) .. (79.84,42.15) .. controls (79.84,45.29) and (74.32,47.84) .. (67.5,47.84) .. controls (60.69,47.84) and (55.17,45.29) .. (55.17,42.15) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (60.76,42.15) .. controls (60.76,40.44) and (63.78,39.05) .. (67.5,39.05) .. controls (71.23,39.05) and (74.24,40.44) .. (74.24,42.15) .. controls (74.24,43.87) and (71.23,45.26) .. (67.5,45.26) .. controls (63.78,45.26) and (60.76,43.87) .. (60.76,42.15) -- cycle ;
                         	\\path  [shading=_olszgkaeg,_5m4y52j6l] (105.17,58.14) -- (105.17,120.55) .. controls (105.17,123.69) and (99.65,126.23) .. (92.84,126.23) .. controls (86.02,126.23) and (80.5,123.69) .. (80.5,120.55) -- (80.5,58.14) .. controls (80.5,55) and (86.02,52.45) .. (92.84,52.45) .. controls (99.65,52.45) and (105.17,55) .. (105.17,58.14) .. controls (105.17,61.28) and (99.65,63.82) .. (92.84,63.82) .. controls (86.02,63.82) and (80.5,61.28) .. (80.5,58.14) ;  
                         	\\draw   (105.17,58.14) -- (105.17,120.55) .. controls (105.17,123.69) and (99.65,126.23) .. (92.84,126.23) .. controls (86.02,126.23) and (80.5,123.69) .. (80.5,120.55) -- (80.5,58.14) .. controls (80.5,55) and (86.02,52.45) .. (92.84,52.45) .. controls (99.65,52.45) and (105.17,55) .. (105.17,58.14) .. controls (105.17,61.28) and (99.65,63.82) .. (92.84,63.82) .. controls (86.02,63.82) and (80.5,61.28) .. (80.5,58.14) ; 
                         	\\path  [shading=_sn7ym0ypb,_jqyrdl5aq] (105.17,43.48) -- (105.17,58.14) .. controls (105.17,61.28) and (99.65,63.82) .. (92.84,63.82) .. controls (86.02,63.82) and (80.5,61.28) .. (80.5,58.14) -- (80.5,43.48) .. controls (80.5,40.35) and (86.02,37.8) .. (92.84,37.8) .. controls (99.65,37.8) and (105.17,40.35) .. (105.17,43.48) .. controls (105.17,46.62) and (99.65,49.17) .. (92.84,49.17) .. controls (86.02,49.17) and (80.5,46.62) .. (80.5,43.48) ; 
                         	\\draw   (105.17,43.48) -- (105.17,58.14) .. controls (105.17,61.28) and (99.65,63.82) .. (92.84,63.82) .. controls (86.02,63.82) and (80.5,61.28) .. (80.5,58.14) -- (80.5,43.48) .. controls (80.5,40.35) and (86.02,37.8) .. (92.84,37.8) .. controls (99.65,37.8) and (105.17,40.35) .. (105.17,43.48) .. controls (105.17,46.62) and (99.65,49.17) .. (92.84,49.17) .. controls (86.02,49.17) and (80.5,46.62) .. (80.5,43.48) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (86.1,43.48) .. controls (86.1,41.77) and (89.11,40.38) .. (92.84,40.38) .. controls (96.56,40.38) and (99.58,41.77) .. (99.58,43.48) .. controls (99.58,45.2) and (96.56,46.59) .. (92.84,46.59) .. controls (89.11,46.59) and (86.1,45.2) .. (86.1,43.48) -- cycle ;
                         	\\path  [shading=_elhct0hch,_noa4yow1t] (130.51,59.47) -- (130.51,121.88) .. controls (130.51,125.02) and (124.98,127.57) .. (118.17,127.57) .. controls (111.36,127.57) and (105.83,125.02) .. (105.83,121.88) -- (105.83,59.47) .. controls (105.83,56.33) and (111.36,53.78) .. (118.17,53.78) .. controls (124.98,53.78) and (130.51,56.33) .. (130.51,59.47) .. controls (130.51,62.61) and (124.98,65.15) .. (118.17,65.15) .. controls (111.36,65.15) and (105.83,62.61) .. (105.83,59.47) ; 
                         	\\draw   (130.51,59.47) -- (130.51,121.88) .. controls (130.51,125.02) and (124.98,127.57) .. (118.17,127.57) .. controls (111.36,127.57) and (105.83,125.02) .. (105.83,121.88) -- (105.83,59.47) .. controls (105.83,56.33) and (111.36,53.78) .. (118.17,53.78) .. controls (124.98,53.78) and (130.51,56.33) .. (130.51,59.47) .. controls (130.51,62.61) and (124.98,65.15) .. (118.17,65.15) .. controls (111.36,65.15) and (105.83,62.61) .. (105.83,59.47) ; 
                         	\\path  [shading=_yultwde1w,_fmpruk0o5] (130.51,44.82) -- (130.51,59.47) .. controls (130.51,62.61) and (124.98,65.15) .. (118.17,65.15) .. controls (111.36,65.15) and (105.83,62.61) .. (105.83,59.47) -- (105.83,44.82) .. controls (105.83,41.68) and (111.36,39.13) .. (118.17,39.13) .. controls (124.98,39.13) and (130.51,41.68) .. (130.51,44.82) .. controls (130.51,47.96) and (124.98,50.5) .. (118.17,50.5) .. controls (111.36,50.5) and (105.83,47.96) .. (105.83,44.82) ; 
                         	\\draw   (130.51,44.82) -- (130.51,59.47) .. controls (130.51,62.61) and (124.98,65.15) .. (118.17,65.15) .. controls (111.36,65.15) and (105.83,62.61) .. (105.83,59.47) -- (105.83,44.82) .. controls (105.83,41.68) and (111.36,39.13) .. (118.17,39.13) .. controls (124.98,39.13) and (130.51,41.68) .. (130.51,44.82) .. controls (130.51,47.96) and (124.98,50.5) .. (118.17,50.5) .. controls (111.36,50.5) and (105.83,47.96) .. (105.83,44.82) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (111.43,44.82) .. controls (111.43,43.1) and (114.45,41.71) .. (118.17,41.71) .. controls (121.89,41.71) and (124.91,43.1) .. (124.91,44.82) .. controls (124.91,46.53) and (121.89,47.92) .. (118.17,47.92) .. controls (114.45,47.92) and (111.43,46.53) .. (111.43,44.82) -- cycle ;
                         	\\path  [shading=_niiz9izbr,_82a5lkwul] (63.17,69.47) -- (63.17,131.88) .. controls (63.17,135.02) and (57.65,137.57) .. (50.84,137.57) .. controls (44.02,137.57) and (38.5,135.02) .. (38.5,131.88) -- (38.5,69.47) .. controls (38.5,66.33) and (44.02,63.78) .. (50.84,63.78) .. controls (57.65,63.78) and (63.17,66.33) .. (63.17,69.47) .. controls (63.17,72.61) and (57.65,75.15) .. (50.84,75.15) .. controls (44.02,75.15) and (38.5,72.61) .. (38.5,69.47) ; 
                         	\\draw   (63.17,69.47) -- (63.17,131.88) .. controls (63.17,135.02) and (57.65,137.57) .. (50.84,137.57) .. controls (44.02,137.57) and (38.5,135.02) .. (38.5,131.88) -- (38.5,69.47) .. controls (38.5,66.33) and (44.02,63.78) .. (50.84,63.78) .. controls (57.65,63.78) and (63.17,66.33) .. (63.17,69.47) .. controls (63.17,72.61) and (57.65,75.15) .. (50.84,75.15) .. controls (44.02,75.15) and (38.5,72.61) .. (38.5,69.47) ;  
                         	\\path  [shading=_6m7qisr1j,_tsm9ugts0] (63.17,54.82) -- (63.17,69.47) .. controls (63.17,72.61) and (57.65,75.15) .. (50.84,75.15) .. controls (44.02,75.15) and (38.5,72.61) .. (38.5,69.47) -- (38.5,54.82) .. controls (38.5,51.68) and (44.02,49.13) .. (50.84,49.13) .. controls (57.65,49.13) and (63.17,51.68) .. (63.17,54.82) .. controls (63.17,57.96) and (57.65,60.5) .. (50.84,60.5) .. controls (44.02,60.5) and (38.5,57.96) .. (38.5,54.82) ; 
                         	\\draw   (63.17,54.82) -- (63.17,69.47) .. controls (63.17,72.61) and (57.65,75.15) .. (50.84,75.15) .. controls (44.02,75.15) and (38.5,72.61) .. (38.5,69.47) -- (38.5,54.82) .. controls (38.5,51.68) and (44.02,49.13) .. (50.84,49.13) .. controls (57.65,49.13) and (63.17,51.68) .. (63.17,54.82) .. controls (63.17,57.96) and (57.65,60.5) .. (50.84,60.5) .. controls (44.02,60.5) and (38.5,57.96) .. (38.5,54.82) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (44.1,54.82) .. controls (44.1,53.1) and (47.11,51.71) .. (50.84,51.71) .. controls (54.56,51.71) and (57.58,53.1) .. (57.58,54.82) .. controls (57.58,56.53) and (54.56,57.92) .. (50.84,57.92) .. controls (47.11,57.92) and (44.1,56.53) .. (44.1,54.82) -- cycle ;
                         	\\path  [shading=_cxz681nva,_wrmprk3gy] (88.84,69.8) -- (88.84,132.22) .. controls (88.84,135.35) and (83.32,137.9) .. (76.5,137.9) .. controls (69.69,137.9) and (64.17,135.35) .. (64.17,132.22) -- (64.17,69.8) .. controls (64.17,66.66) and (69.69,64.12) .. (76.5,64.12) .. controls (83.32,64.12) and (88.84,66.66) .. (88.84,69.8) .. controls (88.84,72.94) and (83.32,75.49) .. (76.5,75.49) .. controls (69.69,75.49) and (64.17,72.94) .. (64.17,69.8) ; 
                         	\\draw   (88.84,69.8) -- (88.84,132.22) .. controls (88.84,135.35) and (83.32,137.9) .. (76.5,137.9) .. controls (69.69,137.9) and (64.17,135.35) .. (64.17,132.22) -- (64.17,69.8) .. controls (64.17,66.66) and (69.69,64.12) .. (76.5,64.12) .. controls (83.32,64.12) and (88.84,66.66) .. (88.84,69.8) .. controls (88.84,72.94) and (83.32,75.49) .. (76.5,75.49) .. controls (69.69,75.49) and (64.17,72.94) .. (64.17,69.8) ; 
                         	\\path  [shading=_cg7slar9v,_gi5l2vlkg] (88.84,55.15) -- (88.84,69.8) .. controls (88.84,72.94) and (83.32,75.49) .. (76.5,75.49) .. controls (69.69,75.49) and (64.17,72.94) .. (64.17,69.8) -- (64.17,55.15) .. controls (64.17,52.01) and (69.69,49.47) .. (76.5,49.47) .. controls (83.32,49.47) and (88.84,52.01) .. (88.84,55.15) .. controls (88.84,58.29) and (83.32,60.84) .. (76.5,60.84) .. controls (69.69,60.84) and (64.17,58.29) .. (64.17,55.15) ; 
                         	\\draw   (88.84,55.15) -- (88.84,69.8) .. controls (88.84,72.94) and (83.32,75.49) .. (76.5,75.49) .. controls (69.69,75.49) and (64.17,72.94) .. (64.17,69.8) -- (64.17,55.15) .. controls (64.17,52.01) and (69.69,49.47) .. (76.5,49.47) .. controls (83.32,49.47) and (88.84,52.01) .. (88.84,55.15) .. controls (88.84,58.29) and (83.32,60.84) .. (76.5,60.84) .. controls (69.69,60.84) and (64.17,58.29) .. (64.17,55.15) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (69.76,55.15) .. controls (69.76,53.44) and (72.78,52.05) .. (76.5,52.05) .. controls (80.23,52.05) and (83.24,53.44) .. (83.24,55.15) .. controls (83.24,56.87) and (80.23,58.26) .. (76.5,58.26) .. controls (72.78,58.26) and (69.76,56.87) .. (69.76,55.15) -- cycle ;
                         	\\path  [shading=_2uiis3xxz,_dzdohorjm] (114.17,71.14) -- (114.17,133.55) .. controls (114.17,136.69) and (108.65,139.23) .. (101.84,139.23) .. controls (95.02,139.23) and (89.5,136.69) .. (89.5,133.55) -- (89.5,71.14) .. controls (89.5,68) and (95.02,65.45) .. (101.84,65.45) .. controls (108.65,65.45) and (114.17,68) .. (114.17,71.14) .. controls (114.17,74.28) and (108.65,76.82) .. (101.84,76.82) .. controls (95.02,76.82) and (89.5,74.28) .. (89.5,71.14) ; 
                         	\\draw   (114.17,71.14) -- (114.17,133.55) .. controls (114.17,136.69) and (108.65,139.23) .. (101.84,139.23) .. controls (95.02,139.23) and (89.5,136.69) .. (89.5,133.55) -- (89.5,71.14) .. controls (89.5,68) and (95.02,65.45) .. (101.84,65.45) .. controls (108.65,65.45) and (114.17,68) .. (114.17,71.14) .. controls (114.17,74.28) and (108.65,76.82) .. (101.84,76.82) .. controls (95.02,76.82) and (89.5,74.28) .. (89.5,71.14) ; 
                         	\\path  [shading=_sqphevlct,_crh6ph8p7] (114.17,56.48) -- (114.17,71.14) .. controls (114.17,74.28) and (108.65,76.82) .. (101.84,76.82) .. controls (95.02,76.82) and (89.5,74.28) .. (89.5,71.14) -- (89.5,56.48) .. controls (89.5,53.35) and (95.02,50.8) .. (101.84,50.8) .. controls (108.65,50.8) and (114.17,53.35) .. (114.17,56.48) .. controls (114.17,59.62) and (108.65,62.17) .. (101.84,62.17) .. controls (95.02,62.17) and (89.5,59.62) .. (89.5,56.48) ; 
                         	\\draw   (114.17,56.48) -- (114.17,71.14) .. controls (114.17,74.28) and (108.65,76.82) .. (101.84,76.82) .. controls (95.02,76.82) and (89.5,74.28) .. (89.5,71.14) -- (89.5,56.48) .. controls (89.5,53.35) and (95.02,50.8) .. (101.84,50.8) .. controls (108.65,50.8) and (114.17,53.35) .. (114.17,56.48) .. controls (114.17,59.62) and (108.65,62.17) .. (101.84,62.17) .. controls (95.02,62.17) and (89.5,59.62) .. (89.5,56.48) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (95.1,56.48) .. controls (95.1,54.77) and (98.11,53.38) .. (101.84,53.38) .. controls (105.56,53.38) and (108.58,54.77) .. (108.58,56.48) .. controls (108.58,58.2) and (105.56,59.59) .. (101.84,59.59) .. controls (98.11,59.59) and (95.1,58.2) .. (95.1,56.48) -- cycle ;
                         	\\path  [shading=_m0vs45ehq,_bazfqrf52] (139.51,72.47) -- (139.51,134.88) .. controls (139.51,138.02) and (133.98,140.57) .. (127.17,140.57) .. controls (120.36,140.57) and (114.83,138.02) .. (114.83,134.88) -- (114.83,72.47) .. controls (114.83,69.33) and (120.36,66.78) .. (127.17,66.78) .. controls (133.98,66.78) and (139.51,69.33) .. (139.51,72.47) .. controls (139.51,75.61) and (133.98,78.15) .. (127.17,78.15) .. controls (120.36,78.15) and (114.83,75.61) .. (114.83,72.47) ; 
                         	\\draw   (139.51,72.47) -- (139.51,134.88) .. controls (139.51,138.02) and (133.98,140.57) .. (127.17,140.57) .. controls (120.36,140.57) and (114.83,138.02) .. (114.83,134.88) -- (114.83,72.47) .. controls (114.83,69.33) and (120.36,66.78) .. (127.17,66.78) .. controls (133.98,66.78) and (139.51,69.33) .. (139.51,72.47) .. controls (139.51,75.61) and (133.98,78.15) .. (127.17,78.15) .. controls (120.36,78.15) and (114.83,75.61) .. (114.83,72.47) ; 
                         	\\path  [shading=_n4uq1kici,_9g9mn097d] (139.51,57.82) -- (139.51,72.47) .. controls (139.51,75.61) and (133.98,78.15) .. (127.17,78.15) .. controls (120.36,78.15) and (114.83,75.61) .. (114.83,72.47) -- (114.83,57.82) .. controls (114.83,54.68) and (120.36,52.13) .. (127.17,52.13) .. controls (133.98,52.13) and (139.51,54.68) .. (139.51,57.82) .. controls (139.51,60.96) and (133.98,63.5) .. (127.17,63.5) .. controls (120.36,63.5) and (114.83,60.96) .. (114.83,57.82) ; 
                         	\\draw   (139.51,57.82) -- (139.51,72.47) .. controls (139.51,75.61) and (133.98,78.15) .. (127.17,78.15) .. controls (120.36,78.15) and (114.83,75.61) .. (114.83,72.47) -- (114.83,57.82) .. controls (114.83,54.68) and (120.36,52.13) .. (127.17,52.13) .. controls (133.98,52.13) and (139.51,54.68) .. (139.51,57.82) .. controls (139.51,60.96) and (133.98,63.5) .. (127.17,63.5) .. controls (120.36,63.5) and (114.83,60.96) .. (114.83,57.82) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (120.43,57.82) .. controls (120.43,56.1) and (123.45,54.71) .. (127.17,54.71) .. controls (130.89,54.71) and (133.91,56.1) .. (133.91,57.82) .. controls (133.91,59.53) and (130.89,60.92) .. (127.17,60.92) .. controls (123.45,60.92) and (120.43,59.53) .. (120.43,57.82) -- cycle ;
                         	\\path  [shading=_kmb57h341,_idc4jv8k6] (75.17,82.14) -- (75.17,144.55) .. controls (75.17,147.69) and (69.65,150.23) .. (62.84,150.23) .. controls (56.02,150.23) and (50.5,147.69) .. (50.5,144.55) -- (50.5,82.14) .. controls (50.5,79) and (56.02,76.45) .. (62.84,76.45) .. controls (69.65,76.45) and (75.17,79) .. (75.17,82.14) .. controls (75.17,85.28) and (69.65,87.82) .. (62.84,87.82) .. controls (56.02,87.82) and (50.5,85.28) .. (50.5,82.14) ; 
                         	\\draw   (75.17,82.14) -- (75.17,144.55) .. controls (75.17,147.69) and (69.65,150.23) .. (62.84,150.23) .. controls (56.02,150.23) and (50.5,147.69) .. (50.5,144.55) -- (50.5,82.14) .. controls (50.5,79) and (56.02,76.45) .. (62.84,76.45) .. controls (69.65,76.45) and (75.17,79) .. (75.17,82.14) .. controls (75.17,85.28) and (69.65,87.82) .. (62.84,87.82) .. controls (56.02,87.82) and (50.5,85.28) .. (50.5,82.14) ; 
                         	\\path  [shading=_1gze1me5h,_log1aq3hm] (75.17,67.48) -- (75.17,82.14) .. controls (75.17,85.28) and (69.65,87.82) .. (62.84,87.82) .. controls (56.02,87.82) and (50.5,85.28) .. (50.5,82.14) -- (50.5,67.48) .. controls (50.5,64.35) and (56.02,61.8) .. (62.84,61.8) .. controls (69.65,61.8) and (75.17,64.35) .. (75.17,67.48) .. controls (75.17,70.62) and (69.65,73.17) .. (62.84,73.17) .. controls (56.02,73.17) and (50.5,70.62) .. (50.5,67.48) ; 
                         	\\draw   (75.17,67.48) -- (75.17,82.14) .. controls (75.17,85.28) and (69.65,87.82) .. (62.84,87.82) .. controls (56.02,87.82) and (50.5,85.28) .. (50.5,82.14) -- (50.5,67.48) .. controls (50.5,64.35) and (56.02,61.8) .. (62.84,61.8) .. controls (69.65,61.8) and (75.17,64.35) .. (75.17,67.48) .. controls (75.17,70.62) and (69.65,73.17) .. (62.84,73.17) .. controls (56.02,73.17) and (50.5,70.62) .. (50.5,67.48) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (56.1,67.48) .. controls (56.1,65.77) and (59.11,64.38) .. (62.84,64.38) .. controls (66.56,64.38) and (69.58,65.77) .. (69.58,67.48) .. controls (69.58,69.2) and (66.56,70.59) .. (62.84,70.59) .. controls (59.11,70.59) and (56.1,69.2) .. (56.1,67.48) -- cycle ;
                         	\\path  [shading=_y4hmlupkd,_z13g3htd9] (100.84,82.47) -- (100.84,144.88) .. controls (100.84,148.02) and (95.32,150.57) .. (88.5,150.57) .. controls (81.69,150.57) and (76.17,148.02) .. (76.17,144.88) -- (76.17,82.47) .. controls (76.17,79.33) and (81.69,76.78) .. (88.5,76.78) .. controls (95.32,76.78) and (100.84,79.33) .. (100.84,82.47) .. controls (100.84,85.61) and (95.32,88.15) .. (88.5,88.15) .. controls (81.69,88.15) and (76.17,85.61) .. (76.17,82.47) ;  
                         	\\draw   (100.84,82.47) -- (100.84,144.88) .. controls (100.84,148.02) and (95.32,150.57) .. (88.5,150.57) .. controls (81.69,150.57) and (76.17,148.02) .. (76.17,144.88) -- (76.17,82.47) .. controls (76.17,79.33) and (81.69,76.78) .. (88.5,76.78) .. controls (95.32,76.78) and (100.84,79.33) .. (100.84,82.47) .. controls (100.84,85.61) and (95.32,88.15) .. (88.5,88.15) .. controls (81.69,88.15) and (76.17,85.61) .. (76.17,82.47) ; 
                         	\\path  [shading=_eb83rsfge,_38gyg57mf] (100.84,67.82) -- (100.84,82.47) .. controls (100.84,85.61) and (95.32,88.15) .. (88.5,88.15) .. controls (81.69,88.15) and (76.17,85.61) .. (76.17,82.47) -- (76.17,67.82) .. controls (76.17,64.68) and (81.69,62.13) .. (88.5,62.13) .. controls (95.32,62.13) and (100.84,64.68) .. (100.84,67.82) .. controls (100.84,70.96) and (95.32,73.5) .. (88.5,73.5) .. controls (81.69,73.5) and (76.17,70.96) .. (76.17,67.82) ; 
                         	\\draw   (100.84,67.82) -- (100.84,82.47) .. controls (100.84,85.61) and (95.32,88.15) .. (88.5,88.15) .. controls (81.69,88.15) and (76.17,85.61) .. (76.17,82.47) -- (76.17,67.82) .. controls (76.17,64.68) and (81.69,62.13) .. (88.5,62.13) .. controls (95.32,62.13) and (100.84,64.68) .. (100.84,67.82) .. controls (100.84,70.96) and (95.32,73.5) .. (88.5,73.5) .. controls (81.69,73.5) and (76.17,70.96) .. (76.17,67.82) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (81.76,67.82) .. controls (81.76,66.1) and (84.78,64.71) .. (88.5,64.71) .. controls (92.23,64.71) and (95.24,66.1) .. (95.24,67.82) .. controls (95.24,69.53) and (92.23,70.92) .. (88.5,70.92) .. controls (84.78,70.92) and (81.76,69.53) .. (81.76,67.82) -- cycle ;
                         	\\path  [shading=_1a6ng5n5g,_5q9ou7os9] (126.17,83.8) -- (126.17,146.22) .. controls (126.17,149.35) and (120.65,151.9) .. (113.84,151.9) .. controls (107.02,151.9) and (101.5,149.35) .. (101.5,146.22) -- (101.5,83.8) .. controls (101.5,80.66) and (107.02,78.12) .. (113.84,78.12) .. controls (120.65,78.12) and (126.17,80.66) .. (126.17,83.8) .. controls (126.17,86.94) and (120.65,89.49) .. (113.84,89.49) .. controls (107.02,89.49) and (101.5,86.94) .. (101.5,83.8) ; 
                         	\\draw   (126.17,83.8) -- (126.17,146.22) .. controls (126.17,149.35) and (120.65,151.9) .. (113.84,151.9) .. controls (107.02,151.9) and (101.5,149.35) .. (101.5,146.22) -- (101.5,83.8) .. controls (101.5,80.66) and (107.02,78.12) .. (113.84,78.12) .. controls (120.65,78.12) and (126.17,80.66) .. (126.17,83.8) .. controls (126.17,86.94) and (120.65,89.49) .. (113.84,89.49) .. controls (107.02,89.49) and (101.5,86.94) .. (101.5,83.8) ; 
                         	\\path  [shading=_w6j4oj3h2,_busm1hady] (126.17,69.15) -- (126.17,83.8) .. controls (126.17,86.94) and (120.65,89.49) .. (113.84,89.49) .. controls (107.02,89.49) and (101.5,86.94) .. (101.5,83.8) -- (101.5,69.15) .. controls (101.5,66.01) and (107.02,63.47) .. (113.84,63.47) .. controls (120.65,63.47) and (126.17,66.01) .. (126.17,69.15) .. controls (126.17,72.29) and (120.65,74.84) .. (113.84,74.84) .. controls (107.02,74.84) and (101.5,72.29) .. (101.5,69.15) ; 
                         	\\draw   (126.17,69.15) -- (126.17,83.8) .. controls (126.17,86.94) and (120.65,89.49) .. (113.84,89.49) .. controls (107.02,89.49) and (101.5,86.94) .. (101.5,83.8) -- (101.5,69.15) .. controls (101.5,66.01) and (107.02,63.47) .. (113.84,63.47) .. controls (120.65,63.47) and (126.17,66.01) .. (126.17,69.15) .. controls (126.17,72.29) and (120.65,74.84) .. (113.84,74.84) .. controls (107.02,74.84) and (101.5,72.29) .. (101.5,69.15) ; 
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (107.1,69.15) .. controls (107.1,67.44) and (110.11,66.05) .. (113.84,66.05) .. controls (117.56,66.05) and (120.58,67.44) .. (120.58,69.15) .. controls (120.58,70.87) and (117.56,72.26) .. (113.84,72.26) .. controls (110.11,72.26) and (107.1,70.87) .. (107.1,69.15) -- cycle ;
                         	\\path  [shading=_2qmoehqxy,_olz7bju8s] (181.51,107.14) -- (181.51,169.55) .. controls (181.51,172.69) and (175.98,175.23) .. (169.17,175.23) .. controls (162.36,175.23) and (156.83,172.69) .. (156.83,169.55) -- (156.83,107.14) .. controls (156.83,104) and (162.36,101.45) .. (169.17,101.45) .. controls (175.98,101.45) and (181.51,104) .. (181.51,107.14) .. controls (181.51,110.28) and (175.98,112.82) .. (169.17,112.82) .. controls (162.36,112.82) and (156.83,110.28) .. (156.83,107.14) ; 
                         	\\draw   (181.51,107.14) -- (181.51,169.55) .. controls (181.51,172.69) and (175.98,175.23) .. (169.17,175.23) .. controls (162.36,175.23) and (156.83,172.69) .. (156.83,169.55) -- (156.83,107.14) .. controls (156.83,104) and (162.36,101.45) .. (169.17,101.45) .. controls (175.98,101.45) and (181.51,104) .. (181.51,107.14) .. controls (181.51,110.28) and (175.98,112.82) .. (169.17,112.82) .. controls (162.36,112.82) and (156.83,110.28) .. (156.83,107.14) ; 
                         	\\path  [shading=_ta6qrdh7q,_0thz05okw] (181.51,92.48) -- (181.51,107.14) .. controls (181.51,110.28) and (175.98,112.82) .. (169.17,112.82) .. controls (162.36,112.82) and (156.83,110.28) .. (156.83,107.14) -- (156.83,92.48) .. controls (156.83,89.35) and (162.36,86.8) .. (169.17,86.8) .. controls (175.98,86.8) and (181.51,89.35) .. (181.51,92.48) .. controls (181.51,95.62) and (175.98,98.17) .. (169.17,98.17) .. controls (162.36,98.17) and (156.83,95.62) .. (156.83,92.48) ; 
                         	\\draw   (181.51,92.48) -- (181.51,107.14) .. controls (181.51,110.28) and (175.98,112.82) .. (169.17,112.82) .. controls (162.36,112.82) and (156.83,110.28) .. (156.83,107.14) -- (156.83,92.48) .. controls (156.83,89.35) and (162.36,86.8) .. (169.17,86.8) .. controls (175.98,86.8) and (181.51,89.35) .. (181.51,92.48) .. controls (181.51,95.62) and (175.98,98.17) .. (169.17,98.17) .. controls (162.36,98.17) and (156.83,95.62) .. (156.83,92.48) ;
                         	\\draw  [fill={rgb, 255:red, 228; green, 226; blue, 226 }  ,fill opacity=1 ] (162.43,92.48) .. controls (162.43,90.77) and (165.45,89.38) .. (169.17,89.38) .. controls (172.89,89.38) and (175.91,90.77) .. (175.91,92.48) .. controls (175.91,94.2) and (172.89,95.59) .. (169.17,95.59) .. controls (165.45,95.59) and (162.43,94.2) .. (162.43,92.48) -- cycle ;
                         \\end{tikzpicture}}
    - Mức 1 là mức an toàn: Với $%s$ viên pin đầu tiên thì mức thuế môi trường là cố định $%s$ nghìn đồng/viên.\\\\
    - Mức 2 là mức vượt ngưỡng: Nếu sản xuất từ $%s$ viên trở lên, công ty phải chịu phí phạt lũy tiến. Cụ thể, tổng số tiền thuế phải đóng cho phần vượt trội $(x - %s)$ viên được tính theo công thức $T(x) = %s(x - %s) + %s(x - %s)^2$ (nghìn đồng).\\\\
    Hỏi lợi nhuận lớn nhất mà công ty đạt được là bao nhiêu triệu đồng? (Kết quả làm tròn đến hàng phần chục).'''
                         % (latex(p0), k1_str, latex(C0), latex(c1_val),
                            latex(X0), latex(t0),
                            latex(X0 + 1), latex(X0), latex(t0), latex(X0), k2_str, latex(X0)))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        x_star_str = str(Decimal(str(x_star)).quantize(Decimal('0.01'))).replace('.', ',')
        P_max_nghin_str = str(Decimal(str(P_max_nghin)).quantize(Decimal('0.1'))).replace('.', ',')
        base_tax_str = str(int(t0 * X0))

        # Nội dung lời giải chi tiết
        loigiai = ('''Hàm doanh thu của công ty khi sản xuất $x$ viên pin là:\\\\
                     $R(x) = x \\cdot p(x) = x(%s - %s x) = %s x - %s x^2$ (nghìn đồng).\\\\
                     Xét trường hợp số lượng sản xuất $x > %s$ viên pin:\\\\
                     Tổng số tiền thuế môi trường công ty phải đóng là:\\\\
                     $Tax(x) = %s \\cdot %s + T(x) = %s + %s(x - %s) + %s(x - %s)^2$\\\\
                     $= %s x + %s(x^2 - %s x + %s) = %s x^2 - %s x + %s$ (nghìn đồng).\\\\
                     Tổng chi phí sản xuất (bao gồm chi phí cơ bản và thuế) là:\\\\
                     $C_{\\text{tổng}}(x) = C(x) + Tax(x) = (%s + %s x) + (%s x^2 - %s x + %s)$\\\\
                     $= %s x^2 - %s x + %s$ (nghìn đồng).\\\\
                     Lợi nhuận của công ty thu được là:\\\\
                     $P(x) = R(x) - C_{\\text{tổng}}(x) = (%s x - %s x^2) - (%s x^2 - %s x + %s)$\\\\
                     $= -%s x^2 + %s x - %s$ (nghìn đồng).\\\\
                     Vì $P(x)$ là một hàm số bậc hai biến $x$ có hệ số của $x^2$ là $-%s < 0$, nên $P(x)$ đạt giá trị lớn nhất tại đỉnh parabol:\\\\
                     $x = \\frac{-B}{2A} = \\frac{-%s}{2 \\cdot (-%s)} = \\frac{%s}{%s} \\approx %s$ (viên).\\\\
                     Giá trị lợi nhuận lớn nhất thu được tính theo đơn vị nghìn đồng là:\\\\
                     $P_{\\max} = P(%s) \\approx %s$ (nghìn đồng).\\\\
                     Đổi sang đơn vị triệu đồng và làm tròn đến hàng phần chục, ta được:\\\\
                     $P_{\\max} \\approx %s$ triệu đồng.'''
                     % (latex(p0), k1_str, latex(p0), k1_str,
                        latex(X0),
                        latex(X0), latex(t0), base_tax_str, latex(t0), latex(X0), k2_str, latex(X0),
                        latex(t0), k2_str, latex(2 * X0), str(X0**2), a_tax_str, b_tax_abs_str, c_tax_str,
                        latex(C0), latex(c1_val), a_tax_str, b_tax_abs_str, c_tax_str,
                        a_cost_str, b_cost_abs_str, c_cost_str,
                        latex(p0), k1_str, a_cost_str, b_cost_abs_str, c_cost_str,
                        A_str, B_str, C_const_str,
                        A_str, B_str, A_str, B_str, two_A_str, x_star_str,
                        x_star_str, P_max_nghin_str,
                        kq))
    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

