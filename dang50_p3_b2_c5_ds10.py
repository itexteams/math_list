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


def bt_dang50_p3_b2_c5_ds10(self):
            while True:
                # Thu hẹp dải số để tích các tổ hợp không vượt quá 9999
                # Giả sử chọn n1 câu trắc nghiệm (5-12 câu), chọn k1 (2-4 câu)
                # Chọn n2 câu tự luận (4-8 câu), chọn k2 (1-3 câu)
                n1 = randint(8, 15)
                k1 = randint(2, 4)
                n2 = randint(5, 10)
                k2 = randint(1, 3)

                # Tính toán giá trị từng phần
                val_c1 = math.comb(n1, k1)
                val_c2 = math.comb(n2, k2)
                kq_val = val_c1 * val_c2

                # Kiểm tra điều kiện: kết quả phải nhỏ hơn 9999
                if 0 < kq_val < 9999:
                    kq = int(kq_val)
                    break

            # Đáp án đúng dạng số tự nhiên
            da_d_val = '$%s$' % latex(kq)

            # Tạo các phương án sai (số tự nhiên)
            s_set = set()
            while len(s_set) < 3:
                # Các bẫy: Quy tắc cộng, dùng Chỉnh hợp, hoặc sai lệch đơn vị
                sai_cong = val_c1 + val_c2
                sai_chinh_hop = math.perm(n1, k1) + math.perm(n2, k2)
                offset = random.choice([10, 50, 100, -10, -50, 2, -2])

                # Chọn ngẫu nhiên kiểu sai
                nhieu_val = random.choice([sai_cong, sai_chinh_hop, kq + offset])

                if nhieu_val > 0 and nhieu_val != kq:
                    s_set.add('$%s$' % latex(nhieu_val))

            list_ans = ['\\True ' + da_d_val] + list(s_set)
            random.shuffle(list_ans)

            # Câu hỏi
            noidungcauhoi = ("Ngân hàng đề thi gồm $%s$ câu hỏi trắc nghiệm khác nhau và $%s$ câu hỏi tự luận khác nhau. Hỏi có thể lập được bao nhiêu đề thi sao cho mỗi đề thi gồm $%s$ câu hỏi trắc nghiệm khác nhau và $%s$ câu hỏi tự luận khác nhau?"
                             %(latex(n1), latex(n2), latex(k1), latex(k2)))

            # Nội dung lời giải chi tiết
            loigiai = ("Để lập được một đề thi theo yêu cầu, ta thực hiện qua $2$ giai đoạn: \\\\ \n"
                       "- Giai đoạn 1: Chọn $%s$ câu hỏi trắc nghiệm từ $%s$ câu hỏi có: $C_{%s}^{%s} = %s$ cách. \\\\ \n"
                       "- Giai đoạn 2: Chọn $%s$ câu hỏi tự luận từ $%s$ câu hỏi có: $C_{%s}^{%s} = %s$ cách. \\\\ \n"
                       "Theo quy tắc nhân, tổng số cách lập đề thi là: $%s \\cdot %s = %s$ (đề)."
                       %(latex(k1), latex(n1), latex(n1), latex(k1), latex(val_c1),
                         latex(k2), latex(n2), latex(n2), latex(k2), latex(val_c2),
                         latex(val_c1), latex(val_c2), latex(kq)))

            # Đáp án ngắn (Số tự nhiên)
            dapan = '\\shortans[0]{$%s$}\n' % (latex(kq))

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')

            return content

