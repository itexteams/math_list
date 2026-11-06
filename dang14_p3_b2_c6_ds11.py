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


def bt_dang14_p3_b2_c6_ds11(self):
            # Khai báo biến
            # Khai báo biến loại câu hỏi
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # p_anh: phần trăm giỏi Tiếng Anh (từ 10% đến 25%)
                # p_toan: phần trăm giỏi Toán (từ 30% đến 50%)
                # p_cahai: phần trăm giỏi cả hai (phải nhỏ hơn p_anh và p_toan)
                p_anh = randint(10, 25)
                p_toan = randint(30, 55)
                p_cahai = randint(5, min(p_anh, p_toan) - 2)

                # Tính toán các giá trị xác suất
                pa = Decimal(p_anh) / 100
                pb = Decimal(p_toan) / 100
                pab = Decimal(p_cahai) / 100

                # Xác suất giỏi ít nhất một môn: P(A union B)
                p_union_val = pa + pb - pab

                # Xác suất không giỏi môn nào: 1 - P(A union B)
                kq_val = Decimal(1) - p_union_val

                # Định dạng kết quả (làm tròn hàng phần trăm, dùng dấu phẩy cho số thập phân)
                kq_str = str(kq_val.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')

                # Đáp án đúng
                da = '$' + kq_str + '$'

                # Bước 4: Điều chỉnh các phương án sai không trùng đáp án đúng
                s_list = []
                while len(s_list) < 3:
                    # Tạo sai số ngẫu nhiên từ -0.2 đến 0.2
                    sai_so = Decimal(randint(-20, 20)) / 100
                    val_sai = kq_val + sai_so
                    if val_sai > 0 and val_sai < 1 and val_sai != kq_val:
                        val_sai_str = '$' + str(val_sai.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',') + '$'
                        if val_sai_str not in s_list:
                            s_list.append(val_sai_str)

                das1, das2, das3 = s_list

                # Câu hỏi
                noidungcauhoi = (
                    'Tại một trường trung học phổ thông $X$, có $%s\\%%$ học sinh học giỏi môn Tiếng Anh, '
                    '$%s\\%%$ học sinh học giỏi môn Toán và $%s\\%%$ học sinh học giỏi cả hai môn Toán, Tiếng Anh. '
                    'Chọn ngẫu nhiên một học sinh từ trường $X$, xác suất để chọn được một học sinh không giỏi '
                    'môn nào trong hai môn Toán, Tiếng Anh bằng bao nhiêu? (làm tròn kết quả đến hàng phần trăm).'
                    % (latex(p_anh), latex(p_toan), latex(p_cahai))
                )

                # Các đáp án
                da_d = '\\True ' + str(da)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải (Viết chi tiết, không viết tắt, dùng \left \right)
                # Chuyển đổi dấu chấm thành dấu phẩy cho hiển thị lời giải
                pa_s = str(pa).replace('.', ',')
                pb_s = str(pb).replace('.', ',')
                pab_s = str(pab).replace('.', ',')
                pu_s = str(p_union_val).replace('.', ',')

                loigiai = (
                    'Gọi $A$ là biến cố: "Chọn được một học sinh học giỏi môn Tiếng Anh", '
                    '$B$ là biến cố: "Chọn được một học sinh học giỏi môn Toán". \\\\ '
                    'Xác suất để chọn được một học sinh giỏi Toán hoặc giỏi Anh là: \\\\ '
                    '$P\\left( A \\cup B \\right) = P\\left( A \\right) + P\\left( B \\right) - P\\left( AB \\right) = '
                    '\\frac{%s}{100} + \\frac{%s}{100} - \\frac{%s}{100} = %s$. \\\\ '
                    'Xác suất để chọn được một em học sinh không giỏi môn nào trong hai môn Toán, Tiếng Anh là: \\\\ '
                    '$P\\left( \\overline{A \\cup B} \\right) = 1 - P\\left( A \\cup B \\right) = 1 - %s = %s$.'
                    % (latex(p_anh), latex(p_toan), latex(p_cahai), pu_s, pu_s, kq_str)
                )
                dapan=' \\shortans[0]{$%s$} '%(kq_str)
            # Xuất câu trắc nghiệm (Không dùng tiền tố r, đúng cấu trúc content)
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

