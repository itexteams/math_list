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


def bt_dang55_p1_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến và chọn dạng (Dạng 1: Xác suất chọn học sinh theo tổ hoặc giới tính)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # --- B3: Suy nghĩ tìm cách random bài toán ---
                # Số tổ trong lớp (từ 3 đến 5 tổ)
                n_to = random.randint(3, 5)
                # Số học sinh nam mỗi tổ (từ 3 đến 6)
                n_nam = random.randint(3, 6)
                # Số học sinh nữ mỗi tổ (từ 4 đến 7)
                n_nu = random.randint(4, 7)
                # Tổ mục tiêu (ví dụ tổ cuối cùng)
                to_muc_tieu = n_to

                # Tính toán các thông số cho lời giải
                hs_moi_to = n_nam + n_nu
                tong_hs = n_to * hs_moi_to

                # Biến cố A: "Học sinh được gọi là nam hoặc ở tổ n"
                # Cách 1: Số HS tổ n + Số HS nam ở các tổ còn lại
                nam_ngoai_to = (n_to - 1) * n_nam
                so_cach_chon = hs_moi_to + nam_ngoai_to

                # Xác suất
                xac_suat = Rational(so_cach_chon, tong_hs)

                # --- B4: Điều chỉnh các phương án sai không được trùng đáp án đúng ---
                da_dung_str = '$%s$' % latex(xac_suat)

                # Tạo danh sách các phương án nhiễu (sai)
                cac_phuong_an_sai = []

                # Nhiễu 1: Chỉ tính xác suất là nam
                sai1 = Rational(n_nam * n_to, tong_hs)
                # Nhiễu 2: Chỉ tính xác suất thuộc tổ n
                sai2 = Rational(hs_moi_to, tong_hs)
                # Nhiễu 3: Nhầm lẫn phép cộng (ví dụ: lấy tổng nam + tổng nữ / tổng - một giá trị nào đó)
                sai3 = Rational(so_cach_chon - 1, tong_hs)
                # Nhiễu 4: Đảo ngược tử mẫu hoặc giá trị ngẫu nhiên gần đó
                sai4 = Rational(so_cach_chon, tong_hs + 2)

                s_potential = [sai1, sai2, sai3, sai4]
                s_vaild = []

                for item in s_potential:
                    val_str = '$%s$' % latex(item)
                    if val_str != da_dung_str and val_str not in s_vaild:
                        s_vaild.append(val_str)

                # Nếu chưa đủ 3 đáp án sai, tạo thêm ngẫu nhiên
                while len(s_vaild) < 3:
                    fake_num = random.randint(5, tong_hs - 1)
                    fake_frac = '$%s$' % latex(Rational(fake_num, tong_hs))
                    if fake_frac != da_dung_str and fake_frac not in s_vaild:
                        s_vaild.append(fake_frac)

                das1 = s_vaild[0]
                das2 = s_vaild[1]
                das3 = s_vaild[2]

                # --- B2: Viết lại nội dung đề bài (không dùng raw string r) ---
                noidungcauhoi = ("Một lớp học có %s tổ, mỗi tổ có %s học sinh nam và %s học sinh nữ. Xác suất để giáo viên gọi được một học sinh lên bảng kiểm tra bài sao cho học sinh đó là nam hoặc ở tổ %s là"
                                 % (latex(n_to), latex(n_nam), latex(n_nu), latex(to_muc_tieu)))

                # Các đáp án
                da_d = ("\\True " + da_dung_str)
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # --- Lời giải chi tiết (không viết tắt, trình bày giống ảnh) ---
                loigiai = ("Số học sinh của lớp là $%s \\cdot %s = %s$ nên có $%s$ cách gọi một học sinh bất kỳ lên bảng. \\\\ "
                           "Có $%s$ cách gọi một học sinh ở tổ %s và có $%s$ cách gọi một học sinh nam không ở tổ %s "
                           "nên có tất cả $%s + %s = %s$ cách gọi một học sinh lên bảng sao cho học sinh đó là nam hoặc ở tổ %s. \\\\ "
                           "Vậy xác suất cần tìm là $P = \\frac{%s}{%s} = %s$."
                           % (latex(hs_moi_to), latex(n_to), latex(tong_hs), latex(tong_hs),
                              latex(hs_moi_to), latex(to_muc_tieu), latex(nam_ngoai_to), latex(to_muc_tieu),
                              latex(hs_moi_to), latex(nam_ngoai_to), latex(so_cach_chon), latex(to_muc_tieu),
                              latex(so_cach_chon), latex(tong_hs), latex(xac_suat)))

            # --- Xuất nội dung theo cấu trúc mẫu ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_1[0]) + '}\n'
                       '{' + str(list_1[1]) + '}\n'
                       '{' + str(list_1[2]) + '}\n'
                       '{' + str(list_1[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content 

