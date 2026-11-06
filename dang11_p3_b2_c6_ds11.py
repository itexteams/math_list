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


def bt_dang11_p3_b2_c6_ds11(self):
            # Khai báo biến
            # Đảm bảo điều kiện: n(A) + n(B) - n(A giao B) <= Tổng số hộ
            tong_ho = random.randint(40, 80)
            nuoi_cho = random.randint(15, tong_ho // 2)
            nuoi_meo = random.randint(12, tong_ho // 2)
            ca_hai = random.randint(4, min(nuoi_cho, nuoi_meo) - 2)

            # Tính toán các giá trị xác suất
            # n(A hợp B) = n(A) + n(B) - n(A giao B)
            tu_so_hop = nuoi_cho + nuoi_meo - ca_hai
            xac_suat_chinh_xac = tu_so_hop / tong_ho

            # Làm tròn đến hàng phần trăm theo quy tắc ROUND_HALF_UP
            kq_decimal = Decimal(str(xac_suat_chinh_xac)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            da_dung = str(kq_decimal).replace('.', ',')

            # B4: Tạo các phương án sai không trùng với đáp án đúng
            s = []
            while len(s) < 3:
                sai_lech = random.choice([-0.12, -0.08, -0.05, 0.05, 0.07, 0.11, 0.15])
                kq_sai = kq_decimal + Decimal(str(sai_lech))
                # Đảm bảo xác suất dương và không trùng
                if kq_sai > 0 and kq_sai < 1:
                    sai_str = str(kq_sai.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
                    if sai_str != da_dung and sai_str not in s:
                        s.append('$%s$' % sai_str)

            # Thiết lập nội dung câu hỏi
            noidungcauhoi = (
                'Một khu phố có $%s$ hộ gia đình trong đó có $%s$ hộ nuôi chó, $%s$ hộ nuôi mèo và $%s$ hộ nuôi cả chó và mèo. '
                'Chọn ngẫu nhiên một hộ trong khu phố trên, xác suất để hộ đó nuôi chó hoặc nuôi mèo bằng bao nhiêu? '
                '(làm tròn kết quả đến hàng phần trăm).'
                % (latex(tong_ho), latex(nuoi_cho), latex(nuoi_meo), latex(ca_hai))
            )

            # Thiết lập lời giải chi tiết (B2: Viết lại y hệt logic trong ảnh)
            # Rút gọn các phân số để trình bày giống mẫu
            pA_tu = Rational(nuoi_cho, tong_ho)
            pB_tu = Rational(nuoi_meo, tong_ho)
            pAB_tu = Rational(ca_hai, tong_ho)

            loigiai = (
                'Gọi các biến cố $A$: "Chọn được hộ nuôi chó", và $B$: "Chọn được hộ nuôi mèo".\\\\ '
                'Ta có: $P\\left(A\\right) = \\frac{%s}{%s} = %s, P\\left(B\\right) = \\frac{%s}{%s} = %s, P\\left(AB\\right) = \\frac{%s}{%s}$.\\\\ '
                'Xác suất để chọn được hộ nuôi chó hoặc nuôi mèo là:\\\\ '
                '$P\\left(A \\cup B\\right) = P\\left(A\\right) + P\\left(B\\right) - P\\left(AB\\right) = %s + %s - \\frac{%s}{%s} = \\frac{%s}{%s} \\approx %s$.'
                % (
                    latex(nuoi_cho), latex(tong_ho), latex(pA_tu),
                    latex(nuoi_meo), latex(tong_ho), latex(pB_tu),
                    latex(ca_hai), latex(tong_ho),
                    latex(pA_tu), latex(pB_tu), latex(ca_hai), latex(tong_ho),
                    latex(tu_so_hop), latex(tong_ho), da_dung
                )
            )
            dapan=' \\shortans[0]{$%s$} '%(da_dung)
            # Trộn đáp án
            da_d = '\\True $%s$' % da_dung
            list_1 = [da_d, s[0], s[1], s[2]]
            random.shuffle(list_1)

            # Xuất nội dung theo cấu trúc mẫu
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

