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


def bt_dang8_p3_b5_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Hàm chuyển đổi số sang chuỗi hiển thị chuẩn tiếng Việt (thay dấu chấm bằng dấu phẩy)
        def fmt_num(val):
            if isinstance(val, (int, Integer)):
                return str(val)
            val_float = float(val)
            if val_float.is_integer():
                return str(int(val_float))
            s = ('%.2f' % val_float).rstrip('0').rstrip('.')
            return s.replace('.', ',')

        # Chọn tỉ số AD : DB = m : n
        ds_ti_le = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]
        m, n = choice(ds_ti_le)
        tong_mn = m + n

        # Chọn độ dài B'C' sao cho phép nhân (m / tong_mn) * bc_prime cho ra kết quả đẹp
        k_mult = choice([1, 2, 3, 4, 5, 6])
        bc_prime_val = tong_mn * k_mult

        # Tính D'E' = (m / (m + n)) * B'C'
        de_prime_val = m * k_mult

        # Làm tròn và chuẩn hóa đáp án
        number = Decimal(str(de_prime_val))
        if number == number.to_integral():
            kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        else:
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        str_m = str(m)
        str_n = str(n)
        str_tong = str(tong_mn)
        str_bc_prime = fmt_num(bc_prime_val)
        str_de_prime = fmt_num(de_prime_val)

        # Nội dung câu hỏi (chú ý: thay || bằng // trong LaTeX)
        noidungcauhoi = ('''Trong tam giác $ABC$, điểm $D \\in AB$ thỏa mãn $AD : DB = %s : %s$. Qua $D$ kẻ $DE // BC$ với $E \\in AC$. Một phép chiếu song song biến tam giác thành $A'B'C'$ và đoạn $DE$ thành $D'E'$. Biết $B'C' = %s\\text{ cm}$. Độ dài $D'E'$ (đơn vị: cm) bằng bao nhiêu?'''
                         % (str_m, str_n, str_bc_prime))

        # Nội dung lời giải (trình bày chi tiết, phân số dạng \\dfrac{}{}, thay || bằng //)
        loigiai = ('''Từ $AD : DB = %s : %s$ suy ra $AB = AD + DB$ và \\\\
                   $\\dfrac{AD}{AB} = \\dfrac{%s}{%s + %s} = \\dfrac{%s}{%s}$ \\\\
                   Vì $DE // BC$, hai tam giác $ADE$ và $ABC$ đồng dạng, nên \\\\
                   $\\dfrac{DE}{BC} = \\dfrac{AD}{AB} = \\dfrac{%s}{%s}$ \\\\
                   Qua phép chiếu song song, $DE // BC$ được biến thành $D'E' // B'C'$ và tỉ số độ dài trên hai đường thẳng song song được bảo toàn: \\\\
                   $\\dfrac{D'E'}{B'C'} = \\dfrac{DE}{BC} = \\dfrac{%s}{%s}$ \\\\
                   Với $B'C' = %s\\text{ cm}$, ta có $D'E' = \\dfrac{%s}{%s}\\cdot %s = %s\\text{ cm}$.'''
                   % (str_m, str_n,
                      str_m, str_m, str_n, str_m, str_tong,
                      str_m, str_tong,
                      str_m, str_tong,
                      str_bc_prime, str_m, str_tong, str_bc_prime, str_de_prime))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

