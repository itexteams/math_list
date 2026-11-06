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


def bt_dang40_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- BƯỚC 1: RANDOM THÔNG SỐ BÀI TOÁN ---
            # Giá nhập một chiếc máy tính (triệu đồng)
            gia_nhap = random.randint(7, 10) 
            # Hệ số trong công thức số lượng bán (18 - x) -> (k - x)
            # Đảm bảo k > gia_nhap để có lãi
            k = gia_nhap + random.randint(8, 12) 

            # Hàm số lượng: n(x) = k - x
            # Hàm lợi nhuận trên 1 chiếc: l(x) = x - gia_nhap
            # Hàm tổng lợi nhuận: T(x) = (x - gia_nhap) * (k - x)

            noidungcauhoi = ('''Một cửa hàng bán máy tính xách tay nhập một chiếc với giá là %s triệu đồng. Cửa hàng ước tính rằng nếu chiếc máy tính được bán với giá $x$ triệu đồng thì mỗi tháng khách hàng sẽ mua $(%s-x)$ chiếc máy tính.''' 
                             %(latex(gia_nhap), latex(k)))

            ########################################################################
            # a) Tiền lãi 1 chiếc ##################################################
            lai_1_chiec_dung = '\\True Tiền lãi thu được khi bán 1 chiếc máy tính là $(x-%s)$ triệu đồng' % (latex(gia_nhap))
            lai_1_chiec_sai = 'Tiền lãi thu được khi bán 1 chiếc máy tính là $(%s-x)$ triệu đồng' % (latex(gia_nhap))

            list_a = [lai_1_chiec_dung, lai_1_chiec_sai]
            chosen_a = random.choice(list_a)
            loigiai_a = 'Tiền lãi khi bán một chiếc máy tính bằng giá bán trừ đi giá nhập: $x - %s$ (triệu đồng).' % (latex(gia_nhap))

            ########################################################################
            # b) Hàm tổng tiền lãi #################################################
            # T(x) = (x - gia_nhap)(k - x)
            ham_dung = '\\True Tiền lãi mỗi tháng là $T = (x-%s)(%s-x)$ triệu đồng' % (latex(gia_nhap), latex(k))
            ham_sai = 'Tiền lãi mỗi tháng là $T = (x-%s)(%s-x)$ triệu đồng' % (latex(gia_nhap), latex(k+gia_nhap))

            list_b = [ham_dung, ham_sai]
            chosen_b = random.choice(list_b)
            loigiai_b = 'Tổng tiền lãi mỗi tháng bằng tiền lãi một chiếc nhân với số lượng chiếc bán được: $T = (x-%s)(%s-x)$ (triệu đồng).' % (latex(gia_nhap), latex(k))

            ########################################################################
            # c) Tiền lãi tối đa ###################################################
            # T(x) = -x^2 + (k+gia_nhap)x - k*gia_nhap
            # Đỉnh Parabol tại x = (k+gia_nhap)/2. T_max = T((k+gia_nhap)/2)
            x_val = (k + gia_nhap) / 2
            t_max = (x_val - gia_nhap) * (k - x_val)

            t_max_str = latex(float(t_max)) if t_max % 1 != 0 else latex(int(t_max))
            t_max_sai = latex(int(t_max) + random.randint(2, 5))

            lai_max_dung = '\\True Tiền lãi mỗi tháng tối đa là $%s$ triệu đồng' % (t_max_str)
            lai_max_sai = 'Tiền lãi mỗi tháng tối đa là $%s$ triệu đồng' % (t_max_sai)

            list_c = [lai_max_dung, lai_max_sai]
            chosen_c = random.choice(list_c)
            loigiai_c = 'Hàm số $T(x) = -x^2 + %s x - %s$ đạt giá trị lớn nhất tại $x = %s$. Khi đó, tiền lãi tối đa là $T(%s) = %s$ triệu đồng.' % (latex(k+gia_nhap), latex(k*gia_nhap), latex(x_val), latex(x_val), t_max_str)

            ########################################################################
            # d) Số phương án khả thi (x nguyên) ###################################
            # Giải bất phương trình: (x - gia_nhap)(k - x) >= 9
            target_lai = 9
            vế_trái = (x - gia_nhap) * (k - x) - target_lai
            nghiem = solve(vế_trái, x)
            # Giả sử nghiệm thực x1, x2. Số giá trị nguyên x trong [x1, x2]
            x1 = float(min(nghiem))
            x2 = float(max(nghiem))
            so_pa_dung = 0
            for i in range(int(x1-5), int(x2+5)):
                if (i - gia_nhap)*(k - i) >= target_lai:
                    so_pa_dung += 1

            so_pa_sai = so_pa_dung + random.choice([-2, 2])
            pa_dung = '\\True Có %s phương án giá bán nguyên để tiền lãi mỗi tháng không dưới $%s$ triệu đồng' % (so_pa_dung, target_lai)
            pa_sai = 'Có %s phương án giá bán nguyên để tiền lãi mỗi tháng không dưới $%s$ triệu đồng' % (so_pa_sai, target_lai)

            list_d = [pa_dung, pa_sai]
            chosen_d = random.choice(list_d)
            loigiai_d = 'Để tiền lãi không dưới %s triệu đồng, ta có: $(x-%s)(%s-x) \\geq %s \\Leftrightarrow -x^2 + %sx - %s \\geq 0$. Giải bất phương trình ta được $x \\in [%s; %s]$. Vì $x$ nguyên nên có %s giá trị thỏa mãn.' % (target_lai, gia_nhap, k, target_lai, k+gia_nhap, k*gia_nhap + target_lai, round(x1, 2), round(x2, 2), so_pa_dung)

            # --- BƯỚC 2: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(chosen_a) + '}\n'
                '{' + str(chosen_b) + '}\n'
                '{' + str(chosen_c) + '}\n'
                '{' + str(chosen_d) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_a) + '\n'
                '\\item ' + str(loigiai_b) + '\n'
                '\\item ' + str(loigiai_c) + '\n'
                '\\item ' + str(loigiai_d) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

