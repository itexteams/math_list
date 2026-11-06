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


def bt_dang37_p3_b2_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (ở đây có 1 dạng bài xác suất)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random dữ liệu bài toán
                # n1: số sản phẩm nhà máy I, n2: số sản phẩm nhà máy II
                n1 = random.choice([100, 200, 300, 400, 500])
                n2 = random.choice([150, 250, 350, 450, 550])
                tong = n1 + n2

                # tr1, tr2: Tỉ lệ phế phẩm (%)
                tr1 = random.randint(1, 5)
                tr2 = random.randint(2, 6)
                while tr1 == tr2: # Tránh tỉ lệ giống hệt nhau để bài toán hay hơn
                    tr2 = random.randint(2, 6)

                p1 = tr1 / 100
                p2 = tr2 / 100

                # Bước 2: Tính toán theo công thức Bayes
                pb1 = n1 / tong
                pb2 = n2 / tong

                # Xác suất không là phế phẩm
                pa_b1 = 1 - p1
                pa_b2 = 1 - p2

                # Công thức Bayes: P(B2|A) = (P(B2)*P(A|B2)) / (P(B1)*P(A|B1) + P(B2)*P(A|B2))
                tu = pb2 * pa_b2
                mau = (pb1 * pa_b1) + (pb2 * pa_b2)
                kq_chinh_xac = tu / mau

                # Làm tròn đến hàng phần trăm (2 chữ số thập phân)
                kq_decimal = Decimal(str(kq_chinh_xac)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_decimal).replace('.', ',')

                # Bước 3: Tạo các đáp án sai
                sai = set()
                while len(sai) < 3:
                    lech = random.choice([-0.1, 0.1, -0.05, 0.05, 0.15, -0.15])
                    da_sai = Decimal(str(float(kq_decimal) + lech)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    da_sai_str = str(da_sai).replace('.', ',')
                    if da_sai_str != kq_str and float(da_sai) > 0 and float(da_sai) < 1:
                        sai.add('$%s$' % da_sai_str)

                list_sai = list(sai)

                # Bước 4: Nội dung câu hỏi và lời giải
                noidungcauhoi = (
                    'Một loại linh kiện do hai nhà máy I và II cùng sản xuất. Tỉ lệ phế phẩm của các nhà máy I và II lần lượt là $%s$\\%% và $%s$\\%%. Trong một lô linh kiện để lẫn lộn $%s$ sản phẩm của nhà máy I và $%s$ sản phẩm của nhà máy II. Một nhân viên kiểm tra lấy ngẫu nhiên một linh kiện từ lô hàng đó. Biết rằng linh kiện được lấy ra không là phế phẩm. Xác suất để linh kiện đó do nhà máy II sản xuất bằng bao nhiêu? (kết quả làm tròn đến hàng phần trăm).'
                    % (latex(tr1), latex(tr2), latex(n1), latex(n2))
                )

                da_d = ('\\True $%s$' % kq_str)
                list_ans = [da_d, list_sai[0], list_sai[1], list_sai[2]]
                random.shuffle(list_ans)

                # Chuyển đổi số sang dạng chuỗi có dấu phẩy cho lời giải
                pb1_s = str(round(pb1, 4)).replace('.', ',')
                pb2_s = str(round(pb2, 4)).replace('.', ',')
                pa_b1_s = str(round(pa_b1, 4)).replace('.', ',')
                pa_b2_s = str(round(pa_b2, 4)).replace('.', ',')
                tu_s = str(round(tu, 4)).replace('.', ',')
                mau_s = str(round(mau, 4)).replace('.', ',')
                kq_cx_s = str(round(kq_chinh_xac, 3)).replace('.', ',')

                loigiai = (
                    'Gọi $B_1$ là biến cố: Linh kiện lấy ra do nhà máy I sản xuất, \\\\ '
                    '$B_2$ là biến cố: Linh kiện lấy ra do nhà máy II sản xuất, \\\\ '
                    '$A$ là biến cố: Linh kiện được lấy ra không phải là phế phẩm. \\\\ '
                    'Theo bài ra, ta có: \\\\ '
                    '$P(B_1) = \\frac{%s}{%s} = %s$; $P(B_2) = \\frac{%s}{%s} = %s$; $P(A|B_1) = %s$; $P(A|B_2) = %s$. \\\\ '
                    'Áp dụng công thức xác suất Bayes, ta có: \\\\ '
                    '$P(B_2 | A) = \\frac{P(B_2).P(A|B_2)}{P(B_1).P(A|B_1) + P(B_2).P(A|B_2)} = \\frac{%s.%s}{%s.%s + %s.%s} = \\frac{%s}{%s} \\approx %s \\approx %s$.'
                    % (latex(n1), latex(tong), pb1_s, latex(n2), latex(tong), pb2_s, pa_b1_s, pa_b2_s,
                       pb2_s, pa_b2_s, pb1_s, pa_b1_s, pb2_s, pa_b2_s, tu_s, mau_s, kq_cx_s, kq_str)
                )
                dapan=' \\shortans[0]{$%s$} '%(kq_str)

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

