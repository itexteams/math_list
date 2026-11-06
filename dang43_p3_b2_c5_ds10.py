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


def bt_dang43_p3_b2_c5_ds10(self):
            while True:
                # Thu hẹp dải số để tích các tổ hợp không quá bùng nổ
                nm = randint(5, 12) # Số nam
                nf = randint(5, 12) # Số nữ
                kt = randint(3, 5)  # Tổng số chọn ra (chọn ít thôi để kq nhỏ)
                kf = randint(1, kt - 1) # Số nữ chọn ra (đảm bảo có cả nam và nữ)
                kn = kt - kf         # Số nam chọn ra

                # Tính toán kết quả
                # binomial(n, k) trả về số cách chọn k từ n
                cach_chon_nu = math.comb(nf, kf)
                cach_chon_nam = math.comb(nm, kn)
                kq_val = cach_chon_nu * cach_chon_nam

                # Kiểm tra điều kiện: kết quả phải nhỏ hơn 9999
                if 0 < kq_val < 9999:
                    kq = int(kq_val)
                    break

            # Bước 4: Tạo các phương án sai (số tự nhiên)
            s = set()
            while len(s) < 3:
                # Lỗi thường gặp: dùng quy tắc cộng thay vì nhân, hoặc lệch đơn vị
                sai_quy_tac_cong = cach_chon_nu + cach_chon_nam
                offset = random.choice([10, 20, 50, -10, -20, 100, -100])

                # Chọn ngẫu nhiên kiểu sai
                phuong_an_sai = random.choice([sai_quy_tac_cong, kq + offset])

                if phuong_an_sai > 0 and phuong_an_sai != kq:
                    s.add('$%s$' % latex(phuong_an_sai))

            list_sai = list(s)
            das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

            # Câu hỏi
            noidungcauhoi = ('''Một lớp có $%s$ học sinh nam và $%s$ học sinh nữ. Có bao nhiêu cách chọn $%s$ bạn học sinh sao cho trong đó có đúng $%s$ học sinh nữ?'''
                             %(latex(nm), latex(nf), latex(kt), latex(kf)))

            # Các đáp án
            da_d = ('\\True $%s$' % latex(kq))

            # Nội dung lời giải
            loigiai = ('''Số cách chọn $%s$ học sinh nữ từ $%s$ học sinh nữ là: $C_{%s}^{%s} = %s$ cách. \\\\
                         Vì cần chọn tổng cộng $%s$ học sinh nên số học sinh nam cần chọn là $%s - %s = %s$ học sinh. \\\\
                         Số cách chọn $%s$ học sinh nam từ $%s$ học sinh nam là: $C_{%s}^{%s} = %s$ cách. \\\\
                         Theo quy tắc nhân, số cách chọn $%s$ bạn thỏa mãn yêu cầu bài toán là: $%s \\cdot %s = %s$ cách.'''
                       %(latex(kf), latex(nf), latex(nf), latex(kf), latex(cach_chon_nu),
                         latex(kt), latex(kt), latex(kf), latex(kn),
                         latex(kn), latex(nm), latex(nm), latex(kn), latex(cach_chon_nam),
                         latex(kt), latex(cach_chon_nu), latex(cach_chon_nam), latex(kq)))

            # Đáp án ngắn (Số tự nhiên)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

