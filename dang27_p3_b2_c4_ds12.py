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


def bt_dang27_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Giữ k1=2 và k2=3 như mẫu để đảm bảo tính logic của lời giải chi tiết
            nx = random.randint(8, 12)  # Số viên bi xanh (mẫu là 10)
            nd = random.randint(5, 8)   # Số viên bi đỏ (mẫu là 5)
            k1 = 2  # Số bi Bình lấy nếu An lấy bi xanh
            k2 = 3  # Số bi Bình lấy nếu An lấy bi đỏ

            tong = nx + nd
            # Xác suất An lấy bi
            pa = Rational(nx, tong)
            pa_bar = Rational(nd, tong)

            # Tính xác suất có điều kiện P(B|A)
            # An lấy 1 xanh (đã có màu xanh), Bình lấy k1 viên. 
            # Để có đủ 2 màu thì Bình phải lấy ít nhất 1 viên đỏ.
            c_total_a = binomial(tong - 1, k1)
            c_only_blue_a = binomial(nx - 1, k1)
            pb_a = Rational(c_total_a - c_only_blue_a, c_total_a)

            # Tính xác suất có điều kiện P(B|A_bar)
            # An lấy 1 đỏ (đã có màu đỏ), Bình lấy k2 viên.
            # Để có đủ 2 màu thì Bình phải lấy ít nhất 1 viên xanh.
            c_total_abar = binomial(tong - 1, k2)
            c_only_red_abar = binomial(nd - 1, k2)
            pb_abar = Rational(c_total_abar - c_only_red_abar, c_total_abar)

            # Áp dụng công thức Bayes
            tu = pa * pb_a
            mau = pa * pb_a + pa_bar * pb_abar
            kq_rational = tu / mau
            kq_float = float(kq_rational)
            kq_decimal = Decimal(str(kq_float)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            kq_str = str(kq_decimal).replace('.', ',')

            # Bước 4: Tạo các phương án sai không trùng đáp án đúng
            wrong_answers = set()
            while len(wrong_answers) < 3:
                # Tạo độ lệch ngẫu nhiên
                offset = random.choice([-0.12, -0.08, -0.05, 0.05, 0.07, 0.11, 0.15])
                wa_val = max(0.01, min(0.99, kq_float + offset))
                wa_dec = Decimal(str(wa_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                wa_str = str(wa_dec).replace('.', ',')
                if wa_str != kq_str:
                    wrong_answers.add(wa_str)

            list_ans_val = list(wrong_answers)
            da_d = '\\True ' + '$' + kq_str + '$'
            da_s1 = '$' + list_ans_val[0] + '$'
            da_s2 = '$' + list_ans_val[1] + '$'
            da_s3 = '$' + list_ans_val[2] + '$'

            list_final = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_final)

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Một hộp chứa %s viên bi xanh và %s viên bi đỏ. Bạn An lấy ra ngẫu nhiên 1 viên bi từ hộp, '
                'xem màu, rồi bỏ ra ngoài. Nếu viên bi An lấy ra có màu xanh, bạn Bình sẽ lấy ra ngẫu nhiên %s viên bi từ hộp; '
                'còn nếu viên bi An lấy ra có màu đỏ, bạn Bình sẽ lấy ra ngẫu nhiên %s viên bi từ hộp. '
                'Xác suất để An lấy được viên bi màu xanh, biết rằng tất cả các viên bi được hai bạn chọn ra đều có đủ cả hai màu bằng bao nhiêu? '
                '(làm tròn kết quả đến hàng phần trăm).'
                % (latex(nx), latex(nd), latex(k1), latex(k2))
            )

            # Nội dung lời giải chi tiết
            loigiai = (
                'Gọi $A$ là biến cố: An lấy ra viên bi màu xanh. \\\\ '
                'Khi đó $\\{A, \\bar{A}\\}$ là một hệ đầy đủ các biến cố với $P(A) = \\frac{%s}{%s} = %s$; $P(\\bar{A}) = \\frac{%s}{%s} = %s$. \\\\ '
                'Gọi $B$ là biến cố: Tất cả các viên bi được hai bạn chọn ra đều có đủ cả hai màu. \\\\ '
                'Ta có $P(B|A)$ là xác suất %s viên bi Bình lấy ra có ít nhất một viên bi màu đỏ (vì An đã lấy 1 viên xanh), do đó: \\\\ '
                '$P(B|A) = \\frac{C_{%s}^{%s} - C_{%s}^{%s}}{C_{%s}^{%s}} = %s$. \\\\ '
                'Tương tự $P(B|\\bar{A})$ là xác suất %s viên bi Bình lấy ra có ít nhất một viên bi màu xanh (vì An đã lấy 1 viên đỏ), do đó: \\\\ '
                '$P(B|\\bar{A}) = \\frac{C_{%s}^{%s} - C_{%s}^{%s}}{C_{%s}^{%s}} = %s$. \\\\ '
                'Áp dụng công thức xác suất Bayes, ta có: \\\\ '
                '$P(A|B) = \\frac{P(A).P(B|A)}{P(A).P(B|A) + P(\\bar{A}).P(B|\\bar{A})} = \\frac{%s \\cdot %s}{%s \\cdot %s + %s \\cdot %s} \\approx %s$.'
                % (latex(nx), latex(tong), latex(pa), latex(nd), latex(tong), latex(pa_bar),
                   latex(k1), latex(tong-1), latex(k1), latex(nx-1), latex(k1), latex(tong-1), latex(k1), latex(pb_a),
                   latex(k2), latex(tong-1), latex(k2), latex(nd-1), latex(k2), latex(tong-1), latex(k2), latex(pb_abar),
                   latex(pa), latex(pb_a), latex(pa), latex(pb_a), latex(pa_bar), latex(pb_abar), kq_str)
            )
            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(kq_str)

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

