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


def bt_dang22_p3_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # --- BƯỚC 1: RANDOM HỆ SỐ ---
                # Dạng bài: lim (sqrt(an^2 + b) - sqrt(cn + d)) / (en + f)

                # Chọn hệ số a sao cho căn bậc 2 là số nguyên (số chính phương) để đáp án đẹp
                can_a = randint(1, 5) # Căn của a = 1, 2, 3, 4, 5
                a = can_a ** 2        # a = 1, 4, 9, 16, 25
                b = randint(1, 9)     # Hằng số trong căn 1

                # Căn thứ 2: sqrt(cn+d). Hệ số n nhỏ để không ảnh hưởng giới hạn
                c = randint(1, 5)
                d = randint(1, 9)

                # Mẫu số: en + f
                e = randint(1, 4) * random.choice([-1, 1]) # Hệ số n ở mẫu (khác 0)
                f = randint(1, 9) * random.choice([-1, 1]) # Hằng số ở mẫu

                # --- BƯỚC 2: TÍNH TOÁN KẾT QUẢ ---
                # Lim = sqrt(a) / e
                kq_chinh_xac = Rational(can_a, e)
                h1=can_a/e
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq1=str(kq).replace('.', ',')

                # Xử lý hiển thị dấu cho mẫu số (để in ra 2n - 3 thay vì 2n + -3)
                dau_f = "+" if f > 0 else "-"
                tri_tuyet_doi_f = abs(f)

                # --- BƯỚC 3: TẠO ĐÁP ÁN NHIỄU (DISTRACTORS) ---
                # Tạo tập hợp các đáp án sai để tránh trùng lặp
                tap_hop_dap_an = set()
                tap_hop_dap_an.add(kq_chinh_xac)

                # Tạo các đáp án sai logic thường gặp
                ds_nhieu = []
                ds_nhieu.append(Rational(-can_a, e))          # Sai dấu
                ds_nhieu.append(Rational(can_a, e) * 2)       # Gấp đôi
                ds_nhieu.append(Rational(0, 1))               # Bằng 0
                ds_nhieu.append(Rational(1, 1))               # Bằng 1
                ds_nhieu.append(Rational(can_a + 1, e))       # Lệch tử
                ds_nhieu.append(Rational(e, can_a) if can_a!=0 else 0) # Nghịch đảo

                dap_an_sai = []
                for x in ds_nhieu:
                    if x not in tap_hop_dap_an:
                        dap_an_sai.append(x)
                        tap_hop_dap_an.add(x)
                        if len(dap_an_sai) == 3: # Chỉ cần lấy 3 đáp án sai
                            break

                # Nếu không đủ 3 đáp án sai (do trùng nhau), random thêm số ngẫu nhiên
                while len(dap_an_sai) < 3:
                    random_val = Rational(randint(-5, 5), randint(1, 3))
                    if random_val not in tap_hop_dap_an:
                        dap_an_sai.append(random_val)
                        tap_hop_dap_an.add(random_val)

                # Format đáp án về dạng LaTeX
                da = '$%s$' % latex(kq_chinh_xac)
                list_s = ['$%s$' % latex(val) for val in dap_an_sai]

                das1 = list_s[0]
                das2 = list_s[1]
                das3 = list_s[2]

                # --- BƯỚC 4: NỘI DUNG CÂU HỎI & LỜI GIẢI ---

                # Nội dung câu hỏi
                # Sử dụng kỹ thuật string formatting thủ công để đảm bảo thứ tự n^2 đứng trước
                tu_so = "\\sqrt{%sn^2 + %s} - \\sqrt{%sn + %s}" % (a, b, c, d)
                mau_so = "%sn %s %s" % (e, dau_f, tri_tuyet_doi_f)

                noidungcauhoi = ('''$\\lim_{n\\to+\\infty} \\frac{%s}{%s}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).''' % (tu_so, mau_so))

                # Nội dung lời giải
                # Xây dựng các bước giải chi tiết giống ảnh mẫu

                # Bước chia n trong căn
                tu_so_b1 = "\\sqrt{%s + \\frac{%s}{n^2}} - \\sqrt{\\frac{%s}{n} + \\frac{%s}{n^2}}" % (a, b, c, d)
                mau_so_b1 = "%s %s \\frac{%s}{n}" % (e, dau_f, tri_tuyet_doi_f)

                # Kết quả phép tính tử và mẫu
                kq_tu = "%s - 0" % (can_a)
                kq_mau = "%s" % (e)

                loigiai = ('''Ta có: \\\\
                $\\begin{aligned}
                \\lim_{n\\to+\\infty} \\frac{%s}{%s} 
                &= \\lim_{n\\to+\\infty} \\frac{%s}{%s} \\\\
                &= \\frac{%s}{%s} = %s \\approx %s.
                \\end{aligned}$''' % (tu_so, mau_so, tu_so_b1, mau_so_b1, kq_tu, kq_mau, latex(kq_chinh_xac),str(kq1)))

                # --- BƯỚC 5: XUẤT OUTPUT ---

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(str(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

